import os
import requests
import json
import ipaddress
import socket
from flask import Flask, render_template, request, jsonify, redirect, url_for
from time import sleep

app = Flask(__name__)

# Diese Funktion scannt nach Shelly-Geräten im Netzwerk
def get_devices():
    """Scans the network for Shelly devices and returns a list."""
    devices = []
    # Annahme: Shelly-Geräte im AP-Modus verwenden die Standard-IP 192.168.33.1
    # Oder Sie können einen IP-Bereich scannen, wenn das Add-on im Host-Netzwerk ist.
    # Hier verwenden wir eine einfache Methode, die auf bekannte IP-Adressen abzielt.

    print("Starte den Scan nach Shelly-Geräten...")
    ip_to_check = '192.168.33.1'
    
    try:
        # Versucht, auf das Shelly-Gerät über seine Standard-AP-IP-Adresse zuzugreifen
        url = f"http://{ip_to_check}/shelly"
        response = requests.get(url, timeout=2)
        
        if response.status_code == 200:
            # Überprüfen, ob es sich um ein Shelly-Gerät handelt
            info = response.json()
            if 'model' in info and 'id' in info:
                print(f"Gerät gefunden: {info['model']} mit ID {info['id']}")
                devices.append({
                    'ip': ip_to_check,
                    'name': f"{info['model']}-{info['id']}",
                    'status': 'AP-Modus'
                })
    except requests.exceptions.RequestException as e:
        print(f"Fehler beim Scannen nach Geräten: {e}")
        return jsonify({'error': f'Fehler beim Scannen: {e}'}), 500
    
    # Hier können Sie weitere IP-Adressen oder mDNS-Discovery hinzufügen
    # Die hier implementierte Logik ist grundlegend, kann aber erweitert werden.
    # Zum Beispiel: ipaddress.IPv4Network('192.168.178.0/24')
    
    return devices

def configure_device(ip, ssid, password):
    """Configures a Shelly device with the given Wi-Fi credentials."""
    try:
        url = f"http://{ip}/rpc/Shelly.SetConfig"
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
    try:
        devices = get_devices()
        return jsonify(devices)
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")
        return jsonify({'error': 'Ein unerwarteter Fehler ist aufgetreten.'}), 500

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
