FROM 761183306127.dkr.ecr.af-south-1.amazonaws.com/sataxi/base-python-postgres-sqlserver:1.0.0

ARG AWS_PIP_INDEX_URL

RUN apt-get update && apt install -y wkhtmltopdf && mkdir -p -m 0700 /run/user/0

COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt --extra-index-url ${AWS_PIP_INDEX_URL}

COPY ./docker/content-store-service/openssl.cnf /etc/ssl/openssl.cnf
COPY ./docker/content-store-service/config.yaml /config/config.yaml
COPY ./docker/content-store-service/correspondence_safe_senders.yaml /config/correspondence_safe_senders.yaml
COPY ./database/flyway/ /flyway

WORKDIR /app

COPY ./src/python .
COPY ./docker/content-store-service/start.sh .
RUN chmod +x ./start.sh

ENV CONFIG_FILE=/config/config.yaml
ENV SAFE_SENDERS_FILE=/config/correspondence_safe_senders.yaml

RUN opentelemetry-bootstrap --action=install
RUN /utils/patch_logging_instrumentor.sh
ENV XDG_RUNTIME_DIR=/run/user/0
ENV LOGGING_FORMAT="%(levelname)s [%(filename)s:%(lineno)d] [trace_id=%(otelTraceID)s span_id=%(otelSpanID)s] - %(message)s"

VOLUME ["/config", "/flyway"]
EXPOSE 8080

ENTRYPOINT ["./start.sh"]
