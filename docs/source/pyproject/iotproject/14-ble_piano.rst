.. note:: 

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche mit anderen Technikbegeisterten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum solltest du mitmachen?**

    - **Expertenunterstützung**: Erhalte Hilfe bei Problemen nach dem Kauf sowie bei technischen Herausforderungen – durch unser Team und unsere Community.
    - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Einblicke**: Erfahre als Erste*r von neuen Produkten und erhalte exklusive Vorschauen.
    - **Sonderrabatte**: Profitiere von exklusiven Angeboten auf unsere neuesten Produkte.
    - **Aktionen und Gewinnspiele**: Nimm an spannenden Aktionen und festlichen Verlosungen teil.

    👉 Bereit für Entdeckungen und Kreativität? Klicke auf [|link_sf_facebook|] und sei dabei!

.. _py_iot_ble_piano:

8.14 Bluetooth-Piano
==========================================

In diesem Projekt wird eine selbst entwickelte App genutzt, um ein Raspberry Pi Pico 2 W in ein Bluetooth-fähiges Piano zu verwandeln. Das Pico 2 W führt ein MicroPython-Skript aus, das es als BLE-Peripheriegerät konfiguriert, damit es Notendaten von einem verbundenen Gerät empfangen kann. Beim Empfang einer Note verarbeitet das Board die Daten und spielt den entsprechenden Ton über einen passiven Summer.

Dieses Projekt ist ideal, um die Grundlagen der Bluetooth-Low-Energy-Kommunikation (BLE), Tonerzeugung per PWM und die Entwicklung interaktiver Anwendungen mit dem Raspberry Pi Pico 2 W zu erlernen.

Die in diesem Projekt verwendete App wurde mit |link_appinventor| erstellt.


1. Schaltung aufbauen
+++++++++++++++++++++++++++++++++

**Benötigte Komponenten**

Für dieses Projekt werden die folgenden Komponenten benötigt.

Ein komplettes Kit ist sehr praktisch – hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ENTHALTENE TEILE
        - LINK
    *   - Pico 2 W Starter Kit	
        - 450+
        - |link_pico2w_kit|

Alternativ kannst du die Teile auch einzeln über die folgenden Links erwerben:


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
        - Micro-USB-Kabel
        - 1
        - 
    *   - 3
        - :ref:`cpn_breadboard`
        - 1
        - |link_breadboard_buy|
    *   - 4
        - :ref:`cpn_wire`
        - Mehrere
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_transistor`
        - 1 (S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_resistor`
        - 1 (1KΩ)
        - |link_resistor_buy|
    *   - 7
        - Passiver :ref:`cpn_buzzer`
        - 1
        - |link_passive_buzzer_buy|


.. image:: img/wiring/8.14_bb.png
   :width: 90%

.. raw:: html

   <br/>

2. Android-App erstellen
+++++++++++++++++++++++++++++++++

Die Android-App wird mit |link_appinventor| entwickelt – einer kostenlosen Webanwendung, ideal für Einsteiger in die Android-Entwicklung. Sie bietet eine intuitive Drag-and-Drop-Oberfläche für die Erstellung funktionaler Apps.

So beginnst du:

#. Gehe zu |link_appinventor_login| und klicke auf "Online Tool", um dich anzumelden. Du benötigst ein Google-Konto für die Registrierung bei MIT App Inventor.

   .. image:: img/13-ai-signup.png
       :width: 90%
       :align: center

#. Nach der Anmeldung navigierst du zu **Projects** → **Import project (.aia) from my computer**. Lade dann die Datei ``ble_piano_picow.aia`` aus dem Verzeichnis ``pico-2w-kit/micropython/iot/8.14-ble_piano`` hoch.

   Alternativ kannst du die Datei direkt hier herunterladen: :download:`ble_piano_picow.aia</_static/other/ble_piano_picow.aia>`

   .. image:: img/13-ai-import.png
        :align: center

#. Nach dem Upload erscheint die App-Vorlage in der MIT-App-Inventor-Oberfläche. Diese vorgefertigte Vorlage kann später individuell angepasst werden.

#. MIT App Inventor besteht aus zwei Hauptbereichen: **Designer** und **Blocks**. Oben rechts auf der Seite kannst du zwischen beiden wechseln.

   .. image:: img/13-ai-intro-1.png

#. Im **Designer**-Bereich kannst du Buttons, Texte und Bildschirme hinzufügen und das App-Layout gestalten.

   .. image:: img/14-ai-intro-2.png
      :width: 100%

#. Im **Blocks**-Bereich erstellst du individuelle Funktionen für die App und programmierst die Logik hinter den Bedienelementen.

   .. image:: img/14-ai-intro-3.png
      :width: 100%

#. Um die App auf deinem Smartphone zu installieren, gehe zum Reiter **Build**.

   .. image:: img/13-ai-intro-4.png
      :width: 60%
      :align: center

   * Erzeuge eine ``.apk``-Datei. Du kannst die Datei anschließend herunterladen oder per QR-Code auf dem Handy installieren. Folge den Anweisungen zur Installation.

     Oder lade unsere vorgefertigte APK hier herunter: :download:`ble_piano_picow.apk</_static/other/ble_piano_picow.apk>`

   * Falls du die App im Google Play Store veröffentlichen möchtest, kannst du auch eine ``.aab``-Datei erzeugen.


3. Code ausführen
+++++++++++++++++++++++++++++++++

Öffne die Datei ``8.14-ble_piano.py`` im Verzeichnis ``pico-2w-kit/micropython/iot/8.14-ble_piano`` oder kopiere den Code in deine Entwicklungsumgebung.

.. note:: 
   Dieser Code erfordert die Datei ``ble_advertising.py``. Stelle sicher, dass du sie vor dem Start auf den Pico hochlädst.

.. code-block:: python

   import bluetooth
   import random
   import struct
   import time
   from ble_example.ble_advertising import advertising_payload
   from machine import Pin, PWM
   import time
   
   from micropython import const
   
   buzzer = PWM(Pin(15)) 
   
   NOTES = {
       'NOTE_C4': 262,
       'NOTE_D4': 294,
       'NOTE_E4': 330,
       'NOTE_F4': 349,
       'NOTE_G4': 392,
       'NOTE_A4': 440,
       'NOTE_B4': 494,
       'NOTE_C5': 523
   }
   
   _IRQ_CENTRAL_CONNECT = const(1)
   _IRQ_CENTRAL_DISCONNECT = const(2)
   _IRQ_GATTS_WRITE = const(3)
   
   _FLAG_READ = const(0x0002)
   _FLAG_WRITE_NO_RESPONSE = const(0x0004)
   _FLAG_WRITE = const(0x0008)
   _FLAG_NOTIFY = const(0x0010)
   
   _PIANO_UUID = bluetooth.UUID("952cc3a7-1801-4c07-b141-e1e3964f54b5")
   _NOTE_CHAR = (
       bluetooth.UUID("ea30277b-d7a5-4eeb-af70-6179c45d7ee6"),
       _FLAG_READ | _FLAG_WRITE | _FLAG_WRITE_NO_RESPONSE,
   )
   _PIANO_SERVICE = (
       _PIANO_UUID,
       (_NOTE_CHAR,),
   )
   
   
   class BLEPiano:
       def __init__(self, ble, name="ble-piano"):
   
           self._ble = ble
           self._ble.active(True)
           self._ble.irq(self._irq)
   
           handles = self._ble.gatts_register_services((_PIANO_SERVICE,))
           # print("Registered handles:", handles)
   
           ((self._handle_note,),) = handles
           self._connections = set()
   
           self._write_callback = None
   
           self._payload = advertising_payload(name=name, services=[_PIANO_UUID])
           self._advertise()
   
       def _irq(self, event, data):
           # Track connections so we can send notifications.
           if event == _IRQ_CENTRAL_CONNECT:
               conn_handle, _, _ = data
               print("New connection", conn_handle)
               self._connections.add(conn_handle)
           elif event == _IRQ_CENTRAL_DISCONNECT:
               conn_handle, _, _ = data
               print("Disconnected", conn_handle)
               self._connections.remove(conn_handle)
               # Start advertising again to allow a new connection.
               self._advertise()
           elif event == _IRQ_GATTS_WRITE:
               conn_handle, value_handle = data
               value = self._ble.gatts_read(value_handle)
               # print("Write event: conn_handle={}, value_handle={}, value={}".format(conn_handle, value_handle, value))
               if value_handle == self._handle_note and self._write_callback:
                   self._write_callback(value)
                   
   
       def is_connected(self):
           return len(self._connections) > 0
   
       def _advertise(self, interval_us=500000):
           print("Starting advertising")
           self._ble.gap_advertise(interval_us, adv_data=self._payload)
   
       def on_write(self, callback):
           self._write_callback = callback
   
   def note_update(data):
       print("Receive:", data)
   
       decoded_data = data.decode('utf-8').rstrip('*\x00')
   
       buzzer.freq(NOTES[decoded_data])
       buzzer.duty_u16(32768)  
       time.sleep(0.15)
       buzzer.duty_u16(0)  
   
   def demo():
       ble = bluetooth.BLE()
       piano = BLEPiano(ble,"pico2w")
   
       while True:
           if piano.is_connected():
               piano.on_write(note_update)
           # time.sleep_ms(100)
   
   if __name__ == "__main__":
       demo()

4. App und Bluetooth-Verbindung
++++++++++++++++++++++++++++++++++++++++++

Stelle sicher, dass die App BLE Piano installiert ist.

#. Aktiviere Bluetooth auf deinem Smartphone.

#. Öffne die App **BLE Piano**.

   .. image:: img/14_app_2.png
      :width: 25%
      :align: center

#. Beim ersten Start erscheinen zwei aufeinanderfolgende Dialoge zur Berechtigungsanfrage. Diese sind notwendig für Bluetooth-Funktionalität.

   .. image:: img/14_app_3.png
      :width: 90%
      :align: center

#. Klicke in der App auf den Button **Connect**, um eine Verbindung per Bluetooth mit dem Pico 2 W herzustellen.

   .. image:: img/14_app_4.png
      :width: 90%
      :align: center

#. Es wird eine Liste aller verfügbaren Bluetooth-Geräte angezeigt. Wähle das Gerät ``xx.xx.xx.xx.xx.xx pico2w`` aus. Jedes Gerät ist mit seiner MAC-Adresse aufgeführt.

   .. image:: img/13_app_5.png
      :width: 60%
      :align: center

#. Falls keine Geräte angezeigt werden, aktiviere die Standortdienste auf deinem Smartphone. (Bei manchen Android-Versionen ist Bluetooth daran gekoppelt.)

#. Nach erfolgreicher Verbindung wirst du zur Hauptansicht weitergeleitet. Durch Tippen auf die Notensymbole kannst du Töne abspielen. Die App sendet die Notendaten an das Pico-Board, das den Summer ansteuert, um den gewünschten Ton zu erzeugen.

   .. image:: img/14_app_7.png
      :width: 90%
      :align: center