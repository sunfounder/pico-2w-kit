.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ar_joystick:

4.1 Reading Values from a Joystick
==================================

In this lesson, we'll learn how to use a **joystick** with the Raspberry Pi Pico 2 W to read analog values and detect button presses. A joystick is a common input device that allows you to control movement along two axes (X and Y) and often includes a button when pressed down (Z-axis).

* :ref:`cpn_joystick`

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
        - :ref:`cpn_resistor`
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_joystick`
        - 1
        - 

**Understanding the Joystick**

A typical joystick module consists of two potentiometers positioned at right angles to each other:

* **X-axis potentiometer**: Measures left-right movement.
* **Y-axis potentiometer**: Measures up-down movement.
* **Z-axis (Switch)**: A digital button activated when you press down on the joystick.

By reading the analog values from the X and Y axes, you can determine the position of the joystick. The Z-axis button allows you to detect when the joystick is pressed down.

**Schematic**

|sch_joystick|

The SW pin is connected to a 10K pull-up resistor, the reason is to be able to get a stable high level on the SW pin (Z axis) when the joystick is not pressed; otherwise the SW is in a suspended state and the output value may vary between 0/1.


**Wiring**

|wiring_joystick|

**Writing the Code**

.. note::

    * You can open the file ``4.1_toggle_the_joyostick.ino`` under the path of ``pico-2 w-kit-main/arduino/4.1_toggle_the_joyostick``. 
    * Or copy this code into **Arduino IDE**.
    * Don't forget to select the board(Raspberry Pi Pico) and the correct port before clicking the **Upload** button.

    

.. code-block:: arduino

   // Define the pins
   const int joystickX = 26;  // GP26 (ADC0) connected to VRx
   const int joystickY = 27;  // GP27 (ADC1) connected to VRy
   const int joystickSW = 22; // GP22 connected to SW (button)

   void setup() {
     // Initialize serial communication at 115200 baud
     Serial.begin(115200);

     // Initialize the joystick switch pin as input
     pinMode(joystickSW, INPUT_PULLUP);

   }

   void loop() {
     // Read analog values from the joystick
     int xValue = analogRead(joystickX);
     int yValue = analogRead(joystickY);

     // Read the joystick button state
     int buttonState = digitalRead(joystickSW);

     // Print the joystick values to the Serial Monitor
     Serial.print("X: ");
     Serial.print(xValue);
     Serial.print(" | Y: ");
     Serial.print(yValue);
     Serial.print(" | Button: ");
     Serial.println(buttonState == LOW ? "Pressed" : "Released");

     delay(500); // Wait for half a second before the next reading
   }

When the code is running and the Serial Monitor is open:

* Move the joystick in different directions (left, right, up, down) and observe the X and Y values changing accordingly in the Serial Monitor.
* Press the joystick button (Z-axis) and observe the button state changing from "Released" to "Pressed".


**Understanding the Code**

#. Defining Pins:

   * ``joystickX`` and ``joystickY``: Analog pins connected to the joystick's X and Y axes.
   * ``joystickSW``: Digital pin connected to the joystick's button (Z-axis).

#. Setup Function:

   * Initializes serial communication for debugging and monitoring.
   * Sets the joystick button pin as input with an internal pull-up resistor to stabilize the input.

   .. code-block:: arduino

        void setup() {
          Serial.begin(115200); // Initialize serial communication at 115200 baud
          pinMode(joystickSW, INPUT_PULLUP); // Set joystick button as input with pull-up resistor
        }
  
#. ``loop()`` Function:

   * Reading Analog Values:
       
     Reads the current position of the joystick along the X and Y axes. The values range from 0 to 1023, corresponding to the analog voltage levels.
   
     .. code-block:: arduino
   
           int xValue = analogRead(joystickX);
           int yValue = analogRead(joystickY);
       
   * Reading Button State:
       
     Reads the state of the joystick's button. ``LOW`` indicates pressed, and ``HIGH`` indicates released.
   
     .. code-block:: arduino
   
           int buttonState = digitalRead(joystickSW);
       
   * Printing to Serial Monitor:
       
     Outputs the current joystick position and button state to the Serial Monitor for debugging and monitoring.
   
     .. code-block:: arduino
   
       Serial.print("X: ");
       Serial.print(xValue);
       Serial.print(" | Y: ");
       Serial.print(yValue);
       Serial.print(" | Button: ");
       Serial.println(buttonState == LOW ? "Pressed" : "Released");

**Further Exploration**

* Mapping Analog Values to Actions:
  
  * Use the joystick's position to control servos, LEDs, or other actuators based on movement direction and magnitude.

* Dead Zone Implementation:
  
  * Implement a dead zone around the center position to prevent unintentional movements due to slight joystick fluctuations.

* Combining with Other Sensors:
  
  * Integrate the joystick with other sensors (e.g., accelerometers, distance sensors) to create more complex interactions.

* Creating a Game Controller:
  
  * Use multiple joysticks and buttons to build a custom game controller for simple games or robotic control.

**Conclusion**

In this lesson, you've learned how to interface a joystick with the Raspberry Pi Pico to read analog values from the X and Y axes and detect button presses on the Z-axis. This setup can be used as an input method for various projects, including remote controls, robotics, and interactive installations. By understanding how to read and interpret the joystick's values, you can create responsive and dynamic applications.


