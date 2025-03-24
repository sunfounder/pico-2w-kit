.. note:: 

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche mit Gleichgesinnten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum beitreten?**

    - **Expertenunterstützung**: Erhalte Hilfe von unserer Community und unserem Team bei technischen Herausforderungen und Support-Anfragen nach dem Kauf.
    - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um deine Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Profitiere von exklusiven Vergünstigungen auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nimm an Verlosungen und saisonalen Sonderaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _py_neopixel:

3.3 RGB-LED-Streifen
=======================

In dieser Lektion lernen wir, wie man einen **RGB-LED-Streifen** 
(speziell den WS2812-Typ) mit dem Raspberry Pi Pico 2 W und MicroPython steuert.

Der WS2812 ist eine intelligente LED, die einen Steuerchip und ein RGB-Modul in einem 5050-LED-Gehäuse vereint. Jede LED verfügt über einen eigenen integrierten Controller, wodurch jede LED individuell über eine einzige Datenleitung gesteuert werden kann. Dadurch lassen sich Farbe und Helligkeit jeder LED im Streifen unabhängig voneinander einstellen.

* :ref:`cpn_ws2812`

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
        - :ref:`cpn_ws2812`
        - 1
        - |link_ws2812_buy|


**Schaltplan**

|sch_ws2812|


**Verdrahtung**


|wiring_ws2812|

Achte auf den Stromverbrauch. Während der VBUS-Pin des Pico eine kleine Anzahl an LEDs (z. B. 8) mit Strom versorgen kann, erfordert eine größere Anzahl möglicherweise eine externe Stromquelle, um eine Überlastung des Pico zu vermeiden.




**Code schreiben**

.. note::

    * Öffne die Datei ``3.3_rgb_led_strip.py`` im Verzeichnis ``pico-2w-kit-main/micropython`` oder kopiere den Code in Thonny. Klicke dann auf "Run" oder drücke **F5**.

    * Stelle sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx.

    * Für dieses Projekt wird die Bibliothek ``ws2812.py`` benötigt. Überprüfe, ob sie auf den Pico hochgeladen wurde. Eine detaillierte Anleitung findest du unter :ref:`add_libraries_py`.
    

.. code-block:: python

    import machine
    from ws2812 import WS2812

    # LED-Streifen initialisieren
    led_strip = WS2812(machine.Pin(0), 8)  # GP0 verwenden, 8 LEDs

    # Farben für jede LED festlegen
    led_strip[0] = [255, 0, 0]     # Rot
    led_strip[1] = [0, 255, 0]     # Grün
    led_strip[2] = [0, 0, 255]     # Blau
    led_strip[3] = [255, 255, 0]   # Gelb
    led_strip[4] = [0, 255, 255]   # Cyan
    led_strip[5] = [255, 0, 255]   # Magenta
    led_strip[6] = [255, 255, 255] # Weiß
    led_strip[7] = [128, 128, 128] # Grau

    # LED-Streifen aktualisieren, um die Farben anzuzeigen
    led_strip.write()

Wenn dieser Code ausgeführt wird, zeigt der WS2812-LED-Streifen, der mit GP0 verbunden ist, die folgenden Farben an:

* **LED 0**: Rot (255, 0, 0)
* **LED 1**: Grün (0, 255, 0)
* **LED 2**: Blau (0, 0, 255)
* **LED 3**: Gelb (255, 255, 0)
* **LED 4**: Cyan (0, 255, 255)
* **LED 5**: Magenta (255, 0, 255)
* **LED 6**: Weiß (255, 255, 255)
* **LED 7**: Grau (128, 128, 128)

**Den Code verstehen**

#. Bibliotheken importieren:

   * ``machine``: Zugriff auf hardwarebezogene Funktionen.
   * ``WS2812``: Bibliothek zur Steuerung des WS2812-LED-Streifens.

#. LED-Streifen initialisieren:

   * ``led_strip = WS2812(machine.Pin(0), 8)``: Initialisiert den LED-Streifen mit 8 LEDs an GP0.

#. Farben festlegen:

   * ``led_strip[0] = [255, 0, 0]``: Jede LED erhält eine RGB-Farbe mit Werten zwischen 0 und 255.

#. LED-Streifen aktualisieren:

   * ``led_strip.write()``: Sendet die Farbdaten an den LED-Streifen.

**Erstelle einen fließenden Regenbogeneffekt!**

Jetzt erzeugen wir eine dynamische Lichtanimation, indem wir zufällig generierte Farben entlang des Streifens bewegen.

.. code-block:: python

    import machine
    from ws2812 import WS2812
    import utime
    import urandom

    # Anzahl der LEDs im Streifen
    NUM_LEDS = 8

    # LED-Streifen initialisieren
    led_strip = WS2812(machine.Pin(0), NUM_LEDS)

    def flowing_light():
        # Farben entlang des Streifens verschieben
        for i in range(NUM_LEDS - 1, 0, -1):
            led_strip[i] = led_strip[i - 1]
        # Zufällige Farbe für die erste LED erzeugen
        led_strip[0] = [urandom.getrandbits(8), urandom.getrandbits(8), urandom.getrandbits(8)]
        # LED-Streifen aktualisieren
        led_strip.write()
        # Kleine Verzögerung für sanfte Animation
        utime.sleep_ms(100)

    # Hauptschleife
    while True:
        flowing_light()


Wenn dieser Code läuft, zeigt der LED-Streifen eine dynamische Farbanimation mit zufälligen Farben, wobei eine neue zufällige Farbe vorne eingefügt wird und die Farben entlang des Streifens verschoben werden.

**Den Code verstehen**

#. Zufällige Farben erzeugen: Erstellt eine RGB-Farbe mit Werten zwischen 0 und 255.

   .. code-block:: python

        [urandom.getrandbits(8), urandom.getrandbits(8), urandom.getrandbits(8)]

#. Farben verschieben: Bewegt jede LED-Farbe um eine Position weiter, um den Fließeffekt zu erzeugen.

   .. code-block:: python

        for i in range(NUM_LEDS - 1, 0, -1):
            led_strip[i] = led_strip[i - 1]

#. Endlosschleife: Hält die Animation in Gang.

   .. code-block:: python

        while True:
            flowing_light()

**Weitere Experimente**

* **Geschwindigkeit anpassen**: Ändere ``utime.sleep_ms(100)``, um den Effekt zu beschleunigen oder zu verlangsamen.
* **Längere LED-Streifen**: Passe die Anzahl der LEDs in ``WS2812(machine.Pin(0), anzahl_leds)`` an.
* **Eigene Animationen**: Experimentiere mit Farbmustern, um eigene Effekte zu erstellen.

**Fazit**

Du hast gelernt, wie du einen RGB-LED-Streifen mit dem Raspberry Pi Pico 2 W und MicroPython steuerst! Dies eröffnet eine Vielzahl kreativer Möglichkeiten für beeindruckende Lichtinstallationen, Stimmungsbeleuchtung oder interaktive Kunstprojekte.



