.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein und tausche dich mit anderen Technikbegeisterten aus.

    **Warum beitreten?**

    - **Expertenunterstützung**: Erhalte Hilfe bei technischen Herausforderungen und Fragen nach dem Kauf von unserer Community und unserem Team.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Previews.
    - **Spezielle Rabatte**: Profitiere von exklusiven Vergünstigungen für unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nimm an Verlosungen und saisonalen Promotions teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _py_keypad:

4.2 4x4 Tastenfeld
========================

In dieser Lektion lernen wir, wie man ein **4x4-Matrix-Tastenfeld** mit dem Raspberry Pi Pico 2 W verbindet, um Tasteneingaben zu erkennen. Matrix-Tastaturen werden häufig in Geräten wie Taschenrechnern, Telefonen, Verkaufsautomaten und Sicherheitssystemen für numerische Eingaben verwendet.

* :ref:`cpn_keypad`
* `E.161 - Wikipedia <https://en.wikipedia.org/wiki/E.161>`_

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Es ist praktisch, ein komplettes Kit zu kaufen – hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name    
        - ENTHALTENE ARTIKEL IM KIT
        - LINK
    *   - Pico 2 W Starter Kit    
        - 450+
        - |link_pico2w_kit|

Alternativ kannst du die Komponenten auch einzeln über die unten stehenden Links erwerben.


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

**Das 4x4-Tastenfeld verstehen**

Ein 4x4-Tastenfeld besteht aus:

* **16 Tasten**, angeordnet in 4 Reihen und 4 Spalten.
* **8 Pins**: 4 sind mit den Reihen und 4 mit den Spalten verbunden.

Wenn eine Taste gedrückt wird, verbindet sie eine bestimmte Reihe mit einer bestimmten Spalte, sodass wir die Taste anhand der Zeilen- und Spaltennummern identifizieren können.

So ist das Tastenfeld angeordnet:

|img_keypad|

**Schaltplan**

|sch_keypad|

Vier Pull-Down-Widerstände sind mit jeder Spalte der Matrix-Tastatur verbunden, sodass G6 ~ G9 bei nicht gedrückten Tasten ein stabiles Low-Signal erhalten.

Die Reihen der Tastatur (G2 ~ G5) werden im Code auf High gesetzt. Wenn einer der Pins G6 ~ G9 auf High gelesen wird, wissen wir, dass eine Taste gedrückt wurde.

Beispiel: Wenn G6 auf High erkannt wird, wurde die Taste „1“ gedrückt. Das liegt daran, dass die Steuerpins von „1“ G2 und G6 sind. Wenn die Taste „1“ gedrückt wird, verbindet sie G2 mit G6, sodass G6 ebenfalls High ist.


**Verdrahtung**

|wiring_keypad|

Um die Verdrahtung zu erleichtern, werden in der obigen Abbildung die Spalten der Matrix-Tastatur und die 10K-Widerstände direkt an die Pins G6 ~ G9 angeschlossen.


**Code schreiben**

Lass uns ein MicroPython-Programm schreiben, um zu erkennen, welche Taste gedrückt wird.

.. note::

    * Öffne die Datei ``4.2_4x4_keypad.py`` aus ``pico-2w-kit-main/micropython`` oder kopiere den Code in Thonny. Klicke dann auf "Run" oder drücke F5.
    * Stelle sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx.


.. code-block:: python

    import machine
    import time

    # Zeichen auf dem Tastenfeld definieren
    keys = [
        ['1', '2', '3', 'A'],
        ['4', '5', '6', 'B'],
        ['7', '8', '9', 'C'],
        ['*', '0', '#', 'D']
    ]

    # GPIO-Pins für Reihen und Spalten definieren
    row_pins = [2, 3, 4, 5]   # GP2-GP5
    col_pins = [6, 7, 8, 9]   # GP6-GP9

    # Reihen als Ausgänge initialisieren
    rows = [machine.Pin(pin_num, machine.Pin.OUT) for pin_num in row_pins]

    # Spalten als Eingänge mit Pull-Down-Widerständen initialisieren
    cols = [machine.Pin(pin_num, machine.Pin.IN, machine.Pin.PULL_DOWN) for pin_num in col_pins]

    def scan_keypad():
        for i, row in enumerate(rows):
            # Alle Reihen auf Low setzen
            for r in rows:
                r.value(0)
            # Aktuelle Reihe auf High setzen
            row.value(1)
            # Spalten auf gedrückte Tasten überprüfen
            for j, col in enumerate(cols):
                if col.value() == 1:
                    # Taste erkannt
                    return keys[i][j]
        return None

    last_key = None

    while True:
        key = scan_keypad()
        if key != last_key:
            if key is not None:
                print("Key pressed:", key)
            last_key = key
        time.sleep(0.1)

**Den Code verstehen**

#. Tastenfeld-Layout definieren

   Diese 2D-Liste stellt das physische Layout des Tastenfelds dar.

   .. code-block:: python

        keys = [
            ['1', '2', '3', 'A'],
            ['4', '5', '6', 'B'],
            ['7', '8', '9', 'C'],
            ['*', '0', '#', 'D']
        ]


#. Pins initialisieren:

   .. code-block:: python

        row_pins = [2, 3, 4, 5]   # GPIO-Pins für die Reihen
        col_pins = [6, 7, 8, 9]   # GPIO-Pins für die Spalten

        # Reihen als Ausgänge initialisieren
        rows = [machine.Pin(pin_num, machine.Pin.OUT) for pin_num in row_pins]

        # Spalten als Eingänge mit Pull-Down-Widerständen initialisieren
        cols = [machine.Pin(pin_num, machine.Pin.IN, machine.Pin.PULL_DOWN) for pin_num in col_pins]

#. Die Funktion zur Tastenerkennung definieren:

    Diese Funktion scannt jede Reihe, indem sie auf High gesetzt wird, und überprüft, ob eine der Spalten ebenfalls High ist. Dies zeigt an, dass eine Taste gedrückt wurde.

   .. code-block:: python

        def scan_keypad():
            for i, row in enumerate(rows):
                # Alle Reihen auf Low setzen
                for r in rows:
                    r.value(0)
                # Aktuelle Reihe auf High setzen
                row.value(1)
                # Spalten auf gedrückte Tasten überprüfen
                for j, col in enumerate(cols):
                    if col.value() == 1:
                        # Taste erkannt
                        return keys[i][j]
            return None

#. Hauptschleife zur Erkennung von Tastendrücken:

   * Die Schleife scannt kontinuierlich nach Tastendrücken.
   * Sie überprüft, ob die aktuell erkannte Taste sich von der vorherigen unterscheidet, um Mehrfacherfassungen derselben Taste zu vermeiden (Entprellung).
   * Gibt die erkannte Taste aus, wenn eine neue Taste gedrückt wurde.

   .. code-block:: python

        last_key = None

        while True:
            key = scan_keypad()
            if key != last_key:
                if key is not None:
                    print("Key pressed:", key)
                last_key = key
            time.sleep(0.1)

Nachdem das Programm gestartet wurde, kannst du verschiedene Tasten auf dem Tastenfeld drücken. Das entsprechende Zeichen der Taste wird in der Thonny-Shell ausgegeben.

**Fehlersuche**

* Keine Ausgabe beim Drücken der Tasten:

  * Stelle sicher, dass alle Verbindungen korrekt sind.
  * Überprüfe, ob die Pull-Down-Widerstände richtig zwischen den Spalten-Pins und GND angeschlossen sind.

* Falsche Taste erkannt:

  * Prüfe die keys-Matrix, um sicherzustellen, dass sie mit dem Layout deines Tastenfelds übereinstimmt.
  * Stelle sicher, dass die Zeilen- und Spalten-Pins im Code mit den physischen Anschlüssen übereinstimmen.

* Mehrere Tasten erkannt:

  Mechanische Tastenfelder können gelegentlich Ghosting (Fehlregistrierung mehrerer Tasten) verursachen, wenn mehrere Tasten gleichzeitig gedrückt werden. Für diese grundlegende Einrichtung sollte immer nur eine Taste gleichzeitig gedrückt werden.

**Weitere Experimente**

* **Einfaches Passwortschloss implementieren**: Speichere eine Sequenz von Tastendrücken und vergleiche sie mit einem voreingestellten Passwort.
* **Ein LCD-Display hinzufügen**: Zeige die gedrückten Tasten auf einem LCD-Bildschirm an.
* **Einen Taschenrechner erstellen**: Nutze das Tastenfeld, um Zahlen einzugeben und einfache Rechenoperationen durchzuführen.

**Fazit**

In dieser Lektion hast du gelernt, wie du ein 4x4-Matrix-Tastenfeld mit dem Raspberry Pi Pico 2 W verbindest und programmierst. Damit kannst du nun Tastendrücke erkennen und sie zur Interaktion mit deinen Projekten nutzen – beispielsweise für Zugangskontrollen, Taschenrechner oder Steuerungsinterfaces.
