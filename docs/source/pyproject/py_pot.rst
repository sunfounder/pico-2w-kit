.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_pot:

2.11 Turn the Knob
===========================

In this lesson, we'll explore how to read analog input using the Raspberry Pi Pico 2 W's built-in Analog-to-Digital Converter (ADC) and use that input to control the brightness of an LED. Specifically, we'll use a potentiometer—a variable resistor—as an analog input device. By turning the knob of the potentiometer, we'll adjust the voltage level read by the Pico, which we'll then use to control the LED's brightness via Pulse Width Modulation (PWM).

**Understanding Analog Input**

So far, we've worked with digital inputs and outputs, which are either ON (high voltage) or OFF (low voltage). However, many real-world signals are analog, meaning they can vary continuously over a range of values. Examples include light intensity, temperature, and sound levels.

The Raspberry Pi Pico 2 W has a built-in ADC that allows it to read analog voltages and convert them into digital values that can be processed in code.

The ADC converts the analog voltage from the potentiometer into a digital value using the formula:

.. code-block::

  Digital Value = (Analog Voltage/3.3V) * 65535


**Pico's ADC Pins**

|pin_adc|

The Pico has three GPIO pins that can be used for analog input:

* **GP26** (ADC0)
* **GP27** (ADC1)
* **GP28** (ADC2)

In addition, there's a fourth ADC channel connected internally to a temperature sensor (ADC4), which we'll explore in later lessons.

* :ref:`cpn_potentiometer`

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
        - :ref:`cpn_resistor`
        - 1(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 7
        - :ref:`cpn_potentiometer`
        - 1
        - |link_potentiometer_buy|


**Schematic**

|sch_pot|

The potentiometer is an analog device and when you turn it in 2 different directions.

Connect the middle pin of the potentiometer to the analog pin GP28. The Raspberry Pi Pico 2 W wcontains a multi-channel, 16-bit analog-to-digital converter. This means that it maps the input voltage between 0 and the operating voltage (3.3V) to an integer value between 0 and 65535, so the GP28 value ranges from 0 to 65535.

The calculation formula is shown below.

    (Vp/3.3V) x 65535 = Ap

Then program the value of GP28 (potentiometer) as the PWM value of GP15 (LED).
This way you will find that by rotating the potentiometer, the brightness of the LED will change at the same time.

**Wiring**



|wiring_pot|


**Writing the Code**

.. note::

  * Open the ``2.11_turn_the_knob.py`` file under the path ``pico-2 w-kit-main/micropython`` or copy the code below into Thonny. Then click "Run Current Script" or press **F5** to run it.
  * Ensure that the "MicroPython (Raspberry Pi Pico).COMxx" interpreter is selected in the bottom right corner of Thonny.
  * For detailed instructions, refer to :ref:`open_run_code_py`.

.. code-block:: python

  import machine
  import utime

  # Initialize ADC on GP28
  potentiometer = machine.ADC(28)

  # Initialize PWM on GP15
  led = machine.PWM(machine.Pin(15))
  led.freq(1000)  # Set PWM frequency to 1000Hz

  while True:
      # Read the analog value (0-65535)
      value = potentiometer.read_u16()
      print("Potentiometer value:", value)

      # Set the LED brightness
      led.duty_u16(value)

      # Small delay to stabilize readings
      utime.sleep_ms(200)

When you run the program, the LED's brightness will change as you turn the potentiometer knob. Additionally, the console will display the current analog value read from the potentiometer.

**Understanding the Code**

#. Analog Reading:

   * ``potentiometer = machine.ADC(28)`` initializes the ADC on pin GP28.
   * ``value = potentiometer.read_u16()`` reads the analog voltage from the potentiometer and returns a 16-bit integer between **0** and **65535**.
     
     * **0** corresponds to **0V**.
     * **65535** corresponds to **3.3V** (the Pico's operating voltage).

#. Controlling the LED with PWM:

   * ``led = machine.PWM(machine.Pin(15))`` sets up PWM on pin GP15.
   * ``led.freq(1000)`` sets the PWM frequency to 1000Hz.
   * ``led.duty_u16(value)`` sets the duty cycle of the PWM signal based on the potentiometer's reading.

     * A higher ``value`` increases the duty cycle, making the LED brighter.
     * A lower ``value`` decreases the duty cycle, dimming the LED.

#. Printing the Value:

   * ``print("Potentiometer value:", value)`` outputs the current analog value to the console for monitoring.


**Experimenting Further**

* **Change the PWM Frequency**: Try different frequencies with ``led.freq()`` and observe the effect on the LED.
  
* **Map the ADC Value**: Introduce a scaling factor or map the ADC value to a different range to see how it affects LED brightness.

* **Use Other ADC Pins**: Connect the potentiometer to GP26 or GP27 and adjust the code accordingly.

**Troubleshooting Tips**

* LED Not Changing Brightness:

  * Ensure the LED and resistor are connected correctly.
  * Verify that the potentiometer is wired properly.

* Incorrect ADC Values:

  * Check the connections to GP28.
  * Make sure the potentiometer's outer pins are connected to 3.3V and GND.

**Conclusion**

By integrating analog input with PWM output, we've created a simple yet powerful way to control the brightness of an LED using a potentiometer. This project demonstrates how to read analog signals and use them to control other components, a fundamental skill in electronics and microcontroller programming.

**References**

* |link_wiki_pwm|
* |link_mpython_adc|