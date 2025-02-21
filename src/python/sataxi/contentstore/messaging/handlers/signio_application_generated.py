import os

import pandas as pd
from sataxi.contentstore.messaging.commands.send_correspondence import (
    SendEmailCorrespondenceV1,
)

import bbdcommon.pybus.service_bus as sb
from bbdcommon.pybus.common_types import SagaBase
from bbdcommon.pybus.handler_register_functions import (
    HandleFuncRegister,
    HandleRegister,
)
from bbdcontent.common.api.upload_content.v2 import upload_cs_db_content
from bbdcontent.common.schemas.content import ContentType
from sataxi.finance.messaging.events.sigino_application import (
    SignioApplicationGeneratedV1,
)


@HandleRegister()
class EventSaga(SagaBase):
    def __init__(self, bus: sb.KombuBus = None):
        super(EventSaga, self).__init__(bus)
        self.session = self.bus_ref.db_registry["ContentDB"].get_session()

    @HandleFuncRegister(SignioApplicationGeneratedV1)
    def upload_content_handler(self, msg: SignioApplicationGeneratedV1):
        try:
            self.logger.debug("Upload Content Message Received.")
            path = os.path.join(
                os.path.dirname(__file__),
                f"sig_application_{msg.user_specified_key}.xlsx",
            )
            writer = pd.ExcelWriter(
                path,
                engine="xlsxwriter",
                options={"numbers_to_strings": True, "strings_to_formulas": False},
            )

            include_list = [
                "caseNumber",
                "campaign",
                "bankingDetails",
                "eApplication",
                "employerDetails",
                "financeDetails",
                "personalDetails",
                "relativeDetails",
                "saTaxiInsurance",
                "vehicleDetails",
                "saTaxiRoute",
            ]
            for key, value in msg.signio_application_data.items():
                if key in include_list:
                    data_frame = pd.DataFrame([value], index=["DATA"])
                    data_frame.to_excel(writer, sheet_name=key, index=False)
            writer.save()
            writer.close()

            with open(file=path, mode="rb") as signio_application_excel:
                upload_cs_db_content(
                    session=self.session,
                    content_type=ContentType(msg.content_type),
                    source_type=msg.source_type,
                    source_id=msg.source_id,
                    user_specified_key=msg.user_specified_key,
                    file={
                        "filename": msg.file_name,
                        "content_type": msg.mime_type,
                        "body": signio_application_excel.read(),
                    },
                    user=msg.user,
                    encryption_password=msg.encryption_password,
                )
            self.logger.debug("Upload Completed!")
            self.session.commit()
            signio_application_excel.close()
            os.remove(path)

            send_email_command = SendEmailCorrespondenceV1(
                receivers=[
                    "smothiba@sataxi.co.za",
                    "ntmthembu@sataxi.co.za",
                    "sdube@sataxi.co.za",
                    "mmonyamane@sataxi.co.za",
                    "mrooi@sataxi.co.za",
                ],
                # receivers=["bradleyp@bbd.co.za"],
                agent=msg.user,
                body={
                    "MESSAGE_BODY": f"Please see attached the Signio application for the ID Number - "
                    f"{msg.signio_application_data['eApplication']['customerIdNumber']}.",
                    "SUBJECT": f"SIGNIO APPLICATION LEAD -  "
                    f"{msg.signio_application_data['eApplication']['customerIdNumber']}",
                },
                template_identifier="GENERIC_EMAIL",
                template_version=None,
                user_specified_keys=[f"cs://USERSPECIFIEDKEY={msg.user_specified_key}"],
                send_as_async=True,
            )
            self.bus_ref.send(msg_obj=send_email_command, reply_node_id=None)
            self.bus_ref.commit_messaging()
            self.bus_ref.emit_prompts()
            self.bus_ref.reset_state()
        except Exception as exception:
            self.logger.exception(exception)
