import base64
import csv
import io
import json
import logging
import os
import uuid
from datetime import datetime

import pandas as pd
import pdfkit

from bbdcommon.spechelpers.misc import schema_field
from smb.SMBConnection import SMBConnection
from smb.base import SMBTimeout
from smb.smb_structs import OperationFailure
from tornado.httpclient import HTTPError

from bbdcontent.common.api.correspondence import (
    get_correspondence_template_and_template_out,
)
from bbdcontent.common.api.get_content.v2 import (
    get_content_info_by_content_store_uri,
    get_content,
)
from bbdcontent.common.api.upload_content.v2 import upload_cs_db_content
from bbdcontent.common.schemas.content import ContentType

from sataxi.contentstore.common.schemas.csv_schema import CSVRequest, CSVResponse
from sataxi.contentstore.common.schemas.doc_data_schema import HiveDocDataRequest
from sataxi.contentstore.common.schemas.document_template import (
    DocumentTemplate,
    DocumentTemplateResponse,
)
from sataxi.contentstore.common.schemas.shared_location_store_schema import (
    SharedLocationConfig,
)
from sataxi.contentstore.db.sqlalchemy.sataxi.contentstore import (
    DB_DocDataInsert,
    DB_VG_Validation_LoanSelectLoanDetails,
    DB_VG_Validation_LoanSelectAccountByAccountNumber,
)
from sataxi.contentstore.messaging.commands.attach_document import AttachDocumentV1

output_path = os.path.abspath(
    os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__))))
)


class AcquireConfigs:
    server_username: str = schema_field(data_key="Username")
    server_password: str = schema_field(data_key="Password")
    server_name: str = schema_field(data_key="ServerName")
    path: str = schema_field(data_key="SharedPath")


async def generate_document_template(self, document_template: DocumentTemplate):
    try:
        pdf_path = output_path + f"/{document_template.template_identifier}.pdf"
        sataxi_logo = open(output_path + "/configs/sataxi-logo-dark.png", "rb")
        signature = open(output_path + "/configs/signature.png", "rb")
        document_template.template_parameters.update(
            {
                "SATAXI_LOGO": f'data:image/png;base64,{base64.b64encode(sataxi_logo.read()).decode("utf-8")}',
                "SIGNATURE": f'data:image/png;base64,{base64.b64encode(signature.read()).decode("utf-8")}',
            }
        )
        sataxi_logo.close()
        template = get_correspondence_template_and_template_out(
            self.session,
            document_template.template_identifier,
            document_template.template_version,
            document_template.template_parameters,
            "DOCUMENT",
        )
        config = pdfkit.configuration(wkhtmltopdf=os.environ.get("WKHTMLTOPDF_PATH"))
        pdfkit.from_string(
            template.template, pdf_path, verbose=True, configuration=config
        )
        pdf_datafile = open(pdf_path, "rb")
        pdf_data = pdf_datafile.read()
        pdf_datafile.close()
        guid = str(uuid.uuid4())
        file_name = f"{document_template.template_identifier}_{datetime.now().strftime('%Y%m%d%H%M%S')}.pdf"
        config = self.application.server_base.config.get("SharedLocationConfig")
        shared_location_config = SharedLocationConfig(
            username=config.get("Username"),
            password=config.get("Password"),
            server_local_name=config.get("ServerLocalName"),
            shared_volume=config.get("SharedVolume"),
            server_name=config.get("ServerName"),
            system_id=config.get("SystemID"),
            server_url=config.get("ServerURL"),
        )
        loan_accounts = DB_VG_Validation_LoanSelectAccountByAccountNumber.execute(
            self.sessions["HiveRepository"], document_template.account_number
        )
        loan_details = DB_VG_Validation_LoanSelectLoanDetails.execute(
            self.sessions["HiveRepository"], document_template.account_number
        )

        hive_docdata_request = HiveDocDataRequest(
            account_number=document_template.account_number,
            chassis_number=loan_details[0].ChassisNumber,
            customer_id_number=loan_accounts[0].IDNo,
            doc_description=f"{document_template.template_identifier} generated via Vanguard",
            engine_number=loan_details[0].EngineNumber,
            file_name=file_name,
            process=document_template.template_identifier,
            reg_number=str(loan_details[0].RegistrationNumber),
            store_shared_location=True,
            upload_by=self.current_user,
            user_specified_key=f"USERSPECIFIEDKEY={guid}",
            doc_data=pdf_data,
        )
        hive_docdata_insert(self, hive_docdata_request, shared_location_config)

        upload_cs_db_content(
            session=self.session,
            content_type=ContentType.STRING,
            source_type=1,
            source_id="Vanguard",
            user_specified_key=guid,
            file={
                "filename": file_name,
                "content_type": "application/pdf",
                "body": pdf_data,
            },
            user=self.current_user,
            encryption_password=document_template.encryption_password,
        )
        self.session.commit()

        attach_document = AttachDocumentV1(
            document_template.case_number, self.current_user, file_name, guid
        )
        self.application.server_base.node.bus.send(
            msg_obj=attach_document, reply_node_id=None
        )
        self.application.server_base.node.bus.commit_messaging()
        self.application.server_base.node.bus.emit_prompts()
        self.application.server_base.node.bus.reset_state()
        return DocumentTemplateResponse(
            payload=base64.b64encode(pdf_data),
            case_number=document_template.case_number,
            guid=guid,
        )
    except OSError as e:
        logging.error("Unable to Generate Document")
        logging.error(f"Error: {e}")
    finally:
        os.remove(pdf_path)


def generate_csv(self, csv_request: CSVRequest):
    guid = str(uuid.uuid4())
    file_name = f"/{csv_request.file_name}.csv"
    csv_path = "".join([output_path, file_name])
    date_time = datetime.now().strftime("%Y_%m_%d_%H%M%S")

    with open(csv_path, "w", newline="", encoding="utf_8") as file:
        for data in csv_request.json_data:
            columns = pd.DataFrame(data.column_names)
            rows = pd.DataFrame(data.data)
            if columns.shape[0] < rows.shape[1]:
                raise ValueError(
                    "CSV shape does not match! There are more data columns than there are column names."
                )
            writer = csv.writer(file, delimiter=csv_request.delimiter)
            writer.writerow(data.column_names)
            for row in data.data:
                writer.writerow(row)
            writer.writerow("")

    with open(csv_path, "rb") as csv_datafile:
        csv_data = csv_datafile.read()
        csv_datafile.close()

    upload_cs_db_content(
        session=self.session,
        content_type=ContentType.STRING,
        source_type=1,
        source_id="Vanguard",
        user_specified_key=guid,
        file={
            "filename": "".join([csv_request.file_name, "_", date_time]),
            "content_type": "application/csv",
            "body": csv_data,
        },
        user=self.current_user,
        encryption_password=None,
    )

    self.session.commit()
    os.remove(csv_path)
    return CSVResponse(payload=base64.b64encode(csv_data), guid=guid)


def hive_docdata_insert(
    self,
    hive_doc_data_request: HiveDocDataRequest,
    shared_location_config: SharedLocationConfig,
):
    try:
        session = self.sessions["ContentDB"]
        # content_data (bytes)
        if not hive_doc_data_request.doc_data:
            content_info = get_content_info_by_content_store_uri(
                session, hive_doc_data_request.user_specified_key
            )
            hive_doc_data_request.doc_data = get_content(
                session, content_info.content_link_id
            )

        if hive_doc_data_request.store_shared_location:
            logging.debug("Saving To Shared Location")
            shared_location_store(
                shared_location_config,
                hive_doc_data_request.account_number,
                hive_doc_data_request.file_name,
                hive_doc_data_request.doc_data,
            )

        session = self.sessions["HiveRepository"]
        doc_path = "".join(
            [
                "\\\\",
                shared_location_config.server_url.split(".")[0],
                "/",
                shared_location_config.shared_volume,
                "/",
                hive_doc_data_request.account_number.replace(":", "_"),
                "/",
                hive_doc_data_request.file_name,
            ]
        )
        logging.debug("Inserting Document Record into Hive")
        DB_DocDataInsert.execute(
            session=session,
            SystemId=int(shared_location_config.system_id),
            ViewName=hive_doc_data_request.view_name,
            AccountNumber=hive_doc_data_request.account_number,
            ChassisNumber=hive_doc_data_request.chassis_number,
            EngineNumber=hive_doc_data_request.engine_number,
            RegistrationNumber=hive_doc_data_request.reg_number,
            DocPath=doc_path,
            Process=hive_doc_data_request.process,
            UploadDate=datetime.now(),
            UploadBy=hive_doc_data_request.upload_by,
            CustomerIDNumber=hive_doc_data_request.customer_id_number,
        )
        session.commit()
    except HTTPError as e:
        raise HTTPError(
            code=e.code,
            message=json.loads(e.response.body.decode("utf-8"))["results"]["error"],
        )


def shared_location_store(
    shared_location_config: SharedLocationConfig,
    account_number: str,
    file_name: str,
    file_data: bytes,
):
    # Extract configuration values
    username = shared_location_config.username
    password = shared_location_config.password
    server_local_name = shared_location_config.server_local_name

    server_shared_volume = shared_location_config.shared_volume
    server_url = shared_location_config.server_url
    server_name = shared_location_config.server_name

    base_folder = account_number.replace(":", "_")
    file_path = os.path.join(base_folder, file_name)

    # Create an SMBConnection object
    conn = SMBConnection(
        username,
        password,
        server_local_name,
        server_name,
        use_ntlm_v2=True,
        is_direct_tcp=True,
    )
    try:
        # Establish the connection
        if not conn.connect(server_url, 445):
            raise SMBTimeout("Failed to connect to the server.")
        logging.info("Connection to SMB server succeeded.")

        # Check if directory exists, create if it doesn't
        try:
            conn.listPath(server_shared_volume, base_folder)
            logging.info("Directory already exists.")
        except OperationFailure:
            conn.createDirectory(server_shared_volume, base_folder)
            logging.info("Directory created.")

        # Check if file exists, store if it doesn't
        try:
            conn.getAttributes(server_shared_volume, file_path)
            logging.info("File already exists.")
        except OperationFailure:
            file_object = io.BytesIO(file_data)
            conn.storeFile(server_shared_volume, file_path, file_object)
            logging.info("File written successfully.")
    except SMBTimeout as exception:
        logging.error(exception)
        raise Exception(exception)
    except OperationFailure as e:
        logging.error(f"Error: {e}")
        raise Exception(e)
    finally:
        # Close the connection
        conn.close()
