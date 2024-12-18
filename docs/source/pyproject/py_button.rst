.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_button:

2.5 Reading Button Value
==============================================

In this lesson, we'll learn how to read input from a pushbutton using the Raspberry Pi Pico 2 W. So far, we've used the GPIO pins mainly for output, like lighting up LEDs. Now, we'll use a GPIO pin as an input to detect when a button is pressed. This is a fundamental skill for creating interactive projects.

* :ref:`cpn_button`

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
        - :ref:`cpn_button`
        - 1
        - |link_button_buy|

**Circuit Diagram**

|sch_button|

As long as one side of the button pin is connected to 3.3v, and the other side pin is connected to GP14, then when the button is pressed, GP14 will be high. However, when the button is not pressed, GP14 is in a suspended state and may be high or low. In order to get a stable low level when the button is not pressed, GP14 needs to be reconnected to GND through a 10K pull-down resistor.

* **Button Not Pressed**: The GP14 pin is connected to GND through the resistor, so it reads **LOW (0)**.
* **Button Pressed**: The GP14 pin is connected to 3.3V through the button, so it reads **HIGH (1)**.


**Wiring Diagram**




.. Let's follow the direction of the circuit to build the circuit!

.. 1. Connect the 3V3 pin of Pico 2 W to the positive power bus of the breadboard.
.. #. Insert the button into the breadboard and straddle the central dividing line.

.. note::
    A four-pin button is shaped like an H. Its left two pins or right two pins are connected, which means that when it crosses the central gap, it connects two half rows with the same row number. (For example, in my circuit, E23 and F23 are already connected, as are E25 and F25).

    Until the button is pressed, the left and right pins are independent of each other and current cannot flow from one side to the other.

.. #. Use a jumper wire to connect one of the button pins to the positive bus (mine is the pin on the upper right).
.. #. Connect the other pin (upper left or lower left) to GP14 with a jumper wire.
.. #. Use a 10K resistor to connect the pin on the upper left corner of the button and the negative bus.
.. #. Connect the negative power bus of the breadboard to Pico's GND.

|wiring_button|

**Writing the Code**

We'll write a simple program that prints a message when the button is pressed.

.. note::

  * Open the ``2.5_read_button_value.py`` from ``pico-2 w-kit-main/micropython`` or copy the code into Thonny, then click "Run" or press F5.
  * Ensure the correct interpreter is selected: MicroPython (Raspberry Pi Pico).COMxx. 

.. code-block:: python

    import machine
    import utime

    # Initialize GP14 as an input pin
    button = machine.Pin(14, machine.Pin.IN)

    while True:
        if button.value() == 1:
            print("Button pressed!")
            utime.sleep(0.2)  # Debounce delay

When the code is running, you will observe the following phenomenon:

* **Not Pressed**: No message should appear.
* **Pressed**: "Button pressed!" should appear in the console each time you press the switch.



**Understanding the Code**

#. Import Modules:

   * ``machine``: Provides access to the hardware functions.
   * ``utime``: Allows us to use time-related functions like delays.

#. Set Up the Button Pin:

   * ``button = machine.Pin(14, machine.Pin.IN)``: Initializes GPIO pin 14 as an input.

#. Main Loop:

   * ``while True``: Creates an infinite loop.
   * ``if button.value() == 1``: Checks if the button is pressed.
   * ``button.value()`` returns 1 when the pin reads high (button pressed).
   * ``print("Button pressed!")``: Prints a message to the console.
   * ``utime.sleep(0.2)``: Waits for 200 milliseconds to debounce the button.

**Alternate Wiring: Pull-Up Resistor**

You can also wire the button using a pull-up resistor configuration.

#. Connect a 10kΩ resistor between GP14 and the 3.3V rail. This pulls the pin high when the button is not pressed.

    |sch_button_pullup|

    |wiring_button_pullup|

   * **Button Not Pressed**: The GP14 pin is connected to 3.3V through the resistor, so it reads HIGH (1).
   * **Button Pressed**: The GP14 pin is connected to GND through the button, so it reads LOW (0).

#. Modified Code for Pull-Up Configuration.

   .. code-block:: python
   
       import machine
       import utime
   
       # Initialize GP14 as an input pin
       button = machine.Pin(14, machine.Pin.IN)
   
       while True:
           if button.value() == 0:
               print("Button pressed!")
               utime.sleep(0.2)

**Using Internal Pull-Up/Pull-Down Resistors**

The Raspberry Pi Pico 2 W allows you to enable internal pull-up or pull-down resistors, eliminating the need for external resistors.

Using internal resistors simplifies wiring and saves space by eliminating the need for additional external resistors on the breadboard.

* Enabling Internal Pull-Down Resistor:

  .. code-block:: python
  
      import machine
      import utime
  
      # Initialize GP14 as an input with an internal pull-down resistor
      button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
  
      while True:
          if button.value() == 1:
              print("Button pressed!")
              utime.sleep(0.2)

* Enabling Internal Pull-Up Resistor:

  .. code-block:: python

    import machine
    import utime

    # Initialize GP14 as an input with an internal pull-up resistor
    button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)

    while True:
        if button.value() == 0:
            print("Button pressed!")
            utime.sleep(0.2)

**Experimenting Further**

* **Multiple Buttons**: Connect additional buttons to other GPIO pins and modify the code to handle multiple inputs.
* **LED Control**: Combine button input with LED output to toggle the LED state when the button is pressed.

.. code-block:: python

    import machine
    import utime

    button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
    led = machine.Pin(15, machine.Pin.OUT)
    led_state = False

    while True:
        if button.value() == 1:
            led_state = not led_state  # Toggle LED state
            led.value(led_state)
            utime.sleep(0.2)

**Conclusion**

Reading input from a button is a fundamental skill in microcontroller programming. It allows you to make your projects interactive and responsive to user input. Understanding how to use pull-up and pull-down resistors ensures reliable and stable readings from your input devices.
