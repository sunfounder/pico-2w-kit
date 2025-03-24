.. note:: 

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein und tausche dich mit anderen Enthusiasten aus.

    **Warum beitreten?**

    - **Expertenunterstützung**: Löse nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Sonderrabatte**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nimm an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke [|link_sf_facebook|] und tritt noch heute bei!

8.11 Daten an Bluetooth senden
=================================

In diesem Projekt fungiert der Raspberry Pi Pico 2 W als Peripheriegerät in einem Bluetooth Low Energy (BLE) Netzwerk. Er bietet einen benutzerdefinierten BLE-Dienst mit einer Eigenschaft, die sowohl das Lesen als auch Benachrichtigungen unterstützt. Ein zentrales Gerät, wie ein Smartphone, kann sich mit dem Pico W verbinden, um Textnachrichten über BLE zu empfangen.

Die an Bord befindliche LED zeigt den Verbindungsstatus an: Sie leuchtet auf, wenn sich ein zentrales Gerät verbindet, und erlischt, wenn die Verbindung getrennt wird. Du kannst den Gerätenamen anpassen oder das System automatisch einen Namen basierend auf der MAC-Adresse generieren lassen. Das Skript bewirbt kontinuierlich den BLE-Dienst und ermöglicht es den Benutzern, über das Terminal Text einzugeben, der dann an alle verbundenen zentralen Geräte gesendet wird.

1. Baue den Schaltkreis
+++++++++++++++++++++++++++++++++

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten. 

Es ist definitiv praktisch, ein gesamtes Kit zu kaufen, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ARTIKEL IN DIESEM KIT
        - LINK
    *   - Pico 2 W Starter Kit	
        - 450+
        - |link_pico2w_kit|

Du kannst sie auch einzeln über die folgenden Links kaufen.


.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - KOMPONENTE	
        - MENGE
        - LINK

    *   - 1
        - :ref:`cpn_pico_2w`
        - 1
        - |link_pico2w_buy|
    *   - 2
        - Micro USB Kabel
        - 1
        - 

Für dieses Projekt sind keine zusätzlichen Schaltungen erforderlich. Schließe einfach das Raspberry Pi Pico 2 W über ein USB-Datenkabel an deinen Computer an.

2. Code ausführen
+++++++++++++++++++++++++++++++++

Kopiere den folgenden Code in deine IDE. Alternativ findest du ihn in unserem Repository unter dem Pfad: ``pico-2w-kit/micropython/iot/8.11-write_to_ble/8.11-write_to_ble.py``.

Hinweis: Dieser Code hängt von der Datei ``ble_advertising.py`` ab. Stelle sicher, dass du diese auf das Pico-Board hochlädst, bevor du das Skript ausführst.

.. code-block:: python

   import bluetooth
   import struct
   import time
   import machine
   import ubinascii
   from ble_advertising import advertising_payload
   from micropython import const
   from machine import Pin 
   
   _IRQ_CENTRAL_CONNECT = const(1)
   _IRQ_CENTRAL_DISCONNECT = const(2)
   _IRQ_GATTS_INDICATE_DONE = const(20)
   
   _FLAG_READ = const(0x0002)
   _FLAG_NOTIFY = const(0x0010)
   
   # Benutzerdefinierte UUIDs für Dienst und Eigenschaft
   # Diese bei Bedarf anpassen.
   _SERVICE_UUID = bluetooth.UUID("3ec837af-b0c6-4e7e-a8c5-4b31311d98cf")
   _CHAR_UUID = (
       bluetooth.UUID("945c4d90-825d-452f-820a-0d8b0cc74a12"),
       _FLAG_READ | _FLAG_NOTIFY,
   )
   
   _SERVICE = (
       _SERVICE_UUID,
       (_CHAR_UUID,),
   )
   
   led = Pin("LED", Pin.OUT)
   
   class BLEText:
       def __init__(self, ble, name=""):
           # BLE-Schnittstelle initialisieren und benutzerdefinierten Dienst registrieren
           self._ble = ble
           self._ble.active(True)
           self._ble.irq(self._irq)
           ((self._handle,),) = self._ble.gatts_register_services((_SERVICE,))
           self._connections = set()
   
           # Wenn kein Name angegeben wird, einen basierend auf der MAC-Adresse generieren
           if len(name) == 0:
               name = 'Pico %s' % ubinascii.hexlify(self._ble.config('mac')[1], ':').decode().upper()
           print('Device name: %s' % name)
   
           # Erstelle die Werbe-Payload mit dem benutzerdefinierten Dienst
           self._payload = advertising_payload(
               name=name, services=[_SERVICE_UUID]
           )
           self._advertise()
   
       def _irq(self, event, data):
           # BLE-Ereignisse behandeln
           if event == _IRQ_CENTRAL_CONNECT:
               # Ein zentrales Gerät hat sich verbunden
               conn_handle, _, _ = data
               self._connections.add(conn_handle)
               print("New connection", conn_handle)
               led.value(1)
           elif event == _IRQ_CENTRAL_DISCONNECT:
               # Ein zentrales Gerät hat sich getrennt
               conn_handle, _, _ = data
               self._connections.remove(conn_handle)
               print("Disconnected", conn_handle)
               led.value(0)
               # Starte erneut die Werbung, um eine neue Verbindung zu ermöglichen
               self._advertise()
           elif event == _IRQ_GATTS_INDICATE_DONE:
               # Bestätigung der Indikation empfangen (hier nicht verwendet)
               conn_handle, value_handle, status = data
   
       def send_text(self, text):
           # Den gegebenen Text in den Eigenschaftswert schreiben
           self._ble.gatts_write(self._handle, text.encode('utf-8'))
           # Alle verbundenen Zentralen über den neuen Wert benachrichtigen
           for conn_handle in self._connections:
               self._ble.gatts_notify(conn_handle, self._handle)
   
       def _advertise(self, interval_us=500000):
           print("Starting advertising")
           # BLE-Werbung mit dem gegebenen Intervall starten
           self._ble.gap_advertise(interval_us, adv_data=self._payload)
       
       def is_connected(self):
           return len(self._connections) > 0
   
   def demo():
       # Eine BLE-Instanz und ein BLEText-Peripheriegerät erstellen
       ble = bluetooth.BLE()
       ble_text = BLEText(ble,"pico2w")
   
       # Ununterbrochen Eingaben vom Terminal lesen und über BLE senden
       while True:
           if ble_text.is_connected():
               line = input("Enter text to send via BLE (Ctrl+C to exit): ")
               ble_text.send_text(line)
   
   
   if __name__ == "__main__":
       demo()

3. Daten vom Bluetooth empfangen
++++++++++++++++++++++++++++++++++++

Um mit den in diesem Code definierten Diensten und Eigenschaften zu interagieren, verwende eine allgemeine Bluetooth® Low Energy Zentral-App, wie zum Beispiel LightBlue (für iOS und Android) oder nRF Connect (für Android).

In diesem Abschnitt wird LightBlue als Beispiel verwendet, um zu zeigen, wie du die Funktionen des Pico 2 W über Bluetooth steuern kannst. 

a. Installiere LightBlue

   Lade die LightBlue-App aus dem |link_lightblue_apple| (für iOS) oder |link_lightblue_google| (für Android) herunter.

   .. image:: img/lightblue.png
      :width: 90%

b. Verbinde dich mit dem Pico 2 W

   Starte LightBlue und erlaube die Standort- und Bluetooth-Berechtigungen, falls du dazu aufgefordert wirst. Auf der Seite **Peripheriegeräte** suche nach „pico“ in der Suchleiste und tippe, um dich mit dem Pico 2 W Gerät zu verbinden.

   .. image:: img/11-1-connect-pico.png
      :width: 60%
      :align: center

c. Daten vom BLE lesen

   Nach der Verbindung zeigt LightBlue detaillierte Informationen über das Pico 2 W Bluetooth-Gerät an. Scrolle nach unten, um den **Dienst (3ec837af-b0c6-4e7e-a8c5-4b31311d98cf)** und die **Eigenschaft (945c4d90-825d-452f-820a-0d8b0cc74a12)** zu finden.

   Tippe auf die Eigenschaft 945c4d90-825d-452f-820a-0d8b0cc74a12. Die App zeigt die Eigenschaften dieser Eigenschaft an: Sie unterstützt das Lesen und Benachrichtigungen.

   .. image:: img/11-2-new.png
      :width: 100%

   Wähle oben rechts **"UTF-8 String"** als Datentyp aus.

   .. image:: img/11-4-new.png
      :width: 100%
    
   Tippe auf "Lesen", um den aktuellen Wert abzurufen. Da noch keine Daten definiert sind, wird der Wert als „Kein Wert“ angezeigt. Kehre nun zum Computer zurück und gib „hello“ im Terminal ein. Wechsle zurück zu LightBlue und tippe erneut auf **"Lesen"**. Die Nachricht "hello" erscheint nun, gesendet vom Pico 2 W an das Telefon.

   .. image:: img/11-6-new.png
      :width: 100%

   .. image:: img/11-6-micropython.png
      :align: center
      :width: 80%

   Um kontinuierlich Updates zu überwachen, kannst du auch **"Abonnieren"** tippen, um diese Eigenschaft zu abonnieren. Wenn du neue Zeichen aus dem Terminal sendest, werden sie automatisch aktualisiert und auf deinem Telefon angezeigt.

   .. image:: img/11-8-new.png
      :width: 100%

