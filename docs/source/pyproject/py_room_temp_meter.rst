.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in Raspberry Pi, Arduino und ESP32 ein mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Löse Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unserem Team.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Promotionen und Giveaways**: Nimm an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt heute bei!

.. _py_room_temp:

7.2 Bau eines Raumtemperaturmessgeräts
============================================================

In diesem Projekt werden wir ein **Raumtemperaturmessgerät** mit einem Thermistor und einem I2C LCD1602 Display bauen. Dieses einfache, aber praktische Gerät wird die Umgebungstemperatur messen und auf dem LCD-Bildschirm anzeigen, was Echtzeit-Temperaturmessungen deiner Umgebung liefert.

:ref:`py_temp`

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
        - Micro USB-Kabel
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
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_thermistor`
        - 1
        - |link_thermistor_buy|
    *   - 7
        - :ref:`cpn_i2c_lcd`
        - 1
        - |link_i2clcd1602_buy|

**Verständnis der Komponenten**

* **Thermistor:** Ein Typ Widerstand, dessen Widerstand sich mit der Temperatur deutlich verändert. Wir verwenden einen NTC-Thermistor (Negative Temperature Coefficient), dessen Widerstand mit steigender Temperatur sinkt.
* **Spannungsteiler:** Durch die Kombination des Thermistors mit einem festen Widerstand erstellen wir einen Spannungsteiler, der es uns ermöglicht, Spannungsänderungen entsprechend den Temperaturänderungen zu messen.
* **I2C LCD1602 Display:** Ein 16x2 Zeichen LCD-Display mit einer I2C-Schnittstelle, die die Verdrahtung und den Code durch die Verwendung von nur zwei Datenleitungen (SDA und SCL) vereinfacht.

**Schaltplan**

|sch_room_temp|


**Verdrahtung**

|wiring_room_temp|

**Programmierung**

Wir werden ein MicroPython-Programm schreiben, das die Temperatur vom Thermistor liest und auf dem LCD anzeigt.

.. note::

    * Öffne die ``7.2_room_temperature_meter.py`` aus ``pico-2w-kit-main/micropython`` oder kopiere den Code in Thonny, dann klicke auf "Ausführen" oder drücke F5.
    * Stelle sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx. 
    * Hier benötigst du die Bibliothek ``lcd1602.py``, überprüfe bitte, ob sie auf den Pico hochgeladen wurde, für eine detaillierte Anleitung siehe :ref:`add_libraries_py`.


.. code-block:: python

    from lcd1602 import LCD
    from machine import I2C, Pin, ADC
    import utime
    import math

    # Initialisiere den Thermistor (ADC an Pin 28)
    thermistor = ADC(28)  # Analogeingang vom Thermistor

    # Initialisiere die I2C-Kommunikation für das LCD1602 Display
    i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=400000)

    # Erstelle ein LCD-Objekt, um das LCD1602 Display zu steuern
    lcd = LCD(i2c)

    # Konstanten für die Steinhart-Hart-Gleichung
    BETA = 3950  # Beta-Koeffizient des Thermistors
    R0 = 10000   # Widerstand bei 25 Grad Celsius
    T0 = 298.15  # Referenztemperatur in Kelvin (25°C)

    def read_temperature():
        # Lese den rohen ADC-Wert vom Thermistor
        adc_value = thermistor.read_u16()

        # Wandle den rohen ADC-Wert in Spannung um
        voltage = adc_value * 3.3 / 65535

        # Berechne den Widerstand des Thermistors
        Rt = (voltage * R0) / (3.3 - voltage)

        # Wende die Steinhart-Hart-Gleichung an, um die Temperatur in Kelvin zu berechnen
        tempK = 1 / ((1 / T0) + (1 / BETA) * math.log(Rt / R0))

        # Wandle die Temperatur von Kelvin in Celsius um
        tempC = tempK - 273.15

        return tempC

    def main():
        while True:
            temperature = read_temperature()
            # Formatiere die Temperatur auf zwei Dezimalstellen
            temp_str = "{:.2f} C".format(temperature)

            # Zeige die Temperatur auf dem LCD an
            lcd.clear()
            lcd.write(0, 0, "Room Temp:")
            lcd.write(4, 1, temp_str)

            # Optional: Gib die Temperatur in der Konsole aus
            print("Temperature:", temp_str)

            utime.sleep(1)

    if __name__ == "__main__":
        main()

Sobald das Programm läuft, sollte das LCD die aktuelle Raumtemperatur in Celsius anzeigen.
Wenn das LCD leer ist, justiere den Kontrast mit dem Potentiometer auf der Rückseite.
Die Konsole in Thonny wird auch die Temperaturmessungen ausgeben.

**Verständnis des Codes**

#. Imports und Initialisierung:

   * ``lcd1602.LCD``: Zur Steuerung des LCD-Displays.
   * ``machine.ADC``: Zum Lesen analoger Werte vom Thermistor.
   * ``math``: Für logarithmische Berechnungen, die für die Temperaturumrechnung benötigt werden.

#. Variablen:

   * **BETA**: Der Beta-Koeffizient, spezifisch für deinen Thermistor (häufig 3950).
   * **R0**: Der Widerstand des Thermistors bei der Referenztemperatur (üblicherweise 10kΩ bei 25°C).
   * **T0**: Die Referenztemperatur in Kelvin (25°C + 273.15).

   .. code-block:: python

        BETA = 3950  # Beta-Koeffizient des Thermistors
        R0 = 10000   # Widerstand bei 25 Grad Celsius
        T0 = 298.15  # Referenztemperatur in Kelvin (25°C)
    
#. Temperatur lesen (``read_temperature Function``):

   * **ADC-Lesung**: Erfasst den analogen Wert vom Thermistor.
   * **Spannungsberechnung**: Wandelt den ADC-Wert in eine tatsächliche Spannung um.
   * **Widerstandsberechnung (Rt)**: Berechnet den Widerstand des Thermistors mit der Spannungsteilerformel.
   * **Steinhart-Hart-Gleichung**: Ein mathematisches Modell, das den Widerstand eines Thermistors mit seiner Temperatur in Verbindung setzt.
   * **Umrechnung in Celsius**: Passt die Temperatur von Kelvin auf Celsius an.

   .. code-block:: python

        def read_temperature():
                # Lese rohen ADC-Wert vom Thermistor
                adc_value = thermistor.read_u16()

                # Wandle den rohen ADC-Wert in Spannung um
                voltage = adc_value * 3.3 / 65535

                # Berechne den Widerstand des Thermistors
                Rt = (voltage * R0) / (3.3 - voltage)

                # Wende die Steinhart-Hart-Gleichung an, um die Temperatur in Kelvin zu berechnen
                tempK = 1 / ((1 / T0) + (1 / BETA) * math.log(Rt / R0))

                # Wandle die Temperatur von Kelvin in Celsius um
                tempC = tempK - 273.15

                return tempC

#. Hauptschleife (main Funktion): 

   * Liest kontinuierlich die Temperatur.
   * Formatiert und zeigt die Temperatur auf dem LCD an.
   * Gibt die Temperatur optional zur Fehlersuche auf der Konsole aus.
   * Wartet 1 Sekunde, bevor die Schleife wiederholt wird.

   .. code-block:: python

        def main():
            while True:
                temperature = read_temperature()
                # Formatiere die Temperatur auf zwei Dezimalstellen
                temp_str = "{:.2f} C".format(temperature)

                # Zeige die Temperatur auf dem LCD an
                lcd.clear()
                lcd.write(0, 0, "Room Temp:")
                lcd.write(4, 1, temp_str)

                # Optional: Gib die Temperatur auf der Konsole aus
                print("Temperature:", temp_str)

                utime.sleep(1)


**Fehlerbehebung**

* LCD zeigt keinen Text an:

  * Überprüfe die SDA- und SCL-Anschlüsse (GP6 und GP7).
  * Stelle sicher, dass das LCD korrekt mit Strom versorgt wird.
  * Justiere das Kontrastpotentiometer am LCD-Modul.

* Falsche Temperaturanzeige:

  * Stelle sicher, dass der Thermistor und der Widerstand korrekt verbunden sind.
  * Überprüfe die Widerstandswerte erneut.
  * Bestätige, dass der BETA-Wert den Spezifikationen deines Thermistors entspricht.

* Programmfehler:

  * Stelle sicher, dass alle notwendigen Bibliotheken korrekt auf den Pico hochgeladen wurden.
  * Überprüfe auf Tippfehler oder Einrückungsfehler im Code.

**Weiteres Experimentieren**

* Temperaturanzeige in Fahrenheit:

  Modifiziere die Funktion read_temperature, um Celsius in Fahrenheit umzurechnen: ``tempF = (tempC * 9 / 5) + 32``.

* Feuchtigkeitsmessung hinzufügen:

  Integriere einen DHT11 oder DHT22 Sensor, um neben der Temperatur auch die Luftfeuchtigkeit anzuzeigen.

* Datenprotokollierung:

  Speichere Temperaturmessungen über die Zeit in einer Datei auf dem Pico. Analysiere die Daten später am Computer.

* Visuelle Alarme:

  Füge LEDs oder einen Summer hinzu, um zu alarmieren, wenn die Temperatur bestimmte Schwellenwerte überschreitet.

**Verständnis der Wissenschaft**

* Thermistoren und Temperaturmessung:

  * Thermistoren sind empfindlich gegenüber Temperaturänderungen und daher ideal für präzise Messungen.
  * Der Spannungsteiler wandelt Widerstandsänderungen in Spannungsänderungen um, die vom ADC des Pico gelesen werden können.

* Steinhart-Hart-Gleichung:

  * Bietet eine genauere Temperaturberechnung als eine einfache lineare Annäherung.
  * Wesentlich für Anwendungen, die präzise Temperaturmessungen erfordern.

**Fazit**

Herzlichen Glückwunsch! Du hast erfolgreich ein funktionales Raumtemperaturmessgerät mit dem Raspberry Pi Pico 2 W gebaut. Dieses Projekt demonstriert nicht nur, wie man analoge Sensoren und I2C-Geräte anbindet, sondern bietet auch praktische Erfahrung mit Temperaturmessung und Anzeigetechnologien.

Fühle dich frei, dein Temperaturmessgerät durch Hinzufügen neuer Funktionen oder die Integration anderer Sensoren zu erweitern. Dieses Projekt dient als solide Grundlage für die Erforschung von Umweltüberwachungs- und Steuerungssystemen.
