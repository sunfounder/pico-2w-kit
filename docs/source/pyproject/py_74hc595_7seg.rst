.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_74hc_7seg:

5.2 Displaying Numbers
========================

In this lesson, we'll learn how to use a **7-segment display** to show numbers using the Raspberry Pi Pico 2 W and a **74HC595 shift register**. The 7-segment display is a common electronic component used in devices like digital clocks, calculators, and appliances to display numerical information.

By combining the 74HC595 shift register with the 7-segment display, we can control all the segments using only a few GPIO pins on the Pico, saving valuable I/O resources for other components.

* :ref:`cpn_7_segment`

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
        - 1(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_7_segment`
        - 1
        - |link_7segment_buy|
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|

**Understanding the 7-Segment Display**

A 7-segment display consists of 7 LEDs (segments) arranged in a figure-eight pattern to display digits from 0 to 9. There's also an eighth LED for the decimal point. Each segment is labeled from **a** to **g**, and the decimal point is labeled **dp**.

Here's the segment labeling:

|img_7seg_cathode|

In a **common cathode** 7-segment display, all the cathodes (negative sides) of the LEDs are connected together to a common ground.


**Schematic**

|sch_74hc_7seg|

Here the wiring principle is basically the same as :ref:`py_74hc_led`, the only difference is that Q0-Q7 are connected to the a ~ g pins of the 7 Segment Display.

.. list-table:: Wiring
    :widths: 15 25
    :header-rows: 1

    *   - :ref:`cpn_74hc595`
        - :ref:`cpn_led` Segment Display
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

**Wiring**

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



**Writing the Code**

Let's write a MicroPython program to display digits from 0 to 9 on the 7-segment display.

.. note::

    * Open the ``5.2_number_display.py`` from ``pico-2 w-kit-main/micropython`` or copy the code into Thonny, then click "Run" or press F5.
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

When you run this code, the 7-segment display will sequentially display the digits 0 to 9, changing every 0.5 seconds. This creates a looping counting effect where the numbers increment one by one, and after reaching 9, the display returns to 0 and repeats the cycle continuously.

**Explanation of the Code**

#. Import Modules:

   * ``machine``: Provides access to GPIO pins and hardware functions.
   * ``utime``: Contains time-related functions for delays.

#. Define Segment Codes:

   Each entry corresponds to the segments that need to be lit to display a digit. The values are in hexadecimal format for readability.
   
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

   Suppose that the 7-segment Display display the number "1", we need to write a high level for b, c, and write a low level for a, d, e, f, g, and dg.

   |img_1_segment|

   That is, the binary number "00000110" needs to be written. For readability, we will use hexadecimal notation as "0x06".


#. Initialize Control Pins:

   Assigns the Pico's GPIO pins to control the 74HC595.

   .. code-block:: python

      SDI = machine.Pin(0, machine.Pin.OUT)
      RCLK = machine.Pin(1, machine.Pin.OUT)
      SRCLK = machine.Pin(2, machine.Pin.OUT)


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

#. Main Loop to Display Numbers:

   * Iterates through the numbers 0 to 9.
   * Calls shift_out with the corresponding segment code.
   * Adds a delay of 0.5 seconds between each number.

   .. code-block:: python

        while True:
            for num in range(10):
                shift_out(SEGMENT_CODES[num])
                utime.sleep(0.5)


**Understanding the Segment Codes**

Each segment code corresponds to the segments that need to be illuminated to display a specific digit. Here's how the segments map to each digit:

* **0**: Segments a, b, c, d, e, f (code 0x3F)
* **1**: Segments b, c (code 0x06)
* **2**: Segments a, b, g, e, d (code 0x5B)
* **3**: Segments a, b, c, d, g (code 0x4F)
* **4**: Segments b, c, f, g (code 0x66)
* **5**: Segments a, c, d, f, g (code 0x6D)
* **6**: Segments a, c, d, e, f, g (code 0x7D)
* **7**: Segments a, b, c (code 0x07)
* **8**: Segments a, b, c, d, e, f, g (code 0x7F)
* **9**: Segments a, b, c, d, f, g (code 0x6F)

**Experimenting Further**

* Display Hexadecimal Characters:

  Extend the ``SEGMENT_CODES`` list to include letters A-F for hexadecimal representation. For example, to display 'A', the segment code is 0x77.

* Create a Counter:

  Modify the code to create an up-counter or down-counter. Use button inputs to increment or decrement the displayed number.

* Control Multiple Displays:

  Use additional 74HC595 shift registers to control multiple 7-segment displays. Implement multiplexing to manage multiple displays with minimal GPIO usage.

**Conclusion**

In this lesson, you've learned how to use a 7-segment display with a 74HC595 shift register to display numbers using the Raspberry Pi Pico 2 W. By understanding how to control each segment through binary codes and utilizing the shift register, you can efficiently manage multiple outputs with limited GPIO pins.

