.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ar_photoresistor:


2.12 Feel the Light
=====================

In this lesson, we'll learn how to use a **photoresistor** (also known as a light-dependent resistor or LDR) with the Raspberry Pi Pico 2 W to measure light intensity. A photoresistor changes its resistance based on the amount of light it receives: the brighter the light, the lower the resistance. This makes it ideal for detecting changes in ambient light.

* :ref:`cpn_photoresistor`

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
        - :ref:`cpn_photoresistor`
        - 1
        - |link_photoresistor_buy|

**Schematic**

|sch_photoresistor|

In this circuit, a 10K resistor and a photoresistor are connected in series, forming a voltage divider. GP28 reads the voltage across the photoresistor, while the 10K resistor provides protection by limiting current.

* **Bright Light**: The photoresistor's resistance decreases, lowering its voltage and the GP28 reading. In strong light, its resistance approaches zero, and GP28 reads close to 0. At this time, the 10K resistor plays a protective role, so that 3.3V and GND are not connected together, resulting in a short circuit.
* **Darkness**: The photoresistor's resistance increases, raising its voltage and the GP28 value. In complete darkness, its resistance is nearly infinite (the 10K resistor is negligible), and GP28 reads close to 1023.

The calculation formula is shown below.

.. code-block::

  Digital Value = (Analog Voltage/3.3V) * 1023




**Wiring**


|wiring_photoresistor|


**Writing the Code**


.. code-block:: Arduino

   const int sensorPin = 28;   // Photoresistor connected to GP28 (ADC2)

   void setup() {
     Serial.begin(115200);    // Initialize Serial Monitor
   }

   void loop() {
     // Read the analog value from the photoresistor
     int sensorValue = analogRead(sensorPin);
     // Print the sensor value to the Serial Monitor
     Serial.println(sensorValue);
     delay(500);  // Wait half a second before reading again
   }

When the code is running and the Serial Monitor is open:

* Observing the Sensor Values:

  You should see a stream of numbers representing the analog values from the photoresistor.

* Interacting with the Photoresistor:

  * Shine a flashlight or a lamp on the photoresistor. The sensor values should decrease (since resistance decreases with more light).
  * Cover the photoresistor with your hand or place it in a dark area. The sensor values should increase (since resistance increases with less light).

**Understanding the Code**

#. Defining the Sensor Pin:

   Assigns sensorPin to GPIO 28, which is connected to the analog input.

   .. code-block:: arduino

        const int sensorPin = 28;   // Photoresistor connected to GP28 (ADC2)

#. Initializing Serial Communication:

   Starts serial communication, allowing you to print messages to the Serial Monitor.

   .. code-block:: arduino

        Serial.begin(115200);

#. Reading the Analog Value:

   Reads the analog voltage at sensorPin and returns a value between 0 and 1023.

   .. code-block:: arduino

        int sensorValue = analogRead(sensorPin);

#. Printing the Sensor Value:

   Outputs the sensor value to the Serial Monitor.

   .. code-block:: arduino

        Serial.println(sensorValue);

#. Adding a Delay:

   Waits for 500 milliseconds before the next reading.

   .. code-block:: arduino

        delay(500);

**Converting to Voltage**

If you want to see the actual voltage value being read, you can modify the code:

.. code-block:: arduino

   const int sensorPin = 28;   // Photoresistor connected to GP28 (ADC2)

   void setup() {
     Serial.begin(115200);    // Initialize Serial Monitor
   }

    void loop() {
      int sensorValue = analogRead(sensorPin);
      // Convert the analog reading to voltage
      float voltage = sensorValue * (3.3 / 1023.0);
      Serial.print("Sensor Value: ");
      Serial.print(sensorValue);
      Serial.print("  Voltage: ");
      Serial.print(voltage);
      Serial.println(" V");
      delay(500);
    }

**Further Exploration**

* Control an LED Based on Light:

  Use the photoresistor to control the brightness of an LED or turn it on/off based on light levels.

* Data Logging:

  Record the light intensity over time to monitor changes in the environment.

* Build a Night Light:

  Create a light that turns on automatically when it gets dark.

**Conclusion**

In this lesson, you've learned how to use a photoresistor with the Raspberry Pi Pico to measure light intensity. By reading the analog voltage from a voltage divider circuit, you can detect changes in light levels and use this information in your projects.




