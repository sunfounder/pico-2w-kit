.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ar_micro:

2.8 - Press Gently
==========================

|img_micro_switch|

In this lesson, we'll learn how to use a **micro switch** (also known as a limit switch) with the Raspberry Pi Pico 2 W to detect when it's pressed or released. Micro switches are commonly used in devices like microwave oven doors, printer covers, or as end stops in 3D printers because they are reliable and can handle frequent activation.

* :ref:`cpn_micro_switch`

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
        - :ref:`cpn_micro_switch`
        - 1
        - 

**Understanding the Micro Switch**

A micro switch typically has three pins:

|img_micro_switch|

- **Common (C)**: The middle pin.
- **Normally Open (NO)**: Connected to the common pin when the switch is **pressed**.
- **Normally Closed (NC)**: Connected to the common pin when the switch is **not pressed**.

By connecting the switch appropriately, we can detect when it's pressed by reading the voltage level on a GPIO pin.

**Schematic**

|sch_limit_sw|

By default, GP14 is low and when pressed, GP14 is high.

The purpose of the 10K resistor is to keep the GP14 low during pressing.

When you press a mechanical switch, the contacts may bounce, causing multiple rapid transitions between open and closed states. The capacitor connected between GP14 and GND helps filter out this noise.

* **Switch Not Pressed**:

  * The **Common (C)** pin is connected to the **NC** pin, which is connected to **GND**.
  * **GP14** reads **LOW** (0V).

* **Switch Pressed**:

  * The **Common (C)** pin is connected to the **NO** pin, which is connected to **3.3V**.
  * **GP14** reads **HIGH** (3.3V).

**Wiring**

|wiring_limit_sw|


**Writing the Code**

We'll write a simple program that detects when the micro switch is pressed and prints a message to the Serial Monitor.

.. note::

    * You can open the file ``2.8_press_gently.ino`` under the path of ``pico-2 w-kit-main/arduino/2.8_press_gently``. 
    * Or copy this code into **Arduino IDE**.
    * Don't forget to select the board(Raspberry Pi Pico) and the correct port before clicking the **Upload** button.



.. code-block:: Arduino

   const int switchPin = 14;   // GPIO pin connected to the micro switch
   int switchState = 0;

   void setup() {
     Serial.begin(115200);       // Initialize Serial Monitor at 115200 baud
     pinMode(switchPin, INPUT);  // Set the switch pin as input
   }

   void loop() {
     switchState = digitalRead(switchPin);  // Read the state of the switch

     if (switchState == HIGH) {
       Serial.println("The switch is pressed!");
     } else {
       Serial.println("The switch is not pressed.");
     }
     delay(200);  // Small delay to avoid flooding the Serial Monitor
   }

When the code is running and the Serial Monitor is open, press and release the micro switch.
The Serial Monitor will display "The switch is pressed!" when you press the switch and "The switch is not pressed." when you release it.

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

   Reads the current state of the switch. It will be HIGH when pressed and LOW when not pressed.

   .. code-block:: Arduino

        switchState = digitalRead(switchPin);

#. Responding to Switch Press:

   Prints a message based on whether the switch is pressed or not.

   .. code-block:: Arduino

        if (switchState == HIGH) {
          Serial.println("The switch is pressed!");
        } else {
          Serial.println("The switch is not pressed.");
        }


**Alternative: Using Internal Pull-Up Resistor**

If you prefer to simplify the circuit and reduce the number of components, you can use the internal pull-up resistor of the Pico.

* GP14 is connected to GND when the switch is pressed, so it reads LOW (0).
* GP14 reads HIGH when the switch is not pressed due to the internal pull-up resistor.

* Circuit Modifications:

  Remove the External 10KΩ Resistor and Capacitor.

* Micro Switch Connections:

  * **Common (C) Terminal**: Connect to GP14 on the Pico.
  * **Normally Open (NO) Terminal**: Connect to GND on the Pico.
  * **Normally Closed (NC) Terminal**: Leave unconnected.

* Code Modifications:

  .. code-block:: Arduino

        const int switchPin = 14;   // GPIO pin connected to the micro switch
        int switchState = 0;

        void setup() {
          Serial.begin(115200);          // Initialize Serial Monitor at 115200 baud
          pinMode(switchPin, INPUT_PULLUP);  // Enable internal pull-up resistor
        }

        void loop() {
          switchState = digitalRead(switchPin);  // Read the state of the switch

          if (switchState == LOW) {
            Serial.println("The switch is pressed!");
          } else {
            Serial.println("The switch is not pressed.");
          }
          delay(200);  // Small delay to avoid flooding the Serial Monitor
        }

**Debouncing the Switch**

Mechanical switches can generate noise due to bouncing contacts. To improve the reliability of your readings, you can implement software debouncing.


.. code-block:: Arduino

    const int switchPin = 14;   // GPIO pin connected to the micro switch
    int switchState = 0;        // Current state of the switch
    int lastSwitchState = HIGH; // Previous state of the switch
    unsigned long lastDebounceTime = 0;  // Time of the last state change
    unsigned long debounceDelay = 50;    // Debounce time in milliseconds

    void setup() {
      Serial.begin(115200);
      pinMode(switchPin, INPUT_PULLUP);
    }

    void loop() {
      int reading = digitalRead(switchPin);

      if (reading != lastSwitchState) {
        lastDebounceTime = millis();
      }

      if ((millis() - lastDebounceTime) > debounceDelay) {
        if (reading != switchState) {
          switchState = reading;

          if (switchState == LOW) {
            Serial.println("The switch is pressed!");
          } else {
            Serial.println("The switch is not pressed.");
          }
        }
      }

      lastSwitchState = reading;
    }

* Checks if the reading has changed from the last state.
* If it has, resets the ``lastDebounceTime``.
* If the reading remains stable past the debounce delay, it considers the new state as valid.

**Conclusion**

In this lesson, you've learned how to use a micro switch with the Raspberry Pi Pico to detect when it's pressed or released. You've also seen how to implement a pull-down resistor in the circuit to ensure reliable readings and how to use the internal pull-up resistor to simplify the circuit. Additionally, you've learned about debouncing to handle mechanical switch noise.

**Further Exploration**

* **Control an LED**: Modify the code to turn an LED on when the switch is pressed.
* **Multiple Switches**: Try adding more micro switches to detect different inputs.
* **Create a Counter**: Count the number of times the switch is pressed and display it.
