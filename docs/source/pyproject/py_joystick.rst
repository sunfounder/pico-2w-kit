.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein und tausche dich mit anderen Technikbegeisterten aus.

    **Warum beitreten?**

    - **Expertenunterstützung**: Erhalte Hilfe bei technischen Herausforderungen und Fragen nach dem Kauf durch unsere Community und unser Team.
    - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Profitiere von exklusiven Vergünstigungen auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nimm an besonderen Aktionen und Verlosungen teil.

    👉 Bereit, mit uns zu experimentieren und zu erschaffen? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _py_joystick:

4.1 Den Joystick verwenden
================================

In dieser Lektion lernen wir, wie man einen **Joystick** mit dem Raspberry Pi Pico 2 W verbindet, um analoge Werte auszulesen und Tastendrücke zu erkennen. Ein Joystick ist ein weit verbreitetes Eingabegerät, das Bewegungen entlang der X- und Y-Achse erfasst und oft eine zusätzliche Taste (Z-Achse) beinhaltet.

* :ref:`cpn_joystick`

**Benötigte Komponenten**

Für dieses Projekt benötigen wir folgende Bauteile:

Es ist praktisch, ein Komplettset zu kaufen. Hier ist der Link: 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name
        - ENTHALTENE TEILE
        - LINK
    *   - Pico 2 W Starter Kit
        - 450+
        - |link_pico2w_kit|

Alternativ kannst du die Komponenten auch einzeln kaufen:

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
        - :ref:`cpn_joystick`
        - 1
        - 

**Funktionsweise des Joysticks**

Ein typischer Joystick-Modul besteht aus zwei Potentiometern, die im rechten Winkel zueinander angeordnet sind:

* **X-Achse-Potentiometer**: Misst die Bewegung nach links und rechts.
* **Y-Achse-Potentiometer**: Misst die Bewegung nach oben und unten.
* **Z-Achse (Schalter)**: Eine digitale Taste, die beim Drücken aktiviert wird.

Durch das Auslesen der analogen Werte der X- und Y-Achse kann die Position des Joysticks bestimmt werden. Der Z-Achsen-Schalter ermöglicht die Erkennung eines Tastendrucks.


**Schaltplan**

|sch_joystick|

Der SW-Pin ist mit einem 10K-Pull-up-Widerstand verbunden, um einen stabilen High-Pegel sicherzustellen, wenn der Joystick nicht gedrückt wird. Andernfalls wäre der SW-Pin in einem undefinierten Zustand und könnte zufällige Werte liefern.

**Verdrahtung**

|wiring_joystick|


**Code schreiben**

Schreiben wir nun ein MicroPython-Programm, um die X- und Y-Positionen des Joysticks auszulesen und Tastendrücke zu erkennen.

.. note::

    * Öffne die Datei ``4.1_toggle_the_joystick.py`` aus dem Verzeichnis ``pico-2w-kit-main/micropython`` oder kopiere den Code in Thonny und klicke auf „Run“ oder drücke F5.
    * Stelle sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx. 



.. code-block:: python

    import machine
    import utime

    # ADC für die X- und Y-Achsen initialisieren
    x_adc = machine.ADC(27)  # GP27
    y_adc = machine.ADC(26)  # GP26

    # Digitale Eingabe für den Schalter initialisieren
    z_button = machine.Pin(22, machine.Pin.IN, machine.Pin.PULL_UP)

    while True:
        # Analoge Werte (0-65535) auslesen
        x_value = x_adc.read_u16()
        y_value = y_adc.read_u16()
        
        # Zustand des Schalters auslesen (0 oder 1)
        z_state = z_button.value()
        
        # Werte ausgeben
        print("X:", x_value, "Y:", y_value, "Button:", z_state)
        
        # Kleine Verzögerung zur besseren Lesbarkeit
        utime.sleep(0.2)


**Code-Erklärung**

#. Module importieren:

   * ``machine``: Zugriff auf die Hardware-Funktionen.
   * ``utime``: Zeitbezogene Funktionen für Verzögerungen.

#. ADC-Eingänge initialisieren:

   Die Pins GP27 und GP26 werden als ADC-Eingänge konfiguriert, um die Joystick-Positionen auszulesen.

   .. code-block:: python

      x_adc = machine.ADC(27)  # X-Achse an GP27
      y_adc = machine.ADC(26)  # Y-Achse an GP26

#. Digitale Eingabe initialisieren:

   * GP22 wird als digitaler Eingang für den Joystick-Schalter konfiguriert.
   * ``machine.Pin.PULL_UP`` sorgt dafür, dass der Pin High (1) ist, wenn der Schalter nicht gedrückt wird, und Low (0), wenn er gedrückt wird.

   .. code-block:: python

      z_button = machine.Pin(22, machine.Pin.IN, machine.Pin.PULL_UP)

#. Hauptschleife zur Erfassung der Werte:
   * Analoge Werte auslesen: ``read_u16()`` liest einen 16-Bit-Wert (0 bis 65535), der den Spannungspegel repräsentiert.
   * Werte ausgeben: Zeigt die X- und Y-Positionen sowie den Zustand des Tasters in der Konsole an.

   .. code-block:: python

      while True:
          x_value = x_adc.read_u16()
          y_value = y_adc.read_u16()
          z_state = z_button.value()
          
          print("X:", x_value, "Y:", y_value, "Button:", z_state)
          
          utime.sleep(0.2)

Nach dem Start des Programms öffne das Shell- oder REPL-Fenster in Thonny.

* Dort sollten die X-, Y- und Tastenwerte ausgegeben werden.
* Bewege den Joystick in verschiedene Richtungen und drücke den Knopf, um die Werteänderungen zu beobachten.

**Werte interpretieren**

* X- und Y-Werte:

  * Bereich von 0 bis 65535.
  * Mittlere Position: Etwa 32768.
  * Ganz links oder oben: Nahe 0.
  * Ganz rechts oder unten: Nahe 65535.

* Tastenstatus:

  * Nicht gedrückt: 1.
  * Gedrückt: 0.

**Weitere Experimente**

* Werte normalisieren:

  Konvertiere die Rohwerte des ADC in den Bereich -100 bis 100 für eine leichtere Interpretation.

  .. code-block:: python

    import machine
    import utime

    # ADC für X- und Y-Achsen initialisieren
    x_adc = machine.ADC(27)  # GP27
    y_adc = machine.ADC(26)  # GP26

    # Digitale Eingabe für den Schalter initialisieren
    z_button = machine.Pin(22, machine.Pin.IN, machine.Pin.PULL_UP)

    # Funktion zur Normalisierung von ADC-Werten in den Bereich -100 bis 100
    def normalize(value):
        return int((value - 32768) / 327.68)

    while True:
        # Analoge Werte (0-65535) auslesen
        x_value = x_adc.read_u16()
        y_value = y_adc.read_u16()
        
        # Zustand des Schalters auslesen (0 oder 1)
        z_state = z_button.value()
        
        # Werte normalisieren auf -100 bis 100
        x_normalized = normalize(x_value)
        y_normalized = normalize(y_value)
        
        # Normalisierte Werte ausgeben
        print("X:", x_normalized, "Y:", y_normalized, "Button:", z_state)
        
        # Kleine Verzögerung für bessere Lesbarkeit
        utime.sleep(0.2)


* Eine Ausgangssteuerung implementieren:

  Verwende die Joystick-Eingaben zur Steuerung einer LED, eines Servos oder eines Motors. Zum Beispiel kann die Bewegung entlang der X-Achse genutzt werden, um ein Objekt nach links oder rechts zu bewegen.

* Einen Game-Controller erstellen:

  Kombiniere die Joystick-Eingaben, um ein einfaches Spiel oder eine grafische Darstellung zu steuern.

**Fazit**

In dieser Lektion hast du gelernt, wie man analoge und digitale Eingaben eines Joysticks mit dem Raspberry Pi Pico 2 W ausliest. Mit diesem Wissen kannst du Joystick-Steuerungen in deine Projekte integrieren und interaktive Anwendungen wie Roboter, Spiele oder Fernbedienungen entwickeln.
