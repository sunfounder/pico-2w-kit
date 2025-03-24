.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein – gemeinsam mit anderen Technikbegeisterten.

    **Warum beitreten?**

    - **Experten-Support**: Erhalte Unterstützung bei technischen Herausforderungen und Problemen nach dem Kauf – direkt von unserer Community und unserem Team.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten weiterzuentwickeln.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Profitiere von exklusiven Vergünstigungen auf unsere neuesten Produkte.
    - **Feiertagsaktionen und Gewinnspiele**: Nimm an Sonderaktionen und Verlosungen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und trete noch heute bei!

.. _ar_74hc_788bs:


5.4 Grafiken auf einer 8x8-LED-Matrix anzeigen
===================================================================

In dieser Lektion lernen wir, wie man eine **8x8-LED-Matrix** mit dem Raspberry Pi Pico 2 W und zwei **74HC595-Schieberegistern** steuert. Wir werden Muster und einfache Grafiken anzeigen, indem wir einzelne LEDs der Matrix gezielt ansteuern.

* :ref:`cpn_dot_matrix`
* :ref:`cpn_74hc595`

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
        - 450+ Komponenten
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
        - :ref:`cpn_dot_matrix`
        - 1
        - 
    *   - 6
        - :ref:`cpn_74hc595`
        - 2
        - |link_74hc595_buy|


**Funktionsweise der 8x8-LED-Matrix**

Eine 8x8-LED-Matrix besteht aus 64 LEDs, die in 8 Reihen und 8 Spalten angeordnet sind. Jede LED kann individuell gesteuert werden, indem eine Spannung zwischen ihrer Reihe und Spalte angelegt wird. Durch gezielte Steuerung der Reihen- und Spaltenströme können Zeichen oder Muster auf der Matrix dargestellt werden.

In diesem Aufbau verwenden wir zwei 74HC595-Schieberegister zur Steuerung der Reihen und Spalten der LED-Matrix. Dadurch erweitern wir die Anzahl der Ausgänge des Raspberry Pi Pico, während wir nur wenige GPIO-Pins verwenden.

**Schaltplan**

|sch_ledmatrix|

Die 8x8-LED-Matrix wird von zwei **74HC595**-Schieberegistern gesteuert: Eines kontrolliert die Reihen, das andere die Spalten. Beide ICs teilen sich die GPIO-Pins **GP18**, **GP19** und **GP20** des Pico, wodurch dessen I/O-Pins effizient genutzt werden.

Der Pico sendet jeweils ein 16-Bit-Binärsignal aus. Die ersten 8 Bits werden an das 74HC595 übermittelt, das die Reihen steuert, und die letzten 8 Bits an das 74HC595 für die Spalten. Dadurch kann die Matrix gezielt Muster anzeigen.

**Q7' (Pin 9)**: Dieser serielle Ausgang des ersten 74HC595 ist mit dem **DS (Pin 14)** des zweiten 74HC595 verbunden, wodurch mehrere Schieberegister in Reihe geschaltet werden können.

**Verdrahtung**

Der Aufbau der Schaltung kann komplex sein, daher gehen wir schrittweise vor.

**Schritt 1:** Setze zunächst den Pico 2 W, die LED-Matrix und zwei 74HC595-Chips 
auf das Breadboard. Verbinde 3,3V und GND des Pico 2 W mit den Stromschienen des 
Boards. Anschließend verbinde Pin 16 und 10 der beiden 74HC595-Chips mit VCC sowie 
Pin 13 und 8 mit GND.

.. note::
   In der obigen Fritzing-Grafik befindet sich die Seite mit der Beschriftung unten.

|wiring_ledmatrix_4|

**Schritt 2:** Verbinde Pin 11 der beiden 74HC595-Chips miteinander und anschließend 
mit GP20. Danach verbinde Pin 12 der beiden Chips mit GP19. Schließlich verbinde Pin 14 des linken 74HC595 mit GP18 und Pin 9 mit Pin 14 des zweiten 74HC595.

|wiring_ledmatrix_3|

**Schritt 3:** Der 74HC595 auf der rechten Seite steuert die Spalten der LED-Matrix. 
Die folgende Tabelle zeigt die Zuordnung der Pins. Die Pins Q0-Q7 des 74HC595 sind 
den Pins 13, 3, 4, 10, 6, 11, 15 und 16 der LED-Matrix zugeordnet.

+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **74HC595**        | **Q0** | **Q1** | **Q2** | **Q3** | **Q4** | **Q5** | **Q6** | **Q7** |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **LED Dot Matrix** | **13** | **3**  | **4**  | **10** | **6**  | **11** | **15** | **16** |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+

|wiring_ledmatrix_2|

**Schritt 4:** Verbinde nun die Reihen (Rows) der LED-Matrix. Der linke 74HC595 
steuert die Reihen der Matrix. In der folgenden Tabelle siehst du die Zuordnung 
der Pins. Q0-Q7 des linken 74HC595 sind den Pins 9, 14, 8, 12, 1, 7, 2 und 5 der 
LED-Matrix zugeordnet.

+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **74HC595**        | **Q0** | **Q1** | **Q2** | **Q3** | **Q4** | **Q5** | **Q6** | **Q7** |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **LED Dot Matrix** | **9**  | **14** | **8**  | **12** | **1**  | **7**  | **2**  | **5**  |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+

|wiring_ledmatrix_1|

**Code schreiben**

.. note::

    * Die Datei ``5.4_8x8_pixel_graphics.ino`` befindet sich unter ``pico-2w-kit-main/arduino/5.4_8x8_pixel_graphics``. 
    * Alternativ kann der Code in die **Arduino IDE** kopiert werden.
    * Vor dem Hochladen muss das richtige Board (Raspberry Pi Pico) und der **korrekte Port** ausgewählt werden.

.. code-block:: arduino

    const int STcp = 19;  // Pin für ST_CP (Latch-Pin) des 74HC595
    const int SHcp = 20;  // Pin für SH_CP (Takt-Pin) des 74HC595
    const int DS = 18;    // Pin für DS (Daten-Pin) des 74HC595

    // Datenarray für das 'X'-Muster auf einer 8x8-LED-Matrix
    byte datArray[] = {0x7E, 0xBD, 0xDB, 0xE7, 0xE7, 0xDB, 0xBD, 0x7E};

    void setup() {
      // Set pins as outputs
      pinMode(STcp, OUTPUT);
      pinMode(SHcp, OUTPUT);
      pinMode(DS, OUTPUT);
    }

    void loop()
    {
      for(int num = 0; num <8; num++)
      {
        digitalWrite(STcp,LOW); //ground ST_CP and hold low for as long as you are transmitting
        shiftOut(DS,SHcp,MSBFIRST,datArray[num]);
        shiftOut(DS,SHcp,MSBFIRST,0x80>>num);    
        //return the latch pin high to signal chip that it 
        //no longer needs to listen for information
        digitalWrite(STcp,HIGH); //pull the ST_CPST_CP to save the data
      }
    }

Nach dem Hochladen des Codes sollte die LED-Matrix ein 'X'-Muster anzeigen, indem die entsprechenden LEDs aufleuchten.
Falls das Muster nicht sichtbar ist, überprüfe die Verdrahtung oder passe die Timing-Werte an.

**Verständnis des Codes**

#. Definition der Pins:

   * ``STcp (ST_CP)``: Speichert die übertragenen Daten in den Ausgangsregistern bei steigender Flanke.
   * ``SHcp (SH_CP)``: Verschiebt Daten bei jeder steigenden Taktflanke in das Register.
   * ``DS``: Serieller Dateneingang für das Schieberegister.

   .. code-block:: arduino

      const int STcp = 19;  // Latch-Pin (ST_CP) des 74HC595
      const int SHcp = 20;  // Takt-Pin (SH_CP) des 74HC595
      const int DS = 18;    // Daten-Pin (DS) des 74HC595

#. Datenarray (``datArray``):

   * Jedes Element entspricht einer Reihe der LED-Matrix.
   * Die hexadezimalen Werte geben an, welche LEDs leuchten (0) oder ausgeschaltet bleiben (1).
   * Dieses Muster bildet ein symmetrisches 'X' über die Matrix.

   .. code-block:: arduino

      byte datArray[] = {0x7E, 0xBD, 0xDB, 0xE7, 0xE7, 0xDB, 0xBD, 0x7E};


#. Setup-Funktion:

   Initialisiert die Steuerpins als Ausgänge zur Kommunikation mit den Schieberegistern.

   .. code-block:: arduino

      void setup() {
        // Set pins as outputs
        pinMode(STcp, OUTPUT);
        pinMode(SHcp, OUTPUT);
        pinMode(DS, OUTPUT);
      }

#. Loop-Funktion:

   * ``num`` läuft von 0 bis 7 und steht für jede Reihe der LED-Matrix.
   * ``0x80>>num`` aktiviert jeweils eine Reihe.
   * ``shiftOut()`` sendet Spalten- und Reihendaten an die Schieberegister, beginnend mit dem höchstwertigen Bit (``MSBFIRST``).
   * Durch das Umschalten des ``STcp`` wird das Signal an die LEDs übertragen.

   .. code-block:: arduino

      void loop()
      {
        for(int num = 0; num <8; num++)
        {
          digitalWrite(STcp,LOW); //ground ST_CP and hold low for as long as you are transmitting
          shiftOut(DS,SHcp,MSBFIRST,datArray[num]);
          shiftOut(DS,SHcp,MSBFIRST,0x80>>num);    
          //return the latch pin high to signal chip that it 
          //no longer needs to listen for information
          digitalWrite(STcp,HIGH); //pull the ST_CPST_CP to save the data
        }
      }

**Fehlersuche**

* Keine LEDs leuchten auf:

  * Überprüfe die Stromversorgung.
  * Stelle sicher, dass die Schieberegister korrekt mit dem Pico verbunden sind.
  
* Falsche Muster:

  * Kontrolliere das Datenarray.
  * Stelle sicher, dass Reihen und Spalten richtig mit den Schieberegistern verbunden sind.

* Flackern oder instabile Anzeige:

  * Passe den Verzögerungswert in der Schleife an, um eine gute Balance zwischen Leistung und Stabilität zu finden.
  * Stelle sicher, dass die Stromversorgung stabil und ausreichend für die Anzahl der verwendeten LEDs ist.


**Weitere Experimente** 

* Muster ändern

  Versuche, die Musterliste mit den folgenden Arrays zu ersetzen, um verschiedene Grafiken anzuzeigen. Ersetze das Muster in deinem Code mit ``pattern_heart`` oder ``pattern_smile``, um unterschiedliche Bilder zu sehen.

  .. code-block:: arduino

      // Herzmuster
      byte pattern_heart[] = {
        0xFF, // 11111111
        0x99, // 10011001
        0x00, // 00000000
        0x00, // 00000000
        0x00, // 00000000
        0x81, // 10000001
        0xC3, // 11000011
        0xE7  // 11100111
      };

      // Lachgesicht-Muster
      byte pattern_smile[] = {
        0xC3, // 11000011
        0xBD, // 10111101
        0x5A, // 01011010
        0x7E, // 01111110
        0x5A, // 01011010
        0x66, // 01100110
        0xBD, // 10111101
        0xC3  // 11000011
      };

* Animation der Anzeige

  Erstelle mehrere Muster und wechsle sie zyklisch, um Animationen zu erzeugen:

  .. code-block:: arduino
        
      const int STcp = 19;  // Pin für ST_CP (Latch-Pin) des 74HC595
      const int SHcp = 20;  // Pin für SH_CP (Takt-Pin) des 74HC595
      const int DS = 18;    // Pin für DS (Daten-Pin) des 74HC595

      // Herzmuster
      byte pattern_heart[] = { 0xFF, 0x99, 0x00, 0x00, 0x00, 0x81, 0xC3, 0xE7 };

      // Lachgesicht-Muster
      byte pattern_smile[] = { 0xC3, 0xBD, 0x5A, 0x7E, 0x5A, 0x66, 0xBD, 0xC3 };

      void setup() {
        // Setze Pins als Ausgänge
        pinMode(STcp, OUTPUT);
        pinMode(SHcp, OUTPUT);
        pinMode(DS, OUTPUT);
      }

      void latchData() {
        // Speichert die übertragenen Daten in den Ausgängen des 74HC595
        digitalWrite(STcp, HIGH);  // Daten speichern
        digitalWrite(STcp, LOW);   // Vorbereitung für die nächste Übertragung
      }

      void displayPattern(byte pattern[]) {
        for (int repeat = 0; repeat < 500; repeat++) {  // Muster für eine bestimmte Zeit anzeigen
          for (int row = 0; row < 8; row++) {
            // Beginne die Datenübertragung
            digitalWrite(STcp, LOW);  // Vorbereitung zur Datenübertragung

            // Übertrage die Spaltendaten (Muster für die aktuelle Zeile)
            shiftOut(DS, SHcp, MSBFIRST, pattern[row]);

            // Übertrage die Zeilendaten (aktiviert jeweils eine Zeile)
            shiftOut(DS, SHcp, MSBFIRST, 1 << row);

            // Daten zur Anzeige speichern
            latchData();

            // Kurze Verzögerung für das Nachbild auf der Netzhaut
            delay(1);
          }
        }
      }

      void loop() {
        // Zeigt fortlaufend die Muster "Herz" und "Lachgesicht" an
        displayPattern(pattern_heart);  // Herzform anzeigen
        displayPattern(pattern_smile);  // Lachgesicht anzeigen
      }

**Fazit**

In dieser Lektion hast du gelernt, wie du eine 8x8-LED-Matrix mit dem Raspberry Pi Pico und zwei 74HC595-Schieberegistern steuerst. Durch den Einsatz von Schieberegistern kannst du mehrere LEDs effizient mit minimalem GPIO-Aufwand verwalten, was komplexere und interaktive Projekte ermöglicht. Das Verständnis der seriellen Datenübertragung und des Latch-Prozesses erlaubt dir, dynamische Muster und Grafiken auf der LED-Matrix zu erzeugen.
