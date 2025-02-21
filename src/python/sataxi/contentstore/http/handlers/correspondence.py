from bbdcommon.spechelpers.funcs import api_description, api_tag
from bbdcommon.spechelpers.misc import api_response, api_request, api_validate
from bbdcommon.tornadohelpers.base.authorization import authorized
from bbdcommon.tornadohelpers.base.db_handler import DBHandlerBase
from bbdcommon.tornadohelpers.base.schemas import FailedResponseSchema

from sataxi.contentstore.common.schemas.sms import SendSmsRequest
from sataxi.contentstore.common.api.sms import send_sms


class SmsSendHandler(DBHandlerBase):
    @api_description("Send an SMS using a template to the specified destination")
    @api_tag("Correspondence")
    @api_request(None, "SMS Send request", SendSmsRequest)
    @api_response(None, "200", "SMS successfully sent", None)
    @api_response(None, 400, "Request failure.", FailedResponseSchema)
    @api_response(None, 404, "Requested data does not exist.", FailedResponseSchema)
    @api_response(None, 500, "GenericFailure.", FailedResponseSchema)
    @api_validate()
    @authorized("vgd.cs.correspondence.write", required_scopes=["vgd.cs"])
    def post(self, body: SendSmsRequest):

        send_sms(
            self.session,
            self.application.server_base.correspondence_config,
            self.application.server_base.sms_config,
            self.current_user,
            body,
        )
        self.finish()
