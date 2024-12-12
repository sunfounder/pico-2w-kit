.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ar_74hc_788bs:


5.4 Displaying Graphics on an 8x8 LED Matrix
===================================================================

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
        - :ref:`cpn_dot_matrix`
        - 1
        - 
    *   - 6
        - :ref:`cpn_74hc595`
        - 2
        - |link_74hc595_buy|


**Understanding the 8x8 LED Matrix**

An 8x8 LED matrix consists of 64 LEDs arranged in 8 rows and 8 columns. Each LED can be individually controlled by applying voltage across its row and column. By controlling the current through each pair of rows and columns, we can control each LED to display characters or patterns.

In this setup, we'll use two 74HC595 shift registers to control the rows and columns of the LED matrix, effectively expanding the number of outputs from the Raspberry Pi Pico 2 while using only a few GPIO pins.

**Schematic**

|sch_ledmatrix|

The 8x8 LED dot matrix is controlled by two **74HC595** shift registers: one controls the rows, and the other controls the columns. These two chips share the Pico's GPIO pins **GP18**, **GP19**, and **GP20**, greatly conserving the Pico's I/O ports.

The Pico outputs a 16-bit binary number at a time. The first 8 bits are sent to the 74HC595 controlling the rows, and the last 8 bits are sent to the 74HC595 controlling the columns. This allows the dot matrix to display specific patterns.

**Q7' (Pin 9)**: This serial data output pin of the first 74HC595 connects to the **DS (Pin 14)** of the second 74HC595, enabling you to chain multiple 74HC595 chips together.

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

.. note::

    * You can open the file ``5.4_8x8_pixel_graphics.ino`` under the path of ``pico-2w-starter-kit-main/arduino/5.4_8x8_pixel_graphics``. 
    * Or copy this code into **Arduino IDE**.
    * Don't forget to select the board(Raspberry Pi Pico) and the correct port before clicking the **Upload** button.



.. code-block:: arduino

    const int STcp = 19;  // Pin connected to ST_CP (latch pin) of 74HC595
    const int SHcp = 20;  // Pin connected to SH_CP (clock pin) of 74HC595
    const int DS = 18;    // Pin connected to DS (data pin) of 74HC595

    // Data array representing the 'X' shape on an 8x8 LED matrix
    byte datArray[] = {0x7E, 0xBD, 0xDB, 0xE7, 0xE7, 0xDB, 0xBD, 0x7E};

    void setup() {
      // Set pins as outputs
      pinMode(STcp, OUTPUT);
      pinMode(SHcp, OUTPUT);
      pinMode(DS, OUTPUT);
    }

    void loop()
    {
      for(int num = 0; num <8; num++)
      {
        digitalWrite(STcp,LOW); //ground ST_CP and hold low for as long as you are transmitting
        shiftOut(DS,SHcp,MSBFIRST,datArray[num]);
        shiftOut(DS,SHcp,MSBFIRST,0x80>>num);    
        //return the latch pin high to signal chip that it 
        //no longer needs to listen for information
        digitalWrite(STcp,HIGH); //pull the ST_CPST_CP to save the data
      }
    }



After uploading the code, the LED matrix should display an 'X' pattern by lighting up the appropriate LEDs.
If the pattern is not visible, try adjusting the timing or check the wiring connections.

**Understanding the Code**

#. Pin Definitions:

   * ``STcp (ST_CP)``: Used to latch the shifted data into the output register on a rising edge.
   * ``SHcp (SH_CP)``: Shifts data into the register on each rising edge.
   * ``DS``: Serial data input for the shift register.

   .. code-block:: arduino

      const int STcp = 19;  // Latch pin (ST_CP) of 74HC595
      const int SHcp = 20;  // Clock pin (SH_CP) of 74HC595
      const int DS = 18;    // Data pin (DS) of 74HC595

#. Data Array (``datArray``):

   * Each element represents a row in the LED matrix.
   * The hex values correspond to the LEDs that should be lit (0) or off (1) in each row.
   * This pattern forms a symmetrical 'X' shape across the matrix.

   .. code-block:: arduino

      byte datArray[] = {0x7E, 0xBD, 0xDB, 0xE7, 0xE7, 0xDB, 0xBD, 0x7E};
  

#. Setup Function:

   Initializes the control pins as outputs to communicate with the shift registers.

   .. code-block:: arduino

      void setup() {
        // Set pins as outputs
        pinMode(STcp, OUTPUT);
        pinMode(SHcp, OUTPUT);
        pinMode(DS, OUTPUT);
      }

#. Loop Function:

   * ``num`` ranges from 0 to 7, representing each row of the LED matrix.
   * ``0x80>>num`` activates one row at a time.
   * ``shiftOut()`` sends the column and row data to the shift registers, starting with the most significant bit (``MSBFIRST``).
   * Latches the data to the output pins by toggling the ``STcp``.

   .. code-block:: arduino

      void loop()
      {
        for(int num = 0; num <8; num++)
        {
          digitalWrite(STcp,LOW); //ground ST_CP and hold low for as long as you are transmitting
          shiftOut(DS,SHcp,MSBFIRST,datArray[num]);
          shiftOut(DS,SHcp,MSBFIRST,0x80>>num);    
          //return the latch pin high to signal chip that it 
          //no longer needs to listen for information
          digitalWrite(STcp,HIGH); //pull the ST_CPST_CP to save the data
        }
      }

**Troubleshooting**

* No Dots Lighting Up:

  * Verify all power connections.
  * Ensure that the shift registers are properly connected to the Pico.
  
* Incorrect Patterns:

  * Double-check the pattern array.
  * Ensure that the rows and columns are correctly wired to the shift registers.

* Flickering or Unstable Display:

  * Adjust the delay value in the loop to find a balance between performance and visual stability.
  * Ensure that power supply is stable and sufficient for the number of LEDs being used.


**Experimenting Further**

* Changing the Pattern

  Try replacing the pattern list with the following arrays to display different graphics. Replace pattern in your code with ``pattern_heart`` or ``pattern_smile`` to see different images.

  .. code-block:: arduino

      // Heart shape pattern
      byte pattern_heart[] = {
        0xFF, // 11111111
        0x99, // 10011001
        0x00, // 00000000
        0x00, // 00000000
        0x00, // 00000000
        0x81, // 10000001
        0xC3, // 11000011
        0xE7  // 11100111
      };

      // Smile face pattern
      byte pattern_smile[] = {
        0xC3, // 11000011
        0xBD, // 10111101
        0x5A, // 01011010
        0x7E, // 01111110
        0x5A, // 01011010
        0x66, // 01100110
        0xBD, // 10111101
        0xC3  // 11000011
      };

* Animating the Display

  Create multiple patterns and cycle through them to create animations:

  .. code-block:: arduino
        
      const int STcp = 19;  // Pin connected to ST_CP (latch pin) of 74HC595
      const int SHcp = 20;  // Pin connected to SH_CP (clock pin) of 74HC595
      const int DS = 18;    // Pin connected to DS (data pin) of 74HC595

      // Heart shape pattern
      byte pattern_heart[] = { 0xFF, 0x99, 0x00, 0x00, 0x00, 0x81, 0xC3, 0xE7 };

      // Smile face pattern
      byte pattern_smile[] = { 0xC3, 0xBD, 0x5A, 0x7E, 0x5A, 0x66, 0xBD, 0xC3 };

      void setup() {
        // Set pins as outputs
        pinMode(STcp, OUTPUT);
        pinMode(SHcp, OUTPUT);
        pinMode(DS, OUTPUT);
      }

      void latchData() {
        // Latch the shifted data to the output pins of the 74HC595
        digitalWrite(STcp, HIGH);  // Latch data
        digitalWrite(STcp, LOW);   // Prepare for the next data transmission
      }

      void displayPattern(byte pattern[]) {
        for (int repeat = 0; repeat < 500; repeat++) {  // Display the pattern for a certain duration
          for (int row = 0; row < 8; row++) {
            // Begin data transmission
            digitalWrite(STcp, LOW);  // Prepare to shift data

            // Shift out column data (pattern for the current row)
            shiftOut(DS, SHcp, MSBFIRST, pattern[row]);

            // Shift out row data (activating one row at a time)
            shiftOut(DS, SHcp, MSBFIRST, 1 << row);

            // Latch the data to display
            latchData();

            // Short delay for persistence of vision
            delay(1);
          }
        }
      }

      void loop() {
        // Continuously display patterns: heart and smiley face
        displayPattern(pattern_heart);  // Display the heart shape
        displayPattern(pattern_smile);  // Display the smiley face
      }

**Conclusion**

In this lesson, you've learned how to control an 8x8 LED matrix using the Raspberry Pi Pico and two 74HC595 shift registers. By leveraging shift registers, you can efficiently manage multiple LEDs with minimal GPIO usage, allowing for more complex and interactive projects. Understanding how to send serial data and latch it into parallel outputs enables you to create dynamic patterns and graphics on the LED matrix.
