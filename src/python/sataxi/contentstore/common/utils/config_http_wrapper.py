import logging

from marshmallow_dataclass import class_schema
from tornado.web import HTTPError

from sataxi.contentstore.common.schemas.mobaylz_document_schema import (
    MobalyzDocumentResponse,
    MobalyzDocumentTemplate,
)
from sataxi.contentstore.common.utils.http_wrapper import HttpWrapper

logger = logging.getLogger(__name__)


class ConfigHttpWrapper(HttpWrapper):
    def __init__(self):
        super().__init__({"content-type": "application/json"})

    async def generate_mobalyz_doc(
        self, url: str, document_template: MobalyzDocumentTemplate
    ) -> MobalyzDocumentResponse:
        payload = class_schema(MobalyzDocumentTemplate)().dumps(document_template)
        logger.info(f"Sending request to {url} with body: {document_template}")
        try:
            response = (await self.send_http_request("POST", url, payload, 30)).decode(
                "utf-8"
            )
            logger.info(f"Received response from: {url} with body: {response}")
            save_response: MobalyzDocumentResponse = class_schema(
                MobalyzDocumentResponse
            )().loads(response)
            return save_response
        except HTTPError as http_error:
            logger.error(
                f"Received exception from {url} "
                f"with code {http_error.status_code}, "
                f"and messsage: {http_error.log_message}"
            )
            raise http_error
