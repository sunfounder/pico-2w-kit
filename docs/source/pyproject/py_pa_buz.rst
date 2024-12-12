.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_pa_buz:

3.2 Play Custom Tones with a Passive Buzzer
==============================================


In this lesson, we'll learn how to use a **passive buzzer** with the Raspberry Pi Pico 2w to play different tones and even simple melodies! Unlike an active buzzer, a passive buzzer needs a changing electrical signal to produce sound, which means we can control the pitch of the sound by changing the signal's frequency.


* :ref:`cpn_buzzer`

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

**Understanding the Passive Buzzer**

A passive buzzer works like a tiny speaker. It doesn't produce sound on its own; instead, it needs an oscillating signal to make sound. By providing signals of different frequencies, we can make the buzzer produce different pitches, allowing us to play notes and melodies.

|img_buzzer|

**Circuit Diagram**

|sch_buzzer|

In this circuit, the passive buzzer is powered through a transistor (**S8050** NPN). The transistor amplifies the current, making the buzzer sound louder than if it were connected directly to the Pico. 

Here's what happens:

* **GP15** outputs a high signal to control the transistor.
* When the transistor is activated, it allows current to flow through the buzzer, making it beep.

A **1kΩ resistor** is used to limit the current to protect the transistor.

**Wiring Diagram**

Make sure you are using the **passive buzzer**. You can tell it's the correct one by looking for the exposed PCB (as opposed to the sealed back, which is a active buzzer).

|img_buzzer|

|wiring_buzzer|


.. 1. Connect 3V3 and GND of Pico 2W to the power bus of the breadboard.
.. #. Connect the positive pin of the buzzer to the positive power bus.
.. #. Connect the cathode pin of the buzzer to the **collector** lead of the transistor.
.. #. Connect the **base** lead of the transistor to the GP15 pin through a 1kΩ resistor.
.. #. Connect the **emitter** lead of the transistor to the negative power bus.


**Writing the Code**

Now, let's write some code to make the buzzer play different tones.

.. note::

    * Open the ``3.2_custom_tone.py`` from ``pico-2w-kit-main/micropython`` or copy the code into Thonny, then click "Run" or press F5.
    * Ensure the correct interpreter is selected: MicroPython (Raspberry Pi Pico).COMxx. 
    

.. code-block:: python

   import machine
   import utime

   # Initialize PWM on GP15
   buzzer = machine.PWM(machine.Pin(15))

   def play_tone(frequency, duration):
       # Set the frequency of the PWM signal
       buzzer.freq(frequency)
       # Set duty cycle to 50%
       buzzer.duty_u16(32768)
       # Play the tone for the specified duration
       utime.sleep_ms(duration)
       # Turn off the buzzer
       buzzer.duty_u16(0)

   # Play some tones
   play_tone(440, 500)  # A4 note for 500ms
   utime.sleep_ms(200)
   play_tone(494, 500)  # B4 note for 500ms
   utime.sleep_ms(200)
   play_tone(523, 500)  # C5 note for 500ms

When the code runs, you will hear the passive buzzer play the A4 note for 500ms, the B4 note for 500ms, and the C5 note for 500ms respectively.


**Explanation of the Code**

#. Initialize PWM:

   * ``buzzer = machine.PWM(machine.Pin(15))``: This sets up PWM (Pulse Width Modulation) on pin GP15, which we'll use to control the buzzer.

#. Define the ``play_tone`` Function: 

   .. code-block:: python

      def play_tone(frequency, duration):
          buzzer.freq(frequency)
          buzzer.duty_u16(32768)
          utime.sleep_ms(duration)
          buzzer.duty_u16(0)

   * ``frequency``: The pitch of the tone. Higher frequency means a higher pitch.
   * ``duration``: How long the tone plays, in milliseconds.
   * ``buzzer.duty_u16(32768)``: Sets the duty cycle to 50% (half of 65535), which is ideal for generating sound.
   * After the duration, we turn off the buzzer by setting the duty cycle to 0.

#. Play Notes:

   We call ``play_tone`` with different frequencies corresponding to musical notes.

   .. code-block:: python

      # Play some tones
      play_tone(440, 500)  # A4 note for 500ms
      utime.sleep_ms(200)
      play_tone(494, 500)  # B4 note for 500ms
      utime.sleep_ms(200)
      play_tone(523, 500)  # C5 note for 500ms

   
**Playing a Melody**

Now that we've learned how to play individual tones with the passive buzzer, let's create a simple melody! This will help us understand how to sequence notes and control their durations to produce music.

.. code-block:: python

    import machine
    import utime

    # Note frequencies (in Hz)
    NOTE_C4 = 262
    NOTE_D4 = 294
    NOTE_E4 = 330
    NOTE_F4 = 349
    NOTE_G4 = 392
    NOTE_A4 = 440
    NOTE_B4 = 494
    NOTE_C5 = 523

    melody = [
        NOTE_C4, NOTE_D4, NOTE_E4, NOTE_F4,
        NOTE_G4, NOTE_A4, NOTE_B4, NOTE_C5
    ]

    note_durations = [
        500, 500, 500, 500,
        500, 500, 500, 500
    ]

    # Initialize PWM on GP15
    buzzer = machine.PWM(machine.Pin(15))

    def play_tone(frequency, duration):
        buzzer.freq(frequency)
        buzzer.duty_u16(32768)
        utime.sleep_ms(duration)
        buzzer.duty_u16(0)
        utime.sleep_ms(50)  # Short pause between notes

    for i in range(len(melody)):
        play_tone(melody[i], note_durations[i])

When you run this code, the buzzer will play a simple melody by sounding each note in the sequence. Each note lasts for 500 milliseconds, and there's a short pause between notes. You'll hear the buzzer play an ascending scale from Middle C (C4) up to the next octave's C (C5).

**Experimenting Further**

* **Create Your Own Melody**: Change the notes and durations in the melody and ``note_durations`` lists to compose your own tune.
* **Adjust the Tempo**: Modify the values in ``note_durations`` to speed up or slow down the melody.
* **Add More Notes**: Define additional notes by adding their frequencies and include them in your melody.
* **Change the Volume**: Adjust the duty cycle in ``buzzer.duty_u16()`` to make the buzzer louder or quieter. A value around 32768 gives 50% duty cycle.

**Conclusion**

In this lesson, you've learned how to use a passive buzzer to play tones and melodies with the Raspberry Pi Pico 2w. By controlling the frequency of the PWM signal, you can create a variety of sounds and even play simple songs. This is a great way to add audio feedback or fun musical elements to your projects.
