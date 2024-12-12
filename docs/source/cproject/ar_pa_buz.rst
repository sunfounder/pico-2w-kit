.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ar_pa_buz:


3.2 Play Custom Tones with a Passive Buzzer
===========================================

In this lesson, we'll learn how to use a **passive buzzer** with the Raspberry Pi Pico 2w to play different tones and even simple melodies! Unlike an active buzzer, a passive buzzer needs a changing electrical signal to produce sound, which means we can control the pitch of the sound by changing the signal's frequency.

* :ref:`Buzzer`

**Required Components**

In this project, we need the following components. 

It's definitely convenient to buy a whole kit, here's the link: 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ITEMS IN THIS KIT
        - PURCHASE LINK
    *   - Pico 2 W Starter Kit	
        - 450+
        - |link_pico2w_kit|

You can also buy them separately from the links below.


.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - COMPONENT INTRODUCTION	
        - QUANTITY
        - PURCHASE LINK

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

**Schematic**

|sch_buzzer|

In this circuit, the passive buzzer is powered through a transistor (**S8050** NPN). The transistor amplifies the current, making the buzzer sound louder than if it were connected directly to the Pico. 

Here's what happens:

* **GP15** outputs a high signal to control the transistor.
* When the transistor is activated, it allows current to flow through the buzzer, making it beep.

A **1kΩ resistor** is used to limit the current to protect the transistor.

**Wiring**

|img_buzzer|

Make sure you are using the **passive buzzer**. You can tell it's the correct one by looking for the exposed PCB (as opposed to the sealed back, which is a active buzzer).

|wiring_buzzer|

**Writing the Code**


.. note::

    * You can open the file ``3.2_custom_tone.ino`` under the path of ``pico-2w-starter-kit-main/arduino/3.2_custom_tone``. 
    * Or copy this code into **Arduino IDE**.
    * Don't forget to select the board(Raspberry Pi Pico) and the correct port before clicking the **Upload** button.




.. code-block:: arduino

    const int buzzerPin = 15;  // GPIO pin connected to the transistor base

    void setup() {
      pinMode(buzzerPin, OUTPUT);
    }

    void loop() {
      // Play a tone at 440 Hz (A4 note) for 1 second
      tone(buzzerPin, 440, 1000);
      delay(1000);  // Wait for the tone to finish
      // Wait for 1 second before playing again
      delay(1000);
    }

The code plays a 440 Hz tone (standard A note) for 1 second, waits for 1 second, and repeats.

* ``tone(pin, frequency, duration)``:

  * ``pin``: The GPIO pin connected to the buzzer (through the transistor).
  * ``frequency``: The frequency of the tone in hertz (Hz). Higher frequencies produce higher pitches.
  * ``duration (optional)``: The duration to play the tone in milliseconds.


**Playing a Melody**

Let's expand the code to play a simple melody by defining the notes and their corresponding frequencies.

* An array ``melody[]`` holds the sequence of notes to play.
* An array ``noteDurations[]`` defines the duration of each note. A duration of 4 represents a quarter note.
* The ``for`` loop iterates through each note in the melody.

  * Calculates the note duration in milliseconds.
  * Uses ``tone()`` to play each note.
  * Uses ``delay()`` to pause between notes.
  * Calls ``noTone()`` to stop the tone before moving to the next note.

.. code-block:: arduino

        // Define the buzzer pin
        const int buzzerPin = 15;

        // Define note frequencies
        #define NOTE_C4  262
        #define NOTE_D4  294
        #define NOTE_E4  330
        #define NOTE_F4  349
        #define NOTE_G4  392
        #define NOTE_A4  440
        #define NOTE_B4  494
        #define NOTE_C5  523

        // Melody notes
        int melody[] = {
          NOTE_C4, NOTE_D4, NOTE_E4, NOTE_F4,
          NOTE_G4, NOTE_A4, NOTE_B4, NOTE_C5
        };

        // Note durations: 4 = quarter note, 8 = eighth note, etc.
        int noteDurations[] = {
          4, 4, 4, 4,
          4, 4, 4, 4
        };

        void setup() {
          pinMode(buzzerPin, OUTPUT);
        }

        void loop() {
          // Iterate over the notes of the melody
          for (int thisNote = 0; thisNote < 8; thisNote++) {
            int noteDuration = 1000 / noteDurations[thisNote];
            tone(buzzerPin, melody[thisNote], noteDuration);
            // Pause between notes
            int pauseBetweenNotes = noteDuration * 1.30;
            delay(pauseBetweenNotes);
            // Stop the tone playing
            noTone(buzzerPin);
          }
          // Add a delay before repeating the melody
          delay(2000);
        }

After uploading the code, you should hear the buzzer play the melody. If the sound is too quiet, ensure all connections are secure. Remember that passive buzzers may not produce very loud sounds.


**Learn More**

* Creating Your Own Melodies:

  You can create your own melodies by changing the ``melody[]`` and ``noteDurations[]`` arrays.

* Using the ``pitches.h`` Library:

  For convenience, you can include a library file ``pitches.h`` that contains definitions for many notes.
  Create a file named ``pitches.h`` and include it in your sketch.
  
  .. code-block:: arduino

    #include "pitches.h"

**Further Exploration**

* Compose a Song:

  Try composing your own song by defining a new sequence of notes and durations.

* Interactive Music:

  Add buttons or sensors to control the playback of the melody.

* Visual Feedback:

  Integrate LEDs to light up in sync with the notes played.

**Conclusion**

In this lesson, you've learned how to use a passive buzzer with the Raspberry Pi Pico to play different tones and melodies. By controlling the frequency of the signal sent to the buzzer, you can produce various pitches and create music in your projects.




