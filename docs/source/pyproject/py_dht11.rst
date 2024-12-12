.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_dht11:

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

Let's write a MicroPython program to read temperature and humidity values from the DHT11 sensor.

.. note::

    * Open the ``6.2_temperature_humidity.py`` from ``pico-2w-kit-main/micropython`` or copy the code into Thonny, then click "Run" or press F5.

    * Ensure the correct interpreter is selected: MicroPython (Raspberry Pi Pico).COMxx. 

     
    
    * Here you need to use the library called ``dht.py``, please check if it has been uploaded to Pico, for a detailed tutorial refer to :ref:`add_libraries_py`.

.. code-block:: python

   from machine import Pin
   import utime
   import dht

   # Initialize the DHT11 sensor
   sensor = dht.DHT11(Pin(16))

   while True:
      try:
         # Trigger measurement
         sensor.measure()
         # Read values
         temperature = sensor.temperature  # In Celsius
         humidity = sensor.humidity        # In Percent
         # Print values
         print("Temperature: {}°C   Humidity: {}%".format(temperature, humidity))
      except OSError as e:
         print("Failed to read sensor.")
      # Wait before the next reading
      utime.sleep(2)

Once the code is running, the temperature and humidity readings will display in the Thonny Shell.

.. code-block::

  Temperature: 29.3°C   Humidity: 60.0%
  Temperature: 29.2°C   Humidity: 60.0%
  Temperature: 29.2°C   Humidity: 60.0%
  Temperature: 29.1°C   Humidity: 60.0%
  Temperature: 29.2°C   Humidity: 60.0%
  Temperature: 29.3°C   Humidity: 60.0%

**Understanding the Code**

#. Import Modules:

   * ``machine.Pin``: For controlling the GPIO pins.
   * ``utime``: Contains time-related functions.
   * ``dht``: The library for DHT sensors.

#. Initialize the Sensor:

   .. code-block:: python

      sensor = dht.DHT11(Pin(16))
      Creates an instance of the DHT11 sensor connected to GP16.

#. Main Loop:

   * ``sensor.measure()``: Triggers the sensor to take a measurement.
   * ``sensor.temperature``: Reads the temperature in Celsius.
   * ``sensor.humidity``: Reads the humidity percentage.
   * ``Exception Handling``: Catches any errors that occur during reading.
   * ``utime.sleep(2)``: Waits 2 seconds between readings.

   .. code-block:: python

      while True:
         try:
            sensor.measure()
            temperature = sensor.temperature
            humidity = sensor.humidity
            print("Temperature: {}°C   Humidity: {}%".format(temperature, humidity))
         except OSError as e:
            print("Failed to read sensor.")
         utime.sleep(2)

**Experimenting Further**

* Convert Temperature to Fahrenheit:

   .. code-block:: python

      temperature_f = temperature * 9 / 5 + 32
      print("Temperature: {}°F   Humidity: {}%".format(temperature_f, humidity))

* Display Readings on an LCD:

  Integrate an LCD display to show the readings without a computer.


* Set Up Alerts:

  Use an LED or buzzer to alert when temperature or humidity exceeds certain thresholds.

**Troubleshooting Tips**

* Incorrect Readings:

  * Ensure the sensor is connected properly.
  * Check for loose wires or poor connections.

* Failed to Read Sensor:

  This may happen occasionally due to timing issues. The code includes a try-except block to handle this.

* Pull-Up Resistor:

  If the sensor doesn't work, ensure that a pull-up resistor is connected between VCC and Data pins if your sensor requires it.

**Conclusion**

In this lesson, you've learned how to use the DHT11 temperature and humidity sensor with the Raspberry Pi Pico 2. Monitoring environmental conditions is a fundamental aspect of many projects, from weather stations to home automation systems.

* `Try Statement - Python Docs <https://docs.python.org/3/reference/compound_stmts.html?#the-try-statement>`_
