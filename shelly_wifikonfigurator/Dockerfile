FROM python:3.11-slim

WORKDIR /data

# Kopiert die Startdatei
COPY run.sh /usr/local/bin/run.sh

# Kopiert den Rest der Dateien
COPY . /data

# Stellt sicher, dass das Skript ausführbar ist
RUN chmod a+x /usr/local/bin/run.sh

RUN pip install --no-cache-dir Flask pydbus requests

ENTRYPOINT [ "/usr/local/bin/run.sh" ]