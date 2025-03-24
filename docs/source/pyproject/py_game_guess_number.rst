.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein – gemeinsam mit anderen Technikbegeisterten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Erhalte Hilfe bei technischen Problemen und Fragen nach dem Kauf durch unsere Community und unser Team.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Profitiere von exklusiven Vergünstigungen auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nimm an Verlosungen und Sonderaktionen zu Feiertagen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und trete noch heute bei!

.. _py_guess_number:

7.7 Erstellen eines „Zahlenraten“-Spiels
=============================================================

In diesem Projekt entwickeln wir ein interaktives **Zahlenraten**-Spiel mit dem Raspberry Pi Pico 2 W, einer 4x4-Matrix-Tastatur und einem I2C LCD1602-Display. Das Spiel generiert eine zufällige Zahl zwischen 0 und 99, und die Spieler geben nacheinander ihre Vermutungen ein. Nach jeder Eingabe wird der Wertebereich entsprechend eingegrenzt, bis jemand die richtige Zahl errät.


**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Bauteile.

Es ist besonders praktisch, ein komplettes Kit zu kaufen. Hier ist der Link: 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ENTHALTENE TEILE IM KIT
        - LINK
    *   - Pico 2 W Starter Kit	
        - 450+
        - |link_pico2w_kit|

Die Komponenten können auch einzeln über die folgenden Links erworben werden.


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
        - 4 (10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_keypad`
        - 1
        - |link_keypad_buy|
    *   - 7
        - :ref:`cpn_i2c_lcd`
        - 1
        - |link_i2clcd1602_buy|

**Verständnis der Komponenten**

* **4x4-Matrix-Tastatur**: Eine Tastatur mit 16 Tasten in einer 4x4-Matrix. Sie wird zur Eingabe von Zahlen und Befehlen verwendet.
* **I2C LCD1602-Display**: Ein 16x2-Zeichen-LCD mit I2C-Schnittstelle, das die Verkabelung vereinfacht, da nur zwei Datenleitungen (SDA und SCL) benötigt werden.

**Schaltplan**


|sch_guess_number|

Diese Schaltung basiert auf :ref:`py_keypad` und ergänzt ein I2C LCD1602-Display zur Anzeige der eingegebenen Zahlen.


**Verdrahtung**

|wiring_game_guess_number| 

Um die Verdrahtung zu erleichtern, wurden in der obigen Schaltung die Spalten der Matrix-Tastatur und die 10K-Widerstände gleichzeitig in die Steckplätze G10 bis G13 eingesetzt.


**Code schreiben**

Wir schreiben ein MicroPython-Programm, das:

* Eine zufällige Zahl zwischen 0 und 99 generiert.
* Tastatureingaben liest.
* Das LCD-Display mit Hinweisen und Benutzereingaben aktualisiert.
* Nach jeder Eingabe den Wertebereich eingrenzt.

.. note::

    * Öffne die Datei ``7.7_game_guess_number.py`` aus ``pico-2w-kit-main/micropython`` oder kopiere den Code in Thonny, dann klicke auf "Run" oder drücke F5.
    * Stelle sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx.
    * Die benötigte Bibliothek ``lcd1602.py`` muss auf den Pico hochgeladen sein. Eine detaillierte Anleitung findest du unter :ref:`add_libraries_py`.

.. code-block:: python

    from lcd1602 import LCD
    from machine import I2C, Pin
    import utime
    import urandom

    # I2C-Kommunikation für das LCD1602-Display initialisieren
    i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)
    lcd = LCD(i2c)

    # Tastatur-Zuordnung für eine 4x4-Matrix-Tastatur
    keypad_map = [
        ["1", "2", "3", "A"],
        ["4", "5", "6", "B"],
        ["7", "8", "9", "C"],
        ["*", "0", "#", "D"]
    ]

    # Reihen- und Spalten-Pins definieren
    row_pins = [Pin(pin_num, Pin.OUT) for pin_num in [21, 20, 19, 18]]  # R1-R4
    col_pins = [Pin(pin_num, Pin.IN, Pin.PULL_DOWN) for pin_num in [13, 12, 11, 10]]  # C1-C4

    # Funktion zum Scannen der Tastatur
    def read_keypad():
        for row_num, row_pin in enumerate(row_pins):
            row_pin.high()
            for col_num, col_pin in enumerate(col_pins):
                if col_pin.value() == 1:
                    row_pin.low()
                    return keypad_map[row_num][col_num]
            row_pin.low()
        return None

    # Spielvariablen initialisieren
    def init_game():
        global target_number, lower_bound, upper_bound, guess
        target_number = urandom.randint(0, 99)
        lower_bound = 0
        upper_bound = 99
        guess = ""
        lcd.clear()
        lcd.message("Press A to Start")

    # Anzeige aktualisieren
    def update_display(message):
        lcd.clear()
        lcd.message(message)

    # Hauptprogramm
    init_game()
    game_started = False

    while True:
        key = read_keypad()
        if key:
            utime.sleep(0.2)  # Entprellung

            if not game_started:
                if key == "A":
                    game_started = True
                    update_display("Enter your guess:")
            else:
                if key in "0123456789":
                    if len(guess) < 2:
                        guess += key
                        update_display("Guess: {}\n{} < ? < {}".format(guess, lower_bound, upper_bound))
                elif key == "D":
                    if guess != "":
                        guess_number = int(guess)
                        if guess_number < lower_bound or guess_number > upper_bound:
                            update_display("Out of range!\n{} < ? < {}".format(lower_bound, upper_bound))
                        elif guess_number > target_number:
                            upper_bound = guess_number - 1
                            guess = ""
                            update_display("Too High!\n{} < ? < {}".format(lower_bound, upper_bound))
                        elif guess_number < target_number:
                            lower_bound = guess_number + 1
                            guess = ""
                            update_display("Too Low!\n{} < ? < {}".format(lower_bound, upper_bound))
                        else:
                            update_display("Correct!\nNumber is {}".format(target_number))
                            game_started = False
                            utime.sleep(2)
                            init_game()
                    else:
                        update_display("Enter a number")
                elif key == "A":
                    # Restart the game
                    init_game()
                    game_started = True
                    update_display("Enter your guess:")
                elif key == "B":
                    # Clear current guess
                    guess = ""
                    update_display("Guess cleared")
                elif key == "C":
                    # Show hint or any other functionality
                    update_display("Hint not available")
        utime.sleep(0.1)

Nach dem Start des Codes folge diesen Schritten, um das Spiel zu spielen:

* Spiel starten:

  Drücke die 'A'-Taste auf der Tastatur.

* Eine Zahl eingeben:

  * Verwende die Zahlentasten, um deine Vermutung (0-99) einzugeben.
  * Drücke 'D', um deine Eingabe zu bestätigen.

* Rückmeldung erhalten:

  * Das LCD zeigt an, ob die Eingabe zu hoch, zu niedrig oder korrekt ist.
  * Der Wertebereich wird entsprechend angepasst.

* Das Spiel gewinnen:

  * Wenn du die richtige Zahl errätst, zeigt das LCD „Richtig! Die Zahl ist XX“ an.
  * Das Spiel wird nach einer kurzen Verzögerung automatisch zurückgesetzt.

**Verständnis des Codes**

#. Importieren und Initialisierung:

   * ``lcd1602.LCD``: Steuert das LCD-Display.
   * ``machine.Pin``: Ermöglicht die Interaktion mit den GPIO-Pins.
   * ``urandom``: Erzeugt Zufallszahlen.
   * Initialisiert die I2C-Kommunikation für das LCD1602-Display.

#. Tastatur-Scan-Funktion (``read_keypad``):

   * Setzt jede Zeile nacheinander auf HIGH.
   * Prüft, ob eine Spalte HIGH liest, um eine Tastenbetätigung zu erkennen.
   * Gibt das Zeichen der gedrückten Taste zurück.

   .. code-block:: python

        def read_keypad():
            for row_num, row_pin in enumerate(row_pins):
                row_pin.high()
                for col_num, col_pin in enumerate(col_pins):
                    if col_pin.value() == 1:
                        row_pin.low()
                        return keypad_map[row_num][col_num]
                row_pin.low()
            return None

#. Spielvariablen und Initialisierung (``init_game``):

   * ``target_number``: Zufallszahl zwischen 0 und 99.
   * ``lower_bound und upper_bound``: Beginnen bei 0 bzw. 99.
   * ``guess``: Speichert die aktuelle Eingabe.

   .. code-block:: python

        def init_game():
            global target_number, lower_bound, upper_bound, guess
            target_number = urandom.randint(0, 99)
            lower_bound = 0
            upper_bound = 99
            guess = ""
            lcd.clear()
            lcd.message("Press A to Start")

#. Anzeigeaktualisierung (``update_display``):

   Löscht das LCD und zeigt die übergebene Nachricht an.

   .. code-block:: python

        # Anzeigeaktualisierung
        def update_display(message):
            lcd.clear()
            lcd.message(message)

#. Hauptprogrammschleife:

   * Wartet auf Tastenanschläge und verarbeitet die Spiellogik.
   * Taste ``A``: Startet oder setzt das Spiel zurück.
   * Zahlen ``0``-``9``: Erstellt die aktuelle Zahleneingabe.
   * Taste ``D``: Bestätigt die Eingabe und aktualisiert den Wertebereich.
   * Prüft, ob die Eingabe innerhalb der aktuellen Grenzen liegt.
   * Aktualisiert ``lower_bound`` oder ``upper_bound`` basierend auf der Eingabe.
   * Setzt die Eingabe nach jeder Überprüfung zurück.
   * Falls die Eingabe korrekt ist, wird eine Erfolgsmeldung angezeigt und das Spiel zurückgesetzt.
   * Taste ``B``: Löscht die aktuelle Eingabe.
   * Taste ``C``: Reserviert für weitere Funktionen (z. B. Hinweise).

   .. code-block:: python

        while True:
            key = read_keypad()
            if key:
                utime.sleep(0.2)  # Entprellung

                if not game_started:
                    if key == "A":
                        game_started = True
                        update_display("Enter your guess:")
        ...
        ...
            utime.sleep(0.1)

#. Entprellung und Verzögerungen:

   * ``utime.sleep(0.2)``: Kurze Verzögerung nach einer Tasteneingabe zur Entprellung.
   * ``utime.sleep(0.1)``: Kleine Verzögerung in der Hauptschleife zur Reduzierung der CPU-Auslastung.


**Fehlersuche**

* LCD zeigt keinen Text an:

  * Überprüfe die SDA- und SCL-Verbindungen (GP6 und GP7).
  * Stelle sicher, dass das LCD korrekt mit Strom versorgt wird.
  * Passe das Kontrastpotentiometer auf der Rückseite des LCD-Moduls an.

* Tastatur reagiert nicht:

  * Prüfe alle Reihen- und Spaltenverbindungen.
  * Stelle sicher, dass Pull-Down-Widerstände angeschlossen sind, falls keine internen Pull-Downs verwendet werden.
  * Vergewissere dich, dass die Tastatur ordnungsgemäß funktioniert.

* Zufallszahl ändert sich nicht:

  * Stelle sicher, dass ``urandom`` korrekt importiert und verwendet wird.
  * Falls nötig, initialisiere den Zufallszahlengenerator für eine bessere Zufallsverteilung.

* Probleme mit der Spiellogik:

  * Überprüfe die Bedingungen und Grenzen bei der Verarbeitung der Eingaben.
  * Stelle sicher, dass lower bound und upper bound korrekt aktualisiert werden.

**Erweiterungen und Verbesserungen**

* Mehrspieler-Modus hinzufügen:

  * Speichere die Anzahl der Versuche pro Spieler.
  * Wechselnde Runden zwischen den Spielern.

* Punktesystem implementieren:

  * Vergib Punkte basierend darauf, wie schnell die Zahl erraten wurde.
  * Zeige Punktzahlen auf dem LCD an.

* Hinweise bereitstellen:

  Verwende die 'C'-Taste, um Hinweise anzuzeigen, z. B. „Zahl ist gerade“ oder „Zahl ist ein Vielfaches von 5“.

* Zahlenbereich vergrößern:

  * Erweitere das Spiel auf Zahlen zwischen 0 und 999.
  * Passe Anzeige und Eingabemethoden entsprechend an.

* Visuelles und akustisches Feedback:

  Füge LEDs oder einen Summer hinzu, um zusätzliches Feedback zu geben.

**Fazit**

Du hast erfolgreich ein interaktives „Zahlenraten“-Spiel mit dem Raspberry Pi Pico 2 W entwickelt! Dieses Projekt kombiniert Benutzereingaben, Zufallszahlengenerierung und Display-Ausgabe zu einem unterhaltsamen und lehrreichen Spiel. Es ist eine hervorragende Möglichkeit, den Umgang mit Tastaturen, LCD-Displays und Spielmechaniken in MicroPython zu üben.

Verbessere das Spiel weiter, indem du neue Funktionen hinzufügst oder die Benutzeroberfläche optimierst. Dieses Projekt kann als Grundlage für komplexere interaktive Anwendungen dienen.
