import base64

import bbdcommon.pybus.service_bus as sb
from bbdcommon.pybus.common_types import SagaBase
from bbdcommon.pybus.handler_register_functions import (
    HandleFuncRegister,
    HandleRegister,
)
from bbdcontent.common.api.upload_content.v2 import ContentType
from bbdcontent.common.api.upload_content.v2 import upload_cs_db_content

from sataxi.contentstore.messaging.commands.upload_content import UploadContentV1


@HandleRegister()
class EventSaga(SagaBase):
    def __init__(self, bus: sb.KombuBus = None):
        super(EventSaga, self).__init__(bus)
        self.session = self.bus_ref.db_registry["ContentDB"].get_session()

    @HandleFuncRegister(UploadContentV1)
    def upload_content_handler(self, msg: UploadContentV1):
        try:
            self.logger.debug("Upload Content Message Received.")
            content_byte_data: bytes = base64.b64decode(msg.content_data, validate=True)
            upload_cs_db_content(
                session=self.session,
                content_type=ContentType(msg.content_type),
                source_type=msg.source_type,
                source_id=msg.source_id,
                user_specified_key=msg.user_specified_key,
                file={
                    "filename": msg.file_name,
                    "content_type": msg.mime_type,
                    "body": content_byte_data,
                },
                user=msg.user,
                encryption_password=msg.encryption_password,
            )
            self.session.commit()
            self.logger.debug("Upload Completed!")
        except Exception as exception:
            self.logger.exception(exception)
            self.logger.error(f"Unable to process upload message for {msg.user_specified_key}.")

        finally:
            self.session.close()
