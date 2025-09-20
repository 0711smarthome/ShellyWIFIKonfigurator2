FROM python:3.11-slim

WORKDIR /data

# Erstellt die Startdatei direkt im Container
RUN echo "#!/bin/bash" > /data/run.sh
RUN echo "python3 /data/shelly_configurator.py" >> /data/run.sh

# Macht die Startdatei ausführbar
RUN chmod a+x /data/run.sh

# Kopiert die Hauptanwendung
COPY shelly_configurator.py /data/shelly_configurator.py

# Kopiert den templates-Ordner
COPY templates/ /data/templates/

# Installiert Python-Abhängigkeiten
RUN pip install --no-cache-dir Flask pydbus requests

# Definiert den Startpunkt des Containers
ENTRYPOINT [ "/data/run.sh" ]