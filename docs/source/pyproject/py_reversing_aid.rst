

.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_reversing_aid:

7.10 Building a Reversing Aid
=================================

In this project, we'll create a **Reversing Aid System** using the Raspberry Pi Pico 2 W, an ultrasonic sensor, an LED, and a buzzer. 
This system simulates how real-world parking sensors work by detecting the distance to an obstacle and providing audio and visual 
feedback that changes based on proximity. You can attach this setup to a remote-controlled car to mimic the experience of reversing into a garage.


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
        - 2(1KΩ, 220Ω)
        - |link_resistor_buy|
    *   - 7
        - Active :ref:`cpn_buzzer`
        - 1
        -
    *   - 8
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 9
        - :ref:`cpn_ultrasonic`
        - 1
        - |link_ultrasonic_buy|

**Understanding the Components**

* **Ultrasonic Sensor (HC-SR04):** Measures the distance to an object by sending out ultrasonic waves and measuring the time it takes for the echo to return.
* **Buzzer:** Provides audio feedback; beeps more frequently as the object gets closer.
* **LED:** Provides visual feedback; blinks more rapidly as the object gets closer.

**Schematic**

|sch_reversing_aid|


**Wiring**

|wiring_reversing_aid| 

**Writing the Code**

We'll write a MicroPython script that:

* Measures the distance using the ultrasonic sensor.
* Adjusts the beep frequency of the buzzer and the blink rate of the LED based on the distance.
* Provides continuous feedback as the object moves closer or further away.

.. note::

    * Open the ``7.10_reversing_aid.py`` from ``pico-2 w-kit-main/micropython`` or copy the code into Thonny, then click "Run" or press F5.

    * Ensure the correct interpreter is selected: MicroPython (Raspberry Pi Pico).COMxx. 

.. code-block:: python

    import machine
    import utime

    # Set up pins
    trigger = machine.Pin(17, machine.Pin.OUT)
    echo = machine.Pin(16, machine.Pin.IN)
    buzzer = machine.Pin(15, machine.Pin.OUT)
    led = machine.Pin(14, machine.Pin.OUT)

    # Function to measure distance
    def measure_distance():
        # Ensure trigger is low
        trigger.low()
        utime.sleep_us(2)
        # Send 10us pulse to trigger
        trigger.high()
        utime.sleep_us(10)
        trigger.low()

        # Measure the duration of the echo pulse
        while echo.value() == 0:
            signaloff = utime.ticks_us()
        while echo.value() == 1:
            signalon = utime.ticks_us()

        timepassed = utime.ticks_diff(signalon, signaloff)
        distance = (timepassed * 0.0343) / 2  # Convert to cm
        return distance

    # Function to control buzzer and LED
    def alert(interval):
        buzzer.high()
        led.high()
        utime.sleep(0.1)
        buzzer.low()
        led.low()
        utime.sleep(interval)

    # Main loop
    try:
        while True:
            dist = measure_distance()
            print("Distance: {:.2f} cm".format(dist))
            if dist < 0:
                print("Out of range")
                utime.sleep(1)
            elif dist <= 10:
                alert(0.2)  # Very close, alert rapidly
            elif dist <= 20:
                alert(0.5)  # Close, alert moderately
            elif dist <= 50:
                alert(1)    # Not too close, alert slowly
            else:
                alert(2)    # Far away, alert infrequently
    except KeyboardInterrupt:
        print("Measurement stopped by User")

Once the code is running, place an object at varying distances from the ultrasonic sensor.
Observe the changes in the beep frequency and LED blink rate.
The console will display the measured distance.

**Understanding the Code**

#. Distance Measurement:

   * The ``measure_distance()`` function sends a 10-microsecond pulse to the TRIG pin.
   * It then measures the time until the ECHO pin goes high and then back low.
   * Calculates the distance based on the time it takes for the ultrasonic pulse to return.

   .. code-block:: python

        def measure_distance():
            # Ensure trigger is low
            trigger.low()
            utime.sleep_us(2)
            # Send 10us pulse to trigger
            trigger.high()
            utime.sleep_us(10)
            trigger.low()

            # Measure the duration of the echo pulse
            while echo.value() == 0:
                signaloff = utime.ticks_us()
            while echo.value() == 1:
                signalon = utime.ticks_us()

            timepassed = utime.ticks_diff(signalon, signaloff)
            distance = (timepassed * 0.0343) / 2  # Convert to cm
            return distance


#. Alert Function:

   * The ``alert(interval)`` function turns the buzzer and LED on for 0.1 seconds and then off.
   * The interval parameter adjusts the pause between alerts based on the distance.

   .. code-block:: python

        def measure_distance():
            # Ensure trigger is low
            trigger.low()
            utime.sleep_us(2)
            # Send 10us pulse to trigger
            trigger.high()
            utime.sleep_us(10)
            trigger.low()

            # Measure the duration of the echo pulse
            while echo.value() == 0:
                signaloff = utime.ticks_us()
            while echo.value() == 1:
                signalon = utime.ticks_us()

            timepassed = utime.ticks_diff(signalon, signaloff)
            distance = (timepassed * 0.0343) / 2  # Convert to cm
            return distance

#. Main Loop:

   * Continuously measures the distance.
   * Adjusts the alert frequency according to predefined distance thresholds.

   .. code-block:: python

        try:
            while True:
                dist = measure_distance()
                print("Distance: {:.2f} cm".format(dist))
                if dist < 0:
                    print("Out of range")
                    utime.sleep(1)
                elif dist <= 10:
                    alert(0.2)  # Very close, alert rapidly
                elif dist <= 20:
                    alert(0.5)  # Close, alert moderately
                elif dist <= 50:
                    alert(1)    # Not too close, alert slowly
                else:
                    alert(2)    # Far away, alert infrequently
        except KeyboardInterrupt:
            print("Measurement stopped by User")
        
**Safety Considerations**

* Voltage Levels:

  * Be cautious with the ECHO pin voltage from the ultrasonic sensor if using 5V.
  * Use a voltage divider or level shifter to protect the Pico's GPIO pins.

* Power Supply:

  Ensure the power supply can handle the current requirements of all components.

**Experimenting Further**

* Visual Display:

  Add an LCD or OLED display to show the distance visually.

* Multiple Sensors:

  Use additional ultrasonic sensors to cover more directions.

* Advanced Alerts:

  Implement different tones or patterns on the buzzer for different distances.

**Conclusion**

You've successfully built a Reversing Aid System using the Raspberry Pi Pico 2 W! This project demonstrates how sensors can be used to provide real-time feedback, a fundamental concept in robotics and automation.



