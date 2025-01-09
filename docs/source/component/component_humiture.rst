.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _cpn_dht11:

DHT11 Humiture Sensor
=============================

The DHT11 digital temperature and humidity sensor is a composite sensor that provides calibrated digital output for both temperature and humidity. It combines advanced digital signal processing with reliable temperature and humidity sensing technologies to deliver high reliability and excellent long-term stability.

The sensor integrates a resistive humidity sensing component and an NTC thermistor for temperature measurement, paired with a high-performance 8-bit microcontroller for precise data processing.

.. The schematic diagram of the Humiture Sensor Module is as shown following: |img_Hum-sch| 

Only three pins are available for use: VCC, GND, and DATA. 
The communication process begins with the DATA line sending start signals to DHT11, and DHT11 receives the signals and returns an answer signal. 
Then the host receives the answer signal and begins to receive 40-bit humiture data (8-bit humidity integer + 8-bit humidity decimal + 8-bit temperature integer + 8-bit temperature decimal + 8-bit checksum).

|img_Dht11|

**Features**

    #. Humidity measurement range: 20 - 90%RH
    #. Temperature measurement range: 0 - 60℃
    #. Output digital signals indicating temperature and humidity
    #. Working voltage:DC 5V; PCB size: 2.0 x 2.0 cm
    #. Humidity measurement accuracy: ±5%RH
    #. Temperature measurement accuracy: ±2℃


* `DHT11 Datasheet <http://wiki.sunfounder.cc/images/c/c7/DHT11_datasheet.pdf>`_

**Example**

* :ref:`py_dht11` (For MicroPython User)
* :ref:`py_iot_adafruitio` (For MicroPython User)
* :ref:`py_iot_sunfounder_controller_plant` (For MicroPython User)
* :ref:`py_iot_ble_home` (For MicroPython User)
* :ref:`ar_dht11` (For Arduino User)