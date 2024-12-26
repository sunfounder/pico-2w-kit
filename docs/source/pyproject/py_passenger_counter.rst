.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_passage_counter:


7.4 Building a Passenger Counter
=======================================================

In this lesson, we'll create a **Passenger Counter** using a Raspberry Pi Pico 2 W, a PIR (Passive Infrared) motion sensor, and a 4-digit 7-segment display. This device will count the number of times motion is detected by the PIR sensor and display the count on the 7-segment display. This simulates how such counters are used in public places to monitor foot traffic.


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
    *   - 8
        - :ref:`cpn_pir`
        - 1
        - |link_pir_buy|

**Understanding the Components**

* **PIR Motion Sensor**: Detects motion by measuring infrared (IR) light radiating from objects in its field of view. When motion is detected, it outputs a HIGH signal.
* **4-Digit 7-Segment Display**: Allows us to display numbers from 0000 to 9999. We'll use shift registers to control the display using fewer GPIO pins.
* **74HC595 Shift Register**: This is a 8-bit serial-in, parallel-out shift register with output latche. It allows us to control multiple outputs using just a few GPIO pins.

**Schematic**

|sch_passager_counter| 

* This circuit is based on the :ref:`py_74hc_4dig` with the addition of a PIR module.
* The PIR will send a high signal of about 2.8s long when someone passes by.
* The PIR module has two potentiometers: one adjusts sensitivity, the other adjusts detection distance. To make the PIR module work better, you need to turn both of them counterclockwise to the end.

    |img_PIR_TTE|


**Wiring**


|wiring_passager_counter| 


**Writing the Code**

We'll write a MicroPython script that:

* Detects motion using the PIR sensor.
* Increments a counter each time motion is detected.
* Updates the 4-digit 7-segment display with the current count.
* Uses multiplexing to control the display.

.. note::

    * Open the ``7.4_passager_counter.py`` from ``pico-2w-kit-main/micropython`` or copy the code into Thonny, then click "Run" or press F5.
    * Ensure the correct interpreter is selected: MicroPython (Raspberry Pi Pico).COMxx. 

.. code-block:: python

    from machine import Pin
    import utime

    # Define the PIR sensor pin
    pir_sensor = Pin(16, Pin.IN)

    # Initialize the counter
    count = 0

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

    # Interrupt handler for PIR sensor
    def pir_handler(pin):
        global count
        count += 1
        if count > 9999:
            count = 0

    # Set up PIR sensor interrupt
    pir_sensor.irq(trigger=Pin.IRQ_RISING, handler=pir_handler)

    # Main loop
    while True:
        # Continuously refresh the display
        display_number(count)

When the code is running, the 7-segment display should initialize and show 0000.
Move in front of the PIR sensor.
The count displayed should increment by one each time motion is detected.
If the count reaches 9999, it will reset to 0000.

**Understanding the Code**

#. Imports and Pin Definitions:

   * ``machine.Pin``: For controlling GPIO pins.
   * ``utime``: For timing functions.
   * Define SDI, SRCLK, and RCLK pins for controlling the shift register.
   * Define ``pir_sensor`` on GP16 as an input pin for the PIR sensor.

#. Segment Codes:

   * ``SEGMENT_CODES``: A list containing the binary codes for displaying digits 0-9 on a 7-segment display. Each byte represents which segments should be lit.

   .. code-block:: python

        # 7-segment display segment codes for digits 0-9 (common cathode)
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

#. Counter Initialization:

   * ``count``: A global variable that keeps track of the number of times motion has been detected.

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

#. PIR Interrupt Handler:

   * ``pir_handler``: This function is called automatically when the PIR sensor detects motion.
   * Increments the count variable.
   * Resets the count to 0 if it exceeds 9999.

   .. code-block:: python

        def pir_handler(pin):
            global count
            count += 1
            if count > 9999:
                count = 0

#. PIR Sensor Interrupt Setup:

   ``pir_sensor.irq``: Sets up an interrupt to call ``pir_handler`` on a rising edge signal from the PIR sensor (i.e., when motion is detected).

   .. code-block:: python

        pir_sensor.irq(trigger=Pin.IRQ_RISING, handler=pir_handler)

#. Main Loop:

   Continuously calls ``display_number(count)`` to refresh the display with the current count.

   .. code-block:: python

        while True:
            display_number(count)

**Troubleshooting**

* Display Issues:

  * If the display is not showing numbers correctly, verify the segment codes and wiring connections.
  * Ensure that the shift register is connected properly and that data is being shifted out in the correct order.

* PIR Sensor Sensitivity:

  * The PIR sensor may have adjustable potentiometers for sensitivity and delay.
  * Adjust these to fine-tune motion detection for your environment.
  * Note that the PIR sensor may have a short delay after detecting motion before it can detect again.

* Counting Accuracy:

  * In environments with a lot of movement, the counter may increment rapidly.
  * Consider adding logic to debounce the PIR sensor or limit counting frequency if necessary.

**Extensions and Enhancements**

* Reset Button:

  Add a push button connected to another GPIO pin to reset the count to zero when pressed.

* Bidirectional Counting:

  Use two PIR sensors placed strategically to detect the direction of movement (entering or exiting) and increment or decrement the count accordingly.

* Data Logging:

  Extend the program to log counts over time, either by storing data on the Pico or sending it to a computer for analysis.

* Display Improvements:

  Use an LCD display to show additional information such as timestamps, total counts, or messages.

* Network Connectivity:

  Connect the Pico to a network (using Wi-Fi modules like ESP8266) to send data to a server or cloud service for remote monitoring.

**Conclusion**

In this lesson, you've learned how to create a practical Passenger Counter using the Raspberry Pi Pico 2 W, a PIR motion sensor, and a 4-digit 7-segment display. This project demonstrates how microcontrollers can interact with sensors and output devices to collect and display data in real-time.

Feel free to experiment with the code and hardware to add new features or improve functionality. This project can serve as a foundation for more complex systems involving data analysis, remote monitoring, or integration with other sensors and devices.


