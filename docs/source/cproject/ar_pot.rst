.. note:: 
   
    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein, zusammen mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unserem Team.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_pot:

2.11 Den Drehregler betätigen
==================================

In dieser Lektion werden wir die Verwendung des eingebauten Analog-Digital-Umsetzers (ADC) des Raspberry Pi Pico 2 W zur Erfassung analoger Eingaben untersuchen und diese Eingaben nutzen, um die Helligkeit einer LED zu steuern. Konkret werden wir ein Potentiometer – einen variablen Widerstand – als analoges Eingabegerät verwenden. Durch Drehen des Knopfes am Potentiometer justieren wir die vom Pico gelesene Spannung, welche dann über die Pulsweitenmodulation (PWM) zur Steuerung der LED-Helligkeit verwendet wird.


**Verständnis für analogen Eingang**

Bisher haben wir mit digitalen Eingängen und Ausgängen gearbeitet, die entweder EIN (hohe Spannung) oder AUS (niedrige Spannung) sind. Viele reale Signale sind jedoch analog, d.h. sie variieren kontinuierlich über einen Bereich von Werten. Beispiele hierfür sind Lichtintensität, Temperatur und Geräuschpegel.

Der Raspberry Pi Pico 2 W verfügt über einen eingebauten ADC, der es ermöglicht, analoge Spannungen zu lesen und in digitale Werte umzuwandeln, die im Code verarbeitet werden können.

Der ADC wandelt die analoge Spannung vom Potentiometer mittels folgender Formel in einen digitalen Wert um:

.. code-block::

  Digitalwert = (Analogspannung / 3.3V) * 1023


**ADC-Pins des Pico**

|pin_adc|

Der Pico hat drei GPIO-Pins, die für analoge Eingaben genutzt werden können:

* **GP26** (ADC0)
* **GP27** (ADC1)
* **GP28** (ADC2)

Zusätzlich gibt es einen vierten ADC-Kanal, der intern mit einem Temperatursensor verbunden ist (ADC4), den wir in späteren Lektionen erkunden werden.


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

Sie können sie auch separat über die untenstehenden Links kaufen.


.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - KOMPONENTEN-EINFÜHRUNG	
        - ANZAHL
        - KAUF-LINK

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
        - 1(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 7
        - :ref:`cpn_potentiometer`
        - 1
        - |link_potentiometer_buy|

**Schaltplan**

|sch_pot|


**Verdrahtung**

|wiring_pot|

**Code**


.. note::

    * Sie können die Datei ``2.11_turn_the_knob.ino`` im Pfad ``pico-2w-kit-main/arduino/2.11_turn_the_knob`` öffnen. 
    * Oder kopieren Sie diesen Code in die **Arduino IDE**.
    * Vergessen Sie nicht, das Board (Raspberry Pi Pico) und den richtigen Port auszuwählen, bevor Sie auf den **Hochladen** -Button klicken.



.. code-block:: Arduino

   // Definieren der Pins
   const int potPin = 28;   // Potentiometer an GP28 (ADC2) angeschlossen
   const int ledPin = 15;   // LED an GP15 angeschlossen (PWM-fähig)

   void setup() {
     // Initialisieren der seriellen Kommunikation zur Fehlerbehebung
     Serial.begin(115200);
     // Einrichten des LED-Pins als Ausgang
     pinMode(ledPin, OUTPUT);
   }

   void loop() {
     // Lesen des analogen Wertes vom Potentiometer (0-1023)
     int sensorValue = analogRead(potPin);
     // Ausgeben des Sensorwertes zur Fehlerbehebung
     Serial.println(sensorValue);

     // Zuordnen des Sensorwertes zu einem PWM-Wert (0-255)
     int brightness = map(sensorValue, 0, 1023, 0, 255);
     // Einstellen der Helligkeit der LED
     analogWrite(ledPin, brightness);

     // Kleine Verzögerung für Stabilität
     delay(10);
   }

Wenn der Code läuft und der Serial Monitor geöffnet ist:

* Wenn Sie den Knopf des Potentiometers drehen, sollte sich die Helligkeit der LED von dunkel zu hell ändern.
* Sie sollten die analogen Werte sehen, die von etwa 0 bis 1023 variieren, wenn Sie das Potentiometer anpassen.

**Verständnis des Codes**

#. Definition der Pins:

   Weist die GPIO-Pins zu, die für das Potentiometer und die LED verwendet werden.

   .. code-block:: Arduino

        const int potPin = 28;   // Potentiometer an GP28 (ADC2) angeschlossen
        const int ledPin = 15;   // LED an GP15 angeschlossen (PWM-fähig)

#. Initialisieren der seriellen Kommunikation:

   Beginnt die serielle Kommunikation, um Nachrichten an den Serial Monitor zu senden.

   .. code-block:: Arduino

        Serial.begin(115200);

#. Lesen des analogen Wertes:

   Liest die analoge Spannung am potPin (GP28) und gibt einen Wert zwischen 0 und 1023 zurück.

   .. code-block:: Arduino

        int sensorValue = analogRead(potPin);

#. Ausgeben des Sensorwertes:

   Gibt den aktuellen Sensorwert zur Fehlerbehebung im Serial Monitor aus.

   .. code-block:: Arduino

        Serial.println(sensorValue);

#. Zuordnen des Sensorwertes:

   Wandelt den Sensorwert (0-1023) in einen Helligkeitswert um, der für die PWM-Ausgabe geeignet ist (0-255).

   .. code-block:: Arduino

        int brightness = map(sensorValue, 0, 1023, 0, 255);

#. Einstellen der LED-Helligkeit:

   Stellt die Helligkeit der LED ein, indem der PWM-Tastgrad am ledPin (GP15) eingestellt wird.

   .. code-block:: Arduino

        analogWrite(ledPin, brightness);

#. Hinzufügen einer kleinen Verzögerung:

   Eine kurze Verzögerung, um die Messwerte zu stabilisieren und zu verhindern, dass die Schleife zu schnell läuft.

   .. code-block:: Arduino

        delay(10);

**Weiterführende Erkundungen**

* **Spannung anzeigen**: Modifizieren Sie den Code, um die tatsächlich gelesene Spannung vom Potentiometer zu berechnen und anzuzeigen.

  .. code-block:: Arduino

        // Definieren der Pins
        const int potPin = 28;  // Potentiometer an GP28 (ADC2) angeschlossen
        const int ledPin = 15;  // LED an GP15 angeschlossen (PWM-fähig)
        
        void setup() {
          // Initialisieren der seriellen Kommunikation zur Fehlerbehebung
          Serial.begin(115200);
          // Einrichten des LED-Pins als Ausgang
          pinMode(ledPin, OUTPUT);
        }
        
        void loop() {
          // Lesen des analogen Wertes vom Potentiometer (0-1023)
          int sensorValue = analogRead(potPin);
        
          // Ausgeben des Sensorwertes zur Fehlerbehebung
          Serial.println(sensorValue);
        
          // Berechnen und anzeigen der tatsächlichen Spannung
          float voltage = sensorValue * (3.3 / 1023.0);
          Serial.print("Spannung: ");
          Serial.print(voltage);
          Serial.println(" V");
        
          // Zuordnen des Sensorwertes zu einem PWM-Wert (0-255)
          int brightness = map(sensorValue, 0, 1023, 0, 255);
          // Einstellen der Helligkeit der LED
          analogWrite(ledPin, brightness);
        
          // Kleine Verzögerung für Stabilität
          delay(10);
        }

* **Mehrere LEDs steuern**: Verwenden Sie mehrere Potentiometer, um verschiedene LEDs oder Farben einer RGB-LED zu steuern.
* **Verwendung mit anderen Sensoren**: Ersetzen Sie das Potentiometer durch einen anderen analogen Sensor, wie z.B. einen lichtabhängigen Widerstand (LDR), um die LED in Abhängigkeit vom Umgebungslicht zu steuern.


**Erläuterung der Konzepte**

* Analog-Digital-Umsetzung (ADC):

  * Der ADC im Pico wandelt die analoge Spannung vom Potentiometer in einen digitalen Wert um.
  * Der Spannungsbereich von 0V bis 3.3V wird in einen numerischen Wert zwischen 0 und 1023 umgewandelt.

* Pulsweitenmodulation (PWM):

  * PWM ist eine Technik, die verwendet wird, um eine analoge Spannung zu simulieren, indem ein digitaler Pin schnell zwischen den Zuständen HOCH und NIEDRIG geschaltet wird.
  * Durch Anpassen des Anteils der Zeit, in der das Signal HOCH ist (Tastverhältnis), können wir Geräte wie LEDs und Motoren steuern.

* Wertezuordnung:

  * Die Funktion ``map()`` skaliert einen Bereich von Werten auf einen anderen.
  * In diesem Fall ordnen wir den Bereich 0-1023 des Potentiometers dem PWM-Bereich 0-255 zu.

**Fazit**

In dieser Lektion haben Sie gelernt, wie man analogen Eingang von einem Potentiometer mit dem ADC des Raspberry Pi Pico liest und diesen Eingang nutzt, um die Helligkeit einer LED über PWM zu steuern. Diese grundlegende Fähigkeit ermöglicht es Ihnen, mit einer Vielzahl von analogen Sensoren zu arbeiten und Ausgänge proportional zu steuern.
