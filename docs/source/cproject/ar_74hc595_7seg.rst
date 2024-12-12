.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ar_74hc_7seg:

5.2 Displaying Numbers
===========================================================

In this lesson, we'll learn how to use a **7-segment display** to show numbers using the Raspberry Pi Pico 2w and a **74HC595 shift register**. The 7-segment display is a common electronic component used in devices like digital clocks, calculators, and appliances to display numerical information.

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
        - PURCHASE LINK
    *   - Pico 2 W Starter Kit	
        - 450+
        - |link_pico2w_kit|

You can also buy them separately from the links below.


.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - COMPONENT INTRODUCTION	
        - QUANTITY
        - PURCHASE LINK

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

    *   - 74HC595
        - LED Segment Display
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

|wiring_74hc_7seg|


**Writing the Code**

We'll write a program that controls the 7-segment display by sending serial data to the 74HC595 shift register. The display will cycle through the numbers 0 to 9 in sequence.

.. note::

    * You can open the file ``5.2_number_display.ino`` under the path of ``pico-2w-kit-main/arduino/5.2_number_display``. 
    * Or copy this code into **Arduino IDE**.
    * Don't forget to select the board(Raspberry Pi Pico) and the correct port before clicking the **Upload** button.

.. code-block:: arduino

    // Define the pins connected to the 74HC595
    const int DS = 0;    // GPIO 0 -> DS (Pin 14)
    const int SHCP = 1;  // GPIO 1 -> SHCP (Pin 11)
    const int STCP = 2;  // GPIO 2 -> STCP (Pin 12)

    // Array of hexadecimal codes for digits 0-9 on a common cathode 7-segment display
    const byte numArray[] = {
      0x3F, // 0: 00111111
      0x06, // 1: 00000110
      0x5B, // 2: 01011011
      0x4F, // 3: 01001111
      0x66, // 4: 01100110
      0x6D, // 5: 01101101
      0x7D, // 6: 01111101
      0x07, // 7: 00000111
      0x7F, // 8: 01111111
      0x6F  // 9: 01101111
    };

    void setup() {
      // Initialize the control pins as outputs
      pinMode(DS, OUTPUT);
      pinMode(SHCP, OUTPUT);
      pinMode(STCP, OUTPUT);
    }

    void loop() {
      // Iterate through each number 0-9
      for (int num = 0; num < 10; num++) {
        // Set STCP to LOW to prepare for data
        digitalWrite(STCP, LOW);

        // Shift out the data to the shift register
        shiftOut(DS, SHCP, MSBFIRST, numArray[num]);

        // Set STCP to HIGH to latch the data to the output pins
        digitalWrite(STCP, HIGH);

        delay(1000); // Wait for one second before displaying the next number
      }

      // Turn off all segments after displaying 0-9
      digitalWrite(STCP, LOW);
      shiftOut(DS, SHCP, MSBFIRST, 0x00);
      digitalWrite(STCP, HIGH);
      delay(1000);
    }

After uploading the code, the display should cycle through the numbers 0 to 9, showing each number for one second.
After reaching 9, all segments should turn off for one second before starting the sequence again.

**Understanding the Code**

#. Defining Control Pins:

   * ``DS (Data Serial Input)``: Receives serial data to be shifted into the register.
   * ``SHCP (Shift Register Clock Input)``: Controls the shifting of data into the register.
   * ``STCP (Storage Register Clock Input)``: Controls the latching of data from the shift register to the output pins.

   .. code-block:: arduino

        const int DS = 0;    // GPIO 0 -> DS (Pin 14)
        const int SHCP = 2;  // GPIO 2 -> SHCP (Pin 11)
        const int STCP = 1;  // GPIO 1 -> STCP (Pin 12)

#. Creating Data Patterns:

   * ``numArray``: An array holding the hexadecimal codes for displaying numbers 0-9 on a common cathode 7-segment display.
   * Each hexadecimal value corresponds to the segments that need to be lit to display a particular number.

   .. code-block:: arduino

        const byte numArray[] = {
          0x3F, // 0: 00111111
          0x06, // 1: 00000110
          0x5B, // 2: 01011011
          0x4F, // 3: 01001111
          0x66, // 4: 01100110
          0x6D, // 5: 01101101
          0x7D, // 6: 01111101
          0x07, // 7: 00000111
          0x7F, // 8: 01111111
          0x6F  // 9: 01101111
        };

   Suppose that the 7-segment Display display the number "1", we need to write a high level for b, c, and write a low level for a, d, e, f, g, and dg.

   |img_1_segment|

   That is, the binary number "00000110" needs to be written. For readability, we will use hexadecimal notation as "0x06".

#. Setup Function:

   Sets the ``DS``, ``SHCP``, and ``STCP`` pins as outputs to send data to the shift register.

   .. code-block:: arduino

        void setup() {
          // Initialize the control pins as outputs
          pinMode(DS, OUTPUT);
          pinMode(SHCP, OUTPUT);
          pinMode(STCP, OUTPUT);
        }

#. Loop Function: The ``for`` loop cycles through each pattern in the ``numArray`` array.

   * Shifting Out Data:

     * ``shiftOut`` sends the byte of data one bit at a time.
     * ``MSBFIRST`` indicates that the most significant bit is sent first.

     .. code-block:: arduino

        shiftOut(DS, SHCP, MSBFIRST, numArray[num]);

   * Latching Data:

     * Setting ``STCP`` ``LOW`` prepares the shift register for new data.
     * After shifting out the data, setting ``STCP`` ``HIGH`` latches the data to the output pins, updating the 7-segment display.

     .. code-block:: arduino

        digitalWrite(STCP, LOW);
        // shiftOut(...)
        digitalWrite(STCP, HIGH);

   * ``delay(500);`` adds a half-second pause between each pattern for visibility.

   * Turning Off All Segments: After displaying numbers 0-9, the code sends 0x00 to turn off all segments. The display remains off for one second before the loop repeats.

     .. code-block:: arduino

        digitalWrite(STCP, LOW);
        shiftOut(DS, SHCP, MSBFIRST, 0x00);
        digitalWrite(STCP, HIGH);
        delay(1000);

**Troubleshooting**

* No Numbers Displayed:

  * Check all wiring connections.
  * Ensure the 74HC595 is properly powered.
  * Verify that the GPIO pins on the Pico are correctly connected to the shift register.
  * Make sure the 7-segment display is connected correctly, with each segment connected through a resistor.

* Incorrect Numbers Displayed:

  * Double-check the hexadecimal codes in numArray.
  * Ensure that the shift register outputs are correctly connected to the corresponding segments.

* Flickering or Unstable Display:

  * Verify that the power connections are stable.
  * Ensure that the resistors are properly connected to limit the current to each segment.

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

**Further Exploration**

* Controlling Multiple 7-Segment Displays:

  Chain multiple 74HC595 shift registers to control additional 7-segment displays, enabling multi-digit displays.

* Implementing LED Animations:

  Create dynamic animations or scrolling text by modifying the data patterns sent to the shift register.

* Integrating with Sensors:

  Combine the 7-segment display with sensors (e.g., temperature, light) to display real-time data.

* Building a Digital Clock:

  Use multiple 7-segment displays and real-time clock modules to create a functional digital clock.

* Adding Decimal Points and Indicators:

  Utilize the decimal point (dp) and additional indicators (e.g., colons) for more complex displays.


**Conclusion**

In this lesson, you've learned how to use the 74HC595 shift register with the Raspberry Pi Pico to control a 7-segment display. By sending serial data to the shift register, you can efficiently manage multiple outputs using just a few GPIO pins. This technique not only conserves valuable I/O resources but also opens up possibilities for expanding your projects with more LEDs, displays, or other peripherals.
