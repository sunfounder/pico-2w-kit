.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ar_rgb:


2.4 Colorful Light
====================

In this lesson, we'll explore how to create various colors using an RGB LED and the Raspberry Pi Pico 2 W. By adjusting the intensity of the red, green, and blue components, we can mix light to produce a wide range of colors. This concept is based on the additive method of color mixing.

**What is Additive Color Mixing?**

Additive color mixing involves combining different colors of light to produce new colors. When red, green, and blue light are combined in various intensities, they can create any color in the visible spectrum. For example:

* **Red + Green = Yellow**
* **Red + Blue = Magenta**
* **Green + Blue = Cyan**
* **Red + Green + Blue = White**

|img_rgb_mix|

* :ref:`cpn_rgb`

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
        - 3(1-330Ω, 2-220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_rgb`
        - 1
        - |link_rgb_led_buy|

**Schematic**

|sch_rgb|

The PWM pins GP13, GP14 and GP15 control the Red, Green and Blue pins of the RGB LED respectively, and connect the common cathode pin to GND. This allows the RGB LED to display a specific color by superimposing light on these pins with different PWM values.



**Wiring**

|img_rgb_pin|

The RGB LED has 4 pins: the long pin is the common cathode pin, which is usually connected to GND; the left pin next to the longest pin is Red; and the two pins on the right are Green and Blue.

We use a higher resistance for the red LED because it is typically brighter than the green and blue LEDs at the same current.


|wiring_rgb|


**Writing the Code**

Here, we can choose our favorite color in drawing software (such as paint) and display it with RGB LED.

.. note::

    * You can open the file ``2.4_colorful_light.ino`` under the path of ``pico-2 w-kit-main/arduino/2.4_colorful_light``. 
    * Or copy this code into **Arduino IDE**.
    * Don't forget to select the board(Raspberry Pi Pico) and the correct port before clicking the **Upload** button.




.. code-block:: Arduino

   // Define the GPIO pins connected to the RGB LED
   const int redPin = 13;   // Red pin
   const int greenPin = 14; // Green pin
   const int bluePin = 15;  // Blue pin

   void setup() {
     // Initialize each RGB LED pin as an output
     pinMode(redPin, OUTPUT);
     pinMode(greenPin, OUTPUT);
     pinMode(bluePin, OUTPUT);
   }

   // Function to set the color
   void setColor(unsigned char red, unsigned char green, unsigned char blue) {
     analogWrite(redPin, red);
     analogWrite(greenPin, green);
     analogWrite(bluePin, blue);
   }

   void loop() {
     // Red color
     setColor(255, 0, 0);
     delay(1000);

     // Green color
     setColor(0, 255, 0);
     delay(1000);

     // Blue color
     setColor(0, 0, 255);
     delay(1000);

     // Yellow color (Red + Green)
     setColor(255, 255, 0);
     delay(1000);

     // Cyan color (Green + Blue)
     setColor(0, 255, 255);
     delay(1000);

     // Magenta color (Red + Blue)
     setColor(255, 0, 255);
     delay(1000);

     // White color (Red + Green + Blue)
     setColor(255, 255, 255);
     delay(1000);

     // Turn off
     setColor(0, 0, 0);
     delay(1000);
   }

After uploading the code, the RGB LED should cycle through red, green, blue, yellow, cyan, magenta, white, and then turn off, with each color displayed for one second.

**Understanding the Code**

#. Defining the Pins:

   Assign the GPIO pins connected to the RGB LED components.

   .. code-block:: Arduino

        const int redPin = 13;
        const int greenPin = 14;
        const int bluePin = 15;

#. Initializing the Pins:

   Set the RGB LED pins as outputs.

   .. code-block:: Arduino

        void setup() {
          pinMode(redPin, OUTPUT);
          pinMode(greenPin, OUTPUT);
          pinMode(bluePin, OUTPUT);
        }

#. Setting the Color:

   The ``setColor`` function uses PWM (Pulse Width Modulation) to adjust the brightness of each color component.

   .. code-block:: Arduino

        void setColor(unsigned char red, unsigned char green, unsigned char blue) {
          analogWrite(redPin, red);
          analogWrite(greenPin, green);
          analogWrite(bluePin, blue);
        }

#. Looping Through Colors:

   In the ``loop()`` function, we call ``setColor()`` with different values to display various colors, each followed by a 1-second delay.


   .. code-block:: Arduino

        void loop() {
          // Red color
          setColor(255, 0, 0);
          delay(1000);
          ...

          // Turn off
          setColor(0, 0, 0);
          delay(1000);
        }


**Experimenting with Colors**

You can create your own colors by adjusting the values passed to ``setColor()``. The values range from 0 (off) to 255 (full brightness). For example:

* Orange: setColor(255, 165, 0);
* Purple: setColor(128, 0, 128);

To find RGB values for specific colors, you can use a color picker tool or software like **Paint**.

**Conclusion**

In this lesson, you've learned how to control an RGB LED using the Raspberry Pi Pico and how to create various colors by mixing red, green, and blue light. This knowledge is fundamental for projects involving LED displays, mood lights, or any application requiring color control.

