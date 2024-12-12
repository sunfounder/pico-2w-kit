.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ar_relay:


2.16 Control Another Circuit with a Relay
==========================================

In this lesson, we will learn how to control another circuit using a **relay** and the Raspberry Pi Pico 2w. A relay acts like a switch controlled by a low-voltage circuit (like Pico) to operate a high-voltage circuit. For example, you can use a relay to turn on a lamp or any other device, making it possible to automate electrical appliances.

.. warning::
    Modification of electrical appliances comes with great danger, do not try it lightly, please do it under the guidance of professionals.

* :ref:`cpn_relay`

Here we only use a simple circuit powered by a breadboard power module as an example to show how to control it using relay.

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
        - :ref:`cpn_transistor`
        - 1(S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_diode`
        - 1
        - 
    *   - 7
        - :ref:`cpn_relay`
        - 1
        - |link_relay_buy|

**Circuit Diagram**

|sch_relay_1|

* Relay Activation:

  * The relay's coil is energized by the transistor when the Pico outputs a **high signal** (3.3V) to GP15.
  * The transistor allows current to flow through the relay, activating the switch inside.
  * The relay makes a "click" sound when switching, indicating the control of the load circuit.

* Flyback Diode:

  * The diode is placed across the relay coil to protect the transistor from voltage spikes that occur when the relay is turned off.

**Wiring Diagram**

|wiring_relay_1|

**Code**


.. note::

    * You can open the file ``2.16_relay.ino`` under the path of ``pico-2w-kit-main/arduino/2.16_relay``. 
    * Or copy this code into **Arduino IDE**.
    * Don't forget to select the board(Raspberry Pi Pico) and the correct port before clicking the **Upload** button.

.. code-block:: arduino

   const int relayPin = 15;  // GPIO pin connected to the transistor base

   void setup() {
     pinMode(relayPin, OUTPUT);
     digitalWrite(relayPin, LOW);  // Ensure the relay is off at startup
   }

   void loop() {
     // Turn the relay on
     digitalWrite(relayPin, HIGH);
     Serial.println("Relay ON");
     delay(2000);  // Wait for 2 seconds

     // Turn the relay off
     digitalWrite(relayPin, LOW);
     Serial.println("Relay OFF");
     delay(2000);  // Wait for 2 seconds
   }

After uploading the code, you should hear a "click" sound from the relay every 2 seconds as it switches on and off.

**Understanding the Code**

#. Defining the Relay Pin:

   Assigns ``relayPin`` to GPIO 15, which controls the transistor and thus the relay.

   .. code-block:: arduino

        const int relayPin = 15;  // GPIO pin connected to the transistor base

#. Setting Up the Pin Modes:

   Sets ``relayPin`` as an output. Initializes the relay in the OFF state.

   .. code-block:: arduino

        void setup() {
          pinMode(relayPin, OUTPUT);
          digitalWrite(relayPin, LOW);  // Ensure the relay is off at startup
        }

#. Controlling the Relay:

   * Sets ``relayPin`` ``HIGH`` to turn on the transistor, energizing the relay coil.
   * Waits for 2 seconds.
   * Sets ``relayPin`` ``LOW`` to turn off the transistor, de-energizing the relay coil.
   * Waits for another 2 seconds.
   * Repeats the cycle indefinitely.

   .. code-block:: arduino

        // Turn the relay on
        digitalWrite(relayPin, HIGH);
        Serial.println("Relay ON");
        delay(2000);  // Wait for 2 seconds

        // Turn the relay off
        digitalWrite(relayPin, LOW);
        Serial.println("Relay OFF");
        delay(2000);  // Wait for 2 seconds

**Experimenting Further**

* **Set a Timer**: Modify the code to turn the relay on for 10 minutes and then automatically turn it off.
* **Control Home Appliances**: With appropriate guidance, you can connect high-voltage devices to the relay for automation tasks such as turning lights or fans on and off.

  * The circuit should look like this: To demonstrate controlling an external circuit safely, we'll add an external 5V power supply (through a breadboard power module) to power an LED. This simulates how you could control higher voltage devices (like home appliances) using the relay. Here's how to modify the circuit:

    |sch_relay_2|
  
    |wiring_relay_2|

  * Code to Control the Relay:

    .. code-block:: arduino
    
       const int relayPin = 15;  // GPIO pin connected to the transistor base

       void setup() {
         pinMode(relayPin, OUTPUT);
         digitalWrite(relayPin, LOW);  // Ensure the relay is off at startup
       }

       void loop() {
         // Turn the relay on
         digitalWrite(relayPin, HIGH);
         Serial.println("Relay ON");
         delay(2000);  // Wait for 2 seconds

         // Turn the relay off
         digitalWrite(relayPin, LOW);
         Serial.println("Relay OFF");
         delay(2000);  // Wait for 2 seconds
       }

    When the relay is activated (GP15 outputs high), the Normally Open (NO) and Common (C) pins of the relay connect, allowing the external 5V power to flow through the LED. The LED will light up, simulating how a relay can control an external appliance.

    When the relay is deactivated (GP15 outputs low), the Normally Open (NO) pin disconnects from the Common (C) pin, cutting off the external power, and the LED turns off.


**Safety Considerations for Controlling Real Appliances**

This example uses an LED and a 5V power source to demonstrate relay control. If you are controlling higher voltage devices (like household appliances), ensure:

* **Proper Voltage Rating**: Use a relay rated for the appropriate voltage and current for your appliance.
* **Isolation**: For safety, ensure proper isolation between the low-voltage control circuit (like the Pico) and the high-voltage appliance circuit.
* **Fuse Protection**: Consider adding fuses or circuit breakers to protect against short circuits or overloads.
* **Professional Guidance**: When working with high-voltage circuits, always seek professional guidance to ensure safe operation.

This project can serve as the basis for home automation, such as controlling lamps, fans, or other devices based on timers or sensors connected to the Raspberry Pi Pico 2w.

**Using the NC Terminal**

* If you connect your controlled circuit between COM and NC:

  * The circuit will be closed (ON) when the relay is not energized.
  * The circuit will be open (OFF) when the relay is energized.
  * Example: Controlling an External Device
  * Warning: Do not attempt to control high-voltage devices without proper knowledge and safety precautions.

* If you want to control a small DC motor or another device:

  * Replace the LED with the device you want to control.
  * Ensure the device's voltage and current requirements are compatible.
  * Provide an appropriate power supply for the device.
  * Connect the device in series with the relay's COM and NO (or NC) terminals.

**Conclusion**

In this lesson, you've learned how to control another circuit using a relay and the Raspberry Pi Pico. By using a transistor to switch the relay coil, you've safely controlled a higher-current circuit without overloading the Pico's GPIO pins. Understanding how to use relays opens up many possibilities for controlling various devices and appliances in your projects.

