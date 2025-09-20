import os
import requests
import json
from flask import Flask, render_template, request, jsonify, redirect, url_for
from time import sleep

app = Flask(__name__)

# Diese Funktionen müssen Sie mit Ihrer Shelly-Logik füllen
def get_devices():
    # Fügen Sie hier Ihre Logik zum Scannen von Geräten im Hotspot-Modus ein
    # Beispiel-Rückgabe:
    return [{'ip': '192.168.33.1', 'name': 'shellypro4pm-8888', 'status': 'AP-Modus'}]

def configure_device(ip, ssid, password):
    # Fügen Sie hier Ihre Logik zur Konfiguration des Shelly-Geräts ein
    # Beispiel:
    try:
        url = f"http://{ip}/rpc/Shelly.setconfig"
        data = {
            "wifi": {
                "sta": {
                    "enable": True,
                    "ssid": ssid,
                    "pass": password
                }
            }
        }
        response = requests.post(url, json=data, timeout=10)
        response.raise_for_status()
        return {'success': True, 'message': f'Gerät {ip} auf {ssid} konfiguriert'}
    except requests.exceptions.RequestException as e:
        return {'success': False, 'message': f'Fehler bei der Konfiguration von {ip}: {e}'}

# Route für die Hauptseite
@app.route('/')
def index():
    return render_template('index.html')

# API-Endpunkt, um nach Shelly-Geräten zu suchen
@app.route('/api/scan', methods=['GET'])
def scan_devices():
    devices = get_devices()
    return jsonify(devices)

# API-Endpunkt, um ein Gerät zu konfigurieren
@app.route('/api/configure', methods=['POST'])
def configure():
    data = request.json
    ip = data.get('ip')
    ssid = data.get('ssid')
    password = data.get('password')

    if not ip or not ssid or not password:
        return jsonify({'success': False, 'message': 'Fehlende Daten'}), 400

    result = configure_device(ip, ssid, password)
    return jsonify(result)

if __name__ == '__main__':
    print("Startet den Shelly Konfigurator Webserver...")
    app.run(host='0.0.0.0', port=8099)