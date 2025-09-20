import os
import requests
import time

WIFI_SSID = os.environ.get('your_wifi_ssid')
WIFI_PASSWORD = os.environ.get('your_wifi_password')

# Shelly API Endpunkt für die WLAN-Konfiguration
SHELLY_CONFIG_URL = "http://192.168.33.1/settings/sta"

# Überprüfen, ob die Umgebungsvariablen gesetzt sind
if not WIFI_SSID or not WIFI_PASSWORD:
    print("Fehler: Umgebungsvariablen 'WIFI_SSID' und 'WIFI_PASSWORD' sind nicht gesetzt.")
    exit(1)

# Daten für die API-Anfrage
payload = {
    "sta_ssid": WIFI_SSID,
    "sta_pass": WIFI_PASSWORD,
    "sta_enable": True
}

try:
    print(f"Versuche, Shelly mit dem WLAN {WIFI_SSID} zu verbinden...")
    response = requests.post(SHELLY_CONFIG_URL, data=payload, timeout=10)
    response.raise_for_status()

    print("Erfolgreich! Die WLAN-Konfiguration wurde an den Shelly gesendet.")
    print("Shelly startet neu...")

except requests.exceptions.RequestException as e:
    print(f"Fehler bei der Anfrage an den Shelly: {e}")
    print("Stellen Sie sicher, dass Ihr Home Assistant-Gerät mit dem Shelly AP verbunden ist.")
    exit(1)

print("Skript beendet. Sie können das Add-on nun stoppen.")
