.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ar_pir:

2.10 Detect Human Movement
==========================

In this lesson, we'll learn how to use a Passive Infrared (PIR) sensor with the Raspberry Pi Pico 2w to detect human movement. PIR sensors are commonly used in security systems, automatic lighting, and other applications where motion detection is required. They detect infrared radiation emitted by warm objects, such as humans or animals, in their field of view.

:ref:`cpn_pir`

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
        - :ref:`cpn_pir`
        - 1
        - |link_pir_buy|


**Schematic**

|sch_pir|

When the PIR module detects someone passing by, GP14 will be high, otherwise it will be low.

.. note::

    The PIR sensor have two potentiometers:

    * **Sensitivity Adjustment**: Controls the range of detection.
    * **Time Delay Adjustment**: Controls how long the output remains HIGH after motion is detected.

    For initial testing, turn both potentiometers counterclockwise to their minimum positions. This sets the sensor to its most sensitive and shortest delay settings, allowing you to observe immediate responses.


    |img_PIR_TTE|

**Wiring**

|wiring_pir|

**Writing the Code**

.. note::

    * You can open the file ``2.10_detect_human_movement.ino`` under the path of ``pico-2w-kit-main/arduino/2.10_detect_human_movement``. 
    * Or copy this code into **Arduino IDE**.
    * Don't forget to select the board(Raspberry Pi Pico) and the correct port before clicking the **Upload** button.



.. code-block:: python

   const int pirPin = 14;     // PIR sensor output pin connected to GP14
   int pirState = LOW;        // Current state of PIR sensor
   int val = 0;               // Variable to store the PIR reading

   void setup() {
     Serial.begin(115200);    // Initialize Serial Monitor
     pinMode(pirPin, INPUT);  // Set the PIR pin as input
     Serial.println("PIR Sensor Test");
     delay(2000);             // Allow the PIR sensor to stabilize
   }

   void loop() {
     val = digitalRead(pirPin);  // Read the PIR sensor

     if (val == HIGH) {
       if (pirState == LOW) {
         Serial.println("Motion detected!");
         pirState = HIGH;
       }
     } else {
       if (pirState == HIGH) {
         Serial.println("Motion ended!");
         pirState = LOW;
       }
     }
     delay(500);  // Wait half a second before checking again
   }

When the code is running and the Serial Monitor is open:

* Move in front of the PIR sensor. The Serial Monitor should display "Motion detected!"
* Stop moving or move out of the sensor's range. After a short delay, the Serial Monitor should display "Motion ended!"

**Understanding the Code**

#. Reading the PIR Sensor:

   Reads the current state of the PIR sensor. It will be HIGH when motion is detected and LOW when no motion is detected.

   .. code-block:: Arduino

      val = digitalRead(pirPin);

#. Detecting Motion:

   * When motion is detected, and it's the first detection, it prints "Motion detected!" and updates pirState.
   * When motion ends, it prints "Motion ended!" and updates pirState.
  
   .. code-block:: Arduino

      if (val == HIGH) {
        if (pirState == LOW) {
          Serial.println("Motion detected!");
          pirState = HIGH;
        }
      } else {
        if (pirState == HIGH) {
          Serial.println("Motion ended!");
          pirState = LOW;
        }
      }


**Practical Applications**

* **Security Systems**: Detect intruders or unauthorized movement.
* **Automatic Lighting**: Turn lights on when motion is detected.
* **Energy Saving**: Power down devices when no movement is detected for a period.

**Troubleshooting Tips**

* False Triggers:

  * PIR sensors can be sensitive to environmental factors like temperature changes or sunlight.
  * Avoid pointing the sensor directly at heat sources or windows.

* Sensor Not Detecting Motion:

  * Ensure the sensor has had time to initialize (some sensors require up to 60 seconds).
  * Adjust the sensitivity potentiometer.

* Interference: 

  * Keep the sensor away from electronics that may cause electromagnetic interference.

**Conclusion**

In this lesson, you've learned how to use a PIR sensor with the Raspberry Pi Pico to detect human movement. You've set up the hardware, written code to read the sensor's output, and tested it to respond to motion. Understanding how to adjust the PIR sensor's settings allows you to tailor it to your specific application, whether it's for security, automation, or interactive projects.

