.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ar_pot:

2.11 Turn the Knob
==========================

In this lesson, we'll explore how to read analog input using the Raspberry Pi Pico 2w's built-in Analog-to-Digital Converter (ADC) and use that input to control the brightness of an LED. Specifically, we'll use a potentiometer—a variable resistor—as an analog input device. By turning the knob of the potentiometer, we'll adjust the voltage level read by the Pico, which we'll then use to control the LED's brightness via Pulse Width Modulation (PWM).


**Understanding Analog Input**

So far, we've worked with digital inputs and outputs, which are either ON (high voltage) or OFF (low voltage). However, many real-world signals are analog, meaning they can vary continuously over a range of values. Examples include light intensity, temperature, and sound levels.

The Raspberry Pi Pico 2 has a built-in ADC that allows it to read analog voltages and convert them into digital values that can be processed in code.

The ADC converts the analog voltage from the potentiometer into a digital value using the formula:

.. code-block::

  Digital Value = (Analog Voltage/3.3V) * 1023


**Pico's ADC Pins**

|pin_adc|

The Pico has three GPIO pins that can be used for analog input:

* **GP26** (ADC0)
* **GP27** (ADC1)
* **GP28** (ADC2)

In addition, there's a fourth ADC channel connected internally to a temperature sensor (ADC4), which we'll explore in later lessons.


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
        - 1(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 7
        - :ref:`cpn_potentiometer`
        - 1
        - |link_potentiometer_buy|

**Schematic**

|sch_pot|


**Wiring**

|wiring_pot|

**Code**


.. note::

    * You can open the file ``2.11_turn_the_knob.ino`` under the path of ``pico-2w-starter-kit-main/arduino/2.11_turn_the_knob``. 
    * Or copy this code into **Arduino IDE**.
    * Don't forget to select the board(Raspberry Pi Pico) and the correct port before clicking the **Upload** button.



.. code-block:: Arduino

   // Define the pins
   const int potPin = 28;   // Potentiometer connected to GP28 (ADC2)
   const int ledPin = 15;   // LED connected to GP15 (PWM capable)

   void setup() {
     // Initialize serial communication for debugging
     Serial.begin(115200);
     // Set up the LED pin as output
     pinMode(ledPin, OUTPUT);
   }

   void loop() {
     // Read the analog value from the potentiometer (0-1023)
     int sensorValue = analogRead(potPin);
     // Print the sensor value for debugging
     Serial.println(sensorValue);

     // Map the sensor value to a PWM value (0-255)
     int brightness = map(sensorValue, 0, 1023, 0, 255);
     // Set the brightness of the LED
     analogWrite(ledPin, brightness);

     // Small delay for stability
     delay(10);
   }

When the code is running and the Serial Monitor is open:

* As you turn the potentiometer knob, the brightness of the LED should change smoothly from dim to bright.
* You should see the analog values printed, ranging from approximately 0 to 1023 as you adjust the potentiometer.

**Understanding the Code**

#. Defining the Pins:

   Assigns the GPIO pins used for the potentiometer and the LED.

   .. code-block:: Arduino

        const int potPin = 28;   // Potentiometer connected to GP28 (ADC2)
        const int ledPin = 15;   // LED connected to GP15 (PWM capable)

#. Initializing Serial Communication:

   Starts serial communication, allowing you to print messages to the Serial Monitor.

   .. code-block:: Arduino

        Serial.begin(115200);

#. Reading the Analog Value:

   Reads the analog voltage on potPin (GP28) and returns a value between 0 and 1023.

   .. code-block:: Arduino

        int sensorValue = analogRead(potPin);

#. Printing the Sensor Value:

   Prints the current sensor value to the Serial Monitor for debugging purposes.

   .. code-block:: Arduino

        Serial.println(sensorValue);

#. Mapping the Sensor Value:

   Converts the sensor value (0-1023) to a brightness value suitable for PWM output (0-255).

   .. code-block:: Arduino

        int brightness = map(sensorValue, 0, 1023, 0, 255);

#. Setting the LED Brightness:

   Adjusts the brightness of the LED by setting the PWM duty cycle on ledPin (GP15).

   .. code-block:: Arduino

        analogWrite(ledPin, brightness);

#. Adding a Small Delay:

   A short delay to stabilize the readings and prevent the loop from running too fast.

   .. code-block:: Arduino

        delay(10);

**Further Exploration**

* **Display Voltage**: Modify the code to calculate and display the actual voltage read from the potentiometer.

  .. code-block:: Arduino

        // Define the pins
        const int potPin = 28;  // Potentiometer connected to GP28 (ADC2)
        const int ledPin = 15;  // LED connected to GP15 (PWM capable)
        
        void setup() {
          // Initialize serial communication for debugging
          Serial.begin(115200);
          // Set up the LED pin as output
          pinMode(ledPin, OUTPUT);
        }
        
        void loop() {
          // Read the analog value from the potentiometer (0-1023)
          int sensorValue = analogRead(potPin);
        
          // Print the sensor value for debugging
          Serial.println(sensorValue);
        
          // Calculate and display the actual voltage
          float voltage = sensorValue * (3.3 / 1023.0);
          Serial.print("Voltage: ");
          Serial.print(voltage);
          Serial.println(" V");
        
          // Map the sensor value to a PWM value (0-255)
          int brightness = map(sensorValue, 0, 1023, 0, 255);
          // Set the brightness of the LED
          analogWrite(ledPin, brightness);
        
          // Small delay for stability
          delay(10);
        }

* **Control Multiple LEDs**: Use multiple potentiometers to control different LEDs or colors in an RGB LED.
* **Use with Other Sensors**: Replace the potentiometer with another analog sensor, such as a light-dependent resistor (LDR), to control the LED based on ambient light.


**Explanation of Concepts**

* Analog-to-Digital Conversion (ADC):

  * The ADC on the Pico converts the analog voltage from the potentiometer into a digital value.
  * The voltage range from 0V to 3.3V is converted into a numerical value between 0 and 1023.

* Pulse Width Modulation (PWM):

  * PWM is a technique used to simulate an analog voltage by rapidly switching a digital pin between HIGH and LOW states.
  * By adjusting the proportion of time the signal is HIGH (duty cycle), we can control devices like LEDs and motors.

* Mapping Values:

  * The ``map()`` function scales one range of values to another.
  * In this case, we map the potentiometer's 0-1023 range to the PWM's 0-255 range.

**Conclusion**

In this lesson, you've learned how to read analog input from a potentiometer using the Raspberry Pi Pico's ADC and use that input to control the brightness of an LED via PWM. This fundamental skill allows you to interface with a variety of analog sensors and control outputs in a proportional manner.


