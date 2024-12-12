.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_keypad:

4.2 4x4 Keypad
========================

In this lesson, we'll learn how to interface a **4x4 matrix keypad** with the Raspberry Pi Pico 2 to detect which keys are pressed. Matrix keypads are commonly used in devices like calculators, telephones, vending machines, and security systems for numerical input.

* :ref:`cpn_keypad`
* `E.161 - Wikipedia <https://en.wikipedia.org/wiki/E.161>`_

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

|sch_keypad|

4 pull-down resistors are connected to each of the columns of the matrix keyboard, so that G6 ~ G9 get a stable low level when the keys are not pressed.

The rows of the keyboard (G2 ~ G5) are programmed to go high; if one of G6 ~ G9 is read high, then we know which key is pressed.

For example, if G6 is read high, then numeric key 1 is pressed; this is because the control pins of numeric key 1 are G2 and G6, when numeric key 1 is pressed, G2 and G6 will be connected together and G6 is also high.


**Wiring**

|wiring_keypad|

To make the wiring easier, in the above diagram, the column row of the matrix keyboard and the 10K resistors are inserted into the holes where G6 ~ G9 are located at the same time.


**Writing the Code**

Let's write a MicroPython program to read which key is pressed.

.. note::

    * Open the ``4.2_4x4_keypad.py`` from ``pico-2w-kit-main/micropython`` or copy the code into Thonny, then click "Run" or press F5.
    * Ensure the correct interpreter is selected: MicroPython (Raspberry Pi Pico).COMxx. 
    

.. code-block:: python

    import machine
    import time

    # Define the characters on the keypad
    keys = [
        ['1', '2', '3', 'A'],
        ['4', '5', '6', 'B'],
        ['7', '8', '9', 'C'],
        ['*', '0', '#', 'D']
    ]

    # Define the GPIO pins connected to the rows and columns
    row_pins = [2, 3, 4, 5]   # GP2-GP5
    col_pins = [6, 7, 8, 9]   # GP6-GP9

    # Initialize row pins as outputs
    rows = [machine.Pin(pin_num, machine.Pin.OUT) for pin_num in row_pins]

    # Initialize column pins as inputs with pull-down resistors
    cols = [machine.Pin(pin_num, machine.Pin.IN, machine.Pin.PULL_DOWN) for pin_num in col_pins]

    def scan_keypad():
        for i, row in enumerate(rows):
            # Set all rows low
            for r in rows:
                r.value(0)
            # Set the current row high
            row.value(1)
            # Check columns for a high signal
            for j, col in enumerate(cols):
                if col.value() == 1:
                    # Key detected
                    return keys[i][j]
        return None

    last_key = None

    while True:
        key = scan_keypad()
        if key != last_key:
            if key is not None:
                print("Key pressed:", key)
            last_key = key
        time.sleep(0.1)

**Understanding the Code**

#. Define Keypad Characters

   This 2D list represents the keypad layout, matching the physical arrangement.

   .. code-block:: python

        keys = [
            ['1', '2', '3', 'A'],
            ['4', '5', '6', 'B'],
            ['7', '8', '9', 'C'],
            ['*', '0', '#', 'D']
        ]


#. Initialize Pins:

   .. code-block:: python

        row_pins = [2, 3, 4, 5]   # GPIO pins for rows
        col_pins = [6, 7, 8, 9]   # GPIO pins for columns

        # Initialize rows as outputs
        rows = [machine.Pin(pin_num, machine.Pin.OUT) for pin_num in row_pins]

        # Initialize columns as inputs with pull-down resistors
        cols = [machine.Pin(pin_num, machine.Pin.IN, machine.Pin.PULL_DOWN) for pin_num in col_pins]

#. Define the Keypad Scanning Function:

    The function scans each row by setting it high and checking if any column reads high, indicating a key press at that row and column.

   .. code-block:: python

        def scan_keypad():
            for i, row in enumerate(rows):
                # Set all rows low
                for r in rows:
                    r.value(0)
                # Set the current row high
                row.value(1)
                # Check columns for a key press
                for j, col in enumerate(cols):
                    if col.value() == 1:
                        # Key is pressed
                        return keys[i][j]
            return None

#. Main Loop to Detect Key Presses

   * The loop continuously scans for key presses.
   * It checks if the current key is different from the last key to prevent multiple detections of the same key press (debouncing).
   * Prints the key when a new key press is detected.

   .. code-block:: python

        last_key = None

        while True:
            key = scan_keypad()
            if key != last_key:
                if key is not None:
                    print("Key pressed:", key)
                last_key = key
            time.sleep(0.1)

After running the program, Press different keys on the keypad. The corresponding key character should be printed in the Thonny Shell.

**Troubleshooting Tips**

* No Output When Pressing Keys:

  * Ensure all connections are correct.
  * Verify that the pull-down resistors are properly connected between the column pins and GND.

* Incorrect Key Detected:

  * Double-check the keys array to ensure it matches your keypad's layout.
  * Make sure the row and column pins in the code match the physical connections.

* Multiple Keys Detected:

  Mechanical keypads may sometimes detect ghosting (false key presses) if multiple keys are pressed simultaneously. For this basic setup, avoid pressing multiple keys at once.

**Experimenting Further**

* **Implement a Simple Password Lock**: Store a sequence of key presses and compare them to a preset password.
* **Add an LCD Display**: Display the keys pressed on an LCD screen.
* **Create a Calculator**: Use the keypad to input numbers and perform basic arithmetic operations.

**Conclusion**

In this lesson, you've learned how to connect and program a 4x4 matrix keypad with the Raspberry Pi Pico 2w. You can now detect key presses and use them to interact with your projects, opening up possibilities for creating interactive devices like locks, calculators, and control interfaces.
