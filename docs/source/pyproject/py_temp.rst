.. note:: 
    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Vertiefe dein Wissen über Raspberry Pi, Arduino und ESP32 zusammen mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Löse Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühen Zugang zu neuen Produktankündigungen und Einblicke.
    - **Spezialrabatte**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nimm an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt heute bei!

.. _py_temp:


2.13 Thermometer
===========================

In dieser Lektion lernen wir, wie man einen **Thermistor** mit dem Raspberry Pi Pico 2 W zur Temperaturmessung verwendet. Ein Thermistor ist ein Widerstand, dessen Widerstandswert sich mit der Temperatur erheblich ändert. Wir verwenden speziell einen NTC-Thermistor, dessen Widerstand mit steigender Temperatur abnimmt.


* :ref:`cpn_thermistor`

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Es ist definitiv praktisch, ein ganzes Kit zu kaufen, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ARTIKEL IN DIESEM KIT
        - LINK
    *   - Pico 2 W Starter Kit	
        - 450+
        - |link_pico2w_kit|

Du kannst sie auch einzeln über die untenstehenden Links kaufen.


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
        - :ref:`cpn_resistor`
        - 1 (10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_thermistor`
        - 1
        - |link_thermistor_buy|


**Verständnis des Thermistors**

Ein NTC-Thermistor ist ein temperaturabhängiger Widerstand. Sein Widerstand verringert sich mit steigender Temperatur. Indem wir ihn in einen Spannungsteiler-Schaltkreis einbauen, können wir die Spannung über ihm messen, die sich mit der Temperatur ändert. Mit dem Analog-Digital-Wandler (ADC) des Raspberry Pi Pico 2 W können wir diese Spannung messen und die entsprechende Temperatur berechnen.

**Schaltbild**

|sch_temp|

In diesem Schaltkreis bilden ein 10K-Widerstand und ein NTC-Thermistor einen Spannungsteiler, wobei GP28 die Spannung über dem Thermistor liest. Der 10K-Widerstand bietet auch Schutz, indem er den Strom begrenzt.

* **Hohe Temperatur**: Der Widerstand des Thermistors sinkt, was seine Spannung und den GP28-Wert verringert. Bei hohen Temperaturen nähert sich der Widerstand Null und GP28 liest nahezu 0.
* **Niedrige Temperatur**: Der Widerstand des Thermistors steigt, was seine Spannung und den GP28-Wert erhöht. Bei extremer Kälte wird der Widerstand nahezu unendlich und GP28 liest nahezu 65535.

Der 10K-Widerstand stellt sicher, dass 3.3V und GND nicht direkt verbunden sind, was einen Kurzschluss verhindert.

**Verdrahtungsdiagramm**

|wiring_temp|

.. #. Verbinde 3V3 und GND des Pico 2 W mit der Stromschiene des Breadboards.
.. #. Verbinde ein Ende des Thermistors mit dem GP28-Pin und verbinde dasselbe Ende mit der positiven Stromschiene über einen 10K-Ohm-Widerstand.
.. #. Verbinde das andere Ende des Thermistors mit der negativen Stromschiene.

.. note::
    * Der Thermistor ist schwarz und mit 103 gekennzeichnet.
    * Der Farbring des 10K-Ohm-Widerstands ist rot, schwarz, schwarz, rot und braun.

**Programmierung**

Wir schreiben ein MicroPython-Programm, um den analogen Wert des Thermistors zu lesen, die Temperatur in Celsius und Fahrenheit zu berechnen und anzuzeigen.

.. note::

    * Öffne die ``2.13_thermometer.py`` aus ``pico-2w-kit-main/micropython`` oder kopiere den Code in Thonny, dann klicke auf "Ausführen" oder drücke F5.

    * Stelle sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx. 

.. code-block:: python

    import machine
    import utime
    import math

    # Konstanten
    BETA = 3950  # Beta-Koeffizient des Thermistors
    T0 = 298.15  # Referenztemperatur (25°C in Kelvin)
    R0 = 10000   # Widerstand bei T0 (10 kΩ)

    # Initialisiere ADC auf GP28
    thermistor = machine.ADC(28)

    while True:
        # Lese den analogen Wert (0-65535)
        analog_value = thermistor.read_u16()

        # Konvertiere den analogen Wert in Spannung
        voltage = analog_value * 3.3 / 65535

        # Berechne den Widerstand des Thermistors
        Rt = (voltage * R0) / (3.3 - voltage)

        # Berechne die Temperatur in Kelvin mit der Beta-Formel
        tempK = 1 / ( (1 / T0) + (1 / BETA) * math.log(Rt / R0) )

        # Konvertiere Kelvin in Celsius
        tempC = tempK - 273.15

        # Konvertiere Celsius in Fahrenheit
        tempF = tempC * 9 / 5 + 32

        # Drucke die Ergebnisse
        print('Temperature: {:.2f}°C  {:.2f}°F'.format(tempC, tempF))

        # Warte vor der nächsten Messung
        utime.sleep(2)

Wenn der Code läuft, zeigt die Konsole die Temperatur in Celsius und Fahrenheit an.

* Versuche, den Thermistor zu berühren, um zu sehen, wie die Temperatur steigt.
* Verwende Eis oder einen kalten Gegenstand, um eine Temperaturabnahme zu beobachten.

**Verständnis des Codes**

#. Importiere Module:

   * ``machine``: Ermöglicht den Zugriff auf hardwarebezogene Funktionen.
   * ``utime``: Ermöglicht die Nutzung von zeitbezogenen Funktionen wie sleep.
   * ``math``: Enthält mathematische Funktionen wie log.

#. Konstanten:

   * ``BETA``: Der Beta-Koeffizient des Thermistors (im Datenblatt angegeben, häufig um 3950).
   * ``T0``: Referenztemperatur in Kelvin (25°C + 273.15).
   * ``R0``: Widerstand des Thermistors bei T0 (10 kΩ).

#. Initialisiere den ADC-Pin:

   * ``thermistor = machine.ADC(28)``: Richtet GP28 als analogen Eingang ein.

#. Hauptschleife:

   * ``analog_value = thermistor.read_u16()``: Liest den rohen analogen Wert.
   * ``voltage = analog_value * 3.3 / 65535``: Konvertiert den rohen Wert in eine Spannung.
   * ``Rt = (voltage * R0) / (3.3 - voltage)``: Verwendet die Spannungsteilerformel, um den Widerstand des Thermistors zu finden.
   * ``tempK = 1 / ( (1 / T0) + (1 / BETA) * math.log(Rt / R0) )``: Verwendet die Steinhart-Hart-Gleichung, vereinfacht für einen einzigen Beta-Wert.
   * Konvertiere Kelvin in Celsius und Fahrenheit:
     
     .. code-block:: python
    
        tempC = tempK - 273.15
        tempF = tempC * 9 / 5 + 32

   * ``print('Temperatur: {:.2f}°C {:.2f}°F'.format(tempC, tempF))``: Drucke die Ergebnisse
   * ``utime.sleep(2)``: Wartet 2 Sekunden vor der nächsten Messung.


**Verständnis der Temperaturberechnung**

* Steinhart-Hart-Gleichung:

Die Steinhart-Hart-Gleichung liefert ein Modell des Widerstands des Thermistors in Abhängigkeit von der Temperatur:

|temp_format|

* ``T`` ist die Temperatur des Thermistors in Kelvin.
* ``T0`` ist eine Referenztemperatur, üblicherweise bei 25°C (was 273.15 + 25 in Kelvin ist).
* ``B`` ist der Beta-Parameter des Materials, der Beta-Koeffizient des in diesem Kit verwendeten NTC-Thermistors beträgt 3950.
* ``R`` ist der gemessene Widerstand.
* ``R0`` ist der Widerstand bei der Referenztemperatur T0, der Widerstand des NTC-Thermistors in diesem Kit bei 25°C beträgt 10 Kilohm.

**Sicherheitshinweis**

Sei vorsichtig beim Erhitzen des Thermistors. Setze ihn keinen hohen Temperaturen aus, die ihn oder den Raspberry Pi Pico 2 beschädigen könnten.

**Weitere Experimente**

* **Datenprotokollierung**: Modifiziere den Code, um Temperaturmessungen auf dem Pico in einer Datei zu protokollieren.
* **Temperaturschwellen**: Füge Bedingungen hinzu, um Aktionen auszulösen, wenn die Temperatur bestimmte Werte über- oder unterschreitet (z.B. eine LED einschalten oder einen Summer aktivieren).
* **Anzeigeausgabe**: Verbinde ein LCD- oder OLED-Display, um die Temperaturmessungen anzuzeigen.

**Fazit**

Durch den Einsatz eines Thermistors mit dem Raspberry Pi Pico 2 W hast du ein grundlegendes Thermometer erstellt, das Temperaturänderungen messen kann. Dieses Projekt demonstriert, wie man analoge Eingänge liest, Berechnungen durchführt und Sensordaten interpretiert, um aussagekräftige Informationen zu gewinnen.
