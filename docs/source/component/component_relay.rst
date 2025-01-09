.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _cpn_relay:

Relay
==========================================

|img_relay|

A relay is a device that connects two or more points or devices in response to an input signal. Essentially, relays provide isolation between the controller and the device, as the device may operate on either AC or DC power. Relays are necessary because microcontrollers, which typically operate on DC, require a mechanism to interface with and control devices operating on different electrical standards.

Relays are particularly useful for controlling large currents or voltages with small electrical signals, making them invaluable in many applications.

Every relay consists of five main components:

**Electromagnet** - It consists of an iron core wrapped with a coil of wire. When electricity flows through the coil, it generates a magnetic field, turning the core into an electromagnet.

**Armature** - The movable magnetic strip, known as the armature, interacts with the coil when current flows through it. The energized coil generates a magnetic field, enabling the armature to make or break connections at the normally open (N/O) or normally closed (N/C) contact points. The armature can operate with both direct current (DC) and alternating current (AC).

**Spring** - When no current flows through the electromagnet's coil, the spring pulls the armature away, preventing the circuit from being completed.

Set of electrical **contacts** - There are two contact points:

-  Normally open - connected when the relay is activated, and disconnected when it is inactive.

-  Normally close - not connected when the relay is activated, and connected when it is inactive.

**Molded frame** - Relays are covered with plastic for protection.

The working principle of a relay is straightforward. When power is supplied to the relay, current flows through the control coil, energizing the electromagnet. This causes the armature to be attracted to the coil, pulling the moving contact down to connect with the normally open (N/O) contact, thereby energizing the load circuit.

To break the circuit, the process is reversed. When the power is removed, the spring pulls the moving contact back to its original position, reconnecting it with the normally closed (N/C) contact. This mechanism enables the relay to control the on/off state of a load circuit efficiently.

|img_relay_sche|


* `Relay - Wikipedia <https://en.wikipedia.org/wiki/Relay>`_

**Example**

* :ref:`py_relay` (For MicroPython User)
* :ref:`py_iot_ble_relay` (For MicroPython User)
* :ref:`ar_relay` (For Arduino User)