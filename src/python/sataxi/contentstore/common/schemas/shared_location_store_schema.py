from dataclasses import dataclass

from bbdcommon.spechelpers.misc import schema_field


@dataclass
class SharedLocationConfig:
    username: str = schema_field(data_key="username", description="Username")
    password: str = schema_field(data_key="password", description="Password")
    server_local_name: str = schema_field(
        data_key="serverLocalName", description="Server Local Name"
    )
    shared_volume: str = schema_field(
        data_key="sharedVolume", description="Shared Volume"
    )
    server_name: str = schema_field(data_key="serverName", description="Server Name")
    system_id: str = schema_field(data_key="systemID", description="System ID")
    server_url: str = schema_field(data_key="serverUrl", description="Server Url")
