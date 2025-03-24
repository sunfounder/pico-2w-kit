.. note:: 

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche mit Gleichgesinnten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum beitreten?**

    - **Expertenunterstützung**: Erhalte Hilfe von unserer Community und unserem Team bei technischen Herausforderungen und Support-Anfragen nach dem Kauf.
    - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um deine Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Profitiere von exklusiven Vergünstigungen auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nimm an Verlosungen und saisonalen Sonderaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _py_pa_buz:

3.2 Eigene Töne mit einem passiven Buzzer erzeugen
=====================================================

In dieser Lektion lernen wir, wie man mit einem **passiven Buzzer** und dem Raspberry Pi Pico 2 W verschiedene Töne und sogar einfache Melodien erzeugt! Im Gegensatz zu einem aktiven Buzzer benötigt ein passiver Buzzer ein wechselndes elektrisches Signal, um einen Ton zu erzeugen. Durch Ändern der Frequenz dieses Signals können wir die Tonhöhe steuern.

* :ref:`cpn_buzzer`

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Bauteile.

Es ist praktisch, ein komplettes Kit zu kaufen. Hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name
        - ENTHALTENE TEILE
        - LINK
    *   - Pico 2 W Starter Kit
        - 450+
        - |link_pico2w_kit|

Alternativ können die Komponenten auch einzeln über die folgenden Links erworben werden.


.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - KOMPONENTE
        - MENGE
        - LINK

    *   - 1
        - :ref:`cpn_pico_2w`
        - 1
        - |link_pico2w_buy|
    *   - 2
        - Micro-USB-Kabel
        - 1
        - 
    *   - 3
        - :ref:`cpn_breadboard`
        - 1
        - |link_breadboard_buy|
    *   - 4
        - :ref:`cpn_wire`
        - Mehrere
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_transistor`
        - 1 (S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_resistor`
        - 1 (1KΩ)
        - |link_resistor_buy|
    *   - 7
        - Passiver :ref:`cpn_buzzer`
        - 1
        - |link_passive_buzzer_buy|

**Funktionsweise eines passiven Buzzers**

Ein passiver Buzzer funktioniert wie ein kleiner Lautsprecher. Er erzeugt keinen eigenen Ton, sondern benötigt ein externes Wechselstromsignal. Durch die Steuerung der Frequenz des Signals kann der Buzzer verschiedene Tonhöhen wiedergeben und so Noten oder Melodien spielen.

|img_buzzer|

**Schaltplan**

|sch_buzzer|

In dieser Schaltung wird der passive Buzzer über einen **S8050**-NPN-Transistor gesteuert. Der Transistor verstärkt den Stromfluss und macht den Ton lauter, als wenn der Buzzer direkt an den Pico angeschlossen wäre.

Funktionsweise:

* **GP15** gibt ein hohes Signal aus, um den Transistor zu aktivieren.
* Wenn der Transistor leitend wird, fließt Strom durch den Buzzer, wodurch ein Ton erzeugt wird.

Ein **1kΩ-Widerstand** begrenzt den Stromfluss, um den Transistor zu schützen.

**Verdrahtung**

Achte darauf, dass du einen **passiven Buzzer** verwendest. Du kannst ihn daran erkennen, dass die Leiterplatte auf der Unterseite sichtbar ist (im Gegensatz zum versiegelten Gehäuse eines aktiven Buzzers).

|img_buzzer|

|wiring_buzzer|

.. 1. Verbinde 3V3 und GND des Pico 2 W mit den Stromschienen des Breadboards.
.. #. Verbinde den positiven Pin des Buzzers mit der positiven Stromschiene.
.. #. Verbinde den Kathoden-Pin des Buzzers mit dem **Kollektor** des Transistors.
.. #. Verbinde den **Basisanschluss** des Transistors über einen 1kΩ-Widerstand mit GP15.
.. #. Verbinde den **Emitter** des Transistors mit der negativen Stromschiene.

**Code schreiben**

Nun schreiben wir ein Programm, das den Buzzer verschiedene Töne spielen lässt.

.. note::

    * Öffne die Datei ``3.2_custom_tone.py`` aus dem Verzeichnis ``pico-2w-kit-main/micropython`` oder kopiere den Code in Thonny. Klicke dann auf "Run" oder drücke **F5**.
    * Stelle sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx.

.. code-block:: python

   import machine
   import utime

   # PWM auf GP15 initialisieren
   buzzer = machine.PWM(machine.Pin(15))

   def play_tone(frequency, duration):
       # Frequenz des PWM-Signals setzen
       buzzer.freq(frequency)
       # Duty Cycle auf 50% setzen
       buzzer.duty_u16(32768)
       # Ton für die angegebene Dauer spielen
       utime.sleep_ms(duration)
       # Buzzer ausschalten
       buzzer.duty_u16(0)

   # Ein paar Töne abspielen
   play_tone(440, 500)  # A4-Ton für 500 ms
   utime.sleep_ms(200)
   play_tone(494, 500)  # B4-Ton für 500 ms
   utime.sleep_ms(200)
   play_tone(523, 500)  # C5-Ton für 500 ms

Nach dem Start des Codes spielt der Buzzer die Noten A4, B4 und C5 für jeweils 500 ms.


**Erklärung des Codes**

#. PWM initialisieren:

   * ``buzzer = machine.PWM(machine.Pin(15))``: Aktiviert PWM auf GP15 zur Steuerung des Buzzers.

#. Die Funktion ``play_tone`` definieren:

   .. code-block:: python

      def play_tone(frequency, duration):
          buzzer.freq(frequency)
          buzzer.duty_u16(32768)
          utime.sleep_ms(duration)
          buzzer.duty_u16(0)

   * ``frequency``: Die Tonhöhe des Signals.
   * ``duration``: Die Abspielzeit in Millisekunden.
   * ``buzzer.duty_u16(32768)``: Setzt den Duty Cycle auf 50% (max. Wert 65535).
   * Nach der Dauer wird der Ton gestoppt, indem der Duty Cycle auf 0 gesetzt wird.

#. Noten abspielen:

   Durch Aufrufe von ``play_tone`` mit verschiedenen Frequenzen spielen wir verschiedene Töne.

   .. code-block:: python

      play_tone(440, 500)  # A4-Ton für 500 ms
      utime.sleep_ms(200)
      play_tone(494, 500)  # B4-Ton für 500 ms
      utime.sleep_ms(200)
      play_tone(523, 500)  # C5-Ton für 500 ms


**Eine Melodie spielen**

Jetzt erstellen wir eine einfache Melodie, indem wir mehrere Noten in einer Sequenz spielen.

.. code-block:: python

    import machine
    import utime

    # Notenfrequenzen (Hz)
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

Wenn du diesen Code ausführst, spielt der Buzzer eine einfache Melodie, indem er jede Note der Reihe nach wiedergibt. Jede Note dauert 500 Millisekunden, mit einer kurzen Pause dazwischen. Du wirst hören, wie der Buzzer eine aufsteigende Tonleiter von Mittlerem C (C4) bis zum C der nächsten Oktave (C5) spielt.

**Weitere Experimente**

* **Eigene Melodie erstellen**: Ändere die Noten und Dauern in den Listen ``melody`` und ``note_durations``, um deine eigene Komposition zu erstellen.
* **Tempo anpassen**: Modifiziere die Werte in ``note_durations``, um die Melodie schneller oder langsamer abzuspielen.
* **Weitere Noten hinzufügen**: Definiere zusätzliche Noten durch Angabe ihrer Frequenzen und integriere sie in deine Melodie.
* **Lautstärke verändern**: Passe den Duty Cycle in ``buzzer.duty_u16()`` an, um die Lautstärke des Buzzers zu erhöhen oder zu verringern. Ein Wert um 32768 entspricht einem Duty Cycle von 50 %.

**Fazit**

In dieser Lektion hast du gelernt, wie du mit einem passiven Buzzer Töne und Melodien auf dem Raspberry Pi Pico 2 W erzeugst. Durch die Steuerung der PWM-Frequenz kannst du eine Vielzahl von Klängen erzeugen und sogar einfache Lieder spielen. Dies ist eine großartige Möglichkeit, um Audio-Feedback oder unterhaltsame musikalische Elemente in deine Projekte zu integrieren.
