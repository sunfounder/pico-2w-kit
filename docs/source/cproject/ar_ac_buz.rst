.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ar_ac_buz:

3.1 Make the Buzzer Beep!
==========================

In this lesson, we will learn how to make a **buzzer** beep using the Raspberry Pi Pico 2w. A buzzer is a digital output device, just like an LED, and it's very simple to control. We'll use an **active buzzer** for this project, which generates sound when it receives a signal.

**What is an Active Buzzer?**

An **active buzzer** has an internal oscillator that makes it easier to use. You only need to send a signal to the buzzer to make it beep—no complex frequency control is required. This is different from a **passive buzzer**, which requires an external signal to generate sound.

|img_buzzer|

* :ref:`cpn_buzzer`

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
        - :ref:`cpn_transistor`
        - 1(S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_resistor`
        - 1(1KΩ)
        - |link_resistor_buy|
    *   - 7
        - Active :ref:`cpn_buzzer`
        - 1
        - 

**Schematic**

|sch_buzzer|

In this circuit, the buzzer is powered through a transistor (**S8050** NPN). The transistor amplifies the current, making the buzzer sound louder than if it were connected directly to the Pico. 

Here's what happens:
* **GP15** outputs a high signal to control the transistor.
* When the transistor is activated, it allows current to flow through the buzzer, making it beep.

A **1kΩ resistor** is used to limit the current to protect the transistor.

**Wiring**

Make sure you are using the **active buzzer**. You can tell it's the correct one by looking for the sealed back (as opposed to the exposed PCB, which is a passive buzzer).

|img_buzzer|

|wiring_beep|


**Writing the Code**


.. note::

    * You can open the file ``3.1_beep.ino`` under the path of ``pico-2w-starter-kit-main/arduino/3.1_beep``. 
    * Or copy this code into **Arduino IDE**.
    * Don't forget to select the board(Raspberry Pi Pico) and the correct port before clicking the **Upload** button.


.. code-block:: Arduino

    const int buzzerPin = 15;  // GPIO pin connected to the transistor base

    void setup() {
      pinMode(buzzerPin, OUTPUT);
    }

    void loop() {
      digitalWrite(buzzerPin, HIGH);  // Turn the buzzer on
      delay(1000);                    // Wait for 1 second
      digitalWrite(buzzerPin, LOW);   // Turn the buzzer off
      delay(1000);                    // Wait for 1 second
    }

After uploading the code:
The buzzer should beep for 1 second, then stay silent for 1 second, and repeat this pattern continuously.
If you do not hear the buzzer, check the wiring to ensure all connections are correct.
Make sure you are using an active buzzer.

**Understanding the Code**

#. Defining the Buzzer Pin:

   Assigns buzzerPin to GPIO 15, which controls the transistor and thus the buzzer.

   .. code-block:: Arduino

        const int buzzerPin = 15;  // GPIO pin connected to the transistor base

#. Setting Up the Pin Mode:

   Configures buzzerPin as an output.

   .. code-block:: Arduino

        void setup() {
          pinMode(buzzerPin, OUTPUT);
        }

#. Controlling the Buzzer: The ``loop()`` function repeats this process indefinitely, making the buzzer beep every second.


   * ``digitalWrite(buzzerPin, HIGH)``: Sets ``buzzerPin`` ``HIGH``, turning on the transistor, which allows current to flow through the buzzer, making it beep.
   * ``delay(1000)``: Pauses the program for 1000 milliseconds (1 second).
   * ``digitalWrite(buzzerPin, LOW)``: Sets ``buzzerPin`` ``LOW``, turning off the transistor, stopping the current flow, and silencing the buzzer.

   .. code-block:: Arduino

        void loop() {
          digitalWrite(buzzerPin, HIGH);  // Turn the buzzer on
          delay(1000);                    // Wait for 1 second
          digitalWrite(buzzerPin, LOW);   // Turn the buzzer off
          delay(1000);                    // Wait for 1 second
        }


**Further Exploration**

* Varying the Beep Duration:

  * Modify the ``delay()`` values to change how long the buzzer stays on and off.
  * Experiment with shorter or longer durations.

* Creating Patterns:

  * Create more complex patterns by adjusting the timing in the ``loop()`` function.
  * For example, create an SOS signal in Morse code.

* Using a Passive Buzzer:

  * Try using a passive buzzer and the ``tone()`` function to generate different frequencies.
  * Note that the wiring and code will be different for a passive buzzer.

**Conclusion**

In this lesson, you've learned how to make an active buzzer beep using the Raspberry Pi Pico and a transistor. By controlling the transistor with a GPIO pin, you can safely switch the buzzer on and off without overloading the Pico's GPIO pins. This basic concept can be expanded upon to create more complex sounds or to use buzzers in alarms, notifications, and interactive projects.

