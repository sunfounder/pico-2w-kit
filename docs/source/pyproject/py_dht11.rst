.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche gemeinsam mit anderen Technikbegeisterten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum beitreten?**

    - **Expertenhilfe**: Erhalte Unterstützung bei Problemen nach dem Kauf und technischen Herausforderungen durch unsere Community und unser Team.
    - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und Einblicken.
    - **Sonderrabatte**: Profitiere von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festliche Aktionen & Verlosungen**: Nimm an Gewinnspielen und saisonalen Aktionen teil.

    👉 Bereit, mit uns zu entdecken und zu entwickeln? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _py_dht11:

6.2 Temperatur und Luftfeuchtigkeit mit dem DHT11 messen
===========================================================

In dieser Lektion lernen wir, wie man den **DHT11 Temperatur- und Feuchtigkeitssensor** mit dem Raspberry Pi Pico 2 W verwendet. Der DHT11 ist ein einfacher, kostengünstiger digitaler Sensor, der die Umgebungstemperatur und -feuchtigkeit misst und ein kalibriertes digitales Ausgangssignal liefert.

|img_Dht11|

* :ref:`cpn_dht11`

**Benötigte Komponenten**

Für dieses Projekt werden folgende Bauteile benötigt:

Ein Komplett-Kit ist besonders praktisch – hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name
        - ENTHALTENE TEILE
        - LINK
    *   - Pico 2 W Starter Kit
        - 450+
        - |link_pico2w_kit|

Du kannst die Komponenten auch einzeln über die folgenden Links erwerben:


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
        - :ref:`cpn_dht11`
        - 1
        - |link_dht22_buy|

**Funktionsweise des DHT11-Sensors**

Der **DHT11** verwendet einen kapazitiven Feuchtigkeitssensor und einen Thermistor, um die Umgebungsluft zu messen. Er gibt ein digitales Signal über den Datenpin aus. Die Nutzung ist relativ einfach, allerdings erfordert das Auslesen eine präzise Zeitsteuerung.

* Temperaturbereich: 0–50 °C mit ±2 °C Genauigkeit
* Luftfeuchtigkeitsbereich: 20–80 % r.F. mit ±5 % Genauigkeit
* Abtastrate: 1 Hz (einmal pro Sekunde)

**Schaltplan**

|sch_dht11|


**Verdrahtung**


|wiring_dht11|

**Code schreiben**

Wir schreiben ein MicroPython-Programm, um Temperatur- und Feuchtigkeitswerte vom DHT11 auszulesen.

.. note::

    * Öffne die Datei ``6.2_temperature_humidity.py`` aus ``pico-2w-kit-main/micropython`` oder kopiere den Code in Thonny und klicke auf „Run“ bzw. drücke F5.

    * Stelle sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico) COMxx.

    * Du benötigst die Bibliothek ``dht.py`` – prüfe, ob sie auf den Pico hochgeladen wurde. Eine detaillierte Anleitung findest du unter :ref:`add_libraries_py`.

.. code-block:: python

   from machine import Pin
   import utime
   import dht

   # DHT11-Sensor initialisieren
   sensor = dht.DHT11(Pin(16))

   while True:
      try:
         # Messung auslösen
         sensor.measure()
         # Werte auslesen
         temperature = sensor.temperature  # In Grad Celsius
         humidity = sensor.humidity        # In Prozent
         # Werte ausgeben
         print("Temperature: {}°C   Humidity: {}%".format(temperature, humidity))
      except OSError as e:
         print("Failed to read sensor.")
      # Warten bis zur nächsten Messung
      utime.sleep(2)

Sobald der Code läuft, werden die Temperatur- und Feuchtigkeitswerte in der Thonny-Shell angezeigt.

.. code-block::

  Temperature: 29.3°C   Humidity: 60.0%
  Temperature: 29.2°C   Humidity: 60.0%
  Temperature: 29.2°C   Humidity: 60.0%
  Temperature: 29.1°C   Humidity: 60.0%
  Temperature: 29.2°C   Humidity: 60.0%
  Temperature: 29.3°C   Humidity: 60.0%

**Den Code verstehen**

#. Module importieren:

   * ``machine.Pin``: Zur Steuerung der GPIO-Pins.
   * ``utime``: Enthält zeitbezogene Funktionen.
   * ``dht``: Bibliothek für DHT-Sensoren.

#. Sensor initialisieren:

   .. code-block:: python

      sensor = dht.DHT11(Pin(16))
      Erstellt eine Instanz des DHT11-Sensors an Pin GP16.

#. Hauptschleife:

   * ``sensor.measure()``: Startet eine neue Messung.
   * ``sensor.temperature``: Liest die Temperatur in Grad Celsius.
   * ``sensor.humidity``: Liest die relative Luftfeuchtigkeit in Prozent.
   * ``Exception Handling``: Fängt mögliche Lesefehler ab.
   * ``utime.sleep(2)``: Wartet 2 Sekunden bis zur nächsten Messung.

   .. code-block:: python

      while True:
         try:
            sensor.measure()
            temperature = sensor.temperature
            humidity = sensor.humidity
            print("Temperature: {}°C   Humidity: {}%".format(temperature, humidity))
         except OSError as e:
            print("Failed to read sensor.")
         utime.sleep(2)

**Weitere Experimente**

* Temperatur in Fahrenheit umrechnen:

   .. code-block:: python

      temperature_f = temperature * 9 / 5 + 32
      print("Temperature: {}°F   Humidity: {}%".format(temperature_f, humidity))

* Werte auf einem LCD anzeigen:

  Integriere ein LCD-Display, um die Werte ohne PC anzuzeigen.


* Warnungen einrichten:

  Verwende eine LED oder einen Summer, um bei zu hoher Temperatur oder Luftfeuchtigkeit eine Warnung auszugeben.

**Fehlersuche**

* Falsche Messwerte:

  * Stelle sicher, dass der Sensor korrekt angeschlossen ist.
  * Überprüfe auf lockere oder fehlerhafte Verbindungen.

* Sensor lässt sich nicht auslesen:

  Kann gelegentlich durch Timing-Probleme auftreten – der Code nutzt try-except, um solche Fehler abzufangen.

* Pull-Up-Widerstand:

  Falls der Sensor nicht funktioniert, überprüfe, ob ein Pull-Up-Widerstand zwischen VCC und Datenleitung vorhanden ist, sofern dein Sensor dies benötigt.

**Fazit**

In dieser Lektion hast du gelernt, wie man den DHT11 Temperatur- und Feuchtigkeitssensor mit dem Raspberry Pi Pico 2 verwendet. Die Überwachung von Umgebungsbedingungen ist ein grundlegender Bestandteil vieler Projekte – von Wetterstationen bis hin zu Hausautomatisierungssystemen.

* `Try Statement - Python Docs <https://docs.python.org/3/reference/compound_stmts.html?#the-try-statement>`_
