.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_fade:

2.3 Fading LED
========================

In this lesson, we'll learn how to control the brightness of an LED using Pulse Width Modulation (PWM) on the Raspberry Pi Pico 2 W. This is a fundamental technique in electronics that allows us to control devices like LEDs and motors with varying intensities.

**What is PWM?**

**Pulse Width Modulation (PWM)** is a method of controlling the amount of power delivered to an electronic device by cycling the power on and off at a high frequency. The "width" of the pulse (the duration it stays on) determines how much power the device receives.

|img_pwm_duty_cycle|

* **Duty Cycle**: The percentage of one period in which a signal is active. A 100% duty cycle means the signal is always on, and 0% means it's always off.
* **Frequency**: How often the signal cycles on and off per second.

By adjusting the duty cycle, we can simulate analog output using digital signals. For example, if we rapidly turn an LED on and off, our eyes perceive varying brightness levels depending on how long the LED stays on during each cycle.

**Why Use PWM?**

* **LED Brightness Control**: Smoothly adjust the brightness of LEDs.
* **Motor Speed Control**: Control the speed of DC motors.
* **Efficiency**: PWM is more efficient than using variable resistors because it reduces energy loss in the form of heat.

**Understanding PWM on the Raspberry Pi Pico 2 W**

The Raspberry Pi Pico 2 W has PWM capabilities on all its GPIO pins, but it actually has 8 PWM slices (from PWM0 to PWM7), each with two channels (A and B), giving a total of 16 independent PWM outputs.

|pin_pwm|

.. note::
     Pins sharing the same PWM slice (like GP0 and GP16) cannot have different frequencies but can have different duty cycles.


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

**Circuit Diagram**

|sch_led|

**Wiring Diagram**

|wiring_led|


**Writing the Code**


.. note::

  * Open the ``2.3_fading_led.py`` from ``pico-2 w-kit-main/micropython`` or copy the code into Thonny, then click "Run" or press F5.
  
  * Ensure the correct interpreter is selected: MicroPython (Raspberry Pi Pico).COMxx. 
  


.. code-block:: python

    import machine
    import utime

    # Set up PWM on pin GP15
    led = machine.PWM(machine.Pin(15))
    led.freq(1000)  # Set frequency to 1000Hz

    # Gradually increase brightness
    for duty in range(0, 65536, 64):
        led.duty_u16(duty)  # Set duty cycle (16-bit value)
        utime.sleep(0.01)   # Wait 10ms

    # Turn off the LED
    led.duty_u16(0)


When the code is running, the LED connected to pin GP15 will gradually increase in brightness from off to full brightness.


**Understanding the Code**

* Import Libraries:

  * ``machine``: Provides access to the hardware components.
  * ``utime``: Allows us to add delays.

* Set Up PWM:

  * ``machine.PWM(machine.Pin(15))``: Initializes PWM on GP15.
  * ``led.freq(1000)``: Sets the PWM frequency to 1000Hz (1ms per cycle).

* Adjust Duty Cycle:

  * ``for duty in range(0, 65536, 64)``: Loops from 0 to 65535 in steps of 64.
  * ``led.duty_u16(duty)``: Sets the duty cycle. The ``duty_u16`` function accepts a 16-bit value (0 to 65535), where 0 is 0% and 65535 is 100% duty cycle.
  * ``utime.sleep(0.01)``: Adds a small delay so the change in brightness is perceptible.

* Turn Off the LED:

  * ``led.duty_u16(0)``: Sets the duty cycle to 0%, turning off the LED.


**Experimenting Further**

* **Fade In and Out**: Modify the code to make the LED fade in and then fade out.
* **Change Speed**: Adjust the ``utime.sleep()`` value to change how quickly the brightness changes.
* **Different Frequencies**: Try different PWM frequencies using ``led.freq()`` to see how it affects the LED.

**Conclusion**

PWM is a powerful technique for controlling devices that require analog-like inputs using digital outputs. Understanding PWM opens up possibilities for more complex projects like motor control, audio signal generation, and more.

By mastering the basics of PWM on the Raspberry Pi Pico 2 W, you're well on your way to creating more advanced electronics projects.

**References**

* |link_mpython_pwm|