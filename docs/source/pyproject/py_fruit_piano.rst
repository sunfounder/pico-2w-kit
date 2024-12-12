.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_fruit_piano:

7.9 Building a Fruit Piano
=================================================

In this project, we'll create a **Fruit Piano** using the Raspberry Pi Pico 2w, an MPR121 capacitive touch sensor, a buzzer, and an RGB LED. By connecting fruits (or any conductive objects) to the capacitive touch sensor, we'll transform them into piano keys that play musical notes and display colorful lights when touched.

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
        - :ref:`cpn_transistor`
        - 1(S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_resistor`
        - 4(1-1KΩ, 1-330Ω, 2-220Ω)
        - |link_resistor_buy|
    *   - 7
        - Passive :ref:`cpn_buzzer`
        - 1
        - |link_passive_buzzer_buy|
    *   - 8
        - :ref:`cpn_rgb`
        - 1
        - |link_rgb_led_buy|
    *   - 9
        - :ref:`cpn_mpr121`
        - 1
        - 

**Understanding the Components**

*  **MPR121 Capacitive Touch Sensor**: A capacitive touch sensor controller that can handle up to 12 touch inputs. It detects changes in capacitance caused by touching connected electrodes.
*  **Passive Buzzer**: An electronic component that produces sound when driven with a PWM signal. We'll use it to play different musical notes.
*  **RGB LED**: An LED that combines red, green, and blue LEDs into one package. By adjusting the intensity of each color, we can produce a wide range of colors.
*  **Fruits or Conductive Objects**: Items like fruits, metal objects, or even water can act as conductive touch inputs when connected to the MPR121.

**Schematic**

|sch_fruit_piano| 

To turn the fruit into a piano key, you still need to connect the electrodes on the MPR121 to the fruit (e.g. into the banana handle).

In the beginning, MPR121 will initialize and each electrode will get a value based on the current charge; when a conductor (such as a human body) touches an electrode, the charge will shift and rebalance.
As a result, the electrode's value is different from its initial value, telling the main control board that it has been touched.
During this process, ensure that the wiring of each electrode is stable so that its charge is balanced when initializing.


**Wiring**


|wiring_fruit_piano| 


**Writing the Code**

We'll write a MicroPython script that:

* Initializes the MPR121 touch sensor.
* Detects touch inputs from the connected fruits.
* Plays corresponding musical notes on the buzzer.
* Lights up the RGB LED with random colors.

.. note::

    * Open the ``7.9_fruit_piano.py`` from ``pico-2w-starter-kit-main/micropython`` or copy the code into Thonny, then click "Run" or press F5.
    * Ensure the correct interpreter is selected: MicroPython (Raspberry Pi Pico).COMxx. 
    * Here you need to use the library called ``mpr121.py``, please check if it has been uploaded to Pico, for a detailed tutorial refer to :ref:`add_libraries_py`.

.. code-block:: python

    from mpr121 import MPR121
    from machine import Pin, I2C, PWM
    import time
    import urandom

    # Initialize I2C connection for MPR121 capacitive touch sensor
    i2c = I2C(1, sda=Pin(6), scl=Pin(7))
    mpr = MPR121(i2c)

    # Define note frequencies (in Hertz)
    NOTE_FREQUENCIES = [
        220,  # A3
        247,  # B3
        262,  # C4
        294,  # D4
        330,  # E4
        349,  # F4
        392,  # G4
        440,  # A4
        494,  # B4
        523,  # C5
        587,  # D5
        659   # E5
    ]

    # Initialize PWM for buzzer on GP15
    buzzer = PWM(Pin(15))

    # Initialize PWM for RGB LED on GP13 (Red), GP12 (Green), GP11 (Blue)
    red = PWM(Pin(13))
    green = PWM(Pin(12))
    blue = PWM(Pin(11))

    # Set PWM frequency for LEDs
    red.freq(1000)
    green.freq(1000)
    blue.freq(1000)

    # Function to play a tone
    def play_tone(frequency):
        if frequency == 0:
            buzzer.duty_u16(0)
        else:
            buzzer.freq(frequency)
            buzzer.duty_u16(32768)  # 50% duty cycle

    # Function to stop the tone
    def stop_tone():
        buzzer.duty_u16(0)

    # Function to set a random color on the RGB LED
    def set_random_color():
        red.duty_u16(urandom.getrandbits(16))
        green.duty_u16(urandom.getrandbits(16))
        blue.duty_u16(urandom.getrandbits(16))

    # Function to turn off the RGB LED
    def turn_off_led():
        red.duty_u16(0)
        green.duty_u16(0)
        blue.duty_u16(0)

    # Main loop
    try:
        last_touched = mpr.touched()
        while True:
            current_touched = mpr.touched()
            for i in range(12):
                pin_bit = 1 << i
                if current_touched & pin_bit and not last_touched & pin_bit:
                    # Electrode i was just touched
                    print("Pin {} touched".format(i))
                    play_tone(NOTE_FREQUENCIES[i])
                    set_random_color()
                if not current_touched & pin_bit and last_touched & pin_bit:
                    # Electrode i was just released
                    print("Pin {} released".format(i))
                    stop_tone()
                    turn_off_led()
            last_touched = current_touched
            time.sleep(0.01)
    except KeyboardInterrupt:
        pass
    finally:
        stop_tone()
        turn_off_led()


.. note::
    
    Do not touch the fruits or conductive objects before running the program to ensure proper initialization.

After the program starts, gently touch the fruits.

* The buzzer will play the corresponding musical note.
* The RGB LED will light up with a random color.
* Experiment by touching different fruits to play different notes.

**Understanding the Code**

#. Initialization:

   * **I2C Connection**: Sets up communication with the MPR121 sensor.
   * **PWM Setup**: Initializes PWM for the buzzer and RGB LED pins.

#. Note Frequencies:

   A list of frequencies corresponding to musical notes (A3 to E5).

#. Functions:

   * ``play_tone(frequency)``: Starts playing a tone at the specified frequency.
   * ``stop_tone()``: Stops the buzzer.
   * ``set_random_color()``: Sets the RGB LED to a random color.
   * ``turn_off_led()``: Turns off the RGB LED.

#. Main Loop:

   * **Touch Detection**: Continuously checks for touch events on the electrodes.
   * **Touch Handling**:

     * When an electrode is touched, plays the corresponding note and lights up the RGB LED.
     * When an electrode is released, stops the tone and turns off the LED.

   * **Debouncing**: A short delay (``time.sleep(0.01)``) to prevent bouncing issues.

#. Exception Handling:

   * Uses a try block to allow for graceful exit on a keyboard interrupt.
   * Ensures that the buzzer and LED are turned off in the finally block.


**Troubleshooting**

* No Sound or Lights:

  * Check all wiring connections.
  * Ensure that the MPR121 is properly connected to the Pico.
  * Verify that the fruits are connected securely to the electrodes.
  * Ensure that ``mpr121.py`` is correctly uploaded to the Pico.

* Touch Not Detected:

  * Make sure you're not touching multiple electrodes simultaneously.
  * Avoid touching the wires directly; touch the fruits or conductive objects.
  * Ensure that the fruits are not too dry; moist fruits conduct better.

* Unstable Behavior:

  * Ensure that the Pico and sensor are not exposed to static electricity.
  * Keep the wires and connections stable to maintain consistent capacitance readings.

**Experimenting Further**

* Expand the Instrument:

  * Use different conductive materials (e.g., water, metal objects) to act as keys.
  * Increase the number of notes by mapping more frequencies to the electrodes.

* Visual Effects:

  * Modify the ``set_random_color()`` function to create specific color patterns.
  * Add more LEDs to enhance the visual experience.

* Adjust Sensitivity:

  Experiment with the MPR121's touch threshold settings to adjust sensitivity.

* Combine with Other Sensors:

  Integrate other sensors (e.g., light sensors) to modify the sound or light effects based on environmental conditions.

**Conclusion**

You've successfully built a Fruit Piano using the Raspberry Pi Pico 2w! This project demonstrates how capacitive touch sensing can be combined with sound and light to create interactive experiences. It's a fun way to explore the principles of conductivity, touch sensing, and creative coding.

Feel free to expand upon this project by adding new features, experimenting with different materials, or integrating additional components.
