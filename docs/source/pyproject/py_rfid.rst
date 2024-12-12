.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_rfid:


6.5 Interfacing RFID
===========================================

In this lesson, we'll explore how to use **Radio Frequency Identification (RFID)** technology with the Raspberry Pi Pico 2w. RFID allows for wireless communication between a reader and tags, which can be used for identification, authentication, and data storage.

* :ref:`cpn_mfrc522`

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
        - :ref:`cpn_mfrc522`
        - 1
        - |link_rfid_buy|

**Understanding RFID**

RFID technology uses electromagnetic fields to automatically identify and track tags attached to objects. The tags contain electronically stored information, which can be read from a distance without direct line-of-sight.

* **RFID Reader (MFRC522):** A device that emits radio waves to communicate with RFID tags.
* **RFID Tag:** A small object, such as a card or key fob, that contains a microchip and antenna. It can be passive (no battery) or active (battery-powered).

**Schematic**

|sch_rfid|

**Wiring**

|wiring_rfid|

**Writing the Code**

We'll write two separate scripts:

.. note::

    Here you need to use the libraries in ``mfrc522`` folder, please check if it has been uploaded to Pico, for a detailed tutorial refer to :ref:`add_libraries_py`.

1. Writing Data to an RFID Tag:

   * ``SimpleMFRC522`` class from the ``mfrc522`` library simplifies interactions with the RFID reader.
   * The reader is initialized with the specified SPI pins.
   * Prompts the user to input data to write.
   * Instructs the user to place the tag near the reader.
   * Writes the data to the tag using ``reader.write(data)``.

   .. note::

       Open the ``6.5_rfid_write.py`` file from ``pico-2w-kit-main/micropython`` or copy this code into Thonny, then click “Run Current Script” or simply press F5 to run it.

   .. code-block:: python

        from mfrc522 import SimpleMFRC522
        from machine import Pin, SPI

        # Initialize the RFID reader
        reader = SimpleMFRC522(spi_id=0, sck=18, mosi=19, miso=16, cs=17, rst=9)

        def write_to_tag():
            try:
                data = input("Enter data to write to the tag: ")
                print("Place your tag near the reader...")
                reader.write(data)
                print("Data written successfully!")
            finally:
                pass  # Cleanup actions if necessary

        write_to_tag()

   After running, the following occurs:
   
   * The program displays: 
   
     .. code-block::
   
       Enter data to write to the tag:"
   
   * You input the text you want to write to the RFID tag and press Enter.
   * The program then shows:
   
     .. code-block::
       
       Place your tag near the reader...
   
   * You place the RFID tag near the reader module.
   * After successfully writing the data, it displays:
   
     .. code-block::
   
       Data written successfully!

2. Reading Data from an RFID Tag:

   * Instructs the user to place the tag near the reader.
   * Reads the tag's ID and stored text using ``reader.read()``.
   * Prints out the tag's ID and the data read from the tag.

   .. note::

       Open the ``6.5_rfid_read.py`` file from ``pico-2w-kit-main/micropython`` or copy this code into Thonny, then click “Run Current Script” or simply press F5 to run it.


   .. code-block:: python
   
       from mfrc522 import SimpleMFRC522
       from machine import Pin, SPI
   
       # Initialize the RFID reader
       reader = SimpleMFRC522(spi_id=0, sck=18, mosi=19, miso=16, cs=17, rst=9)
   
       def read_from_tag():
           try:
               print("Place your tag near the reader...")
               id, text = reader.read()
               print("Tag ID: {}".format(id))
               print("Data: {}".format(text.strip()))
           finally:
               pass  # Cleanup actions if necessary
   
       read_from_tag()
   
   After running, the program prints the message "Place your tag near the reader...".
   You need to place an RFID tag near the MFRC522 reader module, then program prints the retrieved information to the console. The output will look something like:
   
   .. code-block:: 
   
       Tag ID: 1234567890
       Data: Your stored message

**Understanding the Code**

* **RFID Communication**: The MFRC522 module communicates with the RFID tag using radio waves. When the tag is within range, the reader can read or write data to the tag's memory.
* **SPI Interface**: The module communicates with the Pico via the SPI protocol, allowing for fast data transfer.
* **Data Storage**: RFID tags have limited storage capacity, suitable for storing small amounts of data like IDs or short text.

**Applications**

* **Access Control Systems**: Use RFID tags as keys to unlock doors or devices.
* **Inventory Management**: Track items in a warehouse or store by tagging them with RFID tags.
* **Attendance Systems**: Record attendance by scanning RFID tags assigned to individuals.

**Experimenting Further**

* **Multiple Tags**: Try writing different data to multiple tags and reading them back.
* **Security Measures**: Implement basic authentication to prevent unauthorized access.
* **Data Formatting**: Store structured data, such as JSON or CSV, for more complex applications.

**Conclusion**

In this lesson, you've learned how to interface an RFID reader with the Raspberry Pi Pico 2w to read and write data to RFID tags. This technology opens up possibilities for numerous applications in identification, tracking, and automation.

