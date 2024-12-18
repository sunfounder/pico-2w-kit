.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ar_transistor:

2.15 Two Types of Transistors: NPN and PNP
=============================================

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
        - PURCHASE LINK
    *   - Pico 2 W Starter Kit	
        - 450+
        - |link_pico2w_kit|

You can also buy them separately from the links below.


.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - COMPONENT INTRODUCTION	
        - QUANTITY
        - PURCHASE LINK

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

.. 1. Connect 3V3 and GND of Pico 2 W to the power bus of the breadboard.
.. #. Connect the anode lead of the LED to the positive power bus via a 220Ω resistor.
.. #. Connect the cathode lead of the LED to the **collector** lead of the transistor.
.. #. Connect the base lead of the transistor to the GP15 pin through a 1kΩ resistor.
.. #. Connect the **emitter** lead of the transistor to the negative power bus.
.. #. Connect one side of the button to the GP14 pin, and use a 10kΩ resistor connect the same side and negative power bus. The other side to the positive power bus.

..     * The color ring of 220Ω resistor is red, red, black, black and brown.
..     * The color ring of the 1kΩ resistor is brown, black, black, brown and brown.
..     * The color ring of the 10kΩ resistor is brown, black, black, red and brown.

**Wiring the PNP (S8550) Transistor**

|sch_s8550|

For the PNP transistor circuit, the button starts with a low signal on GP14 and changes to high when pressed. When GP15 outputs a **low signal**, the PNP transistor conducts, allowing current to flow and lighting up the LED.

|wiring_s8550|

.. 1. Connect 3V3 and GND of Pico 2 W to the power bus of the breadboard.
.. #. Connect the anode lead of the LED to the positive power bus via a 220Ω resistor.
.. #. Connect the cathode lead of the LED to the **emitter** lead of the transistor.
.. #. Connect the base lead of the transistor to the GP15 pin through a 1kΩ resistor.
.. #. Connect the **collector** lead of the transistor to the negative power bus.
.. #. Connect o

**Writing the Code**

.. note::

    * You can open the file ``2.15_transistor.ino`` under the path of ``pico-2 w-kit-main/arduino/2.15_transistor``. 
    * Or copy this code into **Arduino IDE**.
    * Don't forget to select the board(Raspberry Pi Pico) and the correct port before clicking the **Upload** button.



.. code-block:: arduino

    // Define the pins
    const int buttonPin = 14;  // Button connected to GP14
    const int transistorPin = 15;  // Transistor base connected to GP15

    int buttonState = 0;  // Variable to hold the button state

    void setup() {
      pinMode(buttonPin, INPUT);
      pinMode(transistorPin, OUTPUT);
    }

    void loop() {
      // Read the state of the button
      buttonState = digitalRead(buttonPin);

      // control the transistor
      digitalWrite(transistorPin, buttonState);

      delay(10);  // Small delay for debouncing
    }

**Results**

* For NPN Transistor (S8050):

  When you press the button, the LED should turn on.
  When you release the button, the LED should turn off.

* For PNP Transistor (S8550):

  When you press the button, the LED should turn off.
  When you release the button, the LED should turn on.

**Understanding the Code**

#. Reading the Button State:

   Reads the current state of the button.

   .. code-block:: arduino

        buttonState = digitalRead(buttonPin);

#. Controlling the Transistor:

   * **For NPN Transistor**: When the button is pressed (``buttonState`` is HIGH), the transistor is turned on, allowing current to flow and lighting up the LED.
   * **For PNP Transistor**: When the button is pressed (``buttonState`` is HIGH), the transistor is turned off (LOW), and when the button is not pressed, the transistor is turned on.

   .. code-block:: arduino

        digitalWrite(transistorPin, buttonState);


**Further Exploration**

* Control Larger Loads:

  Use transistors to control devices that require more current than the Pico can provide directly, such as motors or relays.

* Transistor as an Amplifier:

  Explore how transistors can be used to amplify signals.

* Experiment with Darlington Pair:

  Use two transistors to create a Darlington pair for higher current gain.

**Conclusion**

In this lesson, you've learned how to use both NPN and PNP transistors to control an LED using a Raspberry Pi Pico and a button. Understanding the differences between NPN and PNP transistors is crucial for designing circuits that require switching or amplification.






