.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ar_fade:

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


* :ref:`cpn_led`

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
        - 1(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|

**Schematic**

|sch_led|


**Wiring**


|wiring_led|


**Writing the Code**


.. note::

    * You can open the file ``2.3_fading_led.ino`` under the path of ``pico-2w-kit-main/arduino/2.3_fading_led``. 
    * Or copy this code into **Arduino IDE**.
    * Don't forget to select the board(Raspberry Pi Pico) and the correct port before clicking the **Upload** button.



.. code-block:: Arduino

    const int ledPin = 15; // GPIO pin connected to the LED

    void setup() {
      pinMode(ledPin, OUTPUT); // Initialize the GPIO pin as an output
    }

    void loop() {
      // Increase brightness
      for (int value = 0; value <= 255; value += 5) {
        analogWrite(ledPin, value); // Set the brightness
        delay(30);                  // Wait for 30 milliseconds
      }
      // Decrease brightness
      for (int value = 255; value >= 0; value -= 5) {
        analogWrite(ledPin, value);
        delay(30);
      }
    }

After uploading the code, you should see the LED gradually increase in brightness and then fade, creating a smooth pulsing effect.

**Understanding the Code**

#. Declaring the LED Pin:
   
   Declare a constant integer ``ledPin`` and assign it the value 15, which corresponds to GPIO pin 15 where the LED is connected.

   .. code-block:: Arduino

        const int ledPin = 15;


#. Setting Up the Pin:
   
   The ``setup()`` function runs once when the board powers up. We initialize ``ledPin`` as an output using ``pinMode()``.

   .. code-block:: Arduino

        void setup() {
          pinMode(ledPin, OUTPUT);
        }


#. The Loop Function:
   
    The ``loop()`` function runs repeatedly. It contains two ``for`` loops:

     * Increasing Brightness: Starts with ``value = 0`` and increases by 5 until it reaches 255.
     * Decreasing Brightness: Starts with value = 255 and decreases by 5 down to 0.
     
   * The ``analogWrite()`` function writes a PWM signal to the specified pin. The value ranges from 0 (always off) to 255 (always on), allowing for 256 levels of brightness.
   * Adding ``delay(30);`` slows down the loop, so the change in brightness is gradual and visible to the human eye.

   .. code-block:: Arduino

        void loop() {
          // Increase brightness
          for (int value = 0; value <= 255; value += 5) {
            analogWrite(ledPin, value);
            delay(30);
          }
          // Decrease brightness
          for (int value = 255; value >= 0; value -= 5) {
            analogWrite(ledPin, value);
            delay(30);
          }
        }


**Additional Tips**

* **Experiment**: Try changing the value increments or the delay duration to see how it affects the fading speed.
* **Understanding PWM Limitations**: While all GPIO pins on the Pico support PWM, pins sharing the same PWM slice cannot have different frequencies but can have different duty cycles.
* **Safety First**: Always use a resistor with the LED to prevent it from drawing too much current and burning out.

**Conclusion**

You've successfully created a fading LED effect using PWM on the Raspberry Pi Pico 2 W. This project demonstrates how PWM can be used to simulate analog behavior with digital signals, a fundamental concept in electronics and programming microcontrollers.
