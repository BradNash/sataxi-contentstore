import os
import tempfile
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Dict

from bbdcommon.config.common import handle_config, parse_config, _DummyConfigParser
from sqlalchemy.orm import Session

from sataxi.contentstore.common.document_service import hive_docdata_insert
from sataxi.contentstore.common.schemas.doc_data_schema import HiveDocDataRequest
from sataxi.contentstore.common.schemas.shared_location_store_schema import (
    SharedLocationConfig,
)
from sataxi.contentstore.db.sqlalchemy.sataxi.contentstore import (
    DB_VG_Validation_LoanSelectLoanDetails,
)
from sataxi.contentstore.messaging.commands.send_correspondence import (
    SendEmailCorrespondenceV1,
)
from smb.SMBConnection import SMBConnection
from smb.base import SMBTimeout

import bbdcommon.pybus.service_bus as sb
from bbdcommon.pybus.common_types import SagaBase
from bbdcommon.pybus.handler_register_functions import (
    HandleFuncRegister,
    HandleRegister,
)
from bbdcontent.common.api.upload_content.v2 import upload_cs_db_content
from bbdcontent.common.schemas.content import ContentType
from sataxi.finance.messaging.events.statement_generated import StatementGeneratedV1


@dataclass
class EmailIdentifier(Enum):
    EARLY_SETTLEMENT = "EARLY_SETTLEMENT_QUOTATION"
    DEAL_TAKEOVER_GENERIC = "DEAL_TAKEOVER_GENERIC_SETTLEMENT_QUOTATION"
    DEAL_TAKEOVER_DECEASED = "DEAL_TAKEOVER_DECEASED_SETTLEMENT_QUOTATION"
    INSURANCE_CLAIM = "INSURANCE_SETTLEMENT_QUOTATION"
    STATEMENT = "ACCOUNT_STATEMENT"


@HandleRegister()
class EventSaga(SagaBase):
    def __init__(self, bus: sb.KombuBus = None):
        super(EventSaga, self).__init__(bus)
        self.sessions: Dict[str, Session] = {
            "ContentDB": self.bus_ref.db_registry["ContentDB"].get_session(),
            "HiveRepository": self.bus_ref.db_registry["HiveRepository"].get_session(),
        }

    def load_config_file(self, arg_parser_add_func=None):
        self.args = handle_config(None, arg_parser_add_func)
        config_dict = parse_config(
            os.getcwd(), self.args, config_type=_DummyConfigParser
        )
        return config_dict

    @HandleFuncRegister(StatementGeneratedV1)
    def process_generated_statement_event(self, statement_event: StatementGeneratedV1):
        try:
            self.logger.debug(
                f"Statement Event Message Received for Case {statement_event.case_number}"
            )
            config = self.load_config_file().get("SharedLocationConfig")
            shared_location_config = SharedLocationConfig(
                username=config.get("Username"),
                password=config.get("Password"),
                server_local_name=config.get("ServerLocalName"),
                shared_volume=config.get("SharedVolume"),
                server_name=config.get("ServerName"),
                system_id=config.get("SystemID"),
                server_url=config.get("ServerURL"),
            )
            with tempfile.NamedTemporaryFile() as file_obj:
                con: SMBConnection = self.smb_connection_steup(shared_location_config)
                con.retrieveFile("Storage", statement_event.file_name, file_obj)
                file_obj.seek(0)
                data = file_obj.read()

            upload_cs_db_content(
                session=self.sessions["ContentDB"],
                content_type=ContentType.STRING,
                source_type=1,
                source_id="StatementGeneratedV1",
                user_specified_key=statement_event.guid,
                file={
                    "filename": statement_event.file_name.rpartition("\\")[-1],
                    "content_type": "application/pdf",
                    "body": data,
                },
                user=statement_event.username,
                encryption_password=statement_event.encryption_password,
            )
            self.sessions["ContentDB"].commit()
            self.logger.debug(
                f"Upload Completed ({datetime.now()}): Case Number {statement_event.case_number}"
            )

            self.logger.debug("Saving Document to Shared Location & Hive")
            loan_details = DB_VG_Validation_LoanSelectLoanDetails.execute(
                self.sessions["HiveRepository"], statement_event.account_number
            )
            hive_docdata_request = HiveDocDataRequest(
                account_number=statement_event.account_number,
                chassis_number=loan_details[0].ChassisNumber,
                customer_id_number=statement_event.id_number,
                doc_description=f"{statement_event.document_type} generated via acquire",
                engine_number=loan_details[0].EngineNumber,
                file_name=statement_event.file_name.split("\\", 1)[1],
                process=statement_event.document_type,
                reg_number=str(loan_details[0].RegistrationNumber),
                store_shared_location=False,
                upload_by=statement_event.username,
                user_specified_key=f"USERSPECIFIEDKEY={statement_event.guid}",
                doc_data=None,
            )
            hive_docdata_insert(self, hive_docdata_request, shared_location_config)

            receivers_list = statement_event.customer_email.split(",")
            self.logger.debug("Sending Email....")
            send_email_command = SendEmailCorrespondenceV1(
                receivers=receivers_list,
                agent=statement_event.username,
                body={
                    "ACCOUNT_NUMBER": statement_event.account_number,
                    "CLIENT_NAME": statement_event.customer_name,
                },
                template_identifier=EmailIdentifier[
                    statement_event.document_type
                ].value,
                template_version=None,
                user_specified_keys=[f"cs://USERSPECIFIEDKEY={statement_event.guid}"],
                send_as_async=False,
            )
            self.bus_ref.send(msg_obj=send_email_command, reply_node_id=None)
            self.bus_ref.commit_messaging()
            self.bus_ref.emit_prompts()
            self.bus_ref.reset_state()
            self.logger.debug(
                f"Handler ({datetime.now()}): Case Number {statement_event.case_number}"
            )
        except Exception as exception:
            self.logger.exception(exception)

    def smb_connection_steup(
        self, shared_location_config: SharedLocationConfig
    ) -> SMBConnection:
        attempts = 0
        while True:
            attempts += 1
            self.logger.info("Connecting to SMB SERVER...")
            try:
                con = SMBConnection(
                    shared_location_config.username,
                    shared_location_config.password,
                    "Vanguard",
                    shared_location_config.server_name,
                    use_ntlm_v2=True,
                    is_direct_tcp=True,
                )
                con.connect(shared_location_config.server_url, 445)
                self.logger.info("Connection to SMB SERVER Succeeded.")
                return con
            except SMBTimeout as exception:
                self.logger.info("Failed to connect to SMB Server, retrying...")
                if attempts == 3:
                    raise self.logger.exception(
                        f"Failed to connect to SMB Server, "
                        f"retried 3 times. Reason: {exception}"
                    )
