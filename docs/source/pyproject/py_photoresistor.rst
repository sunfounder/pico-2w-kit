.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_photoresistor:

2.12 Feel the Light
=============================

In this lesson, we'll learn how to use a **photoresistor** (also known as a light-dependent resistor or LDR) with the Raspberry Pi Pico 2w to measure light intensity. A photoresistor changes its resistance based on the amount of light it receives: the brighter the light, the lower the resistance. This makes it ideal for detecting changes in ambient light.


* :ref:`cpn_photoresistor`

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
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_photoresistor`
        - 1
        - |link_photoresistor_buy|


**Schematic**

|sch_photoresistor|

In this circuit, a 10K resistor and a photoresistor are connected in series, forming a voltage divider. GP28 reads the voltage across the photoresistor, while the 10K resistor provides protection by limiting current.

* **Bright Light**: The photoresistor's resistance decreases, lowering its voltage and the GP28 reading. In strong light, its resistance approaches zero, and GP28 reads close to 0. At this time, the 10K resistor plays a protective role, so that 3.3V and GND are not connected together, resulting in a short circuit.
* **Darkness**: The photoresistor's resistance increases, raising its voltage and the GP28 value. In complete darkness, its resistance is nearly infinite (the 10K resistor is negligible), and GP28 reads close to 65535.

The calculation formula is shown below.

.. code-block::

  Digital Value = (Analog Voltage/3.3V) * 65535



**Wiring**

|wiring_photoresistor|

**Writing the Code**

We'll write a MicroPython program to read the analog value from the photoresistor and display it.

.. note::

  * Open the ``2.12_feel_the_light.py`` file under the path ``pico-2w-kit-main/micropython`` or copy the code below into Thonny. Then click "Run Current Script" or press **F5** to run it.
  * Ensure that the "MicroPython (Raspberry Pi Pico).COMxx" interpreter is selected in the bottom right corner of Thonny.
  * For detailed instructions, refer to :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    # Initialize ADC on GP28
    photoresistor = machine.ADC(28)

    while True:
        # Read the analog value (0-65535)
        light_value = photoresistor.read_u16()
        print("Light value:", light_value)
        utime.sleep(0.5)

When the code is running, observe the values printed in the console.

* Cover the photoresistor with your hand to simulate darkness; the value should increase.
* Shine a light or a flashlight on the photoresistor; the value should decrease.

**Understanding the Code**

#. Import Modules:

   * ``machine``: Provides access to hardware-related functions.
   * ``utime``: Allows us to use time-related functions like sleep.

#. Initialize the ADC Pin:

   * ``photoresistor = machine.ADC(28)``: Sets up GP28 as an analog input to read voltage levels.

#. Main Loop:

   ``while True``: Starts an infinite loop.
   ``light_value = photoresistor.read_u16()``: Reads the analog value from the photoresistor. The value ranges from 0 (0V) to 65535 (3.3V).
   ``print("Light value:", light_value)``: Outputs the light value to the console.
   ``utime.sleep(0.5)``: Pauses the loop for 0.5 seconds before the next reading.


**Experimenting Further**

* Calibrating the Readings: 

  Map the analog values to a percentage or a more meaningful scale.

  .. code-block:: python
  
      import machine
      import utime
  
      photoresistor = machine.ADC(28)
  
      while True:
          light_value = photoresistor.read_u16()
          light_percentage = (light_value / 65535) * 100
          print("Light level: {:.2f}%".format(light_percentage))
          utime.sleep(0.5)

* Control an LED Based on Light Intensity:

  Use the light sensor to turn an LED on in the dark and off in bright light.

  .. code-block:: python

    import machine
    import utime

    photoresistor = machine.ADC(28)
    led = machine.Pin(15, machine.Pin.OUT)

    while True:
        light_value = photoresistor.read_u16()
        if light_value > 50000:
            led.value(1)  # Turn on LED in darkness
        else:
            led.value(0)  # Turn off LED in bright light
        utime.sleep(0.5)

* Create a Light-Activated Alarm or Notification: Trigger an action when light levels change significantly.

**Conclusion**

By using a photoresistor with the Raspberry Pi Pico 2w, you've learned how to read analog inputs and respond to changes in environmental light. This knowledge can be applied to various projects, such as automatic lighting systems, light-following robots, or security devices that react to changes in lighting.


