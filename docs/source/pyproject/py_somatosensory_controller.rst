.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_somato_controller:


7.11 Building a Somatosensory Controller
============================================

In this exciting project, we'll create a **Somatosensory Controller** using the Raspberry Pi Pico 2 W, an MPU6050 accelerometer and gyroscope module, and a servo motor. This device captures human motion—specifically the tilt of your hand—and translates it into movement of the servo motor. This technology is similar to that used in robotics and remote operation systems, such as surgical robots or robotic arms.

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
    *   - 6
        - :ref:`cpn_servo`
        - 1
        - |link_servo_buy|

**Understanding the Components**

* **MPU6050 Accelerometer and Gyroscope**: A 6-axis motion tracking device that measures acceleration and angular velocity along the X, Y, and Z axes. We'll use it to detect the tilt of your hand.
* **Servo Motor**: A motor that can be controlled to move to a specific angle. We'll use it to mimic the movement detected by the MPU6050.

**Schematic**

|sch_somato|

The MPU6050 calculates the attitude angle based on the acceleration values in each direction.

The program will control the servo to make the corresponding deflection angle as the attitude angle changes.

**Wiring**

|wiring_somatosensory_controller| 


**Writing the Code**

We'll write a MicroPython script that:

* Reads accelerometer data from the MPU6050.
* Calculates the tilt angle of your hand.
* Controls the servo motor to mimic the tilt.

.. note::

    * Open the ``7.11_somatosensory_controller.py`` from ``pico-2 w-kit-main/micropython`` or copy the code into Thonny, then click "Run" or press F5.
    * Ensure the correct interpreter is selected: MicroPython (Raspberry Pi Pico).COMxx. 
    * Here you need to use the ``imu.py`` and ``vector3d.py``, please check if it has been uploaded to Pico, for a detailed tutorial refer to :ref:`add_libraries_py`.

.. code-block:: python

    from imu import MPU6050
    from machine import I2C, Pin, PWM
    import utime
    import math

    # Initialize I2C communication for MPU6050
    i2c = I2C(1, scl=Pin(7), sda=Pin(6))
    mpu = MPU6050(i2c)

    # Initialize PWM for the servo motor on GP15
    servo = PWM(Pin(15))
    servo.freq(50)  # Set frequency to 50Hz for servo

    # Function to map angle to PWM duty cycle
    def angle_to_duty(angle):
        # Convert angle (0-180) to duty cycle (0.5ms - 2.5ms pulse width)
        # Duty cycle range is from 2% to 12% for 0.5ms to 2.5ms at 50Hz
        duty_cycle = (angle / 18) + 2
        duty_u16 = int(duty_cycle / 100 * 65535)
        return duty_u16

    # Function to get the tilt angle from accelerometer data
    def get_tilt_angle():
        accel = mpu.accel
        x = accel.x
        y = accel.y
        z = accel.z
        angle = math.atan2(y, z) * (180 / math.pi)
        return angle + 90  # Adjust angle to range from 0 to 180

    # Main loop
    try:
        while True:
            angle = get_tilt_angle()
            if angle < 0:
                angle = 0
            elif angle > 180:
                angle = 180
            duty = angle_to_duty(angle)
            servo.duty_u16(duty)
            utime.sleep(0.1)
    except KeyboardInterrupt:
        servo.deinit()
        print("Program stopped.")

After the program starts, tilt your hand up and down.
The servo motor should mimic the tilt by moving correspondingly.
Observe how the servo responds to your hand movements.

**Understanding the Code**

#. Initialization:

   * **I2C Communication**: Set up to read data from the MPU6050.
   * **Servo Motor PWM**: Initialized on GP15 with a frequency of 50Hz.

#. Angle Calculation:

   * ``get_tilt_angle()``: Calculates the tilt angle based on accelerometer readings. The angle is adjusted to be between 0 and 180 degrees.

   .. code-block:: python

        def get_tilt_angle():
            accel = mpu.accel
            x = accel.x
            y = accel.y
            z = accel.z
            angle = math.atan2(y, z) * (180 / math.pi)
            return angle + 90  # Adjust angle to range from 0 to 180

#. Servo Control:

   * ``angle_to_duty(angle)``: Converts the angle to the appropriate PWM duty cycle for the servo motor.
   * Duty Cycle Calculation: The servo expects pulses between 0.5ms (0 degrees) and 2.5ms (180 degrees) at 50Hz.

   .. code-block:: python

        def angle_to_duty(angle):
            # Convert angle (0-180) to duty cycle (0.5ms - 2.5ms pulse width)
            # Duty cycle range is from 2% to 12% for 0.5ms to 2.5ms at 50Hz
            duty_cycle = (angle / 18) + 2
            duty_u16 = int(duty_cycle / 100 * 65535)
            return duty_u16

#. Main Loop:

   * Reads the tilt angle.
   * Adjusts the angle to ensure it's within 0 to 180 degrees.
   * Sets the servo position accordingly.
   * Includes a short delay to prevent jitter.
   * Captures a keyboard interrupt to deinitialize the servo safely.

   .. code-block:: python

        try:
            while True:
                angle = get_tilt_angle()
                if angle < 0:
                    angle = 0
                elif angle > 180:
                    angle = 180
                duty = angle_to_duty(angle)
                servo.duty_u16(duty)
                utime.sleep(0.1)
        except KeyboardInterrupt:
            servo.deinit()
            print("Program stopped.")

**Troubleshooting**

* Servo Not Moving:

  * Check that the servo is powered correctly.
  * Ensure the signal wire is connected to GP15.
  * Verify that the grounds are connected between the Pico and the servo.

* Inaccurate Movements:

  * Make sure the MPU6050 is securely attached and not shaking excessively.
  * Adjust the angle calculations if needed.

* Program Errors:

  * Ensure that imu.py and vector3d.py are correctly uploaded.
  * Check for typos or indentation errors in the code.

**Extensions and Enhancements**

* Control Multiple Servos:

  * Add more servos to control additional axes of movement.
  * Expand the code to handle rotation around other axes.

* Wireless Communication:

  Use Bluetooth or Wi-Fi modules to transmit sensor data to another device controlling the servos.

* Data Smoothing:

  Implement filters (e.g., Kalman filter) to smooth out sensor readings.

* Visual Feedback:

  Add an OLED or LCD display to show real-time angle data.

**Conclusion**

You've successfully built a Somatosensory Controller that captures human motion and translates it into mechanical movement. This project demonstrates how sensors and actuators can work together to create interactive systems, similar to those used in robotics and remote operations.

Feel free to enhance this project by adding more features or integrating it into larger systems.
