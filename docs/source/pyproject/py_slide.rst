.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_slide:

2.7 Toggle Left and Right
====================================

|img_slide|

In this lesson, we'll learn how to use a **slide switch** with the Raspberry Pi Pico 2 W to detect its position (left or right) and perform actions based on that. A slide switch is a simple mechanical device that connects the common (middle) pin to one of the two outer pins depending on its position.

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
        - :ref:`cpn_capacitor`
        - 1(104)
        - |link_capacitor_buy|
    *   - 7
        - :ref:`cpn_slide_switch`
        - 1
        - 

**Schematic**

|img_slide|

A slide switch has three pins:

- **Pin 1**: Connected when the switch is toggled to one side (e.g., left)
- **Pin 2**: Common pin (middle pin)
- **Pin 3**: Connected when the switch is toggled to the other side (e.g., right)

By reading the voltage on the common pin, we can determine the position of the switch.

**Circuit Diagram**

|sch_slide|

GP14 will get a different level, when you toggle the slide switch to the right or left.

The purpose of the 10K resistor is to keep the GP14 low during toggling (not toggling to the far left and not toggling to the far right).

When you toggle the switch, the mechanical contacts can cause rapid, noisy signals known as "bounce." The capacitor connected between GP14 and GND helps to filter out these rapid fluctuations, providing a cleaner signal.

* Switch Toggled to the Right:

  * Pin 2 (GP14) is connected to **3.3V** through Pin 1.
  * The GPIO pin reads **HIGH** (1).

* Switch Toggled to the Left:

  * Pin 2 (GP14) is connected to **GND** through Pin 3.
  * The GPIO pin reads **LOW** (0).

* Switch in the Middle Position:

  * Pin 2 (GP14) is not connected to either **3.3V** or **GND**.
  * The pull-down resistor keeps the GPIO pin at **LOW** (0).
  * The capacitor helps to reduce switch bounce (noise due to mechanical movement).


**Wiring**

|wiring_slide|

**Writing the Code**

We'll write a MicroPython program that detects the position of the slide switch and prints a message accordingly.

.. note::

  * Open the ``2.7_slide_switch.py`` from ``pico-2w-kit-main/micropython`` or copy the code into Thonny, then click "Run" or press F5.

  * Ensure the correct interpreter is selected: MicroPython (Raspberry Pi Pico).COMxx. 

  

.. code-block:: python

  import machine
  import utime

  # Initialize GP14 as an input
  slide_switch = machine.Pin(14, machine.Pin.IN)

  while True:
      switch_state = slide_switch.value()
      if switch_state == 1:
          print("Switch is toggled to the LEFT!")
      else:
          print("Switch is toggled to the RIGHT!")
      utime.sleep(0.5)

When the code is running, you will observe the following phenomenon:

* **Toggle to the Right**: You should see "Switch is toggled to the RIGHT!" in the console.
* **Toggle to the Left**: You should see "Switch is toggled to the LEFT!" in the console.


**Understanding the Code**

#. Import Modules:

   * ``import machine``: Access hardware functions.
   * ``import utime``: Use time-related functions.

#. Initialize the Slide Switch Pin:

   * ``slide_switch = machine.Pin(14, machine.Pin.IN)``: Sets up GP14 as an input pin.

#. Main Loop:

   * ``while True``: Creates an infinite loop to continuously check the switch state.
   * ``switch_state = slide_switch.value()``: Reads the current state of the switch.
   * ``if switch_state == 1``: Checks if the GPIO pin is HIGH (switch toggled to the left).
   * ``print("Switch is toggled to the RIGHT!")``: Prints a message.
   * ``else``: If the GPIO pin is LOW (switch toggled to the right or in the middle).
   * ``print("Switch is toggled to the LEFT!")``: Prints a message.
   * ``utime.sleep(0.5)``: Adds a short delay to debounce the switch and avoid flooding the console.


**Alternative: Using an internal pull-down resistor**

The Raspberry Pi Pico 2 W allows us to enable internal pull-down resistors, eliminating the need for an external resistor.

* Modify the Circuit:

  Remove the external 10 kΩ resistor and 0.1 µF capacitor.

* Modified Code:

  .. code-block:: python

    import machine
    import utime

    # Initialize GP14 as an input with internal pull-down resistor
    slide_switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

    while True:
        switch_state = slide_switch.value()
        if switch_state == 1:
            print("Switch is toggled to the LEFT!")
        else:
            print("Switch is toggled to the RIGHT!")
        utime.sleep(0.5)
  
**Practical Applications**

* **Mode Selection**: Use the switch to toggle between different modes in your program.
* **Power Control**: Control power to certain parts of your circuit.
* **User Input**: Provide simple user controls for your projects.

**Experimenting Further**

* Add an LED Indicator:

  Connect an LED to another GPIO pin (e.g., GP15) with a suitable resistor.Modify the code to turn the LED on or off based on the switch position.

  .. code-block:: python

    import machine
    import utime

    slide_switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
    led = machine.Pin(15, machine.Pin.OUT)

    while True:
        if slide_switch.value() == 1:
            led.value(1)  # Turn on the LED
        else:
            led.value(0)  # Turn off the LED
        utime.sleep(0.1)

* Detect Middle Position:

  To detect when the switch is in the middle (neither left nor right), you'll need to modify the wiring and code to read all three states.

**Conclusion**

Using a slide switch with the Raspberry Pi Pico 2 W allows you to add physical input controls to your projects. By understanding how to read the switch's state and handle potential issues like switch bounce, you can create more interactive and user-friendly applications.

