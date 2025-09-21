FROM python:3.11-slim

# Installiert Git, um das Repository zu klonen
RUN apt-get update && apt-get install -y git

WORKDIR /data

# Klont das Repository
RUN git clone https://github.com/0711smarthome/ShellyWIFIKonfigurator2.git

# Wechselt in den Projektordner
WORKDIR /data/ShellyWIFIKonfigurator2/shelly_wifikonfigurator

# Installiert die Python-Abhängigkeiten
RUN pip install --no-cache-dir Flask pydbus requests

# Definiert den Standard-Befehl für den Container
CMD [ "python3", "shelly_configurator.py" ]