.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ar_temp:

2.13 Thermometer
===========================

In this lesson, we'll learn how to use a **thermistor** with the Raspberry Pi Pico 2w to measure temperature. A thermistor is a type of resistor whose resistance varies significantly with temperature. Specifically, we'll use a Negative Temperature Coefficient (NTC) thermistor, which decreases its resistance as the temperature increases.

* :ref:`cpn_thermistor`


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
        - :ref:`cpn_thermistor`
        - 1
        - |link_thermistor_buy|


**Understanding the Thermistor**

An NTC thermistor is a temperature-sensitive resistor. Its resistance decreases as the temperature rises. By incorporating it into a voltage divider circuit, we can measure the voltage across it, which changes with temperature. Using the Raspberry Pi Pico 2w's analog-to-digital converter (ADC), we can read this voltage and calculate the corresponding temperature.

**Schematic**

|sch_temp|

In this circuit, a 10K resistor and an NTC thermistor form a voltage divider, with GP28 reading the voltage across the thermistor. The 10K resistor also provides protection by limiting current.

* **High Temperature**: The thermistor's resistance decreases, lowering its voltage and the GP28 reading. At high enough temperatures, resistance approaches zero, and GP28 reads close to 0.
* **Low Temperature**: The thermistor's resistance increases, raising its voltage and the GP28 value. In extreme cold, resistance becomes nearly infinite, and GP28 reads close to 1023.

The 10K resistor ensures 3.3V and GND are not directly connected, preventing a short circuit.



**Wiring**


|wiring_temp|
 
.. #. Connect 3V3 and GND of Pico 2W to the power bus of the breadboard.
.. #. Connect one lead of the thermistor to the GP28 pin, then connect the same lead to the positive power bus with a 10K ohm resistor.
.. #. Connect another lead of thermistor to the negative power bus.


**Writing the Code**

.. note::

    * You can open the file ``2.13_thermometer.ino`` under the path of ``pico-2w-starter-kit-main/arduino/2.13_thermometer``. 
    * Or copy this code into **Arduino IDE**.
    * Don't forget to select the board(Raspberry Pi Pico) and the correct port before clicking the **Upload** button.



.. code-block:: arduino

    // Define the pins
    const int thermistorPin = 28;  // Thermistor connected to GP28 (ADC2)

    // Constants for the thermistor and calculations
    const float BETA = 3950;       // Beta value of the thermistor (provided by manufacturer)
    const float SERIES_RESISTOR = 10000; // 10KΩ resistor
    const float NOMINAL_RESISTANCE = 10000; // Resistance at 25°C (provided by manufacturer)
    const float NOMINAL_TEMPERATURE = 25.0; // 25°C in Celsius

    void setup() {
      Serial.begin(115200);  // Initialize Serial Monitor
    }

    void loop() {
      // Read the analog value from the thermistor
      int adcValue = analogRead(thermistorPin);
      // Convert the ADC value to voltage
      float voltage = adcValue * (3.3 / 1023.0);
      // Calculate the resistance of the thermistor
      float resistance = (voltage * SERIES_RESISTOR) / (3.3-voltage);
      // Calculate the temperature in Kelvin using the Beta formula
      float temperatureK = 1 / ( (1 / (NOMINAL_TEMPERATURE + 273.15)) + (1 / BETA) * log(resistance / NOMINAL_RESISTANCE) );
      // Convert Kelvin to Celsius
      float temperatureC = temperatureK - 273.15;
      // Convert Celsius to Fahrenheit
      float temperatureF = (temperatureC * 9.0 / 5.0) + 32.0;

      // Print the temperature readings
      Serial.print("Temperature: ");
      Serial.print(temperatureC);
      Serial.print(" °C, ");
      Serial.print(temperatureF);
      Serial.println(" °F");

      delay(1000);  // Wait a second before the next reading
    }

When the code is running and the Serial Monitor is open:

* You should see the temperature readings in Celsius and Fahrenheit.
* Gently hold the thermistor between your fingers. The temperature reading should increase as the thermistor warms up.
* Blow cool air over the thermistor or place a cold object near it. The temperature reading should decrease.

**Understanding the Code**

#. Defining the Pins and Constants:

   Assigns the GPIO pin used for reading the thermistor.

   .. code-block:: arduino

        const int thermistorPin = 28;  // Thermistor connected to GP28 (ADC2)

#. Constants for Calculations:

   These constants are used in the calculations to determine the temperature.

   .. code-block:: arduino

        const float BETA = 3950;       // Beta value of the thermistor
        const float SERIES_RESISTOR = 10000; // 10KΩ resistor
        const float NOMINAL_RESISTANCE = 10000; // Resistance at 25°C
        const float NOMINAL_TEMPERATURE = 25.0; // 25°C in Celsius

#. Reading the Analog Value:

   Reads the analog voltage at thermistorPin and returns a value between 0 and 1023.

   .. code-block:: arduino

        int adcValue = analogRead(thermistorPin);

#. Calculating the Voltage:

   Converts the ADC value to the actual voltage.

   .. code-block:: arduino

        float voltage = adcValue * (3.3 / 1023.0);

#. Calculating the Thermistor Resistance:

   Uses the voltage divider formula to calculate the resistance of the thermistor.

   .. code-block:: arduino

        float resistance = (voltage * SERIES_RESISTOR) / (3.3-voltage);

#. Calculating the Temperature:

   .. code-block:: arduino

        float temperatureK = 1 / ( (1 / (NOMINAL_TEMPERATURE + 273.15)) + (1 / BETA) * log(resistance / NOMINAL_RESISTANCE) );
        float temperatureC = temperatureK - 273.15;
        float temperatureF = (temperatureC * 9.0 / 5.0) + 32.0;

#. Printing the Temperature:

   Outputs the temperature in Celsius and Fahrenheit to the Serial Monitor.

   .. code-block:: arduino

        Serial.print("Temperature: ");
        Serial.print(temperatureC);
        Serial.print(" °C, ");
        Serial.print(temperatureF);
        Serial.println(" °F");

#. Delay:

   Waits for one second before taking the next reading.

   .. code-block:: arduino

        delay(1000);

**Understanding the Temperature Calculation**

* Steinhart-Hart Equation:

The Steinhart-Hart equation provides a model of the thermistor's resistance as a function of temperature:

|temp_format|

* ``T`` is the temperature of the thermistor in Kelvin.
* ``T0`` is a reference temperature, usually at 25°C (which is 273.15 + 25 in Kelvin).
* ``B`` is the beta parameter of the material, the beta coefficient of the NTC thermistor used in this kit is 3950.
* ``R`` is the resistance we measure.
* ``R0`` is the resistance at the reference temperature T0, the resistance of the NTC thermistor in this kit at 25°C is 10 kilohms.

**Note on Accuracy**

* Thermistors are nonlinear devices, and the Beta equation provides an approximation.
* For more accurate temperature measurements over a wider range, the Steinhart-Hart equation can be used.
* Calibration may be necessary for precise applications.

**Further Exploration**

* Display Temperature on an LCD:

  Connect an LCD display to show the temperature readings without a computer.

* Data Logging:

  Record temperature readings over time to monitor environmental changes.

* Temperature-Controlled Devices:

  Use the temperature readings to control a fan or heater.

**Conclusion**

In this lesson, you've learned how to use a thermistor with the Raspberry Pi Pico to measure temperature. By creating a voltage divider and using the Beta equation, you've been able to read analog values, calculate resistance, and determine the temperature in both Celsius and Fahrenheit.


