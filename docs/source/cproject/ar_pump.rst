.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ar_pump:

3.6 Controlling a Water Pump
=============================

In this lesson, we'll learn how to control a **small water pump** using the Raspberry Pi Pico 2 W and an **TA6586 motor driver**. A small centrifugal pump can be used for projects like automatic plant watering systems or creating miniature water features. Controlling the pump is similar to controlling a DC motor, as it uses the same principles.

* :ref:`cpn_pump`
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
        - :ref:`cpn_lipo_charger`
        - 1
        -  
    *   - 7
        - 18650 Battery
        - 1
        -  
    *   - 8
        - :ref:`cpn_pump`
        - 1
        -  


**Schematic**

|sch_pump|


**Wiring**

.. note::

    * Since pump require a high current, we use a Li-po Charger module to power the motor here for safety reasons.
    * Make sure your Li-po Charger Module is connected as shown in the diagram. Otherwise, a short circuit will likely damage your battery and circuitry.


|wiring_pump|

**Code**

.. note::

    * You can open the file ``3.6_pumping.ino`` under the path of ``pico-2w-kit-main/arduino/3.6_pumping``. 
    * Or copy this code into **Arduino IDE**.
    * Don't forget to select the board(Raspberry Pi Pico) and the correct port before clicking the **Upload** button.

    
.. code-block:: Arduino

    const int motor1A = 14; // Motor control pin 1
    const int motor2A = 15; // Motor control pin 2

    void setup() {
      // Set motor control pins as OUTPUT
      pinMode(motor1A, OUTPUT); // Configure motor1A as an output pin
      pinMode(motor2A, OUTPUT); // Configure motor2A as an output pin
    }

    void loop() {
      // Rotate the motor in a clockwise direction
      digitalWrite(motor1A, HIGH); // Set motor1A to HIGH (activates one side of the motor)
      digitalWrite(motor2A, LOW);  // Set motor2A to LOW (deactivates the opposite side of the motor)
    }




After the code is run, the pump starts working and you will see water flowing out of the tube at the same time.
* This cycle repeats indefinitely.
* If water doesn't flow initially, make sure the pump is submerged, and there are no air bubbles in the tubing.


**Safety Precautions**

* Water and Electricity:

  * Be extremely careful to keep water away from the Pico and other electronic components.
  * Ensure all connections are secure and insulated if necessary.

* Power Supply:

  * Use a power supply that matches the pump's voltage requirements (typically 3V-6V).
  * Do not power the pump directly from the Pico's 3.3V pin.

* Current Draw:

  * Pumps can draw significant current.
  * Ensure your power source can handle the pump's current requirements.

* Resetting the Pico:

  If you encounter issues uploading code after running the pump, you can manually reset the Pico by connecting the RUN pin to GND momentarily.

  |wiring_run_reset|

**Further Exploration**

* Automated Plant Watering:

  Incorporate soil moisture sensors to automate the watering process based on soil dryness.

* PWM Speed Control:

  Use Pulse Width Modulation (PWM) to control the pump's speed by varying the voltage.

* Timing and Scheduling:

  Implement more complex timing using real-time clocks or schedulers.

**Conclusion**

In this lesson, you've learned how to control a small water pump using the Raspberry Pi Pico and the TA6586 motor driver. This technique can be used in various projects like automated plant watering systems, fountains, or hydroponic setups.

