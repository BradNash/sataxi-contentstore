from bbdcommon.spechelpers.funcs import api_description, api_tag
from bbdcommon.spechelpers.misc import api_response, api_request, api_validate
from bbdcommon.tornadohelpers.base.authorization import authorized
from bbdcommon.tornadohelpers.base.db_handler import DBHandlerBase
from bbdcommon.tornadohelpers.base.schemas import FailedResponseSchema
from marshmallow_dataclass import class_schema

from sataxi.contentstore.common.document_service import (
    generate_document_template,
    generate_csv,
)
from sataxi.contentstore.common.schemas.csv_schema import CSVRequest, CSVResponse
from sataxi.contentstore.common.schemas.document_template import (
    DocumentTemplate,
    DocumentTemplateResponse,
)


class GenerateDocumentHandler(DBHandlerBase):
    @api_description("Generate Document via template identifier")
    @api_tag("Document Templates")
    @api_request(None, "Document Template request", DocumentTemplate)
    @api_response(
        None, "200", "Document Templates", DocumentTemplateResponse, many=False
    )
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, "500", "Generic Failure", FailedResponseSchema)
    @api_validate()
    @authorized("vgd.cs.correspondence.write", required_scopes=["vgd.cs"])
    async def post(self, body: DocumentTemplate):
        document_response = await generate_document_template(self, body)
        self.finish(class_schema(DocumentTemplateResponse)().dump(document_response))


class GenerateCSVHandler(DBHandlerBase):
    @api_description("Generate CSV")
    @api_tag("Document Templates")
    @api_request(None, "CSV request", CSVRequest)
    @api_response(None, "200", "CSV Response", CSVResponse, many=False)
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, "500", "Generic Failure", FailedResponseSchema)
    @api_validate()
    @authorized("vgd.cs.correspondence.write", required_scopes=["vgd.cs"])
    async def post(self, body: CSVRequest):
        csv_response = generate_csv(self, body)
        self.finish(class_schema(CSVResponse)().dump(csv_response))
