from dataclasses import dataclass
from typing import Optional, Dict, Union, List

from bbdcommon.pybus.service_bus import BaseMessage
from bbdcommon.spechelpers.misc import schema_field


@dataclass
class SendEmailCorrespondenceV1(BaseMessage):
    receivers: List[str] = schema_field(data_key="receiver", required=True)
    agent: str = schema_field(data_key="agent", required=True)
    body: dict = schema_field(data_key="body", required=True)
    template_identifier: str = schema_field(
        data_key="templateIdentifier", required=True
    )
    send_as_async: bool = schema_field(
        data_key="sendAsAsync", required=True, default=True
    )
    template_version: Optional[int] = schema_field(
        data_key="templateVersion", required=False, default_factory=None
    )
    user_specified_keys: List[str] = schema_field(
        data_key="userSpecifiedKeys", default_factory=list
    )
    sender_address: str = schema_field(
        data_key="senderAddress", required=False, default=None
    )


@dataclass
class SendSmsCorrespondenceV1(BaseMessage):
    destination_phone_number: List[str] = schema_field(
        required=True,
        description="The phone number to send the SMS to",
    )
    template_identifier: str = schema_field(
        required=True, description="The ID of the template to populate"
    )
    template_parameters: Dict[str, str] = schema_field(
        required=True,
        description="The parameters required by the template",
        example={"NAME": "Clark Kent"},
    )
    template_version: Union[int, None] = schema_field(
        required=False,
        description=(
            "The version of the template to use. If not provider,"
            + "the latest version of the specified template will get used."
        ),
        default=None,
    )
    agent: str = schema_field(data_key="agent", required=True, default=None)
    sender: str = schema_field(data_key="sender", required=False, default=None)
