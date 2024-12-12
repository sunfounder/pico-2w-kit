.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ar_irremote:


6.4 Using an Infrared Remote Control
==========================================================

In this lesson, we'll learn how to use an **infrared (IR) remote control** and an **IR receiver** with the Raspberry Pi Pico 2w. This will allow us to receive and decode signals from an IR remote, enabling us to control our projects wirelessly.

* :ref:`cpn_ir_receiver`

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
        - :ref:`cpn_ir_receiver`
        - 1
        - |link_receiver_buy|


**Understanding Infrared Communication**

Infrared communication involves transmitting data wirelessly using infrared light. Common household devices like TVs and DVD players use IR remote controls for operation.

* **IR Transmitter (Remote Control):** Emits modulated infrared light when a button is pressed.
* **IR Receiver:** Detects the modulated IR light and converts it into electrical signals that can be decoded.

**Schematic**

|sch_irrecv|

**Wiring**

|wiring_irrecv|


**Writing the Code**

We'll write a program that initializes the IR receiver, listens for incoming IR signals, decodes them, and prints the corresponding button presses to the Serial Monitor.


.. note::

    * You can open the file ``6.4_ir_remote_control.ino`` under the path of ``pico-2w-kit-main/arduino/6.4_ir_remote_control``. 
    * Or copy this code into **Arduino IDE**.
    * Then select the Raspberry Pi Pico board and the correct port before clicking the Upload button.
    * The ``IRremote`` library is used here, you can install it from the **Library Manager**.

      .. image:: img/lib_ir.png

.. code-block:: arduino

    #define SEND_PWM_BY_TIMER

    #include <IRremote.hpp>  // Include the IRremote library

    const int receiverPin = 17;  // Define the pin number for the IR Sensor

    void setup() {
      // Start serial communication at a baud rate of 115200
      Serial.begin(115200);
      // Initialize the IR receiver on the specified pin with LED feedback enabled
      IrReceiver.begin(receiverPin, ENABLE_LED_FEEDBACK);
    }

    void loop() {
      if (IrReceiver.decode()) {  // Check if the IR receiver has received a signal
        bool result = 0;
        String key = decodeKeyValue(IrReceiver.decodedIRData.command);
        if (key != "ERROR") {
          Serial.println(key);  // Print the readable command
          delay(100);
        }
      IrReceiver.resume();  // Prepare the IR receiver to receive the next signal
      }
    }

    // Function to map received IR signals to corresponding keys
    String decodeKeyValue(long result) {
      switch (result) {
        case 0x45: return "POWER";
        case 0x47: return "MUTE";
        case 0x46: return "MODE";
        case 0x44: return "PLAY/PAUSE";
        case 0x40: return "BACKWARD";
        case 0x43: return "FORWARD";
        case 0x7: return "EQ";
        case 0x15: return "-";
        case 0x9: return "+";
        case 0x19: return "CYCLE";
        case 0xD: return "U/SD";
        case 0x16: return "0";
        case 0xC: return "1";
        case 0x18: return "2";
        case 0x5E: return "3";
        case 0x8: return "4";
        case 0x1C: return "5";
        case 0x5A: return "6";
        case 0x42: return "7";
        case 0x52: return "8";
        case 0x4A: return "9";
        case 0x0: return "ERROR";
        default: return "ERROR";
      }
    }

After uploading the code, press buttons on the IR remote control. Observe the corresponding key labels printed in the Serial Monitor.

.. code-block:: arduino

    BACKWARD
    CYCLE
    POWER
    MODE
    EQ
    5
    9

.. note::

  The new remote control may have a plastic piece at the end to isolate the battery. Pull out this plastic piece to activate the remote.


**Understanding the Code**

#. Header and Constants:

   * ``#define SEND_PWM_BY_TIMER``: This line appears to define a macro for sending PWM signals by using a timer. However, it is not used anywhere in the code, so it might be a leftover or a placeholder.
   * ``#include <IRremote.hpp>``: Includes the ``IRremote`` library, which provides functionalities for sending and receiving IR signals.
   * ``const int receiverPin = 17;``: Defines the pin (17) that the IR receiver module is connected to on the Arduino.

#. Setup Function:

   * ``Serial.begin(115200);``: Initializes serial communication at a baud rate of 115200, which allows the Arduino to communicate with a computer for debugging purposes.
   * ``IrReceiver.begin(receiverPin, ENABLE_LED_FEEDBACK);``: Initializes the IR receiver on ``receiverPin`` and enables LED feedback, which will light up an LED when the IR receiver gets a signal.

   .. code-block:: arduino

      void setup() {
        Serial.begin(115200);
        IrReceiver.begin(receiverPin, ENABLE_LED_FEEDBACK);
      }

#. Loop Function: 

   * ``if (IrReceiver.decode())``: Checks if the IR receiver has received a valid IR signal. If it has, the function proceeds to decode it.
   * ``decodeKeyValue(IrReceiver.decodedIRData.command)``: Calls a function to convert the received IR command into a more human-readable key (like "POWER" or "MUTE").
   * ``Serial.println(key);``: Prints the decoded key to the serial monitor.
   * ``delay(100);``: Adds a short delay to avoid printing the same signal multiple times.
   * ``IrReceiver.resume();``: Prepares the IR receiver to receive the next signal by clearing the previous one.

   .. code-block:: arduino

      void loop() {
        if (IrReceiver.decode()) {
          bool result = 0;
          String key = decodeKeyValue(IrReceiver.decodedIRData.command);
          if (key != "ERROR") {
            Serial.println(key);
            delay(100);
          }
          IrReceiver.resume();
        }
      }

#. ``decodeKeyValue`` Function:

   * This function takes a long value result (the raw IR command) and uses a switch statement to map it to a specific key name. Each case corresponds to a different button on the remote.
   * For example, 0x45 maps to "POWER," and 0x47 maps to "MUTE."
   * If the command does not match any known key, the function returns "ERROR."

   .. code-block:: arduino

      String decodeKeyValue(long result) {
        switch (result) {
          case 0x45: return "POWER";
          case 0x47: return "MUTE";
          case 0x46: return "MODE";
          ...
          case 0x4A: return "9";
          case 0x0: return "ERROR";
          default: return "ERROR";
        }
      }

**Troubleshooting**

* No Readings Displayed:

  * Ensure the IR receiver is properly connected to GPIO 17.
  * Verify that the IR receiver is receiving power (VCC and GND connections).
  * Check that the correct GPIO pin is defined in the code (``receiverPin``).

* Incorrect Readings:

  * Confirm that the remote control is compatible with the IR receiver.
  * Check that the ``decodeKeyValue`` function correctly maps the IR codes from your specific remote.
  * Use a universal remote to ensure compatibility.

* Unknown Commands:

  * Update the ``decodeKeyValue`` function to include the IR codes specific to your remote control.
  * Use an IR decoding tool or reference to find the correct codes emitted by your remote.

* Signal Interference:

  * Ensure there are no obstructions between the remote and the IR receiver.
  * Avoid placing the sensor near other IR-emitting devices that might cause interference.

**Further Exploration**

* Controlling Devices with IR Signals:

  Use decoded IR signals to control LEDs, motors, servos, or other actuators based on remote inputs.

* Creating a Universal Remote:

  Expand the ``decodeKeyValue()`` function to support multiple remotes by mapping a broader range of IR codes.

* Adding Feedback Mechanisms:

  Implement LCD or OLED displays to show the current state or received commands.

**Conclusion**

In this lesson, you've learned how to use an infrared (IR) remote control and an IR receiver with the Raspberry Pi Pico to receive and decode IR signals. By integrating the IRremote library, you can easily interpret remote control inputs and use them to interact with your projects wirelessly. This setup is foundational for creating remote-controlled devices, automated systems, and user-friendly interfaces in various applications.

