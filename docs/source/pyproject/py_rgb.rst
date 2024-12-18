.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_rgb:


2.4 Colorful Light
==============================================

In this lesson, we'll explore how to create various colors using an RGB LED and the Raspberry Pi Pico 2 W. By adjusting the intensity of the red, green, and blue components, we can mix light to produce a wide range of colors. This concept is based on the additive method of color mixing.

**What is Additive Color Mixing?**

Additive color mixing involves combining different colors of light to produce new colors. When red, green, and blue light are combined in various intensities, they can create any color in the visible spectrum. For example:

* **Red + Green = Yellow**
* **Red + Blue = Magenta**
* **Green + Blue = Cyan**
* **Red + Green + Blue = White**

|img_rgb_mix|

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
        - 3(1-330Ω, 2-220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_rgb`
        - 1
        - |link_rgb_led_buy|

**Schematic**

|sch_rgb|

The PWM pins GP13, GP14 and GP15 control the Red, Green and Blue pins of the RGB LED respectively, and connect the common cathode pin to GND. This allows the RGB LED to display a specific color by superimposing light on these pins with different PWM values.


**Wiring Diagram**

|img_rgb_pin|

The RGB LED has 4 pins: the long pin is the common cathode pin, which is usually connected to GND; the left pin next to the longest pin is Red; and the two pins on the right are Green and Blue.

We use a higher resistance for the red LED because it is typically brighter than the green and blue LEDs at the same current.


|wiring_rgb|



**Writing the Code**

We'll write a MicroPython program that controls the intensity of each color using Pulse Width Modulation (PWM) to produce different colors.

.. note::

    * Open the ``2.4_colorful_light.py`` from ``pico-2 w-kit-main/micropython`` or copy the code into Thonny, then click "Run" or press F5.
    * Ensure the correct interpreter is selected: MicroPython (Raspberry Pi Pico).COMxx. 
    

.. code-block:: python

    import machine
    import utime

    # Initialize PWM for red, green, and blue pins
    red = machine.PWM(machine.Pin(13))
    green = machine.PWM(machine.Pin(14))
    blue = machine.PWM(machine.Pin(15))

    # Set the PWM frequency
    red.freq(1000)
    green.freq(1000)
    blue.freq(1000)

    def map_value(x, in_min, in_max, out_min, out_max):
        # Map a value from one range to another
        return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

    def set_color(r, g, b):
        # Set the color by adjusting duty cycles
        red.duty_u16(map_value(r, 0, 255, 0, 65535))
        green.duty_u16(map_value(g, 0, 255, 0, 65535))
        blue.duty_u16(map_value(b, 0, 255, 0, 65535))

    # Example: Set the color to orange
    set_color(255, 165, 0)

When the code is running, the RGB LED will emit an orange light.

**Understanding the Code**

#. Import Libraries:

   * ``machine``: To access hardware-specific functions.
   * ``utime``: For time-related functions (not used in this example but useful for animations).

#. Initialize PWM Objects:

   * Create PWM objects for the red, green, and blue pins connected to the RGB LED and set the PWM frequency to 1000 Hz for all colors.

   .. code-block:: python

        # Initialize PWM for red, green, and blue pins
        red = machine.PWM(machine.Pin(13))
        green = machine.PWM(machine.Pin(14))
        blue = machine.PWM(machine.Pin(15))

        # Set the PWM frequency
        red.freq(1000)
        green.freq(1000)
        blue.freq(1000)

#. Define ``map_value`` Function:

   * Since the ``duty_u16`` method accepts values from 0 to 65535, but color values are typically in the range 0 to 255, we need to map the 0-255 range to 0-65535.
   * The ``map_value`` function scales the input value accordingly.

   .. code-block:: python

        def map_value(x, in_min, in_max, out_min, out_max):
            # Map a value from one range to another
            return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

#. Define ``set_color`` Function:

   This function takes RGB values (each from 0 to 255) and sets the duty cycle for each color channel after mapping.

   .. code-block:: python

        def set_color(r, g, b):
            # Set the color by adjusting duty cycles
            red.duty_u16(map_value(r, 0, 255, 0, 65535))
            green.duty_u16(map_value(g, 0, 255, 0, 65535))
            blue.duty_u16(map_value(b, 0, 255, 0, 65535))
    
#. Set the Desired Color:

   Call ``set_color(255, 165, 0)`` to set the RGB LED to orange. You can change the values to any RGB color you like.

**Example: Color Cycling**

Let's enhance the code to cycle through different colors.

#. To find the RGB values for different colors, you can use any graphic software or an online color picker. For example:

   * Red: (255, 0, 0)
   * Green: (0, 255, 0)
   * Blue: (0, 0, 255)
   * White: (255, 255, 255)
   * Purple: (128, 0, 128)

#. Write the code.

   We define a list of RGB tuples representing different colors.
   The ``while True`` loop cycles through each color, sets the RGB LED to that color, and waits for 1 second before moving to the next color.

   .. code-block:: python
   
       import machine
       import utime
   
       # Initialize PWM for red, green, and blue pins
       red = machine.PWM(machine.Pin(13))
       green = machine.PWM(machine.Pin(14))
       blue = machine.PWM(machine.Pin(15))
   
       # Set the PWM frequency
       red.freq(1000)
       green.freq(1000)
       blue.freq(1000)
   
       def map_value(x, in_min, in_max, out_min, out_max):
           return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
   
       def set_color(r, g, b):
           red.duty_u16(map_value(r, 0, 255, 0, 65535))
           green.duty_u16(map_value(g, 0, 255, 0, 65535))
           blue.duty_u16(map_value(b, 0, 255, 0, 65535))
   
       # List of colors to cycle through
       colors = [
           (255, 0, 0),     # Red
           (0, 255, 0),     # Green
           (0, 0, 255),     # Blue
           (255, 255, 0),   # Yellow
           (0, 255, 255),   # Cyan
           (255, 0, 255),   # Magenta
           (255, 255, 255)  # White
       ]
   
       while True:
           for color in colors:
               set_color(*color)
               utime.sleep(1)

When this code is running, the RGB LED will cycle through a sequence of colors: red, green, blue, yellow, cyan, magenta, and white.

Each color will be displayed for 1 second before transitioning to the next one in the list.

**Conclusion**

By controlling the intensity of the red, green, and blue components of an RGB LED using PWM, we can create a vast array of colors. This project demonstrates the principles of additive color mixing and provides a foundation for creating colorful light displays with microcontrollers.


**References**

* |link_mpython_pwm|
