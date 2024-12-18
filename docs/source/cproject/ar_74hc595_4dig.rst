.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ar_74hc_4dig:

5.3 Creating a Time Counter with a 4-Digit 7-Segment Display
==============================================================

In this lesson, we'll learn how to use a **4-digit 7-segment display** with the Raspberry Pi Pico 2 W to create a simple time counter. The display will count up every second, showing the elapsed time in seconds.


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

Here the wiring principle is basically the same as :ref:`ar_74hc_led`, the only difference is that Q0-Q7 are connected to the a ~ g pins of the 4-digit 7-segment display.

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

.. note::

    * You can open the file ``5.3_time_counter.ino`` under the path of ``pico-2 w-kit-main/arduino/5.3_time_counter``. 
    * Or copy this code into **Arduino IDE**.
    * Don't forget to select the board(Raspberry Pi Pico) and the correct port before clicking the **Upload** button.


.. code-block:: arduino

    // Define the connection pins for the shift register
    #define DATA_PIN 18   // DS (Serial Data Input)
    #define LATCH_PIN 19  // STCP (Storage Register Clock)
    #define CLOCK_PIN 20  // SHCP (Shift Register Clock)

    // Define the digit control pins for the 4-digit 7-segment display
    const int digitPins[4] = { 10, 11, 12, 13 };  // DIG1, DIG2, DIG3, DIG4

    // Segment byte maps for numbers 0-9
    const byte digitCodes[10] = {
      // Pgfedcba
      0b00111111,  // 0
      0b00000110,  // 1
      0b01011011,  // 2
      0b01001111,  // 3
      0b01100110,  // 4
      0b01101101,  // 5
      0b01111101,  // 6
      0b00000111,  // 7
      0b01111111,  // 8
      0b01101111   // 9
    };

    unsigned long previousMillis = 0;  // Stores the last time the display was updated
    unsigned int counter = 0;          // Counter value

    void setup() {
      // Initialize the shift register pins
      pinMode(DATA_PIN, OUTPUT);
      pinMode(LATCH_PIN, OUTPUT);
      pinMode(CLOCK_PIN, OUTPUT);

      // Initialize the digit control pins
      for (int i = 0; i < 4; i++) {
        pinMode(digitPins[i], OUTPUT);
        digitalWrite(digitPins[i], HIGH);  // Turn off all digits
      }
    }

    void loop() {
      unsigned long currentMillis = millis();

      // Update the counter every 1000 milliseconds (1 second)
      if (currentMillis - previousMillis >= 1000) {
        previousMillis = currentMillis;
        counter++;  // Increment the counter
        if (counter > 9999) {
          counter = 0;  // Reset counter after 9999
        }
      }

      // Display the counter value
      displayNumber(counter);
    }

    void displayNumber(int num) {
      // Break the number into digits
      int digits[4];
      digits[0] = num / 1000;        // Thousands
      digits[1] = (num / 100) % 10;  // Hundreds
      digits[2] = (num / 10) % 10;   // Tens
      digits[3] = num % 10;          // Units

      // Display each digit
      for (int i = 0; i < 4; i++) {
        digitalWrite(digitPins[i], LOW);  // Activate digit
        shiftOutDigit(digitCodes[digits[i]]);
        delay(5);                          // Small delay for multiplexing
        digitalWrite(digitPins[i], HIGH);  // Deactivate digit
      }
    }

    void shiftOutDigit(byte data) {
      // Send data to the shift register
      digitalWrite(LATCH_PIN, LOW);
      shiftOut(DATA_PIN, CLOCK_PIN, MSBFIRST, data);
      digitalWrite(LATCH_PIN, HIGH);
    }

After uploading the code, the 4-digit 7-segment display should start counting up from 0000, incrementing by 1 every second.
The count should progress as follows: 0000, 0001, 0002, ..., 9999, then reset to 0000.

**Understanding the Code**

#. Defining Control Pins:

   * ``DATA_PIN (DS)``: Receives serial data to be shifted into the 74HC595.
   * ``LATCH_PIN (STCP)``: Controls the latching of data from the shift register to the output pins.
   * ``CLOCK_PIN (SHCP)``: Controls the shifting of data into the shift register.

   .. code-block:: arduino

      #define DATA_PIN   18  // DS (Serial Data Input)
      #define LATCH_PIN  19  // STCP (Storage Register Clock)
      #define CLOCK_PIN  20  // SHCP (Shift Register Clock)
  
#. Defining Digit Control Pins:

   * Each digit's common cathode is connected to a separate GPIO pin.
   * Setting a digit pin LOW activates that digit, while HIGH deactivates it.

   .. code-block:: arduino

      const int digitPins[4] = {10, 11, 12, 13}; // DIG1, DIG2, DIG3, DIG4
  
#. Creating Segment Byte Maps:

   * Each byte represents the segments that need to be lit to display numbers 0 to 9 on a common cathode 7-segment display.
   * The bits correspond to segments a to g and dp:

   .. code-block:: arduino

      const byte digitCodes[10] = {
        0b00111111, // 0
        0b00000110, // 1
        0b01011011, // 2
        0b01001111, // 3
        0b01100110, // 4
        0b01101101, // 5
        0b01111101, // 6
        0b00000111, // 7
        0b01111111, // 8
        0b01101111  // 9
      };

#. Setup Function:

   * Sets the ``DATA_PIN``, ``LATCH_PIN``, and ``CLOCK_PIN`` as outputs.
   * Sets all digit control pins to ``HIGH`` to deactivate all digits at startup.

   .. code-block:: arduino

      void setup() {
        // Initialize the shift register pins
        pinMode(DATA_PIN, OUTPUT);
        pinMode(LATCH_PIN, OUTPUT);
        pinMode(CLOCK_PIN, OUTPUT);

        // Initialize the digit control pins
        for (int i = 0; i < 4; i++) {
          pinMode(digitPins[i], OUTPUT);
          digitalWrite(digitPins[i], HIGH); // Turn off all digits initially
        }
      }

#. Loop Function:

   * Uses the ``millis()`` function to track elapsed time without blocking the program.
   * Increments the ``counter`` every second and resets it after reaching 9999.

   .. code-block:: arduino

      void loop() {
        unsigned long currentMillis = millis();

        // Update the counter every 1000 milliseconds (1 second)
        if (currentMillis - previousMillis >= 1000) {
          previousMillis = currentMillis;
          counter++; // Increment the counter
          if (counter > 9999) {
            counter = 0; // Reset counter after 9999
          }
        }

        // Display the counter value
        displayNumber(counter);
      }

#. Displaying the Number:

   * Breaks the ``counter`` value into thousands, hundreds, tens, and units.
   * Activates each digit one by one, sends the corresponding segment data, and deactivates the digit.
   * The rapid cycling between digits creates the illusion that all digits are lit simultaneously.

   .. code-block:: arduino

      void displayNumber(int num) {
        // Break the number into individual digits
        int digits[4];
        digits[0] = num / 1000;         // Thousands
        digits[1] = (num / 100) % 10;   // Hundreds
        digits[2] = (num / 10) % 10;    // Tens
        digits[3] = num % 10;           // Units

        // Display each digit one by one
        for (int i = 0; i < 4; i++) {
          digitalWrite(digitPins[i], LOW); // Activate current digit

          // Shift out the segment data for the current digit
          shiftOutDigit(digitCodes[digits[i]]);

          delay(5);                        // Small delay for multiplexing
          digitalWrite(digitPins[i], HIGH); // Deactivate current digit
        }
      }

#. Shifting Out the Segment Data:

   * Sends the segment data to the 74HC595 shift register.
   * ``shiftOut()`` sends the data one bit at a time, starting with the most significant bit (``MSBFIRST``).
   * Latches the data to the output pins by toggling the ``LATCH_PIN``.

   .. code-block:: arduino

      void shiftOutDigit(byte data) {
        // Send data to the shift register
        digitalWrite(LATCH_PIN, LOW);
        shiftOut(DATA_PIN, CLOCK_PIN, MSBFIRST, data);
        digitalWrite(LATCH_PIN, HIGH);
      }
  
**Experimenting Further**

* Add a Reset Button:

  Connect a button to the Pico to reset the counter when pressed.

* Display Different Data: 

  Modify the code to display sensor readings, such as temperature or light levels.

* Create a Stopwatch:

  Implement start, stop, and reset functionality to use the display as a stopwatch.

**Conclusion**

This project demonstrates how to control a 4-digit 7-segment display using a shift register and multiplexing techniques. By efficiently managing timing with ``millis()``, we create a responsive and accurate time counter without hindering the display's performance.