.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_servo:

3.7 Swinging Servo
===================

In this lesson, we'll learn how to control a **servo motor** using the Raspberry Pi Pico 2 W. A servo motor is a device that can rotate to a specific angle between 0° and 180°. It's widely used in remote control toys, robots, and other applications that require precise position control.

Let's get started and make the servo swing back and forth!

* :ref:`cpn_servo`

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
        - :ref:`cpn_servo`
        - 1
        - |link_servo_buy|


**Schematic**

|sch_servo|

**Wiring**

|wiring_servo|

* Orange wire is signal and connected to GP15.
* Red wire is VCC and connected to VBUS(5V).
* Brown wire is GND and connected to GND.

Servos can draw significant current, especially under load. Since we're using a small servo and not putting it under heavy load, powering it from the Pico's VBUS pin is acceptable for this simple experiment. For larger servos or multiple servos, use an external power supply.

**Setting Up the Servo Arm**

* Attach the servo arm (also called a horn) to the servo's output shaft.
* Secure it with the small screw provided with the servo if necessary.


.. 1. Press the Servo Arm into the Servo output shaft. If necessary, fix it with screws.
.. #. Connect **VBUS** (not 3V3) and GND of Pico 2 W to the power bus of the breadboard.
.. #. Connect the red lead of the servo to the positive power bus with a jumper.
.. #. Connect the yellow lead of the servo to the GP15 pin with a jumper wire.
.. #. Connect the brawn lead of the servo to the negative power bus with a jumper wire.

**Writing the Code**

We'll write a MicroPython program to make the servo sweep back and forth between 0° and 180°.

.. note::

    * Open the ``3.7_swinging_servo.py`` from ``pico-2w-kit-main/micropython`` or copy the code into Thonny, then click "Run" or press F5.
    * Ensure the correct interpreter is selected: MicroPython (Raspberry Pi Pico).COMxx. 
    

.. code-block:: python

    import machine
    import utime

    # Initialize PWM on pin GP15
    servo = machine.PWM(machine.Pin(15))
    servo.freq(50)  # Set the frequency to 50Hz

    # Function to map angle to duty cycle
    def angle_to_duty(angle):
        min_duty = 1638  # Corresponds to 0.5ms pulse (0°)
        max_duty = 8192  # Corresponds to 2.5ms pulse (180°)
        duty = int(min_duty + (angle / 180) * (max_duty - min_duty))
        return duty

    while True:
        # Move servo from 0° to 180°
        for angle in range(0, 181, 1):
            servo.duty_u16(angle_to_duty(angle))
            utime.sleep_ms(20)
        # Move servo from 180° back to 0°
        for angle in range(180, -1, -1):
            servo.duty_u16(angle_to_duty(angle))
            utime.sleep_ms(20)

When the code is running, the servo should smoothly sweep back and forth between 0° and 180°.


**Understanding the Code**

#. Import Modules:

   * ``machine``: Provides access to hardware-related functions.
   * ``utime``: Contains time-related functions for delays.

#. Initialize PWM:

   We set up PWM on GP15.
   The frequency is set to 50Hz, which is standard for servos.

   .. code-block:: python

      servo = machine.PWM(machine.Pin(15))
      servo.freq(50)

#. Define the ``angle_to_duty`` Function:

   * This function maps an angle (0° to 180°) to the corresponding duty cycle value for the servo.
   * The ``min_duty`` and ``max_duty`` correspond to the minimum and maximum pulse widths for the servo control signal.
   * The calculation scales the angle to the appropriate duty cycle.

   .. code-block:: python

      def angle_to_duty(angle):
          min_duty = 1638  # 0.5ms pulse width
          max_duty = 8192  # 2.5ms pulse width
          duty = int(min_duty + (angle / 180) * (max_duty - min_duty))
          return duty
    
#. Main Loop to Move the Servo:

   * The servo moves from 0° to 180°, increasing the angle by 1° each time.
   * Then it moves back from 180° to 0°.
   * ``utime.sleep_ms(20)`` adds a small delay to smooth the movement.

   .. code-block:: python

      while True:
          for angle in range(0, 181, 1):
              servo.duty_u16(angle_to_duty(angle))
              utime.sleep_ms(20)
          for angle in range(180, -1, -1):
              servo.duty_u16(angle_to_duty(angle))
              utime.sleep_ms(20)

**More about the Code**

Servos are controlled by sending a PWM signal with a specific pulse width.
A 50Hz PWM signal (period of 20ms) is standard for servos.
The pulse width within each period determines the servo's angle:

* 0.5ms pulse width corresponds to 0°.
* 1.5ms pulse width corresponds to 90°.
* 2.5ms pulse width corresponds to 180°.

By adjusting the duty cycle of the PWM signal, we change the pulse width.

The ``duty_u16()`` function accepts values from 0 to 65535.
To calculate the duty cycle corresponding to a pulse width:

.. code-block::

  Duty cycle = (Pulse Width / Period) * 65535

For example, for a 0.5ms pulse width:

.. code-block::

  Duty cycle = (0.5ms / 20ms) * 65535 ≈ 1638

**Experimenting Further**

* **Change the Speed**: Adjust the ``utime.sleep_ms(20)`` delay to make the servo move faster or slower.
* **Set Specific Angles**: Modify the code to move the servo to specific angles.

  .. code-block:: python

    servo.duty_u16(angle_to_duty(90))  # Move to 90°

* **Control with Input**: Connect a potentiometer or buttons to control the servo's angle interactively.

**Important Notes**

* **Power Supply**: Ensure the servo is powered adequately. If you notice jitter or erratic movement, consider using an external 5V power supply for the servo.
* **Avoid Overloading**: Do not force the servo beyond its physical limits (usually 0° to 180°) to prevent damage.

**Conclusion**

In this lesson, you've learned how to control a servo motor using the Raspberry Pi Pico 2 W. You now understand how to generate PWM signals to set the servo's angle and make it move smoothly. This skill is fundamental for robotics and automation projects where precise movement is required.

