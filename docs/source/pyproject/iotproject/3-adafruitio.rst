.. note::
    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauche tiefer in die Welt des Raspberry Pi, Arduino und ESP32 ein mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Löse Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Tutorials zur Verbesserung deiner Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalte frühen Zugang zu neuen Produktankündigungen und Einblicke.
    - **Sonderangebote**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nimm an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bist du bereit, mit uns zu erkunden und zu kreieren? Klicke auf [|link_sf_facebook|] und trete heute bei!

.. _py_iot_adafruitio:

8.3 Temperatur- und Feuchtigkeitsüberwachung über @AdafruitIO
====================================================================

In diesem Projekt wirst du Adafruit IO erkunden, eine leistungsstarke und benutzerfreundliche IoT-Plattform. Mit MicroPython verbindet sich dein Raspberry Pi Pico W mit Wi-Fi und integriert sich in Adafruit IO, um seine Echtzeitkommunikations- und Steuerungsfähigkeiten zu demonstrieren.

Das Projekt verwendet einen DHT11-Sensor, der Temperatur und Feuchtigkeit misst und die Daten mithilfe des MQTT-Protokolls an das Adafruit IO-Dashboard sendet. Zusätzlich ermöglicht der Status eines virtuellen Schalters auf dem Dashboard die Fernsteuerung einer LED. Der Code nutzt auch die Adafruit IO REST API während der Einrichtung, um den Zustand der LED mit der Hardware zu synchronisieren und so einen reibungslosen Betrieb zu gewährleisten.

Durch die Kombination von MQTT für den Echtzeitaustausch von Daten und REST-APIs für die Einrichtungssynchronisation bietet dieses Projekt eine hervorragende Einführung in die Konzepte der IoT-Programmierung.

1. Baue den Schaltkreis
+++++++++++++++++++++++++++++++++

**Benötigte Komponenten**

Für dieses Projekt benötigst du die folgenden Komponenten.

Es ist definitiv praktisch, ein ganzes Kit zu kaufen, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name
        - ITEMS IN THIS KIT
        - LINK
    *   - Pico 2 W Starter Kit
        - 450+
        - |link_pico2w_kit|

Du kannst sie auch separat über die unten stehenden Links kaufen.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - COMPONENT
        - QUANTITY
        - LINK

    *   - 1
        - :ref:`cpn_pico_2w`
        - 1
        - |link_pico2w_buy|
    *   - 2
        - Micro USB Cable
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
        - :ref:`cpn_dht11`
        - 1
        - \-

.. image:: img/wiring/8.13_bb.png
   :width: 90%

.. raw:: html

   <br/>

2. Einrichtung des Adafruit IO-Dashboards
+++++++++++++++++++++++++++++++++++++++++++

#. Besuche |link_adafruit_io| und klicke auf **Start for Free**, um ein kostenloses Konto zu erstellen.

   .. image:: img/3-1_get_start.png
      :width: 90%

#. Fülle das Anmeldeformular aus, um dein Konto zu erstellen.

   .. image:: img/3-2_sign_up.png
      :width: 90%

#. Sobald dein Konto erstellt ist, navigiere zurück zu Adafruit IO. Klicke auf **Dashboards**, dann wähle **New Dashboard**.

   .. image:: img/3-3_create_dashboard.png
      :width: 90%

#. Erstelle ein **New Dashboard**.

   .. image:: img/3-4_create_dashboard_2.png
      :width: 75%

#. Betrete das neu erstellte **Dashboard** und erstelle einen neuen Block.

   .. image:: img/3-5_create_block.png
      :width: 90%

   .. image:: img/3-6_create_block_2.png
      :width: 90%

#. Füge einen **Toggle Block** zu deinem Dashboard hinzu.

   .. image:: img/3-7_toggle_block.png
      :width: 90%

#. Erstelle einen neuen Feed für diesen Block. Dieser Feed wird die LED steuern, benenne ihn also LED.

   .. image:: img/3-8_connect_feed.png
      :width: 90%

#. Wähle den **LED**-Feed aus und fahre mit dem nächsten Schritt fort.

   .. image:: img/3-9_connect_feed_2.png
      :width: 90%

#. Vervollständige die Blockeinstellungen (hauptsächlich Blocktitel, Text für Ein und Text für Aus), dann klicke unten rechts auf den **Create block**-Knopf, um fertigzustellen.

   .. image:: img/3-10_create_block_2.png
      :width: 90%

#. Erstelle zwei zusätzliche **Text Blocks**, um Temperatur und Feuchtigkeit anzuzeigen. Für diese Blöcke erstelle Feeds namens **temperature** und **humidity**.

   .. image:: img/3-11_text_block.png
      :width: 90%

   .. image:: img/3-12_connect_feed.png
      :width: 90%

#. Nachdem du die Blöcke erstellt hast, sollte dein Dashboard ähnlich aussehen wie dieses:

   .. image:: img/3-13_connect_feed.png
      :width: 90%

#. Passe das Layout nach Bedarf mit der Option **Edit Layout** an.

   .. image:: img/3-14_edit_layout.png
      :width: 50%

#. Klicke auf **API Key**, um deinen Benutzernamen und API-Schlüssel anzuzeigen. Notiere dir diese Anmeldeinformationen, da sie in deinem Code benötigt werden.

   .. image:: img/3-15_api_key.png
      :width: 90%

   .. image:: img/3-16_api_key.png
      :width: 90%


3. Führe den Code aus
+++++++++++++++++++++++++++++++++

#. Dann verbinde das Pico 2 W-Board mit dem Computer über das USB-Kabel.

#. Öffne die Datei ``8.3_adafruitio.py`` unter dem Pfad ``pico-2w-kit/micropython/iot/8.3_adafruitio``, oder kopiere diesen Code in deine IDE.
      
   .. note::
      Dieser Code hängt von der Datei ``lib/umqtt/simple.mpy`` ab. Stelle sicher, dass du sie auf das Pico-Board hochgeladen hast, bevor du das Skript ausführst.

   .. note::
      Bevor du den Code ausführst, stelle sicher, dass du die Wi-Fi-Anmeldeinformationen und die Adafruit IO-Konfiguration (wie in Schritt 2.13 erwähnt) aktualisiert hast.

   .. code-block:: python
      :emphasize-lines: 10,11,16,17

      import network
      import time
      from umqtt.simple import MQTTClient
      from machine import Pin
      import utime
      import dht
      import urequests
      
      # Wi-Fi-Konfiguration
      SSID = "your_wifi_ssid"            # ändere dies
      PASSWORD = "your_password"         # ändere dies
      
      # Adafruit IO-Konfiguration
      AIO_SERVER = "io.adafruit.com"
      AIO_PORT = 1883
      AIO_USER = "your_name_adafruitIO"  # ändere dies
      AIO_KEY = "aio_xxxxxxxxx"          # ändere dies
      AIO_FEED_HUM = "humidity"
      AIO_FEED_TEMP = "temperature"
      AIO_FEED_LED = "led"
      
      # DHT11 und LED-Konfiguration
      sensor = dht.DHT11(Pin(15))
      led = Pin("LED", Pin.OUT)
      
      # Zeitstempel für periodische Aufgaben
      last_update = time.ticks_ms()
      
      # Verbinde mit Wi-Fi
      def connect_wifi():
         wlan = network.WLAN(network.STA_IF)
         wlan.active(True)
         wlan.connect(SSID, PASSWORD)
         while not wlan.isconnected():
            print("Connecting to WiFi...")
            time.sleep(1)
         print("WiFi Connected:", wlan.ifconfig())
      
      # Behandle empfangene MQTT-Nachrichten
      def message_callback(topic, msg):
         global led
         message = msg.decode()
         print("Received message on topic {}: {}".format(topic, message))
         if message.lower() == "on":
            led.value(1)  # LED einschalten
         elif message.lower() == "off":
            led.value(0)  # LED ausschalten
      
      # Verbinde mit Adafruit IO
      def connect_adafruit():
         client = MQTTClient("pico", AIO_SERVER, AIO_PORT, AIO_USER, AIO_KEY)
         client.set_callback(message_callback)
         client.connect()
         print("Connected to Adafruit IO")
         return client
      
      # Hole den letzten Wert aus einem Feed
      def get_feed_value(feed_name):
         url = f"https://io.adafruit.com/api/v2/{AIO_USER}/feeds/{feed_name}/data/last"
         headers = {"X-AIO-Key": AIO_KEY}
         try:
            response = urequests.get(url, headers=headers)
            if response.status_code == 200:
                  data = response.json()
                  print(f"Feed {feed_name} last value: {data['value']}")
                  return data["value"]
            else:
                  print(f"Failed to get feed value: {response.status_code}")
                  return None
         except Exception as e:
            print("Error fetching feed value:", e)
            return None
      
      # Hauptprogramm
      def main():
         global last_update
      
         connect_wifi()
         client = connect_adafruit()
      
         # Abonnieren des LED-Feeds
         led_topic = f"{AIO_USER}/feeds/{AIO_FEED_LED}"
         client.subscribe(led_topic)
         print(f"Subscribed to {led_topic}")
      
         # Anfänglichen LED-Zustand synchronisieren
         led_state = get_feed_value(AIO_FEED_LED)
         if led_state:
            if led_state.lower() == "on":
                  led.value(1)
            elif led_state.lower() == "off":
                  led.value(0)
      
         while True:
            # Überprüfe neue MQTT-Nachrichten
            client.check_msg()
      
            # DHT11-Daten alle 10 Sekunden aktualisieren
            if time.ticks_diff(time.ticks_ms(), last_update) > 10000:
                  try:
                     sensor.measure()
                     temperature = str(sensor.temperature)  # Temperatur
                     humidity = str(sensor.humidity)        # Feuchtigkeit
      
                     print("Temperature: {}C   Humidity: {}%".format(temperature, humidity))
      
                     # Daten an Adafruit IO senden
                     client.publish(f"{AIO_USER}/feeds/{AIO_FEED_TEMP}", temperature)
                     client.publish(f"{AIO_USER}/feeds/{AIO_FEED_HUM}", humidity)
      
                     last_update = time.ticks_ms()  # Zeitstempel aktualisieren
                  except Exception as e:
                     print("Error:", e)
      
      try:
         main()
      except Exception as e:
         print("Error:", e)

#. Sobald der Code erfolgreich auf das Pico gespeichert und ausgeführt wurde, siehst du die folgende Nachricht im seriellen Monitor, die eine erfolgreiche Kommunikation mit Adafruit IO bestätigt.
   
   .. image:: img/3-17_micropython.png
      :width: 90%

#. Navigiere zurück zu Adafruit IO. Du kannst jetzt die Temperatur- und Feuchtigkeitswerte auf dem Dashboard anzeigen oder den LED-Umschalter verwenden, um den Ein-/Ausschaltzustand der externen LED, die mit dem Schaltkreis verbunden ist, zu steuern.

   .. image:: img/3-18_adafruitio.png
      :width: 90%