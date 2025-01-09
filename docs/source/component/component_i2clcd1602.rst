.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _cpn_i2c_lcd:

I2C LCD1602
==============

|i2c_lcd1602|

* **GND**: Ground
* **VCC**: Voltage supply, 5V.
* **SDA**: Serial data line. Connect to VCC through a pullup resistor.
* **SCL**: Serial clock line. Connect to VCC through a pullup resistor.

As we know, LCDs and other displays greatly enhance human-machine interaction. However, they share a common drawback: connecting them to a controller requires multiple I/O pins, which can quickly consume the available ports and limit the controller's ability to perform other functions.

To address this issue, the LCD1602 with an I2C module was developed. The I2C module features a built-in PCF8574 chip that converts I2C serial data into parallel data, allowing the LCD to operate while significantly reducing the number of I/O pins required.

* `PCF8574 Datasheet <https://www.ti.com/lit/ds/symlink/pcf8574.pdf?ts=1627006546204&ref_url=https%253A%252F%252Fwww.google.com%252F>`_

**I2C Address**

The default address is basically 0x27, in a few cases it may be 0x3F.

Taking the default address of 0x27 as an example, the device address can be modified by shorting the A0/A1/A2 pads; in the default state, A0/A1/A2 is 1, and if the pad is shorted, A0/A1/A2 is 0.

|i2c_address|

**Backlight/Contrast**

Backlight can be enabled by jumper cap, unplugg the jumper cap to disable the backlight. The blue potentiometer on the back is used to adjust the contrast (the ratio of brightness between the brightest white and the darkest black).


|back_lcd1602|

* **Shorting Cap**: Backlight can be enabled by this cap, unplugg this cap to disable the backlight.
* **Potentiometer**: It is used to adjust the contrast (the clarity of the displayed text), which is increased in the clockwise direction and decreased in the counterclockwise direction.




**Example**

* :ref:`py_lcd` (For MicroPython User)
* :ref:`py_room_temp` (For MicroPython User)
* :ref:`py_guess_number` (For MicroPython User)
* :ref:`py_iot_openweather` (For MicroPython User)
* :ref:`ar_lcd` (For Arduino User)