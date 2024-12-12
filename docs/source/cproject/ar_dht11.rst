.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ar_dht11:


6.2 Measuring Temperature and Humidity with DHT11
=======================================================

In this lesson, we'll learn how to use a **DHT11 temperature and humidity sensor** with the Raspberry Pi Pico 2w. The DHT11 is a basic, low-cost digital sensor that can measure ambient temperature and humidity, providing a calibrated digital output.

|img_Dht11|

* :ref:`cpn_dht11`

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
        - :ref:`cpn_dht11`
        - 1
        - |link_dht22_buy|

**Understanding the DHT11 Sensor**

The **DHT11** sensor uses a capacitive humidity sensor and a thermistor to measure the surrounding air. It outputs a digital signal on the data pin, and it's fairly simple to use, but requires precise timing to read data.

* Temperature Range: 0–50 °C with ±2 °C accuracy
* Humidity Range: 20–80% RH with ±5% accuracy
* Sampling Rate: 1 Hz (once every second)

**Schematic**

|sch_dht11|

**Wiring**

|wiring_dht11|


**Writing the Code**

We'll write a program that reads temperature and humidity data from the DHT11 sensor and prints the values to the Serial Monitor.


.. note::

    * You can open the file ``6.2_dht11.ino`` under the path of ``pico-2w-starter-kit-main/arduino/6.2_dht11``. 
    * Or copy this code into **Arduino IDE**.
    * Then select the Raspberry Pi Pico board and the correct port before clicking the Upload button.
    * The ``DHT sensor library`` library is used here, you can install it from the **Library Manager**.

      .. image:: img/lib_dht.png



.. code-block:: arduino

    #include <DHT.h>

    // Define the connection pins
    #define DHTPIN 16       // GPIO 16 -> Data pin of DHT11
    #define DHTTYPE DHT11    // Define the sensor type

    // Create a DHT object
    DHT dht(DHTPIN, DHTTYPE);

    unsigned long previousMillis = 0; // Stores the last time the display was updated
    const long interval = 2000;        // Interval at which to read sensor (milliseconds)

    void setup() {
      // Initialize serial communication at 115200 baud
      Serial.begin(115200);
      Serial.println(F("DHT11 Sensor Test!"));
    
      // Initialize the DHT sensor
      dht.begin();
   
    }

    void loop() {
      unsigned long currentMillis = millis();

      // Update the sensor reading every 'interval' milliseconds
      if (currentMillis - previousMillis >= interval) {
        previousMillis = currentMillis;

        // Read humidity and temperature
        float humidity = dht.readHumidity();
        float temperatureC = dht.readTemperature();
        float temperatureF = dht.readTemperature(true);

        // Check if any reads failed
        if (isnan(humidity) || isnan(temperatureC) || isnan(temperatureF)) {
          Serial.println(F("Failed to read from DHT sensor!"));
          return;
        }

        // Calculate heat index
        float heatIndexC = dht.computeHeatIndex(temperatureC, humidity, false);
        float heatIndexF = dht.computeHeatIndex(temperatureF, humidity);

        // Print the results to the Serial Monitor
        Serial.print(F("Humidity: "));
        Serial.print(humidity);
        Serial.print(F("%  Temperature: "));
        Serial.print(temperatureC);
        Serial.print(F("°C "));
        Serial.print(temperatureF);
        Serial.print(F("°F  Heat index: "));
        Serial.print(heatIndexC);
        Serial.print(F("°C "));
        Serial.print(heatIndexF);
        Serial.println(F("°F"));
      }
    }

After uploading the code, the Serial Monitor should display the temperature and humidity readings every two seconds.

.. code-block::

    DHT11 Sensor Test!
    Humidity: 45.00%  Temperature: 25.00°C 77.00°F  Heat index: 25.00°C 77.00°F
    Humidity: 46.00%  Temperature: 25.50°C 78.00°F  Heat index: 25.50°C 78.00°F
    Humidity: 47.00%  Temperature: 26.00°C 79.00°F  Heat index: 26.00°C 79.00°F

* **Humidity**: Expose the sensor to different humidity levels to see changes in readings.
* **Temperature**: Change the temperature around the sensor to observe temperature measurements.

**Understanding the Code**

#. Including Libraries and Defining Constants:

   * ``DHT.h``: Includes the DHT sensor library to simplify interactions with the sensor.
   * ``DHTPIN``: Specifies the GPIO pin connected to the DHT11 data pin.
   * ``DHTTYPE``: Defines the type of DHT sensor being used (DHT11 in this case).

   .. code-block:: arduino

        #include <DHT.h>
        #define DHTPIN 16       // GPIO 16 -> Data pin of DHT11
        #define DHTTYPE DHT11    // Define the sensor type

#. Creating the ``DHT`` Object:

   Initializes a ``DHT`` object with the specified data pin and sensor type.

   .. code-block:: arduino

        DHT dht(DHTPIN, DHTTYPE);

#. Setup Function:

   * **Serial Communication**: Starts serial communication for debugging and data display.
   * **DHT Sensor Initialization**: Prepares the DHT11 sensor for data reading.

   .. code-block:: arduino

        void setup() {
          // Initialize serial communication at 115200 baud
          Serial.begin(115200);
          Serial.println(F("DHT11 Sensor Test!"));

          // Initialize the DHT sensor
          dht.begin();
        }

#. Loop Function:

   * Timing with ``millis()``: 
   
     Uses non-blocking timing to read the sensor every 2 seconds (interval = 2000 milliseconds).
   
     .. code-block:: arduino
   
        if (currentMillis - previousMillis >= interval) {
          previousMillis = currentMillis;
          ...
        }
   
   * Reading Sensor Data:
   
     * ``dht.readHumidity()``: Reads the current humidity.
     * ``dht.readTemperature()``: Reads the current temperature in Celsius.
     * ``dht.readTemperature(true)``: Reads the current temperature in Fahrenheit.
   
   * Error Handling:
   
     Checks if any of the readings failed (returned NaN) and prints an error message if so.
   
     .. code-block:: arduino
   
        if (isnan(humidity) || isnan(temperatureC) || isnan(temperatureF)) {
          Serial.println(F("Failed to read from DHT sensor!"));
          return;
        }
   
   * Calculating Heat Index:
   
     * ``dht.computeHeatIndex(temperatureC, humidity, false)``: Calculates the heat index in Celsius.
     * ``dht.computeHeatIndex(temperatureF, humidity)``: Calculates the heat index in Fahrenheit.
   
   * Displaying Data:
   
     Prints humidity, temperature in Celsius and Fahrenheit, and heat index to the Serial Monitor.
   
     .. code-block:: arduino
   
        Serial.print(F("Humidity: "));
        Serial.print(humidity);
        Serial.print(F("%  Temperature: "));
        Serial.print(temperatureC);
        Serial.print(F("°C "));
        Serial.print(temperatureF);
        Serial.print(F("°F  Heat index: "));
        Serial.print(heatIndexC);
        Serial.print(F("°C "));
        Serial.print(heatIndexF);
        Serial.println(F("°F"));

**Troubleshooting**

* No Readings Displayed:

  * Check all wiring connections.
  * Ensure the DHT11 sensor is receiving power.
  * Verify that the correct GPIO pins are defined in the code.

* Incorrect Readings:

  * Verify that the DHT11 sensor is not damaged.
  * Check the sensor's datasheet for proper timing and signal requirements.

* Sensor Interference:

  * Avoid placing the sensor near other electronic devices that might cause interference.
  * Ensure there are no obstacles blocking the sensor's line of sight.

**Further Exploration**

* Integrating with Displays:

  Connect an LCD or OLED display to show temperature and humidity readings without using the Serial Monitor.

* Creating Alerts:

  Implement buzzer or notification systems that trigger when temperature or humidity exceeds certain thresholds.

* Combining with Other Sensors:

  Pair the DHT11 with motion sensors, light sensors, or other environmental sensors to create comprehensive monitoring systems.

* Building a Weather Station:

  Expand the project by adding additional sensors like barometric pressure sensors, rain gauges, and wind speed sensors to build a full-fledged weather station.

**Conclusion**

In this lesson, you've learned how to use a DHT11 temperature and humidity sensor with the Raspberry Pi Pico to measure and display ambient temperature and humidity levels. By leveraging the DHT library, you can easily integrate environmental sensing into your projects. The optional LED indicator provides a simple way to add visual feedback based on sensor readings, enhancing the interactivity of your system.
