.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _cpn_water_level:

Water Level Sensor Module
=================================

|img_water_sensor|

The water level sensor detects the water level and transmits the signal to a controller. The controller’s computer compares the measured water level with the preset value to calculate the deviation. Based on this deviation, it sends "on" or "off" commands to the feedwater valve, ensuring the water level in the vessel reaches the desired setting.

**Design and Functionality**
The sensor features ten exposed copper traces: five power traces and five sensor traces arranged in an interleaved pattern. When submerged in water, the traces are bridged, allowing current to flow. The circuit board also includes a power indicator LED, which lights up when the sensor is powered.

The traces function as a variable resistor, with resistance changing based on water immersion:

- More Water: Increased conductivity lowers the resistance.
- Less Water: Reduced conductivity raises the resistance.

The sensor processes this varying resistance into an output voltage signal, which is sent to a microcontroller. The microcontroller uses this signal to determine the water level accurately.

.. warning:: 
    The sensor cannot be fully submerged in water, please only leave the part where the ten traces are located in contact with water. In addition, energizing the sensor in a humid environment will speed up the corrosion of the probe and cut the life of the sensor, so we recommend that you only supply power when taking readings.


**Example**

* :ref:`py_water` (For MicroPython User)
* :ref:`py_iot_sunfounder_controller_plant` (For MicroPython User)
* :ref:`ar_water` (For Arduino User)
.. * :ref:`per_water_tank` (For Piper Make User)