import uuid
from dataclasses import dataclass

from bbdcommon.spechelpers.misc import schema_field


@dataclass
class HiveDocDataRequest:
    account_number: str = schema_field(
        data_key="accountNumber",
        description="Account Number",
        required=True,
        example="000000:000000",
    )
    chassis_number: str = schema_field(
        data_key="chassisNumber",
        description="Chassis Number",
        required=False,
        example="AHTSX22P007003131",
    )
    engine_number: str = schema_field(
        data_key="engineNumber",
        description="Engine Number",
        required=False,
        example="2TR8458234",
    )
    reg_number: str = schema_field(
        data_key="registrationNumber",
        description="Registration Number",
        required=False,
        example="YKX482GP",
    )
    file_name: str = schema_field(
        data_key="fileName", description="File Name", required=False, example="file.pdf"
    )
    process: str = schema_field(
        data_key="process",
        description="Document Type (Settlement, Statement etc)",
        required=True,
        example="Settlement",
    )
    doc_description: str = schema_field(
        data_key="docDescription",
        description="Document Description",
        required=True,
        example="Document Description",
    )
    user_specified_key: str = schema_field(
        data_key="userSpecifiedKey",
        description="Key to find document Data",
        required=True,
        example=f"USERSPECIFIEDKEY={str(uuid.uuid4())} or 123",
    )
    store_shared_location: bool = schema_field(
        data_key="storeSharedLocation",
        description="Whether to store file in shared location",
        required=True,
        example=True,
    )
    customer_id_number: str = schema_field(
        data_key="customerIDNumber",
        description="Customer IDNumber",
        required=True,
        example="4501315068083",
    )
    doc_data: bytes = schema_field(
        data_key="docData",
        description="Customer IDNumber",
        required=False,
    )
    upload_by: str = schema_field(
        data_key="uploadedBy", description="Uploaded By", required=True
    )
    view_name: str = schema_field(
        dump_only=True, description="View Name", required=False, default="Vanguard"
    )
