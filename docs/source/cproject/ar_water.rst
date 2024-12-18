.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ar_water:

2.14 Water Level Detection
============================

In this lesson, we will learn how to use a **water sensor** with the Raspberry Pi Pico 2 W to detect the presence of water or measure the water level. This sensor is commonly used in projects related to rainfall detection, water level monitoring, and liquid leakage alerts.

**How the Water Sensor Works**

The water sensor has a series of exposed parallel wire traces that detect water droplets or measure the volume of water. As water comes into contact with these traces, the sensor outputs an analog signal. The more water that comes into contact with the sensor, the higher the output value, which can be read by the Raspberry Pi Pico 2's analog-to-digital converter (ADC).

|img_water_sensor|

* Do not fully submerge the sensor in water. Only the area with the exposed traces should come into contact with water.
* Using the sensor in a humid environment while powered may cause the probe to corrode faster, so it is recommended to power the sensor only when taking readings.

* :ref:`cpn_water_level`

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
        - :ref:`cpn_water_level`
        - 1
        - 

**Schematic**

|sch_water|


**Wiring**

|wiring_water|

**Code**

.. note::

    * You can open the file ``2.14_feel_the_water_level.ino`` under the path of ``pico-2 w-kit-main/arduino/2.14_feel_the_water_level``. 
    * Or copy this code into **Arduino IDE**.
    * Don't forget to select the board(Raspberry Pi Pico) and the correct port before clicking the **Upload** button.


.. code-block:: arduino

   const int waterSensorPin = 28;  // Water sensor connected to GP28 (ADC2)

   void setup() {
     Serial.begin(115200);  // Initialize Serial Monitor
   }

   void loop() {
     // Read the analog value from the water sensor
     int sensorValue = analogRead(waterSensorPin);
     // Print the sensor value to the Serial Monitor
     Serial.print("Water Sensor Value: ");
     Serial.println(sensorValue);
     delay(500);  // Wait half a second before reading again
   }

After uploading the code, open the Serial Monitor and you should see a stream of numbers representing the analog values from the water sensor.

* The sensor values should be low (close to 0) when the sensor is dry.
* Gently dip the sensor into water, starting from the bottom. As more of the sensor's traces are submerged, the sensor values should increase.

**Understanding the Code**

#. Defining the Sensor Pin:

   Assigns ``waterSensorPin`` to GPIO 28, which is connected to the analog input.

   .. code-block:: arduino

      const int waterSensorPin = 28;  // Water sensor connected to GP28 (ADC2)


#. Initializing Serial Communication:

   Starts serial communication, allowing you to print messages to the Serial Monitor.

   .. code-block:: arduino

      Serial.begin(115200);

#. Reading the Analog Value:

   Reads the analog voltage at ``waterSensorPin`` and returns a value between 0 and 1023 (for 10-bit ADC).

   .. code-block:: arduino

      int sensorValue = analogRead(waterSensorPin);

#. Printing the Sensor Value:

   Outputs the sensor value to the Serial Monitor.

   .. code-block:: arduino

      Serial.print("Water Sensor Value: ");
      Serial.println(sensorValue);

#. Adding a Delay:

   Waits for 500 milliseconds before the next reading.

   .. code-block:: arduino

      delay(500);


**Using the Water Sensor as a Digital Sensor**

You can use the analog input module as a digital sensor by setting a threshold value.

* Determine the Threshold:

  * Read the sensor value when the sensor is dry.
  * Use this value as a baseline (e.g., if the dry value is around 100).

* Modify the Code:

   .. code-block:: arduino

      const int waterSensorPin = 28;  // Water sensor connected to GP28 (ADC2)
      const int threshold = 500;      // Set a threshold value

      void setup() {
        Serial.begin(115200);  // Initialize Serial Monitor
      }

      void loop() {
        // Read the analog value from the water sensor
        int sensorValue = analogRead(waterSensorPin);

        // Check if the sensor value exceeds the threshold
        if (sensorValue > threshold) {
          Serial.println("Water Detected!");
        } else {
          Serial.println("No Water Detected.");
        }
        delay(500);  // Wait half a second before reading again
      }

Place the sensor near a potential water leak area.
When water comes into contact with the sensor, the Serial Monitor should display "Water Detected!"

**Safety Precautions**

* Avoid Short Circuits:

  * Ensure that the connections are secure and that the sensor is not submerged beyond the exposed traces.
  * Do not allow water to contact the Pico or any other electronic components.

* Corrosion Prevention:

  * Do not leave the sensor powered while submerged for extended periods.
  * Dry the sensor thoroughly after use to prevent corrosion.


**Further Exploration**

* Water Level Alarm:

  Add a buzzer or LED to alert when water is detected.

* Automated Pump Control:

  Use the sensor to control a pump, turning it on or off based on water levels.

* Data Logging:

  Record water level changes over time for analysis.

**Conclusion**

In this lesson, you've learned how to use a water sensor with the Raspberry Pi Pico to detect water presence or measure water level. By reading the analog values from the sensor, you can monitor changes in water levels and respond accordingly in your projects.
