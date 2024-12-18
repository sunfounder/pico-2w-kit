.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_joystick:

4.1 Toggle the Joystick
================================

In this lesson, we'll learn how to use a **joystick** with the Raspberry Pi Pico 2 W to read analog values and detect button presses. A joystick is a common input device that allows you to control movement along two axes (X and Y) and often includes a button when pressed down (Z-axis).

* :ref:`cpn_joystick`

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
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_joystick`
        - 1
        - 

**Understanding the Joystick**

A typical joystick module consists of two potentiometers positioned at right angles to each other:

* **X-axis potentiometer**: Measures left-right movement.
* **Y-axis potentiometer**: Measures up-down movement.
* **Z-axis (Switch)**: A digital button activated when you press down on the joystick.

By reading the analog values from the X and Y axes, you can determine the position of the joystick. The Z-axis button allows you to detect when the joystick is pressed down.


**Schematic**

|sch_joystick|

The SW pin is connected to a 10K pull-up resistor, the reason is to be able to get a stable high level on the SW pin (Z axis) when the joystick is not pressed; otherwise the SW is in a suspended state and the output value may vary between 0/1.

**Wiring**

|wiring_joystick|


**Writing the Code**

Let's write a MicroPython program to read the joystick's X and Y positions and detect button presses.

.. note::

    * Open the ``4.1_toggle_the_joystick.py`` from ``pico-2 w-kit-main/micropython`` or copy the code into Thonny, then click "Run" or press F5.

    * Ensure the correct interpreter is selected: MicroPython (Raspberry Pi Pico).COMxx. 

    

.. code-block:: python

    import machine
    import utime

    # Initialize ADC for X and Y axes
    x_adc = machine.ADC(27)  # GP27
    y_adc = machine.ADC(26)  # GP26

    # Initialize digital input for the switch
    z_button = machine.Pin(22, machine.Pin.IN, machine.Pin.PULL_UP)

    while True:
        # Read the analog values (0-65535)
        x_value = x_adc.read_u16()
        y_value = y_adc.read_u16()
        
        # Read the button state (0 or 1)
        z_state = z_button.value()
        
        # Print the values
        print("X:", x_value, "Y:", y_value, "Button:", z_state)
        
        # Small delay to make the output readable
        utime.sleep(0.2)


**Understanding the Code**

#. Import Modules:

   * ``machine``: Provides access to hardware-related functions.
   * ``utime``: Contains time-related functions for delays.

#. Initialize the ADC Inputs:

   We set up analog-to-digital converters (ADC) on pins GP27 and GP26 to read the joystick's X and Y positions.

   .. code-block:: python

      x_adc = machine.ADC(27)  # X-axis connected to GP27
      y_adc = machine.ADC(26)  # Y-axis connected to GP26

#. Initialize the Digital Input:

   * Configure GP22 as a digital input with an internal pull-up resistor for the joystick's button (Z-axis).
   * The ``machine.Pin.PULL_UP`` parameter ensures the pin reads high (1) when not pressed and low (0) when pressed.

   .. code-block:: python

      z_button = machine.Pin(22, machine.Pin.IN, machine.Pin.PULL_UP)

#. Main Loop to Read Values:

   * Read Analog Values: ``read_u16()`` reads a 16-bit value (0 to 65535) representing the voltage level.
   * Print the Values: Displays the X and Y positions and the button state in the console.

   .. code-block:: python

      while True:
          x_value = x_adc.read_u16()
          y_value = y_adc.read_u16()
          z_state = z_button.value()
          
          print("X:", x_value, "Y:", y_value, "Button:", z_state)
          
          utime.sleep(0.2)

After running the program, open the Shell or REPL window in Thonny.

* You should see the X, Y, and Button values being printed.
* Move the joystick in different directions and press the button to see the values change.

**Interpreting the Values**

* X and Y Values:

  * Range from 0 to 65535.
  * Center Position: Around 32768.
  * Full Left or Up: Close to 0.
  * Full Right or Down: Close to 65535.

* Button State:

  * Not Pressed: 1.
  * Pressed: 0.

**Experimenting Further**

* Normalize the Values:

  Convert the raw ADC values to a range of -100 to 100 for easier interpretation.

  .. code-block:: python

    import machine
    import utime

    # Initialize ADC for X and Y axes
    x_adc = machine.ADC(27)  # GP27
    y_adc = machine.ADC(26)  # GP26

    # Initialize digital input for the switch
    z_button = machine.Pin(22, machine.Pin.IN, machine.Pin.PULL_UP)

    # Function to normalize ADC values to a range of -100 to 100
    def normalize(value):
        return int((value - 32768) / 327.68)

    while True:
        # Read the analog values (0-65535)
        x_value = x_adc.read_u16()
        y_value = y_adc.read_u16()
        
        # Read the button state (0 or 1)
        z_state = z_button.value()
        
        # Normalize the values to -100 to 100
        x_normalized = normalize(x_value)
        y_normalized = normalize(y_value)
        
        # Print the normalized values
        print("X:", x_normalized, "Y:", y_normalized, "Button:", z_state)
        
        # Small delay to make the output readable
        utime.sleep(0.2)


* Control an Output:

  Use the joystick input to control an LED, servo, or motor. For example, move an object left or right based on the X-axis value.

* Create a Game Controller:

  Combine the joystick inputs to control a simple game or graphical output.

**Conclusion**

In this lesson, you've learned how to read analog and digital inputs from a joystick using the Raspberry Pi Pico 2 W. This knowledge allows you to incorporate joystick controls into your projects, enabling interactive applications like robots, games, or remote controls.


