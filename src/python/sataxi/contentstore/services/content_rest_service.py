import os
import sys

from marshmallow_dataclass import class_schema

from bbdcommon.pybus.py_node import PyNode
from bbdcontent.services.content_rest_service import ContentStoreRestService

from sataxi.contentstore.common.schemas.sms import SmsConfig
from sataxi.contentstore.http.handlers.correspondence import SmsSendHandler

from sataxi.contentstore.http.handlers.document_template_handler import (
    GenerateDocumentHandler,
    GenerateCSVHandler,
)
from sataxi.contentstore.http.handlers.hive_doc_data_handler import HiveDocDataHandler
from sataxi.contentstore.http.handlers.mobalyze_document_template_handler import (
    MobalyzDocumentHandlerV1,
)

DEFAULT_PORT = 8080


class SaTaxiContentStoreService(ContentStoreRestService):
    def __init__(self, port, spec=None):
        self.node = PyNode()
        super().__init__(port=port, spec=spec)

        if (
            "CorrespondenceConfig" in self.config.keys()
            and "SmsConfig" in self.config["CorrespondenceConfig"].keys()
        ):
            self.sms_config = class_schema(SmsConfig)().load(
                self.config["CorrespondenceConfig"]["SmsConfig"]
            )

    def get_url_mappings(self):
        return super().get_url_mappings() + [
            (r"/correspondence/v1/sms/send", SmsSendHandler),
            (r"/documents/v1/generate", GenerateDocumentHandler),
            (r"/documents/v1/generate_csv", GenerateCSVHandler),
            (r"/documents/v1/mobalyz/generate", MobalyzDocumentHandlerV1),
            (r"/documents/v1/save_document_to_hive", HiveDocDataHandler),
        ]


def main():
    config_service = SaTaxiContentStoreService(port=DEFAULT_PORT)
    output_path = os.path.join(
        os.path.dirname(__file__), "content_rest_service_apispec.yaml"
    )
    with open(output_path, "w") as open_api_file:
        open_api_file.writelines(config_service.get_open_api_schema(True))
    if "--spec_only" in sys.argv:
        sys.exit(0)
    config_service.start_with_ioloop()


if __name__ == "__main__":
    main()
