.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein, zusammen mit Gleichgesinnten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unserem Team.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_temp:

2.13 Thermometer
===========================

In dieser Lektion lernen wir, wie man einen **Thermistor** mit dem Raspberry Pi Pico 2 W zur Temperaturmessung verwendet. Ein Thermistor ist eine Art Widerstand, dessen Widerstandswert sich deutlich mit der Temperatur ändert. Speziell werden wir einen Thermistor mit negativem Temperaturkoeffizienten (NTC) verwenden, dessen Widerstand mit steigender Temperatur abnimmt.

* :ref:`cpn_thermistor`


**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Es ist definitiv praktisch, ein ganzes Kit zu kaufen, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name
        - ARTIKEL IN DIESEM KIT
        - KAUF-LINK
    *   - Pico 2 W Starter Kit
        - 450+
        - |link_pico2w_kit|

Sie können sie auch einzeln über die untenstehenden Links kaufen.


.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - KOMPONENTENEINFÜHRUNG
        - MENGE
        - KAUF-LINK

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
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_thermistor`
        - 1
        - |link_thermistor_buy|


**Verständnis des Thermistors**

Ein NTC-Thermistor ist ein temperaturabhängiger Widerstand. Sein Widerstand verringert sich mit steigender Temperatur. Indem wir ihn in einen Spannungsteiler-Schaltkreis einbauen, können wir die Spannung über ihm messen, die sich mit der Temperatur ändert. Mit dem Analog-Digital-Wandler (ADC) des Raspberry Pi Pico 2 W können wir diese Spannung lesen und die entsprechende Temperatur berechnen.

**Schaltplan**

|sch_temp|

In diesem Schaltkreis bilden ein 10K-Widerstand und ein NTC-Thermistor einen Spannungsteiler, wobei GP28 die Spannung über dem Thermistor liest. Der 10K-Widerstand bietet auch Schutz, indem er den Strom begrenzt.

* **Hohe Temperatur**: Der Widerstand des Thermistors verringert sich, senkt seine Spannung und den GP28-Wert. Bei hohen Temperaturen nähert sich der Widerstand dem Nullpunkt, und GP28 liest nahe 0.
* **Niedrige Temperatur**: Der Widerstand des Thermistors steigt, erhöht seine Spannung und den GP28-Wert. Bei extremer Kälte wird der Widerstand fast unendlich, und GP28 liest nahe 1023.

Der 10K-Widerstand stellt sicher, dass 3.3V und GND nicht direkt verbunden sind, um einen Kurzschluss zu verhindern.



**Verdrahtung**


|wiring_temp|
 
.. #. Verbinden Sie 3V3 und GND des Pico 2 W mit der Stromschiene des Breadboards.
.. #. Verbinden Sie ein Ende des Thermistors mit dem GP28-Pin und verbinden Sie dasselbe Ende mit der positiven Stromschiene über einen 10K-Ohm-Widerstand.
.. #. Verbinden Sie das andere Ende des Thermistors mit der negativen Stromschiene.


**Schreiben des Codes**

.. note::

    * Sie können die Datei ``2.13_thermometer.ino`` unter dem Pfad ``pico-2w-kit-main/arduino/2.13_thermometer`` öffnen.
    * Oder kopieren Sie diesen Code in die **Arduino IDE**.
    * Vergessen Sie nicht, das Board (Raspberry Pi Pico) und den richtigen Port vor dem Klicken auf den **Upload** -Button auszuwählen.



.. code-block:: arduino

    // Definieren der Pins
    const int thermistorPin = 28;  // Thermistor an GP28 (ADC2) angeschlossen

    // Konstanten für den Thermistor und Berechnungen
    const float BETA = 3950;       // Beta-Wert des Thermistors (vom Hersteller bereitgestellt)
    const float SERIES_RESISTOR = 10000; // 10KΩ Widerstand
    const float NOMINAL_RESISTANCE = 10000; // Widerstand bei 25°C (vom Hersteller bereitgestellt)
    const float NOMINAL_TEMPERATURE = 25.0; // 25°C in Celsius

    void setup() {
      Serial.begin(115200);  // Serielle Überwachung initialisieren
    }

    void loop() {
      // Den Analogwert vom Thermistor lesen
      int adcValue = analogRead(thermistorPin);
      // Den ADC-Wert in Spannung umwandeln
      float voltage = adcValue * (3.3 / 1023.0);
      // Den Widerstand des Thermistors berechnen
      float resistance = (voltage * SERIES_RESISTOR) / (3.3-voltage);
      // Die Temperatur in Kelvin berechnen mit der Beta-Formel
      float temperatureK = 1 / ( (1 / (NOMINAL_TEMPERATURE + 273.15)) + (1 / BETA) * log(resistance / NOMINAL_RESISTANCE) );
      // Kelvin in Celsius umwandeln
      float temperatureC = temperatureK - 273.15;
      // Celsius in Fahrenheit umwandeln
      float temperatureF = (temperatureC * 9.0 / 5.0) + 32.0;

      // Die Temperaturwerte ausgeben
      Serial.print("Temperature: ");
      Serial.print(temperatureC);
      Serial.print(" °C, ");
      Serial.print(temperatureF);
      Serial.println(" °F");

      delay(1000);  // Eine Sekunde warten vor der nächsten Messung
    }

Wenn der Code läuft und die serielle Überwachung offen ist:

* Sie sollten die Temperaturwerte in Celsius und Fahrenheit sehen.
* Halten Sie den Thermistor sanft zwischen Ihren Fingern. Die Temperaturanzeige sollte steigen, da der Thermistor sich erwärmt.
* Pusten Sie kühle Luft über den Thermistor oder platzieren Sie ein kaltes Objekt in der Nähe. Die Temperaturanzeige sollte sinken.

**Verständnis des Codes**

#. Definieren der Pins und Konstanten:

   Weist den GPIO-Pin zu, der zum Lesen des Thermistors verwendet wird.

   .. code-block:: arduino

        const int thermistorPin = 28;  // Thermistor an GP28 (ADC2) angeschlossen

#. Konstanten für Berechnungen:

   Diese Konstanten werden in den Berechnungen zur Bestimmung der Temperatur verwendet.

   .. code-block:: arduino

        const float BETA = 3950;       // Beta-Wert des Thermistors
        const float SERIES_RESISTOR = 10000; // 10KΩ Widerstand
        const float NOMINAL_RESISTANCE = 10000; // Widerstand bei 25°C
        const float NOMINAL_TEMPERATURE = 25.0; // 25°C in Celsius

#. Lesen des Analogwerts:

   Liest die analoge Spannung am thermistorPin und gibt einen Wert zwischen 0 und 1023 zurück.

   .. code-block:: arduino

        int adcValue = analogRead(thermistorPin);

#. Berechnen der Spannung:

   Wandelt den ADC-Wert in die tatsächliche Spannung um.

   .. code-block:: arduino

        float voltage = adcValue * (3.3 / 1023.0);

#. Berechnen des Thermistorwiderstands:

   Verwendet die Formel des Spannungsteilers, um den Widerstand des Thermistors zu berechnen.

   .. code-block:: arduino

        float resistance = (voltage * SERIES_RESISTOR) / (3.3-voltage);

#. Berechnen der Temperatur:

   .. code-block:: arduino

        float temperatureK = 1 / ( (1 / (NOMINAL_TEMPERATURE + 273.15)) + (1 / BETA) * log(resistance / NOMINAL_RESISTANCE) );
        float temperatureC = temperatureK - 273.15;
        float temperatureF = (temperatureC * 9.0 / 5.0) + 32.0;

#. Ausgeben der Temperatur:

   Gibt die Temperatur in Celsius und Fahrenheit auf den Seriellen Monitor aus.

   .. code-block:: arduino

        Serial.print("Temperature: ");
        Serial.print(temperatureC);
        Serial.print(" °C, ");
        Serial.print(temperatureF);
        Serial.println(" °F");

#. Verzögerung:

   Wartet eine Sekunde, bevor die nächste Messung durchgeführt wird.

   .. code-block:: arduino

        delay(1000);

**Verständnis der Temperaturberechnung**

* Steinhart-Hart-Gleichung:

Die Steinhart-Hart-Gleichung bietet ein Modell des Widerstands des Thermistors als Funktion der Temperatur:

|temp_format|

* ``T`` ist die Temperatur des Thermistors in Kelvin.
* ``T0`` ist eine Referenztemperatur, üblicherweise bei 25°C (was 273.15 + 25 in Kelvin ist).
* ``B`` ist der Beta-Parameter des Materials, der Beta-Koeffizient des in diesem Kit verwendeten NTC-Thermistors ist 3950.
* ``R`` ist der gemessene Widerstand.
* ``R0`` ist der Widerstand bei der Referenztemperatur T0, der Widerstand des NTC-Thermistors in diesem Kit bei 25°C beträgt 10 Kilohm.

**Hinweis zur Genauigkeit**

* Thermistoren sind nichtlineare Geräte, und die Beta-Gleichung bietet eine Annäherung.
* Für genauere Temperaturmessungen über einen breiteren Bereich kann die Steinhart-Hart-Gleichung verwendet werden.
* Eine Kalibrierung kann für präzise Anwendungen notwendig sein.

**Weitere Erkundungen**

* Temperaturanzeige auf einem LCD:

  Schließen Sie ein LCD-Display an, um die Temperaturwerte ohne Computer anzuzeigen.

* Datenprotokollierung:

  Zeichnen Sie Temperaturwerte über die Zeit auf, um Umweltveränderungen zu überwachen.

* Temperaturgesteuerte Geräte:

  Verwenden Sie die Temperaturwerte, um einen Ventilator oder Heizgerät zu steuern.

**Fazit**

In dieser Lektion haben Sie gelernt, wie man einen Thermistor mit dem Raspberry Pi Pico zur Temperaturmessung verwendet. Durch das Erstellen eines Spannungsteilers und die Verwendung der Beta-Gleichung konnten Sie analoge Werte lesen, den Widerstand berechnen und die Temperatur in Celsius und Fahrenheit bestimmen.
