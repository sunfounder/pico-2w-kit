.. note::

    Hallo und herzlich willkommen in der SunFounder-Community für Raspberry Pi-, Arduino- und ESP32-Enthusiasten auf Facebook! Tauche gemeinsam mit anderen Technikbegeisterten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum beitreten?**

    - **Expertenunterstützung**: Erhalte Unterstützung bei technischen Problemen und nach dem Kauf – von unserem Team und der Community.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Kenntnisse zu erweitern.
    - **Exklusive Vorschauen**: Erfahre frühzeitig von neuen Produktankündigungen und Einblicken.
    - **Sonderrabatte**: Profitiere von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Aktionen & Gewinnspiele**: Nimm an festlichen Aktionen und Verlosungen teil.

    👉 Bereit, gemeinsam mit uns zu entdecken und zu entwickeln? Klicke auf [|link_sf_facebook|] und mach noch heute mit!

.. _py_74hc_7seg:

5.2 Zahlen anzeigen
========================

In dieser Lektion lernst du, wie man mit einem **7-Segment-Display** und dem **74HC595-Schieberegister** Zahlen auf dem Raspberry Pi Pico 2 W darstellen kann. Das 7-Segment-Display ist ein weit verbreitetes elektronisches Bauteil, das in Geräten wie digitalen Uhren, Taschenrechnern und Haushaltsgeräten zur Anzeige numerischer Informationen eingesetzt wird.

Durch die Kombination des 74HC595 mit dem 7-Segment-Display können alle Segmente mit nur wenigen GPIO-Pins gesteuert werden, wodurch wertvolle I/O-Ressourcen für andere Komponenten eingespart werden.

* :ref:`cpn_7_segment`

**Benötigte Komponenten**

Für dieses Projekt benötigen wir folgende Bauteile.

Ein komplettes Kit ist besonders praktisch – hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name
        - ENTHALTENE TEILE
        - LINK
    *   - Pico 2 W Starter Kit
        - 450+
        - |link_pico2w_kit|

Die Bauteile können auch einzeln über folgende Links erworben werden:

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

**Funktionsweise des 7-Segment-Displays**

Ein 7-Segment-Display besteht aus 7 LEDs (Segmenten), die in Form einer Acht angeordnet sind, um Ziffern von 0 bis 9 anzuzeigen. Zusätzlich gibt es eine achte LED für den Dezimalpunkt. Jedes Segment ist mit **a** bis **g** und der Dezimalpunkt mit **dp** beschriftet.

Hier die Segmentbezeichnungen:

|img_7seg_cathode|

Bei einem **gemeinsamen Kathoden-Display** (common cathode) sind alle Kathoden der LEDs mit Masse verbunden.


**Schaltplan**

|sch_74hc_7seg|

Die Verdrahtung erfolgt im Prinzip genauso wie bei :ref:`py_74hc_led`, mit dem Unterschied, dass die Pins Q0–Q7 mit den Segmenten a bis g des 7-Segment-Displays verbunden werden.

.. list-table:: Wiring
    :widths: 15 25
    :header-rows: 1

    *   - :ref:`cpn_74hc595`
        - :ref:`cpn_led` Segmentanzeige
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


.. 1. Connect 3V3 and GND of Pico 2 W to the power bus of the breadboard.
.. #. Insert 74HC595 across the middle gap into the breadboard.
.. #. Connect the GP0 pin of Pico 2 W to the DS pin (pin 14) of 74HC595 with a jumper wire.
.. #. Connect the GP1 pin of Pico 2 W to the STcp pin (12-pin) of 74HC595.
.. #. Connect the GP2 pin of Pico 2 W to the SHcp pin (pin 11) of 74HC595.
.. #. Connect the VCC pin (16 pin) and MR pin (10 pin) on the 74HC595 to the positive power bus.
.. #. Connect the GND pin (8-pin) and CE pin (13-pin) on the 74HC595 to the negative power bus.
.. #. Insert the LED Segment Display into the breadboard, and connect a 220Ω resistor in series with the GND pin to the negative power bus.
.. #. Follow the table below to connect the 74hc595 and LED Segment Display.

|wiring_74hc_7seg|



**Code schreiben**



Wir schreiben nun ein MicroPython-Programm, das die Ziffern 0 bis 9 auf dem 7-Segment-Display anzeigt.

.. note::

    * Öffne ``5.2_number_display.py`` aus ``pico-2w-kit-main/micropython`` oder kopiere den Code in Thonny und klicke auf „Run“ oder drücke F5.
    * Stelle sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx.

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
    SDI = machine.Pin(0, machine.Pin.OUT)   # Serial Data Input (DS)
    RCLK = machine.Pin(1, machine.Pin.OUT)  # Register Clock (STCP)
    SRCLK = machine.Pin(2, machine.Pin.OUT) # Shift Register Clock (SHCP)

    # Function to send data to 74HC595
    def shift_out(data):
        RCLK.low()
        for bit in range(7, -1, -1):
            SRCLK.low()
            bit_val = (data >> bit) & 0x01
            SDI.value(bit_val)
            SRCLK.high()
        RCLK.high()

    # Main loop to display numbers 0-9
    while True:
        for num in range(10):
            shift_out(SEGMENT_CODES[num])
            utime.sleep(0.5)

Beim Ausführen des Codes zeigt das 7-Segment-Display nacheinander die Ziffern 0 bis 9 im 0,5-Sekunden-Takt an. Nach der 9 beginnt die Anzeige wieder bei 0 und wiederholt sich endlos.

**Code-Erklärung**

#. Module importieren:

   * ``machine``: Zugriff auf GPIOs und Hardware-Funktionen.
   * ``utime``: Zeitfunktionen und Delays.

#. Segment-Codes definieren:

   Jeder Eintrag steht für die LEDs, die zur Darstellung einer Ziffer leuchten sollen. Zur besseren Lesbarkeit wird Hexadezimal verwendet.

   .. code-block:: python

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

   Angenommen, das 7-Segment-Display soll die Zahl „1“ anzeigen, dann müssen die Segmente b und c auf High gesetzt werden, während a, d, e, f, g und dp auf Low gesetzt werden.

   |img_1_segment|

   Das bedeutet, dass die Binärzahl „00000110“ ausgegeben werden muss. Zur besseren Lesbarkeit verwenden wir die hexadezimale Schreibweise „0x06“.


#. Steuerpins initialisieren:

   Weist den GPIO-Pins des Pico Steuerfunktionen für den 74HC595 zu.

   .. code-block:: python

      SDI = machine.Pin(0, machine.Pin.OUT)
      RCLK = machine.Pin(1, machine.Pin.OUT)
      SRCLK = machine.Pin(2, machine.Pin.OUT)

#. Funktion ``shift_out`` definieren:

   * Sendet 8 Bits an den 74HC595.
   * Beginnt beim höchstwertigen Bit (MSB).
   * Steuert SRCLK und RCLK entsprechend.

   .. code-block:: python

        def shift_out(data):
            RCLK.low()
            for bit in range(7, -1, -1):
                SRCLK.low()
                bit_val = (data >> bit) & 0x01
                SDI.value(bit_val)
                SRCLK.high()
            RCLK.high()

#. Hauptschleife zur Anzeige der Zahlen:

   * Zählt von 0 bis 9.
   * Ruft shift_out mit dem passenden Segmentcode auf.
   * Wartet 0,5 Sekunden zwischen den Zahlen.

   .. code-block:: python

        while True:
            for num in range(10):
                shift_out(SEGMENT_CODES[num])
                utime.sleep(0.5)

**Segmentcodes verstehen**

Jeder Code bestimmt, welche Segmente zur Anzeige der Ziffer aktiv sind:

* **0**: a, b, c, d, e, f → 0x3F
* **1**: b, c → 0x06
* **2**: a, b, g, e, d → 0x5B
* **3**: a, b, c, d, g → 0x4F
* **4**: b, c, f, g → 0x66
* **5**: a, c, d, f, g → 0x6D
* **6**: a, c, d, e, f, g → 0x7D
* **7**: a, b, c → 0x07
* **8**: a, b, c, d, e, f, g → 0x7F
* **9**: a, b, c, d, f, g → 0x6F

**Weitere Experimente**

* Hexadezimal anzeigen:

  Erweitere die ``SEGMENT_CODES``-Liste um Buchstaben A–F für hexadezimale Darstellung. Beispiel: 'A' = 0x77

* Zähler implementieren:

  Ändere den Code in einen Auf- oder Abwärtszähler. Nutze Taster als Eingabe zur Steuerung.

* Mehrere Displays steuern:

  Kaskadiere mehrere 74HC595, um mehrere Ziffern anzuzeigen. Verwende Multiplexing zur Anzeige mit minimalen GPIOs.

**Fazit**

In dieser Lektion hast du gelernt, wie man mit einem 7-Segment-Display und einem 74HC595-Schieberegister Zahlen mit dem Raspberry Pi Pico 2 W darstellt. Durch das gezielte Setzen binärer Segmentcodes und den Einsatz des Schieberegisters kannst du effizient Ausgänge mit wenigen Pins steuern.
