.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ar_led:



2.1 - Hello, LED! 
=======================================

Welcome to your first hardware project with the Raspberry Pi Pico 2w! In this lesson, we'll learn how to make an LED blink using MicroPython. This simple project is a great way to get started with physical computing and understand how to control hardware with code.


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

By setting the GPIO pin high or low, you're controlling the voltage output of that pin. When the pin is high, current flows through the LED (limited by the resistor), causing it to light up. When the pin is low, no current flows, and the LED turns off.

**Wiring**

|wiring_led|


**Writing the Code**

.. note::

    * You can open the file ``2.1_hello_led.ino`` under the path of ``pico-2w-starter-kit-main/arduino/2.1_hello_led``. 
    * Or copy this code into **Arduino IDE**.
    * Don't forget to select the board(Raspberry Pi Pico) and the correct port before clicking the **Upload** button.



.. code-block:: Arduino

    const int ledPin = 15;  // GPIO pin connected to the LED

    void setup() {
      pinMode(ledPin, OUTPUT);  // Initialize the GPIO pin as an output
    }

    void loop() {
      digitalWrite(ledPin, HIGH);  // Turn the LED on
      delay(1000);                 // Wait for 1 second
      digitalWrite(ledPin, LOW);   // Turn the LED off
      delay(1000);                 // Wait for 1 second
    }

After uploading the code, you should see the LED turn on for 1 second and turn off for 1 second.

**Understanding the Code**

#. Variable Declaration:

   Declare a constant integer ``ledPin`` and assign it the value 15, which corresponds to GPIO pin 15 where the LED is connected.

   .. code-block:: Arduino

        const int ledPin = 15;

#. Setup Function:

   The ``setup()`` function runs once when the board is powered on or reset. Here, we initialize ``ledPin`` as an output pin using ``pinMode()``.

   .. code-block:: Arduino

        void setup() {
          pinMode(ledPin, OUTPUT);
        }

#. Loop Function:

   * The ``loop()`` function runs repeatedly after ``setup()``.
   * Use ``digitalWrite()`` to set the voltage of ``ledPin``. Setting it to ``HIGH`` provides 3.3V, turning the LED on. Setting it to ``LOW`` drops the voltage to 0V, turning the LED off. 
   * The ``delay(1000)`` function creates a 1-second pause between the on and off states.

   .. code-block:: Arduino

        void loop() {
          digitalWrite(ledPin, HIGH);
          delay(1000);
          digitalWrite(ledPin, LOW);
          delay(1000);
        }

**Additional Tips**

* **Understanding the Resistor**: The 220Ω resistor limits the current flowing through the LED, preventing it from burning out.
* **Polarity Matters**: Ensure the LED is connected correctly. The longer leg is the positive anode and should be connected to the resistor leading to the GPIO pin.
* **Experiment**: Try changing the ``delay(1000)`` values to make the LED blink faster or slower.

**Conclusion**

Congratulations! You've built your first hardware project with the Raspberry Pi Pico 2w. This simple LED blinking project is a fundamental step into the world of physical computing. From here, you can explore more complex projects by adding buttons, sensors, and other components.
