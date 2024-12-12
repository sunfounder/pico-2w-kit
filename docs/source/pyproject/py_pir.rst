.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_pir:

2.10 Detect Human Movement
========================================
In this lesson, we'll learn how to use a Passive Infrared (PIR) sensor with the Raspberry Pi Pico 2w to detect human movement. PIR sensors are commonly used in security systems, automatic lighting, and other applications where motion detection is required. They detect infrared radiation emitted by warm objects, such as humans or animals, in their field of view.

:ref:`cpn_pir`

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
        - :ref:`cpn_pir`
        - 1
        - |link_pir_buy|


**Schematic**

|sch_pir|

When the PIR module detects someone passing by, GP14 will be high, otherwise it will be low.

.. note::

    The PIR sensor have two potentiometers:

    * **Sensitivity Adjustment**: Controls the range of detection.
    * **Time Delay Adjustment**: Controls how long the output remains HIGH after motion is detected.

    For initial testing, turn both potentiometers counterclockwise to their minimum positions. This sets the sensor to its most sensitive and shortest delay settings, allowing you to observe immediate responses.

    |img_PIR_TTE|

**Wiring**

|wiring_pir|

**Writing the Code**

We'll write a MicroPython program that uses an interrupt to detect motion and prints a message when motion is detected.

.. note::

    * Open the ``2.10_detect_human_movement.py`` from ``pico-2w-kit-main/micropython`` or copy the code into Thonny, then click "Run" or press F5.

    * Ensure the correct interpreter is selected: MicroPython (Raspberry Pi Pico).COMxx. 

    

.. code-block:: python

    import machine
    import utime

    # Initialize GP14 as an input pin
    pir_sensor = machine.Pin(14, machine.Pin.IN)

    def motion_detected(pin):
        print("Motion detected!")

    # Set up an interrupt on the rising edge
    pir_sensor.irq(trigger=machine.Pin.IRQ_RISING, handler=motion_detected)

    # Main loop does nothing, interrupt handles motion detection
    while True:
        utime.sleep(1)

When the code is running, you will observe the following phenomenon:

* Move in front of the PIR sensor.
* When motion is detected, "Motion detected!" should appear in the console.

**Understanding the Code**

#. Import Modules:

   * ``import machine``: Access to hardware functions.
   * ``import utime``: Time-related functions.

#. Initialize the PIR Sensor Pin:

   * ``pir_sensor = machine.Pin(14, machine.Pin.IN)``: Sets up GP14 as an input pin.

#. Define the Interrupt Handler:

   * ``def motion_detected(pin)``: Function that gets called when motion is detected.
   * ``print("Motion detected!")``: Prints a message to the console.

#. Set Up the Interrupt:

   * ``pir_sensor.irq(trigger=machine.Pin.IRQ_RISING, handler=motion_detected)``: Configures an interrupt that triggers on the rising edge of the signal from the PIR sensor.

#. Main Loop:

   * ``while True``: An infinite loop.
   * ``utime.sleep(1)``: The loop sleeps for 1 second in each iteration. The main loop doesn't need to do anything because the interrupt handles the motion detection.

**Example Code for Measuring Duration**

You can modify the code to measure the duration of motion detection and the intervals between detections.

.. code-block:: python

    import machine
    import utime

    pir_sensor = machine.Pin(14, machine.Pin.IN)

    last_trigger_time = utime.ticks_ms()

    def pir_triggered(pin):
        global last_trigger_time
        current_time = utime.ticks_ms()
        duration = utime.ticks_diff(current_time, last_trigger_time)
        last_trigger_time = current_time

        if pir_sensor.value():
            print("Motion detected! Duration since last detection: {} ms".format(duration))
        else:
            print("Motion ended. Duration of motion: {} ms".format(duration))

    # Set up interrupts for both rising and falling edges
    pir_sensor.irq(trigger=machine.Pin.IRQ_RISING | machine.Pin.IRQ_FALLING, handler=pir_triggered)

    while True:
        utime.sleep(1)

* Interrupts for Both Edges: set up the interrupt to trigger on both rising and falling edges using ``machine.Pin.IRQ_RISING`` | ``machine.Pin.IRQ_FALLING``.
* Tracking Time:

  * Use ``utime.ticks_ms()`` to get the current time in milliseconds.
  * Calculate the duration between triggers to measure how long the PIR sensor output remains ``HIGH`` or ``LOW``.

**Practical Applications**

* **Security Systems**: Detect intruders or unauthorized movement.
* **Automatic Lighting**: Turn lights on when motion is detected.
* **Energy Saving**: Power down devices when no movement is detected for a period.

**Troubleshooting Tips**

* False Triggers:

  * PIR sensors can be sensitive to environmental factors like temperature changes or sunlight.
  * Avoid pointing the sensor directly at heat sources or windows.

* Sensor Not Detecting Motion:

  * Ensure the sensor has had time to initialize (some sensors require up to 60 seconds).
  * Adjust the sensitivity potentiometer.

* Interference: 

  * Keep the sensor away from electronics that may cause electromagnetic interference.

**Conclusion**

By integrating a PIR sensor with the Raspberry Pi Pico 2w, you've added motion detection capabilities to your projects. Understanding how to read sensor inputs and handle interrupts allows you to create responsive and efficient programs.


