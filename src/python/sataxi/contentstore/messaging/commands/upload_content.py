from dataclasses import dataclass
from typing import Optional

from bbdcommon.spechelpers.misc import schema_field

from bbdcommon.pybus.service_bus import BaseMessage


@dataclass
class UploadContentV1(BaseMessage):
    content_type: int = schema_field(data_key="contentType")
    source_type: int = schema_field(data_key="sourceType")
    source_id: str = schema_field(data_key="sourceID")
    user: str = schema_field(data_key="user")
    user_specified_key: str = schema_field(data_key="userSpecifiedKey")
    file_name: str = schema_field(data_key="fileName")
    mime_type: str = schema_field(data_key="mimeType")
    content_data: str = schema_field(data_key="contentData")
    encryption_password: Optional[str] = schema_field(data_key="encryptionPassword")
