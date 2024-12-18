.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ar_74hc_led:

5.1 Using the 74HC595 Shift Register
===========================================================

In this lesson, we'll learn how to use the **74HC595 shift register** to control multiple LEDs with just a few GPIO pins on the Raspberry Pi Pico 2. The 74HC595 is an integrated circuit (IC) that allows you to expand the number of digital outputs using a serial input. This is incredibly useful when you want to control many outputs but have limited GPIO pins available.

* :ref:`74HC595`

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
        - 8(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 8
        - |link_led_buy|
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|

**Understanding the 74HC595 Shift Register**

The **74HC595** is an 8-bit serial-in, parallel-out shift register with output latches. It has the ability to take serial data input and convert it into parallel output, allowing you to control 8 outputs using only 3 GPIO pins from the Pico.

**Key Pins on the 74HC595:**

|img_74jc595_pin|

* **DS (Pin 14)**: Serial Data Input
* **SHCP (Pin 11)**: Shift Register Clock Input
* **STCP (Pin 12)**: Storage Register Clock Input (Latch Pin)
* **OE (Pin 13)**: Output Enable (Active Low, connect to GND)
* **MR (Pin 10)**: Master Reset (Active Low, connect to 3.3V)
* **Q0-Q7 (Pins 15, 1-7)**: Parallel Outputs
* **VCC (Pin 16)**: Connect to 3.3V
* **GND (Pin 8)**: Connect to GND

**Schematic**

|sch_74hc_led|


**Wiring**


|wiring_74hc_led|

**Writing the Code**

We'll write a program that controls the LEDs connected to the 74HC595 shift register by sending serial data from the Pico. The LEDs will light up one after another in a sequence.

.. note::

    * You can open the file ``5.1_microchip_74hc595.ino`` under the path of ``pico-2 w-kit-main/arduino/5.1_microchip_74hc595``. 
    * Or copy this code into **Arduino IDE**.
    * Don't forget to select the board(Raspberry Pi Pico) and the correct port before clicking the **Upload** button.


.. code-block:: arduino

  // Define the pins connected to the 74HC595
  const int DS = 0;   // GPIO 0 -> DS (Pin 14)
  const int SHCP = 1; // GPIO 1 -> SHCP (Pin 11)
  const int STCP = 2; // GPIO 2 -> STCP (Pin 12)

  // Array of binary patterns to control LEDs
  int datArray[] = {
    0b00000000, // All LEDs off
    0b00000001, // LED 0 on
    0b00000011, // LEDs 0 and 1 on
    0b00000111, // LEDs 0, 1, and 2 on
    0b00001111, // LEDs 0, 1, 2, and 3 on
    0b00011111, // LEDs 0 to 4 on
    0b00111111, // LEDs 0 to 5 on
    0b01111111, // LEDs 0 to 6 on
    0b11111111  // All LEDs on
  };

  void setup() {
    // Initialize the control pins as outputs
    pinMode(DS, OUTPUT);
    pinMode(SHCP, OUTPUT);
    pinMode(STCP, OUTPUT);
  }

  void loop() {
    // Iterate through each pattern in datArray
    for (int num = 0; num < 9; num++) {
      // Set STCP to LOW to prepare for data
      digitalWrite(STCP, LOW);

      // Shift out the data to the shift register
      shiftOut(DS, SHCP, MSBFIRST, datArray[num]);

      // Set STCP to HIGH to latch the data to the output pins
      digitalWrite(STCP, HIGH);

      delay(500); // Wait for half a second before the next pattern
    }

    // Turn off all LEDs after the sequence
    digitalWrite(STCP, LOW);
    shiftOut(DS, SHCP, MSBFIRST, 0b00000000);
    digitalWrite(STCP, HIGH);
    delay(500);
  }

After uploading the code, the LEDs connected to the 74HC595 should light up one after another, following the patterns defined in ``datArray``.
After all LEDs are turned on, they will turn off in sequence.

**Understanding the Code**

#. Defining Control Pins:

   * ``DS (Data Serial Input)``: Receives the serial data.
   * ``SHCP (Shift Register Clock Input)``: Controls the shifting of data into the register.
   * ``STCP (Storage Register Clock Input)``: Controls the latching of data to the output pins.

   .. code-block:: arduino

      const int DS = 0;   // GPIO 0 -> DS (Pin 14)
      const int SHCP = 1; // GPIO 1 -> SHCP (Pin 11)
      const int STCP = 2; // GPIO 2 -> STCP (Pin 12)

#. Creating Data Patterns:

   * An array ``datArray`` holds different binary patterns to control the LEDs.
   * Each bit represents the state of an LED (1 for on, 0 for off).

   .. code-block:: arduino

      int datArray[] = {
        0b00000000, // All LEDs off
        0b00000001, // LED 0 on
        0b00000011, // LEDs 0 and 1 on
        0b00000111, // LEDs 0, 1, and 2 on
        0b00001111, // LEDs 0, 1, 2, and 3 on
        0b00011111, // LEDs 0 to 4 on
        0b00111111, // LEDs 0 to 5 on
        0b01111111, // LEDs 0 to 6 on
        0b11111111  // All LEDs on
      };
  
#. Setup Function:

   Sets the ``DS``, ``SHCP``, and ``STCP`` pins as outputs to send data to the shift register.

   .. code-block:: arduino

      void setup() {
        // Initialize the control pins as outputs
        pinMode(DS, OUTPUT);
        pinMode(SHCP, OUTPUT);
        pinMode(STCP, OUTPUT);
      }

#. Loop Function: The ``for`` loop cycles through each pattern in the ``datArray`` array.

   * Shifting Out Data:

     * ``shiftOut`` sends the byte of data one bit at a time.
     * ``MSBFIRST`` indicates that the most significant bit is sent first.

     .. code-block:: arduino

        shiftOut(DS, SHCP, MSBFIRST, datArray[num]);

   * Latching Data:

     * Setting ``STCP`` ``LOW`` prepares the shift register for new data.
     * After shifting out the data, setting ``STCP`` ``HIGH`` latches the data to the output pins, updating the LED states.

     .. code-block:: arduino

        digitalWrite(STCP, LOW);
        // shiftOut(...)
        digitalWrite(STCP, HIGH);

   * Delay:
   
     ``delay(500);`` adds a half-second pause between each pattern for visibility.

   * Turning Off LEDs: 
     
     After cycling through all patterns, turns off all LEDs by sending 0b00000000.

     .. code-block:: arduino

        digitalWrite(STCP, LOW);
        shiftOut(DS, SHCP, MSBFIRST, 0b00000000);
        digitalWrite(STCP, HIGH);
        delay(500);

**Troubleshooting**

* No LEDs Lighting Up:

  * Check all wiring connections.
  * Ensure the 74HC595 is properly powered.
  * Verify that the GPIO pins on the Pico are correctly connected to the shift register.

* Incorrect LED Behavior:

  * Double-check the binary patterns in ``datArray``.
  * Ensure that the resistors are correctly placed to limit current to the LEDs.

**Further Exploration**

* Controlling Other Devices:

  Use the 74HC595 to control relays, motors, or other high-power devices.

* Chaining Shift Registers:

  Connect multiple 74HC595s in series to control even more outputs with the same three GPIO pins.

* Creating LED Patterns:

  Design and implement more complex LED animations and patterns by modifying the datArray.

* Integrating with Sensors:

  Combine the shift register with various sensors to create responsive and interactive systems.

* Building a LED Matrix Display:

  Use multiple shift registers to build a larger LED matrix for displays or signage.

**Conclusion**

In this lesson, you've learned how to use the 74HC595 shift register with the Raspberry Pi Pico to control multiple LEDs using just three GPIO pins. This technique allows you to expand the number of digital outputs, enabling more complex and interactive projects without the need for additional GPIO resources. By understanding how to send serial data and latch it into parallel outputs, you can efficiently manage multiple actuators, displays, or other peripherals in your electronics projects.
