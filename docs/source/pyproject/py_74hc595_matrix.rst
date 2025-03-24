.. note:: 

    Hallo und herzlich willkommen in der SunFounder-Community für Raspberry Pi-, Arduino- und ESP32-Enthusiasten auf Facebook! Tauche gemeinsam mit Gleichgesinnten noch tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum beitreten?**

    - **Expertenunterstützung**: Erhalte Unterstützung bei technischen Herausforderungen und nach dem Kauf – von unserem Team und der Community.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erfahre vor allen anderen von neuen Produkten und erhalte exklusive Einblicke.
    - **Sonderrabatte**: Profitiere von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Aktionen und Gewinnspiele**: Nimm an spannenden Verlosungen und saisonalen Aktionen teil.

    👉 Bereit, gemeinsam mit uns kreativ zu werden? Klicke auf [|link_sf_facebook|] und sei dabei!

.. _py_74hc_788bs:

5.4 8x8 Pixel-Grafiken
=============================

In dieser Lektion lernst du, wie man eine **8x8-LED-Matrix** mit dem Raspberry Pi Pico 2 W und zwei **74HC595-Schieberegistern** steuert. Wir zeigen dir, wie du Muster und einfache Grafiken erzeugst, indem du einzelne LEDs in der Matrix gezielt ansteuerst.

* :ref:`cpn_dot_matrix`
* :ref:`cpn_74hc595`

**Benötigte Komponenten**

Für dieses Projekt brauchst du folgende Bauteile.

Am einfachsten ist es, ein Komplett-Kit zu verwenden – hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ENTHALTENE TEILE
        - LINK
    *   - Pico 2 W Starter Kit	
        - 450+
        - |link_pico2w_kit|

Du kannst die Teile auch einzeln über die folgenden Links kaufen:


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
        - :ref:`cpn_dot_matrix`
        - 1
        - 
    *   - 6
        - :ref:`cpn_74hc595`
        - 2
        - |link_74hc595_buy|

**Funktionsweise der 8x8-LED-Matrix**

Die 8x8-Punktmatrix wird über zwei **74HC595-Schieberegister** gesteuert – eines übernimmt die Zeilen, das andere die Spalten. Beide Chips teilen sich die GPIO-Pins **GP18**, **GP19** und **GP20** des Pico, was viele I/O-Pins einspart.

Der Pico sendet jeweils eine 16-Bit-Zahl: Die ersten 8 Bits gehen an den 74HC595 für die Zeilen, die restlichen 8 Bits an den für die Spalten. So lassen sich gezielt LED-Muster darstellen.

**Q7' (Pin 9)**: Dieser serielle Ausgang des ersten 74HC595 wird mit **DS (Pin 14)** des zweiten verbunden, um mehrere Chips in Serie zu schalten.

**Schaltplan**

|sch_ledmatrix|

Die 8x8-Matrix wird durch zwei **74HC595**-ICs gesteuert – einer für Zeilen, einer für Spalten. Beide nutzen gemeinsam GP18~GP20, was I/O-Pins des Pico 2 W spart.

Der Pico 2 W gibt jeweils eine 16-Bit-Binärzahl aus: 8 Bits für die Zeilen (linker IC), 8 Bits für die Spalten (rechter IC). Damit lassen sich gezielt Muster anzeigen.

Q7': Serieller Ausgangspin, verbunden mit DS des nächsten 74HC595, um eine Reihenschaltung zu ermöglichen.

**Verdrahtung**

Da der Aufbau etwas komplex ist, gehen wir Schritt für Schritt vor.

**Schritt 1:** Stecke den Pico 2 W, die LED-Matrix und beide 74HC595-Chips ins 
Breadboard. Verbinde 3.3V und GND des Pico mit den Stromschienen. Pin 16 und 10 
beider ICs gehen an VCC, Pin 13 und 8 an GND.

.. note::
   In der obigen Fritzing-Grafik ist die Seite mit der Beschriftung unten.

|wiring_ledmatrix_4|

**Schritt 2:** Verbinde Pin 11 beider 74HC595 miteinander und mit GP20. 
Dann Pin 12 beider Chips mit GP19. Schließlich Pin 14 des linken 74HC595 
mit GP18 und Pin 9 mit Pin 14 des rechten Chips.

|wiring_ledmatrix_3|

**Schritt 3:** Der rechte 74HC595 steuert die Spalten. Die Zuordnung findest 
du in der folgenden Tabelle – Q0 bis Q7 sind mit den Pins 13, 3, 4, 10, 6, 11, 15 
und 16 der Matrix verbunden.

+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **74HC595**        | **Q0** | **Q1** | **Q2** | **Q3** | **Q4** | **Q5** | **Q6** | **Q7** |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **LED Dot Matrix** | **13** | **3**  | **4**  | **10** | **6**  | **11** | **15** | **16** |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+

|wiring_ledmatrix_2|

**Schritt 4:** Jetzt die Zeilen anschließen. Der linke 74HC595 steuert die 
Zeilen der Matrix. Siehe Tabelle: Q0 bis Q7 sind mit den Pins 9, 14, 8, 12, 
1, 7, 2 und 5 verbunden.

+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **74HC595**        | **Q0** | **Q1** | **Q2** | **Q3** | **Q4** | **Q5** | **Q6** | **Q7** |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **LED Dot Matrix** | **9**  | **14** | **8**  | **12** | **1**  | **7**  | **2**  | **5**  |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+

|wiring_ledmatrix_1|

**Programmcode schreiben**

Jetzt schreiben wir ein MicroPython-Programm, das ein Muster auf der Matrix anzeigt.

.. note::

    * Öffne ``5.4_8x8_pixel_graphics.py`` im Verzeichnis ``pico-2w-kit-main/micropython`` oder kopiere den Code in Thonny. Klicke auf „Run“ oder drücke F5.
    * Achte darauf, dass MicroPython (Raspberry Pi Pico).COMxx als Interpreter ausgewählt ist.

.. code-block:: python

    import machine
    import time

    # Define the pins connected to the 74HC595 shift register
    sdi = machine.Pin(18, machine.Pin.OUT)   # Serial Data Input
    rclk = machine.Pin(19, machine.Pin.OUT)  # Storage Register Clock (RCLK)
    srclk = machine.Pin(20, machine.Pin.OUT) # Shift Register Clock (SRCLK)

    # Define the glyph data for the letter 'X' with lit pixels and background off
    glyph = [0x7E, 0xBD, 0xDB, 0xE7, 0xE7, 0xDB, 0xBD, 0x7E]

    def hc595_in(dat):
        """
        Shifts 8 bits of data into the 74HC595 shift register.
        """
        for bit in range(7, -1, -1):
            srclk.low()
            sdi.value((dat >> bit) & 1)  # Output data bit by bit
            srclk.high()
            time.sleep_us(1)  # Short delay to ensure proper timing

    def hc595_out():
        """
        Latches the data from the shift register to the storage register,
        updating the outputs.
        """
        rclk.high()
        rclk.low()

    while True:
        for i in range(8):
            hc595_in(glyph[i])       # Send the column data for the current row
            hc595_in(1 << i)         # Activate the current row
            hc595_out()              # Update the display
            time.sleep_ms(1)         # Delay for visual persistence

Wenn du diesen Code ausführst, wird auf der LED-Matrix ein „X“ dargestellt, bei dem die LEDs entsprechend leuchten.

**Den Code verstehen**

#. Module importieren:

   * ``machine``: Ermöglicht die Steuerung der GPIO-Pins.
   * ``time``: Wird für zeitliche Steuerung und Verzögerungen verwendet.

#. Pinbelegung definieren:

   * ``sdi``: Serielle Dateneingabe zum Schieberegister.
   * ``rclk``: Takt zum Speichern der Daten in den Ausgängen.
   * ``srclk``: Takt zum Schieben der Daten ins Register.

#. Zeichenmuster „X“:

   * Jedes Element steht für eine Zeile der Matrix.
   * Die Hex-Werte bestimmen, welche LEDs in dieser Zeile leuchten.
   * Das ergibt ein symmetrisches „X“-Muster.

   .. code-block:: python

        glyph = [0x7E, 0xBD, 0xDB, 0xE7, 0xE7, 0xDB, 0xBD, 0x7E]

#. Funktion ``hc595_in(dat)``:

   * Diese Funktion sendet 8 Bits (``dat``) seriell an das Schieberegister.
   * Dabei wird vom höchstwertigen zum niederwertigsten Bit iteriert.
   * Der ``srclk``-Pin wird getoggelt, um jedes Bit in das Register zu schieben.
   * Der ``sdi``-Pin legt abhängig vom aktuellen Bit den Datenpegel auf High oder Low.

   .. code-block:: python

        def hc595_in(dat):
            """
            Shifts 8 bits of data into the 74HC595 shift register.
            """
            for bit in range(7, -1, -1):
                srclk.low()
                sdi.value((dat >> bit) & 1)  # Output data bit by bit
                srclk.high()
                time.sleep_us(1)  # Short delay to ensure proper timing


#. Funktion ``hc595_out()``:

   * Diese Funktion übernimmt die verschobenen Daten vom Schieberegister ins Ausgaberegister.
   * Eine steigende Flanke am ``rclk``-Pin überträgt die Daten auf die Ausgänge und aktualisiert die LEDs.

   .. code-block:: python

        def hc595_out():

            rclk.high()
            rclk.low()

#. Hauptschleife:

   * Die Schleife aktualisiert kontinuierlich das Display, um ein dauerhaft sichtbares „X“ zu erzeugen.
   * Die ``for``-Schleife durchläuft alle Zeilenindizes von 0 bis 7.
   * ``hc595_in(1 << i)`` aktiviert jeweils eine einzelne Zeile, indem genau ein Bit gesetzt wird.
   * ``hc595_in(glyph[i])`` sendet die Spalteninformationen für die aktuelle Zeile und bestimmt, welche LEDs leuchten.
   * ``hc595_out()`` übernimmt die Daten ins Ausgaberegister.
   * ``time.sleep_ms(1)`` sorgt dafür, dass jede Zeile lang genug angezeigt wird, um vom menschlichen Auge wahrgenommen zu werden.
   * Durch das schnelle Umschalten entsteht der Eindruck, dass das komplette „X“ gleichzeitig dargestellt wird.

   .. code-block:: python

        while True:
            for i in range(8):
                hc595_in(glyph[i])       # Send the column data for the current row
                hc595_in(1 << i)         # Activate the current row
                hc595_out()              # Update the display
                time.sleep_ms(1)         # Delay for visual persistence


**Weitere Experimente**

* Muster ändern

  Ersetze die Musterliste durch folgende Arrays, um unterschiedliche Grafiken anzuzeigen. Ersetze in deinem Code glyph durch ``pattern_heart`` oder ``pattern_smile``, um verschiedene Bilder darzustellen.

  .. code-block:: python

        # Herzform
        pattern_heart = [
            0b11111111,
            0b10011001,
            0b00000000,
            0b00000000,
            0b00000000,
            0b10000001,
            0b11000011,
            0b11100111
        ]

        # Smiley-Gesicht
        pattern_smile = [
            0b11000011,  # Row 0
            0b10111101,  # Row 1
            0b01011010,  # Row 2
            0b01111110,  # Row 3
            0b01011010,  # Row 4
            0b01100110,  # Row 5
            0b10111101,  # Row 6
            0b11000011   # Row 7
        ]


* Anzeige animieren

  Erstelle mehrere Muster und lasse sie abwechselnd anzeigen, um Animationen zu erzeugen:

  .. code-block:: python

        import machine
        import time
        
        # Pins für die 74HC595-Schieberegister definieren
        sdi = machine.Pin(18, machine.Pin.OUT)   # Serial Data Input
        rclk = machine.Pin(19, machine.Pin.OUT)  # Register Clock (Latch)
        srclk = machine.Pin(20, machine.Pin.OUT) # Shift Register Clock
        
        # Herzform
        pattern_heart = [
            0b11111111,
            0b10011001,
            0b00000000,
            0b00000000,
            0b00000000,
            0b10000001,
            0b11000011,
            0b11100111
        ]
        
        # Smiley-Gesicht
        pattern_smile = [
            0b11000011,  # Row 0
            0b10111101,  # Row 1
            0b01011010,  # Row 2
            0b01111110,  # Row 3
            0b01011010,  # Row 4
            0b01100110,  # Row 5
            0b10111101,  # Row 6
            0b11000011   # Row 7
        ]
        
        def hc595_in(dat):
            """
            Shift 8 bits of data into the 74HC595 shift register.
            """
            for bit in range(7, -1, -1):
                srclk.low()                            # Prepare to shift data
                sdi.value((dat >> bit) & 1)            # Set data bit
                srclk.high()                           # Shift data bit into register
                time.sleep_us(1)                       # Short delay for timing
        
        def hc595_out():
            """
            Latch the shifted data to the output pins of the 74HC595.
            """
            rclk.high()                               # Latch data (rising edge)
            rclk.low()                                # Prepare for next data
        
        def display_pattern(pattern):
            """
            Display a given 8x8 pattern on the LED matrix.
            """
            for _ in range(500):                      # Display the pattern for a certain duration
                for i in range(8):
                    hc595_in(pattern[i])              # Send column data for current row
                    hc595_in(1 << i)                  # Activate current row
                    hc595_out()                       # Update the output
                    time.sleep_ms(1)                  # Short delay for persistence
        
        while True:
            display_pattern(pattern_heart)            # Display the heart shape
            display_pattern(pattern_smile)            # Display the smiley face

* Eigene Muster erstellen

  Jedes Byte steht für eine Zeile; Bits mit dem Wert 0 schalten die entsprechende LED ein. Definiere eigene Musterlisten, um individuelle Symbole oder Bilder darzustellen.

**Fazit**

In dieser Lektion hast du gelernt, wie man eine 8x8-LED-Matrix mit dem Raspberry Pi Pico 2 W und zwei 74HC595-Schieberegistern steuert. Durch das gezielte Setzen von Bits und den Einsatz von Schieberegistern kannst du Muster und einfache Grafiken auf der Matrix darstellen.
