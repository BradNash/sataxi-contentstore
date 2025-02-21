import asyncio
import os

import bbdcommon.pybus.service_bus as sb
import confuse
from bbdcommon.config.common import (
    _DummyConfigParser,
    parse_config,
    handle_config,
)
from bbdcommon.pybus.common_types import SagaBase
from bbdcommon.pybus.handler_register_functions import (
    HandleFuncRegister,
    HandleRegister,
)
from bbdcontent.common.api.email import send_email, send_email_async
from bbdcontent.common.schemas.correspondence import CorrespondenceConfig
from bbdcontent.common.schemas.email import EmailConfig
from marshmallow_dataclass import class_schema

from sataxi.contentstore.common.api.sms import send_sms
from sataxi.contentstore.common.schemas.sms import SmsConfig, SendSmsRequest
from sataxi.contentstore.messaging.commands.send_correspondence import (
    SendEmailCorrespondenceV1, SendSmsCorrespondenceV1,
)


@HandleRegister()
class EventSaga(SagaBase):
    def __init__(self, bus: sb.KombuBus = None):
        super(EventSaga, self).__init__(bus)
        self.args = None
        self.session = self.bus_ref.db_registry["ContentDB"].get_session()
        self.config = self.load_config_file()
        self.correspondence_config: CorrespondenceConfig
        self.email_config: EmailConfig
        self.sms_config: SmsConfig

    def add_additional_command_line_arguments(self, parser):
        parser.add_argument(
            "--safeSendersFile",
            help="Safe Senders List Config file name. Must be absolute path. Defaults to config.yaml inside "
                 "the node folder/zip",
            dest="safe_senders_file",
            required=False,
            default=None,
        )

    def load_config_file(self):
        self.args = handle_config(None, self.add_additional_command_line_arguments)
        config_dict = parse_config(
            os.getcwd(), self.args, config_type=_DummyConfigParser
        )
        return config_dict

    @HandleFuncRegister(SendEmailCorrespondenceV1)
    def send_email_correspondence(self, msg: SendEmailCorrespondenceV1):
        try:
            safe_senders = confuse.load_yaml(self.args.safe_senders_file)
            correspondence_config = class_schema(CorrespondenceConfig)().load(
                {
                    "is_production": self.config["CorrespondenceConfig"][
                        "IsProduction"
                    ],
                    "safe_senders": safe_senders,
                    "safe_senders_file": self.args.safe_senders_file,
                }
            )
            email_config = class_schema(EmailConfig)().load(
                self.config["CorrespondenceConfig"]["EmailConfig"]
            )

            if "care@gomo" in msg.sender_address and msg.agent != "sp\\service_super":
                carbon_copy = "care@gomo.co.za"
            else:
                carbon_copy = ''

            self.logger.debug(
                f"Template for identifier {msg.template_identifier} found. Identifier is valid."
            )
            self.logger.debug(f"Destination addresses: {msg.receivers}")
            self.logger.debug(
                f"Sender address: {msg.sender_address if msg.sender_address else email_config.default_sender_address}")
            self.logger.debug(f"Agent: {msg.agent}")
            self.logger.debug(f"Attachments: {msg.user_specified_keys}")
            self.logger.debug("Attempting to send email...")

            if msg.send_as_async:
                self.logger.debug("sending email async...")
                loop = asyncio.get_event_loop()
                task = loop.create_task(
                    send_email_async(
                        session=self.session,
                        correspondence_config=correspondence_config,
                        email_config=email_config,
                        agent=msg.agent,
                        template_identifier=msg.template_identifier,
                        template_version=msg.template_version,
                        template_parameters=msg.body,
                        destination_addresses=msg.receivers,
                        sender_address=msg.sender_address,
                        attachments=msg.user_specified_keys,
                        cc_addresses=[carbon_copy],
                        bcc_addresses=[],
                    )
                )
                asyncio.gather(task)
            else:
                self.logger.debug("sending email sync...")
                send_email(
                    session=self.session,
                    correspondence_config=correspondence_config,
                    email_config=email_config,
                    agent=msg.agent,
                    template_identifier=msg.template_identifier,
                    template_version=msg.template_version,
                    template_parameters=msg.body,
                    destination_addresses=msg.receivers,
                    sender_address=msg.sender_address,
                    attachments=msg.user_specified_keys,
                    cc_addresses=[carbon_copy],
                    bcc_addresses=[],
                )

            self.logger.debug("Email successfully sent.")
            self.session.commit()
            self.logger.debug("Email Correspondence Handler Completed.")

        except Exception as ex:
            self.logger.exception(f"Exception: {ex}")
            self.logger.error(f"Unable to process send email message for {msg.user_specified_keys}.")
        finally:
            self.session.close()

    @HandleFuncRegister(SendSmsCorrespondenceV1)
    def send_sms_correspondence(self, msg: SendSmsCorrespondenceV1):
        try:
            safe_senders = confuse.load_yaml(self.args.safe_senders_file)
            correspondence_config = class_schema(CorrespondenceConfig)().load(
                {
                    "is_production": self.config["CorrespondenceConfig"][
                        "IsProduction"
                    ],
                    "safe_senders": safe_senders,
                    "safe_senders_file": self.args.safe_senders_file,
                }
            )
            sms_config = class_schema(SmsConfig)().load(
                self.config["CorrespondenceConfig"]["SmsConfig"]
            )

            sms_request = class_schema(SendSmsRequest)().load({
                "destination_phone_number": msg.destination_phone_number,
                "template_identifier": msg.template_identifier,
                "template_parameters": msg.template_parameters,
                "template_version": msg.template_version,
                "sender": msg.sender
            })

            send_sms(
                self.session,
                correspondence_config,
                sms_config,
                msg.agent,
                sms_request,
            )

            self.logger.debug("SMS successfully sent.")
            self.session.commit()
            self.logger.debug("SMS Correspondence Handler Completed.")
        except Exception as ex:
            self.logger.exception(f"Exception: {ex}")
            self.logger.error(f"Unable to process send sms message for {msg.destination_phone_number}.")
            raise
        finally:
            self.session.close()
