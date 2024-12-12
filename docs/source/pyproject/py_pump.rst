.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_pump:

3.6 Pumping
=======================


In this lesson, we'll learn how to control a **small water pump** using the Raspberry Pi Pico 2w 
and an **TA6586 motor driver**. A small centrifugal pump can be used for projects like automatic 
plant watering systems or creating miniature water features. Controlling the pump is similar to 
controlling a DC motor, as it uses the same principles.

Its power component is an electric motor, driven in exactly the same way as a normal motor.

* :ref:`cpn_pump`
* :ref:`cpn_motor`
* :ref:`cpn_ta6586`
* :ref:`cpn_power_module`

**Important Notes Before You Begin**

* **Pump Setup**: Connect the tubing to the pump's outlet. Submerge the pump in water before powering it on.
* **Avoid Dry Running**: Ensure the pump is always submerged. Running the pump dry can cause overheating and damage the motor.
* **Prevent Clogging**: If you're using the pump for watering plants, make sure the water is free of debris to prevent clogging.
* **Priming the Pump**: If water doesn't come out initially, there might be air trapped in the tubing. You may need to prime the pump by allowing water to flow through to remove air bubbles.


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
        - :ref:`cpn_ta6586`
        - 1
        - 
    *   - 6
        - :ref:`cpn_lipo_charger`
        - 1
        -  
    *   - 7
        - 18650 Battery
        - 1
        -  
    *   - 8
        - Battery Holder
        - 1
        -  
    *   - 9
        - :ref:`cpn_pump`
        - 1
        -  


**Important Notes Before You Begin**

* **Pump Setup**: Connect the tubing to the pump's outlet. Submerge the pump in water before powering it on.
* **Avoid Dry Running**: Ensure the pump is always submerged. Running the pump dry can cause overheating and damage the motor.
* **Prevent Clogging**: If you're using the pump for watering plants, make sure the water is free of debris to prevent clogging.
* **Priming the Pump**: If water doesn't come out initially, there might be air trapped in the tubing. You may need to prime the pump by allowing water to flow through to remove air bubbles.

**Schematic**

|sch_pump|


**Wiring**

In this circuit, you will see that the button is connected to the RUN pin. This is because the motor is operating with too much current, which may cause the Pico to disconnect from the computer, and the button needs to be pressed (for the Pico's **RUN** pin to receive a low level) to reset.

|wiring_pump|

**Code**

.. note::

    * Open the ``3.6_pumping.py`` file under the path of ``pico-2w-kit-main/micropython`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.

    * Don't forget to click on the "MicroPython (Raspberry Pi Pico)" interpreter in the bottom right corner. 

    * For detailed tutorials, please refer to :ref:`open_run_code_py`.


.. code-block:: python

    import machine
    import utime

    # Define the control pins connected to the TA6586
    motor1A = machine.Pin(14, machine.Pin.OUT)
    motor2A = machine.Pin(15, machine.Pin.OUT)

    # Start the pump by setting motor1A high and motor2A low
    while True:
        motor1A.high()
        motor2A.low()


When the code is running, the pump starts working and you will see water flowing out of the tube at the same time.

**Understanding the Code**

#. Import Modules:

   * ``machine``: Access to hardware-related functions.
   * ``utime``: Time-related functions for delays.

#. Initialize Control Pins:

   ``motor1A`` and ``motor2A`` control the pump via the TA6586.

   .. code-block:: python

      motor1A = machine.Pin(14, machine.Pin.OUT)
      motor2A = machine.Pin(15, machine.Pin.OUT)

#. Start the Pump:

   Sets the pump to run in one direction by applying a high signal to motor1A and a low signal to motor2A.

   .. code-block:: python

      motor1A.high()
      motor2A.low()



**Troubleshooting Tips**

* Pump Doesn't Start:

  * Check all wiring connections.
  * Make sure the pump is submerged in water.

* Pico Becomes Unresponsive:

  * If the Pico disconnects or the program stops, you may need to reset it.
  * Use the reset connection by momentarily connecting the RUN pin to GND.

* Pump Continues Running After Stopping the Script:

  * The last state of the GPIO pins remains unchanged after stopping the script.
  * Reset the Pico to stop the pump by connecting RUN to GND.

  |wiring_run_reset|

**Safety Precautions**

* Electrical Safety:

  * Be cautious when working with water and electronics.
  * Keep the Pico and other electronic components away from water to prevent damage or injury.

* Pump Care:

  * Do not let the pump run dry.
  * Clean the pump regularly if using it with water that may contain particles.

**Conclusion**

In this lesson, you've learned how to control a small water pump using the Raspberry Pi Pico 2w and an TA6586 motor driver. This setup can be the foundation for projects like automated plant watering systems or miniature fountains.
