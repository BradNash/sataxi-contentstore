FROM 761183306127.dkr.ecr.af-south-1.amazonaws.com/sataxi/base-python-postgres:1.0.0

#COPY ./requirements.txt /requirements.txt
RUN pip install bbd-services-contentstore==2.0.1b8 psycopg2-binary==2.9.3

COPY ./docker/correspondence-importer/config.yaml /config/config.yaml

WORKDIR /app

COPY ./src/import-configs ./import-configs
COPY ./docker/correspondence-importer/start.sh .
RUN chmod +x ./start.sh

ENV CONFIG_FILE=/config/config.yaml
ENV IMPORT_CONFIGS_DIR=./import-configs

VOLUME ["/config"]

#ENTRYPOINT tail -f /dev/null
ENTRYPOINT ["./start.sh"]
