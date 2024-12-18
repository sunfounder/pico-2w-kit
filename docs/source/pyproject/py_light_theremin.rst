.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_light_theremin:

7.1 Creating a Light Theremin
====================================================

In this exciting project, we'll build a **Light Theremin** using a Raspberry Pi Pico 2 W, a photoresistor, and a passive buzzer. A theremin is a unique musical instrument that is played without physical contact, producing different tones based on the position of the player's hands. While we can't replicate a traditional theremin entirely, we can simulate its functionality by using light intensity to control sound frequency.

* `Theremin - Wikipedia <https://en.wikipedia.org/wiki/Theremin>`_

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
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 6
        - :ref:`cpn_transistor`
        - 1(S8050)
        - |link_transistor_buy|
    *   - 7
        - :ref:`cpn_resistor`
        - 3(1KΩ, 220Ω, 10KΩ)
        - |link_resistor_buy|
    *   - 8
        - Passive :ref:`cpn_buzzer`
        - 1
        - 
    *   - 9
        - :ref:`cpn_photoresistor`
        - 1
        - |link_photoresistor_buy|

**Understanding the Concept**

* **Photoresistor:** A sensor that changes its resistance based on light intensity. More light decreases resistance, less light increases it.
* **Passive Buzzer:** Requires an external signal to produce sound. We can control its frequency using Pulse Width Modulation (PWM).
* **Transistor (S8050):** Used to amplify the current, allowing the buzzer to be driven effectively by the Pico.

By reading the values from the photoresistor, we can map light intensity to sound frequency. This means moving your hand over the photoresistor will change the pitch of the sound produced by the buzzer, similar to playing a theremin.

**Schematic**

|sch_light_theremin|

Before starting the project, wave your hand up and down over the photoresistor to calibrate the range of light intensity. The LED connected in GP16 is used to indicate the debugging time, and the LED is lit to indicate the start of debugging and off to indicate the end of debugging.

When GP15 outputs high level, S8050 (NPN transistor) conducts and the passive buzzer starts to sound.

When the light is stronger, GP28's value is smaller; vice versa, it is larger when the light is weaker.
By programming the value of the photoresistor to affect the frequency of the passive buzzer, a photosensitive device can be simulated.

**Wiring**

|wiring_light_theremin|

**Writing the Code**

Let's write a MicroPython program that reads the light intensity from the photoresistor, maps it to a frequency, and plays that frequency on the buzzer.

.. note::

    * Open the ``7.1_light_theremin.py`` from ``pico-2 w-kit-main/micropython`` or copy the code into Thonny, then click "Run" or press F5.
    * Ensure the correct interpreter is selected: MicroPython (Raspberry Pi Pico).COMxx. 


.. code-block:: python

    import machine
    import utime

    # Initialize components
    led = machine.Pin(16, machine.Pin.OUT)  # LED on GP16
    photoresistor = machine.ADC(28)         # Photoresistor connected to ADC0 (GP28)
    buzzer = machine.PWM(machine.Pin(15))   # Buzzer connected to GP15

    # Variables for calibration
    light_low = 65535
    light_high = 0

    # Function to map values from one range to another
    def interval_mapping(x, in_min, in_max, out_min, out_max):
        # Ensure in_min != in_max to avoid division by zero
        if in_max - in_min == 0:
            return out_min
        return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

    # Function to play a tone on the buzzer
    def play_tone(pin, frequency):
        if frequency <= 0:
            pin.duty_u16(0)
        else:
            pin.freq(frequency)
            pin.duty_u16(32768)  # 50% duty cycle

    # Calibration process
    def calibrate():
        global light_low, light_high
        print("Calibrating... Move your hand over the sensor.")
        led.value(1)  # Turn on LED to indicate calibration
        start_time = utime.ticks_ms()
        while utime.ticks_diff(utime.ticks_ms(), start_time) < 5000:  # 5 seconds calibration
            light_value = photoresistor.read_u16()
            if light_value > light_high:
                light_high = light_value
            if light_value < light_low:
                light_low = light_value
            utime.sleep_ms(10)
        led.value(0)  # Turn off LED after calibration
        print("Calibration complete.")
        print("Light Low:", light_low)
        print("Light High:", light_high)

    # Main function
    def main():
        calibrate()
        try:
            while True:
                light_value = photoresistor.read_u16()
                # Map the light value to a frequency range (e.g., 200 Hz to 2000 Hz)
                frequency = interval_mapping(light_value, light_low, light_high, 200, 2000)
                play_tone(buzzer, frequency)
                utime.sleep_ms(20)
        except KeyboardInterrupt:
            buzzer.deinit()
            print("Program stopped.")

    # Run the main function
    if __name__ == "__main__":
        main()

When the code is running, the LED will light up, indicating the calibration period.

* Calibration:

  * Move your hand over the photoresistor during the 5-second calibration.
  * This helps the program understand the range of light conditions.

* Playing the Theremin:

  * After calibration, the LED turns off.
  * Move your hand over the photoresistor.
  * The buzzer will emit tones that change pitch based on the light intensity.
  * Experiment with different hand positions and movements to create sounds.


**Understanding the Code**

#. Initialization:

   * **LED Indicator**: Used to signal when calibration is happening.
   * **Photoresistor**: Reads analog values corresponding to light intensity.
   * **Buzzer**: Controlled using PWM to generate tones at different frequencies.

#. Calibration Function (``calibrate()``):

   * Runs for 5 seconds, during which it records the minimum and maximum light values.
   * Instructs the user to move their hand over the sensor to capture the range.
   * Uses the LED as a visual indicator.

   .. code-block:: python

        # Calibration process
        def calibrate():
            global light_low, light_high
            print("Calibrating... Move your hand over the sensor.")
            led.value(1)  # Turn on LED to indicate calibration
            start_time = utime.ticks_ms()
            while utime.ticks_diff(utime.ticks_ms(), start_time) < 5000:  # 5 seconds calibration
                light_value = photoresistor.read_u16()
                if light_value > light_high:
                    light_high = light_value
                if light_value < light_low:
                    light_low = light_value
                utime.sleep_ms(10)
            led.value(0)  # Turn off LED after calibration
            print("Calibration complete.")
            print("Light Low:", light_low)
            print("Light High:", light_high)


#. Interval Mapping Function (``interval_mapping()``):

   * Maps the light sensor values to a frequency range suitable for the buzzer.
   * Prevents division by zero errors.

   .. code-block:: python

        # Function to map values from one range to another
        def interval_mapping(x, in_min, in_max, out_min, out_max):
            # Ensure in_min != in_max to avoid division by zero
            if in_max - in_min == 0:
                return out_min
            return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

#. Playing Tones (``play_tone()``):

   * Sets the frequency of the buzzer using PWM.
   * If the frequency is zero or negative, turns off the buzzer.

   .. code-block:: python

        # Function to play a tone on the buzzer
        def play_tone(pin, frequency):
            if frequency <= 0:
                pin.duty_u16(0)
            else:
                pin.freq(frequency)
                pin.duty_u16(32768)  # 50% duty cycle

#. Main Loop:

   * Continuously reads the light value from the photoresistor.
   * Maps this value to a frequency.
   * Plays the tone corresponding to the frequency.
   * Includes error handling to clean up on exit.

   .. code-block:: python

        # Main function
        def main():
            calibrate()
            try:
                while True:
                    light_value = photoresistor.read_u16()
                    # Map the light value to a frequency range (e.g., 200 Hz to 2000 Hz)
                    frequency = interval_mapping(light_value, light_low, light_high, 200, 2000)
                    play_tone(buzzer, frequency)
                    utime.sleep_ms(20)
            except KeyboardInterrupt:
                buzzer.deinit()
                print("Program stopped.")

**Experimenting Further**

* Adjust Frequency Range:

  Modify the values in ``interval_mapping()`` to change the pitch range. Example: Change 200, 2000 to 100, 5000 for a wider range.

* Visual Feedback:

  Use additional LEDs to provide visual cues corresponding to the pitch.

* Add a Second Sensor:

  Introduce another photoresistor to control volume or another parameter.

* Create a Musical Instrument:

  Combine with other sensors or inputs to build a more complex instrument.

**Understanding Limitations**

* Ambient Light:

  Changes in ambient light can affect performance. Ensure consistent lighting or recalibrate as needed.

* Sensor Sensitivity:

  The photoresistor may not respond quickly to rapid hand movements.

* Sound Quality:

  Passive buzzers have limited sound quality. For better audio, consider using an active speaker with a DAC output.

**Conclusion**

You've successfully created a Light Theremin using the Raspberry Pi Pico 2 W! This project demonstrates how sensors and actuators can be combined to create interactive and fun experiments. Keep exploring and modifying the project to enhance your understanding and creativity.

