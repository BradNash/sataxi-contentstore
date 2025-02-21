#!/bin/bash

opentelemetry-instrument \
    python -m sataxi.contentstore.services.content_rest_service \
    --nodeName=content_rest_service \
    --handlerSearchPath ./sataxi/contentstore/messaging/handlers \
    --configFile=$CONFIG_FILE \
    --safeSendersFile=$SAFE_SENDERS_FILE $@
