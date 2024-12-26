.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_led:

2.1 Hello, LED! 
=======================================

Welcome to your first hardware project with the Raspberry Pi Pico ! In this lesson, we'll learn how to make an LED blink using MicroPython. This simple project is a great way to get started with physical computing and understand how to control hardware with code.

* :ref:`cpn_led`

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
        - 1(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|


**Schematic**

|sch_led|

By setting the GPIO pin high or low, you're controlling the voltage output of that pin. When the pin is high, current flows through the LED (limited by the resistor), causing it to light up. When the pin is low, no current flows, and the LED turns off.

**Wiring Diagram**

|wiring_led|

**Writing the Code**

.. note::

    * Open the ``2.1_hello_led.py`` file under the path of ``pico-2w-kit-main/micropython`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.

    * Ensure the correct interpreter is selected: MicroPython (Raspberry Pi Pico).COMxx. 

    * For detailed tutorials, please refer to :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime
    
    led = machine.Pin(15, machine.Pin.OUT)
    while True:
        led.value(1)      # Turn the LED on
        utime.sleep(2)    # Wait for 2 second
        led.value(0)      # Turn the LED off
        utime.sleep(2)    # Wait for 2 second

When the code is running, the LED is turn on for 2 second and turn off for 2 second.



**Understanding the Code**

#. Importing Libraries:

   * ``machine``: Provides access to the hardware components.
   * ``utime``: Allows us to use time-related functions like delays.

#. Setting Up the LED Pin:

   * ``led = machine.Pin(15, machine.Pin.OUT)``: Initializes GP15 as an output pin and assigns it to the variable ``led``.


#. Creating an Infinite Loop:

   * ``while True``: Starts an endless loop to continuously run the code inside it.

#. Controlling the LED:

   * ``led.value(1)``: Sets the pin output to high (3.3V), turning the LED on.
   * ``utime.sleep(2)``: Pauses the program for 2 second.
   * ``led.value(0)``: Sets the pin output to low (0V), turning the LED off.
   * ``utime.sleep(2)``: Pauses the program for another 2 second.

**Experimenting Further**

* **Change Blink Rate**: Modify the ``utime.sleep(1)`` values to make the LED blink faster or slower.
* **Use Different Pins**: Try connecting the LED to a different GPIO pin and update the code accordingly.
* **Multiple LEDs**: Add more LEDs to different pins and control them in your code.

**Troubleshooting**

* LED Not Lighting Up:

  * Check the orientation of the LED. Ensure the anode and cathode are connected correctly.
  * Verify all connections are secure.
  * Ensure the resistor is connected in series with the LED.

* Error Messages in Thonny:

  * Make sure you have selected the correct interpreter.
  * Check for typos in your code.

**Conclusion**

Congratulations! You've successfully made an LED blink using the Raspberry Pi Pico  and MicroPython. This foundational project introduces you to controlling hardware with code, setting the stage for more complex projects.


**References**

* |link_mpython_machine_pin|
* |link_mpython_machine|
* |link_mpython_utime|
* |link_python_while|