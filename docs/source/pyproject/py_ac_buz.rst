.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_ac_buz:

3.1 Beep
==================


In this lesson, we will learn how to make a **buzzer** beep using the Raspberry Pi Pico 2w. A buzzer is a digital output device, just like an LED, and it's very simple to control. We'll use an **active buzzer** for this project, which generates sound when it receives a signal.

* :ref:`cpn_buzzer`

**What is an Active Buzzer?**

An active buzzer has an internal oscillator that makes it easier to use. You only need to send a signal to the buzzer to make it beep—no complex frequency control is required. This is different from a **passive buzzer**, which requires an external signal to generate sound.

|img_buzzer|

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
        - :ref:`cpn_resistor`
        - 1(1KΩ)
        - |link_resistor_buy|
    *   - 7
        - Active :ref:`cpn_buzzer`
        - 1
        - 

**Schematic**

|sch_buzzer|

In this circuit, the buzzer is powered through a transistor (**S8050** NPN). The transistor amplifies the current, making the buzzer sound louder than if it were connected directly to the Pico. 

Here's what happens:

* **GP15** outputs a high signal to control the transistor.
* When the transistor is activated, it allows current to flow through the buzzer, making it beep.

A **1kΩ resistor** is used to limit the current to protect the transistor.

**Wiring**

Make sure you are using the **active buzzer**. You can tell it's the correct one by looking for the sealed back (as opposed to the exposed PCB, which is a passive buzzer).

|img_buzzer|

The buzzer needs to use a transistor when working, here we use S8050 (NPN Transistor).


|wiring_beep|


**Writing the Code**

Let's write a simple MicroPython program to control the buzzer.

.. note::

    * Open the ``3.1_beep.py`` from ``pico-2w-kit-main/micropython`` or copy the code into Thonny, then click "Run" or press F5.
    * Ensure the correct interpreter is selected: MicroPython (Raspberry Pi Pico).COMxx. 
    

.. code-block:: python

    import machine
    import utime

    # Initialize the buzzer pin (GP15)
    buzzer = machine.Pin(15, machine.Pin.OUT)

    while True:
        # Loop to beep the buzzer 4 times
        for i in range(4):
            buzzer.value(1)  # Turn the buzzer on
            utime.sleep(0.3)  # Wait for 0.3 seconds
            buzzer.value(0)  # Turn the buzzer off
            utime.sleep(0.3)  # Wait for 0.3 seconds
        utime.sleep(1)  # Longer pause before the next cycle

When the code is running, you should hear:

* The buzzer will beep 4 times in a row, with a 0.3-second pause between each beep.
* After the 4 beeps, there will be a longer 1-second pause before the cycle repeats.

**Explanation of the Code**

#. Buzzer Initialization:

   * ``buzzer = machine.Pin(15, machine.Pin.OUT``): Initializes GP15 as the output pin to control the buzzer.

#. Main Loop:

   * The ``while True``: loop ensures the code runs indefinitely.
   * Inside the loop, the buzzer is turned on (``buzzer.value(1)``) and off (``buzzer.value(0)``) four times, each with a 0.3-second delay.
   * After the four beeps, there is a 1-second pause before the cycle repeats.


**Experimenting Further**

* **Change the Beep Duration**: Adjust the ``utime.sleep(0.3)`` values to make the beeps longer or shorter.
* **Vary the Number of Beeps**: Change the number of iterations in the loop to make the buzzer beep more or fewer times.
* **Add Button Control**: Try connecting a button to GP14, and modify the code to beep only when the button is pressed.

**Conclusion**

In this lesson, you learned how to control an active buzzer using a transistor and the Raspberry Pi Pico 2w. You now have a basic understanding of how to use a digital output device to create sound in your projects. The same principles can be applied to other output devices, like LEDs, motors, and more.
