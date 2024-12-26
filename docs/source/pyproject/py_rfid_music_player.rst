.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_music_player:

7.8 RFID Music Player
==========================

In this project, we'll create an **RFID Music Player** using the Raspberry Pi Pico 2 W, an MFRC522 RFID reader, a passive buzzer, and WS2812 RGB LEDs. By writing musical notes to RFID tags, we'll read them back and have the Pico play the corresponding melody while displaying colorful LED effects. This project combines RFID technology with music generation, allowing you to store and share melodies on RFID cards or key fobs.


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
        - :ref:`cpn_transistor`
        - 1(S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_resistor`
        - 1(1KΩ)
        - |link_resistor_buy|
    *   - 7
        - Passive :ref:`cpn_buzzer`
        - 1
        - |link_passive_buzzer_buy|
    *   - 8
        - :ref:`cpn_mfrc522`
        - 1
        - |link_rfid_buy|
    *   - 9
        - :ref:`cpn_ws2812`
        - 1
        - |link_ws2812_buy|

**Understanding the Components**

* **MFRC522 RFID Reader Module**: A low-cost RFID reader that communicates over SPI. It can read and write data to RFID tags operating at 13.56 MHz.
* **RFID Tags/Key Fobs**: Passive devices that can store small amounts of data. We'll write musical notes to these tags.
* **Passive Buzzer**: An electronic component that can produce sound when driven with a PWM signal. We'll use it to play musical notes.
* **WS2812 RGB LEDs**: Also known as NeoPixels, these LEDs can display a wide range of colors and can be individually controlled over a single data line.

**Schematic**

|sch_music_player|


**Wiring**

|wiring_rfid_music_player| 


**Writing the Code**

We'll write two scripts:

* ``6.5_rfid_write.py``: To store the musical notes on the RFID tag.
* ``7.8_rfid_music_player.py``: To read the stored notes and play the melody.

.. note::

    Here you need to use the libraries in ``mfrc522`` folder, please check if it has been uploaded to Pico, for a detailed tutorial refer to :ref:`add_libraries_py`.

#. Open the ``6.5_rfid_write.py`` file from ``pico-2w-kit-main/micropython`` or copy this code into Thonny, then click “Run Current Script” or simply press F5 to run it.

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
                pass

        write_to_tag()

#. After running, type ``EEFGGFEDCCDEEDD EEFGGFEDCCDEDCC`` in the shell, then bring the RFID tag near the reader to store a score of "Ode to Joy". Wait for the confirmation message: "Data written successfully!"

#. Open the ``7.8_rfid_music_player.py`` file from ``pico-2w-kit-main/micropython`` or copy this code into Thonny, then click “Run Current Script” or simply press F5 to run it.

   .. code-block:: python

        from mfrc522 import SimpleMFRC522
        import machine
        import time
        from ws2812 import WS2812
        import urandom

        # WS2812 LED setup
        # Initialize an 8-LED WS2812 strip on pin 0
        ws = WS2812(machine.Pin(0), 8)

        # MFRC522 RFID reader setup
        # Initialize the RFID reader using SPI on specific pins
        reader = SimpleMFRC522(spi_id=0, sck=18, miso=16, mosi=19, cs=17, rst=9)

        # Buzzer note frequencies (in Hertz)
        NOTE_C4 = 262
        NOTE_D4 = 294
        NOTE_E4 = 330
        NOTE_F4 = 349
        NOTE_G4 = 392
        NOTE_A4 = 440
        NOTE_B4 = 494
        NOTE_C5 = 523

        # Initialize PWM for buzzer on pin 15
        buzzer = machine.PWM(machine.Pin(15))

        # List of note frequencies corresponding to musical notes
        note = [NOTE_C4, NOTE_D4, NOTE_E4, NOTE_F4, NOTE_G4, NOTE_A4, NOTE_B4, NOTE_C5]

        # Function to play a tone on the buzzer with a specified frequency and duration
        def tone(pin, frequency, duration):
         pin.freq(frequency)  # Set the buzzer frequency
         pin.duty_u16(30000)  # Set duty cycle to 50% (approx)
         time.sleep_ms(duration)  # Play the tone for the specified duration
         pin.duty_u16(0)  # Stop the tone by setting duty cycle to 0

        # Function to light up a WS2812 LED at a specific index with a random color
        def lumi(index):
         for i in range(8):
             ws[i] = 0x000000  # Turn off all LEDs
         ws[index] = int(urandom.uniform(0, 0xFFFFFF))  # Set a random color for the LED at the given index
         ws.write()  # Write the color data to the WS2812 LEDs

        # Encode musical notes text into indices and play the corresponding notes
        words = ["C", "D", "E", "F", "G", "A", "B", "N"]  # Mapping of musical notes to text characters
        def take_text(text):
         string = text.replace(' ', '').upper()  # Remove spaces and convert the text to uppercase
         while len(string) > 0:
             index = words.index(string[0])  # Find the index of the first note in the string
             tone(buzzer, note[index], 250)  # Play the corresponding note on the buzzer for 250 ms
             lumi(index)  # Light up the LED corresponding to the note
             string = string[1:]  # Move to the next character in the string

        # Function to read from the RFID card and play the stored score
        def read():
         print("Reading...Please place the card...")
         id, text = reader.read()  # Read the RFID card (ID and stored text)
         print("ID: %s\nText: %s" % (id, text))  # Print the ID and text
         take_text(text)  # Play the score from the text stored on the card

        # Start reading from the RFID card and play the corresponding score
        read()



#. After running, the console will display: "Place your tag near the reader...".

   Place the RFID Tag Near the Reader:
   
   * The Pico reads the data from the tag.
   * The console displays the tag ID and text.
   * The buzzer plays the melody corresponding to the notes stored on the tag.
   * The WS2812 LEDs light up with effects synchronized to the music.

**Understanding the Code**

* RFID Interaction:

  * The ``SimpleMFRC522`` class simplifies reading and writing to RFID tags.
  * **Writing Data**: In ``write_to_tag()``, user input is written to the tag.
  * **Reading Data**: In ``read_and_play()``, data is read from the tag when it's near the reader.

* Music Playback:

  * **Notes Dictionary**: Maps ``note`` characters to frequencies.
  * **Parsing Notes**: The text from the RFID tag is cleaned and iterated character by character.
  * **Playing Notes**: For each character, the corresponding frequency is played on the buzzer.

* LED Effects:

  * **WS2812 Control**: The ``ws`` object controls the RGB LEDs.
  * **Lighting LEDs**: For each note played, an LED lights up with a random color.

* Timing:

  * **Note Duration**: Each note is played for 300 milliseconds.
  * **Pause Between Notes**: A short pause of 100 milliseconds between notes.

**Experimenting Further**

* Create Your Own Melodies:

  * Write different musical notes to RFID tags.
  * Use notes C, D, E, F, G, A, B, and N (for rest).
  * Share your musical RFID tags with friends.

* Extend Note Range:

  * Add more octaves by defining additional frequencies.
  * Update the notes dictionary accordingly.

* Visual Enhancements:

  * Modify the light_led function to create different LED patterns.
  * Synchronize LED effects more closely with the music.

* Multiple Tags for Different Songs:

  * Program multiple RFID tags with different melodies.
  * Build a simple RFID-based music library.

**Understanding Limitations**

* Data Storage on RFID Tags:

  * RFID tags have limited storage capacity (typically up to 48 characters for the MFRC522).
  * Keep your musical sequences concise.

* Audio Quality:

  * Passive buzzers produce simple tones.
  * For better sound quality, consider using an active speaker with a DAC output.

* RFID Tag Compatibility:

  Ensure that your RFID tags are compatible with the MFRC522 reader.

**Conclusion**

You've successfully created an RFID Music Player using the Raspberry Pi Pico 2 W! This project combines RFID technology, music generation, and LED control to create an interactive and enjoyable experience. By storing melodies on RFID tags, you can easily share and play different tunes.
