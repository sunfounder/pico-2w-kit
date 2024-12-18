.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_lcd:

3.4 Liquid Crystal Display
===============================

LIn this lesson, we will learn how to use a **1602 LCD** with the Raspberry Pi Pico cpn_pico_2w to display text. The LCD1602 is a character-based liquid crystal display that can show 16 characters on 2 lines, making it ideal for projects that need to display information like messages, sensor readings, or status updates.

Connecting an LCD directly to a microcontroller typically requires many GPIO pins, which can limit the functionality of your project. To solve this problem, we can use an LCD1602 module that has an **I2C interface**. The I2C protocol uses only two data lines (SDA and SCL), allowing you to control the LCD with just two GPIO pins, freeing up other pins for additional sensors or devices.

* :ref:`cpn_i2c_lcd`


**Understanding I2C on the Raspberry Pi Pico 2**

The Raspberry Pi Pico 2 supports I2C communication through multiple GPIO pins, providing flexibility for your projects. It has two I2C buses, I2C0 and I2C1, and each can be mapped to several sets of pins.

Here's a breakdown of the I2C-capable pins on the Pico cpn_pico_2w:

|pin_i2c|

You can choose any matching pair of SDA and SCL pins for either I2C0 or I2C1. This flexibility allows you to avoid pin conflicts with other peripherals in your project.

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
        - :ref:`cpn_i2c_lcd`
        - 1
        - |link_i2clcd1602_buy|

**Schematic**

|sch_lcd|

**Wiring**

|wiring_lcd|

**Writing the Code**

Let's write a MicroPython program to display messages on the LCD1602.

.. note::

   * Open the ``3.4_liquid_crystal_display.py`` from ``pico-2 w-kit-main/micropython`` or copy the code into Thonny, then click "Run" or press F5.
   * Ensure the correct interpreter is selected: MicroPython (Raspberry Pi Pico).COMxx.  
   * Here you need to use the library called ``lcd1602.py``, please check if it has been uploaded to Pico, for a detailed tutorial refer to :ref:`add_libraries_py`.


.. code-block:: python

   from machine import I2C, Pin
   from lcd1602 import LCD
   import utime

   # Initialize I2C communication (I2C0)
   i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)

   # Create an LCD object
   lcd = LCD(i2c)

   # Display the first message
   lcd.clear()
   lcd.message("Hello, World!")
   utime.sleep(2)

   # Move to the second line and display another message
   lcd.write(0, 1,"LCD1602 with I2C")  # Column 0, Line 1
   utime.sleep(5)

   # Clear the display
   lcd.clear()

When the code is running, you will see:

* The LCD should display "Hello, World!" on the first line.
* After 2 seconds, the second line will display "LCD1602 with I2C".
* After 5 more seconds, the display will clear.

**Understanding the Code**

#. Import Modules:

   * ``machine``: Provides access to the hardware.
   * ``lcd1602``: Custom library to control the LCD.
   * ``utime``: Time-related functions for delays.

#. Initialize I2C Communication:

   .. code-block:: python
   
      i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)
   
   * ``I2C(0, ...)``: Uses I2C0 bus.
   * ``sda=Pin(4)``: Sets GP4 as SDA.
   * ``scl=Pin(5)``: Sets GP5 as SCL.
   * ``freq=400000``: Sets the I2C frequency to 400kHz.

#. Create an LCD Object:

   * ``lcd = LCD(i2c)``: Creates an instance of the LCD class, passing the I2C object.

#. Display Messages:

   * ``lcd.clear()``: Clears any existing text on the display.
   * ``lcd.message("Hello, World!")``: Displays the string "Hello, World!" on the LCD.
   * ``utime.sleep(2)``: Waits for 2 seconds before executing the next command.

#. Move Cursor and Display More Text:

   * ``lcd.write(0, 1,"LCD1602 with I2C")``: Moves the cursor to the first column of the second line and displays the string on the second line.

#. Final Delay and Clear:

   * ``utime.sleep(5)``: Waits for 5 seconds
   * ``lcd.clear()``: Clears the display.

**Experimenting Further**

* **Display Custom Messages**: Modify the strings in ``lcd.message()`` to display your own messages.
* **Use Line Breaks**: Since the LCD1602 has two lines, you can move the cursor to the second line using ``(0, 1, message[i:i+16])``.
* **Create Scrolling Text**: You can create a scrolling effect by updating the display within a loop.

  .. code-block:: python

      from machine import I2C, Pin
      from lcd1602 import LCD
      import utime

      # Initialize I2C communication (I2C0)
      i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)

      # Create an LCD object
      lcd = LCD(i2c)

      message = "Scrolling Text Demo "
      lcd.clear()
      while True:
         for i in range(len(message)):
            lcd.write(0, 0, message[i:i+16])  # Display 16 characters at a time
            utime.sleep(0.3)

**Troubleshooting Tips**

* Incorrect Characters or No Display:

  * Ensure that the wiring is correct, especially the SDA and SCL connections.
  * Make sure the I2C address in the lcd1602 library matches your LCD's address. The default is often 0x27 or 0x3F.

* Adjust Contrast:

  Some LCD modules have a contrast adjustment potentiometer. If nothing appears on the screen, try adjusting it.

* Power Supply:

  Ensure the LCD is receiving adequate power. If using 5V, connect to the Pico's VSYS pin (if powered via USB) or an external 5V supply.

* Understanding I2C Addresses

  If your LCD does not display text, it's possible that it uses a different I2C address. You can scan for devices on the I2C bus:

  .. code-block:: python
  
      from machine import I2C, Pin
      i2c = I2C(0, sda=Pin(4), scl=Pin(5))
      devices = i2c.scan()

      # Print the I2C addresses in hexadecimal format
      print("I2C addresses found:", [hex(device) for device in devices])

  This will print the addresses of devices connected to the I2C bus. Update the lcd1602.py library or your code to use the correct address.

**Conclusion**

You've successfully learned how to control an LCD1602 display using the I2C interface with your Raspberry Pi Pico 2! This skill allows you to add visual output to your projects, making them more interactive and informative.
