.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ar_keypad:

4.2 Using a 4x4 Keypad
=================================================

In this lesson, we'll learn how to interface a **4x4 matrix keypad** with the Raspberry Pi Pico 2w to detect which keys are pressed. Matrix keypads are commonly used in devices like calculators, telephones, vending machines, and security systems for numerical input.

* :ref:`cpn_keypad`


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
        - 4(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_keypad`
        - 1
        - |link_keypad_buy|

**Understanding the 4x4 Keypad**

A 4x4 keypad consists of:

* **16 keys** arranged in 4 rows and 4 columns.
* **8 pins**: 4 connected to rows and 4 connected to columns.

When you press a key, it connects a specific row and column, allowing us to identify the key based on the row and column numbers.

Here's how the keys are arranged:

|img_keypad|

**Schematic**

|sch_keypad_ar|

The rows of the keyboard (G2 ~ G5) are programmed to go high; if one of G6 ~ G9 is read high, then we know which key is pressed.

For example, if G6 is read high, then numeric key 1 is pressed; this is because the control pins of numeric key 1 are G2 and G6, when numeric key 1 is pressed, G2 and G6 will be connected together and G6 is also high.


**Wiring**

|wiring_keypad_ar|

**Writing the Code**


.. note::

    * You can open the file ``4.2_4x4_keypad.ino`` under the path of ``pico-2w-starter-kit-main/arduino/4.2_4x4_keypad``. 
    * Or copy this code into **Arduino IDE**.
    * Then select the Raspberry Pi Pico board and the correct port before clicking the Upload button.
    * The ``Adafruit Keypad`` library is used here, you can install it from the **Library Manager**.

      .. image:: img/lib_ad_keypad.png

.. code-block:: arduino

    #include "Adafruit_Keypad.h"

    // Define the number of rows and columns
    const byte ROWS = 4;
    const byte COLS = 4;

    // Define the keymap for the keypad
    char keys[ROWS][COLS] = {
      { '1', '2', '3', 'A' },
      { '4', '5', '6', 'B' },
      { '7', '8', '9', 'C' },
      { '*', '0', '#', 'D' }
    };

    // Connect to the row pinouts of the keypad
    byte rowPins[ROWS] = { 2, 3, 4, 5 };

    // Connect to the column pinouts of the keypad
    byte colPins[COLS] = { 6, 7, 8, 9 };

    // Create the Keypad object
    Adafruit_Keypad myKeypad = Adafruit_Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

    void setup() {
      // Initialize Serial communication
      Serial.begin(115200);

      // Initialize the keypad
      myKeypad.begin();
    }

    void loop() {
      // Update the state of keys
      myKeypad.tick();

      // Check if there are any new keypad events
      while (myKeypad.available()) {
        // Read the keypad event
        keypadEvent e = myKeypad.read();

        // Check if the event is a key press
        if (e.bit.EVENT == KEY_JUST_PRESSED) {
          // Print the key value to the Serial Monitor
          Serial.println((char)e.bit.KEY);
        }
      }

      delay(10); // Short delay to improve stability
    }

After uploading the code, press any key on the keypad. The corresponding key label (e.g., '1', 'A') should appear in the Serial Monitor.

Ensure that each key press is accurately detected and displayed. Test all keys to confirm proper functionality.

**Understanding the Code**

#. Including the Library:

   This line includes the Adafruit Keypad library, which provides functions to interact with the keypad.

   .. code-block:: arduino

      #include "Adafruit_Keypad.h"

#. Defining the Keypad Layout:

   ``ROWS`` and ``COLS`` define the dimensions of the keypad. ``keys`` is a 2D array representing the label of each key on the keypad.

   .. code-block:: arduino

      const byte ROWS = 4;
      const byte COLS = 4;

      char keys[ROWS][COLS] = {
        { '1', '2', '3', 'A' },
        { '4', '5', '6', 'B' },
        { '7', '8', '9', 'C' },
        { '*', '0', '#', 'D' }
      };

#. Connecting the Keypad to GPIO Pins:

   ``rowPins`` and ``colPins`` are arrays that store the GPIO pins connected to the keypad's rows and columns, respectively.

   .. code-block:: arduino

      byte rowPins[ROWS] = { 2, 3, 4, 5 };
      byte colPins[COLS] = { 6, 7, 8, 9 };

#. Initializing the Keypad Object:

   This line creates an instance of the ``Adafruit_Keypad`` class, initializing it with the keymap and pin configurations.

   .. code-block:: arduino

      Adafruit_Keypad myKeypad = Adafruit_Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

#. Setup Function:

   Initializes serial communication for debugging and starts the keypad.

   .. code-block:: arduino

      void setup() {
        Serial.begin(115200);    // Initialize serial communication at 115200 baud
        myKeypad.begin();        // Initialize the keypad
      }

#. Loop Function:

   * Continuously checks for key events.
   * When a key is pressed, it prints the key value to the Serial Monitor.

   .. code-block:: arduino

      void loop() {
        myKeypad.tick(); // Update the state of keys

        while (myKeypad.available()) {
          keypadEvent e = myKeypad.read(); // Read the keypad event

          if (e.bit.EVENT == KEY_JUST_PRESSED) {
            Serial.println((char)e.bit.KEY); // Print the pressed key
          }
        }
        delay(10); // Short delay to improve stability
      }

**Further Exploration**

* Implementing Key Debouncing:

  Improve the reliability of key detection by implementing debouncing techniques to filter out false triggers caused by mechanical noise.

* Creating a Password Entry System:

  Use the keypad to enter a password and control access to certain functionalities in your project.

* Integrating with Other Components:

  Combine the keypad with LCD displays, LEDs, or buzzers to create more complex user interfaces.

* Building a Simple Calculator:

  Use the keypad to input numbers and perform basic arithmetic operations displayed on an LCD.

**Conclusion**

In this lesson, you've learned how to interface a 4x4 matrix keypad with the Raspberry Pi Pico using the Adafruit Keypad library. By detecting key presses, you can create interactive projects such as key-based input systems, password entry mechanisms, and more. Understanding how to read and process keypad inputs is essential for building user-friendly interfaces in your electronics projects.
