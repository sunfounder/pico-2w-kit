.. note:: 

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein und tausche dich mit anderen Enthusiasten aus.

    **Warum beitreten?**

    - **Expertenunterstützung**: Löse nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Sonderrabatte**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nimm an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke [|link_sf_facebook|] und tritt noch heute bei!

.. _py_iot_read_ble:

8.12 Daten vom Bluetooth empfangen
=====================================

In diesem Projekt fungiert der Pico 2 W als Peripheriegerät in einem Bluetooth Low Energy (BLE) Netzwerk. Er bietet einen benutzerdefinierten BLE-Dienst zur Steuerung eines LED-basierten Ampelsystems. Dieser Dienst umfasst eine schreibbare Eigenschaft, die es einem zentralen Gerät, wie einem Smartphone oder Computer, ermöglicht, Befehle zu senden. Das Pico-Board verarbeitet diese Befehle, um die roten, gelben oder grünen LEDs umzuschalten und somit den Betrieb einer Ampel zu simulieren. Debugging-Informationen, einschließlich empfangener Befehle, werden im seriellen Monitor angezeigt, um die Entwicklung zu unterstützen.

Die an Bord befindliche LED zeigt den Verbindungsstatus an: Sie leuchtet, wenn sich ein zentrales Gerät verbunden hat, und erlischt, wenn die Verbindung verloren geht.

1. Schaltkreis aufbauen
+++++++++++++++++++++++++++++++++

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten. 

Es ist definitiv praktisch, ein komplettes Kit zu kaufen, hier ist der Link:

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
    *   - 3
        - :ref:`cpn_breadboard`
        - 1
        - |link_breadboard_buy|
    *   - 4
        - :ref:`cpn_wire`
        - Mehrere
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_resistor`
        - 3 (220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 3
        - |link_led_buy|



.. image:: img/wiring/8.12_bb.png
   :width: 90%

2. Code hochladen
+++++++++++++++++++++++++++++++++

Kopiere den folgenden Code in deine IDE. Alternativ findest du ihn in unserem Repository unter dem Pfad: ``pico-2w-kit/micropython/iot/8.12-read_from_ble/ble_trafficlight.py``.

Hinweis: Dieser Code hängt von den Dateien ``ble_advertising.py`` und ``ble_simple_peripheral.py`` ab. Stelle sicher, dass du diese auf das Pico-Board hochlädst, bevor du das Skript ausführst.

.. code-block:: python

   # Notwendige Module importieren
   from machine import Pin 
   import bluetooth
   from ble_example.ble_simple_peripheral import BLESimplePeripheral
   
   # Erstelle ein Bluetooth Low Energy (BLE) Objekt
   ble = bluetooth.BLE()
   
   # Erstelle eine Instanz der BLESimplePeripheral-Klasse mit dem BLE-Objekt
   sp = BLESimplePeripheral(ble,"pico2w")
   
   # Erstelle ein Pin-Objekt für die an Bord befindliche LED und konfiguriere es als Ausgang
   led = Pin("LED", Pin.OUT)
   
   red = machine.Pin(13, machine.Pin.OUT)
   yellow = machine.Pin(12, machine.Pin.OUT)
   green = machine.Pin(11, machine.Pin.OUT)
   
   def update_traffic(data):
       
       decoded_data = data.decode('utf-8').rstrip('\r\n')
       
       red.off()
       green.off()
       yellow.off()
       
       if decoded_data == "R" or decoded_data == "r":
           red.on()
       elif decoded_data == "G" or decoded_data == "g":
           green.on()
       elif decoded_data == "Y" or decoded_data == "y":
           yellow.on()
       
   
   # Definiere eine Callback-Funktion zum Behandeln empfangener Daten
   def on_rx(data):
       print("Data received: ", data)  # Print the received data
       
       update_traffic(data)
   
   # Starte eine Endlosschleife
   while True:
       if sp.is_connected():  # Überprüfen, ob eine BLE-Verbindung besteht
           sp.on_write(on_rx)  # Setze die Callback-Funktion für den Empfang von Daten


3. Daten an Bluetooth senden
+++++++++++++++++++++++++++++++++

Um mit den in diesem Code definierten Diensten und Eigenschaften zu interagieren, verwende eine allgemeine Bluetooth® Low Energy Zentral-App, wie zum Beispiel LightBlue (verfügbar für iOS und Android) oder nRF Connect (für Android).

In diesem Abschnitt wird LightBlue als Beispiel verwendet, um zu zeigen, wie du die Funktionen des Pico 2 W über Bluetooth steuern kannst.

a. Installiere LightBlue

   Lade die LightBlue-App aus dem |link_lightblue_apple| (für iOS) oder |link_lightblue_google| (für Android) herunter.

   .. image:: img/lightblue.png
      :width: 90%

b. Pico 2 W verbinden

   Starte LightBlue und erlaube die Standort- und Bluetooth-Berechtigungen, falls du dazu aufgefordert wirst. Auf der Seite **Peripheriegeräte** suche nach „pico“ in der Suchleiste und tippe, um dich mit dem Pico 2 W Gerät zu verbinden.

   .. image:: img/11-1-connect-pico.png
      :width: 60%
      :align: center

c. Daten senden, um das Licht umzuschalten

   Nach der Verbindung zeigt LightBlue detaillierte Informationen über das Pico 2 W Bluetooth-Gerät an. Scrolle nach unten, um den **Dienst (6E400001-B5A3-F393-E0A9-E50E24DCCA9E)** und die **Eigenschaft (6E400002-B5A3-F393-E0A9-E50E24DCCA9E)** zu finden.

   Tippe auf die Eigenschaft 6E400002-B5A3-F393-E0A9-E50E24DCCA9E. Die App zeigt die Eigenschaften dieser Eigenschaft an: sie ist schreibbar.

   .. image:: img/12-2-new.png
      :width: 100%

   Wähle oben rechts **"UTF-8 String"** als Datentyp aus.

   .. image:: img/12-4-new.png
      :width: 100%   

   Klicke auf **"Neuen Wert schreiben"** und gib ``R`` ein. Dieses Zeichen wird über Bluetooth an das Pico-Board gesendet. Das Pico-Board wird das empfangene Zeichen interpretieren und die entsprechenden LEDs steuern:  
   
   - ``r`` schaltet die rote LED ein
   - ``y`` schaltet die gelbe LED ein
   - ``g`` schaltet die grüne LED ein

   .. image:: img/12-6-new.png
      :width: 100%