.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_motor:

3.5 Controlling a Small Fan (DC Motor)
=========================================


In this lesson, we'll learn how to control a **DC motor** (like a small fan) using the 
Raspberry Pi Pico 2 W and an **TA6586 motor driver**. The TA6586 allows us to control the 
direction of the motor rotation—both clockwise and counterclockwise. 
Since the DC motor requires a relatively large current, for safety reasons, 
here we use a power module to supply power to the motor.

* :ref:`cpn_motor`
* :ref:`cpn_ta6586`
* :ref:`cpn_power_module`

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
        - :ref:`cpn_ta6586`
        - 1
        - 
    *   - 6
        - :ref:`cpn_motor`
        - 1
        - |link_motor_buy| 
    *   - 7
        - :ref:`cpn_lipo_charger`
        - 1
        -  
    *   - 8
        - 18650 Battery
        - 1
        -   



**Schematic**

|sch_motor|



**Wiring**

.. note::

    * Since DC motors require a high current, we use a Li-po Charger module to power the motor here for safety reasons.
    * Make sure your Li-po Charger Module is connected as shown in the diagram. Otherwise, a short circuit will likely damage your battery and circuitry.


|wiring_motor|


**Code**

.. note::

    * Open the ``3.5_small_fan.py`` from ``pico-2 w-kit-main/micropython`` or copy the code into Thonny, then click "Run" or press F5.

    * Ensure the correct interpreter is selected: MicroPython (Raspberry Pi Pico).COMxx. 

.. code-block:: python

    import machine
    import utime

    motor1A = machine.Pin(14, machine.Pin.OUT)
    motor2A = machine.Pin(15, machine.Pin.OUT)

    def clockwise():
        motor1A.high()
        motor2A.low()

    def anticlockwise():
        motor1A.low()
        motor2A.high()

    def stopMotor():
        motor1A.low()
        motor2A.low()

    while True:
        clockwise()
        utime.sleep(1)
        stopMotor()
        utime.sleep(1)
        anticlockwise()
        utime.sleep(1)
        stopMotor()
        utime.sleep(1)


Once the program is running, the motor will rotate back and forth in a regular pattern.


**Understanding the Code**

#. Initialize the Pins:

   ``motor1A`` and ``motor2A`` are connected to GP14 and GP15, controlling the direction of the motor.

   .. code-block:: python

     motor1A = machine.Pin(14, machine.Pin.OUT)
     motor2A = machine.Pin(15, machine.Pin.OUT)

#. Define Functions:

   * ``rotate_clockwise()``: Sets ``motor1A`` high and ``motor2A`` low to rotate the motor clockwise.
   * ``rotate_counterclockwise()``: Sets ``motor1A`` low and ``motor2A`` high to rotate counterclockwise.
   * ``stop_motor()``: Sets both ``motor1A`` and ``motor2A`` low to stop the motor.

#. Main Loop:

   The motor rotates clockwise, stops, rotates counterclockwise, and stops again, each for one second, repeatedly.

   .. code-block:: python

    while True:
        clockwise()
        utime.sleep(1)
        stopMotor()
        utime.sleep(1)
        anticlockwise()
        utime.sleep(1)
        stopMotor()
        utime.sleep(1)

**Troubleshooting Tips**

* Motor Keeps Spinning After Stopping the Script:

  If the motor continues to run after stopping the program, you may need to reset the Pico. Use a wire or a button to momentarily connect the RUN pin to GND, which resets the Pico.

  |wiring_run_reset|

* Pico Disconnects or Becomes Unresponsive:

  The motor may draw too much current, causing voltage fluctuations. Ensure you're using a separate power supply for the motor and that all grounds are connected.

**Conclusion**

In this lesson, you've learned how to control a DC motor using the TA6586 motor driver and the Raspberry Pi Pico 2 W. You can now control the motor's direction and create projects like a small fan or a motorized device.

**Next Steps**

* **Speed Control**: Try using PWM (Pulse Width Modulation) to control the speed of the motor by connecting the EN1 pin to a PWM-capable GPIO pin.
* **Control Multiple Motors**: Use the other channels of the TA6586 to control additional motors.
* **Sensor Integration**: Incorporate sensors to control the motor based on input (e.g., temperature, light).
