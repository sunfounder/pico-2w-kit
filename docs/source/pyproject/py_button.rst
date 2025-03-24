.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche gemeinsam mit anderen Technikbegeisterten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum solltest du beitreten?**

    - **Expertenunterstützung**: Erhalte Hilfe bei Problemen nach dem Kauf und bei technischen Herausforderungen – durch unsere Community und unser Team.
    - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte vorab Einblicke in neue Produktankündigungen.
    - **Sonderrabatte**: Profitiere von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Aktionen und Verlosungen**: Nimm an saisonalen Events und Gewinnspielen teil.

    👉 Bereit für spannende Projekte? Klicke auf [|link_sf_facebook|] und mach mit!

.. _py_button:

2.5 Tasterwert auslesen
==============================================

In dieser Lektion lernst du, wie du mit dem Raspberry Pi Pico 2 W einen Taster als Eingang verwendest. Bisher haben wir die GPIO-Pins hauptsächlich für Ausgaben genutzt, z. B. zum Einschalten von LEDs. Nun verwenden wir einen GPIO-Pin als Eingang, um zu erkennen, wann ein Taster gedrückt wird – eine wichtige Grundlage für interaktive Projekte.

* :ref:`cpn_button`

**Benötigte Komponenten**

Für dieses Projekt benötigen wir folgende Bauteile:

Ein Komplettset ist besonders praktisch – hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name
        - ENTHALTENE TEILE
        - LINK
    *   - Pico 2 W Starter Kit
        - 450+
        - |link_pico2w_kit|

Du kannst die Teile auch einzeln über die folgenden Links beziehen:


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
        - 1 (10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_button`
        - 1
        - |link_button_buy|

**Schaltplan**

|sch_button|

Wenn eine Seite des Tasters mit 3,3 V verbunden ist und die andere Seite mit GP14, dann ist GP14 beim Drücken des Tasters HIGH. Ohne Tastendruck ist GP14 jedoch im Schwebezustand und kann HIGH oder LOW sein. Um im Ruhezustand einen stabilen LOW-Pegel zu erhalten, muss GP14 über einen 10K-Pull-Down-Widerstand mit GND verbunden werden.

* **Taster nicht gedrückt**: GP14 ist über den Widerstand mit GND verbunden und liest **LOW (0)**.
* **Taster gedrückt**: GP14 ist über den Taster mit 3,3 V verbunden und liest **HIGH (1)**.

**Verdrahtung**

.. Folgen wir dem Stromlaufplan, um die Schaltung aufzubauen!

.. 1. Verbinde den 3V3-Pin des Pico 2 W mit der positiven Spannungsleiste des Breadboards.
.. #. Stecke den Taster so ins Breadboard, dass er die mittlere Trennlinie überbrückt.

.. note::
    Ein vierpoliger Taster ist H-förmig aufgebaut. Die beiden linken bzw. rechten Pins sind intern miteinander verbunden. Das bedeutet, dass der Taster beim Überbrücken der Mittelreihe zwei Hälften mit derselben Reihennummer verbindet (z. B. sind in meiner Schaltung E23 mit F23 und E25 mit F25 verbunden).

    Solange der Taster nicht gedrückt wird, sind die linken und rechten Pins voneinander unabhängig – es fließt kein Strom von einer Seite zur anderen.



.. #. Verwende ein Jumperkabel, um einen der Tasterpins mit der positiven Spannungsleiste zu verbinden (in meinem Fall der Pin oben rechts).
.. #. Verbinde den anderen Pin (oben links oder unten links) mit GP14 über ein Jumperkabel.
.. #. Nutze einen 10K-Widerstand, um den Pin oben links mit der negativen Spannungsleiste zu verbinden.
.. #. Verbinde die negative Spannungsleiste des Breadboards mit GND des Pico.


|wiring_button|



**Code schreiben**

Wir schreiben ein einfaches Programm, das beim Drücken des Tasters eine Nachricht ausgibt.

.. note::

  * Öffne ``2.5_read_button_value.py`` aus ``pico-2w-kit-main/micropython`` oder kopiere den Code in Thonny. Klicke anschließend auf „Run“ oder drücke F5.
  * Achte darauf, dass der richtige Interpreter eingestellt ist: MicroPython (Raspberry Pi Pico).COMxx.

.. code-block:: python

    import machine
    import utime

    # GP14 als Eingang initialisieren
    button = machine.Pin(14, machine.Pin.IN)

    while True:
        if button.value() == 1:
            print("Button pressed!")
            utime.sleep(0.2)  # Entprell-Verzögerung

Während der Code läuft, beobachtest du Folgendes:

* **Nicht gedrückt**: Keine Ausgabe im Terminal.
* **Gedrückt**: „Button pressed!“ erscheint bei jedem Tastendruck in der Konsole.



**Codeerklärung**

#. Module importieren:

   * ``machine``: Zugriff auf Mikrocontroller-Hardware.
   * ``utime``: Zeitfunktionen wie Verzögerungen.

#. Tasterpin einrichten:

   * ``button = machine.Pin(14, machine.Pin.IN)``: Initialisiert GPIO14 als Eingang.

#. Hauptschleife:

   * ``while True``: Erstellt eine Endlosschleife.
   * ``if button.value() == 1``: Prüft, ob der Knopf gedrückt wurde.
   * ``button.value()`` gibt 1 zurück, wenn der Pin ein High-Signal liest (Knopf gedrückt).
   * ``print("Button pressed!")``: Gibt eine Nachricht in der Konsole aus.
   * ``utime.sleep(0.2)``: Wartet 200 Millisekunden, um den Knopf zu entprellen.

**Alternative Verdrahtung: Pull-Up-Widerstand**

Du kannst den Taster auch mit Pull-Up-Konfiguration anschließen:

#. Verbinde einen 10 kΩ-Widerstand zwischen GP14 und 3,3 V. Dadurch liegt der Pin im Ruhezustand auf HIGH.

|sch_button_pullup|

|wiring_button_pullup|

* **Taster nicht gedrückt**: GP14 liest HIGH (1).
* **Taster gedrückt**: GP14 wird über den Taster auf GND gezogen und liest LOW (0).

#. Angepasster Code für Pull-Up:

.. code-block:: python

    import machine
    import utime

       # Initialize GP14 as an input pin
    button = machine.Pin(14, machine.Pin.IN)

    while True:
        if button.value() == 0:
            print("Button pressed!")
            utime.sleep(0.2)

**Using Internal Pull-Up/Pull-Down Resistors**

Der Raspberry Pi Pico 2 W ermöglicht die Aktivierung interner Pull-up- bzw. Pull-down-Widerstände, wodurch externe Widerstände überflüssig werden.

Der Einsatz interner Widerstände vereinfacht die Verdrahtung und spart Platz, da auf zusätzliche externe Komponenten auf dem Breadboard verzichtet werden kann.

* Aktivieren des internen Pull-down-Widerstands:

  .. code-block:: python
  
      import machine
      import utime
  
      # Initialisiert GP14 als Eingang mit internem Pull-down-Widerstand
      button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
  
      while True:
          if button.value() == 1:
              print("Button pressed!")
              utime.sleep(0.2)

* Aktivieren des internen Pull-up-Widerstands:

  .. code-block:: python

    import machine
    import utime

    # Initialisiert GP14 als Eingang mit internem Pull-up-Widerstand
    button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)

    while True:
        if button.value() == 0:
            print("Button pressed!")
            utime.sleep(0.2)

**Experimenting Further**

* **Mehrere Taster**: Schließe zusätzliche Taster an andere GPIO-Pins an und passe den Code an, um mehrere Eingaben zu verarbeiten.
* **LED-Steuerung**: Kombiniere die Tastereingabe mit einer LED-Ausgabe, um den LED-Zustand beim Drücken des Tasters umzuschalten.

.. code-block:: python

    import machine
    import utime

    button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
    led = machine.Pin(15, machine.Pin.OUT)
    led_state = False

    while True:
        if button.value() == 1:
            led_state = not led_state  # Schaltet den LED-Zustand um
            led.value(led_state)
            utime.sleep(0.2)

**Conclusion**

Das Auslesen eines Tastersignals ist eine grundlegende Fähigkeit in der Mikrocontroller-Programmierung. Es ermöglicht die Entwicklung interaktiver Projekte, die auf Benutzereingaben reagieren. Das Verständnis über Pull-up- und Pull-down-Widerstände gewährleistet eine zuverlässige und stabile Signalverarbeitung von Eingabegeräten.
