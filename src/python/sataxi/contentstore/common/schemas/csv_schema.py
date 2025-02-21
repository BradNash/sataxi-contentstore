from dataclasses import dataclass
from typing import List

from bbdcommon.spechelpers.misc import schema_field


@dataclass
class CSVData:
    index: int = schema_field(
        data_key="index",
        description="CSV index",
        required=True,
    )
    column_names: List[str] = schema_field(
        data_key="column_names",
        description="CSV column names",
        required=True,
    )
    data: List[List[str]] = schema_field(
        data_key="data",
        description="CSV Data",
        required=True,
    )


@dataclass
class CSVRequest:
    json_data: List[CSVData] = schema_field(
        data_key="csv_data",
        description="CSV Data",
        required=True,
        example=[
            {
                "index": 0,
                "column_names": ["Column1", "Column2", "Column3"],
                "data": [
                    ["AAA", "AAA", "AAA"],
                    ["BBB", "BBB", "BBB"],
                    ["CCC", "CCC", "CCC"],
                ],
            },
            {
                "index": 1,
                "column_names": ["Data1", "Data2", "Data3", "Data4", "Data5"],
                "data": [
                    [000, 000, "000", "000", 000],
                    [111, 111, "111", "111", 111],
                    [222, 222, "222", "222", 222],
                    [333, 333, "333", "333", 333],
                ],
            },
        ],
    )
    file_name: str = schema_field(
        data_key="fileName",
        description="CSV Delimiter",
        required=True,
    )
    delimiter: str = schema_field(
        data_key="delimiter",
        description="CSV Delimiter",
        required=True,
        example=";",
        default_factory=";",
    )


@dataclass
class CSVResponse:
    payload: bytes = schema_field(data_key="payload")
    guid: str = schema_field(data_key="guid", description="key to find document")
