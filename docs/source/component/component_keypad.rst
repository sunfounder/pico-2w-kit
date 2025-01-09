.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _cpn_keypad:

4x4 Keypad
========================


In microcontroller systems, devices requiring multiple keys—such as electronic locks or telephone keypads—often use a matrix keypad, especially when 12 to 16 keys are needed.

A matrix keypad, also known as a row-column keypad, is designed with four I/O lines serving as rows and another four as columns. Each intersection of a row and a column corresponds to a key, resulting in a total of 4×4 keys. This structure efficiently optimizes the use of I/O ports in a microcontroller system.

The keypad's contacts are typically accessible via a header, which can connect to a ribbon cable or be directly inserted into a printed circuit board. In some keypads, each button connects to an individual contact in the header, while all buttons share a common ground connection.


|img_keypad|

More often, the buttons are matrix encoded, meaning that each of them bridges a unique pair of conductors in a matrix. 
This configuration is suitable for polling by a microcontroller, which can be programmed to send an output pulse to each of the four horizontal wires in turn. 
During each pulse, it checks the remaining four vertical wires in sequence, to determine which one, if any, is carrying a signal. 
Pullup or pulldown resistors should be added to the input wires to prevent the inputs of the microcontroller from behaving unpredictably when no signal is present.

* `Keypad - Wikipedia <https://en.wikipedia.org/wiki/Keypad>`_

**Example**

* :ref:`py_keypad` (For MicroPython User)
* :ref:`py_guess_number` (For MicroPython User)
* :ref:`ar_keypad` (For Arduino User)