FROM python:3.11-slim

WORKDIR /data

COPY . /data

RUN pip install --no-cache-dir Flask pydbus requests

RUN chmod a+x /data/run.sh

ENTRYPOINT [ "/data/run.sh" ]