.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_micro:

2.8 Press Gently
==========================

|img_micro_switch|

In this lesson, we'll learn how to use a **micro switch** (also known as a limit switch) with the Raspberry Pi Pico 2 W to detect when it's pressed or released. Micro switches are commonly used in devices like microwave oven doors, printer covers, or as end stops in 3D printers because they are reliable and can handle frequent activation.

* :ref:`cpn_micro_switch`

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
        - :ref:`cpn_micro_switch`
        - 1
        - 

**Understanding the Micro Switch**

A micro switch typically has three pins:

|img_micro_switch|

- **Common (C)**: The middle pin.
- **Normally Open (NO)**: Connected to the common pin when the switch is **pressed**.
- **Normally Closed (NC)**: Connected to the common pin when the switch is **not pressed**.

By connecting the switch appropriately, we can detect when it's pressed by reading the voltage level on a GPIO pin.

**Schematic**

|sch_limit_sw|

By default, GP14 is low and when pressed, GP14 is high.

The purpose of the 10K resistor is to keep the GP14 low during pressing.

When you press a mechanical switch, the contacts may bounce, causing multiple rapid transitions between open and closed states. The capacitor connected between GP14 and GND helps filter out this noise.

* **Switch Not Pressed**:

  * The **Common (C)** pin is connected to the **NC** pin, which is connected to **GND**.
  * **GP14** reads **LOW** (0V).

* **Switch Pressed**:

  * The **Common (C)** pin is connected to the **NO** pin, which is connected to **3.3V**.
  * **GP14** reads **HIGH** (3.3V).


**Wiring**

|wiring_limit_sw|


**Writing the Code**

We'll write a MicroPython program that detects when the micro switch is pressed and prints a message accordingly.

.. note::

  * Open the ``2.8_micro_switch.py`` from ``pico-2 w-kit-main/micropython`` or copy the code into Thonny, then click "Run" or press F5.

  * Ensure the correct interpreter is selected: MicroPython (Raspberry Pi Pico).COMxx. 

  

.. code-block:: python

    import machine
    import utime

    # Initialize GP14 as an input pin
    switch = machine.Pin(14, machine.Pin.IN)

    while True:
        if switch.value() == 1:
            print("The switch is pressed!")
            utime.sleep(0.5)  # Debounce delay

When the code is running, you will observe the following phenomenon:

* **Not Pressed**: No message should appear.
* **Pressed**: "The switch is pressed!" should appear in the console each time you press the switch.

**Understanding the Code**

#. Import Modules:

   * ``import machine``: Access to hardware functions.
   * ``import utime``: Time-related functions.

#. Initialize the Switch Pin:

   * ``switch = machine.Pin(14, machine.Pin.IN)``: Sets up GP14 as an input pin.

#. Main Loop:

   * ``while True``: Starts an infinite loop.
   * ``if switch.value() == 1``: Checks if the switch is pressed (GP14 reads HIGH).
   * ``print("The switch is pressed!")``: Outputs a message to the console.
   * ``utime.sleep(0.5)``: Adds a delay to debounce the switch and prevent multiple detections from a single press.


**Alternative Wiring: Using Internal Pull-Down Resistor**

If you prefer to simplify the wiring even further, you can rely solely on the internal pull-down resistor:

* Modify the Circuit:

  * Remove the external 10 kΩ resistor and 0.1 µF capacitor.
  * Micro Switch Connections:

    * **Common (C) Terminal**: Connect to GP14 on the Pico.
    * **Normally Open (NO) Terminal**: Connect to 3.3V on the Pico.
    * **Normally Closed (NC) Terminal**: Leave unconnected.

* Modified Code:

  .. code-block:: python

      import machine
      import utime

      # Initialize GP14 as an input pin with an internal pull-down resistor
      switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

      while True:
          if switch.value() == 1:
              print("The switch is pressed!")
              utime.sleep(0.5)  # Debounce delay
    

**Practical Applications**

* **Limit Detection**: Use the micro switch as an end stop in CNC machines or 3D printers to detect the limit of movement.
* **Safety Interlocks**: Ensure a device operates only when certain conditions are met (e.g., a door is closed).
* **User Input**: Incorporate into projects where a robust and reliable button is needed.

**Experimenting Further**

* Control an LED:

  Connect an LED to another GPIO pin (e.g., GP15) with a suitable resistor. Modify the code to turn the LED on when the switch is pressed.
  
  .. code-block:: python
    
    import machine
    import utime

    switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
    led = machine.Pin(15, machine.Pin.OUT)

    while True:
        if switch.value() == 1:
            led.value(1)  # Turn on the LED
            print("The switch is pressed!")
            utime.sleep(0.5)
        else:
            led.value(0)  # Turn off the LED

* Counting Presses:

  Modify the code to count how many times the switch has been pressed.

  * Control an LED:

   .. code-block:: python

      import machine
      import utime

      switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
      count = 0

      while True:
          if switch.value() == 1:
              count += 1
              print("Switch pressed {} times".format(count))
              utime.sleep(0.5)

**Conclusion**

Using a micro switch with the Raspberry Pi Pico 2 W allows you to detect physical interactions reliably. Understanding how to wire the switch and read its state in your code is essential for creating responsive and interactive projects.

