.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_irremote:


6.4 Using an Infrared Remote Control
==========================================================

In this lesson, we'll learn how to use an **infrared (IR) remote control** and an **IR receiver module** with the Raspberry Pi Pico 2w. This will allow us to receive and decode signals from an IR remote, enabling us to control our projects wirelessly.

* :ref:`cpn_ir_receiver`

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
        - :ref:`cpn_ir_receiver`
        - 1
        - |link_receiver_buy|

**Understanding Infrared Communication**

Infrared communication involves transmitting data wirelessly using infrared light. Common household devices like TVs and DVD players use IR remote controls for operation.

* **IR Transmitter (Remote Control):** Emits modulated infrared light when a button is pressed.
* **IR Receiver Module:** Detects the modulated IR light and converts it into electrical signals that can be decoded.

**Schematic**

|sch_irrecv|

**Wiring**


|wiring_irrecv|


**Writing the Code**

Let's write a MicroPython script to receive and decode IR signals from the remote control.

.. note::

    * Open the ``6.4_ir_remote_control.py`` from ``pico-2w-starter-kit-main/micropython`` or copy the code into Thonny, then click "Run" or press F5.
    * Ensure the correct interpreter is selected: MicroPython (Raspberry Pi Pico).COMxx. 
    * Here you need to use the libraries in ``ir_rx`` folder, please check if it has been uploaded to Pico, for a detailed tutorial refer to :ref:`add_libraries_py`.

.. code-block:: python

    import time
    from machine import Pin
    from ir_rx.nec import NEC_8  # Adjust based on your remote's protocol
    from ir_rx.print_error import print_error

    # Initialize the IR receiver pin
    ir_pin = Pin(17, Pin.IN)

    # Callback function to handle received data
    def ir_callback(data, addr, ctrl):
        if data < 0:  # Repeat code or error
            pass
        else:
            key = decode_key(data)
            print("Received Key:", key)

    # Function to decode the received data into key presses
    def decode_key(data):
        key_codes = {
            0x45: "POWER",
            0x46: "MODE",
            0x47: "MUTE",
            0x44: "PLAY/PAUSE",
            0x40: "BACKWARD",
            0x43: "FORWARD",
            0x07: "EQ",
            0x15: "-",
            0x09: "+",
            0xD: "U/SD",
            0x16: "0",
            0x19: "cycle",
            0xC: "1",
            0x5E: "3",
            0x18: "2",
            0x8: "4",
            0x1C: "5",
            0x5A: "6",
            0x42: "7",
            0x52: "8",
            0x4A: "9",
            0x0: "ERROR",
            # Add more key codes based on your remote
        }
        return key_codes.get(data, "UNKNOWN")

    # Instantiate the IR receiver
    ir = NEC_8(ir_pin, ir_callback)
    ir.error_function(print_error)  # Optional: to print errors

    try:
        while True:
            time.sleep(1)  # Keep the main thread alive
    except KeyboardInterrupt:
        ir.close()
        print("Program terminated")

When you run this code and press buttons on your infrared remote control, the Thonny Shell (or any other serial monitor) will display the name of the key you pressed. For example, if you press the "PLAY" button on the remote, the Shell will show "Received Key: PLAY".

**Understanding the Code**

#. Import Modules:

   * ``ir_rx.nec.NEC_8``: The NEC protocol decoder for 8-bit addresses.
   * ``print_error``: Function to print error messages.

   .. code-block:: python

        import time
        from machine import Pin
        from ir_rx.nec import NEC_8
        from ir_rx.print_error import print_error

#. Initialize IR Receiver Pin:

   .. code-block:: python

        ir_pin = Pin(17, Pin.IN)

#. Define Callback Function:

   This function is called automatically when data is received. The data parameter contains the key code.

   .. code-block:: python

        def ir_callback(data, addr, ctrl):
            if data < 0:
                pass  # Ignore repeat codes
            else:
                key = decode_key(data)
                print("Received Key:", key)

#. Decode Key Function:

   Maps received key codes to human-readable labels.

   .. code-block:: python

        def decode_key(data):
            key_codes = {
            0x45: "POWER",
            0x46: "MODE",
            0x47: "MUTE",
            0x44: "PLAY/PAUSE",
            0x40: "BACKWARD",
            0x43: "FORWARD",
            0x07: "EQ",
            0x15: "-",
            0x09: "+",
            0xD: "U/SD",
            0x16: "0",
            0x19: "cycle",
            0xC: "1",
            0x5E: "3",
            0x18: "2",
            0x8: "4",
            0x1C: "5",
            0x5A: "6",
            0x42: "7",
            0x52: "8",
            0x4A: "9",
            0x0: "ERROR",
            # Add more key codes based on your remote
            }
            return key_codes.get(data, "UNKNOWN")

#. Instantiate IR Receiver:

   Sets up the IR receiver with the callback function.

   .. code-block:: python

        ir = NEC_8(ir_pin, ir_callback)
        ir.error_function(print_error)


#. Main Loop:

   Keeps the program running to listen for IR signals. Gracefully handles program termination.

   .. code-block:: python

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            ir.close()
            print("Program terminated")

**Applications**

* **Control Projects Wirelessly**: Use the IR remote to control LEDs, motors, or other peripherals.
* **Build a Universal Remote Decoder**: Expand the code to handle multiple protocols or remotes.

**Conclusion**

In this lesson, you've learned how to use an IR receiver with the Raspberry Pi Pico 2w to decode signals from an infrared remote control. This enables you to add wireless control to your projects using common household remotes.

* `Callback Function - Wikipedia <https://en.wikipedia.org/wiki/Callback_(computer_programming)>`_

