from dataclasses import dataclass
from typing import Dict, Union, List

from bbdcommon.spechelpers.misc import schema_field


@dataclass
class SmsConfig:
    url: str = schema_field(data_key="Url")
    system_id: str = schema_field(data_key="SystemID")
    user_id: str = schema_field(data_key="UserID")


@dataclass
class SendSmsRequest:
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
    sender: str = schema_field(required=False, description="The sender of the sms")
    template_version: Union[int, None] = schema_field(
        required=False,
        description=(
            "The version of the template to use. If not provider,"
            + "the latest version of the specified template will get used."
        ),
        default=None,
    )


@dataclass
class SMSRequest:
    phone_number: str = schema_field(data_key="PhoneNumber", required=True)
    system_id: str = schema_field(data_key="SystemID", required=True)
    result_template: str = schema_field(data_key="ResultTemplate", required=True)
    pref_language: str = schema_field(
        data_key="Pref_Language", required=False, default="English"
    )
    customer_id_number: str = schema_field(
        data_key="CustomerIdNumber", required=False, default=""
    )
    customer_name: str = schema_field(
        data_key="CustomerName", required=False, default=""
    )
    user_id: int = schema_field(data_key="UserID", required=True, default=0)
    template_id: int = schema_field(data_key="TemplateID", required=False, default=0)
    response_msg: str = schema_field(data_key="Responsemsg", required=False, default="")
    account_number: str = schema_field(
        data_key="AccountNumber", required=False, default=""
    )
