.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_74hc_788bs:

5.4 8x8 Pixel Graphics
=============================

In this lesson, we'll learn how to control an **8x8 LED matrix** using the Raspberry Pi Pico 2w and two **74HC595 shift registers**. We'll display patterns and simple graphics by controlling individual LEDs on the matrix.

* :ref:`cpn_dot_matrix`
* :ref:`cpn_74hc595`

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
        - :ref:`cpn_dot_matrix`
        - 1
        - 
    *   - 6
        - :ref:`cpn_74hc595`
        - 2
        - |link_74hc595_buy|

**Understanding the 8x8 LED Matrix**

The 8x8 LED dot matrix is controlled by two **74HC595** shift registers: one controls the rows, and the other controls the columns. These two chips share the Pico's GPIO pins **GP18**, **GP19**, and **GP20**, greatly conserving the Pico's I/O ports.

The Pico outputs a 16-bit binary number at a time. The first 8 bits are sent to the 74HC595 controlling the rows, and the last 8 bits are sent to the 74HC595 controlling the columns. This allows the dot matrix to display specific patterns.

**Q7' (Pin 9)**: This serial data output pin of the first 74HC595 connects to the **DS (Pin 14)** of the second 74HC595, enabling you to chain multiple 74HC595 chips together.

**Schematic**

|sch_ledmatrix|

The 8x8 dot matrix is controlled by two **74HC595** chips, one controlling the rows and one controlling the columns, while these two chips share G18~G20, which can greatly save the I/O ports of the Pico 2W board. 

Pico 2W needs to output a 16-bit binary number at a time, the first 8 bits are given to the 74HC595 which controls the rows, and the last 8 bits are given to the 75HC595 which controls the columns, so that the dot matrix can display a specific pattern.

Q7': Series output pin, connected to DS of another 74HC595 to connect multiple 74HC595s in series.

**Wiring**

Building the circuit can be complex, so let's proceed step by step.

**Step 1:**  First, insert the Pico 2W, the LED dot matrix
and two 74HC595 chips into breadboard. Connect the 3.3V and GND of the
Pico 2W to holes on the two sides of the board, then hook up pin16 and
10 of the two 74HC595 chips to VCC, pin 13 and pin 8 to GND.

.. note::
   In the Fritzing image above, the side with label is at the bottom.

|wiring_ledmatrix_4|

**Step 2:** Connect pin 11 of the two 74HC595 together, and then to
GP20; then pin 12 of the two chips, and to GP19; next, pin 14 of the
74HC595 on the left side to GP18 and pin 9 to pin 14 of the second
74HC595.

|wiring_ledmatrix_3|

**Step 3:** The 74HC595 on the right side is to control columns of the
LED dot matrix. See the table below for the mapping. Therefore, Q0-Q7
pins of the 74HC595 are mapped with pin 13, 3, 4, 10, 6, 11, 15, and 16
respectively.

+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **74HC595**        | **Q0** | **Q1** | **Q2** | **Q3** | **Q4** | **Q5** | **Q6** | **Q7** |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **LED Dot Matrix** | **13** | **3**  | **4**  | **10** | **6**  | **11** | **15** | **16** |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+

|wiring_ledmatrix_2|

**Step 4:** Now connect the ROWs of the LED dot matrix. The 74HC595 on
the left controls ROW of the LED dot matrix. See the table below for the
mapping. We can see, Q0-Q7 of the 74HC595 on the left are mapped with
pin 9, 14, 8, 12, 1, 7, 2, and 5 respectively.

+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **74HC595**        | **Q0** | **Q1** | **Q2** | **Q3** | **Q4** | **Q5** | **Q6** | **Q7** |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **LED Dot Matrix** | **9**  | **14** | **8**  | **12** | **1**  | **7**  | **2**  | **5**  |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+

|wiring_ledmatrix_1|

**Writing the Code**

We'll write a MicroPython program to display a pattern on the LED matrix.

.. note::

    * Open the ``5.4_8x8_pixel_graphics.py`` from ``pico-2w-starter-kit-main/micropython`` or copy the code into Thonny, then click "Run" or press F5.
    * Ensure the correct interpreter is selected: MicroPython (Raspberry Pi Pico).COMxx. 
    

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



When you run this code, the 8x8 LED matrix will display an 'X' shape, with the LEDs lighting up to form the pattern of the letter 'X' across the matrix.

**Understanding the Code**

#. Importing Modules:

   * ``machine``: Provides access to hardware-related functions, such as controlling GPIO pins.
   * ``time``: Used for adding delays to control timing.

#. Defining Pins:

   * ``sdi``: Sends serial data into the shift register.
   * ``rclk``: Latches the shifted data to the output pins.
   * ``srclk``: Shifts the data into the register on each rising edge.

#. Defining the Glyph for 'X':

   * Each element represents a row in the LED matrix.
   * The hex values correspond to the LEDs that should be lit (0) or off (1) in each row.
   * This pattern forms a symmetrical 'X' shape across the matrix.

   .. code-block:: python
    
        glyph = [0x7E, 0xBD, 0xDB, 0xE7, 0xE7, 0xDB, 0xBD, 0x7E]

#. Function ``hc595_in(dat)``:

   * This function sends 8 bits of data (``dat``) into the shift register serially.
   * It iterates from the most significant bit to the least significant bit.
   * The ``srclk`` pin is toggled to shift each bit into the register.
   * The ``sdi`` pin sets the data line high or low depending on the current bit.


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


#. Function ``hc595_out()``:

   * This function latches the shifted data from the shift register to the output register.
   * A rising edge on the ``rclk`` pin transfers the data to the output pins, updating the LEDs.

   .. code-block:: python
    
        def hc595_out():

            rclk.high()
            rclk.low()

#. Main Loop:

   * The loop continuously refreshes the display to create a persistent image of the letter 'X'.
   * The ``for`` loop iterates over each row index from 0 to 7.
   * ``hc595_in(1 << i)`` activates one row at a time by setting a single bit high.
   * ``hc595_in(glyph[i])`` sends the column data for the current row, determining which LEDs in that row should be lit.
   * ``hc595_out()`` latches the data, updating the LED matrix display.
   * ``time.sleep_ms(1)`` provides a short delay to ensure that each row is displayed long enough to be perceived by the human eye.
   * This rapid scanning creates the illusion of the entire 'X' being displayed simultaneously.

   .. code-block:: python
    
        while True:
            for i in range(8):
                hc595_in(glyph[i])       # Send the column data for the current row
                hc595_in(1 << i)         # Activate the current row
                hc595_out()              # Update the display
                time.sleep_ms(1)         # Delay for visual persistence


**Experimenting Further**

* Changing the Pattern

  Try replacing the pattern list with the following arrays to display different graphics. Replace pattern in your code with ``pattern_heart`` or ``pattern_smile`` to see different images.

  .. code-block:: python

        # Heart shape
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

        # Smile face
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


* Animating the Display

  Create multiple patterns and cycle through them to create animations:

  .. code-block:: python

        import machine
        import time
        
        # Define pins connected to the 74HC595 shift registers
        sdi = machine.Pin(18, machine.Pin.OUT)   # Serial Data Input
        rclk = machine.Pin(19, machine.Pin.OUT)  # Register Clock (Latch)
        srclk = machine.Pin(20, machine.Pin.OUT) # Shift Register Clock
        
        # Heart shape
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
        
        # Smile face
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

* Design Your Own Patterns

  Each byte represents a row; bits set to 0 turn on the LED in that column. Create custom patterns by defining your own pattern list.

**Conclusion**

In this lesson, you've learned how to control an 8x8 LED matrix using the Raspberry Pi Pico 2w and two 74HC595 shift registers. By understanding how to manipulate bits and use shift registers, you can display patterns and graphics on the LED matrix.