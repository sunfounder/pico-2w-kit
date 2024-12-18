.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ar_tilt:

2.6 Tilt It!
=======================

In this lesson, we'll learn how to use a tilt switch with the Raspberry Pi Pico 2 W to detect changes in orientation. A tilt switch is a simple device that can sense whether it is upright or tilted, making it useful for applications like motion detection, orientation sensing, or as a trigger based on position.


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
        - :ref:`cpn_tilt`
        - 1
        - 

**Schematic**

|sch_tilt|

* **When Upright (Switch Closed)**:

  * The tilt switch connects **3.3V** directly to **GP14**.
  * The GPIO pin reads **HIGH** (1).

* **When Tilted (Switch Open)**:

  * The tilt switch disconnects **3.3V** from **GP14**.
  * The pull-down resistor pulls **GP14** to **GND**.
  * The GPIO pin reads **LOW** (0).

**Wiring**

|wiring_tilt|

**Writing the Code**

.. note::

    * You can open the file ``2.6_tilt_it.ino`` under the path of ``pico-2 w-kit-main/arduino/2.4_colorful_light``. 
    * Or copy this code into **Arduino IDE**.
    * Don't forget to select the board(Raspberry Pi Pico) and the correct port before clicking the **Upload** button.



.. code-block:: Arduino

   const int tiltPin = 14;  // GPIO pin connected to the tilt switch

   void setup() {
     Serial.begin(115200);       // Initialize Serial Monitor at 115200 baud
     pinMode(tiltPin, INPUT);    // Set the tilt pin as input
   }

   void loop() {
     int tiltState = digitalRead(tiltPin);  // Read the state of the tilt switch

     if (tiltState == HIGH) {
       Serial.println("The switch works!");
     }
     delay(100);  // Small delay to avoid flooding the Serial Monitor
   }

When the code is running, and the Serial Monitor is open, tilt the breadboard or the tilt switch.
Each time you tilt the switch to the upright position, "The switch works!" should appear in the Serial Monitor.

**Understanding the Code**

#. Initializing Serial Communication:

   Starts serial communication at a baud rate of 115200. This allows us to print messages to the Serial Monitor.

   .. code-block:: Arduino

        Serial.begin(115200);

#. Setting Up the Tilt Pin:

   Configures ``tiltPin`` (GP14) as an input to read the state of the tilt switch.

   .. code-block:: Arduino

        pinMode(tiltPin, INPUT);


#. Reading the Tilt Switch State:

   Reads the current state of the tilt switch. It will be ``HIGH`` when upright and ``LOW`` when tilted.

   .. code-block:: Arduino

        int tiltState = digitalRead(tiltPin);

#. Responding to Tilt:

   If the tilt switch is upright (closed), print a message to the Serial Monitor.

   .. code-block:: Arduino

        if (tiltState == HIGH) {
          Serial.println("The switch works!");
        }

**Experimenting Further**

* **Control an LED**: Modify the code to turn an LED on when the tilt switch is upright and off when tilted.

  .. code-block:: Arduino

        const int tiltPin = 14;   // GPIO pin connected to the tilt switch
        const int ledPin = 15;    // GPIO pin connected to an LED

        void setup() {
          Serial.begin(115200);
          pinMode(tiltPin, INPUT);
          pinMode(ledPin, OUTPUT);
        }

        void loop() {
          int tiltState = digitalRead(tiltPin);

          if (tiltState == HIGH) {
            Serial.println("The switch works!");
            digitalWrite(ledPin, HIGH);  // Turn on LED
          } else {
            digitalWrite(ledPin, LOW);   // Turn off LED
          }
          delay(100);
        }

* **Adjust Sensitivity**: Some tilt switches have different sensitivity levels. Experiment by adjusting the orientation to see at what angle the switch activates.

**Conclusion**

In this lesson, you've learned how to use a tilt switch with the Raspberry Pi Pico to detect changes in orientation. This fundamental skill allows you to create projects that respond to movement or position, such as alarms, automatic lighting, or interactive devices.

