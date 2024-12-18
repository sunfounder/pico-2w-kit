.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_neopixel:

3.3 RGB LED Strip
======================

In this lesson, we'll learn how to control an **RGB LED strip** (specifically the WS2812 type) 
using the Raspberry Pi Pico 2 W and MicroPython.

The WS2812 is a smart LED that integrates a control circuit and an RGB chip into a 5050-sized LED package. Each LED has its own built-in controller, which allows us to control each LED individually using a single data line. This means we can change the color and brightness of each LED on the strip independently.


* :ref:`cpn_ws2812`

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
        - :ref:`cpn_ws2812`
        - 1
        - |link_ws2812_buy|


**Schematic**

|sch_ws2812|


**Wiring**


|wiring_ws2812|

Be cautious with the current draw. While the Pico's VBUS pin can supply power for a small number of LEDs (like 8), using more LEDs may require an external power supply to prevent overloading the Pico.


    

**Writing the Code**

.. note::

    * Open the ``3.3_rgb_led_strip.py`` from ``pico-2 w-kit-main/micropython`` or copy the code into Thonny, then click "Run" or press F5.

    * Ensure the correct interpreter is selected: MicroPython (Raspberry Pi Pico).COMxx. 

    * Here you need to use the library called ``ws2812.py``, please check if it has been uploaded to Pico, for a detailed tutorial refer to :ref:`add_libraries_py`.


.. code-block:: python

    import machine
    from ws2812 import WS2812

    # Initialize the LED strip
    led_strip = WS2812(machine.Pin(0), 8)  # Using GP0, 8 LEDs

    # Set colors for each LED
    led_strip[0] = [255, 0, 0]     # Red
    led_strip[1] = [0, 255, 0]     # Green
    led_strip[2] = [0, 0, 255]     # Blue
    led_strip[3] = [255, 255, 0]   # Yellow
    led_strip[4] = [0, 255, 255]   # Cyan
    led_strip[5] = [255, 0, 255]   # Magenta
    led_strip[6] = [255, 255, 255] # White
    led_strip[7] = [128, 128, 128] # Gray

    # Update the LED strip to show the colors
    led_strip.write()

When this code is running, the WS2812 LED strip connected to pin GP0 with 8 LEDs will display the following colors:

* **LED 0**: Red (255, 0, 0)
* **LED 1**: Green (0, 255, 0)
* **LED 2**: Blue (0, 0, 255)
* **LED 3**: Yellow (255, 255, 0)
* **LED 4**: Cyan (0, 255, 255)
* **LED 5**: Magenta (255, 0, 255)
* **LED 6**: White (255, 255, 255)
* **LED 7**: Gray (128, 128, 128)

**Understanding the Code**

#. Import Libraries:

   * ``machine``: Provides access to hardware-related functions.
   * ``WS2812``: The library to control the WS2812 LED strip.

#. Initialize the LED Strip:

   * ``led_strip = WS2812(machine.Pin(0), 8)``: Initializes the LED strip connected to pin GP0 with 8 LEDs.

#. Set Colors:

   * ``led_strip[0] = [255, 0, 0]``: Assigns a color to each LED using RGB values (Red, Green, Blue), ranging from 0 to 255.

#. Update the LED Strip:

   * ``led_strip.write()``: Sends the color data to the LED strip to display the colors.

**Let's Make a Flowing Rainbow Effect!**

Now, we'll create a colorful flowing light effect by randomly generating colors and shifting them along the strip.

.. code-block:: python

    import machine
    from ws2812 import WS2812
    import utime
    import urandom

    # Number of LEDs in the strip
    NUM_LEDS = 8

    # Initialize the LED strip with 8 LEDs
    led_strip = WS2812(machine.Pin(0), NUM_LEDS)

    def flowing_light():
        # Shift colors along the strip
        for i in range(NUM_LEDS - 1, 0, -1):
            led_strip[i] = led_strip[i - 1]
        # Generate a random color for the first LED
        led_strip[0] = [urandom.getrandbits(8), urandom.getrandbits(8), urandom.getrandbits(8)]
        # Update the strip
        led_strip.write()
        # Small delay for smooth animation
        utime.sleep_ms(100)

    # Main loop
    while True:
        flowing_light()


When the code runs, the LED strip displays a flowing dynamic effect with random colors, where a new random color is introduced at the beginning and shifts towards the end with each cycle.

**Understanding the Code**

#. Random Color Generation: Generates a random RGB color where each component ranges from 0 to 255.

   .. code-block:: python

        [urandom.getrandbits(8), urandom.getrandbits(8), urandom.getrandbits(8)]

#. Shifting Colors: Moves each LED's color to the next position, creating a flowing effect.

   .. code-block:: python

        for i in range(NUM_LEDS - 1, 0, -1):
            led_strip[i] = led_strip[i - 1]

#. Infinite Loop: Continuously updates the LED strip to keep the animation running.

   .. code-block:: python

        while True:
            flowing_light()

**Experimenting Further**

* **Adjusting Speed**: Modify ``utime.sleep_ms(100)`` to make the flowing effect faster or slower.
* **More LEDs**: If you have a longer strip, change the number in ``WS2812(machine.Pin(0), number_of_leds)`` accordingly.
* **Custom Animations**: Experiment with different patterns and color combinations to create your own animations.

**Conclusion**

You've successfully learned how to control an RGB LED strip using the Raspberry Pi Pico 2 W and MicroPython! This opens up a world of possibilities for creating stunning light displays, mood lighting, or even interactive art projects.



