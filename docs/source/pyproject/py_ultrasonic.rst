.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_ultrasonic:

6.1 Measuring Distance
======================================

In this lesson, we'll learn how to use an **ultrasonic sensor module** with the Raspberry Pi Pico 2w to measure the distance to an object. Ultrasonic sensors are commonly used in robotics and automation systems for object detection and distance measurement.

* :ref:`cpn_ultrasonic`

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
        - :ref:`cpn_ultrasonic`
        - 1
        - |link_ultrasonic_buy|

**Understanding the Ultrasonic Sensor**

The ultrasonic sensor works by emitting a short ultrasonic pulse from the **Trig** pin and listening for the echo on the **Echo** pin. By measuring the time it takes for the echo to return, we can calculate the distance to an object using the speed of sound.

|ultrasonic_prin|

* **Trigger Pulse**: A 10-microsecond high pulse on the Trig pin initiates the measurement.
* **Ultrasonic Burst**: The sensor emits an 8-cycle ultrasonic burst at 40 kHz.
* **Echo Reception**: The Echo pin goes high, and stays high until the echo is received back.
* **Time Measurement**: By measuring the time the Echo pin stays high, we can calculate the distance.

**Schematic**

|sch_ultrasonic|

**Wiring**

|wiring_ultrasonic|

**Writing the Code**

Let's write a MicroPython program to measure distance using the ultrasonic sensor.

.. note::

    * Open the ``6.1_measuring_distance.py`` from ``pico-2w-starter-kit-main/micropython`` or copy the code into Thonny, then click "Run" or press F5.
    * Ensure the correct interpreter is selected: MicroPython (Raspberry Pi Pico).COMxx. 
     

.. code-block:: python

    import machine
    import utime

    # Define the pins connected to the sensor
    TRIG = machine.Pin(17, machine.Pin.OUT)
    ECHO = machine.Pin(16, machine.Pin.IN)

    def measure_distance():
        # Ensure the trigger pin is low
        TRIG.low()
        utime.sleep_us(2)
        # Send a 10µs pulse to trigger the measurement
        TRIG.high()
        utime.sleep_us(10)
        TRIG.low()
        
        # Wait for the echo pin to go high (start of echo pulse)
        while ECHO.value() == 0:
            pass
        start_time = utime.ticks_us()
        
        # Wait for the echo pin to go low (end of echo pulse)
        while ECHO.value() == 1:
            pass
        end_time = utime.ticks_us()
        
        # Calculate the duration of the echo pulse
        duration = utime.ticks_diff(end_time, start_time)
        
        # Calculate the distance (speed of sound is 34300 cm/s)
        distance = (duration * 0.0343) / 2
        return distance

    while True:
        dist = measure_distance()
        print("Distance: {:.2f} cm".format(dist))
        utime.sleep(0.5)

Once the code is running, the Thonny Shell should display the distance readings in centimeters. Move an object closer or farther from the sensor to see the readings change.

**Understanding the Code**

#. Import necessary modules and set up the trigger and echo pins:

   .. code-block:: python
   
       import machine
       import utime
   
       TRIG = machine.Pin(17, machine.Pin.OUT)
       ECHO = machine.Pin(16, machine.Pin.IN)


#. Measuring Distance:

   * Sends a trigger pulse to initiate measurement.
   * Waits for the echo response.
   * Calculates the duration of the echo pulse.
   * Computes the distance using the speed of sound.

   .. code-block:: python

       def measure_distance():
           # Ensure trigger is low
           TRIG.low()
           utime.sleep_us(2)
           # Trigger a 10µs pulse
           TRIG.high()
           utime.sleep_us(10)
           TRIG.low()
           
           # Wait for echo to start
           while ECHO.value() == 0:
               pass
           start_time = utime.ticks_us()
           
           # Wait for echo to end
           while ECHO.value() == 1:
               pass
           end_time = utime.ticks_us()
           
           # Calculate duration
           duration = utime.ticks_diff(end_time, start_time)
           # Calculate distance
           distance = (duration * 0.0343) / 2
           return distance


#. Main Loop:

   * Continuously measures and prints the distance.
   * Pauses for half a second between measurements.

   .. code-block:: python
   
       while True:
           dist = measure_distance()
           print("Distance: {:.2f} cm".format(dist))
           utime.sleep(0.5)

**Understanding Limitations**

* Blocking Code:

  * The while loops used to wait for the echo can block other code from running.
  * For more advanced applications, consider using interrupts or asynchronous programming to avoid blocking.

* Measurement Range:

  * The HC-SR04 sensor typically has a range of 2 cm to 400 cm.
  * Objects closer than 2 cm or farther than 400 cm may not be detected accurately.

* Environmental Factors:

  * Temperature and humidity can affect the speed of sound.
  * For precise measurements, adjust the speed of sound based on ambient conditions.

**Conclusion**

You've successfully used an ultrasonic sensor to measure distance with the Raspberry Pi Pico 2w. This fundamental skill is widely applicable in robotics, automation, and interactive projects.