.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_mpu6050:

6.3 6-axis Motion Tracking
=====================================


In this lesson, we'll explore how to interface the **MPU-6050** 6-axis motion tracking sensor with the Raspberry Pi Pico 2w. The MPU-6050 combines a 3-axis gyroscope and a 3-axis accelerometer, providing raw sensor data over the I2C communication protocol.

* :ref:`cpn_mpu6050`


**Required Components**

In this project, we need the following components. 

It's definitely convenient to buy a whole kit, here's the link: 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ITEMS IN THIS KIT
        - LINK
    *   - Pico 2 W Starter Kit	
        - 450+
        - |link_pico2w_kit|

You can also buy them separately from the links below.


.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - COMPONENT	
        - QUANTITY
        - LINK

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

Let's write a MicroPython script to read accelerometer and gyroscope data from the MPU-6050 sensor.

.. note::

    * Open the ``6.3_6axis_motion_tracking.py`` from ``pico-2w-starter-kit-main/micropython`` or copy the code into Thonny, then click "Run" or press F5.
    * Ensure the correct interpreter is selected: MicroPython (Raspberry Pi Pico).COMxx. 
     
    * Here you need to use the ``imu.py`` and ``vector3d.py``, please check if it has been uploaded to Pico, for a detailed tutorial refer to :ref:`add_libraries_py`.


.. code-block:: python

   from machine import I2C, Pin
   import utime
   from imu import MPU6050

   # Initialize I2C interface (I2C0) with SDA on GP4 and SCL on GP5
   i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)

   # Initialize the MPU-6050 sensor
   mpu = MPU6050(i2c)

   def read_accelerometer():
      """Reads accelerometer data and returns it as a tuple (x, y, z)."""
      accel = mpu.accel
      return accel.x, accel.y, accel.z

   def read_gyroscope():
      """Reads gyroscope data and returns it as a tuple (x, y, z)."""
      gyro = mpu.gyro
      return gyro.x, gyro.y, gyro.z

   def main():
      """Main loop to read and print sensor data."""
      while True:
         # Read accelerometer data
         ax, ay, az = read_accelerometer()
         print("Accelerometer (g) - X: {:.3f}, Y: {:.3f}, Z: {:.3f}".format(ax, ay, az))
         
         # Pause for readability
         utime.sleep(0.5)
         
         # Read gyroscope data
         gx, gy, gz = read_gyroscope()
         print("Gyroscope (°/s) - X: {:.3f}, Y: {:.3f}, Z: {:.3f}".format(gx, gy, gz))
         
         # Pause before the next set of readings
         utime.sleep(0.5)

   # Run the main function
   if __name__ == "__main__":
      main()


The script prints accelerometer and gyroscope readings alternately every 0.5 seconds.

* Accelerometer Output:

  .. code-block::

     Accelerometer (g) - X: 0.000, Y: 0.000, Z: 1.000

  At rest, you should see values close to 0 g on X and Y axes, and approximately 1 g on the Z-axis due to gravity.

* Gyroscope Output:

  .. code-block::

     Gyroscope (°/s) - X: 0.000, Y: 0.000, Z: 0.000

  When stationary, the gyroscope readings should be close to 0 °/s on all axes.
  Rotating the sensor will change these values, reflecting the angular velocity.

**Understanding the Code**

#. Imports and Setup:


   * ``machine.I2C and machine.Pin``: For hardware interface.
   * ``utime``: For timing functions.
   * ``MPU6050``: The sensor class from the imu.py library.

#. I2C Initialization:

   Sets up I2C bus 0 with SDA on GP4 and SCL on GP5. The frequency is set to 400 kHz for fast communication.

   .. code-block:: python

      i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)


#. Sensor Initialization:

   Creates an instance of the MPU-6050 sensor using the I2C interface.

   .. code-block:: python

      mpu = MPU6050(i2c)

#. Reading Accelerometer Data:

   Accesses the accelerometer data and returns the X, Y, Z values.

   .. code-block:: python

      def read_accelerometer():
         accel = mpu.accel
         return accel.x, accel.y, accel.z


#. Reading Gyroscope Data:
   
   Accesses the gyroscope data and returns the X, Y, Z values.

   .. code-block:: python

      def read_gyroscope():
         gyro = mpu.gyro
         return gyro.x, gyro.y, gyro.z


#. Main Loop:

   * Reads and prints accelerometer data.
   * Waits for 0.5 seconds.
   * Reads and prints gyroscope data.
   * Waits for another 0.5 seconds before repeating.

   .. code-block:: python

      def main():
         while True:
            # Read and print accelerometer data
            ax, ay, az = read_accelerometer()
            print("Accelerometer (g) - X: {:.3f}, Y: {:.3f}, Z: {:.3f}".format(ax, ay, az))
            
            utime.sleep(0.5)
            
            # Read and print gyroscope data
            gx, gy, gz = read_gyroscope()
            print("Gyroscope (°/s) - X: {:.3f}, Y: {:.3f}, Z: {:.3f}".format(gx, gy, gz))
            
            utime.sleep(0.5)


#. Program Entry Point:

   Ensures that ``main()`` is called when the script is executed directly.

   .. code-block:: python

      if __name__ == "__main__":
         main()


**Experimenting Further**

* **Focus on One Sensor**: To concentrate on either accelerometer or gyroscope data, you can comment out the print statements for the other sensor.
* **Data Visualization**: Use tools or software to plot the sensor data in real-time for better visualization.
* **Calculating Orientation**: Implement algorithms to calculate pitch and roll from the accelerometer data.
* **Motion Detection**: Create a program that performs actions when certain motion thresholds are exceeded.

**Understanding Sensor Data**

* Accelerometer:

  * Measures acceleration forces in g (gravitational force).
  * Useful for detecting orientation, tilt, and linear motion.

* Gyroscope:

  * Measures rotational velocity in degrees per second (°/s).
  * Useful for detecting rotation and angular motion.

**Troubleshooting Tips**

* No Output or Errors:

  * Verify the wiring connections, especially SDA and SCL lines.
  * Ensure that the sensor is powered correctly.

* Static Readings:

  * If the readings don't change when moving the sensor, check for loose connections.
  * Make sure the correct I2C address is being used.

* Inconsistent Data:

  * Environmental vibrations can affect sensor readings.
  * Place the sensor on a stable surface when testing.

**Conclusion**

In this lesson, you've learned how to interface the MPU-6050 accelerometer and gyroscope sensor with the Raspberry Pi Pico 2w. By reading the raw sensor data, you can explore a wide range of applications involving motion detection, orientation tracking, and more.
