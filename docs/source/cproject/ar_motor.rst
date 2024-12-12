.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ar_motor:

3.5 Controlling a Small Fan (DC Motor)
=========================================

In this lesson, we'll learn how to control a **DC motor** (like a small fan) using the Raspberry Pi Pico 2w and an **TA6586 motor driver**. The TA6586 allows us to control the direction of the motor rotation—both clockwise and counterclockwise. Since DC motors require more current than the Pico can provide directly, we'll use an external power supply to safely power the motor.


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
        - :ref:`cpn_pico_w`
        - 1
        - |link_picow_buy|
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
    *   - 9
        - Battery Holder
        - 1
        - 

**Schematic**

|sch_motor|


**Wiring**

|wiring_motor|



**Code**

.. note::

    * You can open the file ``3.5_small_fan.ino`` under the path of ``pico-2w-kit-main/arduino/3.5_small_fan``. 
    * Or copy this code into **Arduino IDE**.
    * Don't forget to select the board(Raspberry Pi Pico) and the correct port before clicking the **Upload** button.


.. code-block:: arduino

    // Define the pins connected to the motor driver
    const int motor1A = 14; // Motor control pin 1
    const int motor2A = 15; // Motor control pin 2

    void setup() {
      // Initialize the motor control pins as OUTPUT
      pinMode(motor1A, OUTPUT); 
      pinMode(motor2A, OUTPUT); 
    }

    void loop() {
         // Rotate the motor clockwise
         clockwise();
         delay(1000); // Keep the motor running clockwise for 1 second
    
        // Stop the motor
        stopMotor();
        delay(1000); // Pause for 1 second
    
        // Rotate the motor counterclockwise
        anticlockwise();
        delay(1000); // Keep the motor running counterclockwise for 1 second
    
        // Stop the motor
        stopMotor();
        delay(1000); // Pause for 1 second
    }

        // Function to rotate the motor clockwise
    void clockwise()
    {
        digitalWrite(motor1A, HIGH); // Set motor1A to HIGH
        digitalWrite(motor2A, LOW);  // Set motor2A to LOW
       // This combination causes the motor to rotate in the clockwise direction
    }

    // Function to rotate the motor counterclockwise
    void anticlockwise()
    {
        digitalWrite(motor1A, LOW);  // Set motor1A to LOW
        digitalWrite(motor2A, HIGH); // Set motor2A to HIGH
    // This combination causes the motor to rotate in the counterclockwise direction
    }

    // Function to stop the motor
    void stopMotor()
    {
        digitalWrite(motor1A, LOW);  // Set motor1A to LOW
        digitalWrite(motor2A, LOW);  // Set motor2A to LOW
    // Setting both pins LOW stops the motor
    }

After uploading the code: the motor will rotate back and forth in a regular pattern.


**Understanding the Code**

#. Defining Control Pins:

   .. code-block:: arduino

        const int motor1A = 14; // Motor control pin 1
        const int motor2A = 15; // Motor control pin 2

#. Setting Pin Modes:

   .. code-block:: arduino

        void setup() {
          pinMode(motor1A, OUTPUT); 
          pinMode(motor2A, OUTPUT); 
        }

#. Controlling Motor Direction:

   * **Clockwise Rotation**: Sets motor1 HIGH and motor2A LOW, causing the motor to rotate in the clockwise direction.

   .. code-block:: arduino

        digitalWrite(motor1A, HIGH); // Set motor1A to HIGH
        digitalWrite(motor2A, LOW);  // Set motor2A to LOW

   * **Counterclockwise Rotation**: Sets motor1A LOW and motor2A HIGH, causing the motor to rotate in the counterclockwise direction.

   .. code-block:: arduino

        digitalWrite(motor1A, LOW);
        digitalWrite(motor2A, HIGH);

   * Keep the motor running clockwise for 1 second

   .. code-block:: arduino

        anticlockwise();
        delay(1000); 

   * Keep the motor running counterclockwise for 1 second

   .. code-block:: arduino

        anticlockwise();
        delay(1000); 

   #. Stopping the Motor:

   Sets both inputs LOW, stopping the motor.

   .. code-block:: arduino

        digitalWrite(motor1A, LOW);  // Set motor1A to LOW
        digitalWrite(motor2A, LOW);  // Set motor2A to LOW
    
   Pause for 1 second

      .. code-block:: arduino

        stopMotor();
        delay(1000); 

**Further Exploration**

* Speed Control:

  Use Pulse Width Modulation (PWM) to control the speed of the motor by connecting the EN1 pin to a PWM-capable GPIO pin and varying the duty cycle.

* Sensor Integration:

  Incorporate sensors (e.g., limit switches, encoders) to create more advanced motor control systems.


**Safety Precautions**

* Power Supply:

  * Ensure that the external power supply voltage matches the motor's voltage rating.
  * Do not power the motor directly from the Pico's 3.3V pin.

* Current Draw:

  * Motors can draw significant current, especially during startup or when stalled.
  * Ensure that your power supply can handle the motor's current requirements.

* Resetting the Pico:

  * In some cases, the motor's current draw may cause voltage dips, leading the Pico to reset or disconnect.
  * If you encounter issues uploading code after running the motor, you can manually reset the Pico by connecting the RUN pin to GND momentarily.

  |wiring_run_reset|


**Conclusion**

In this lesson, you've learned how to control a DC motor using the Raspberry Pi Pico and the TA6586 motor driver. By controlling the inputs to the TA6586, you can change the direction of the motor's rotation. This fundamental concept is essential in robotics, automation, and many other applications involving motors.
