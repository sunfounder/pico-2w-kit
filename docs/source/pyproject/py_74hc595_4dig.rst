.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_74hc_4dig:

5.3 Time Counter
================================


In this lesson, we'll learn how to use a **4-digit 7-segment display** 
with the Raspberry Pi Pico 2 W to create a simple time counter. The display 
will count up every second, showing the elapsed time in seconds.

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
        - 4(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_4_dit_7_segment`
        - 1
        - 
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|

**Understanding the 4-Digit 7-Segment Display**

A 4-digit 7-segment display consists of four individual 7-segment displays combined into a single module. Each digit shares the same segment control lines (**a** to **g** and **dp**), but each digit has its own **common cathode** control. This configuration allows us to control which digit is active at any given time.

To display different numbers on each digit using shared segment lines, we use a technique called **multiplexing**. We rapidly switch between digits, updating one digit at a time, but so quickly that it appears as if all digits are displayed simultaneously due to the persistence of vision.

|4digit_control_pins|

**Schematic**

|sch_4dig|

Here the wiring principle is basically the same as :ref:`py_74hc_led`, the only difference is that Q0-Q7 are connected to the a ~ g pins of the 4-digit 7-segment display.

Then G10 ~ G13 will select which 7-segment display to work.

**Wiring**

|wiring_4dig|

* **Segment Connections (through 220 Ω resistors):**

  * **Q0** → Segment **a**
  * **Q1** → Segment **b**
  * **Q2** → Segment **c**
  * **Q3** → Segment **d**
  * **Q4** → Segment **e**
  * **Q5** → Segment **f**
  * **Q6** → Segment **g**
  * **Q7** → Segment **dp** (decimal point)

* **Common Cathode Connections (Digit Select Pins):**

  * **Digit 1 (Leftmost Digit):** Connect to **GP10** on the Pico
  * **Digit 2:** Connect to **GP11**
  * **Digit 3:** Connect to **GP12**
  * **Digit 4 (Rightmost Digit):** Connect to **GP13**

**Writing the Code**

Let's write a MicroPython program to create a time counter that increments every second and displays the count on the 4-digit 7-segment display.

.. note::

    * Open the ``5.3_time_counter.py`` from ``pico-2 w-kit-main/micropython`` or copy the code into Thonny, then click "Run" or press F5.
    * Ensure the correct interpreter is selected: MicroPython (Raspberry Pi Pico).COMxx. 
    

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

When you run this code, the 4-digit 7-segment display will function as a counter, incrementing the displayed number by 1 every second, starting from 0 up to 9999, then resetting to 0 and repeating the cycle continuously.

**Understanding the Code**

#. Import Modules:

   * ``machine``: Provides access to GPIO pins and hardware functions.
   * ``utime``: Contains time-related functions for delays and timing.

#. Define Segment Codes:

   Each entry corresponds to the segments that need to be lit to display a digit. The values are in hexadecimal format.

   .. code-block:: python

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

#. Initialize Control Pins:
   
   Assigns the Pico's GPIO pins to control the 74HC595.

   .. code-block:: python

        SDI = machine.Pin(18, machine.Pin.OUT)
        RCLK = machine.Pin(19, machine.Pin.OUT)
        SRCLK = machine.Pin(20, machine.Pin.OUT)


#. Initialize Digit Select Pins:

   Controls which digit is active. Active low (common cathode).

   .. code-block:: python

        digit_pins = [
            machine.Pin(10, machine.Pin.OUT),
            machine.Pin(11, machine.Pin.OUT),
            machine.Pin(12, machine.Pin.OUT),
            machine.Pin(13, machine.Pin.OUT)
        ]

#. Define the ``shift_out`` Function:

   * Sends 8 bits of data to the 74HC595.
   * Shifts out the data starting from the most significant bit (MSB).
   * Pulses the shift and register clocks appropriately.

   .. code-block:: python

        def shift_out(data):
            RCLK.low()
            for bit in range(7, -1, -1):
                SRCLK.low()
                bit_val = (data >> bit) & 0x01
                SDI.value(bit_val)
                SRCLK.high()
            RCLK.high()

#. Define the ``display_digit`` Function:

   * Turns off all digits.
   * Sends the segment code for the digit.
   * Activates the specified digit by setting its pin low.
   * Adds a small delay to make the digit visible.
   * Turns off the digit after displaying.

   .. code-block:: python

        def display_digit(position, digit):
            for dp in digit_pins:
                dp.high()
            shift_out(SEGMENT_CODES[digit])
            digit_pins[position].low()
            utime.sleep_ms(5)
            digit_pins[position].high()


#. Define the ``display_number`` Function:

   * Extracts each digit from the number.
   * Calls ``display_digit`` for each digit rapidly to create the multiplexing effect.

   .. code-block:: python

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

#. Main Loop:

   * Increments the counter every second.
   * Resets the counter after reaching 9999.
   * Continuously calls ``display_number`` to refresh the display.

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


**Experimenting Further**

* Add a Reset Button:

  Connect a button to the Pico to reset the counter when pressed.

* Display Different Data: 

  Modify the code to display sensor readings, such as temperature or light levels.

* Adjust Display Brightness: 

  Change the ``utime.sleep_ms(5)`` delay in the ``display_digit`` function to adjust how long each digit is displayed, affecting brightness.

* Create a Stopwatch:

  Implement start, stop, and reset functionality to use the display as a stopwatch.

**Conclusion**

In this lesson, you've learned how to use a 4-digit 7-segment display with a 74HC595 shift register to create a time counter using the Raspberry Pi Pico 2 W. By understanding multiplexing and efficient timing, you can display dynamic information on multi-digit displays using minimal GPIO pins.