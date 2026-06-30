.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _cpn_servo:

Servo
===========

|img_servo|

A servo motor typically consists of the following components: a case, shaft, gear system, potentiometer, DC motor, and an embedded control board.

**How It Works**
- The microcontroller sends PWM signals to the servo through its signal pin.
- The embedded control board inside the servo interprets these signals and adjusts the motor's operation accordingly.
- The motor drives the gear system, which reduces speed and increases torque, ultimately rotating the shaft.
- The shaft is mechanically linked to the potentiometer. As the shaft rotates, it moves the potentiometer, generating a voltage signal proportional to the shaft's position.
- This feedback signal is sent to the embedded control board, which compares the current position to the target position.
- Based on this comparison, the board adjusts the motor's direction and speed, allowing the servo to accurately stop and hold at the desired position.
- This closed-loop feedback system ensures precision and stability in the servo's movement.

|img_servo_i|

The angle is determined by the duration of a pulse that is applied to the control wire. This is called Pulse width Modulation. The servo expects to see a pulse every 20 ms. The length of the pulse will determine how far the motor turns. For example, a 1.5ms pulse will make the motor turn to the 90 degree position (neutral position).
When a pulse is sent to a servo that is less than 1.5 ms, the servo rotates to a position and holds its output shaft some number of degrees counterclockwise from the neutral point. When the pulse is wider than 1.5 ms the opposite occurs. The minimal width and the maximum width of pulse that will command the servo to turn to a valid position are functions of each servo. Generally the minimum pulse will be about 0.5 ms wide and the maximum pulse will be 2.5 ms wide.

|img_servo_duty|


.. Example
.. -------------------

.. :ref:`Swinging Servo`

**Example**

* :ref:`py_servo` (For MicroPython User)
* :ref:`py_somato_controller` (For MicroPython User)
* :ref:`py_iot_sunfounder_controller` (For MicroPython User)
* :ref:`py_iot_ble_lock` (For MicroPython User)
* :ref:`ar_servo` (For Arduino User)

.. * :ref:`per_water_tank` (For Piper Make User)
.. * :ref:`per_swing_servo` (For Piper Make User)
.. * :ref:`per_lucky_cat` (For Piper Make User)
