FROM python:3.11-slim

WORKDIR /data

# Kopiert die Startdatei run.sh
COPY run.sh /data/run.sh

# Kopiert die Hauptanwendung
COPY shelly_configurator.py /data/shelly_configurator.py

# Kopiert den templates-Ordner
COPY templates/ /data/templates/

# Stellt sicher, dass die Skripte ausführbar sind
RUN chmod a+x /data/run.sh

# Installiert Python-Abhängigkeiten
RUN pip install --no-cache-dir Flask pydbus requests

# Definiert den Startpunkt des Containers
ENTRYPOINT [ "/data/run.sh" ]