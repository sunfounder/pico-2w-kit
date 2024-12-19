.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_bubble_level:

7.12 Building a Digital Bubble Level
==========================================

In this project, we'll create a **Digital Bubble Level** using the Raspberry Pi Pico 2 W, an MPU6050 accelerometer and gyroscope module, and an 8x8 LED matrix display controlled by two 74HC595 shift registers. This device functions similarly to a traditional spirit level, indicating the tilt of a surface. As you tilt the MPU6050, a "bubble" represented by LEDs on the matrix will move accordingly, allowing you to visualize the levelness of a surface.

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
        - :ref:`cpn_dot_matrix`
        - 1
        - 
    *   - 6
        - :ref:`cpn_74hc595`
        - 2
        - |link_74hc595_buy|
    *   - 7
        - :ref:`cpn_mpu6050`
        - 1
        - 

**Understanding the Components**

* **MPU6050 Accelerometer and Gyroscope**: Provides acceleration and angular velocity data along three axes (X, Y, Z), which we'll use to calculate the tilt angles.
* **8x8 LED Matrix Display**: An array of LEDs arranged in 8 rows and 8 columns, allowing us to display patterns or images by controlling individual LEDs.
* **74HC595 Shift Registers**: Allows us to control multiple outputs (in this case, the rows and columns of the LED matrix) using fewer GPIO pins on the Pico.

**Schematic**

|sch_bubble_level|

The MPU6050 takes the acceleration values in each direction and calculates the attitude angle.

As a result, the program draws a 2x2 dot on the dot matrix based on data from the two 74HC595 chips.

As the attitude angle changes, the program sends different data to the 74HC595 chips, and the position of the dot changes, creating a bubble effect.

**Wiring**


|wiring_digital_bubble_level| 


**Writing the Code**

We'll write a MicroPython script that:

* Reads acceleration data from the MPU6050.
* Calculates the tilt angles along the X and Y axes.
* Maps the tilt angles to positions on the 8x8 LED matrix.
* Displays a "bubble" (a 2x2 pixel representation) that moves according to the tilt.

.. note::

    * Open the ``7.12_digital_bubble_level.py`` from ``pico-2 w-kit-main/micropython`` or copy the code into Thonny, then click "Run" or press F5.
    * Ensure the correct interpreter is selected: MicroPython (Raspberry Pi Pico).COMxx. 
    * Here you need to use the ``imu.py`` and ``vector3d.py``, please check if it has been uploaded to Pico, for a detailed tutorial refer to :ref:`add_libraries_py`.

.. code-block:: python

    import machine
    from machine import I2C, Pin
    import time
    import math
    from imu import MPU6050
    
    # Initialize I2C communication with MPU6050 sensor
    i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)
    mpu = MPU6050(i2c)
    
    # Function to calculate the distance between two points
    def dist(a, b):
        return math.sqrt((a * a) + (b * b))
    
    # Function to calculate rotation along the y-axis
    def get_y_rotation(x, y, z):
        radians = math.atan2(x, dist(y, z))
        return -math.degrees(radians)
    
    # Function to calculate rotation along the x-axis
    def get_x_rotation(x, y, z):
        radians = math.atan2(y, dist(x, z))
        return math.degrees(radians)
    
    # Function to get the current angles from the MPU6050 sensor
    def get_angle():
        y_angle = get_y_rotation(mpu.accel.x, mpu.accel.y, mpu.accel.z)
        x_angle = get_x_rotation(mpu.accel.x, mpu.accel.y, mpu.accel.z)
        return x_angle, y_angle
    
    # Initialize shift register pins for controlling the LED matrix
    sdi = machine.Pin(18, machine.Pin.OUT)
    rclk = machine.Pin(19, machine.Pin.OUT)
    srclk = machine.Pin(20, machine.Pin.OUT)
    
    # Function to shift data into the shift register
    def hc595_in(dat):
        for bit in range(7, -1, -1):
            srclk.low()
            time.sleep_us(30)
            sdi.value(1 & (dat >> bit))
            time.sleep_us(30)
            srclk.high()
    
    # Function to output the data from the shift register to the LED matrix
    def hc595_out():
        rclk.high()
        time.sleep_us(200)
        rclk.low()
    
    # Function to display a glyph (8x8 matrix) on the LED matrix
    def display(glyph):
        for i in range(0, 8):
            hc595_in(glyph[i])
            hc595_in(0x80 >> i)
            hc595_out()
    
    # Convert a 2D matrix to a glyph that can be displayed on the LED matrix
    def matrix_2_glyph(matrix):
        glyph = [0 for i in range(8)]
        for i in range(8):
            for j in range(8):
                glyph[i] += matrix[i][j] << j
        return glyph
    
    # Clamp a value between a specified minimum and maximum
    def clamp_number(val, min_val, max_val):
        return min_val if val < min_val else max_val if val > max_val else val
    
    # Map a value from one range to another
    def interval_mapping(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    
    # Calculate the position of the bubble in the matrix based on the MPU6050 readings
    sensitivity = 4  # Sensitivity of the bubble movement
    matrix_range = 7  # The matrix size is 8x8, so the range is 0-7
    point_range = matrix_range - 1  # Bubble's position should be between 0 and 6
    
    # Function to calculate the position of the bubble based on sensor data
    def bubble_position():
        y, x = get_angle()  # Get the current rotation angles
        x = int(clamp_number(interval_mapping(x, 90, -90, 0 - sensitivity, point_range + sensitivity), 0, point_range))
        y = int(clamp_number(interval_mapping(y, -90, 90, point_range + sensitivity, 0 - sensitivity), 0, point_range))
        return [x, y]
    
    # Drop the bubble (represented by turning off 2x2 LEDs) into the matrix
    def drop_bubble(matrix, bubble):
        matrix[bubble[0]][bubble[1]] = 0
        matrix[bubble[0] + 1][bubble[1]] = 0
        matrix[bubble[0]][bubble[1] + 1] = 0
        matrix[bubble[0] + 1][bubble[1] + 1] = 0
        return matrix
    
    # Main loop
    while True:
        matrix = [[1 for i in range(8)] for j in range(8)]  # Create an empty matrix (all LEDs on)
        bubble = bubble_position()  # Get the current bubble position based on sensor data
        matrix = drop_bubble(matrix, bubble)  # Drop the bubble into the matrix
        display(matrix_2_glyph(matrix))  # Display the matrix on the LED grid
        time.sleep(0.1)  # Add a small delay to slow down updates

When the code runs, place the setup on a level surface.
The bubble (a 2x2 pixel area) should appear at the center of the LED matrix.
Tilt the breadboard or the MPU6050 module.
Observe the bubble moving on the LED matrix in the direction of the tilt, simulating a real bubble level.

**Understanding the Code**

This code reads data from an MPU6050 accelerometer and gyroscope sensor to determine the tilt of the device and displays a "bubble" on an 8x8 LED matrix, simulating a digital bubble level.

#. Imports and Initializations:

   * ``machine``: Access to the microcontroller's hardware components.
   * ``I2C``, ``Pin``: For I2C communication and GPIO pin manipulation.
   * ``time``: Timing functions for delays.
   * ``math``: Mathematical functions for calculations.
   * ``MPU6050`` from ``imu``: Library to interface with the MPU6050 sensor.

#. I2C Initialization:

   * Sets up I2C communication on bus 1 with SDA on Pin 6 and SCL on Pin 7.
   * The frequency is set to 400 kHz for fast data transfer.
   * An ``mpu`` object is created to interact with the MPU6050 sensor.

#. Mathematical Functions:

   * ``dist(a, b)`` Function:

     * Calculates the Euclidean distance between two values.
     * Used to compute the magnitude component in angle calculations.

   * ``get_y_rotation(x, y, z)``:
     
     * Calculates the rotation around the Y-axis in degrees.
     * Uses ``math.atan2`` to compute the arctangent of x and the distance between y and z.
     * The result is negated to match the desired orientation.

   * ``get_x_rotation(x, y, z)``:

     * Calculates the rotation around the X-axis in degrees.
     * Similar to ``get_y_rotation`` but computes the arctangent of y and the distance between x and z.

   * ``get_angle()``:

     * Retrieves the current acceleration data from the MPU6050 sensor.
     * Computes the X and Y rotation angles using the accelerometer data.

#. Shift Register Functions:

   * Pin Definitions:

     * ``sdi``: Serial Data Input pin for the shift register (Pin 18).
     * ``rclk``: Register Clock (latch) pin for the shift register (Pin 19).
     * ``srclk``: Shift Register Clock pin for the shift register (Pin 20).

   * ``hc595_in(dat)`` Function:

     * Shifts an 8-bit data byte into the shift register.
     * Iterates over each bit from MSB to LSB.
     * Controls ``srclk`` and ``sdi`` to clock in the data bits.

   * ``hc595_out()``:

     * Latches the shifted data to the output pins of the shift register.
     * Toggles the ``rclk`` pin to transfer the data from the shift register to the storage register.

#. LED Matrix Display Functions:

   * ``display(glyph)`` Function:

     * Displays an 8x8 glyph on the LED matrix.
     * Iterates through each row of the glyph.
     * Shifts in the row data and the corresponding column selector.
     * Calls ``hc595_out()`` to update the display.

   * ``matrix_2_glyph(matrix)`` Function:

     * Converts an 8x8 2D matrix of 0s and 1s into an 8-byte glyph.
     * Each byte in the glyph represents a row in the LED matrix.
     * Bits in each byte correspond to the LEDs in that row.

#. Utility Functions:

   * ``clamp_number(val, min_val, max_val)`` Function:

     * Ensures that ``val`` stays within the specified ``min_val`` and ``max_val`` range.
     * Prevents the bubble from moving outside the LED matrix boundaries.

   * ``interval_mapping(x, in_min, in_max, out_min, out_max)`` Function:

     * Maps a value ``x`` from one numerical range to another.
     * Used to translate angle measurements to matrix positions.

#. Bubble Position Calculation:

   * Sensitivity Settings:

     * ``sensitivity = 4``: Determines how responsive the bubble is to tilt changes.
     * ``matrix_range = 7``: The maximum index for the 8x8 matrix (0 to 7).
     * ``point_range = matrix_range - 1``: Adjusted range to keep the bubble within bounds (0 to 6).

   * ``bubble_position()`` Function:

     * Retrieves the current X and Y rotation angles.
     * Maps the angles to positions on the LED matrix using ``interval_mapping``.
     * Clamps the positions to ensure they stay within the matrix.

#. Bubble Display Function:

   * ``drop_bubble(matrix, bubble)`` Function:

     * Modifies the LED matrix to represent the bubble at the given position.
     * Turns off a 2x2 block of LEDs centered at the bubble's coordinates.
     * Updates the matrix to create the visual effect of a bubble moving.

#. Main Loop

   * Continuously runs to update the display based on sensor input.
   * Initializes a fresh 8x8 matrix with all LEDs turned on (value ``1``).
   * Gets the current bubble position from ``bubble_position()``.
   * Updates the matrix with ``drop_bubble()`` to reflect the bubble's new position.
   * Converts the matrix to a glyph using ``matrix_2_glyph()``.
   * Displays the glyph on the LED matrix with ``display()``.
   * Waits for 0.1 seconds before repeating to control the update rate.

**Troubleshooting**

* LED Matrix Not Displaying Correctly:

  * Check all wiring connections between the shift registers and the LED matrix.
  * Ensure that the shift registers are connected properly to the Pico.
  * Verify that the common anode or cathode configuration of your LED matrix matches the code logic.

* Incorrect Bubble Movement:

  * Ensure the MPU6050 is properly connected and functioning.
  * Check that the MPU6050 is correctly oriented.

* Program Errors:

  * Ensure that ``imu.py`` and ``vector3d.py`` are correctly uploaded.
  * Check for typos or indentation errors in the code.

**Experimenting Further**

* Adjust Sensitivity:

  Modify the mapping of angles to positions to change the sensitivity of the bubble movement.

* Display Enhancements:

  * Change the size or shape of the bubble.
  * Add visual effects, such as trails or different patterns.

* Calibration:

  Implement a calibration routine to set the zero point when the device is placed on an uneven surface.

* Alternative Displays:

  Use an OLED or LCD display to show numerical angle values in addition to the visual bubble.

**Conclusion**

You've successfully built a Digital Bubble Level using the Raspberry Pi Pico 2 W! This project demonstrates how accelerometer data can be used to visualize orientation and tilt, and how to control an LED matrix display using shift registers.

Feel free to expand upon this project by adding new features or integrating it into larger systems.

