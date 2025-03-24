.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein und tausche dich mit anderen Technikbegeisterten aus.

    **Warum beitreten?**

    - **Expertenunterstützung**: Erhalte Hilfe bei technischen Herausforderungen und Fragen nach dem Kauf von unserer Community und unserem Team.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Previews.
    - **Spezielle Rabatte**: Profitiere von exklusiven Vergünstigungen für unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nimm an Verlosungen und saisonalen Promotions teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _py_led_bar:

2.2 Anzeigen des Pegels
=============================

In dieser Lektion lernen wir, wie man eine LED-Balkenanzeige mit dem Raspberry Pi Pico steuert. Eine LED-Balkenanzeige besteht aus 10 in einer Reihe angeordneten LEDs und wird typischerweise zur Anzeige von Pegeln wie Lautstärke, Signalstärke oder anderen Messwerten verwendet. Wir werden die LEDs nacheinander einschalten, um einen ansteigenden Pegel-Effekt zu erzeugen.

|img_led_bar_pin|

* :ref:`cpn_led_bar`

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
        - 10 (220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led_bar`
        - 1
        - 

**Schaltplan**

|sch_ledbar|

In diesem Projekt ist jede der 10 LEDs in der LED-Balkenanzeige mit dem Raspberry Pi Pico 2 W verbunden. Die Anoden (positive Anschlüsse) der LEDs sind mit den GPIO-Pins GP6 bis GP15 verbunden. Die Kathoden (negative Anschlüsse) sind über 220Ω-Widerstände mit dem GND (Masse) verbunden.



**Verdrahtungsdiagramm**

|wiring_ledbar|

**Code schreiben**

.. note::

    * Öffne die Datei ``2.2_display_the_level.py`` unter dem Pfad ``pico-2w-kit-main/micropython`` oder kopiere diesen Code in Thonny, klicke dann auf "Run Current Script" oder drücke **F5**, um ihn auszuführen.

    * Stelle sicher, dass der Interpreter "MicroPython (Raspberry Pi Pico).COMxx" in der unteren rechten Ecke von Thonny ausgewählt ist.

.. code-block:: python

    import machine
    import utime

    # Definiere die GPIO-Pins, die mit den LEDs verbunden sind
    pins = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    leds = []

    # Initialisiere jeden Pin als Ausgang und speichere ihn in der Liste leds
    for pin_number in pins:
        led = machine.Pin(pin_number, machine.Pin.OUT)
        leds.append(led)

    while True:
        # LEDs nacheinander einschalten, um einen ansteigenden Pegel zu simulieren
        for led in leds:
            led.value(1)  # LED einschalten
            utime.sleep(0.2)
        # LEDs nacheinander ausschalten, um einen absteigenden Pegel zu simulieren
        for led in leds:
            led.value(0)  # LED ausschalten
            utime.sleep(0.2)

Wenn du das Programm ausführst, leuchten die LEDs in der LED-Balkenanzeige der Reihe nach von der ersten bis zur letzten auf, wodurch ein ansteigender Pegel-Effekt entsteht. Danach erlöschen sie nacheinander, um einen absteigenden Pegel zu simulieren.

**Den Code verstehen**

In diesem Projekt steuern wir mehrere LEDs mit Listen und Schleifen in MicroPython. Dies macht den Code effizient und gut lesbar.

Lass uns die wichtigsten Abschnitte des Codes durchgehen:

1. Bibliotheken importieren:

   * ``import machine``: Ermöglicht den Zugriff auf die Hardware-Funktionen des Raspberry Pi Pico 2 W.
   * ``import utime``: Ermöglicht die Verwendung von Zeitfunktionen wie Verzögerungen.

2. Pins definieren und LEDs initialisieren:

   * Wir erstellen eine Liste ``pins``, die die GPIO-Pin-Nummern der LEDs enthält, und eine leere Liste ``leds``, um die LED-Objekte zu speichern.

   .. code-block:: python

       # Definiere die GPIO-Pins, die mit den LEDs verbunden sind
       pins = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
       leds = []
      
   * Mit einer ``for``-Schleife durchlaufen wir jede Pin-Nummer, setzen sie als Ausgang und fügen das zugehörige ``Pin``-Objekt der ``leds``-Liste hinzu.

   .. code-block:: python

       for pin_number in pins:
           led = machine.Pin(pin_number, machine.Pin.OUT)
           leds.append(led)
      
3. Erstellen des Pegelanzeige-Effekts:

   * Die ``while True:``-Schleife läuft unendlich.
   * Ansteigender Pegel:
     * Eine ``for``-Schleife durchläuft jede LED in der ``leds``-Liste.
     * ``led.value(1)`` schaltet die LED ein.
     * ``utime.sleep(0.2)`` fügt eine 200ms-Verzögerung hinzu, bevor die nächste LED eingeschaltet wird.

     .. code-block:: python

        for led in leds:
            led.value(1)
            utime.sleep(0.2)

   * Absteigender Pegel:
     * Eine weitere ``for``-Schleife schaltet jede LED nacheinander aus.
     * ``led.value(0)`` schaltet die LED aus.

     .. code-block:: python

        for led in leds:
            led.value(0)
            utime.sleep(0.2)
  
**Weitere Experimente**

Experimentiere mit dem Code:

* Geschwindigkeit anpassen: 

    * Ändere die Verzögerung in ``utime.sleep(0.2)``, um die LEDs schneller oder langsamer ein- und auszuschalten.

* Reihenfolge umkehren: 

    * Verwende ``reversed(leds)``, um die LEDs in umgekehrter Reihenfolge einzuschalten.

  .. code-block:: python

      for led in reversed(leds):
          led.value(1)
          utime.sleep(0.2)

* Ping-Pong-Effekt erstellen: 

    * Lasse die LEDs von links nach rechts und dann wieder zurück von rechts nach links leuchten.

  .. code-block:: python

      while True:
          for led in leds:
              led.value(1)
              utime.sleep(0.1)
          for led in reversed(leds):
              led.value(0)
              utime.sleep(0.1)

**Fazit**

Durch die individuelle Steuerung jeder LED haben wir eine einfache, aber effektive Pegelanzeige mit dem Raspberry Pi Pico 2 W erstellt. Dieses Projekt zeigt die Leistungsfähigkeit von Listen und Schleifen in Python, wodurch sich mehrere Ausgänge effizient verwalten lassen.

Das Verständnis für die Arbeit mit mehreren GPIO-Pins und den Einsatz von Programmierstrukturen wie Listen und Schleifen ist entscheidend für komplexere Projekte – sei es die Erstellung von Animationen, die Steuerung mehrerer Sensoren oder der Bau interaktiver Geräte.

**Referenzen**

* |link_python_for|
* |link_python_list|
