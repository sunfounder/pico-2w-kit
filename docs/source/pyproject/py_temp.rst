.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_temp:


2.13 Thermometer
===========================

In this lesson, we'll learn how to use a **thermistor** with the Raspberry Pi Pico 2 W to measure temperature. A thermistor is a type of resistor whose resistance varies significantly with temperature. Specifically, we'll use a Negative Temperature Coefficient (NTC) thermistor, which decreases its resistance as the temperature increases.


* :ref:`cpn_thermistor`

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


**Understanding the Thermistor**

An NTC thermistor is a temperature-sensitive resistor. Its resistance decreases as the temperature rises. By incorporating it into a voltage divider circuit, we can measure the voltage across it, which changes with temperature. Using the Raspberry Pi Pico 2 W's analog-to-digital converter (ADC), we can read this voltage and calculate the corresponding temperature.

**Circuit Diagram**

|sch_temp|

In this circuit, a 10K resistor and an NTC thermistor form a voltage divider, with GP28 reading the voltage across the thermistor. The 10K resistor also provides protection by limiting current.

* **High Temperature**: The thermistor's resistance decreases, lowering its voltage and the GP28 reading. At high enough temperatures, resistance approaches zero, and GP28 reads close to 0.
* **Low Temperature**: The thermistor's resistance increases, raising its voltage and the GP28 value. In extreme cold, resistance becomes nearly infinite, and GP28 reads close to 65535.

The 10K resistor ensures 3.3V and GND are not directly connected, preventing a short circuit.

**Wiring Diagram**

|wiring_temp|
 
.. #. Connect 3V3 and GND of Pico 2 W to the power bus of the breadboard.
.. #. Connect one lead of the thermistor to the GP28 pin, then connect the same lead to the positive power bus with a 10K ohm resistor.
.. #. Connect another lead of thermistor to the negative power bus.

.. note::
    * The thermistor is black and marked 103.
    * The color ring of the 10K ohm resistor is red, black, black, red and brown.

**Writing the Code**

We'll write a MicroPython program to read the analog value from the thermistor, calculate the temperature in Celsius and Fahrenheit, and display it.

.. note::

    * Open the ``2.13_thermometer.py`` from ``pico-2w-kit-main/micropython`` or copy the code into Thonny, then click "Run" or press F5.

    * Ensure the correct interpreter is selected: MicroPython (Raspberry Pi Pico).COMxx. 

.. code-block:: python

    import machine
    import utime
    import math

    # Constants
    BETA = 3950  # Beta coefficient of the thermistor
    T0 = 298.15  # Reference temperature (25°C in Kelvin)
    R0 = 10000   # Resistance at T0 (10 kΩ)

    # Initialize ADC on GP28
    thermistor = machine.ADC(28)

    while True:
        # Read the analog value (0-65535)
        analog_value = thermistor.read_u16()

        # Convert analog value to voltage
        voltage = analog_value * 3.3 / 65535

        # Calculate thermistor resistance
        Rt = (voltage * R0) / (3.3 - voltage)

        # Calculate temperature in Kelvin using the Beta formula
        tempK = 1 / ( (1 / T0) + (1 / BETA) * math.log(Rt / R0) )

        # Convert Kelvin to Celsius
        tempC = tempK - 273.15

        # Convert Celsius to Fahrenheit
        tempF = tempC * 9 / 5 + 32

        # Print the results
        print('Temperature: {:.2f}°C  {:.2f}°F'.format(tempC, tempF))

        # Wait before the next reading
        utime.sleep(2)

When the code is running, the console will display the temperature in Celsius and Fahrenheit.

* Try touching the thermistor to see the temperature increase.
* Use ice or a cold object to observe the temperature decrease.

**Understanding the Code**

#. Import Modules:

   * ``machine``: Provides access to hardware-related functions.
   * ``utime``: Allows us to use time-related functions like sleep.
   * ``math``: Contains mathematical functions like log.

#. Constants:

   * ``BETA``: The Beta coefficient of the thermistor (provided in the datasheet, commonly around 3950).
   * ``T0``: Reference temperature in Kelvin (25°C + 273.15).
   * ``R0``: Resistance of the thermistor at T0 (10 kΩ).

#. Initialize the ADC Pin:

   * ``thermistor = machine.ADC(28)``: Sets up GP28 as an analog input.

#. Main Loop:

   * ``analog_value = thermistor.read_u16()``: Reads the raw analog value.
   * ``voltage = analog_value * 3.3 / 65535``: Converts the raw value to a voltage.
   * ``Rt = (voltage * R0) / (3.3 - voltage)``: Uses the voltage divider formula to find the thermistor's resistance.
   * ``tempK = 1 / ( (1 / T0) + (1 / BETA) * math.log(Rt / R0) )``: Uses the Steinhart-Hart equation simplified for a single Beta value.
   * Convert Kelvin to Celsius and Fahrenheit:
     
     .. code-block:: python
    
        tempC = tempK - 273.15
        tempF = tempC * 9 / 5 + 32

   * ``print('Temperature: {:.2f}°C {:.2f}°F'.format(tempC, tempF))``: Print the Results
   * ``utime.sleep(2)``: Waits 2 seconds before taking the next reading.


**Understanding the Temperature Calculation**

* Steinhart-Hart Equation:

The Steinhart-Hart equation provides a model of the thermistor's resistance as a function of temperature:

|temp_format|

* ``T`` is the temperature of the thermistor in Kelvin.
* ``T0`` is a reference temperature, usually at 25°C (which is 273.15 + 25 in Kelvin).
* ``B`` is the beta parameter of the material, the beta coefficient of the NTC thermistor used in this kit is 3950.
* ``R`` is the resistance we measure.
* ``R0`` is the resistance at the reference temperature T0, the resistance of the NTC thermistor in this kit at 25°C is 10 kilohms.

**Safety Note**

Be careful when applying heat to the thermistor. Do not expose it to high temperatures that could damage it or the Raspberry Pi Pico 2.

**Experimenting Further**

* **Data Logging**: Modify the code to log temperature readings to a file on the Pico.
* **Temperature Thresholds**: Add conditions to trigger actions when the temperature exceeds or falls below certain values (e.g., turn on an LED or activate a buzzer).
* **Display Output**: Connect an LCD or OLED display to show the temperature readings.

**Conclusion**

By using a thermistor with the Raspberry Pi Pico 2 W, you've created a basic thermometer capable of measuring temperature changes. This project demonstrates how to read analog inputs, perform calculations, and interpret sensor data to derive meaningful information.



