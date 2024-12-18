.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ar_slide:

2.7 Toggle Left and Right
============================

In this lesson, we'll learn how to use a **slide switch** with the Raspberry Pi Pico 2 W to detect its position (left or right) and perform actions based on that. A slide switch is a simple mechanical device that connects the common (middle) pin to one of the two outer pins depending on its position.

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
        - :ref:`cpn_capacitor`
        - 1(104)
        - |link_capacitor_buy|
    *   - 7
        - :ref:`cpn_slide_switch`
        - 1
        - 

**Understanding the Slide Switch**

|img_slide|

A slide switch has three pins:

- **Pin 1**: Connected when the switch is toggled to one side (e.g., left)
- **Pin 2**: Common pin (middle pin)
- **Pin 3**: Connected when the switch is toggled to the other side (e.g., right)

By reading the voltage on the common pin, we can determine the position of the switch.

**Schematic**

|sch_slide|

GP14 will get a different level, when you toggle the slide switch to the right or left.

The purpose of the 10K resistor is to keep the GP14 low during toggling (not toggling to the far left and not toggling to the far right).

When you toggle the switch, the mechanical contacts can cause rapid, noisy signals known as "bounce." The capacitor connected between GP14 and GND helps to filter out these rapid fluctuations, providing a cleaner signal.

* Switch Toggled to the Right:

  * Pin 2 (GP14) is connected to **3.3V** through Pin 1.
  * The GPIO pin reads **HIGH** (1).

* Switch Toggled to the Left:

  * Pin 2 (GP14) is connected to **GND** through Pin 3.
  * The GPIO pin reads **LOW** (0).

* Switch in the Middle Position:

  * Pin 2 (GP14) is not connected to either **3.3V** or **GND**.
  * The pull-down resistor keeps the GPIO pin at **LOW** (0).
  * The capacitor helps to reduce switch bounce (noise due to mechanical movement).



**Wiring**

|wiring_slide|

**Writing the Code**

.. note::

    * You can open the file ``2.7_toggle_left_right.ino`` under the path of ``pico-2 w-kit-main/arduino/2.7_toggle_left_right``. 
    * Or copy this code into **Arduino IDE**.
    * Don't forget to select the board(Raspberry Pi Pico) and the correct port before clicking the **Upload** button.


.. code-block:: Arduino

   const int switchPin = 14;   // GPIO pin connected to the slide switch
   int switchState = 0;

   void setup() {
     Serial.begin(115200);       // Initialize Serial Monitor at 115200 baud
     pinMode(switchPin, INPUT);  // Set the switch pin as input
   }

   void loop() {
     switchState = digitalRead(switchPin);  // Read the state of the switch

     if (switchState == HIGH) {
       Serial.println("ON");   // Switch toggled to the left
     } else {
       Serial.println("OFF");  // Switch toggled to the right
     }
     delay(200);  // Small delay to avoid flooding the Serial Monitor
   }

When the code is running and the Serial Monitor is open:

Prints "ON" when the switch is toggled to the left and "OFF" when toggled to the right.


**Understanding the Code**

#. Initializing Serial Communication:

   Starts serial communication at a baud rate of 115200. This allows us to print messages to the Serial Monitor.

   .. code-block:: Arduino

        Serial.begin(115200);


#. Setting Up the Switch Pin:

   Configures switchPin (GP14) as an input to read the switch state.

   .. code-block:: Arduino

        pinMode(switchPin, INPUT);


#. Reading the Switch State:

   Reads the current state of the switch. It will be HIGH when toggled to the right and LOW when toggled to the left or in the middle position due to the pull-down resistor.

   .. code-block:: Arduino

        switchState = digitalRead(switchPin);


#. Responding to Switch Position:

   Prints "ON" when the switch is toggled to the left (GP14 reads HIGH) and "OFF" when toggled to the right (GP14 reads LOW).

   .. code-block:: Arduino

        if (switchState == HIGH) {
          Serial.println("ON");
        } else {
          Serial.println("OFF");
        }

**Alternative: Using Internal Pull-Up Resistor**

If you prefer to simplify the circuit and reduce the number of components, you can use the internal pull-up resistor of the Pico. However, please note that traditional Arduino boards do not support internal pull-down resistors, only internal pull-up resistors. The Raspberry Pi Pico does support INPUT_PULLDOWN, but in the Arduino environment, its support may vary. For this example, we'll use INPUT_PULLUP.

* Circuit Modifications:

  * Remove the External 10KΩ Resistor and Capacitor.
  * Slide Switch Connections:

    * Pin 1: Connect to GND on the Pico.
    * Pin 2: Connect to GP14 on the Pico.
    * Pin 3: Leave unconnected or connect to GND (since we're using the internal pull-up).

* Code Modifications:

  .. code-block:: Arduino

        const int switchPin = 14;   // GPIO pin connected to the slide switch
        int switchState = 0;

        void setup() {
          Serial.begin(115200);          // Initialize Serial Monitor at 115200 baud
          pinMode(switchPin, INPUT_PULLUP);  // Enable internal pull-up resistor
        }

        void loop() {
          switchState = digitalRead(switchPin);  // Read the state of the switch

          if (switchState == LOW) {
            Serial.println("ON");    // Switch connected to GND, toggled to the right
          } else {
            Serial.println("OFF");   // Switch not connected, reads HIGH due to pull-up
          }
          delay(200);  // Small delay to avoid flooding the Serial Monitor
        }

**Conclusion**

In this lesson, you've learned how to use a slide switch with the Raspberry Pi Pico to detect its position and perform actions based on that. You've also seen how to implement a pull-down resistor in the circuit to ensure reliable readings and how to use the internal pull-up resistor to simplify the circuit.

**Further Exploration**

* **Control an LED**: Modify the code to turn an LED on or off based on the switch position.
* **Multiple Switches**: Try adding more switches to control different actions.
* **Debouncing**: Implement software debouncing to handle any residual switch bounce.
