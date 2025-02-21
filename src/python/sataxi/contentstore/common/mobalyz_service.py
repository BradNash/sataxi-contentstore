import base64
import logging
import os
import uuid

from bbdcontent.common.api.upload_content.v2 import upload_cs_db_content
from bbdcontent.common.schemas.content import ContentType

from sataxi.contentstore.common.schemas.mobaylz_document_schema import (
    MobalyzDocumentTemplateResponse,
    MobalyzDocumentResponse,
    MobalyzDocumentTemplate,
)
from sataxi.contentstore.common.utils.config_http_wrapper import ConfigHttpWrapper
from sataxi.contentstore.messaging.commands.attach_document import AttachDocumentV1


async def generate_mobalyz_document_template(
    self, mobalyze_document_template: MobalyzDocumentTemplate, configs
):
    api_url = configs.get("URL")
    http_wrapper = ConfigHttpWrapper()
    mobalyze_document_template.details.update(
        ApplicationName=configs.get("ApplicationName")
    )
    response: MobalyzDocumentResponse = await http_wrapper.generate_mobalyz_doc(
        api_url, mobalyze_document_template
    )

    guid = str(uuid.uuid4())
    file_name = f"{mobalyze_document_template.case_number}_{mobalyze_document_template.pdf_template_name}.pdf"

    if not response.data and not response.data.pdf_document:
        logging.error(
            f"No pdf document base64 string was returned for case number :[{mobalyze_document_template.case_number}]"
        )

    pdf_data: bytes = base64.b64decode(response.data.pdf_document, validate=True)

    await persist_document(
        file_name, guid, pdf_data, self, mobalyze_document_template.password
    )
    await put_message_on_bus(
        file_name, guid, mobalyze_document_template.case_number, self
    )

    return MobalyzDocumentTemplateResponse(
        payload=response.data.pdf_document,
        case_number=mobalyze_document_template.case_number,
        guid=guid,
    )


async def write_doc_to_drive(response, file_name) -> bytes:
    output_path = os.path.abspath(
        os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__))))
    )
    pdf_path = output_path + f"\\{file_name}"

    file_bytes = base64.b64decode(response.data.pdf_document, validate=True)
    with open(pdf_path, "wb") as pdf_datafile:
        pdf_datafile.write(file_bytes)
    with open(pdf_path, "rb") as pdf_datafile:
        pdf_data = pdf_datafile.read()
    os.remove(pdf_path)
    return pdf_data


async def put_message_on_bus(file_name, guid, case_number, self):
    attach_document = AttachDocumentV1(case_number, self.current_user, file_name, guid)
    self.application.server_base.node.bus.send(
        msg_obj=attach_document, reply_node_id=None
    )
    self.application.server_base.node.bus.commit_messaging()
    self.application.server_base.node.bus.emit_prompts()
    self.application.server_base.node.bus.reset_state()


async def persist_document(file_name, guid, pdf_data, self, password=""):
    upload_cs_db_content(
        session=self.session,
        content_type=ContentType.STRING,
        source_type=1,
        source_id="Vanguard",
        user_specified_key=guid,
        file={
            "filename": file_name,
            "content_type": "application/pdf",
            "body": pdf_data,
        },
        user=self.current_user,
        encryption_password=password,
    )
    self.session.commit()
