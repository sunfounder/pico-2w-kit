.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein – gemeinsam mit anderen Technikbegeisterten.

    **Warum beitreten?**

    - **Experten-Support**: Erhalte Hilfe bei technischen Herausforderungen und Problemen nach dem Kauf – direkt von unserer Community und unserem Team.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten weiterzuentwickeln.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Profitiere von exklusiven Vergünstigungen auf unsere neuesten Produkte.
    - **Feiertagsaktionen und Gewinnspiele**: Nimm an Sonderaktionen und Verlosungen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und trete noch heute bei!

.. _ar_74hc_7seg:

5.2 Zahlen anzeigen
===========================================================

In dieser Lektion lernen wir, wie man eine **7-Segment-Anzeige** verwendet, um Zahlen mit dem Raspberry Pi Pico 2 W und einem **74HC595-Schieberegister** darzustellen. Die 7-Segment-Anzeige ist eine häufig verwendete elektronische Komponente, die in Geräten wie Digitaluhren, Taschenrechnern und Haushaltsgeräten zur Anzeige numerischer Informationen genutzt wird.

Durch die Kombination des 74HC595-Schieberegisters mit der 7-Segment-Anzeige können alle Segmente mit nur wenigen GPIO-Pins des Pico gesteuert werden, wodurch wertvolle I/O-Ressourcen für andere Komponenten gespart werden.
* :ref:`cpn_7_segment`


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
        - :ref:`cpn_resistor`
        - 1 (220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_7_segment`
        - 1
        - |link_7segment_buy|
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|

**Funktionsweise der 7-Segment-Anzeige**

Eine 7-Segment-Anzeige besteht aus 7 LEDs (Segmenten), die in einer Acht-Form angeordnet sind, um Ziffern von 0 bis 9 darzustellen. Zusätzlich gibt es eine achte LED für den Dezimalpunkt. Jedes Segment ist mit den Buchstaben **a** bis **g** gekennzeichnet, der Dezimalpunkt mit **dp**.

Hier ist die Segment-Beschriftung:

|img_7seg_cathode|

Bei einer **gemeinsamen Kathode** sind alle Kathoden (negativen Seiten) der LEDs miteinander verbunden und an Masse angeschlossen.

**Schaltplan**

|sch_74hc_7seg|

Das Verdrahtungsprinzip ist weitgehend identisch mit :ref:`py_74hc_led`, mit dem einzigen Unterschied, dass Q0-Q7 mit den a ~ g-Pins der 7-Segment-Anzeige verbunden sind.

.. list-table:: Wiring
    :widths: 15 25
    :header-rows: 1

    *   - 74HC595
        - 7-Segment-Anzeige
    *   - Q0
        - a
    *   - Q1
        - b
    *   - Q2
        - c
    *   - Q3
        - d
    *   - Q4
        - e
    *   - Q5
        - f
    *   - Q6
        - g
    *   - Q7
        - dp

**Verdrahtung**

|wiring_74hc_7seg|


**Code schreiben**

Wir schreiben ein Programm, das die 7-Segment-Anzeige durch serielle Datenübertragung zum 74HC595-Schieberegister steuert. Die Anzeige wird die Zahlen 0 bis 9 in einer Schleife darstellen.

.. note::

    * Die Datei ``5.2_number_display.ino`` kann unter ``pico-2w-kit-main/arduino/5.2_number_display`` geöffnet werden.
    * Alternativ kann der Code in die **Arduino IDE** kopiert werden.
    * Vor dem Hochladen muss das richtige Board (Raspberry Pi Pico) und der korrekte Port ausgewählt werden.

.. code-block:: arduino

    // Definiere die Pins für das 74HC595
    const int DS = 0;    // GPIO 0 -> DS (Pin 14)
    const int SHCP = 1;  // GPIO 1 -> SHCP (Pin 11)
    const int STCP = 2;  // GPIO 2 -> STCP (Pin 12)

    // Array der Hexadezimalcodes für die Ziffern 0-9 auf einer gemeinsamen Kathoden-7-Segment-Anzeige
    const byte numArray[] = {
      0x3F, // 0: 00111111
      0x06, // 1: 00000110
      0x5B, // 2: 01011011
      0x4F, // 3: 01001111
      0x66, // 4: 01100110
      0x6D, // 5: 01101101
      0x7D, // 6: 01111101
      0x07, // 7: 00000111
      0x7F, // 8: 01111111
      0x6F  // 9: 01101111
    };

    void setup() {
      // Initialisiere die Steuerpins als Ausgänge
      pinMode(DS, OUTPUT);
      pinMode(SHCP, OUTPUT);
      pinMode(STCP, OUTPUT);
    }

    void loop() {
      // Durchläuft die Zahlen 0-9
      for (int num = 0; num < 10; num++) {
        // Bereite das Schieberegister für neue Daten vor
        digitalWrite(STCP, LOW);

        // Übertrage die Daten an das Schieberegister
        shiftOut(DS, SHCP, MSBFIRST, numArray[num]);

        // Latch-Daten an die Ausgangspins
        digitalWrite(STCP, HIGH);

        delay(1000); // Warte eine Sekunde, bevor die nächste Zahl angezeigt wird
      }

      // Schaltet alle Segmente aus, nachdem 0-9 angezeigt wurde
      digitalWrite(STCP, LOW);
      shiftOut(DS, SHCP, MSBFIRST, 0x00);
      digitalWrite(STCP, HIGH);
      delay(1000);
    }

Nach dem Hochladen des Codes sollte die Anzeige die Zahlen 0 bis 9 in einer Schleife anzeigen, wobei jede Zahl eine Sekunde lang sichtbar bleibt.
Nach der Zahl 9 werden alle Segmente für eine Sekunde ausgeschaltet, bevor die Sequenz erneut beginnt.

**Verständnis des Codes**

#. Definition der Steuerpins:

   * ``DS (Data Serial Input)``: Empfängt serielle Daten, die in das Register verschoben werden.
   * ``SHCP (Shift Register Clock Input)``: Steuert das Verschieben der Daten in das Register.
   * ``STCP (Storage Register Clock Input)``: Steuert das Speichern der Daten aus dem Schieberegister in die Ausgangspins.

   .. code-block:: arduino

        const int DS = 0;    // GPIO 0 -> DS (Pin 14)
        const int SHCP = 2;  // GPIO 2 -> SHCP (Pin 11)
        const int STCP = 1;  // GPIO 1 -> STCP (Pin 12)

#. Erstellen von Datenmustern:

   * ``numArray``: Ein Array mit Hexadezimalcodes zur Darstellung der Zahlen 0-9 auf einer gemeinsamen Kathoden-7-Segment-Anzeige.
   * Jeder Hexadezimalwert gibt an, welche Segmente für die jeweilige Zahl aktiviert werden müssen.

   .. code-block:: arduino

        const byte numArray[] = {
          0x3F, // 0: 00111111
          0x06, // 1: 00000110
          0x5B, // 2: 01011011
          0x4F, // 3: 01001111
          0x66, // 4: 01100110
          0x6D, // 5: 01101101
          0x7D, // 6: 01111101
          0x07, // 7: 00000111
          0x7F, // 8: 01111111
          0x6F  // 9: 01101111
        };

   Soll die 7-Segment-Anzeige die Zahl "1" darstellen, müssen die Segmente b und c eingeschaltet werden, während a, d, e, f, g und dp ausgeschaltet bleiben.

   |img_1_segment|

   Das bedeutet, dass das Binärmuster 00000110 geschrieben werden muss. Zur besseren Lesbarkeit wird dies in hexadezimaler Schreibweise als 0x06 dargestellt.

#. Setup-Funktion:

   Setzt die Pins ``DS``, ``SHCP`` und ``STCP`` als Ausgänge, um Daten an das Schieberegister zu senden.

   .. code-block:: arduino

        void setup() {
          // Initialisiert die Steuerpins als Ausgänge
          pinMode(DS, OUTPUT);
          pinMode(SHCP, OUTPUT);
          pinMode(STCP, OUTPUT);
        }

#. Loop-Funktion: Die ``for``-Schleife durchläuft jedes Muster im ``numArray`` -Array.

   * Verschieben der Daten:

     * ``shiftOut`` sendet das Byte der Daten Bit für Bit.
     * ``MSBFIRST`` gibt an, dass das höchstwertige Bit zuerst gesendet wird.

     .. code-block:: arduino

        shiftOut(DS, SHCP, MSBFIRST, numArray[num]);

   * Speichern der Daten:

     * ``STCP`` auf ``LOW`` setzen, um das Schieberegister für neue Daten vorzubereiten.
     * Nach dem Übertragen der Daten ``STCP`` auf ``HIGH`` setzen, um die Daten in die Ausgangspins zu übernehmen und die 7-Segment-Anzeige zu aktualisieren.

     .. code-block:: arduino

        digitalWrite(STCP, LOW);
        // shiftOut(...)
        digitalWrite(STCP, HIGH);

   * ``delay(500);`` fügt eine halbe Sekunde Pause zwischen jeder Zahl für bessere Sichtbarkeit hinzu.

   * Ausschalten aller Segmente: Nachdem die Zahlen 0-9 angezeigt wurden, sendet der Code 0x00, um alle Segmente auszuschalten. Die Anzeige bleibt eine Sekunde lang ausgeschaltet, bevor die Schleife erneut beginnt.

     .. code-block:: arduino

        digitalWrite(STCP, LOW);
        shiftOut(DS, SHCP, MSBFIRST, 0x00);
        digitalWrite(STCP, HIGH);
        delay(1000);

**Fehlersuche**

* Keine Zahlen werden angezeigt:

  * Überprüfe alle Verdrahtungen.
  * Stelle sicher, dass der 74HC595 ordnungsgemäß mit Strom versorgt wird.
  * Vergewissere dich, dass die GPIO-Pins des Pico korrekt mit dem Schieberegister verbunden sind.
  * Prüfe, ob die 7-Segment-Anzeige richtig angeschlossen ist, insbesondere mit Vorwiderständen für jedes Segment.

* Falsche Zahlen werden angezeigt:

  * Überprüfe die Hexadezimalwerte im numArray.
  * Stelle sicher, dass die Ausgänge des Schieberegisters korrekt mit den jeweiligen Segmenten verbunden sind.

* Flackern oder instabile Anzeige:

  * Kontrolliere die Stromversorgung auf stabile Verbindungen.
  * Prüfe, ob die Widerstände ordnungsgemäß angeschlossen sind, um den Strom durch die Segmente zu begrenzen.

**Verständnis der Segmentcodes**

Jeder Segmentcode bestimmt, welche Segmente aktiviert werden, um eine bestimmte Ziffer darzustellen. Hier ist die Zuordnung der Segmente zu den jeweiligen Ziffern:

* **0**: Segmente a, b, c, d, e, f (Code 0x3F)
* **1**: Segmente b, c (Code 0x06)
* **2**: Segmente a, b, g, e, d (Code 0x5B)
* **3**: Segmente a, b, c, d, g (Code 0x4F)
* **4**: Segmente b, c, f, g (Code 0x66)
* **5**: Segmente a, c, d, f, g (Code 0x6D)
* **6**: Segmente a, c, d, e, f, g (Code 0x7D)
* **7**: Segmente a, b, c (Code 0x07)
* **8**: Segmente a, b, c, d, e, f, g (Code 0x7F)
* **9**: Segmente a, b, c, d, f, g (Code 0x6F)

**Weiterführende Experimente**

* Steuerung mehrerer 7-Segment-Anzeigen: 

  Mehrere 74HC595-Schieberegister in Reihe schalten, um zusätzliche Anzeigen zu steuern und mehrstellige Zahlen darzustellen.

* LED-Animationen implementieren:

  Durch Anpassen der Datenmuster im Schieberegister können einfache Animationen oder Laufschriften erstellt werden.

* Integration mit Sensoren:

  Die 7-Segment-Anzeige kann mit Sensoren (z. B. Temperatur-, Licht- oder Abstandssensoren) kombiniert werden, um Echtzeitwerte darzustellen.

* Bau einer digitalen Uhr: 

  Mehrere 7-Segment-Anzeigen zusammen mit Echtzeit-Uhrenmodulen verwenden, um eine funktionale digitale Uhr zu erstellen.

* Hinzufügen von Dezimalpunkten und Indikatoren:

  Den Dezimalpunkt (dp) oder andere Anzeigen (z. B. Doppelpunkte für eine Uhr) für komplexere Darstellungen nutzen.

**Fazit**

In dieser Lektion hast du gelernt, wie du mit dem 74HC595-Schieberegister und dem Raspberry Pi Pico eine 7-Segment-Anzeige steuerst. Durch die serielle Datenübertragung an das Schieberegister lassen sich mehrere Ausgänge effizient mit nur wenigen GPIO-Pins verwalten. Diese Technik spart nicht nur wertvolle I/O-Ressourcen, sondern ermöglicht auch die Erweiterung deiner Projekte um weitere LEDs, Displays oder andere Peripheriegeräte.
