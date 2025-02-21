import logging

import requests
from bbdcontent.common.api.correspondence import (
    save_correspondence,
    get_correspondence_template_and_template_out,
)
from bbdcontent.common.schemas.correspondence import CorrespondenceConfig
from marshmallow_dataclass import class_schema
from sqlalchemy.orm import Session
from tornado.web import HTTPError

from sataxi.contentstore.common.schemas.sms import SmsConfig, SMSRequest, SendSmsRequest


def send_sms(
    session: Session,
    correspondence_config: CorrespondenceConfig,
    sms_config: SmsConfig,
    agent: str,
    sms_request: SendSmsRequest,
):
    templated_sms = get_correspondence_template_and_template_out(
        session,
        sms_request.template_identifier,
        sms_request.template_version,
        sms_request.template_parameters,
        "SMS",
    )

    if not correspondence_config.is_production:
        user_id = agent.split("\\")[1]
        if user_id in correspondence_config.safe_senders.keys():
            sms_request.destination_phone_number = [
                correspondence_config.safe_senders.get(user_id).sms
            ]
        else:
            raise UserWarning(
                f"User {user_id} is not in the safe senders list."
                + "To fix this error please add the user to the file: {correspondence_config.safe_senders_file}"
            )

    for phone_number in sms_request.destination_phone_number:
        new_sms_request = SMSRequest(
            phone_number=phone_number,
            system_id=sms_config.system_id,
            result_template=templated_sms.template,
        )
        logging.debug(
            f"Sending SMS to {phone_number} with template identifier {sms_request.template_identifier}"
        )
        response = requests.post(sms_config.url, json=class_schema(SMSRequest)().dump(new_sms_request), timeout=59)
        if not response.ok:
            raise HTTPError(response.status_code, response.text)
        sender = sms_request.sender if sms_request.sender else "SATAXI_SMS_GATEWAY"
        save_correspondence(
            session=session,
            agent=agent,
            type="SMS",
            template=templated_sms.template,
            destination=phone_number,
            sender=sender,
        )
        session.commit()
