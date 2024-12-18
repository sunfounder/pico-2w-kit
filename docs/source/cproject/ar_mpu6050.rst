.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ar_mpu6050:

6.3 Read from the MPU-6050
===============================

In this lesson, we'll explore how to interface the **MPU-6050** 6-axis motion tracking sensor with the Raspberry Pi Pico 2 W. The MPU-6050 combines a 3-axis gyroscope and a 3-axis accelerometer, providing raw sensor data over the I2C communication protocol.

* :ref:`cpn_mpu6050`

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
        - :ref:`cpn_mpu6050`
        - 1
        - 

**Understanding the MPU-6050 Sensor**

The **MPU-6050** sensor is widely used in projects that require motion tracking and orientation detection, such as drones, robotics, and gaming devices.

* **Accelerometer**: Measures acceleration forces along the X, Y, and Z axes. This includes gravitational acceleration, allowing you to determine the tilt or orientation of the sensor.
* **Gyroscope**: Measures rotational velocity around the X, Y, and Z axes, providing information about how fast the sensor is spinning.

**Schematic**

|sch_mpu6050_ar|

**Wiring**

|wiring_mpu6050_ar|

**Writing the Code**

We'll write a program that initializes the MPU-6050 sensor, reads acceleration and gyroscope data, and prints the values to the Serial Monitor.


.. note::

    * You can open the file ``6.3_6axis_motion_tracking.ino`` under the path of ``pico-2 w-kit-main/arduino/6.3_6axis_motion_tracking``. 
    * Or copy this code into **Arduino IDE**.
    * Then select the Raspberry Pi Pico board and the correct port before clicking the Upload button.
    * The ``Adafruit MPU6050`` library is used here, you can install it from the **Library Manager**.

      .. image:: img/lib_mpu6050.png


.. code-block:: arduino

    #include <Adafruit_MPU6050.h>
    #include <Wire.h>

    // Create an MPU6050 object
    Adafruit_MPU6050 mpu;

    void setup(void) {
      // Initialize Serial Communication
      Serial.begin(115200);

      Serial.println("Adafruit MPU6050 test!");

      // Try to initialize the MPU6050
      if (!mpu.begin()) {
        Serial.println("Failed to find MPU6050 chip");
        while (1) {
          delay(10);
        }
      }
      Serial.println("MPU6050 Found!");

      // Set accelerometer range
      mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
      Serial.print("Accelerometer range set to: ");
      switch (mpu.getAccelerometerRange()) {
        case MPU6050_RANGE_2_G:
          Serial.println("+-2G");
          break;
        case MPU6050_RANGE_4_G:
          Serial.println("+-4G");
          break;
        case MPU6050_RANGE_8_G:
          Serial.println("+-8G");
          break;
        case MPU6050_RANGE_16_G:
          Serial.println("+-16G");
          break;
      }

      // Set gyroscope range
      mpu.setGyroRange(MPU6050_RANGE_500_DEG);
      Serial.print("Gyro range set to: ");
      switch (mpu.getGyroRange()) {
        case MPU6050_RANGE_250_DEG:
          Serial.println("+-250 deg/s");
          break;
        case MPU6050_RANGE_500_DEG:
          Serial.println("+-500 deg/s");
          break;
        case MPU6050_RANGE_1000_DEG:
          Serial.println("+-1000 deg/s");
          break;
        case MPU6050_RANGE_2000_DEG:
          Serial.println("+-2000 deg/s");
          break;
      }

      // Set filter bandwidth
      mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);
      Serial.print("Filter bandwidth set to: ");
      switch (mpu.getFilterBandwidth()) {
        case MPU6050_BAND_260_HZ:
          Serial.println("260 Hz");
          break;
        case MPU6050_BAND_184_HZ:
          Serial.println("184 Hz");
          break;
        case MPU6050_BAND_94_HZ:
          Serial.println("94 Hz");
          break;
        case MPU6050_BAND_44_HZ:
          Serial.println("44 Hz");
          break;
        case MPU6050_BAND_21_HZ:
          Serial.println("21 Hz");
          break;
        case MPU6050_BAND_10_HZ:
          Serial.println("10 Hz");
          break;
        case MPU6050_BAND_5_HZ:
          Serial.println("5 Hz");
          break;
      }

      Serial.println("");
      delay(100);
    }

    void loop() {
      // Get new sensor events with the readings
      sensors_event_t a, g, temp;
      mpu.getEvent(&a, &g, &temp);

      // Print acceleration values
      Serial.print("Acceleration X: ");
      Serial.print(a.acceleration.x);
      Serial.print(" m/s^2, Y: ");
      Serial.print(a.acceleration.y);
      Serial.print(" m/s^2, Z: ");
      Serial.print(a.acceleration.z);
      Serial.println(" m/s^2");

      // Print gyroscope values
      Serial.print("Rotation X: ");
      Serial.print(g.gyro.x);
      Serial.print(" rad/s, Y: ");
      Serial.print(g.gyro.y);
      Serial.print(" rad/s, Z: ");
      Serial.print(g.gyro.z);
      Serial.println(" rad/s");

      delay(500); // Adjust delay as needed
    }


After uploading the code, the Serial Monitor should display the acceleration and rotation values continuously.

.. code-block::

    Adafruit MPU6050 test!
    MPU6050 Found!
    Accelerometer range set to: +-8G
    Gyro range set to: +-500 deg/s
    Filter bandwidth set to: 21 Hz

    Acceleration X: 0.00 m/s^2, Y: 0.00 m/s^2, Z: 9.81 m/s^2
    Rotation X: 0.02 rad/s, Y: -0.01 rad/s, Z: 0.00 rad/s
    Acceleration X: 0.10 m/s^2, Y: 0.05 m/s^2, Z: 9.76 m/s^2
    Rotation X: 0.15 rad/s, Y: -0.05 rad/s, Z: 0.02 rad/s

Gently rotate or move the MPU-6050 sensor module.
Observe changes in the acceleration and rotation values corresponding to the movement.

**Understanding the Code**

#. Including Libraries and Defining Constants:


   * ``Adafruit_MPU6050.h``: Includes the MPU6050 library for easier interfacing.
   * ``Wire.h``: Includes the I2C communication library.
   * ``mpu``: Creates an MPU6050 object to interact with the sensor.

#. Setup Function:

   * MPU6050 Initialization: 
   
     Attempts to initialize the MPU6050 sensor. If unsuccessful, it prints an error message and halts the program.
   
     .. code-block:: arduino
   
         Serial.println("Adafruit MPU6050 test!");
   
         // Try to initialize the MPU6050
         if (!mpu.begin()) {
           Serial.println("Failed to find MPU6050 chip");
           while (1) {
             delay(10);
           }
         }
         Serial.println("MPU6050 Found!");

   * Accelerometer Range: 
   
     Sets the accelerometer range to ±8G and prints the current range.
   
     .. code-block:: arduino
   
         mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
         Serial.print("Accelerometer range set to: ");
         switch (mpu.getAccelerometerRange()) {
           case MPU6050_RANGE_2_G:
             Serial.println("+-2G");
             break;
            ...
           case MPU6050_RANGE_16_G:
             Serial.println("+-16G");
             break;
         }
   
   * Gyroscope Range: 
   
     Sets the gyroscope range to ±500 degrees per second and prints the current range.
   
     .. code-block:: arduino
   
         mpu.setGyroRange(MPU6050_RANGE_500_DEG);
         Serial.print("Gyro range set to: ");
         switch (mpu.getGyroRange()) {
           case MPU6050_RANGE_250_DEG:
             Serial.println("+-250 deg/s");
             break;
            ...
           case MPU6050_RANGE_2000_DEG:
             Serial.println("+-2000 deg/s");
             break;
         }
   
   * Setting Filter Bandwidth: 
   
     Configures the filter bandwidth to 21 Hz to reduce noise and prints the current setting.
   
     .. code-block:: arduino
   
         mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);
         Serial.print("Filter bandwidth set to: ");
         switch (mpu.getFilterBandwidth()) {
           case MPU6050_BAND_260_HZ:
             Serial.println("260 Hz");
             break;
            ...
           case MPU6050_BAND_5_HZ:
             Serial.println("5 Hz");
             break;
         }

#. Loop Function:

   * Reading Sensor Data:
   
     * ``sensors_event_t a, g, temp;``: Creates event objects to store accelerometer, gyroscope, and temperature data.
     * ``mpu.getEvent(&a, &g, &temp);``: Retrieves the latest sensor data.
   
     .. code-block:: arduino
   
         sensors_event_t a, g, temp;
         mpu.getEvent(&a, &g, &temp);
   
   * Printing Sensor Data:
   
     * **Acceleration**: Prints acceleration values along the X, Y, and Z axes in meters per second squared (m/s²).
     * **Rotation**: Prints gyroscope values (rotational velocity) around the X, Y, and Z axes in radians per second (rad/s).
   
     .. code-block:: Arduino
   
       // Print acceleration values
       Serial.print("Acceleration X: ");
       Serial.print(a.acceleration.x);
       ...
       Serial.print(g.gyro.y);
       Serial.print(" rad/s, Z: ");
       Serial.print(g.gyro.z);
       Serial.println(" rad/s");


**Troubleshooting**

* No Readings Displayed:

  * Check all wiring connections, especially the I2C lines (SCL and SDA).
  * Ensure the MPU-6050 sensor is receiving power (VCC and GND connections).
  * Verify that the correct GPIO pins are defined in the code.

* Incorrect Readings:

  * Ensure that the MPU-6050 sensor is properly seated in the breadboard.
  * Verify that the sensor's range and filter settings match the desired application.
  * Check for any loose connections or shorts in the wiring.

* Sensor Interference:

  * Avoid placing the sensor near other electronic devices that might cause interference.
  * Ensure there are no physical obstructions blocking the sensor's movement.

**Further Exploration**

* Combining with Other Sensors:

  Integrate the MPU-6050 with GPS modules, magnetometers, or other sensors to create comprehensive tracking systems.

* Building a Motion-Based Game Controller:

  Use the MPU-6050 to detect movement and orientation, allowing for the creation of motion-controlled gaming devices.

* Creating a Self-Balancing Robot:

  Utilize the accelerometer and gyroscope data to maintain balance and stability in robotic applications.

* Implementing Sensor Fusion Algorithms:

  Combine accelerometer and gyroscope data to calculate orientation angles using algorithms like the Kalman filter or complementary filter.

**Conclusion**

In this lesson, you've learned how to interface the MPU-6050 6-axis motion tracking sensor with the Raspberry Pi Pico. By leveraging the Adafruit MPU6050 library, you can easily retrieve and interpret accelerometer and gyroscope data, enabling a wide range of motion and orientation-based applications. The optional LED indicator adds a simple way to provide visual feedback based on sensor readings, enhancing the interactivity of your projects.
