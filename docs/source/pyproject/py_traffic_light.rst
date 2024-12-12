.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_traffic_light:


7.6 Building a Traffic Light Controller
==============================================================

In this project, we'll create a **Traffic Light Controller** using the Raspberry Pi Pico 2, three LEDs (red, yellow, green), and a 4-digit 7-segment display. This system will simulate a real traffic light sequence, displaying the remaining time for each light on the 7-segment display.

* **Red light**: Traffic should stop if it sees a flashing red light, equivalent to a stop sign.
* **Yellow light**: A warning signal is about to turn red. Yellow lights are interpreted differently in different countries (regions).
* **Green light**: Allows traffic to move in the indicated direction.


**Required Components**

In this project, we need the following components. 

It's definitely convenient to buy a whole kit, here's the link: 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ITEMS IN THIS KIT
        - LINK
    *   - Pico 2 W Starter Kit	
        - 450+
        - |link_pico2w_kit|

You can also buy them separately from the links below.


.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - COMPONENT	
        - QUANTITY
        - LINK

    *   - 1
        - :ref:`cpn_pico_2w`
        - 1
        - |link_pico2w_buy|
    *   - 2
        - Micro USB Cable
        - 1
        - 
    *   - 3
        - :ref:`cpn_breadboard`
        - 1
        - |link_breadboard_buy|
    *   - 4
        - :ref:`cpn_wire`
        - Several
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


**Understanding the Components**

* **LEDs**: Represent the traffic lights. We'll control them to simulate the standard traffic light sequence.
* **4-Digit 7-Segment Display**: Shows the countdown timer for each light.
* **74HC595 Shift Register**: Allow us to control multiple outputs (segments and digits of the display) using fewer GPIO pins on the Pico.


**Schematic**

|sch_traffic_light|


* This circuit is based on the :ref:`py_74hc_4dig` with the addition of 3 LEDs.
* The 3 red, yellow and green LEDs are connected to GP7~GP9 respectively.

**Wiring**


|wiring_traffic_light| 


**Writing the Code**

We'll write a MicroPython script that:

* Controls the traffic light sequence.
* Displays the countdown timer on the 7-segment display.
* Uses shift registers to control the display.

.. note::

    * Open the ``7.6_traffic_light.py`` from ``pico-2w-kit-main/micropython`` or copy the code into Thonny, then click "Run" or press F5.
    * Ensure the correct interpreter is selected: MicroPython (Raspberry Pi Pico).COMxx. 

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


When the code runs, the green LED will light up first, and the display will show a countdown from 30.
After 30 seconds, the yellow LED will light up, and the display will count down from 5.
Then, the red LED will light up, and the display will count down from 30.
The cycle repeats indefinitely.

**Understanding the Code**

#. Imports and Initialization:

   * ``machine``: Provides access to hardware-related functions.
   * ``utime``: Offers time-related functions.
   * ``Timer``: Used for creating hardware timers.

#. LED Initialization:

   Defines GPIO pins for the red, yellow, and green LEDs. Initializes each pin as an output.

   .. code-block:: python

        led_pins = [7, 8, 9]  # Green, Yellow, Red LEDs connected to GP7, GP8, GP9
        leds = [machine.Pin(pin, machine.Pin.OUT) for pin in led_pins]

#. Traffic Light Timings:

   Specifies the duration (in seconds) for each traffic light state.

   .. code-block:: python

        light_time = [30, 5, 30]  # [Green, Yellow, Red]

#. Display Functions:

   * ``display_digit(digit)``: Activates a specific digit on the display.
   * ``shift_out(data)``: Sends data to the shift register.
   * ``display_number(num)``: Breaks down the number into digits and displays them using multiplexing.

#. ``update_leds(state)`` Function:

   * Updates the LED states based on the current traffic light state.
   * Turns off all LEDs and then turns on the LED corresponding to the current state.

   .. code-block:: python

        def update_leds(state):
            # States: 0 = Green, 1 = Yellow, 2 = Red
            for i in range(3):
                leds[i].value(0)
            leds[state].value(1)

#. ``timer_callback(t)`` Function:

   * Timer interrupt callback function.
   * Decrements the counter every second.
   * When the counter reaches zero, it cycles to the next traffic light state and resets the counter.

   .. code-block:: python

        def timer_callback(t):
            global counter, current_state
            counter -= 1
            if counter <= 0:
                current_state = (current_state + 1) % 3  # Cycle through the states
                counter = light_time[current_state]  # Reset counter for the new state
                update_leds(current_state)

#. Main Execution:

   * Initial Variables: Sets the initial state to green and initializes the counter.

     .. code-block:: python

        counter = light_time[0]  # Start with green light duration
        current_state = 0  # 0 = Green, 1 = Yellow, 2 = Red
   
   * Initialize the Timer: Creates a periodic timer that triggers every 1000 milliseconds (1 second) and calls timer_callback.


     .. code-block:: python

        timer = Timer(period=1000, mode=Timer.PERIODIC, callback=timer_callback)
   
   * Set Initial LED State: Ensures the correct LED is lit at the start.

     .. code-block:: python

        update_leds(current_state)

   * Main Loop: Enters an infinite loop displaying the countdown timer. Handles a keyboard interrupt (e.g., Ctrl+C) to safely deinitialize the timer and exit.


     .. code-block:: python

        try:
            while True:
                display_number(counter)
        except KeyboardInterrupt:
            timer.deinit()
            print("Program stopped.")

**Experimenting Further**

* Adjust Timing:

  Change the ``light_time`` list to adjust the durations for each light.

* Add Pedestrian Crossing:

  Implement buttons and additional LEDs to simulate pedestrian crossing signals.

* Improve Display:

  Modify the code to add features like blinking the LED when time is almost up.

* Simulate Real Traffic Lights:

  Add more complex sequences, such as left-turn signals or multiple intersections.

**Conclusion**

You've successfully built a Traffic Light Controller using the Raspberry Pi Pico 2w! This project demonstrates how microcontrollers can be used to control hardware components like LEDs and displays, and how timers and interrupts can create real-time applications.

Feel free to expand upon this project, adding new features or integrating it into a larger system.