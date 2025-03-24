.. note:: 

    Hallo und herzlich willkommen in der SunFounder-Community für Raspberry Pi-, Arduino- und ESP32-Enthusiasten auf Facebook! Tauche mit anderen Technikbegeisterten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum beitreten?**

    - **Expertenunterstützung**: Erhalte Hilfe bei technischen Problemen und Fragen nach dem Kauf – durch unsere Community und unser Team.
    - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um deine Fähigkeiten weiterzuentwickeln.
    - **Exklusive Vorschauen**: Erhalte frühzeitige Informationen über neue Produkte und einen exklusiven Einblick.
    - **Sonderrabatte**: Profitiere von exklusiven Angeboten für unsere neuesten Produkte.
    - **Aktionen & Gewinnspiele**: Nimm an festlichen Aktionen und spannenden Verlosungen teil.

    👉 Bereit, gemeinsam mit uns zu entdecken und zu entwickeln? Klicke auf [|link_sf_facebook|] und mach noch heute mit!

.. _py_74hc_4dig:

5.3 Zeitmesser
================================


In dieser Lektion lernst du, wie man ein **4-stelliges 7-Segment-Display** mit 
dem Raspberry Pi Pico 2 W verwendet, um einen einfachen Zeitmesser zu erstellen. 
Die Anzeige zählt jede Sekunde hoch und zeigt die vergangene Zeit in Sekunden an.

**Benötigte Komponenten**

Für dieses Projekt benötigen wir folgende Bauteile.

Ein vollständiges Kit ist besonders praktisch – hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name
        - ENTHALTENE TEILE
        - LINK
    *   - Pico 2 W Starter Kit
        - 450+
        - |link_pico2w_kit|

Alternativ kannst du die Komponenten auch einzeln über die folgenden Links beziehen:


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

**Funktionsweise des 4-stelligen 7-Segment-Displays**

Ein 4-stelliges 7-Segment-Display besteht aus vier einzelnen 7-Segment-Anzeigen, die zu einem Modul zusammengefasst sind. Alle Ziffern teilen sich die gleichen Segmentleitungen (**a** bis **g** und **dp**), aber jede Ziffer hat eine eigene **gemeinsame Kathode** zur Auswahl der aktiven Stelle.

Um unterschiedliche Zahlen gleichzeitig auf den einzelnen Ziffern anzeigen zu können, wird **Multiplexing** eingesetzt. Dabei werden die Ziffern nacheinander sehr schnell aktualisiert, sodass durch die Trägheit des menschlichen Auges der Eindruck entsteht, alle Ziffern seien gleichzeitig sichtbar.

|4digit_control_pins|

**Schaltplan**

|sch_4dig|

Die Verdrahtung folgt im Wesentlichen dem gleichen Prinzip wie bei :ref:`py_74hc_led`, nur dass hier die Ausgänge Q0–Q7 mit den Segmenten a–g und dp des 4-stelligen Displays verbunden werden.

Die Pins GP10 bis GP13 wählen dabei die aktive Ziffer aus.

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


* **Gemeinsame Kathoden (Ziffernauswahl):**


  * **Ziffer 1 (linke Stelle):** Verbinde mit **GP10** am Pico
  * **Ziffer 2:** Verbinde mit **GP11**
  * **Ziffer 3:** Verbinde mit **GP12**
  * **Ziffer 4 (rechte Stelle):** Verbinde mit **GP13**


**Code schreiben**

Wir schreiben nun ein MicroPython-Programm, das jede Sekunde hochzählt und den aktuellen Zählerstand auf dem 4-stelligen Display anzeigt.

.. note::

    * Öffne ``5.3_time_counter.py`` aus ``pico-2w-kit-main/micropython`` oder kopiere den Code in Thonny, dann auf „Run“ klicken oder F5 drücken.
    * Achte darauf, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx.

.. code-block:: python

    import machine
    import utime

    # Define the binary codes for each digit (0-9)
    SEGMENT_CODES = [
        0x3F,  # 0
        0x06,  # 1
        0x5B,  # 2
        0x4F,  # 3
        0x66,  # 4
        0x6D,  # 5
        0x7D,  # 6
        0x07,  # 7
        0x7F,  # 8
        0x6F   # 9
    ]

    # Initialize the control pins for 74HC595
    SDI = machine.Pin(18, machine.Pin.OUT)   # Serial Data Input (DS)
    RCLK = machine.Pin(19, machine.Pin.OUT)  # Register Clock (STCP)
    SRCLK = machine.Pin(20, machine.Pin.OUT) # Shift Register Clock (SHCP)

    # Initialize digit select pins (common cathodes)
    digit_pins = [
        machine.Pin(10, machine.Pin.OUT),  # Digit 1
        machine.Pin(11, machine.Pin.OUT),  # Digit 2
        machine.Pin(12, machine.Pin.OUT),  # Digit 3
        machine.Pin(13, machine.Pin.OUT)   # Digit 4
    ]

    # Function to send data to 74HC595
    def shift_out(data):
        RCLK.low()
        for bit in range(7, -1, -1):
            SRCLK.low()
            bit_val = (data >> bit) & 0x01
            SDI.value(bit_val)
            SRCLK.high()
        RCLK.high()

    # Function to display a digit at a specific position
    def display_digit(position, digit):
        # Turn off all digits
        for dp in digit_pins:
            dp.high()
        # Send segment data
        shift_out(SEGMENT_CODES[digit])
        # Activate the selected digit (common cathode is active low)
        digit_pins[position].low()
        # Small delay to allow the digit to be visible
        utime.sleep_ms(5)
        # Turn off the digit
        digit_pins[position].high()

    # Function to display a number on the 4-digit display
    def display_number(number):
        # Extract individual digits
        digits = [
            (number // 1000) % 10,
            (number // 100) % 10,
            (number // 10) % 10,
            number % 10
        ]
        # Display each digit rapidly
        for i in range(4):
            display_digit(i, digits[i])

    # Main loop
    counter = 0
    last_update = utime.ticks_ms()

    while True:
        # Update the counter every 1000 ms (1 second)
        current_time = utime.ticks_ms()
        if utime.ticks_diff(current_time, last_update) >= 1000:
            counter += 1
            if counter > 9999:
                counter = 0
            last_update = current_time

        # Continuously refresh the display
        display_number(counter)

Beim Ausführen des Codes zeigt das 4-stellige 7-Segment-Display einen Zähler an, der jede Sekunde um eins erhöht wird – von 0 bis 9999. Danach beginnt er wieder bei 0.

**Den Code verstehen**

#. Module importieren:

   * ``machine``: Zugriff auf GPIOs und Hardware-Funktionen.
   * ``utime``: Funktionen für Zeitmessung und Verzögerung.

#. Segmentcodes definieren:

   Jeder Eintrag entspricht den Segmenten, die leuchten müssen, um eine Ziffer darzustellen. Die Werte sind im Hexadezimalformat angegeben.

   .. code-block:: python

        # Binärcodes für jede Ziffer (0–9) definieren
        SEGMENT_CODES = [
            0x3F,  # 0
            0x06,  # 1
            0x5B,  # 2
            0x4F,  # 3
            0x66,  # 4
            0x6D,  # 5
            0x7D,  # 6
            0x07,  # 7
            0x7F,  # 8
            0x6F   # 9
        ]

#. Steuerpins initialisieren:
   
   Weist die GPIO-Pins des Pico zur Ansteuerung des 74HC595 zu.

   .. code-block:: python

        SDI = machine.Pin(18, machine.Pin.OUT)
        RCLK = machine.Pin(19, machine.Pin.OUT)
        SRCLK = machine.Pin(20, machine.Pin.OUT)


#. Ziffernauswahl-Pins initialisieren:

   Steuert, welche Ziffer aktiv ist (aktive Low bei gemeinsamer Kathode).

   .. code-block:: python

        digit_pins = [
            machine.Pin(10, machine.Pin.OUT),
            machine.Pin(11, machine.Pin.OUT),
            machine.Pin(12, machine.Pin.OUT),
            machine.Pin(13, machine.Pin.OUT)
        ]

#. Funktion ``shift_out`` definieren:

   * Sendet 8 Bits an den 74HC595.
   * Beginnt mit dem höchstwertigen Bit (MSB).
   * Taktet die Daten über die Shift- und Register-Takte ein.

   .. code-block:: python

        def shift_out(data):
            RCLK.low()
            for bit in range(7, -1, -1):
                SRCLK.low()
                bit_val = (data >> bit) & 0x01
                SDI.value(bit_val)
                SRCLK.high()
            RCLK.high()

#. Funktion ``display_digit`` definieren:

   * Schaltet alle Ziffern aus.
   * Sendet den Segmentcode für die gewünschte Ziffer.
   * Aktiviert die entsprechende Ziffer durch Setzen auf Low.
   * Fügt eine kurze Verzögerung zur Sichtbarkeit hinzu.
   * Schaltet die Ziffer anschließend wieder aus.

   .. code-block:: python

        def display_digit(position, digit):
            for dp in digit_pins:
                dp.high()
            shift_out(SEGMENT_CODES[digit])
            digit_pins[position].low()
            utime.sleep_ms(5)
            digit_pins[position].high()


#. Funktion ``display_number`` definieren:

   * Zerlegt die Zahl in ihre Einzelziffern.
   * Ruft für jede Ziffer schnell nacheinander ``display_digit`` auf, um den Multiplexing-Effekt zu erzeugen.

   .. code-block:: python

        def display_number(number):
            # Einzelziffern extrahieren
            digits = [
                (number // 1000) % 10,
                (number // 100) % 10,
                (number // 10) % 10,
                number % 10
            ]
            # Jede Ziffer zügig anzeigen
            for i in range(4):
                display_digit(i, digits[i])

#. Hauptschleife:

   * Erhöht den Zähler jede Sekunde.
   * Setzt den Zähler zurück, wenn 9999 erreicht ist.
   * Ruft kontinuierlich ``display_number`` auf, um das Display zu aktualisieren.

   .. code-block:: python

        counter = 0
        last_update = utime.ticks_ms()

        while True:
            current_time = utime.ticks_ms()
            if utime.ticks_diff(current_time, last_update) >= 1000:
                counter += 1
                if counter > 9999:
                    counter = 0
                last_update = current_time

            display_number(counter)


**Weitere Experimente**

* Reset-Taste hinzufügen:

  Verbinde eine Taste mit dem Pico, um den Zähler bei Betätigung zurückzusetzen.

* Andere Daten anzeigen:

  Ändere den Code, um Sensordaten wie Temperatur oder Helligkeit anzuzeigen.

* Anzeigehelligkeit anpassen:

  Passe die Verzögerung ``utime.sleep_ms(5)`` in der Funktion ``display_digit`` an, um die Anzeigezeit jeder Ziffer zu steuern – das beeinflusst die Helligkeit.

* Stoppuhr erstellen:

  Implementiere Start-, Stopp- und Reset-Funktionen, um das Display als Stoppuhr zu verwenden.

**Fazit**

In dieser Lektion hast du gelernt, wie man ein 4-stelliges 7-Segment-Display zusammen mit einem 74HC595-Schieberegister verwendet, um einen Zeitmesser mit dem Raspberry Pi Pico 2 W zu bauen. Durch das Verständnis von Multiplexing und effizientem Timing kannst du mit nur wenigen GPIO-Pins dynamische Mehrstellenanzeigen realisieren.
