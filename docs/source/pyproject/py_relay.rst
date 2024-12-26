.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_relay:

2.16 Control Another Circuit
=================================

In this lesson, we will learn how to control another circuit using a **relay** and the Raspberry Pi Pico 2 W. A relay acts like a switch controlled by a low-voltage circuit (like Pico) to operate a high-voltage circuit. For example, you can use a relay to turn on a lamp or any other device, making it possible to automate electrical appliances.

.. warning::
    Modification of electrical appliances comes with great danger, do not try it lightly, please do it under the guidance of professionals.

* :ref:`cpn_relay`

Here we only use a simple circuit powered by a breadboard power module as an example to show how to control it using relay.

* :ref:`cpn_power_module`

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
        - :ref:`cpn_transistor`
        - 1(S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_diode`
        - 1
        - 
    *   - 7
        - :ref:`cpn_relay`
        - 1
        - |link_relay_buy|


**Wiring**

First, build a low-voltage circuit for controlling a relay.
Driving the relay requires a high current, so a transistor is needed, and here we use the S8050.

|sch_relay_1|

* Relay Activation:

  * The relay's coil is energized by the transistor when the Pico outputs a **high signal** (3.3V) to GP15.
  * The transistor allows current to flow through the relay, activating the switch inside.
  * The relay makes a "click" sound when switching, indicating the control of the load circuit.

* Flyback Diode:

  * The diode is placed across the relay coil to protect the transistor from voltage spikes that occur when the relay is turned off.

**Wiring Diagram**

|wiring_relay_1|



The following code will control the relay, switching the connected circuit on and off every two seconds.

.. note::

    * Open the ``2.16_control_another_circuit.py`` from ``pico-2w-kit-main/micropython`` or copy the code into Thonny, then click "Run" or press F5.
    * Ensure the correct interpreter is selected: MicroPython (Raspberry Pi Pico).COMxx. 

.. code-block:: python

    import machine
    import utime

    # Initialize the relay pin on GP15
    relay = machine.Pin(15, machine.Pin.OUT)

    while True:
        relay.value(1)  # Turn the relay on
        utime.sleep(2)  # Wait for 2 seconds
        relay.value(0)  # Turn the relay off
        utime.sleep(2)  # Wait for 2 seconds

When the code is running, you should hear a "click" sound from the relay every two seconds, indicating the circuit is being switched on and off.

**Experimenting Further**

* **Set a Timer**: Modify the code to turn the relay on for 10 minutes and then automatically turn it off.
* **Control Home Appliances**: With appropriate guidance, you can connect high-voltage devices to the relay for automation tasks such as turning lights or fans on and off.

  * The circuit should look like this: To demonstrate controlling an external circuit safely, we'll add an external 5V power supply (through a breadboard power module) to power an LED. This simulates how you could control higher voltage devices (like home appliances) using the relay. Here's how to modify the circuit:

    |sch_relay_2|
  
    |wiring_relay_2|

  * Code to Control the Relay:

    .. code-block:: python

        import machine
        import utime

        # Initialize the relay pin on GP15
        relay = machine.Pin(15, machine.Pin.OUT)

        while True:
            relay.value(1)  # Turn the relay on
            utime.sleep(2)  # Wait for 2 seconds
            relay.value(0)  # Turn the relay off
            utime.sleep(2)  # Wait for 2 seconds

    When the relay is activated (GP15 outputs high), the Normally Open (NO) and Common (C) pins of the relay connect, allowing the external 5V power to flow through the LED. The LED will light up, simulating how a relay can control an external appliance.

    When the relay is deactivated (GP15 outputs low), the Normally Open (NO) pin disconnects from the Common (C) pin, cutting off the external power, and the LED turns off.

**Safety Considerations for Controlling Real Appliances**

This example uses an LED and a 5V power source to demonstrate relay control. If you are controlling higher voltage devices (like household appliances), ensure:

* **Proper Voltage Rating**: Use a relay rated for the appropriate voltage and current for your appliance.
* **Isolation**: For safety, ensure proper isolation between the low-voltage control circuit (like the Pico) and the high-voltage appliance circuit.
* **Fuse Protection**: Consider adding fuses or circuit breakers to protect against short circuits or overloads.
* **Professional Guidance**: When working with high-voltage circuits, always seek professional guidance to ensure safe operation.

This project can serve as the basis for home automation, such as controlling lamps, fans, or other devices based on timers or sensors connected to the Raspberry Pi Pico 2.

**Using the NC Terminal**

* If you connect your controlled circuit between COM and NC:

  * The circuit will be closed (ON) when the relay is not energized.
  * The circuit will be open (OFF) when the relay is energized.
  * Example: Controlling an External Device
  * Warning: Do not attempt to control high-voltage devices without proper knowledge and safety precautions.

* If you want to control a small DC motor or another device:

  * Replace the LED with the device you want to control.
  * Ensure the device's voltage and current requirements are compatible.
  * Provide an appropriate power supply for the device.
  * Connect the device in series with the relay's COM and NO (or NC) terminals.


**Conclusion**

By using the relay to control an external circuit, you've learned how to switch on and off external devices, such as LEDs or even higher voltage appliances. This opens the door to creating automated smart devices that can be controlled through code, offering endless possibilities for home automation and other projects.
