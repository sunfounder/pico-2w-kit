.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ar_reed:

2.9 Feel the Magnetism
===============================

In this lesson, we'll explore how to use a **reed switch** with the Raspberry Pi Pico 2w to detect the presence of a magnetic field. A reed switch is a simple electrical switch that operates using a magnetic field. When a magnet comes near the switch, its internal contacts close, completing an electrical circuit.

* :ref:`cpn_reed`

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
        - :ref:`cpn_reed`
        - 1
        - 

**Understanding the Reed Switch**

A reed switch consists of two thin metal reeds sealed within a glass capsule. These reeds are made of ferromagnetic material and are positioned slightly apart. In the absence of a magnetic field, the reeds are separated, and the switch is **open**. When a magnet comes near the switch, the reeds become magnetized, attract each other, and close the circuit.

* **No Magnet Nearby**: Switch is **open**; the circuit is incomplete.
* **Magnet Nearby**: Switch is **closed**; the circuit is complete.

|img_reed_sche|

**Schematic**

|sch_reed|

By default, GP14 is low; and will go high when the magnet is near the reed switch.

The purpose of the 10K resistor is to keep the GP14 at a steady low level when no magnet is near.

* **No Magnet Nearby**:

  * The reed switch is **open**.
  * **GP14** is connected to **GND** through the pull-down resistor.
  * The GPIO pin reads **LOW** (0).

* **Magnet Nearby**:

  * The reed switch is **closed**.
  * **GP14** is connected to **3.3V** through the reed switch.
  * The GPIO pin reads **HIGH** (1).

**Wiring**


|wiring_reed|

**Code**

.. note::

    * You can open the file ``2.9_feel_the_magnetism.ino`` under the path of ``pico-2w-kit-main/arduino/2.9_feel_the_magnetism``. 
    * Or copy this code into **Arduino IDE**.
    * Don't forget to select the board(Raspberry Pi Pico) and the correct port before clicking the **Upload** button.

.. code-block:: Arduino


   const int reedPin = 14;    // GPIO pin connected to the reed switch
   int reedState = 0;

   void setup() {
     Serial.begin(115200);       // Initialize Serial Monitor at 115200 baud
     pinMode(reedPin, INPUT);    // Set the reed pin as input
   }

   void loop() {
     reedState = digitalRead(reedPin);  // Read the state of the reed switch

     if (reedState == HIGH) {
       Serial.println("Magnet Detected!");
     } else {
       Serial.println("No Magnet.");
     }
     delay(500);  // Delay to avoid flooding the Serial Monitor
   }

When the code is running and the Serial Monitor is open:

* **No Magnet Nearby**: The Serial Monitor will display "No Magnet."
* **Magnet Nearby**: Bring a magnet close to the reed switch. The Serial Monitor will display "Magnet Detected!"

**Understanding the Code**

#. Initializing Serial Communication:

   Starts serial communication at a baud rate of 115200. This allows us to print messages to the Serial Monitor.

   .. code-block:: Arduino

        Serial.begin(115200);

#. Setting Up the Reed Pin:
 
   Configures reedPin (GP14) as an input to read the reed switch state.

   .. code-block:: Arduino

        pinMode(reedPin, INPUT);

#. Reading the Reed Switch State:

   Reads the current state of the reed switch. It will be HIGH when the magnet is near (switch closed) and LOW when no magnet is near (switch open).

   .. code-block:: Arduino

        reedState = digitalRead(reedPin);

#. Responding to Magnet Presence:

   Prints a message based on whether the magnet is near the reed switch.

   .. code-block:: Arduino

        if (reedState == HIGH) {
          Serial.println("Magnet Detected!");
        } else {
          Serial.println("No Magnet.");
        }


**Learn More: Using Interrupts with the Reed Switch**

* **Introduction to Interrupts**

  Imagine you're reading a book, fully immersed in the story. Suddenly, someone taps you on the shoulder to ask a question. You pause your reading, address the question, and then return to your book. This interruption is similar to how interrupts work in microcontrollers.
  
  An interrupt allows a program to respond immediately to important events, pausing the main program flow to execute a special function called an Interrupt Service Routine (ISR). After handling the interrupt, the program resumes where it left off.
  
* **Why Use Interrupts?**

  Using interrupts with the reed switch allows the microcontroller to respond instantly when a magnet is detected, rather than continuously polling (checking) the reed switch in the ``loop()`` function. This is more efficient and can save power in battery-powered applications.

* **Writing the Code with Interrupts**

  Let's modify our program to use an interrupt to detect the magnet.

  .. code-block:: Arduino

        const int reedPin = 14;            // GPIO pin connected to the reed switch
        volatile bool magnetDetected = false;  // Flag to indicate if the magnet is detected

        void setup() {
          Serial.begin(115200);               // Initialize Serial Monitor
          pinMode(reedPin, INPUT);            // Set the reed pin as input
          attachInterrupt(digitalPinToInterrupt(reedPin), onMagnetChange, CHANGE);  // Attach interrupt on any change
        }

        void loop() {
          if (magnetDetected) {
            Serial.println("Magnet Present!");
          } else {
            Serial.println("Waiting for magnet...");
          }
          delay(1000);                         // Delay to avoid flooding the serial monitor
        }

        void onMagnetChange() {
          // Update the flag based on the current state of the reed pin
          magnetDetected = digitalRead(reedPin) == HIGH;  // If HIGH, magnet is present; if LOW, magnet is absent
        }


  .. code-block:: Arduino

        attachInterrupt(digitalPinToInterrupt(reedPin), onMagnetChange, CHANGE);
    
  * ``digitalPinToInterrupt(reedPin)``: Converts the pin number to the appropriate interrupt number.
  * ``onMagnetChange``: The name of the ISR function to call when the interrupt occurs.
  * ``CHANGE``: The interrupt will trigger when the pin has any change.


**Conclusion**

In this lesson, you've learned how to use a reed switch with the Raspberry Pi Pico to detect the presence of a magnetic field. You've also explored how interrupts can make your program more efficient by responding immediately to events without constantly checking the sensor in the main loop. Understanding how to use interrupts is a valuable skill in embedded programming, allowing you to create more responsive and efficient applications.

**Further Exploration**

* **Door Sensor**: Use the reed switch to create a simple door alarm that triggers when the door is opened.
* **Counting Revolutions**: Attach a magnet to a rotating object and use the reed switch to count revolutions per minute (RPM).
* **Security Systems**: Incorporate multiple reed switches to monitor windows and doors in a security system.

**Additional Resources**

* `attachInterrupt() - Arduino Reference <https://www.arduino.cc/reference/en/language/functions/external-interrupts/attachinterrupt/>`_


