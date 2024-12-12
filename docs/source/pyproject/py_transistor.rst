.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_transistor:

2.15 Two Kinds of Transistors
==========================================

In this lesson, we'll explore two types of transistors: the **S8050 (NPN)** and the **S8550 (PNP)**. Transistors are commonly used as electronic switches, and we’ll see how both types can be used to control an LED with a button.

|img_NPN&PNP|

* **NPN (S8050)**: This type of transistor allows current to flow from the **collector** to the **emitter** when a high signal is applied to the **base**.
* **PNP (S8550)**: For PNP transistors, current flows from the **emitter** to the **collector** when a low signal is applied to the **base**.


While both transistors serve similar purposes, they behave oppositely when it comes to signal control. Let’s use these transistors to control an LED based on button input.


:ref:`cpn_transistor`

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
        - :ref:`cpn_pico_w`
        - 1
        - |link_picow_buy|
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
        - :ref:`cpn_resistor`
        - 3(220Ω, 1KΩ, 10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 7
        - :ref:`cpn_button`
        - 1
        - |link_button_buy|
    *   - 8
        - :ref:`cpn_transistor`
        - 1(S8050/S8550)
        - |link_transistor_buy|


**Way to connect NPN (S8050) transistor**

|sch_s8050|

In this circuit, pressing the button sends a **high signal** to the GP14 pin. When GP15 outputs a high signal, the NPN transistor conducts, allowing current to flow through the LED, lighting it up.


|wiring_s8050|

**Way to connect PNP(S8550) transistor**

|sch_s8550|

For the PNP transistor circuit, the button starts with a low signal on GP14 and changes to high when pressed. When GP15 outputs a **low signal**, the PNP transistor conducts, allowing current to flow and lighting up the LED.

|wiring_s8550|



**Writing the Code**

Both the NPN and PNP transistors can be controlled with the same code. The button's status is read, and depending on whether it's pressed or not, the Pico outputs a high or low signal to GP15.

.. note::

    * Open the ``2.15_transistor.py`` from ``pico-2w-starter-kit-main/micropython`` or copy the code into Thonny, then click "Run" or press F5.
    * Ensure the correct interpreter is selected: MicroPython (Raspberry Pi Pico).COMxx. 
    

.. code-block:: python

    import machine

    # Initialize the button and signal pins
    button = machine.Pin(14, machine.Pin.IN)
    signal = machine.Pin(15, machine.Pin.OUT)

    while True:
        button_status = button.value()
        if button_status == 1:
            signal.value(1)  # Send high signal to the transistor
        else:
            signal.value(0)  # Send low signal to the transistor


**Results**

* NPN Circuit (S8050):

  The LED lights up when the button is pressed because the NPN transistor conducts when a high signal is applied to its base.

* PNP Circuit (S8550):

  The LED lights up when the button is released because the PNP transistor conducts when a low signal is applied to its base.

Both circuits demonstrate how transistors can be used to control current flow based on different types of signals.

**Conclusion**

By experimenting with these two transistors, you gain a better understanding of how NPN and PNP transistors function and how to use them in circuits to control electronic devices.

