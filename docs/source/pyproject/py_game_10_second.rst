.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in Raspberry Pi, Arduino und ESP32 ein – zusammen mit anderen Technikbegeisterten.

    **Warum solltest du beitreten?**

    - **Expertenunterstützung**: Erhalte Hilfe bei Problemen nach dem Kauf und technischen Herausforderungen durch unsere Community und unser Team.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und ersten Einblicken.
    - **Spezielle Rabatte**: Profitiere von exklusiven Vergünstigungen auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nimm an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu experimentieren und zu entwickeln? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _py_10_second:

7.5 Erstellen eines "10-Sekunden"-Spiels
======================================================

In diesem spannenden Projekt entwickeln wir ein unterhaltsames Spiel namens **"10 Sekunden"**, bei dem der Raspberry Pi Pico 2 W, ein Kippschalter und eine 4-stellige 7-Segment-Anzeige verwendet werden. Ziel des Spiels ist es, einen Zauberstab (simuliert durch den an einem Stab befestigten Kippschalter) zu schütteln, um einen Timer zu starten, und ihn dann erneut zu schütteln, um den Timer so nah wie möglich an **10,00 Sekunden** zu stoppen. Es ist eine großartige Möglichkeit, dein Timing zu testen und Freunde herauszufordern, um herauszufinden, wer der wahre Zeitmagier ist!

**Erforderliche Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Es ist definitiv praktisch, ein komplettes Kit zu kaufen. Hier ist der Link: 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ENTHALTENE TEILE IM KIT
        - LINK
    *   - Pico 2 W Starter Kit	
        - 450+
        - |link_pico2w_kit|

Alternativ kannst du die Komponenten auch einzeln über die folgenden Links erwerben.


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
        - :ref:`cpn_resistor`
        - 5 (4 × 220Ω, 1 × 10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_4_dit_7_segment`
        - 1
        - 
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|
    *   - 8
        - :ref:`cpn_tilt`
        - 1
        - 

**Verständnis der Komponenten**

* **Kippschalter**: Ein Sensor, der die Orientierung oder Bewegung erkennt. Wird er geneigt, wird ein Stromkreis geschlossen oder unterbrochen, sodass Erschütterungen oder Bewegungen erkannt werden können.
* **4-stellige 7-Segment-Anzeige**: Zeigt Zahlen von 0000 bis 9999 an. Zur Steuerung mit weniger GPIO-Pins nutzen wir Schieberegister.
* **74HC595-Schieberegister**: Ein 8-Bit-Serial-In, Parallel-Out-Schieberegister, das es ermöglicht, mehrere Ausgänge mit wenigen GPIO-Pins zu steuern.

**Schaltplan**

|sch_10_second|


* Diese Schaltung basiert auf :ref:`py_74hc_4dig`, ergänzt durch einen Kippschalter.
* GP16 ist "high", wenn der Kippschalter aufrecht steht, und "low", wenn er geneigt wird.

**Verdrahtung**

|wiring_game_10_second| 

**Code schreiben**

Wir erstellen ein MicroPython-Skript, das:

* Erschütterungen mithilfe des Kippschalters erkennt.
* Einen Timer startet und stoppt.
* Die vergangene Zeit auf der 4-stelligen 7-Segment-Anzeige anzeigt.
* Multiplexing und Schieberegister verwendet, um die Anzeige effizient zu steuern.

.. code-block:: python

    from machine import Pin
    import utime

    # Steuerpins für das 74HC595 initialisieren
    SDI = machine.Pin(18, machine.Pin.OUT)   # Serieller Dateneingang (DS)
    RCLK = machine.Pin(19, machine.Pin.OUT)  # Register-Takt (STCP)
    SRCLK = machine.Pin(20, machine.Pin.OUT) # Schieberegister-Takt (SHCP)

    # 7-Segment-Codes für die Ziffern 0-9 (gemeinsame Kathode)
    SEGMENT_CODES = [0x3F,  # 0
                    0x06,  # 1
                    0x5B,  # 2
                    0x4F,  # 3
                    0x66,  # 4
                    0x6D,  # 5
                    0x7D,  # 6
                    0x07,  # 7
                    0x7F,  # 8
                    0x6F]  # 9

    # Pins zur Auswahl der Ziffern (gemeinsame Kathoden)
    digit_pins = [
        machine.Pin(10, machine.Pin.OUT),  # Ziffer 1
        machine.Pin(11, machine.Pin.OUT),  # Ziffer 2
        machine.Pin(12, machine.Pin.OUT),  # Ziffer 3
        machine.Pin(13, machine.Pin.OUT)   # Ziffer 4
    ]

    # Kippschalter initialisieren
    tilt_switch = Pin(16, Pin.IN, Pin.PULL_DOWN)

    # Variablen für die Zeitmessung
    start_time = 0
    elapsed_time = 0
    counting = False

    # Funktion zum Verschieben von Daten in das Schieberegister
    def shift_out(data):
        RCLK.low()
        for bit in range(7, -1, -1):
            SRCLK.low()
            bit_val = (data >> bit) & 0x01
            SDI.value(bit_val)
            SRCLK.high()
        RCLK.high()

    # Funktion zur Anzeige einer Ziffer an einer bestimmten Position
    def display_digit(position, digit):
    # Alle Ziffern ausschalten
    for dp in digit_pins:
        dp.high()
    # Segmentdaten senden
    shift_out(SEGMENT_CODES[digit])
    # Die ausgewählte Ziffer aktivieren (gemeinsame Kathode ist aktiv niedrig)
    digit_pins[position].low()
    # Kurze Verzögerung, um die Anzeige sichtbar zu machen
    utime.sleep_ms(5)
    # Die Ziffer wieder ausschalten
    digit_pins[position].high()

    # Funktion zur Anzeige der verstrichenen Zeit
    def display_time(time_ms):
    # Umwandlung der Zeit in Hundertstelsekunden
    centiseconds = int(time_ms / 10)
    # Begrenzung auf 9999, um die Anzeigegröße einzuhalten
    if centiseconds > 9999:
        centiseconds = 9999

    # Extrahieren der einzelnen Ziffern
    digits = [
        (centiseconds // 1000) % 10,
        (centiseconds // 100) % 10,
        (centiseconds // 10) % 10,
        centiseconds % 10
    ]
    # Jede Ziffer nacheinander anzeigen
    for i in range(4):
        display_digit(i, digits[i])

    # Interrupt-Handler für den Kippschalter
    def tilt_handler(pin):
    global counting, start_time, elapsed_time
    if not counting:
        # Zeitmessung starten
        counting = True
        start_time = utime.ticks_ms()
    else:
        # Zeitmessung stoppen
        counting = False
        elapsed_time = utime.ticks_diff(utime.ticks_ms(), start_time)

    # Einrichtung des Interrupts für den Kippschalter
    tilt_switch.irq(trigger=Pin.IRQ_RISING, handler=tilt_handler)

        # Hauptschleife
    while True:
        if counting:
            # Verstrichene Zeit berechnen
        current_time = utime.ticks_diff(utime.ticks_ms(), start_time)
        display_time(current_time)
    else:
        # Endgültige Zeit anzeigen
        display_time(elapsed_time)



Wenn der Code läuft, sollte die 4-stellige 7-Segment-Anzeige initialisiert werden und **00.00** anzeigen. 

* Timer starten:  

  * Schüttle den Zauberstab oder neige den Kippschalter, um den Interrupt auszulösen.  
  * Der Timer beginnt, ab 00.00 hochzuzählen.  

* Timer stoppen:  

  * Schüttle den Zauberstab erneut oder neige den Kippschalter.  
  * Der Timer stoppt und zeigt die endgültige Zeit an.  

* Ziel des Spiels:  

  * Versuche, den Timer so nah wie möglich an 10,00 Sekunden zu stoppen.  
  * Fordere deine Freunde heraus und finde heraus, wer die beste Zeit erreicht!  

**Den Code verstehen**  

#. Importe und Pin-Definitionen:  

   * ``machine.Pin``: Steuert die GPIO-Pins.  
   * ``utime``: Wird für Zeitfunktionen verwendet.  
   * SDI, SRCLK und RCLK-Pins zur Steuerung der Schieberegister definieren.  
   * Den Kippschalter an GP16 mit einem Pull-Down-Widerstand initialisieren.  

#. Segment- und Zifferncodes:

   * ``SEGMENT_CODES``: Liste mit den Binärcodes zur Darstellung der Ziffern 0–9 auf einer 7-Segment-Anzeige.  
   * ``digit_pins``: Steuerung der Ziffernanzeige. Die gemeinsame Kathode ist aktiv low.  

   .. code-block:: python

        # 7-Segment-Anzeigecodes für die Ziffern 0–9 (gemeinsame Kathode)
        SEGMENT_CODES = [0x3F,  # 0
                        0x06,  # 1
                        0x5B,  # 2
                        0x4F,  # 3
                        0x66,  # 4
                        0x6D,  # 5
                        0x7D,  # 6
                        0x07,  # 7
                        0x7F,  # 8
                        0x6F]  # 9

        # Initialisierung der Ziffernpins (gemeinsame Kathoden)
        digit_pins = [
            machine.Pin(10, machine.Pin.OUT),  # Ziffer 1
            machine.Pin(11, machine.Pin.OUT),  # Ziffer 2
            machine.Pin(12, machine.Pin.OUT),  # Ziffer 3
            machine.Pin(13, machine.Pin.OUT)   # Ziffer 4
        ]

#. Variablen für die Zeitmessung: 

   * ``start_time``: Speichert die Startzeit des Timers.  
   * ``elapsed_time``: Speichert die insgesamt verstrichene Zeit beim Stoppen des Timers.  
   * ``counting``: Ein boolescher Wert, der anzeigt, ob der Timer aktiv ist.  

#. Definition der Funktion ``shift_out``:  

   * Sendet 8-Bit-Daten an das 74HC595-Schieberegister.  
   * Überträgt die Daten beginnend mit dem höchstwertigen Bit (MSB).  
   * Steuert die Taktimpulse für das Schieberegister und das Register.  

   .. code-block:: python

        def shift_out(data):
            RCLK.low()
            for bit in range(7, -1, -1):
                SRCLK.low()
                bit_val = (data >> bit) & 0x01
                SDI.value(bit_val)
                SRCLK.high()
            RCLK.high()

#. Definition der Funktion ``display_digit``:  

   * Schaltet alle Ziffern aus.  
   * Sendet den Segmentcode für die Ziffer.  
   * Aktiviert die angegebene Ziffer durch Setzen ihres Pins auf low.  
   * Fügt eine kurze Verzögerung hinzu, um die Anzeige sichtbar zu machen.  
   * Schaltet die Ziffer nach der Anzeige wieder aus.  

   .. code-block:: python

        def display_digit(position, digit):
            for dp in digit_pins:
                dp.high()
            shift_out(SEGMENT_CODES[digit])
            digit_pins[position].low()
            utime.sleep_ms(5)
            digit_pins[position].high()

#. Funktion ``display_time``:  

   * Wandelt die vergangene Zeit von Millisekunden in Hundertstelsekunden um.  
   * Zerlegt die Zeit in einzelne Ziffern.  
   * Verwendet Multiplexing, um jede Ziffer schnell nacheinander anzuzeigen.  

   .. code-block:: python

        def display_time(time_ms):
            # Umrechnung der Zeit in Hundertstelsekunden
            centiseconds = int(time_ms / 10)
            # Begrenzung auf 9999, um in die Anzeige zu passen
            if centiseconds > 9999:
                centiseconds = 9999

            # Extrahieren der einzelnen Ziffern
            digits = [
                (centiseconds // 1000) % 10,
                (centiseconds // 100) % 10,
                (centiseconds // 10) % 10,
                centiseconds % 10
            ]
            # Jede Ziffer schnell hintereinander anzeigen
            for i in range(4):
                display_digit(i, digits[i])

#. Funktion ``tilt_handler``: 

   * Wird durch den Kippschalter-Interrupt ausgelöst.  
   * Schaltet zwischen Starten und Stoppen des Timers um.  
   * Speichert die ``start_time``, wenn die Messung beginnt.  
   * Berechnet die ``elapsed_time``, wenn die Messung stoppt.  

   .. code-block:: python

        def tilt_handler(pin):
            global counting, start_time, elapsed_time
            if not counting:
                # Zeitmessung starten
                counting = True
                start_time = utime.ticks_ms()
            else:
                # Zeitmessung stoppen
                counting = False
                elapsed_time = utime.ticks_diff(utime.ticks_ms(), start_time)

#. Hauptschleife:  

   * Wenn counting ``True`` ist, wird die Anzeige kontinuierlich mit der aktuellen verstrichenen Zeit aktualisiert.  
   * Wenn counting ``False`` ist, wird die endgültige ``elapsed_time`` angezeigt.  

   .. code-block:: python

        while True:
            if counting:
                # Verstrichene Zeit berechnen
                current_time = utime.ticks_diff(utime.ticks_ms(), start_time)
                display_time(current_time)
            else:
                # Endgültige Zeit anzeigen
                display_time(elapsed_time)

**Fehlersuche**  

* Anzeigeprobleme:  

  * Falls die Anzeige nicht korrekt funktioniert, überprüfe die Segment- und Zifferncodes sowie die Verdrahtung.  
  * Stelle sicher, dass das Schieberegister richtig angeschlossen ist und die Daten in der richtigen Reihenfolge übertragen werden.  

* Empfindlichkeit des Kippschalters:  

  * Falls der Kippschalter zu empfindlich oder nicht empfindlich genug reagiert, versuche, seine Ausrichtung anzupassen oder einen anderen Typ zu verwenden.  
  * Stelle sicher, dass der Pull-Down-Widerstand richtig angeschlossen ist, um Fehltrigger zu vermeiden.  

* Genauigkeit der Zeitmessung:  

  * Der Timer basiert auf der Systemuhr, die eine gewisse Genauigkeit bietet, aber leichte Abweichungen haben kann.  
  * Für höhere Genauigkeit kann ein externes Echtzeitmodul (RTC) verwendet werden.  

**Erweiterungen und Verbesserungen**  

* Visuelle Effekte: 

  * Füge LEDs hinzu, die blinken oder die Farbe ändern, wenn der Timer stoppt.  
  * Verwende einen Summer, um akustisches Feedback beim Starten und Stoppen des Timers zu geben.  

* Highscore-Speicherung:  

  * Speichere die beste Zeit (die am nächsten an 10,00 Sekunden liegt).  
  * Zeige eine Animation oder Nachricht an, wenn ein neuer Rekord erreicht wird.  


* Multiplayer-Modus: 

  * Mehrere Spieler können nacheinander spielen, wobei die Zeiten gespeichert werden.  
  * Zeige die Spielerzahlen und ihre jeweiligen Zeiten an.  

* Schwierigkeitsstufen: 

  * Füge verschiedene Zielzeiten ein (z. B. 5,00 Sekunden, 15,00 Sekunden), um den Schwierigkeitsgrad zu erhöhen.  
  * Wähle die Zielzeit zufällig aus und zeige sie zu Beginn jeder Runde an.  

* Alternative Eingabemethoden:  

  * Ersetze den Kippschalter durch einen Taster oder einen anderen Sensor, um den Timer zu starten und zu stoppen.  
  * Verwende einen Bewegungssensor, um bestimmte Gesten zu erkennen.  

**Fazit**  

Du hast erfolgreich ein "10-Sekunden"-Spiel mit dem Raspberry Pi Pico 2 W entwickelt! Dieses Projekt kombiniert Sensoreingaben, Zeitfunktionen und Anzeigesteuerung und bietet so ein interaktives und unterhaltsames Erlebnis. Es ist ein hervorragendes Beispiel dafür, wie Mikrocontroller für kreative und spielerische Anwendungen genutzt werden können.  

Passe das Projekt gerne an deine Ideen an und erweitere es nach Belieben. Ob neue Funktionen, verbessertes Design oder zusätzliche Komponenten – deiner Kreativität sind keine Grenzen gesetzt.

