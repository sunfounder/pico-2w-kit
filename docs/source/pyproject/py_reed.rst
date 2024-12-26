.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_reed:

2.9 Feel the Magnetism
================================

In this lesson, we'll explore how to use a **reed switch** with the Raspberry Pi Pico 2 W to detect the presence of a magnetic field. A reed switch is a simple electrical switch that operates using a magnetic field. When a magnet comes near the switch, its internal contacts close, completing an electrical circuit.
* :ref:`cpn_reed`

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
        - :ref:`cpn_reed`
        - 1
        - 

**Understanding the Reed Switch**

A reed switch consists of two thin metal reeds sealed within a glass capsule. These reeds are made of ferromagnetic material and are positioned slightly apart. In the absence of a magnetic field, the reeds are separated, and the switch is **open**. When a magnet comes near the switch, the reeds become magnetized, attract each other, and close the circuit.

* **No Magnet Nearby**: Switch is **open**; the circuit is incomplete.
* **Magnet Nearby**: Switch is **closed**; the circuit is complete.

|img_reed_sche|

**Schematic**

|sch_reed|

By default, GP14 is low; and will go high when the magnet is near the reed switch.

The purpose of the 10K resistor is to keep the GP14 at a steady low level when no magnet is near.

* **No Magnet Nearby**:

  * The reed switch is **open**.
  * **GP14** is connected to **GND** through the pull-down resistor.
  * The GPIO pin reads **LOW** (0).

* **Magnet Nearby**:

  * The reed switch is **closed**.
  * **GP14** is connected to **3.3V** through the reed switch.
  * The GPIO pin reads **HIGH** (1).

**Wiring**

|wiring_reed|

**Writing the Code**

We'll write a MicroPython program that detects when a magnet is near the reed switch and prints a message accordingly.

.. note::

  * Open the ``2.9_feel_the_magnetism.py`` from ``pico-2w-kit-main/micropython`` or copy the code into Thonny, then click "Run" or press F5.
  * Ensure the correct interpreter is selected: MicroPython (Raspberry Pi Pico).COMxx. 
  
.. code-block:: python

    import machine
    import utime

    # Initialize GP14 as an input pin
    reed_switch = machine.Pin(14, machine.Pin.IN)

    while True:
        if reed_switch.value() == 1:
            print("Magnet detected!")
            utime.sleep(1)  # Delay to avoid multiple detections

When the code is running, you will observe the following phenomenon:

* **No Magnet Nearby**: No message should appear.
* **Bring a Magnet Close**: "Magnet detected!" should appear in the console.
* **Move Magnet Away**: The message stops appearing.

**Understanding the Code**

#. Import Modules:

   * ``import machine``: Access to hardware functions.
   * ``import utime``: Time-related functions.

#. Initialize the Reed Switch Pin:

   * ``reed_switch = machine.Pin(14, machine.Pin.IN)``: Sets up GP14 as an input pin.

#. Main Loop:

   * ``while True``: Starts an infinite loop.
   * ``if reed_switch.value() == 1``: Checks if a magnet is near (GPIO pin reads HIGH).
   * ``print("Magnet detected!")``: Outputs a message.
   * ``utime.sleep(1)``: Adds a delay to prevent rapid repeated messages.

**Using Interrupts for Efficient Detection**

Instead of constantly polling the reed switch in a loop, we can use an interrupt to detect changes in the reed switch state more efficiently.

Using interrupts enhances efficiency by eliminating the need for continuous checking of the reed switch state and improves responsiveness by immediately calling the handler function when the event occurs.

Modified code using interrupts. When you bring a magnet close to the reed switch, "Magnet detected!" will appear. The main program remains free to perform other tasks.

.. code-block:: python

    import machine

    # Initialize GP14 as an input pin with internal pull-down resistor
    reed_switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

    def magnet_detected(pin):
        print("Magnet detected!")

    # Set up an interrupt on the rising edge (LOW to HIGH transition)
    reed_switch.irq(trigger=machine.Pin.IRQ_RISING, handler=magnet_detected)

* ``def magnet_detected(pin)``: This function is called automatically when the interrupt is triggered.
    
  * ``print("Magnet detected!")``: Outputs a message when a magnet is detected.

* ``reed_switch.irq(trigger=machine.Pin.IRQ_RISING, handler=magnet_detected)``: Configures an interrupt on the reed switch pin.
     
  * ``trigger=machine.Pin.IRQ_RISING``: The interrupt triggers on a rising edge (when the pin value goes from LOW to HIGH).
  * ``handler=magnet_detected``: Specifies the function to call when the interrupt occurs.

**Practical Applications**

* **Security Systems**: Detect when a door or window is opened.
* **Position Sensing**: Determine the position of moving parts in machinery.
* **Proximity Detection**: Trigger events when a magnetic object comes near.

**Experimenting Further**

* Control an LED:

  Connect an LED to another GPIO pin (e.g., GP15) with a suitable resistor. Modify the interrupt handler to turn the LED on when a magnet is detected.
  
  .. code-block:: python
  
      import machine
  
      reed_switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
      led = machine.Pin(15, machine.Pin.OUT)
  
      def magnet_detected(pin):
          led.value(1)  # Turn on the LED
  
      # Set up an interrupt on the rising edge
      reed_switch.irq(trigger=machine.Pin.IRQ_RISING, handler=magnet_detected)
  
      # Main loop
      while True:
          # Turn off the LED when the magnet is not present
          if reed_switch.value() == 0:
              led.value(0)
          machine.sleep(100)
        
* Detect Magnet Removal:

  Set up another interrupt for the falling edge (when the magnet is moved away).

  .. code-block:: python

    def magnet_removed(pin):
        print("Magnet removed!")

    reed_switch.irq(trigger=machine.Pin.IRQ_FALLING, handler=magnet_removed)

**Conclusion**

Using a reed switch with the Raspberry Pi Pico 2 W allows you to detect the presence of a magnetic field, enabling a wide range of applications from security systems to interactive projects. Understanding how to wire the reed switch and utilize interrupts enhances your ability to create efficient and responsive programs.

**References**

* |link_mpython_irq|