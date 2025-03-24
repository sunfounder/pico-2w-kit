.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein – gemeinsam mit anderen Technikbegeisterten.

    **Warum beitreten?**

    - **Experten-Support**: Erhalte Unterstützung bei technischen Herausforderungen und Problemen nach dem Kauf – direkt von unserer Community und unserem Team.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten weiterzuentwickeln.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Profitiere von exklusiven Vergünstigungen auf unsere neuesten Produkte.
    - **Feiertagsaktionen und Gewinnspiele**: Nimm an Sonderaktionen und Verlosungen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und trete noch heute bei!

.. _ar_74hc_led:

5.1 Verwendung des 74HC595-Schieberegisters
=============================================

In dieser Lektion lernen wir, wie man das **74HC595-Schieberegister** verwendet, um mehrere LEDs mit nur wenigen GPIO-Pins des Raspberry Pi Pico 2 W zu steuern. Der 74HC595 ist eine integrierte Schaltung (IC), die es ermöglicht, die Anzahl der digitalen Ausgänge über eine serielle Eingabe zu erweitern. Dies ist besonders nützlich, wenn viele Ausgänge gesteuert werden sollen, aber nur wenige GPIO-Pins verfügbar sind.

* :ref:`74HC595`

**Benötigte Komponenten**

Für dieses Projekt benötigen wir folgende Komponenten.

Ein komplettes Kit ist besonders praktisch. Hier ist der Link: 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ENTHALTENE TEILE IM KIT
        - KAUFLINK
    *   - Pico 2 W Starter Kit	
        - 450+
        - |link_pico2w_kit|

Alternativ können die Komponenten auch einzeln über die folgenden Links erworben werden.


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
        - 8 (220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 8
        - |link_led_buy|
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|

**Funktionsweise des 74HC595-Schieberegisters**

Der **74HC595** ist ein 8-Bit-Seriell-zu-Parallel-Schieberegister mit Ausgangsspeicherung. Er kann serielle Daten empfangen und diese in parallele Ausgangssignale umwandeln, sodass 8 Ausgänge mit nur 3 GPIO-Pins des Pico gesteuert werden können.

**Wichtige Pins des 74HC595:**

|img_74jc595_pin|

* **DS (Pin 14)**: Serielle Dateneingabe
* **SHCP (Pin 11)**: Schieberegister-Takt-Eingang
* **STCP (Pin 12)**: Speicherregister-Takt-Eingang (Latch-Pin)
* **OE (Pin 13)**: Ausgangsaktivierung (Low-Aktiv, mit GND verbinden)
* **MR (Pin 10)**: Master-Reset (Low-Aktiv, mit 3.3V verbinden)
* **Q0-Q7 (Pins 15, 1-7)**: Parallele Ausgänge
* **VCC (Pin 16)**: Mit 3.3V verbinden
* **GND (Pin 8)**: Mit GND verbinden

**Schaltplan**

|sch_74hc_led|


**Verdrahtung**


|wiring_74hc_led|

**Code schreiben**

Wir schreiben ein Programm, das die LEDs steuert, indem serielle Daten vom Pico an das 74HC595-Schieberegister gesendet werden. Die LEDs leuchten nacheinander in einer Sequenz auf.

.. note::

    * Die Datei ``5.1_microchip_74hc595.ino`` kann unter ``pico-2w-kit-main/arduino/5.1_microchip_74hc595`` geöffnet werden.
    * Alternativ kann der Code in die **Arduino IDE** kopiert werden.
    * Vor dem Hochladen muss das richtige Board (Raspberry Pi Pico) und der **korrekte Port** ausgewählt werden.

.. code-block:: arduino

  // Definiere die Pins für das 74HC595
  const int DS = 0;   // GPIO 0 -> DS (Pin 14)
  const int SHCP = 1; // GPIO 1 -> SHCP (Pin 11)
  const int STCP = 2; // GPIO 2 -> STCP (Pin 12)

  // Array mit binären Mustern zur Steuerung der LEDs
  int datArray[] = {
    0b00000000, // Alle LEDs aus
    0b00000001, // LED 0 an
    0b00000011, // LEDs 0 und 1 an
    0b00000111, // LEDs 0, 1 und 2 an
    0b00001111, // LEDs 0 bis 3 an
    0b00011111, // LEDs 0 bis 4 an
    0b00111111, // LEDs 0 bis 5 an
    0b01111111, // LEDs 0 bis 6 an
    0b11111111  // Alle LEDs an
  };

  void setup() {
    // Initialisiere die Steuerpins als Ausgänge
    pinMode(DS, OUTPUT);
    pinMode(SHCP, OUTPUT);
    pinMode(STCP, OUTPUT);
  }

  void loop() {
    // Durchlaufe jedes Muster im datArray
    for (int num = 0; num < 9; num++) {
      // Bereite das Schieberegister für neue Daten vor
      digitalWrite(STCP, LOW);

      // Übertrage die Daten an das Schieberegister
      shiftOut(DS, SHCP, MSBFIRST, datArray[num]);

      // Latch-Daten an die Ausgangspins
      digitalWrite(STCP, HIGH);

      delay(500); // Warte eine halbe Sekunde vor dem nächsten Muster
    }

    // Schalte alle LEDs nach der Sequenz aus
    digitalWrite(STCP, LOW);
    shiftOut(DS, SHCP, MSBFIRST, 0b00000000);
    digitalWrite(STCP, HIGH);
    delay(500);
  }

Nach dem Hochladen des Codes sollten die an den 74HC595 angeschlossenen LEDs nacheinander aufleuchten, entsprechend den in ``datArray`` definierten Mustern. 
Sobald alle LEDs eingeschaltet sind, werden sie der Reihe nach wieder ausgeschaltet.

**Verständnis des Codes** 

#. Definition der Steuerpins:

   * ``DS (Data Serial Input)``: Empfängt serielle Daten.
   * ``SHCP (Shift Register Clock Input)``: Steuert das Verschieben der Daten in das Register.
   * ``STCP (Storage Register Clock Input)``: Steuert das Speichern der Daten in den Ausgangspins.

   .. code-block:: arduino

      const int DS = 0;   // GPIO 0 -> DS (Pin 14)
      const int SHCP = 1; // GPIO 1 -> SHCP (Pin 11)
      const int STCP = 2; // GPIO 2 -> STCP (Pin 12)

#. Erstellen von Datenmustern:

   * Das Array ``datArray`` enthält verschiedene Binärmuster zur Steuerung der LEDs.
   * Jedes Bit repräsentiert den Zustand einer LED (1 für an, 0 für aus).

   .. code-block:: arduino

      int datArray[] = {
        0b00000000, // Alle LEDs aus
        0b00000001, // LED 0 an
        0b00000011, // LEDs 0 und 1 an
        0b00000111, // LEDs 0, 1 und 2 an
        0b00001111, // LEDs 0 bis 3 an
        0b00011111, // LEDs 0 bis 4 an
        0b00111111, // LEDs 0 bis 5 an
        0b01111111, // LEDs 0 bis 6 an
        0b11111111  // Alle LEDs an
      };
  
#. Setup-Funktion:

   Setzt die Pins ``DS``, ``SHCP`` und ``STCP`` als Ausgänge, um Daten an das Schieberegister zu senden.

   .. code-block:: arduino

      void setup() {
        // Initialisiere die Steuerpins als Ausgänge
        pinMode(DS, OUTPUT);
        pinMode(SHCP, OUTPUT);
        pinMode(STCP, OUTPUT);
      }

#. Loop-Funktion: Die ``for``-Schleife durchläuft jedes Muster im ``datArray``-Array.

   * Datenübertragung:

     * ``shiftOut`` sendet die Daten byteweise, ein Bit nach dem anderen.
     * ``MSBFIRST`` gibt an, dass das höchstwertige Bit zuerst gesendet wird.

     .. code-block:: arduino

        shiftOut(DS, SHCP, MSBFIRST, datArray[num]);

   * Speichern der Daten:

     * ``STCP`` auf ``LOW`` setzen, um das Schieberegister auf neue Daten vorzubereiten.
     * Nach der Übertragung ``STCP`` auf ``HIGH`` setzen, um die Daten in die Ausgangspins zu übernehmen und die LED-Zustände zu aktualisieren.

     .. code-block:: arduino

        digitalWrite(STCP, LOW);
        // shiftOut(...)
        digitalWrite(STCP, HIGH);

   * Verzögerung:
   
     ``delay(500);`` fügt eine halbe Sekunde Pause zwischen jeder Sequenz hinzu, um die Anzeige sichtbar zu machen.

   * Ausschalten der LEDs: 
     
     Nachdem alle Muster durchlaufen wurden, werden alle LEDs ausgeschaltet, indem 0b00000000 gesendet wird.

     .. code-block:: arduino

        digitalWrite(STCP, LOW);
        shiftOut(DS, SHCP, MSBFIRST, 0b00000000);
        digitalWrite(STCP, HIGH);
        delay(500);

**Fehlersuche**

* Keine LEDs leuchten auf:

  * Überprüfe alle Kabelverbindungen.
  * Stelle sicher, dass der 74HC595 korrekt mit Strom versorgt wird.
  * Prüfe, ob die GPIO-Pins des Pico korrekt mit dem Schieberegister verbunden sind.

* Falsches LED-Verhalten:

  * Kontrolliere die Binärmuster in ``datArray``.
  * Vergewissere dich, dass die Widerstände korrekt angeschlossen sind, um den Stromfluss zu begrenzen.

**Erweiterungsmöglichkeiten**

* Steuerung weiterer Geräte:

  Verwende den 74HC595 zur Steuerung von Relais, Motoren oder anderen leistungsstarken Komponenten.

* Schieberegister in Reihe schalten:

  Verbinde mehrere 74HC595-Schieberegister, um mit denselben drei GPIO-Pins noch mehr Ausgänge zu steuern.

* LED-Muster programmieren:

  Entwickle komplexere LED-Animationen und Muster durch Anpassung des datArray.

* Integration mit Sensoren:

  Kombiniere das Schieberegister mit verschiedenen Sensoren, um reaktive und interaktive Systeme zu erstellen.

* Aufbau einer LED-Matrix:

  Nutze mehrere Schieberegister, um eine größere LED-Matrix für Anzeigen oder Beschilderungen zu erstellen.

**Fazit**

In dieser Lektion hast du gelernt, wie du mit dem 74HC595-Schieberegister und dem Raspberry Pi Pico mehrere LEDs mit nur drei GPIO-Pins steuern kannst. Diese Technik ermöglicht eine einfache Erweiterung der digitalen Ausgänge und eröffnet zahlreiche Möglichkeiten für komplexe und interaktive Projekte. Indem serielle Daten an das Schieberegister gesendet und in parallele Ausgänge umgewandelt werden, kannst du effizient verschiedene Aktoren, Anzeigen oder andere Peripheriegeräte in deinen Elektronikprojekten steuern.
