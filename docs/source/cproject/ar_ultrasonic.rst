.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ar_ultrasonic:

6.1 Measuring Distance with an Ultrasonic Sensor
================================================

In this lesson, we'll learn how to use an **ultrasonic sensor module** with the Raspberry Pi Pico 2w to measure the distance to an object. Ultrasonic sensors are commonly used in robotics and automation systems for object detection and distance measurement.

* :ref:`cpn_ultrasonic`

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
        - :ref:`cpn_ultrasonic`
        - 1
        - |link_ultrasonic_buy|

**Understanding the Ultrasonic Sensor**

The ultrasonic sensor works by emitting a short ultrasonic pulse from the **Trig** pin and listening for the echo on the **Echo** pin. By measuring the time it takes for the echo to return, we can calculate the distance to an object using the speed of sound.

|ultrasonic_prin|

* **Trigger Pulse**: A 10-microsecond high pulse on the Trig pin initiates the measurement.
* **Ultrasonic Burst**: The sensor emits an 8-cycle ultrasonic burst at 40 kHz.
* **Echo Reception**: The Echo pin goes high, and stays high until the echo is received back.
* **Time Measurement**: By measuring the time the Echo pin stays high, we can calculate the distance.

**Schematic**

|sch_ultrasonic|

**Wiring**

|wiring_ultrasonic|

**Writing the Code**

We'll write a program that triggers the ultrasonic sensor, measures the echo time, and calculates the distance to an object. The distance will be printed to the Serial Monitor.

.. note::

    * You can open the file ``6.1_ultrasonic.ino`` under the path of ``pico-2w-starter-kit-main/arduino/6.1_ultrasonic``. 
    * Or copy this code into **Arduino IDE**.
    * Don't forget to select the board(Raspberry Pi Pico) and the correct port before clicking the **Upload** button.


.. code-block:: arduino

    // Define the connection pins
    const int trigPin = 17;  // GPIO 17 -> Trig
    const int echoPin = 16;  // GPIO 16 -> Echo

    void setup() {
      // Initialize serial communication at 115200 baud
      Serial.begin(115200);
    
      // Initialize the sensor pins
      pinMode(trigPin, OUTPUT);
      pinMode(echoPin, INPUT);
    }

    void loop() {
      long duration;
      float distance;

      // Trigger the sensor by setting Trig HIGH for 10 microseconds
      digitalWrite(trigPin, HIGH);
      delayMicroseconds(10);
      digitalWrite(trigPin, LOW);
    
      // Read the Echo pin, returns the duration in microseconds
      duration = pulseIn(echoPin, HIGH);
    
      // Calculate the distance in centimeters
      distance = duration * 0.034 / 2;
    
      // Print the distance to the Serial Monitor
      Serial.print("Distance: ");
      Serial.print(distance);
      Serial.println(" cm");
    
      delay(500); // Wait for half a second before the next measurement
    }

After uploading the code, the Serial Monitor should display the distance measurements in centimeters.

.. code-block::

    Distance: 25.3 cm
    Distance: 24.8 cm
    Distance: 24.5 cm

Place an object at varying distances from the sensor.
Move the object closer and farther to observe changes in the distance readings.

**Understanding the Code**

#. Defining Connection Pins:

   * ``trigPin``: Sends the ultrasonic pulse.
   * ``echoPin``: Receives the echo of the ultrasonic pulse.

   .. code-block:: arduino

        const int trigPin = 17;  // GPIO 17 -> Trig
        const int echoPin = 16;  // GPIO 16 -> Echo

#. Setup Function:

   * **Serial Communication**: Enables communication between the Pico and the computer for debugging.
   * **Pin Modes**: Sets the ``Trig`` pin as ``OUTPUT`` and the ``Echo`` pin as ``INPUT``.

   .. code-block:: arduino

        void setup() {
          // Initialize serial communication at 115200 baud
          Serial.begin(115200);

          // Initialize the sensor pins
          pinMode(trigPin, OUTPUT);
          pinMode(echoPin, INPUT);
        }

#. Loop Function:

   * **Triggering the Sensor**: Sets the ``Trig`` pin ``HIGH`` for 10 microseconds to send the ultrasonic pulse. Sets the ``Trig`` pin ``LOW`` to end the pulse.

     .. code-block:: arduino

        digitalWrite(trigPin, HIGH);
        delayMicroseconds(10);
        digitalWrite(trigPin, LOW);

   * **Reading the Echo**: Measures the duration (in microseconds) that the ``Echo`` pin stays ``HIGH``, indicating the time taken for the echo to return.

     .. code-block:: arduino

        duration = pulseIn(echoPin, HIGH);

   * **Calculating Distance**: Converts the time to distance (cm/microsecond). Divides by 2 to account for the round-trip of the pulse.

     .. code-block:: arduino

        distance = duration * 0.034 / 2;

   * **Serial Output**: Prints the calculated distance to the Serial Monitor for real-time monitoring.

     .. code-block:: arduino

        Serial.print("Distance: ");
        Serial.print(distance);
        Serial.println(" cm");

   * **Delay**: Adds a 500-millisecond delay to prevent flooding the Serial Monitor and to allow time between measurements.

**Troubleshooting**

* No Readings Displayed:

  * Ensure the Trig and Echo pins are correctly connected.
  * Verify that the sensor is receiving power (VCC and GND connections).
  * Check that the Serial Monitor is set to the correct baud rate.

* Incorrect Readings:

  * Ensure that the calculations in the code are correct.
  * Verify that the speed of sound constant (0.034) is appropriate for your environment (humidity and temperature can affect sound speed).


* Sensor Interference:

  * Make sure there are no obstructions or reflective surfaces that might interfere with the ultrasonic pulses.
  * Avoid placing the sensor near other ultrasonic devices that could cause false readings.


**Further Exploration**

* Integrating with LEDs or Displays:

  * Use multiple LEDs to create a visual distance indicator.
  * Integrate with a 7-segment or LCD display to show the distance numerically.

* Creating a Proximity Alert System:

  Set thresholds to trigger alerts (e.g., sound alarms when objects are too close).

* Building a Simple Obstacle-Avoiding Robot:

  Utilize the ultrasonic sensor to detect obstacles and navigate around them.

**Conclusion**

In this lesson, you've learned how to use an ultrasonic sensor module with the Raspberry Pi Pico to measure the distance to an object. By triggering ultrasonic pulses and measuring the echo time, you can accurately determine the distance of nearby objects. This project serves as a foundation for more complex applications in robotics, automation, and interactive systems.
