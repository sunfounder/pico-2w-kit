    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Vertiefen Sie sich mit anderen Enthusiasten in die Welt von Raspberry Pi, Arduino und ESP32.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unserem Team.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_water:

2.14 Wasserstandserkennung
============================

In dieser Lektion werden wir lernen, wie man einen **Wassersensor** mit dem Raspberry Pi Pico 2 W verwendet, um die Anwesenheit von Wasser zu erkennen oder den Wasserstand zu messen. Dieser Sensor wird häufig in Projekten zur Regenfallerkennung, Wasserstandsüberwachung und zur Warnung bei Flüssigkeitslecks eingesetzt.

**Funktionsweise des Wassersensors**

Der Wassersensor verfügt über eine Reihe von freiliegenden parallelen Drahtspuren, die Wassertröpfchen erkennen oder das Volumen von Wasser messen. Wenn Wasser mit diesen Spuren in Kontakt kommt, gibt der Sensor ein analoges Signal aus. Je mehr Wasser mit dem Sensor in Kontakt kommt, desto höher ist der Ausgabewert, der vom Analog-Digital-Umsetzer (ADC) des Raspberry Pi Pico 2 W gelesen werden kann.

|img_water_sensor|

* Tauchen Sie den Sensor nicht vollständig in Wasser ein. Nur der Bereich mit den freiliegenden Spuren sollte mit Wasser in Kontakt kommen.
* Die Verwendung des Sensors in einer feuchten Umgebung bei eingeschaltetem Zustand kann dazu führen, dass die Sonde schneller korrodiert, daher wird empfohlen, den Sensor nur bei der Messung einzuschalten.

* :ref:`cpn_water_level`

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
        - :ref:`cpn_water_level`
        - 1
        - 

**Schaltplan**

|sch_water|


**Verdrahtung**

|wiring_water|

**Code**

.. note::

    * Sie können die Datei ``2.14_feel_the_water_level.ino`` unter dem Pfad ``pico-2w-kit-main/arduino/2.14_feel_the_water_level`` öffnen.
    * Oder kopieren Sie diesen Code in die **Arduino IDE**.
    * Vergessen Sie nicht, das Board (Raspberry Pi Pico) und den richtigen Port vor dem Klicken auf den **Upload**-Button auszuwählen.


.. code-block:: arduino

   const int waterSensorPin = 28;  // Wassersensor an GP28 (ADC2) angeschlossen

   void setup() {
     Serial.begin(115200);  // Serielle Überwachung initialisieren
   }

   void loop() {
     // Den analogen Wert vom Wassersensor lesen
     int sensorValue = analogRead(waterSensorPin);
     // Den Sensorwert auf dem seriellen Monitor ausgeben
     Serial.print("Water Sensor Value: ");
     Serial.println(sensorValue);
     delay(500);  // Eine halbe Sekunde warten, bevor erneut gelesen wird
   }

Nach dem Hochladen des Codes, öffnen Sie den seriellen Monitor und Sie sollten eine Reihe von Zahlen sehen, die die analogen Werte vom Wassersensor darstellen.

* Die Sensorwerte sollten niedrig (nahe 0) sein, wenn der Sensor trocken ist.
* Tauchen Sie den Sensor vorsichtig ins Wasser, beginnend von unten. Je mehr von den Spuren des Sensors untergetaucht sind, desto höher sollten die Sensorwerte steigen.

**Verständnis des Codes**

#. Definition des Sensorpins:

   Weist ``waterSensorPin`` GPIO 28 zu, der mit dem analogen Eingang verbunden ist.

   .. code-block:: arduino

      const int waterSensorPin = 28;  // Wassersensor an GP28 (ADC2) angeschlossen


#. Initialisierung der seriellen Kommunikation:

   Startet die serielle Kommunikation, um Nachrichten auf den seriellen Monitor zu senden.

   .. code-block:: arduino

      Serial.begin(115200);

#. Lesen des analogen Werts:

   Liest die analoge Spannung am ``waterSensorPin`` und gibt einen Wert zwischen 0 und 1023 zurück (für 10-Bit-ADC).

   .. code-block:: arduino

      int sensorValue = analogRead(waterSensorPin);

#. Ausgeben des Sensorwerts:

   Gibt den Sensorwert auf dem seriellen Monitor aus.

   .. code-block:: arduino

      Serial.print("Water Sensor Value: ");
      Serial.println(sensorValue);

#. Hinzufügen einer Verzögerung:

   Wartet 500 Millisekunden, bevor die nächste Ablesung erfolgt.

   .. code-block:: arduino

      delay(500);


**Verwendung des Wassersensors als digitaler Sensor**

Sie können das analoge Eingabemodul als digitalen Sensor verwenden, indem Sie einen Schwellenwert festlegen.

* Schwellenwert bestimmen:

  * Lesen Sie den Sensorwert, wenn der Sensor trocken ist.
  * Verwenden Sie diesen Wert als Basislinie (z. B., wenn der trockene Wert etwa 100 beträgt).

* Ändern des Codes:

   .. code-block:: arduino

      const int waterSensorPin = 28;  // Wassersensor an GP28 (ADC2) angeschlossen
      const int threshold = 500;      // Schwellenwert festlegen

      void setup() {
        Serial.begin(115200);  // Serielle Überwachung initialisieren
      }

      void loop() {
        // Den analogen Wert vom Wassersensor lesen
        int sensorValue = analogRead(waterSensorPin);

        // Überprüfen, ob der Sensorwert den Schwellenwert überschreitet
        if (sensorValue > threshold) {
          Serial.println("Water Detected!");
        } else {
          Serial.println("No Water Detected.");
        }
        delay(500);  // Eine halbe Sekunde warten, bevor erneut gelesen wird
      }

Platzieren Sie den Sensor in der Nähe eines potenziellen Leckagebereichs.
Wenn Wasser mit dem Sensor in Kontakt kommt, sollte der serielle Monitor "Wasser erkannt!" anzeigen.

**Sicherheitsvorkehrungen**

* Kurzschlüsse vermeiden:

  * Stellen Sie sicher, dass die Verbindungen sicher sind und dass der Sensor nicht über die freiliegenden Spuren hinaus untergetaucht ist.
  * Lassen Sie nicht zu, dass Wasser mit dem Pico oder anderen elektronischen Komponenten in Kontakt kommt.

* Korrosionsschutz:

  * Lassen Sie den Sensor nicht eingeschaltet, während er für längere Zeit untergetaucht ist.
  * Trocknen Sie den Sensor nach Gebrauch gründlich ab, um Korrosion zu verhindern.


**Weiterführende Untersuchungen**

* Wasserstandsalarm:

  Fügen Sie einen Summer oder eine LED hinzu, um zu alarmieren, wenn Wasser erkannt wird.

* Automatisierte Pumpensteuerung:

  Verwenden Sie den Sensor, um eine Pumpe zu steuern, die je nach Wasserstand ein- oder ausgeschaltet wird.

* Datenprotokollierung:

  Zeichnen Sie Änderungen des Wasserstands über die Zeit auf zur Analyse.

**Fazit**

In dieser Lektion haben Sie gelernt, wie man einen Wassersensor mit dem Raspberry Pi Pico verwendet, um die Anwesenheit von Wasser zu erkennen oder den Wasserstand zu messen. Durch das Lesen der analogen Werte des Sensors können Sie Änderungen im Wasserstand überwachen und entsprechend in Ihren Projekten reagieren.
