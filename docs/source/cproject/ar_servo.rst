.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ar_servo:

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

**Writing the Code**


.. note::

    * You can open the file ``3.7_swinging_servo.ino`` under the path of ``pico-2 w-kit-main/arduino/3.7_swinging_servo``. 
    * Or copy this code into **Arduino IDE**.
    * Don't forget to select the board(Raspberry Pi Pico) and the correct port before clicking the **Upload** button.


.. code-block:: arduino

    #include <Servo.h>

    Servo myServo;  // Create a servo object

    void setup() {
      myServo.attach(15);  // Attach the servo to GPIO pin 15
    }

    void loop() {
      // Move the servo from 0 to 180 degrees
      for (int angle = 0; angle <= 180; angle += 1) {
        myServo.write(angle);
        delay(15);  // Wait 15 milliseconds for the servo to reach the position
      }
      // Move the servo from 180 to 0 degrees
      for (int angle = 180; angle >= 0; angle -= 1) {
        myServo.write(angle);
        delay(15);
      }
    }

After uploading the code, the servo arm should start swinging smoothly from 0° to 180° and back.
If the servo doesn't move or behaves erratically:

* Check your wiring connections.
* Ensure the servo is properly powered.
* Make sure the servo is not mechanically blocked.

**Understanding the Code**

#. Including the ``Servo`` Library:

   Includes the ``Servo`` library, which provides functions to control the servo motor.

   .. code-block:: arduino

        #include <Servo.h>

#. Creating a ``Servo`` Object:

   Creates a ``Servo`` object named ``myServo`` to control the servo.

   .. code-block:: arduino

        Servo myServo;

#. Attaching the Servo to a Pin:

   Attaches the servo to GPIO pin 15 on the Pico.

   .. code-block:: arduino

        myServo.attach(15);

#. Moving the Servo:

   * Moves the servo from 0° to 180° in 1-degree increments. The delay(15) provides a small delay to allow the servo to reach each position smoothly.
   
   .. code-block:: arduino

        for (int angle = 0; angle <= 180; angle += 1) {
          myServo.write(angle);
          delay(15);
        }

   * Reversing the Movement: Moves the servo back from 180° to 0°, creating a back-and-forth swinging motion.

   .. code-block:: arduino

        for (int angle = 180; angle >= 0; angle -= 1) {
          myServo.write(angle);
          delay(15);
        }

**Further Exploration**

* Adjusting Speed:

  Change the ``delay()`` value in the loops to make the servo move faster or slower.

* Controlling Position Directly:

  Use ``myServo.write(angle);`` with a specific angle to set the servo to a fixed position.

* Interactive Control:

  Connect a potentiometer to control the servo angle interactively.

**Conclusion**

In this lesson, you've learned how to control a servo motor using the Raspberry Pi Pico and the Servo library. By adjusting the code, you can set the servo to any angle between 0° and 180°, allowing for precise control in your projects.


