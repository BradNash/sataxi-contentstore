from dataclasses import dataclass
from typing import Dict, Any

from bbdcommon.spechelpers.misc import schema_field


@dataclass
class MobalyzDocumentTemplate:
    case_number: int = schema_field(
        data_key="caseNumber",
        description="Case Number to attach document",
        required=True,
    )

    pdf_template_name: str = schema_field(
        data_key="pdfTemplateName",
        description="template that should be used",
        required=True,
    )

    details: Dict[str, Any] = schema_field(
        data_key="details",
        description="The parameters required by the template",
        example={"__name": "Clark Kent", "__IdNum": "9306120815031"},
        required=True,
    )

    password_protect: bool = schema_field(
        data_key="passwordProtect",
        description="Should the document be password protected",
        example=True,
        required=True,
    )

    password: str = schema_field(
        data_key="password",
        description="The password to use to protect",
        example="1234567",
        required=True,
    )


@dataclass
class PdfData:
    internal_errors: str = schema_field(data_key="internalErrors")
    pdf_document: str = schema_field(data_key="pdfDocument")
    document_version: int = schema_field(data_key="documentVersion")


@dataclass
class MetaData:
    code: str = schema_field(data_key="code")
    detail: str = schema_field(data_key="detail")
    message: str = schema_field(data_key="message")
    name: str = schema_field(data_key="name")


@dataclass
class MobalyzDocumentResponse:
    data: PdfData = schema_field(data_key="data")
    meta_data: MetaData = schema_field(data_key="metaData")


@dataclass
class MobalyzDocumentTemplateResponse:
    payload: bytes = schema_field(data_key="payload")
    case_number: int = schema_field(
        data_key="caseNumber", description="Case Number to attach document"
    )
    guid: str = schema_field(data_key="guid", description="key to find document")
