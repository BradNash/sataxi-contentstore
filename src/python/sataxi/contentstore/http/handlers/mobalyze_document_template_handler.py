from bbdcommon.spechelpers.funcs import api_description, api_tag
from bbdcommon.spechelpers.misc import api_response, api_request, api_validate
from bbdcommon.tornadohelpers.base.authorization import authorized
from bbdcommon.tornadohelpers.base.db_handler import DBHandlerBase
from bbdcommon.tornadohelpers.base.schemas import FailedResponseSchema
from marshmallow_dataclass import class_schema

from sataxi.contentstore.common.mobalyz_service import (
    generate_mobalyz_document_template,
)
from sataxi.contentstore.common.schemas.mobaylz_document_schema import (
    MobalyzDocumentTemplate,
    MobalyzDocumentTemplateResponse,
)


class MobalyzDocumentHandlerV1(DBHandlerBase):
    @api_description("Generate Document Mobalyz Document API")
    @api_tag("Document Templates")
    @api_request(None, "Document Template requests", MobalyzDocumentTemplate)
    @api_response(
        None, 200, "Document Templates", MobalyzDocumentTemplateResponse, many=False
    )
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, 500, "Generic Failure", FailedResponseSchema)
    @api_validate()
    @authorized("vgd.cs.correspondence.write", required_scopes=["vgd.cs"])
    async def post(self, body: MobalyzDocumentTemplate):
        config = self.application.server_base.config.get("MobalyzConfig")
        document_response = await generate_mobalyz_document_template(self, body, config)
        self.finish(
            class_schema(MobalyzDocumentTemplateResponse)().dump(document_response)
        )
