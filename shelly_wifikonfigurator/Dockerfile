ARG GHCR_TOKEN
FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y jq libdbus-1-dev && \
    apt-get clean

RUN pip install pydbus requests

COPY shelly_configurator.py /
COPY run.sh /

RUN chmod a+x /run.sh

CMD [ "/run.sh" ]
