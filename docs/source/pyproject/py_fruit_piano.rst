.. note:: 

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche gemeinsam mit anderen Technikbegeisterten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum mitmachen?**

    - **Expertenhilfe**: Erhalte Unterstützung bei Problemen nach dem Kauf und technischen Herausforderungen durch unsere Community und unser Team.
    - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um deine Fähigkeiten zu erweitern.
    - **Exklusive Einblicke**: Erhalte vorab Informationen zu neuen Produkten und exklusive Vorschauen.
    - **Sonderrabatte**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
    - **Aktionen & Gewinnspiele**: Nimm an saisonalen Aktionen und Verlosungen teil.

    👉 Bereit für neue Projekte? Klicke auf [|link_sf_facebook|] und werde noch heute Teil der Community!

.. _py_fruit_piano:

7.9 Bau eines Obst-Pianos
=================================================

In diesem Projekt bauen wir ein **Fruit Piano** mithilfe des Raspberry Pi Pico 2 W, eines kapazitiven MPR121-Touchsensors, eines Buzzers und einer RGB-LED. Indem wir Früchte (oder andere leitfähige Objekte) mit dem Touchsensor verbinden, verwandeln wir sie in Klaviertasten, die beim Berühren Töne abspielen und bunte Lichteffekte erzeugen.

**Benötigte Komponenten**

Für dieses Projekt werden die folgenden Bauteile benötigt:

Ein Komplettset ist besonders praktisch – hier der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ENTHALTENE TEILE
        - LINK
    *   - Pico 2 W Starter Kit	
        - 450+
        - |link_pico2w_kit|

Die Komponenten sind auch einzeln über folgende Links erhältlich:


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
        - 4 (1×1 kΩ, 1×330 Ω, 2×220 Ω)
        - |link_resistor_buy|
    *   - 7
        - Passive :ref:`cpn_buzzer`
        - 1
        - |link_passive_buzzer_buy|
    *   - 8
        - :ref:`cpn_rgb`
        - 1
        - |link_rgb_led_buy|
    *   - 9
        - :ref:`cpn_mpr121`
        - 1
        - 

**Komponenten verstehen**

*  **MPR121 kapazitiver Touchsensor**: Ein Sensorcontroller mit bis zu 12 Eingängen, der Änderungen der Kapazität durch Berührung erkennt.
*  **Passiver Buzzer**: Erzeugt Töne, wenn er über ein PWM-Signal angesteuert wird. Wir nutzen ihn zur Wiedergabe von Musiknoten.
*  **RGB-LED**: Kombiniert rote, grüne und blaue LEDs in einem Gehäuse. Durch Variieren der Helligkeit lassen sich verschiedenste Farben erzeugen.
*  **Früchte oder leitfähige Objekte**: Objekte wie Obst, Metall oder sogar Wasser können als Touch-Elektroden verwendet werden.

**Schaltplan**

|sch_fruit_piano|

Um eine Frucht in eine Klaviertaste zu verwandeln, müssen die MPR121-Elektroden mit der Frucht (z. B. dem Bananenstiel) verbunden werden.

Zu Beginn initialisiert der MPR121 alle Eingänge anhand des aktuellen 
Ladungszustands. Sobald ein Leiter (z. B. eine Hand) eine Elektrode berührt, 
verändert sich die Kapazität, was vom Sensor erkannt wird.

Achte während dieses Prozesses darauf, dass alle Verbindungen stabil sind, 
damit beim Start ein ausgeglichener Ladezustand gewährleistet ist.

**Verdrahtung**

|wiring_fruit_piano|


**Code schreiben**

Wir schreiben ein MicroPython-Skript, das:

* den MPR121-Touchsensor initialisiert,
* Touch-Eingaben von den angeschlossenen Früchten erkennt,
* entsprechende Töne über den Buzzer abspielt,
* und die RGB-LED mit zufälligen Farben leuchten lässt.

.. note::

    * Öffne ``7.9_fruit_piano.py`` aus ``pico-2w-kit-main/micropython`` oder kopiere den Code in Thonny, und klicke auf „Run“ oder drücke F5.
    * Achte darauf, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico) COMxx.
    * Die Bibliothek ``mpr121.py`` wird benötigt – überprüfe, ob sie auf den Pico hochgeladen wurde. Eine Anleitung findest du unter :ref:`add_libraries_py`.

.. code-block:: python

    from mpr121 import MPR121 
    from machine import Pin, I2C, PWM
    import time
    import urandom

    # I2C-Verbindung für den MPR121 kapazitiven Touchsensor initialisieren
    i2c = I2C(1, sda=Pin(6), scl=Pin(7))
    mpr = MPR121(i2c)

    # Notenfrequenzen in Hertz definieren
    NOTE_FREQUENCIES = [
        220,  # A3
        247,  # B3
        262,  # C4
        294,  # D4
        330,  # E4
        349,  # F4
        392,  # G4
        440,  # A4
        494,  # B4
        523,  # C5
        587,  # D5
        659   # E5
    ]

    # PWM für den Buzzer auf GP15 initialisieren
    buzzer = PWM(Pin(15))

    # PWM für die RGB-LED auf GP13 (Rot), GP12 (Grün), GP11 (Blau) initialisieren
    red = PWM(Pin(13))
    green = PWM(Pin(12))
    blue = PWM(Pin(11))

    # PWM-Frequenz für LEDs festlegen
    red.freq(1000)
    green.freq(1000)
    blue.freq(1000)

    # Funktion zum Abspielen eines Tons
    def play_tone(frequency):
        if frequency == 0:
            buzzer.duty_u16(0)
        else:
            buzzer.freq(frequency)
            buzzer.duty_u16(32768)  # 50 % Tastverhältnis

    # Funktion zum Stoppen des Tons
    def stop_tone():
        buzzer.duty_u16(0)

    # Funktion zur zufälligen Farbwahl der RGB-LED
    def set_random_color():
        red.duty_u16(urandom.getrandbits(16))
        green.duty_u16(urandom.getrandbits(16))
        blue.duty_u16(urandom.getrandbits(16))

    # Funktion zum Ausschalten der RGB-LED
    def turn_off_led():
        red.duty_u16(0)
        green.duty_u16(0)
        blue.duty_u16(0)

    # Hauptschleife
    try:
        last_touched = mpr.touched()
        while True:
            current_touched = mpr.touched()
            for i in range(12):
                pin_bit = 1 << i
                if current_touched & pin_bit and not last_touched & pin_bit:
                    # Elektrode i wurde gerade berührt
                    print("Pin {} touched".format(i))
                    play_tone(NOTE_FREQUENCIES[i])
                    set_random_color()
                if not current_touched & pin_bit and last_touched & pin_bit:
                    # Elektrode i wurde gerade losgelassen
                    print("Pin {} released".format(i))
                    stop_tone()
                    turn_off_led()
            last_touched = current_touched
            time.sleep(0.01)
    except KeyboardInterrupt:
        pass
    finally:
        stop_tone()
        turn_off_led()


.. note::

    Berühre die Früchte oder leitfähigen Objekte nicht, bevor das Programm gestartet wurde – dies kann die Initialisierung beeinträchtigen.

Nach dem Start des Programms kannst du die Früchte leicht berühren:

* Der Buzzer spielt den zugewiesenen Ton.
* Die RGB-LED leuchtet in einer zufälligen Farbe.
* Probiere verschiedene Früchte aus, um unterschiedliche Töne zu erzeugen.

**Den Code verstehen**

#. Initialisierung:

   * **I2C-Verbindung**: Stellt die Kommunikation mit dem MPR121 her.
   * **PWM-Einstellungen**: Initialisiert die Pins für den Buzzer und die RGB-LED.

#. Tonfrequenzen:

   Eine Liste mit Frequenzen für Musiknoten von A3 bis E5.

#. Funktionen:

   * ``play_tone(frequency)``: Spielt eine Note mit der angegebenen Frequenz.
   * ``stop_tone()``: Stoppt den Ton.
   * ``set_random_color()``: Setzt eine zufällige Farbe für die RGB-LED.
   * ``turn_off_led()``: Schaltet die RGB-LED aus.

#. Hauptschleife:

   * **Tasterkennung**: Überwacht die Elektroden kontinuierlich auf Berührungen.
   * **Reaktionen**:

     * Bei Berührung wird der Ton abgespielt und die LED aktiviert.
     * Bei Loslassen wird der Ton gestoppt und die LED ausgeschaltet.

   * **Entprellen**: Kurze Verzögerung (``time.sleep(0.01)``), um Störungen zu vermeiden.

#. Fehlerbehandlung:

   * Ermöglicht durch try/except ein sauberes Beenden mit Tastaturunterbrechung.
   * Im finally-Block werden Buzzer und LED sicher deaktiviert.


**Fehlersuche**

* Kein Ton oder Licht:

  * Überprüfe alle Verbindungen.
  * Stelle sicher, dass der MPR121 korrekt mit dem Pico verbunden ist.
  * Achte auf festen Kontakt zwischen Früchten und Elektroden.
  * Kontrolliere, ob ``mpr121.py`` auf dem Pico vorhanden ist.

* Berührungen werden nicht erkannt:

  * Vermeide es, mehrere Elektroden gleichzeitig zu berühren.
  * Berühre nur die Früchte oder leitfähigen Objekte – nicht die Kabel direkt.
  * Verwende am besten feuchte Früchte – sie leiten besser.

* Instabiles Verhalten:

  * Vermeide statische Aufladung am Pico oder Sensor.
  * Halte alle Verbindungen ruhig und stabil für genaue Messungen.

**Weitere Experimente**

* Instrument erweitern:

  * Verwende andere leitfähige Materialien wie Wasser oder Metall.
  * Weise zusätzliche Noten weiteren Elektroden zu.

* Lichteffekte anpassen:

  * Passe ``set_random_color()`` an, um gezielte Farbmuster zu erzeugen.
  * Integriere weitere LEDs für eindrucksvollere Effekte.

* Empfindlichkeit justieren:

  * Experimentiere mit den Schwellenwerten des MPR121 zur Feinabstimmung der Sensitivität.

* Weitere Sensoren integrieren:

  * Kombiniere das Projekt mit z. B. Lichtsensoren, um Ton und Licht an die Umgebung anzupassen.

**Fazit**

Du hast erfolgreich ein Obst-Piano mit dem Raspberry Pi Pico 2 W gebaut! Dieses kreative Projekt zeigt, wie kapazitive Berührungssensorik mit Ton- und Lichtausgabe kombiniert werden kann, um interaktive Erlebnisse zu gestalten.

Experimentiere ruhig weiter, erweitere das Design, füge neue Funktionen hinzu oder kombiniere es mit anderen Komponenten – deiner Kreativität sind keine Grenzen gesetzt.
