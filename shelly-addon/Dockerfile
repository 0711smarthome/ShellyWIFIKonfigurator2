FROM python:3.11-alpine

WORKDIR /usr/src/app

# Installiert Systemwerkzeuge für die Netzwerkkonfiguration
RUN apk update && apk add --no-cache \
    networkmanager-cli \
    avahi \
    dbus \
    net-tools \
    iw

COPY . .

# Installiert Python-Abhängigkeiten
RUN pip install --no-cache-dir Flask pydbus requests

CMD ["python3", "shelly_configurator.py"]