.. note:: 

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche gemeinsam mit anderen Technikbegeisterten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum solltest du beitreten?**

    - **Expertenunterstützung**: Erhalte Hilfe von unserer Community und unserem Team bei technischen Herausforderungen und nach dem Kauf auftretenden Problemen.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Profitiere von exklusiven Preisnachlässen auf unsere neuesten Produkte.
    - **Feierliche Aktionen und Gewinnspiele**: Nimm an Sonderaktionen und Verlosungen zu Feiertagen teil.

    👉 Bereit, mit uns zu experimentieren und zu kreieren? Klicke auf [|link_sf_facebook|] und trete noch heute bei!

.. _ar_fade:

2.3 LED-Dimmen mit PWM
==========================

In dieser Lektion lernen wir, wie man mit Pulsweitenmodulation (PWM) die Helligkeit einer LED auf dem Raspberry Pi Pico 2 W steuert. Diese Technik ist eine grundlegende Methode in der Elektronik, die es ermöglicht, Geräte wie LEDs und Motoren mit variabler Intensität zu steuern.

**Was ist PWM?**

**Pulsweitenmodulation (PWM)** ist ein Verfahren zur Steuerung der Leistung, die einem elektronischen Gerät zugeführt wird, indem das Signal mit hoher Frequenz ein- und ausgeschaltet wird. Die "Breite" des Impulses (die Dauer, in der das Signal eingeschaltet ist) bestimmt, wie viel Energie das Gerät erhält.

|img_pwm_duty_cycle|

* **Tastverhältnis (Duty Cycle)**: Der prozentuale Anteil einer Periode, in der das Signal aktiv ist. Ein Tastverhältnis von 100 % bedeutet, dass das Signal durchgehend eingeschaltet ist, während 0 % bedeutet, dass es immer aus ist.
* **Frequenz**: Gibt an, wie oft das Signal pro Sekunde ein- und ausgeschaltet wird.

Durch die Anpassung des Tastverhältnisses kann ein analoges Verhalten mit digitalen Signalen simuliert werden. Wenn eine LED beispielsweise sehr schnell ein- und ausgeschaltet wird, nehmen unsere Augen eine kontinuierliche Helligkeitsänderung wahr.

**Warum PWM verwenden?**

* **Helligkeitsregelung für LEDs**: Sanftes Dimmen von LEDs.
* **Drehzahlsteuerung von Motoren**: Kontrolle der Geschwindigkeit von Gleichstrommotoren.
* **Hohe Effizienz**: PWM ist energieeffizienter als variable Widerstände, da es weniger Energie in Form von Wärme verliert.

**PWM auf dem Raspberry Pi Pico 2 W verstehen**

Der Raspberry Pi Pico 2 W unterstützt PWM auf allen GPIO-Pins. Er verfügt jedoch über 8 PWM-Blöcke (PWM0 bis PWM7), wobei jeder Block über zwei Kanäle (A und B) verfügt, sodass insgesamt 16 unabhängige PWM-Ausgänge verfügbar sind.

|pin_pwm|

.. note::
     Pins, die denselben PWM-Block teilen (z. B. GP0 und GP16), können nicht unterschiedliche Frequenzen haben, wohl aber unterschiedliche Tastverhältnisse.


* :ref:`cpn_led`

**Benötigte Komponenten**

Für dieses Projekt benötigen wir folgende Komponenten. 

Ein vollständiges Kit ist sehr praktisch, hier ist der Link: 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ENTHALTENE TEILE
        - KAUFLINK
    *   - Pico 2 W Starter Kit	
        - 450+
        - |link_pico2w_kit|

Alternativ kannst du die Komponenten auch einzeln kaufen:


.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - KOMPONENTENBESCHREIBUNG	
        - MENGE
        - KAUFLINK

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
        - 1 (220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|

**Schaltplan**

|sch_led|


**Verdrahtung**


|wiring_led|


**Den Code schreiben**


.. note::

    * Öffne die Datei ``2.3_fading_led.ino`` im Pfad ``pico-2w-kit-main/arduino/2.3_fading_led``. 
    * Oder kopiere den Code in die **Arduino IDE**.
    * Wähle das Board (Raspberry Pi Pico) und den richtigen Port aus, bevor du auf **Hochladen** klickst.



.. code-block:: Arduino

    const int ledPin = 15; // GPIO-Pin, der mit der LED verbunden ist

    void setup() {
      pinMode(ledPin, OUTPUT); // GPIO-Pin als Ausgang festlegen
    }

    void loop() {
      // Helligkeit erhöhen
      for (int value = 0; value <= 255; value += 5) {
        analogWrite(ledPin, value); // Helligkeit setzen
        delay(30);                  // 30 Millisekunden warten
      }
      // Helligkeit verringern
      for (int value = 255; value >= 0; value -= 5) {
        analogWrite(ledPin, value);
        delay(30);
      }
    }

Nach dem Hochladen des Codes sollte die LED allmählich heller werden und dann wieder dunkler, wodurch ein sanfter Pulsierungseffekt entsteht.

**Den Code verstehen**

#. Deklaration des LED-Pins:
   
   Ein konstanter Integer ``ledPin`` wird mit dem Wert 15 deklariert, der dem GPIO-Pin 15 entspricht, an den die LED angeschlossen ist.

   .. code-block:: Arduino

        const int ledPin = 15;


#. Einrichtung des Pins:
   
   Die Funktion ``setup()`` wird einmal ausgeführt, sobald das Board eingeschaltet wird. Dabei initialisieren wir ``ledPin`` als Ausgang mit ``pinMode()``.

   .. code-block:: Arduino

        void setup() {
          pinMode(ledPin, OUTPUT);
        }


#. Die Loop-Funktion:
   
    Die ``loop()``-Funktion wird kontinuierlich ausgeführt und enthält zwei ``for``-Schleifen:

     * Helligkeit erhöhen: Beginnt mit ``value = 0`` und erhöht den Wert in Schritten von 5 bis 255.
     * Helligkeit verringern: Beginnt mit value = 255 und reduziert den Wert schrittweise auf 0.
     
   * ``analogWrite()`` sendet ein PWM-Signal an den angegebenen Pin. Der Wert reicht von 0 (immer aus) bis 255 (immer an) und ermöglicht 256 Helligkeitsstufen.
   * ``delay(30);`` verlangsamt die Schleife, damit die Helligkeitsänderung für das menschliche Auge sichtbar wird.

   .. code-block:: Arduino

        void loop() {
          // Helligkeit erhöhen
          for (int value = 0; value <= 255; value += 5) {
            analogWrite(ledPin, value);
            delay(30);
          }
          // Helligkeit verringern
          for (int value = 255; value >= 0; value -= 5) {
            analogWrite(ledPin, value);
            delay(30);
          }
        }


**Zusätzliche Tipps**

* **Experimentiere**: Ändere die Werte für die Inkremente oder die Verzögerung, um den Effekt zu variieren.
* **PWM-Einschränkungen verstehen**: Während alle GPIO-Pins des Pico PWM unterstützen, können Pins desselben PWM-Blocks nicht unterschiedliche Frequenzen haben, wohl aber verschiedene Tastverhältnisse.
* **Sicherheit beachten**: Verwende stets einen Vorwiderstand für die LED, um zu verhindern, dass sie zu viel Strom zieht und beschädigt wird.

**Fazit**

Du hast erfolgreich einen sanften Dimm-Effekt für eine LED mit PWM auf dem Raspberry Pi Pico 2 W erstellt. Dieses Projekt demonstriert, wie PWM zur Simulation analoger Steuerungen mit digitalen Signalen eingesetzt werden kann – ein grundlegendes Konzept in der Mikrocontroller-Programmierung und Elektronik.
