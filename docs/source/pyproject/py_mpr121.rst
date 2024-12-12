.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_mpr121:

4.3 Electrode Keyboard
================================

In this lesson, we'll learn how to use the **MPR121 capacitive touch sensor** to create a touch-sensitive keyboard with the Raspberry Pi Pico 2w. The MPR121 allows you to detect touch inputs on up to 12 electrodes, which can be connected to conductive materials like wires, foil, or even fruits like bananas!

* :ref:`cpn_mpr121`

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
        - :ref:`cpn_mpr121`
        - 1
        - 

**Understanding the MPR121 Sensor**

The **MPR121** is a capacitive touch sensor controller that communicates via the I2C interface. It can handle up to 12 touch inputs, making it ideal for creating interactive projects with multiple touch points.

The MPR121 sensor detects changes in capacitance on its electrodes. When you touch an electrode, the capacitance changes, and the sensor registers a touch.The sensor communicates this information over I2C to the Raspberry Pi Pico 2w.

**Schematic**

|sch_mpr121_ar|


**Wiring**

|wiring_mpr121_ar|

* Connect wires or conductive materials to the electrode pins (labeled **E0** to **E11**) on the MPR121.
* You can attach the other ends of the wires to conductive objects like fruits, aluminum foil shapes, or touchpads.

**Wiring Diagram**

|wiring_mpr121_ar|

* Connect wires or conductive materials to the electrode pins (labeled **E0** to **E11**) on the MPR121.
* You can attach the other ends of the wires to conductive objects like fruits, aluminum foil shapes, or touchpads.

**Writing the Code**

Let's write a MicroPython program to detect touch inputs on the electrodes and print out which ones are touched.

.. note::

    * Open the ``4.3_electrode_keyboard.py`` from ``pico-2w-kit-main/micropython`` or copy the code into Thonny, then click "Run" or press F5.
    * Ensure the correct interpreter is selected: MicroPython (Raspberry Pi Pico).COMxx. 
    * Here you need to use the library called ``mpr121.py``, please check if it has been uploaded to Pico, for a detailed tutorial refer to :ref:`add_libraries_py`.

.. code-block:: python
    
    from mpr121 import MPR121
    from machine import Pin, I2C
    import utime

    i2c = I2C(0, sda=Pin(4), scl=Pin(5))
    mpr = MPR121(i2c)

    # check all keys
    while True:
        value = mpr.get_all_states()
        if len(value) != 0:
            print(value)
        utime.sleep_ms(100)

After running the program, touch the connected electrodes or conductive objects. Observe the printed output in the Thonny Shell. You should see messages indicating which electrodes are being touched.

**Understanding the Code**

#. Import Modules:

   * ``machine``: Provides access to hardware-related functions.
   * ``mpr121``: The library to interface with the MPR121 sensor.
   * ``utime``: Contains time-related functions for delays.

#. Initialize I2C Communication:


   * ``i2c = I2C(0, sda=Pin(4), scl=Pin(5))``: Sets up I2C communication on I2C0 bus using GP4 (SDA) and GP5 (SCL).

#. Create an MPR121 Object:

   * ``mpr = MPR121(i2c)``: Initializes the MPR121 sensor using the I2C communication established.

#. Main Loop to Detect Touch Inputs:

   * ``get_all_states()``: Returns a list of electrode numbers that are currently being touched.
   * If any electrodes are touched, it prints out their numbers.
   * The loop runs continuously with a short delay of 100 milliseconds.

   .. code-block:: python

        while True:
            value = mpr.get_all_states()
            if len(value) != 0:
                print(value)
            time.sleep_ms(100)

**Extending the Electrodes**

You can enhance your project by connecting the electrodes to various conductive materials:

* **Fruits**: Attach wires to bananas, apples, or other fruits to turn them into touch-sensitive inputs.
* **Foil Shapes**: Cut shapes out of aluminum foil and attach them to the electrodes.
* **Conductive Paint**: Draw patterns with conductive ink or paint.

.. note::
    
    If you change the electrodes (e.g., connect different materials), you may need to reset the sensor to recalibrate the baseline values.

**Experimenting Further**

* Detecting a Specific Electrode:

  If you want to monitor a specific electrode, you can use the ``is_touched(pin)`` method, it will return True if the specified electrode (pin) is being touched; otherwise, it returns False.

  .. code-block:: python
  
        from mpr121 import MPR121
        from machine import Pin, I2C
        import utime

        i2c = I2C(0, sda=Pin(4), scl=Pin(5))
        mpr = MPR121(i2c)

        # check all keys
        while True:
          if mpr.is_touched(0):
              print("Electrode 0 is touched!")
          utime.sleep(0.1)


* **Create a Musical Instrument**: Map each electrode to a musical note and play sounds when touched.
* **Interactive Art**: Use conductive paint to create touch-sensitive artworks.
* **Game Controller**: Design custom touch controls for a game.

**Conclusion**

In this lesson, you've learned how to use the MPR121 capacitive touch sensor with the Raspberry Pi Pico 2w to create a touch-sensitive electrode keyboard. This opens up possibilities for interactive projects that respond to touch inputs in creative ways.


