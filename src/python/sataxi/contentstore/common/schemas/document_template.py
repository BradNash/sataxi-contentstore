from dataclasses import dataclass

from bbdcommon.spechelpers.misc import schema_field
from typing import Dict, Union, Any


@dataclass
class DocumentTemplate:
    case_number: int = schema_field(
        data_key="caseNumber",
        description="Case Number to attach document",
        required=True,
    )
    account_number: str = schema_field(
        data_key="accountNumber",
        description="Account Number of client",
        required=True,
    )

    template_identifier: str = schema_field(
        description="The ID of the template to populate",
        data_key="templateIdentifier",
        required=True,
    )

    template_parameters: Dict[str, Any] = schema_field(
        data_key="templateParameters",
        description="The parameters required by the template",
        example={
            "NAME": "Clark Kent",
            "ACCOUNTS": ["001", "002"],
            "DETAILS": [{"KEY_1": "VALUE_1", "KEY_2": "VALUE_2"}],
        },
        required=True,
    )

    encryption_password: str = schema_field(
        data_key="encryptionPassword",
        description="Password to encrypt password",
        required=True,
    )

    template_version: Union[int, None] = schema_field(
        data_key="templateVersion",
        description=(
            "The version of the template to use. If not "
            "provider, the latest version  of the specified "
            "template will get used."
        ),
        default=None,
        required=False,
    )


@dataclass
class DocumentTemplateResponse:
    payload: bytes = schema_field(data_key="payload")
    case_number: int = schema_field(
        data_key="caseNumber", description="Case Number to attach document"
    )
    guid: str = schema_field(data_key="guid", description="key to find document")


@dataclass
class DocumentTemplates:
    identifier: str = schema_field(data_key="identifier")
    business_rule: str = schema_field(data_key="businessRule")
    note: str = schema_field(data_key="note")
    disabled: bool = schema_field(data_key="disabled")
