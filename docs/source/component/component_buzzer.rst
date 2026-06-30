.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _cpn_buzzer:

Buzzer
=======


Buzzers are electronic components with an integrated structure, commonly powered by DC. They are widely used in a variety of devices, including computers, printers, photocopiers, alarms, electronic toys, automotive electronics, telephones, timers, and other electronic products or audio signaling devices.

Buzzers are categorized into two types: active and passive (as shown in the image below). To identify the type, turn the buzzer so that its pins face upward. A passive buzzer features a green circuit board, while an active buzzer is enclosed with black tape.

|img_buzzer|

Difference Between an Active Buzzer and a Passive Buzzer:

An active buzzer has a built-in oscillating source, allowing it to produce sound as soon as it is powered. In contrast, a passive buzzer lacks an internal oscillating source and will not emit sound if powered by a DC signal. Instead, it requires a square wave with a frequency between 2 kHz and 5 kHz to function. Due to the additional internal circuitry, active buzzers are typically more expensive than passive buzzers.

The electrical symbol for a buzzer is shown below. It features two pins, one positive and one negative. The pin marked with a "+" on the surface indicates the anode, while the other pin represents the cathode.

|img_buzzer_symbol|

You can check the pins of the buzzer, the longer one is the anode and the shorter one is the cathode. Please don't mix them up when connecting, otherwise the buzzer will not make sound. 

`Buzzer - Wikipedia <https://en.wikipedia.org/wiki/Buzzer>`_

.. Example
.. -------------------

.. :ref:`Intruder Alarm`

.. :ref:`Custom Tone`

**Example**

* :ref:`py_ac_buz` (For MicroPython User)
* :ref:`py_pa_buz` (For MicroPython User)
* :ref:`py_light_theremin` (For MicroPython User)
* :ref:`py_alarm_lamp` (For MicroPython User)
* :ref:`py_music_player` (For MicroPython User)
* :ref:`py_fruit_piano` (For MicroPython User)
* :ref:`py_reversing_aid` (For MicroPython User)
* :ref:`py_iot_mqtt_subscribe` (For MicroPython User)
* :ref:`py_iot_ble_piano` (For MicroPython User)
* :ref:`ar_ac_buz` (For Arduino User)
* :ref:`ar_pa_buz` (For Arduino User)

.. * :ref:`per_service_bell` (For Piper Make User)
.. * :ref:`per_reversing_system` (For Piper Make User)
.. * :ref:`per_reaction_game` (For Piper Make User)
