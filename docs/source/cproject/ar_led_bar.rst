.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ar_led_bar:

2.2 - Display the Level
=============================

In this lesson, we'll learn how to control an LED Bar Graph using the Raspberry Pi Pico 2 W. An LED Bar Graph consists of 10 LEDs arranged in a line, typically used to display levels such as volume, signal strength, or other measurements. We'll light up the LEDs sequentially to create a level display effect.

|img_led_bar_pin|

* :ref:`cpn_led_bar`

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
        - 10(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led_bar`
        - 1
        - 

**Schematic**

|sch_ledbar|

The LED Bar Graph contains 10 LEDs, each of which is individually controllable. Here, the anode of each of the 10 LEDs is connected to GP6~GP15, and the cathode is connected to a 220ohm resistor, and then to GND.


**Wiring**

|wiring_ledbar|

**Writing the Code**

.. note::

    * You can open the file ``2.2_display_the_level.ino`` under the path of ``pico-2w-kit-main/arduino/2.2_display_the_level``. 
    * Or copy this code into **Arduino IDE**.
    * Don't forget to select the board(Raspberry Pi Pico) and the correct port before clicking the **Upload** button.



.. code-block:: Arduino

    // Define the GPIO pins connected to the LED Bar Graph
    const int ledPins[] = {6, 7, 8, 9, 10, 11, 12, 13, 14, 15};

    void setup() {
      // Initialize each pin as an output
      for (int i = 0; i < 10; i++) {
        pinMode(ledPins[i], OUTPUT);
      }
    }

    void loop() {
      // Turn on LEDs sequentially
      for (int i = 0; i < 10; i++) {
        digitalWrite(ledPins[i], HIGH); // Turn on LED
        delay(500);                     // Wait 500 milliseconds
        digitalWrite(ledPins[i], LOW);  // Turn off LED
        delay(500);                     // Wait 500 milliseconds
      }
    }    

After uploading the code, the LEDs on the bar graph should light up one after another, creating a level display effect. Each LED turns on for half a second and then turns off before the next one lights up.

**Understanding the Code**

#. Defining the LED Pins:

   Create an array ``ledPins`` that holds the GPIO pin numbers connected to each LED on the bar graph.

   .. code-block:: Arduino

      const int ledPins[] = {6, 7, 8, 9, 10, 11, 12, 13, 14, 15};

#. Initializing the Pins:

   In the ``setup()`` function, we set each pin in the ``ledPins`` array as an output.

   .. code-block:: Arduino

      void setup() {
        for (int i = 0; i < 10; i++) {
          pinMode(ledPins[i], OUTPUT);
        }
      }

#. Controlling the LEDs:

   In the ``loop()`` function, we use a ``for`` loop to iterate through each LED. We turn it on, wait for 500 milliseconds, turn it off, and then wait another 500 milliseconds before moving to the next LED.

   .. code-block:: Arduino

      void loop() {
        for (int i = 0; i < 10; i++) {
          digitalWrite(ledPins[i], HIGH);
          delay(500);
          digitalWrite(ledPins[i], LOW);
          delay(500);
        }
      }

**Experimenting Further**

* **Reverse the Order**: Modify the code to light up the LEDs in reverse order.

* **Create a Bounce Effect**: After reaching the last LED, make the sequence reverse back to the first LED.

  .. code-block:: Arduino
    
      void loop() {
        // Ascending sequence
        for (int i = 0; i < 10; i++) {
          digitalWrite(ledPins[i], HIGH);
          delay(200);
          digitalWrite(ledPins[i], LOW);
        }
        // Descending sequence
        for (int i = 8; i >= 0; i--) {
          digitalWrite(ledPins[i], HIGH);
          delay(200);
          digitalWrite(ledPins[i], LOW);
        }
      }

* **Adjust the Speed**: Change the delay times to make the LEDs light up faster or slower.

**Conclusion**

In this lesson, you've learned how to control multiple LEDs using the Raspberry Pi Pico and how to create visual effects using simple programming constructs like loops and delays. This foundational knowledge is essential for more advanced projects involving LED displays and indicators.