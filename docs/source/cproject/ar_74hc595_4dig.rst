.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein – gemeinsam mit anderen Technikbegeisterten.

    **Warum beitreten?**

    - **Experten-Support**: Erhalte Hilfe bei technischen Herausforderungen und Problemen nach dem Kauf – direkt von unserer Community und unserem Team.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten weiterzuentwickeln.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Profitiere von exklusiven Vergünstigungen auf unsere neuesten Produkte.
    - **Feiertagsaktionen und Gewinnspiele**: Nimm an Sonderaktionen und Verlosungen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und trete noch heute bei!

.. _ar_74hc_4dig:

5.3 Erstellen eines Zeitzählers mit einer 4-stelligen 7-Segment-Anzeige
==========================================================================

In dieser Lektion lernen wir, wie man eine **4-stellige 7-Segment-Anzeige** mit dem Raspberry Pi Pico 2 W verwendet, um einen einfachen Zeitmesser zu erstellen. Die Anzeige zählt jede Sekunde hoch und zeigt die verstrichene Zeit in Sekunden an.


**Benötigte Komponenten**

Für dieses Projekt werden folgende Komponenten benötigt.

Es ist praktisch, ein komplettes Kit zu kaufen. Hier ist der Link: 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ENTHALTENE TEILE IM KIT
        - KAUFLINK
    *   - Pico 2 W Starter Kit	
        - 450+
        - |link_pico2w_kit|


Alternativ kannst du die Komponenten einzeln über die folgenden Links erwerben.

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
        - 4 (220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_4_dit_7_segment`
        - 1
        - 
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|


**Funktionsweise der 4-stelligen 7-Segment-Anzeige**

Eine 4-stellige 7-Segment-Anzeige besteht aus vier einzelnen 7-Segment-Anzeigen, die zu einem Modul zusammengefasst sind. Alle Ziffern teilen sich die Steuerleitungen für die Segmente (**a** bis **g** und **dp**), aber jede Ziffer hat eine eigene **gemeinsame Kathode** zur Steuerung.

Um unterschiedliche Zahlen auf jeder Ziffer anzuzeigen, wird die Technik des **Multiplexing** verwendet. Dabei werden die Ziffern so schnell nacheinander aktualisiert, dass es für das menschliche Auge so aussieht, als ob alle Ziffern gleichzeitig leuchten.

|4digit_control_pins|

**Schaltplan**

|sch_4dig|

Das Verdrahtungsprinzip ist weitgehend identisch mit :ref:`ar_74hc_led`, der einzige Unterschied besteht darin, dass die Pins Q0-Q7 mit den a ~ g Pins der 4-stelligen 7-Segment-Anzeige verbunden sind.

Die Pins G10 ~ G13 bestimmen, welche Ziffer aktiv ist.

**Verdrahtung**

|wiring_4dig|

* **Segmentverbindungen (über 220 Ω Widerstände):**

  * **Q0** → Segment **a**
  * **Q1** → Segment **b**
  * **Q2** → Segment **c**
  * **Q3** → Segment **d**
  * **Q4** → Segment **e**
  * **Q5** → Segment **f**
  * **Q6** → Segment **g**
  * **Q7** → Segment **dp** (Dezimalpunkt)

* **Gemeinsame Kathodenverbindungen (Ziffernauswahl-Pins):**

  * **Ziffer 1 (linke Ziffer):** Verbindung mit **GP10** am Pico
  * **Ziffer 2:** Verbindung mit **GP11**
  * **Ziffer 3:** Verbindung mit **GP12**
  * **Ziffer 4 (rechte Ziffer):** Verbindung mit **GP13**

**Code schreiben**

.. note::

    * Die Datei ``5.3_time_counter.ino`` kann unter ``pico-2w-kit-main/arduino/5.3_time_counter`` geöffnet werden.
    * Alternativ kannst du den Code in die **Arduino IDE** kopieren.
    * Vor dem Hochladen nicht vergessen, das richtige Board (Raspberry Pi Pico) und den **korrekten Port** auszuwählen.

.. code-block:: arduino

    // Verbindungspins für das Schieberegister definieren
    #define DATA_PIN 18   // DS (Serielle Dateneingabe)
    #define LATCH_PIN 19  // STCP (Speicherregister-Takt)
    #define CLOCK_PIN 20  // SHCP (Schieberegister-Takt)

    // Steuerpins für die 4-stellige 7-Segment-Anzeige
    const int digitPins[4] = { 10, 11, 12, 13 };  // DIG1, DIG2, DIG3, DIG4

    // Segmentmuster für Zahlen 0-9
    const byte digitCodes[10] = {
      // Pgfedcba
      0b00111111,  // 0
      0b00000110,  // 1
      0b01011011,  // 2
      0b01001111,  // 3
      0b01100110,  // 4
      0b01101101,  // 5
      0b01111101,  // 6
      0b00000111,  // 7
      0b01111111,  // 8
      0b01101111   // 9
    };

    unsigned long previousMillis = 0;  // Stores the last time the display was updated
    unsigned int counter = 0;          // Counter value

    void setup() {
      // Initialize the shift register pins
      pinMode(DATA_PIN, OUTPUT);
      pinMode(LATCH_PIN, OUTPUT);
      pinMode(CLOCK_PIN, OUTPUT);

      // Initialize the digit control pins
      for (int i = 0; i < 4; i++) {
        pinMode(digitPins[i], OUTPUT);
        digitalWrite(digitPins[i], HIGH);  // Turn off all digits
      }
    }

    void loop() {
      unsigned long currentMillis = millis();

      // Update the counter every 1000 milliseconds (1 second)
      if (currentMillis - previousMillis >= 1000) {
        previousMillis = currentMillis;
        counter++;  // Increment the counter
        if (counter > 9999) {
          counter = 0;  // Reset counter after 9999
        }
      }

      // Display the counter value
      displayNumber(counter);
    }

    void displayNumber(int num) {
      // Break the number into digits
      int digits[4];
      digits[0] = num / 1000;        // Thousands
      digits[1] = (num / 100) % 10;  // Hundreds
      digits[2] = (num / 10) % 10;   // Tens
      digits[3] = num % 10;          // Units

      // Display each digit
      for (int i = 0; i < 4; i++) {
        digitalWrite(digitPins[i], LOW);  // Activate digit
        shiftOutDigit(digitCodes[digits[i]]);
        delay(5);                          // Small delay for multiplexing
        digitalWrite(digitPins[i], HIGH);  // Deactivate digit
      }
    }

    void shiftOutDigit(byte data) {
      // Send data to the shift register
      digitalWrite(LATCH_PIN, LOW);
      shiftOut(DATA_PIN, CLOCK_PIN, MSBFIRST, data);
      digitalWrite(LATCH_PIN, HIGH);
    }

Nach dem Hochladen des Codes beginnt die 4-stellige 7-Segment-Anzeige bei 0000 zu zählen und erhöht sich jede Sekunde um 1. 
Die Zählung verläuft wie folgt: 0000, 0001, 0002, ..., 9999, danach wird sie auf 0000 zurückgesetzt.

**Verständnis des Codes**

#. Definition der Steuerpins:

   * ``DATA_PIN (DS)``: Empfängt serielle Daten, die in das 74HC595-Schieberegister übertragen werden.
   * ``LATCH_PIN (STCP)``: Steuert das Speichern der Daten im Schieberegister, um sie an die Ausgangspins weiterzugeben.
   * ``CLOCK_PIN (SHCP)``: Taktet die Datenübertragung in das Schieberegister.

   .. code-block:: arduino

      #define DATA_PIN   18  // DS (Serielle Dateneingabe)
      #define LATCH_PIN  19  // STCP (Speicherregister-Takt)
      #define CLOCK_PIN  20  // SHCP (Schieberegister-Takt)
  
#. Definition der Ziffernsteuerungs-Pins:

   * Die gemeinsame Kathode jeder Ziffer ist mit einem separaten GPIO-Pin verbunden.
   * Ein LOW-Signal aktiviert die jeweilige Ziffer, während ein HIGH-Signal sie deaktiviert.

   .. code-block:: arduino

      const int digitPins[4] = {10, 11, 12, 13}; // DIG1, DIG2, DIG3, DIG4
  
#. Erstellung der Segment-Byte-Zuordnungen:

   * Jedes Byte repräsentiert die Segmente, die zur Darstellung der Zahlen 0 bis 9 auf einer gemeinsamen Kathoden-7-Segment-Anzeige leuchten müssen.
   * Die Bits entsprechen den Segmenten a bis g und dp:

   .. code-block:: arduino

      const byte digitCodes[10] = {
        0b00111111, // 0
        0b00000110, // 1
        0b01011011, // 2
        0b01001111, // 3
        0b01100110, // 4
        0b01101101, // 5
        0b01111101, // 6
        0b00000111, // 7
        0b01111111, // 8
        0b01101111  // 9
      };

#. Setup-Funktion:

   * Setzt die Pins ``DATA_PIN``, ``LATCH_PIN`` und ``CLOCK_PIN`` als Ausgänge.
   * Setzt alle Ziffernsteuerungs-Pins auf ``HIGH``, um zu Beginn alle Ziffern zu deaktivieren.

   .. code-block:: arduino

      void setup() {
        // Initialisierung der Schieberegister-Pins
        pinMode(DATA_PIN, OUTPUT);
        pinMode(LATCH_PIN, OUTPUT);
        pinMode(CLOCK_PIN, OUTPUT);

        // Initialisierung der Ziffernsteuerungs-Pins
        for (int i = 0; i < 4; i++) {
          pinMode(digitPins[i], OUTPUT);
          digitalWrite(digitPins[i], HIGH); // Deaktiviert alle Ziffern initial
        }
      }

#. Loop-Funktion:

   * Verwendet die ``millis()``-Funktion, um die verstrichene Zeit ohne Blockierung des Programms zu verfolgen.
   * Erhöht die Variable ``counter`` jede Sekunde und setzt sie nach Erreichen von 9999 zurück.

   .. code-block:: arduino

      void loop() {
        unsigned long currentMillis = millis();

        // Aktualisiert den Zähler alle 1000 Millisekunden (1 Sekunde)
        if (currentMillis - previousMillis >= 1000) {
          previousMillis = currentMillis;
          counter++; // Erhöht den Zähler
          if (counter > 9999) {
            counter = 0; // Setzt den Zähler nach 9999 zurück
          }
        }

        // Zeigt den aktuellen Zählerwert an
        displayNumber(counter);
      }

#. Darstellung der Zahl:

   * Zerlegt den ``counter``-Wert in Tausender-, Hunderter-, Zehner- und Einerstellen.
   * Aktiviert jede Ziffer einzeln, sendet die zugehörigen Segmentdaten und deaktiviert die Ziffer anschließend wieder.
   * Durch das schnelle Umschalten zwischen den Ziffern entsteht der Eindruck, dass alle Ziffern gleichzeitig leuchten.

   .. code-block:: arduino

      void displayNumber(int num) {
        // Zerlegt die Zahl in einzelne Ziffern
        int digits[4];
        digits[0] = num / 1000;        // Tausender
        digits[1] = (num / 100) % 10;  // Hunderter
        digits[2] = (num / 10) % 10;   // Zehner
        digits[3] = num % 10;          // Einer

        // Jede Ziffer wird einzeln dargestellt
        for (int i = 0; i < 4; i++) {
          digitalWrite(digitPins[i], LOW); // Aktiviert die aktuelle Ziffer

          // Sendet die Segmentdaten für die aktuelle Ziffer
          shiftOutDigit(digitCodes[digits[i]]);

          delay(5);                        // Kleine Verzögerung für Multiplexing
          digitalWrite(digitPins[i], HIGH); // Deaktiviert die Ziffer
        }
      }

#. Ausgabe der Segmentdaten:

   * Sendet die Segmentdaten an das 74HC595-Schieberegister.
   * ``shiftOut()`` überträgt die Daten bitweise, beginnend mit dem höchstwertigen Bit (``MSBFIRST``).
   * Durch Umschalten des ``LATCH_PIN`` werden die Daten an die Ausgangspins weitergegeben.

   .. code-block:: arduino

      void shiftOutDigit(byte data) {
        // Überträgt die Daten in das Schieberegister
        digitalWrite(LATCH_PIN, LOW);
        shiftOut(DATA_PIN, CLOCK_PIN, MSBFIRST, data);
        digitalWrite(LATCH_PIN, HIGH);
      }
  
**Weitere Experimente**

* Reset-Taste hinzufügen: 

  Schließe eine Taste an den Pico an, um den Zähler bei Bedarf zurückzusetzen.

* Andere Werte anzeigen: 

  Ändere den Code, um Sensordaten anzuzeigen, z. B. Temperatur oder Lichtwerte.

* Stoppuhr-Funktion umsetzen: 

  Implementiere eine Start-, Stopp- und Reset-Funktion, um die Anzeige als Stoppuhr zu nutzen.

**Fazit**

Dieses Projekt zeigt, wie eine 4-stellige 7-Segment-Anzeige mithilfe eines Schieberegisters und Multiplexing-Techniken gesteuert wird. Durch die effiziente Zeitsteuerung mit ``millis()`` entsteht ein reaktionsschneller und präziser Zeitzähler, ohne die Leistung der Anzeige zu beeinträchtigen.
