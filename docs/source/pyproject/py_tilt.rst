.. note::
    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Vertiefe dich mit anderen Enthusiasten in die Welt von Raspberry Pi, Arduino und ESP32.

    **Warum beitreten?**

    - **Expertenunterstützung**: Löse Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Promotionen und Gewinnspiele**: Nimm an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt heute bei!

.. _py_tilt:


2.6 Kippe es!
==========================

|img_tilt|

In dieser Lektion lernen wir, wie man einen Neigungsschalter mit dem Raspberry Pi Pico 2 W verwendet, um Änderungen der Ausrichtung zu erkennen. Ein Neigungsschalter ist ein einfaches Gerät, das erkennen kann, ob es aufrecht oder geneigt ist, was es nützlich für Anwendungen wie Bewegungserkennung, Orientierungssensorik oder als Auslöser basierend auf der Position macht.

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Es ist definitiv praktisch, ein ganzes Kit zu kaufen, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ARTIKEL IN DIESEM KIT
        - LINK
    *   - Pico 2 W Starter Kit	
        - 450+
        - |link_pico2w_kit|


Du kannst sie auch einzeln über die untenstehenden Links kaufen.


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
        - Micro USB-Kabel
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
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_tilt`
        - 1
        - 

**Schaltplan**

|sch_tilt|

* **Im aufrechten Zustand (Schalter geschlossen)**:

  * Der Neigungsschalter verbindet **3,3V** direkt mit **GP14**.
  * Der GPIO-Pin liest **HOCH** (1).

* **Im geneigten Zustand (Schalter geöffnet)**:

  * Der Neigungsschalter trennt **3,3V** von **GP14**.
  * Der Pull-Down-Widerstand zieht **GP14** auf **GND**.
  * Der GPIO-Pin liest **NIEDRIG** (0).

* :ref:`cpn_tilt`

**Verdrahtung**

|wiring_tilt|



**Schreiben des Codes**

Wir schreiben ein einfaches MicroPython-Programm, das den Zustand des Neigungsschalters erkennt und eine Nachricht ausgibt, wenn der Schalter geneigt wird.

.. note::

    * Öffne die Datei ``2.6_tilt_switch.py`` aus ``pico-2w-kit-main/micropython`` oder kopiere den Code in Thonny, dann klicke auf "Ausführen" oder drücke F5.
    * Stelle sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx. 
    

.. code-block:: python

    import machine
    import utime

    # Initialisiere GP14 als Eingangspin
    tilt_switch = machine.Pin(14, machine.Pin.IN)

    while True:
        if tilt_switch.value() == 0:
            print("Tilt detected!")
            utime.sleep(1)  # Verzögerung, um mehrfache schnelle Erkennungen zu vermeiden

Wenn der Code läuft, wirst du folgendes Phänomen beobachten:

* Halte den Neigungsschalter aufrecht; es sollte keine Nachricht erscheinen. 
* Kippe das Breadboard oder den Schalter; "Kippung erkannt!" sollte in der Konsole erscheinen.

**Verständnis des Codes**

#. Module importieren:

   * ``import machine``: Gibt uns Zugang zu den Hardwarekomponenten.
   * ``import utime``: Ermöglicht uns die Verwendung von zeitbezogenen Funktionen.

#. Initialisierung des Neigungsschalter-Pins:

   * ``tilt_switch = machine.Pin(14, machine.Pin.IN)``: Richtet GP14 als Eingangspin ein.

#. Hauptschleife:

   * ``while True``: Erstellt eine unendliche Schleife, um kontinuierlich den Zustand des Neigungsschalters zu überprüfen.
   * ``if tilt_switch.value() == 0``: Überprüft, ob der GPIO-Pin NIEDRIG (0) liest, was darauf hinweist, dass der Schalter geneigt ist.
   * ``print("Tilt detected!")``: Gibt eine Nachricht aus, wenn die Kippung erkannt wird.
   * ``utime.sleep(1)``: Fügt eine 1-Sekunden-Verzögerung hinzu, um den Schalter zu entprellen und mehrfache Erkennungen zu verhindern.

**Alternative Verdrahtung: Verwendung eines internen Pull-Down-Widerstands**

Der Raspberry Pi Pico 2 W ermöglicht es uns, interne Pull-Up- oder Pull-Down-Widerstände zu aktivieren, was den Bedarf an einem externen Widerstand eliminiert.

.. code-block:: python

    import machine
    import utime

    # Initialisiere GP14 als Eingangspin mit internem Pull-Down-Widerstand
    tilt_switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

    while True:
        if tilt_switch.value() == 1:
            print("Tilt detected!")
            utime.sleep(1)

Durch Aktivieren des internen Pull-Down-Widerstands (``machine.Pin.PULL_DOWN``) wird der GPIO-Pin standardmäßig auf NIEDRIG gesetzt, wenn keine Spannung angelegt wird.
Wenn der Neigungsschalter aufrecht (geschlossen) ist, verbindet er 3,3V mit GP14, und der Pin liest HOCH (1).

**Praktische Anwendungen**

* **Orientierungserkennung**: Bestimme, ob ein Gerät aufrecht oder geneigt ist.
* **Bewegungsausgelöste Ereignisse**: Aktiviere Alarme, Benachrichtigungen oder Aktionen, wenn eine Bewegung erkannt wird.
* **Interaktive Projekte**: Verwende es als Eingabe, um Spiele oder Installationen zu steuern, die auf Kippen reagieren.

**Weiteres Experimentieren**

* LED-Anzeige hinzufügen:

Verbinde eine LED mit einem anderen GPIO-Pin (z.B. GP15) mit einem geeigneten Widerstand. Modifiziere den Code, um die LED leuchten zu lassen, wenn eine Kippung erkannt wird.

.. code-block:: python

    import machine
    import utime

    tilt_switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
    led = machine.Pin(15, machine.Pin.OUT)

    while True:
        if tilt_switch.value() == 1:
            print("Tilt detected!")
            led.value(1)  # Schalte die LED ein
            utime.sleep(1)
        else:
            led.value(0)  # Schalte die LED aus

* Verwende es mit anderen Sensoren:

  Kombiniere den Neigungsschalter mit anderen Sensoren wie Tasten oder Lichtsensoren für komplexere Interaktionen.

**Fazit**

Durch die Integration eines Neigungsschalters in deine Raspberry Pi Pico 2 W-Projekte kannst du eine neue Dimension der Interaktivität basierend auf Orientierung und Bewegung hinzufügen. Das Verständnis, wie man digitale Eingaben von Sensoren wie dem Neigungsschalter liest, erweitert deine Fähigkeit, dynamische und reaktionsfähige Elektronik zu erstellen.
