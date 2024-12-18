.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_alarm_lamp:

7.3 Building an Alarm Siren Lamp
=======================================================

In this project, we'll create an **Alarm Siren Lamp** using the Raspberry Pi Pico 2 W. This device simulates the flashing lights and siren sound of a police car or emergency vehicle. It's a fun way to learn about PWM (Pulse Width Modulation), interrupts, and controlling multiple components like LEDs and buzzers.



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
        - |link_passive_buzzer_buy|
    *   - 9
        - :ref:`cpn_capacitor`
        - 1(104)
        - |link_capacitor_buy|
    *   - 10
        - :ref:`cpn_slide_switch`
        - 1
        - 

**Understanding the Components**

* **Passive Buzzer**: Requires an external signal to produce sound. We'll use PWM to generate varying frequencies, creating a siren effect.
* **LED**: Will simulate the flashing light of a siren by changing brightness.
* **Slide Switch**: Acts as an on/off switch to control the alarm.
* **NPN Transistor (S8050)**: Used to drive the buzzer, as the Pico's GPIO pins cannot supply enough current directly.
* **Resistor and Capacitor**: Used to debounce the slide switch, ensuring stable readings.

**Schematic**

|sch_alarm_siren_lamp|

* GP17 is connected to the middle pin of the slider, along with a 10K resistor and a capacitor (filter) in parallel to GND, which allows the slider to output a steady high or low level when toggled to the left or right.
* As soon as GP15 is high, the NPN transistor conducts, causing the passive buzzer to start sounding. This passive buzzer is programmed to gradually increase in frequency to produce a siren sound.
* An LED is connected to GP16 and is programmed to periodically change its brightness in order to simulate a siren.



**Wiring**

|wiring_alarm_siren_lamp|


**Writing the Code**

We'll write a MicroPython script to control the buzzer and LED based on the position of the slide switch.

.. note::

    * Open the ``7.3_alarm_siren_lamp.py`` from ``pico-2 w-kit-main/micropython`` or copy the code into Thonny, then click "Run" or press F5.
    * Ensure the correct interpreter is selected: MicroPython (Raspberry Pi Pico).COMxx. 

.. code-block:: python

    import machine
    import utime

    # Initialize PWM for buzzer and LED
    buzzer = machine.PWM(machine.Pin(15))
    led = machine.PWM(machine.Pin(16))
    led.freq(1000)  # Set LED PWM frequency

    # Initialize the slide switch
    switch = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_DOWN)

    # Function to map values from one range to another
    def interval_mapping(x, in_min, in_max, out_min, out_max):
        # Ensure in_min != in_max to avoid division by zero
        if in_max - in_min == 0:
            return out_min
        return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

    # Main loop
    try:
        while True:
            if switch.value() == 1:
                # Alarm is ON
                # Increase frequency and brightness
                for i in range(0, 100, 2):
                    # Map 'i' to LED brightness and buzzer frequency
                    brightness = interval_mapping(i, 0, 100, 0, 65535)
                    frequency = interval_mapping(i, 0, 100, 500, 2000)
                    
                    # Set LED brightness
                    led.duty_u16(brightness)
                    
                    # Set buzzer frequency and duty cycle
                    buzzer.freq(frequency)
                    buzzer.duty_u16(32768)  # 50% duty cycle
                    
                    utime.sleep(0.01)
                    
                # Decrease frequency and brightness
                for i in range(100, 0, -2):
                    brightness = interval_mapping(i, 0, 100, 0, 65535)
                    frequency = interval_mapping(i, 0, 100, 500, 2000)
                    
                    led.duty_u16(brightness)
                    buzzer.freq(frequency)
                    buzzer.duty_u16(32768)
                    
                    utime.sleep(0.01)
            else:
                # Alarm is OFF
                # Turn off LED and buzzer
                led.duty_u16(0)
                buzzer.duty_u16(0)
                utime.sleep(0.1)
    except KeyboardInterrupt:
        # Clean up
        buzzer.deinit()
        led.deinit()
        print("Program stopped.")

Once the code is running, toggle the slide switch to the ON position.
The buzzer should emit a siren sound, and the LED should flash accordingly.
Toggle the switch to OFF to stop the alarm.

**Understanding the Code**

#. Initialization:

   * **buzzer**: PWM object on GP15.
   * **led**: PWM object on GP16, frequency set to 1kHz for smooth brightness control.
   * **switch**: Input pin on GP17 with an internal pull-down resistor.

#. Interval Mapping Function:

   Maps a value from one range to another, useful for scaling the loop variable to desired frequency and brightness ranges.

   .. code-block:: python

        # Function to map values from one range to another
        def interval_mapping(x, in_min, in_max, out_min, out_max):
            # Ensure in_min != in_max to avoid division by zero
            if in_max - in_min == 0:
                return out_min
            return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

#. Main Loop:

   * Checks the state of the switch.
   * If the switch is ON (``switch.value() == 1``):

     * Runs two loops to simulate the siren effect:
     * Increasing frequency and brightness.
     * Decreasing frequency and brightness.
     * The buzzer frequency varies between 500 Hz and 2000 Hz.
     * The LED brightness varies from off to full brightness and back.

     .. code-block:: python

        if switch.value() == 1:
            # Alarm is ON
            # Increase frequency and brightness
            for i in range(0, 100, 2):
                # Map 'i' to LED brightness and buzzer frequency
                brightness = interval_mapping(i, 0, 100, 0, 65535)
            ...
                
                utime.sleep(0.01)

   * If the switch is OFF: Turns off the LED and buzzer.

     .. code-block:: python

            else:
                # Alarm is OFF
                # Turn off LED and buzzer
                led.duty_u16(0)
                buzzer.duty_u16(0)
                utime.sleep(0.1)

   * Exception Handling: Captures a keyboard interrupt (Ctrl+C) to cleanly deinitialize the PWM objects.

     .. code-block:: python
    
        except KeyboardInterrupt:
            # Clean up
            buzzer.deinit()
            led.deinit()
            print("Program stopped.")

**Experimenting Further**

* Adjusting the Siren Effect:

  * Modify the frequency range in the ``interval_mapping`` function to change the pitch.
  * Adjust the delay in the loops (``utime.sleep(0.01)``) to speed up or slow down the siren cycle.

* Add More LEDs:

  * Incorporate additional LEDs of different colors to create a more dynamic light show.
  * Use multiple GPIO pins and PWM channels.

* Motion Activation:

  Replace the slide switch with a motion sensor (e.g., PIR sensor) to trigger the alarm when movement is detected.

* Remote Control:

  Integrate an IR receiver to control the alarm using a remote control.


**Conclusion**

You've successfully built an Alarm Siren Lamp using the Raspberry Pi Pico 2 W! This project demonstrates how to control multiple components and create interactive effects. It's a great foundation for more complex projects like security systems, emergency signals, or creative art installations.