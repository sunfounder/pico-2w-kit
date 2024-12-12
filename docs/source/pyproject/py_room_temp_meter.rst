.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_room_temp:

7.2 Building a Room Temperature Meter
============================================================

In this project, we'll create a **Room Temperature Meter** using a thermistor and an I2C LCD1602 display. This simple yet practical device will measure the ambient temperature and display it on the LCD screen, providing real-time temperature readings of your environment.

:ref:`py_temp`

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
        - :ref:`cpn_resistor`
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_thermistor`
        - 1
        - |link_thermistor_buy|
    *   - 7
        - :ref:`cpn_i2c_lcd`
        - 1
        - |link_i2clcd1602_buy|

**Understanding the Components**

* **Thermistor:** A type of resistor whose resistance varies significantly with temperature. We'll use a Negative Temperature Coefficient (NTC) thermistor, meaning its resistance decreases as temperature increases.
* **Voltage Divider:** By combining the thermistor with a fixed resistor, we create a voltage divider circuit, allowing us to measure changes in voltage corresponding to temperature changes.
* **I2C LCD1602 Display:** A 16x2 character LCD display with an I2C interface, which simplifies wiring and code by using only two data lines (SDA and SCL).

**Schematic**

|sch_room_temp|


**Wiring**

|wiring_room_temp|

**Writing the Code**

We'll write a MicroPython program that reads the temperature from the thermistor and displays it on the LCD.

.. note::

    * Open the ``7.2_room_temperature_meter.py`` from ``pico-2w-starter-kit-main/micropython`` or copy the code into Thonny, then click "Run" or press F5.
    * Ensure the correct interpreter is selected: MicroPython (Raspberry Pi Pico).COMxx. 
    * Here you need to use the library called ``lcd1602.py``, please check if it has been uploaded to Pico, for a detailed tutorial refer to :ref:`add_libraries_py`.


.. code-block:: python

    from lcd1602 import LCD
    from machine import I2C, Pin, ADC
    import utime
    import math

    # Initialize the thermistor (ADC on pin 28)
    thermistor = ADC(28)  # Analog input from the thermistor

    # Initialize I2C communication for the LCD1602 display
    i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=400000)

    # Create an LCD object for controlling the LCD1602 display
    lcd = LCD(i2c)

    # Constants for the Steinhart-Hart equation
    BETA = 3950  # Beta coefficient of the thermistor
    R0 = 10000   # Resistance at 25 degrees Celsius
    T0 = 298.15  # Reference temperature in Kelvin (25°C)

    def read_temperature():
        # Read raw ADC value from the thermistor
        adc_value = thermistor.read_u16()

        # Convert the raw ADC value to voltage
        voltage = adc_value * 3.3 / 65535

        # Calculate the resistance of the thermistor
        Rt = (voltage * R0) / (3.3 - voltage)

        # Apply the Steinhart-Hart equation to calculate temperature in Kelvin
        tempK = 1 / ((1 / T0) + (1 / BETA) * math.log(Rt / R0))

        # Convert temperature from Kelvin to Celsius
        tempC = tempK - 273.15

        return tempC

    def main():
        while True:
            temperature = read_temperature()
            # Format the temperature to two decimal places
            temp_str = "{:.2f} C".format(temperature)

            # Display the temperature on the LCD
            lcd.clear()
            lcd.write(0, 0, "Room Temp:")
            lcd.write(4, 1, temp_str)

            # Optional: Print the temperature to the console
            print("Temperature:", temp_str)

            utime.sleep(1)

    if __name__ == "__main__":
        main()

Once the code is running, the LCD should display the current room temperature in Celsius.
If the LCD is blank, adjust the contrast using the potentiometer on the back.
The console in Thonny will also print the temperature readings.

**Understanding the Code**

#. Imports and Initialization:

   * ``lcd1602.LCD``: For controlling the LCD display.
   * ``machine.ADC``: To read analog values from the thermistor.
   * ``math``: For logarithmic calculations needed in the temperature conversion.

#. Variables:

   * **BETA**: The beta coefficient specific to your thermistor (commonly 3950).
   * **R0**: The resistance of the thermistor at the reference temperature (usually 10kΩ at 25°C).
   * **T0**: The reference temperature in Kelvin (25°C + 273.15).

   .. code-block:: python

        BETA = 3950  # Beta coefficient of the thermistor
        R0 = 10000   # Resistance at 25 degrees Celsius
        T0 = 298.15  # Reference temperature in Kelvin (25°C)
    
#. Reading Temperature (``read_temperature Function``):

   * **ADC Reading**: Captures the analog value from the thermistor.
   * **Voltage Calculation**: Converts the ADC value to an actual voltage.
   * **Resistance Calculation (Rt)**: Calculates the thermistor's resistance using the voltage divider formula.
   * **Steinhart-Hart Equation**: A mathematical model that relates the resistance of a thermistor to its temperature.
   * **Conversion to Celsius**: Adjusts the temperature from Kelvin to Celsius.

   .. code-block:: python

        def read_temperature():
                # Read raw ADC value from the thermistor
                adc_value = thermistor.read_u16()

                # Convert the raw ADC value to voltage
                voltage = adc_value * 3.3 / 65535

                # Calculate the resistance of the thermistor
                Rt = (voltage * R0) / (3.3 - voltage)

                # Apply the Steinhart-Hart equation to calculate temperature in Kelvin
                tempK = 1 / ((1 / T0) + (1 / BETA) * math.log(Rt / R0))

                # Convert temperature from Kelvin to Celsius
                tempC = tempK - 273.15

                return tempC

#. Main Loop (main Function):

   * Continuously reads the temperature.
   * Formats and displays the temperature on the LCD.
   * Prints the temperature to the console (optional for debugging).
   * Waits for 1 second before repeating.

   .. code-block:: python

        def main():
            while True:
                temperature = read_temperature()
                # Format the temperature to two decimal places
                temp_str = "{:.2f} C".format(temperature)

                # Display the temperature on the LCD
                lcd.clear()
                lcd.write(0, 0, "Room Temp:")
                lcd.write(4, 1, temp_str)

                # Optional: Print the temperature to the console
                print("Temperature:", temp_str)

                utime.sleep(1)


**Troubleshooting**

* LCD Not Displaying Text:

  * Verify SDA and SCL connections (GP6 and GP7).
  * Check that the LCD is powered correctly.
  * Adjust the contrast potentiometer on the LCD module.

* Incorrect Temperature Readings:

  * Ensure the thermistor and resistor are connected properly.
  * Double-check the resistor values.
  * Confirm that the BETA value matches your thermistor's specifications.

* Program Errors:

  * Make sure all necessary libraries are correctly uploaded to the Pico.
  * Check for typos or indentation errors in the code.

**Experimenting Further**

* Display Temperature in Fahrenheit:

  Modify the read_temperature function to convert Celsius to Fahrenheit: ``tempF = (tempC * 9 / 5) + 32``.

* Add Humidity Measurement:

  Integrate a DHT11 or DHT22 sensor to display humidity alongside temperature.

* Data Logging:

  Store temperature readings over time in a file on the Pico. Plot the data using a computer for analysis.

* Visual Alerts:

  Add LEDs or a buzzer to alert when the temperature exceeds certain thresholds.

**Understanding the Science**

* Thermistors and Temperature Measurement:

  * Thermistors are sensitive to temperature changes, making them ideal for precise measurements.
  * The voltage divider circuit converts resistance changes into voltage changes that can be read by the Pico's ADC.

* Steinhart-Hart Equation:

  * Provides a more accurate temperature calculation than a simple linear approximation.
  * Essential for applications requiring precise temperature readings.

**Conclusion**

Congratulations! You've built a functional Room Temperature Meter using the Raspberry Pi Pico 2w. This project not only demonstrates how to interface analog sensors and I2C devices but also provides practical experience with temperature measurement and display technologies.

Feel free to enhance and customize your temperature meter by adding new features or integrating other sensors. This project serves as a solid foundation for exploring environmental monitoring and control systems.
