.. note:: 

    Hallo und herzlich willkommen in der SunFounder-Community für Raspberry Pi-, Arduino- und ESP32-Enthusiasten auf Facebook! Entdecke gemeinsam mit anderen Technikbegeisterten die Welt von Raspberry Pi, Arduino und ESP32 noch intensiver.

    **Warum beitreten?**

    - **Expertenunterstützung**: Erhalte Hilfe bei technischen Herausforderungen und Fragen nach dem Kauf – durch unser Team und die Community.
    - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um dein Wissen zu erweitern.
    - **Exklusive Vorschauen**: Erfahre frühzeitig von neuen Produktveröffentlichungen.
    - **Sonderrabatte**: Profitiere von exklusiven Angeboten auf unsere neuesten Produkte.
    - **Aktionen & Gewinnspiele**: Nimm an Verlosungen und festlichen Aktionen teil.

    👉 Bereit, mit uns zu entdecken und zu entwickeln? Klicke auf [|link_sf_facebook|] und mach mit!

.. _py_74hc_led:

5.1 Verwendung des 74HC595-Schieberegisters
==============================================

In dieser Lektion lernst du, wie du mithilfe des **74HC595-Schieberegisters** mehrere LEDs mit nur wenigen GPIO-Pins des Raspberry Pi Pico 2 W steuern kannst. Der 74HC595 ist ein integrierter Schaltkreis (IC), mit dem sich über serielle Eingabe mehrere digitale Ausgänge ansteuern lassen – ideal, wenn viele Ausgänge benötigt werden, aber nur wenige Pins zur Verfügung stehen.

* :ref:`cpn_74hc595`

**Benötigte Komponenten**

Für dieses Projekt benötigen wir folgende Bauteile.

Am bequemsten ist es, ein Komplett-Kit zu kaufen – hier ist der Link:

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

Der **74HC595** ist ein 8-Bit-Schieberegister mit serieller Eingabe und parallelen Ausgängen sowie integrierten Latches. Er ermöglicht es, serielle Daten in parallele Signale umzuwandeln und dadurch acht Ausgänge mit nur drei GPIO-Pins des Pico zu steuern.

**Wichtige Pins des 74HC595:**

|img_74jc595_pin|

* **DS (Pin 14)**: Serielle Dateneingabe  
* **SHCP (Pin 11)**: Takteingang für das Schieberegister  
* **STCP (Pin 12)**: Takteingang für das Speicheregister (Latch)  
* **OE (Pin 13)**: Ausgangsfreigabe (aktiv Low, mit GND verbinden)  
* **MR (Pin 10)**: Master-Reset (aktiv Low, mit 3.3V verbinden)  
* **Q0–Q7 (Pins 15, 1–7)**: Parallele Ausgänge  
* **VCC (Pin 16)**: Mit 3.3V verbinden  
* **GND (Pin 8)**: Mit Masse verbinden

**Schaltplan**

|sch_74hc_led|



**Verdrahtung**

.. The 74HC595 is a 16-pin IC with a semi-circular notch on one side (usually the left side of the label). With the notch facing upwards, its pins are shown in the diagram below.


.. Refer to the figure below to build the circuit.


|wiring_74hc_led|

.. 1. Verbinde 3V3 und GND des Pico 2 W mit den Stromschienen des Breadboards.
.. #. Setze den 74HC595 mittig ins Breadboard (über den Mittelsteg).
.. #. Verbinde GP0 mit Pin 14 (DS) des 74HC595.
.. #. Verbinde GP1 mit Pin 12 (STCP).
.. #. Verbinde GP2 mit Pin 11 (SHCP).
.. #. Verbinde Pin 16 (VCC) und Pin 10 (MR) mit der positiven Stromschiene.
.. #. Verbinde Pin 8 (GND) und Pin 13 (OE) mit der Masse.
.. #. Setze 8 LEDs ins Breadboard, Anode an die Pins Q0–Q7 (15, 1–7) des 74HC595.
.. #. Die Kathoden der LEDs kommen über je einen 220Ω-Widerstand zur Masse.



**Code schreiben**

Nun schreiben wir ein MicroPython-Programm, um die LEDs über das 74HC595 zu steuern.

.. note::

    * Öffne ``5.1_microchip_74hc595.py`` aus dem Ordner ``pico-2w-kit-main/micropython`` oder kopiere den Code in Thonny und klicke auf „Run“ oder drücke F5.

    * Achte darauf, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx.

.. code-block:: python

    import machine
    import utime

    # Define the pins connected to the 74HC595
    SDI = machine.Pin(0, machine.Pin.OUT)   # Serial Data Input (DS)
    RCLK = machine.Pin(1, machine.Pin.OUT)  # Register Clock (STCP)
    SRCLK = machine.Pin(2, machine.Pin.OUT) # Shift Register Clock (SHCP)

    # Function to send data to 74HC595
    def shift_out(data):
        for bit in range(8):
            # Extract the highest bit and send it first
            bit_val = (data & 0x80) >> 7
            SDI.value(bit_val)
            # Pulse the Shift Register Clock
            SRCLK.high()
            utime.sleep_us(1)
            SRCLK.low()
            utime.sleep_us(1)
            # Shift data left by 1 for the next bit
            data = data << 1
        # Pulse the Register Clock to latch the data
        RCLK.high()
        utime.sleep_us(1)
        RCLK.low()
        utime.sleep_us(1)

    # Main loop to demonstrate shifting patterns
    while True:
        # Light up LEDs one by one from Q0 to Q7
        for i in range(8):
            data = 1 << i
            shift_out(data)
            utime.sleep(0.2)
        # Light up LEDs one by one from Q7 to Q0
        for i in range(7, -1, -1):
            data = 1 << i
            shift_out(data)
            utime.sleep(0.2)
        # Create a moving bar effect
        for i in range(9):
            data = (1 << i) - 1
            shift_out(data)
            utime.sleep(0.2)
        # Turn off all LEDs
        shift_out(0x00)
        utime.sleep(0.5)

Beim Ausführen des Codes zeigen die LEDs dynamische Lichteffekte:

* **Erste Sequenz**: Die LEDs leuchten nacheinander von links nach rechts auf – ein laufendes Licht.
* **Zweite Sequenz**: Die LEDs leuchten nacheinander von rechts nach links – das Licht kehrt zurück.
* **Dritte Sequenz**: Eine wachsende Lichtleiste von links nach rechts – immer mehr LEDs leuchten.
* **Abschließend**: Alle LEDs gehen kurz aus, bevor die Animation von vorne beginnt.

Das Ergebnis ist eine auffällige, sich wiederholende Lichtanimation.

**Den Code verstehen**

#. Module importieren:

   * ``machine``: Ermöglicht Zugriff auf die GPIO-Pins.
   * ``utime``: Stellt Zeitfunktionen bereit.

#. Steuerpins definieren:

   GPIO-Pins, die mit dem 74HC595 verbunden sind, werden festgelegt.

   .. code-block:: python

      SDI = machine.Pin(0, machine.Pin.OUT)   # Data Input
      RCLK = machine.Pin(1, machine.Pin.OUT)  # Latch Clock
      SRCLK = machine.Pin(2, machine.Pin.OUT) # Shift Clock

#. Funktion zum Seriellen Ausgeben (Shift Out):

   * Diese Funktion überträgt 8 Datenbits an das Schieberegister.
   * Dabei wird das höchstwertige Bit (MSB) zuerst gesendet.
   * Der Taktpin des Schieberegisters (SRCLK) wird getoggelt, um jedes Bit einzuschieben.
   * Nachdem alle Bits übertragen wurden, wird der Register-Takt (RCLK) ausgelöst, um die Daten an den Ausgängen zu übernehmen.

   .. code-block:: python

      def shift_out(data):
          for bit in range(8):
              bit_val = (data & 0x80) >> 7
              SDI.value(bit_val)
              SRCLK.high()
              utime.sleep_us(1)
              SRCLK.low()
              utime.sleep_us(1)
              data = data << 1
          RCLK.high()
          utime.sleep_us(1)
          RCLK.low()
          utime.sleep_us(1)

#. Hauptschleife:

   * LEDs einzeln von Q0 bis Q7 einschalten.

   .. code-block:: python

      for i in range(8):
          data = 1 << i
          shift_out(data)
          utime.sleep(0.2)


   * LEDs einzeln von Q7 bis Q0 einschalten.

   .. code-block:: python

      for i in range(7, -1, -1):
          data = 1 << i
          shift_out(data)
          utime.sleep(0.2)

   * Eine wachsende Leiste anzeigen.

   .. code-block:: python

      for i in range(9):
          data = (1 << i) - 1
          shift_out(data)
          utime.sleep(0.2)

   * Alle LEDs ausschalten.

   .. code-block:: python

     shift_out(0x00)
     utime.sleep(0.5)

**Weitere Experimente**

* Eigene Muster erstellen:

  Erstelle neue LED-Muster, z. B. wechselndes Blinken:

  .. code-block:: python

    shift_out(0b10101010)

* Mehr LEDs steuern:

  Mehrere 74HC595 in Reihe schalten. Verbinde Pin 9 (Q7’) des ersten mit Pin 14 (DS) des zweiten ICs.

* Mit Sensoren kombinieren:

  Nutze Eingaben von Tastern oder Sensoren, um die Muster dynamisch zu ändern.

**Fazit**

In dieser Lektion hast du gelernt, wie man mit dem 74HC595-Schieberegister die Ausgabemöglichkeiten des Raspberry Pi Pico 2 W erweitert. Diese Technik ist besonders nützlich für Projekte mit vielen Ausgängen und begrenzten GPIO-Ressourcen.

