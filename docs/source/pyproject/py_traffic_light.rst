.. note::
    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in Raspberry Pi, Arduino und ESP32 ein zusammen mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Löse Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Promotionen und Gewinnspiele**: Nimm an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt heute bei!

.. _py_traffic_light:


7.6 Bau eines Ampelsteuergeräts
==============================================================

In diesem Projekt erstellen wir ein **Ampelsteuergerät** mit dem Raspberry Pi Pico 2 W, drei LEDs (rot, gelb, grün) und einem 4-stelligen 7-Segment-Display. Dieses System simuliert eine echte Ampelsequenz und zeigt die verbleibende Zeit für jedes Licht auf dem 7-Segment-Display an.

* **Rotes Licht**: Der Verkehr sollte bei einem blinkenden roten Licht stoppen, was einem Stoppschild entspricht.
* **Gelbes Licht**: Ein Warnsignal, das gleich rot wird. Gelbe Lichter werden in verschiedenen Ländern (Regionen) unterschiedlich interpretiert.
* **Grünes Licht**: Erlaubt dem Verkehr, in die angezeigte Richtung zu fahren.


**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Es ist definitiv praktisch, ein ganzes Kit zu kaufen, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ARTIKEL IN DIESEM KIT
        - LINK
    *   - Pico 2 W Starter Kit	
        - 450+
        - |link_pico2w_kit|

Du kannst sie auch einzeln über die untenstehenden Links kaufen.


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
        - Micro USB-Kabel
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
        - 7(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_4_dit_7_segment`
        - 1
        - 
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|
    *   - 8
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|


**Verständnis der Komponenten**

* **LEDs**: Repräsentieren die Ampeln. Wir steuern sie, um die standardmäßige Ampelsequenz zu simulieren.
* **4-stelliges 7-Segment-Display**: Zeigt den Countdown-Timer für jedes Licht an.
* **74HC595 Schieberegister**: Ermöglicht es uns, mehrere Ausgänge (Segmente und Ziffern des Displays) mit weniger GPIO-Pins am Pico zu steuern.


**Schaltplan**

|sch_traffic_light|


* Dieser Schaltkreis basiert auf dem :ref:`py_74hc_4dig` mit der Ergänzung von 3 LEDs.
* Die 3 roten, gelben und grünen LEDs sind jeweils mit GP7~GP9 verbunden.

**Verdrahtung**


|wiring_traffic_light| 


**Schreiben des Codes**

Wir schreiben ein MicroPython-Skript, das:

* Die Ampelsequenz steuert.
* Den Countdown-Timer auf dem 7-Segment-Display anzeigt.
* Schieberegister verwendet, um das Display zu steuern.

.. note::

    * Öffne die Datei ``7.6_traffic_light.py`` aus ``pico-2w-kit-main/micropython`` oder kopiere den Code in Thonny, dann klicke auf "Ausführen" oder drücke F5.
    * Stelle sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx. 

.. code-block:: python

    import machine
    import utime
    from machine import Timer

    # Initialize LED pins
    led_pins = [7, 8, 9]  # Green, Yellow, Red LEDs connected to GP7, GP8, GP9
    leds = [machine.Pin(pin, machine.Pin.OUT) for pin in led_pins]

    # Define the duration for each traffic light color in seconds [Green, Yellow, Red]
    light_time = [30, 5, 30]  # [Green, Yellow, Red]

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

    # Function to update the LEDs based on the current state
    def update_leds(state):
        # States: 0 = Green, 1 = Yellow, 2 = Red
        for i in range(3):
            leds[i].value(0)
        leds[state].value(1)

    # Timer variables
    counter = light_time[0]  # Start with green light duration
    current_state = 0  # 0 = Green, 1 = Yellow, 2 = Red

    # Timer interrupt callback to update the traffic light state and counter
    def timer_callback(t):
        global counter, current_state
        counter -= 1
        if counter <= 0:
            current_state = (current_state + 1) % 3  # Cycle through the states
            counter = light_time[current_state]  # Reset counter for the new state
            update_leds(current_state)

    # Initialize the timer
    timer = Timer(period=1000, mode=Timer.PERIODIC, callback=timer_callback)

    # Initial LED state
    update_leds(current_state)

    # Main loop
    try:
        while True:
            display_number(counter)
    except KeyboardInterrupt:
        timer.deinit()
        print("Program stopped.")


Wenn der Code ausgeführt wird, leuchtet zuerst die grüne LED auf, und das Display zeigt einen Countdown von 30 an.
Nach 30 Sekunden leuchtet die gelbe LED auf, und das Display zählt von 5 herunter.
Dann leuchtet die rote LED auf, und das Display zählt von 30 herunter.
Der Zyklus wiederholt sich unendlich.

**Verständnis des Codes**

#. Imports und Initialisierung:

   * ``machine``: Bietet Zugang zu hardwarebezogenen Funktionen.
   * ``utime``: Bietet zeitbezogene Funktionen.
   * ``Timer``: Wird verwendet, um Hardware-Timer zu erstellen.

#. LED-Initialisierung:

   Definiert GPIO-Pins für die roten, gelben und grünen LEDs. Initialisiert jeden Pin als Ausgang.

   .. code-block:: python

        led_pins = [7, 8, 9]  # Grüne, gelbe, rote LEDs verbunden mit GP7, GP8, GP9
        leds = [machine.Pin(pin, machine.Pin.OUT) for pin in led_pins]

#. Ampelzeiten:

   Gibt die Dauer (in Sekunden) für jeden Ampelzustand an.

   .. code-block:: python

        light_time = [30, 5, 30]  # [Grün, Gelb, Rot]

#. Anzeigefunktionen:

   * ``display_digit(digit)``: Aktiviert eine spezifische Ziffer auf der Anzeige.
   * ``shift_out(data)``: Sendet Daten an das Schieberegister.
   * ``display_number(num)``: Zerlegt die Zahl in Ziffern und zeigt sie durch Multiplexing an.

#. ``update_leds(state)`` Funktion:

   * Aktualisiert den Zustand der LEDs basierend auf dem aktuellen Ampelzustand.
   * Schaltet alle LEDs aus und dann die LED ein, die dem aktuellen Zustand entspricht.

   .. code-block:: python

        def update_leds(state):
            # Zustände: 0 = Grün, 1 = Gelb, 2 = Rot
            for i in range 3:
                leds[i].value(0)
            leds[state].value(1)

#. ``timer_callback(t)`` Funktion:

   * Timer-Interrupt-Rückruffunktion.
   * Verringert den Zähler jede Sekunde.
   * Wenn der Zähler null erreicht, wechselt er zum nächsten Ampelzustand und setzt den Zähler zurück.

   .. code-block:: python

        def timer_callback(t):
            global counter, current_state
            counter -= 1
            if counter <= 0:
                current_state = (current_state + 1) % 3  # Durchlaufe die Zustände
                counter = light_time[current_state]  # Setze Zähler für den neuen Zustand zurück
                update_leds(current_state)

#. Hauptausführung:

   * Anfangsvariablen: Setzt den Anfangszustand auf grün und initialisiert den Zähler.

     .. code-block:: python

        counter = light_time[0]  # Beginne mit grüner Lichtdauer
        current_state = 0  # 0 = Grün, 1 = Gelb, 2 = Rot
   
   * Timer initialisieren: Erstellt einen periodischen Timer, der alle 1000 Millisekunden (1 Sekunde) auslöst und timer_callback aufruft.


     .. code-block:: python

        timer = Timer(period=1000, mode=Timer.PERIODIC, callback=timer_callback)
   
   * Setze den anfänglichen LED-Zustand: Stellt sicher, dass die richtige LED zu Beginn leuchtet.

     .. code-block:: python

        update_leds(current_state)

   * Hauptschleife: Betritt eine Endlosschleife, die den Countdown-Timer anzeigt. Behandelt eine Tastaturunterbrechung (z. B. Ctrl+C), um den Timer sicher zu deinitialisieren und zu beenden.


     .. code-block:: python

        try:
            while True:
                display_number(counter)
        except KeyboardInterrupt:
            timer.deinit()
            print("Program stopped.")



**Weiteres Experimentieren**

* Zeit anpassen:

  Ändere die Liste ``light_time``, um die Dauer für jedes Licht anzupassen.

* Fußgängerüberweg hinzufügen:

  Implementiere Knöpfe und zusätzliche LEDs, um Fußgängerampelsignale zu simulieren.

* Anzeige verbessern:

  Modifiziere den Code, um Funktionen wie das Blinken der LED hinzuzufügen, wenn die Zeit fast abgelaufen ist.

* Echte Ampeln simulieren:

  Füge komplexere Sequenzen hinzu, wie Linksabbiegersignale oder mehrere Kreuzungen.

**Fazit**

Du hast erfolgreich ein Ampelsteuergerät mit dem Raspberry Pi Pico 2 W gebaut! Dieses Projekt zeigt, wie Mikrocontroller verwendet werden können, um Hardwarekomponenten wie LEDs und Anzeigen zu steuern, und wie Timer und Interrupts Echtzeitanwendungen erstellen können.

Fühle dich frei, dieses Projekt zu erweitern, indem du neue Funktionen hinzufügst oder es in ein größeres System integrierst.
