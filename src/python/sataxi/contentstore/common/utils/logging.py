import logging

log = logging.getLogger()


def log_request(level: str, info: str):

    if level == "INFO":
        log.info("****** REQUEST ******")
        log.info(info)

    if level == "DEBUG":
        log.debug("****** REQUEST ******")
        log.debug(info)

    if level == "WARNING":
        log.warning("****** REQUEST ******")
        log.warning(info)


def log_response(level: str, info: str):
    if level == "INFO":
        log.info("****** RESPONSE ******")
        log.info(info)

    if level == "DEBUG":
        log.debug("****** RESPONSE ******")
        log.debug(info)

    if level == "WARNING":
        log.warning("****** RESPONSE ******")
        log.warning(info)
