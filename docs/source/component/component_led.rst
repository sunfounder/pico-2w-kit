.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _cpn_led:

LED
==========

|img_led|

A semiconductor light-emitting diode is a component that converts electrical energy into light energy through a PN junction. Based on wavelength, these diodes can be classified into laser diodes, infrared light-emitting diodes, and visible light-emitting diodes, commonly referred to as LEDs.

Due to the diode's unidirectional conductivity, current flows in the direction indicated by the arrow in its circuit symbol. To operate an LED, the anode must be connected to a positive power source and the cathode to a negative one, allowing the LED to emit light.

|img_led_symbol|

An LED has two pins. The longer one is the anode, and shorter one, the cathode. Pay attention not to connect them inversely. There is fixed forward voltage drop in the LED, so it cannot be connected with the circuit directly because the supply voltage can outweigh this drop and cause the LED to be burnt. The forward voltage of the red, yellow, and green LED is 1.8 V and that of the white one is 2.6 V. Most LEDs can withstand a maximum current of 20 mA, so we need to connect a current limiting resistor in series.                   

The formula of the resistance value is as follows:

    R = (Vsupply – VD)/I

**R** stands for the resistance value of the current limiting resistor, **Vsupply** for voltage supply, **VD** for voltage drop and **I** for the working current of the LED.

Here is the detailed introduction for the LED: `LED - Wikipedia <https://en.wikipedia.org/wiki/Light-emitting_diode>`_.

.. **Example**

.. * :ref:`Hello, Breadboard!` (For MicroPython User)
.. * :ref:`fading_led_micropython` (For MicroPython User)
.. * :ref:`fading_led_arduino` (For C/C++(Arduino) User)
.. * :ref:`hello_led_arduino` (For C/C++(Arduino) User)


**Example**

* :ref:`py_led` (For MicroPython User)
* :ref:`py_fade` (For MicroPython User)
* :ref:`py_alarm_lamp` (For MicroPython User)
* :ref:`py_traffic_light` (For MicroPython User)
* :ref:`py_reversing_aid` (For MicroPython User)
* :ref:`py_iot_read_ble` (For MicroPython User)
* :ref:`py_iot_ble_relay` (For MicroPython User)
* :ref:`ar_led` (For Arduino User)
* :ref:`ar_fade` (For Arduino User)
.. * :ref:`per_blink` (For Piper Make User)
.. * :ref:`per_button` (For Piper Make User)
.. * :ref:`per_service_bell` (For Piper Make User)
.. * :ref:`per_reversing_system` (For Piper Make User)
.. * :ref:`per_reaction_game` (For Piper Make User)