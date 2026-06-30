.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _cpn_pir:

PIR Motion Sensor Module
==================================

|img_pir|

The PIR (Passive Infrared) sensor detects infrared radiation, enabling it to sense the presence of organisms that emit heat.

The sensor is divided into two slots connected to a differential amplifier. When a stationary object is in front of the sensor, both slots receive an equal amount of infrared radiation, resulting in zero output. However, when a moving object passes in front of the sensor, one slot detects more radiation than the other. This imbalance causes the output to fluctuate between high and low. These fluctuations in output voltage indicate motion detection.

|img_PIR_working_principle|

After the sensing module is wired, there is a one-minute initialization. During the initialization, module will output for 0~3 times at intervals. Then the module will be in the standby mode. Please keep the interference of light source and other sources away from the surface of the module so as to avoid the misoperation caused by the interfering signal. Even you'd better use the module without too much wind, because the wind can also interfere with the sensor.

|img_pir_back|

**Distance Adjustment**

Turning the knob of the distance adjustment potentiometer clockwise, the range of sensing distance increases, and the maximum sensing distance range is about 0-7 meters. If turn it anticlockwise, the range of sensing distance is reduced, and the minimum sensing distance range is about 0-3 meters.

**Delay adjustment**

Rotate the knob of the delay adjustment potentiometer clockwise, you can also see the sensing delay increasing. The maximum of the sensing delay can reach up to 300s. On the contrary, if rotate it anticlockwise, you can shorten the delay with a minimum of 5s. 

**Two Trigger Modes**

Choosing different modes by using the jumper cap.

* **H**: Repeatable trigger mode, after sensing the human body, the module outputs high level. During the subsequent delay period, if somebody enters the sensing range,the output will keep being the high level.
* **L**: Non-repeatable trigger mode, outputs high level when it senses the human body. After the delay, the output will change from high level into low level automatically.

.. Example 
.. -------------------

.. :ref:`Intruder Alarm`


**Example**

* :ref:`py_pir` (For MicroPython User)
* :ref:`py_passage_counter` (For MicroPython User)
* :ref:`ar_pir` (For Arduino User)

.. * :ref:`per_lucky_cat` (For Piper Make User)
