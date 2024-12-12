.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_tilt:


2.6 Tilt It！
==========================

|img_tilt|

In this lesson, we'll learn how to use a tilt switch with the Raspberry Pi Pico 2w to detect changes in orientation. A tilt switch is a simple device that can sense whether it is upright or tilted, making it useful for applications like motion detection, orientation sensing, or as a trigger based on position.

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
        - :ref:`cpn_tilt`
        - 1
        - 

**Circuit Diagram**

|sch_tilt|

* **When Upright (Switch Closed)**:

  * The tilt switch connects **3.3V** directly to **GP14**.
  * The GPIO pin reads **HIGH** (1).

* **When Tilted (Switch Open)**:

  * The tilt switch disconnects **3.3V** from **GP14**.
  * The pull-down resistor pulls **GP14** to **GND**.
  * The GPIO pin reads **LOW** (0).

* :ref:`cpn_tilt`

**Wiring**

|wiring_tilt|



**Writing the Code**

We'll write a simple MicroPython program that detects the state of the tilt switch and prints a message when the switch is tilted.

.. note::

    * Open the ``2.6_tilt_switch.py`` from ``pico-2w-starter-kit-main/micropython`` or copy the code into Thonny, then click "Run" or press F5.
    * Ensure the correct interpreter is selected: MicroPython (Raspberry Pi Pico).COMxx. 
    

.. code-block:: python

    import machine
    import utime

    # Initialize GP14 as an input pin
    tilt_switch = machine.Pin(14, machine.Pin.IN)

    while True:
        if tilt_switch.value() == 0:
            print("Tilt detected!")
            utime.sleep(1)  # Delay to avoid multiple rapid detections

When the code is running, you will observe the following phenomenon:

* Keep the tilt switch upright; no message should appear. 
* Tilt the breadboard or switch; "Tilt detected!" should appear in the console.

**Understanding the Code**

#. Import Modules:

   * ``import machine``: Gives us access to the hardware components.
   * ``import utime``: Allows us to use time-related functions.

#. Initialize the Tilt Switch Pin:

   * ``tilt_switch = machine.Pin(14, machine.Pin.IN)``: Sets up GP14 as an input pin.

#. Main Loop:

   * ``while True``: Creates an infinite loop to continuously check the tilt switch state.
   * ``if tilt_switch.value() == 0``: Checks if the GPIO pin reads LOW (0), indicating the switch is tilted.
   * ``print("Tilt detected!")``: Outputs a message when the tilt is detected.
   * ``utime.sleep(1)``: Adds a 1-second delay to debounce the switch and prevent multiple detections.

**Alternative Wiring: Using Internal Pull-Down Resistor**

The Raspberry Pi Pico 2w allows us to enable internal pull-up or pull-down resistors, eliminating the need for an external resistor.

.. code-block:: python

    import machine
    import utime

    # Initialize GP14 as an input pin with internal pull-down resistor
    tilt_switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

    while True:
        if tilt_switch.value() == 1:
            print("Tilt detected!")
            utime.sleep(1)

By enabling the internal pull-down resistor (``machine.Pin.PULL_DOWN``), the GPIO pin defaults to LOW when no voltage is applied.
When the tilt switch is upright (closed), it connects 3.3V to GP14, and the pin reads HIGH (1).

**Practical Applications**

* **Orientation Detection**: Determine if a device is upright or tilted.
* **Motion-Triggered Events**: Activate alarms, notifications, or actions when movement is detected.
* **Interactive Projects**: Use as an input to control games or installations that respond to tilting.

**Experimenting Further**

* Add an LED Indicator:

Connect an LED to another GPIO pin (e.g., GP15) with a suitable resistor. Modify the code to light up the LED when a tilt is detected.

.. code-block:: python

    import machine
    import utime

    tilt_switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
    led = machine.Pin(15, machine.Pin.OUT)

    while True:
        if tilt_switch.value() == 1:
            print("Tilt detected!")
            led.value(1)  # Turn on the LED
            utime.sleep(1)
        else:
            led.value(0)  # Turn off the LED

* Use with Other Sensors:

  Combine the tilt switch with other sensors like buttons or light sensors for more complex interactions.

**Conclusion**

By incorporating a tilt switch into your Raspberry Pi Pico 2w projects, you can add a new dimension of interactivity based on orientation and movement. Understanding how to read digital inputs from sensors like the tilt switch expands your ability to create dynamic and responsive electronics.
