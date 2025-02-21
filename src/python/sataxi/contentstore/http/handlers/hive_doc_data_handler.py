from bbdcommon.spechelpers.funcs import api_description, api_tag
from bbdcommon.spechelpers.misc import api_response, api_request, api_validate
from bbdcommon.tornadohelpers.base.authorization import authorized
from bbdcommon.tornadohelpers.base.db_handler import DBHandlerBase
from bbdcommon.tornadohelpers.base.schemas import FailedResponseSchema

from sataxi.contentstore.common.document_service import hive_docdata_insert
from sataxi.contentstore.common.schemas.doc_data_schema import HiveDocDataRequest
from sataxi.contentstore.common.schemas.shared_location_store_schema import (
    SharedLocationConfig,
)


class HiveDocDataHandler(DBHandlerBase):
    @api_description("Save Documents to Shared Location and Hive")
    @api_tag("Document Templates")
    @api_request(None, "Hive Doc Data Request", HiveDocDataRequest)
    @api_response(None, "200", "Hive Doc Response", many=False)
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, "500", "Generic Failure", FailedResponseSchema)
    @api_validate()
    @authorized("vgd.cs.content.write", required_scopes=["vgd.cs"])
    async def post(self, body: HiveDocDataRequest):
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
        hive_docdata_insert(self, body, shared_location_config)
        self.finish()
