.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ar_neopixel:

3.3 Controlling an RGB LED Strip
===========================================================

In this lesson, we'll learn how to control an **RGB LED strip** (specifically the WS2812 type) using the Raspberry Pi Pico 2 W and MicroPython.

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

    * You can open the file ``3.3_rgb_led_strip.ino`` under the path of ``pico-2w-kit-main/arduino/3.3_rgb_led_strip``. 
    * Or copy this code into **Arduino IDE**.
    * Then select the Raspberry Pi Pico board and the correct port before clicking the Upload button.
    * The ``Adafruit_NeoPixel`` library is used here, you can install it from the **Library Manager**.

      .. image:: img/lib_neopixel.png

.. code-block:: arduino

  #include <Adafruit_NeoPixel.h>

  #define PIXEL_PIN    0    // Digital IO pin connected to the NeoPixels
  #define PIXEL_COUNT  8    // Number of NeoPixels

  // Declare our NeoPixel strip object
  Adafruit_NeoPixel strip(PIXEL_COUNT, PIXEL_PIN, NEO_GRB + NEO_KHZ800);

  void setup() {
    strip.begin();           // Initialize the NeoPixel library
    strip.show();            // Turn OFF all pixels ASAP
  }

  void loop() {
    // Set the color of each pixel
    strip.setPixelColor(0, strip.Color(255, 0, 0));   // Red
    strip.setPixelColor(1, strip.Color(0, 255, 0));   // Green
    strip.setPixelColor(2, strip.Color(0, 0, 255));   // Blue
    strip.setPixelColor(3, strip.Color(255, 255, 0)); // Yellow
    strip.setPixelColor(4, strip.Color(0, 255, 255)); // Cyan
    strip.setPixelColor(5, strip.Color(255, 0, 255)); // Magenta
    strip.setPixelColor(6, strip.Color(255, 255, 255)); // White
    strip.setPixelColor(7, strip.Color(0, 0, 0));     // Off

    strip.show();  // Update the strip with new contents
    delay(1000);   // Wait for a second

    // Turn off all pixels
    strip.clear();
    strip.show();
    delay(1000);   // Wait for a second
  }

After uploading the code, you should see the LEDs light up with different colors, stay on for a second, then turn off for a second.

**Understanding the Code**

#. Include the Library:

   .. code-block:: arduino
    
      #include <Adafruit_NeoPixel.h>

#. Define Constants:

   * ``PIXEL_PIN``: The GPIO pin connected to the data input of the LED strip (GP0).
   * ``PIXEL_COUNT``: The number of LEDs on the strip.

#. Initialize the Strip:

   ``NEO_GRB + NEO_KHZ800``: Specifies the color order and communication speed.

   .. code-block:: arduino
    
      Adafruit_NeoPixel strip(PIXEL_COUNT, PIXEL_PIN, NEO_GRB + NEO_KHZ800);
      
#. In ``setup()`` function:

   * ``strip.begin()``: Initializes the NeoPixel library.
   * ``strip.show()``: Ensures all pixels are off.

#. In ``loop()`` function:

   * ``strip.setPixelColor(index, color)``: Sets the color of a specific pixel.
   * ``strip.Color(r, g, b)``: Creates a 24-bit color value from red, green, and blue components (0-255).
   * ``strip.show()``: Sends the updated color data to the strip.
   * ``strip.clear()``: Clears the pixel data in memory (turns off the pixels on the next ``show()``).

**Advanced Example: Color Wipe Animation**

Let's create a simple animation where each LED lights up in sequence.

* ``colorWipe()``: Lights up each pixel in sequence with the specified color.
* Calls ``colorWipe()`` with different colors to create an animation.

.. code-block:: arduino
    
  #include <Adafruit_NeoPixel.h>

  #define PIXEL_PIN    0
  #define PIXEL_COUNT  8

  Adafruit_NeoPixel strip(PIXEL_COUNT, PIXEL_PIN, NEO_GRB + NEO_KHZ800);

  void setup() {
    strip.begin();
    strip.show(); // Initialize all pixels to 'off'
  }

  void loop() {
    colorWipe(strip.Color(255, 0, 0), 50); // Red
    colorWipe(strip.Color(0, 255, 0), 50); // Green
    colorWipe(strip.Color(0, 0, 255), 50); // Blue
  }

  void colorWipe(uint32_t color, int wait) {
    for(int i=0; i<strip.numPixels(); i++) {
      strip.setPixelColor(i, color);
      strip.show();
      delay(wait);
    }
  }

After uploading the code, you should see the LEDs light up one by one in red, then green, then blue.

**Advanced Example: Rainbow Cycle Animation**

* ``rainbowCycle()`` Function: Cycles through the colors of the rainbow across all pixels.
* The nested loops create a smooth transition of colors.
* ``Wheel()`` Function: Generates rainbow colors across 0-255 positions.

.. code-block:: arduino
    
  #include <Adafruit_NeoPixel.h>

  #define PIXEL_PIN    0
  #define PIXEL_COUNT  8

  Adafruit_NeoPixel strip(PIXEL_COUNT, PIXEL_PIN, NEO_GRB + NEO_KHZ800);

  void setup() {
    strip.begin();
    strip.show(); // Initialize all pixels to 'off'
  }

  void loop() {
    rainbowCycle(20); // Rainbow cycle with 20ms delay per step
  }

  void rainbowCycle(int wait) {
    uint16_t i, j;

    for(j=0; j<256*5; j++) { // 5 cycles of all colors on the wheel
      for(i=0; i< strip.numPixels(); i++) {
        strip.setPixelColor(i, Wheel(((i * 256 / strip.numPixels()) + j) & 255));
      }
      strip.show();
      delay(wait);
    }
  }

  // Input a value 0 to 255 to get a color value.
  // The colors are a transition r - g - b - back to r.
  uint32_t Wheel(byte WheelPos) {
    if(WheelPos < 85) {
      return strip.Color(WheelPos * 3, 255 - WheelPos * 3, 0);
    } else if(WheelPos < 170) {
      WheelPos -= 85;
      return strip.Color(255 - WheelPos * 3, 0, WheelPos * 3);
    } else {
      WheelPos -= 170;
      return strip.Color(0, WheelPos * 3, 255 - WheelPos * 3);
    }
  }

After uploading the code, the LED strip should display a rainbow of colors cycling smoothly.

**Further Exploration**

* Create Custom Animations:

  * Experiment with different colors and animations.
  * Combine multiple animation functions.

* Respond to Sensors:

  Use input from sensors to change the LED colors or patterns.

* Build a Visualizer:

  Create a music visualizer that changes the LEDs based on sound input.

**Power Considerations**

* Current Draw:

  * Each LED can draw up to 60mA at full brightness.
  * For 8 LEDs, that's up to 480mA.
  * Ensure your power source can supply the required current.

* External Power Supply:

  * For larger strips or higher brightness, use an external 5V power supply.
  * Connect the ground of the external power supply to the Pico's ground.

**Conclusion**

In this lesson, you've learned how to control a WS2812 RGB LED strip using the Raspberry Pi Pico and the Adafruit NeoPixel library. By manipulating individual pixels, you can create stunning visual effects for your projects.

