.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer ein in Raspberry Pi, Arduino und ESP32 zusammen mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Löse Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Community und unserem Team.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Promotionen und Giveaways**: Nimm an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt heute bei!

.. _py_rgb:


2.4 Buntes Licht
==============================================

In dieser Lektion erforschen wir, wie man verschiedene Farben mit einer RGB-LED und dem Raspberry Pi Pico 2 W erzeugt. Durch Anpassen der Intensität der roten, grünen und blauen Komponenten können wir Licht mischen, um eine breite Palette von Farben zu erzeugen. Dieses Konzept basiert auf der additiven Methode der Farbmischung.

**Was ist additive Farbmischung?**

Die additive Farbmischung beinhaltet das Kombinieren verschiedener Lichtfarben, um neue Farben zu erzeugen. Wenn rotes, grünes und blaues Licht in verschiedenen Intensitäten kombiniert werden, können sie jede Farbe im sichtbaren Spektrum erzeugen. Zum Beispiel:

* **Rot + Grün = Gelb**
* **Rot + Blau = Magenta**
* **Grün + Blau = Cyan**
* **Rot + Grün + Blau = Weiß**

|img_rgb_mix|

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
        - 3(1-330Ω, 2-220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_rgb`
        - 1
        - |link_rgb_led_buy|

**Schaltplan**

|sch_rgb|

Die PWM-Pins GP13, GP14 und GP15 steuern die Rot-, Grün- und Blau-Pins der RGB-LED und verbinden den gemeinsamen Kathoden-Pin mit GND. Dies ermöglicht der RGB-LED, eine spezifische Farbe anzuzeigen, indem Licht auf diesen Pins mit verschiedenen PWM-Werten überlagert wird.


**Verdrahtungsdiagramm**

|img_rgb_pin|

Die RGB-LED hat 4 Pins: Der lange Pin ist der gemeinsame Kathoden-Pin, der normalerweise mit GND verbunden ist; der linke Pin neben dem längsten Pin ist Rot; und die zwei Pins rechts sind Grün und Blau.

Wir verwenden einen höheren Widerstand für die rote LED, da sie typischerweise heller als die grünen und blauen LEDs bei gleichem Strom ist.


|wiring_rgb|



**Programmierung**

Wir werden ein MicroPython-Programm schreiben, das die Intensität jeder Farbe mit Pulsweitenmodulation (PWM) steuert, um verschiedene Farben zu erzeugen.

.. note::

    * Öffne die ``2.4_colorful_light.py`` aus ``pico-2w-kit-main/micropython`` oder kopiere den Code in Thonny, dann klicke auf "Ausführen" oder drücke F5.
    * Stelle sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx. 
    

.. code-block:: python

    import machine
    import utime

    # Initialisiere PWM für die roten, grünen und blauen Pins
    rot = machine.PWM(machine.Pin(13))
    grün = machine.PWM(machine.Pin(14))
    blau = machine.PWM(machine.Pin(15))

    # Setze die PWM-Frequenz
    rot.freq(1000)
    grün.freq(1000)
    blau.freq(1000)

    def map_value(x, in_min, in_max, out_min, out_max):
        # Mappe einen Wert von einem Bereich in einen anderen
        return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

    def set_color(r, g, b):
        # Stelle die Farbe durch Anpassen der Tastzyklen ein
        rot.duty_u16(map_value(r, 0, 255, 0, 65535))
        grün.duty_u16(map_value(g, 0, 255, 0, 65535))
        blau.duty_u16(map_value(b, 0, 255, 0, 65535))

    # Beispiel: Stelle die Farbe auf Orange ein
    set_color(255, 165, 0)

Wenn das Programm läuft, wird die RGB-LED ein orangenes Licht ausstrahlen.

**Verständnis des Codes**

#. Importierte Bibliotheken:

   * ``machine``: Um hardware-spezifische Funktionen zu nutzen.
   * ``utime``: Für zeitbezogene Funktionen (nicht in diesem Beispiel verwendet, aber nützlich für Animationen).

#. Initialisiere PWM-Objekte:

   * Erstelle PWM-Objekte für die mit der RGB-LED verbundenen roten, grünen und blauen Pins und setze die PWM-Frequenz auf 1000 Hz für alle Farben.

   .. code-block:: python

        # Initialisiere PWM für die roten, grünen und blauen Pins
        rot = machine.PWM(machine.Pin(13))
        grün = machine.PWM(machine.Pin(14))
        blau = machine.PWM(machine.Pin(15))

        # Setze die PWM-Frequenz
        rot.freq(1000)
        grün.freq(1000)
        blau.freq(1000)

#. Definiere die ``map_value`` Funktion:

   * Da die Methode ``duty_u16`` Werte von 0 bis 65535 akzeptiert, aber Farbwerte typischerweise im Bereich 0 bis 255 liegen, müssen wir den Bereich 0-255 auf 0-65535 mappen.
   * Die Funktion ``map_value`` skaliert den Eingabewert entsprechend.

   .. code-block:: python

        def map_value(x, in_min, in_max, out_min, out_max):
            # Mappe einen Wert von einem Bereich in einen anderen
            return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

#. Definiere die ``set_color`` Funktion:

   Diese Funktion nimmt RGB-Werte (jeweils von 0 bis 255) und stellt den Tastzyklus für jeden Farbkanal nach der Mapping ein.

   .. code-block:: python

        def set_color(r, g, b):
            # Stelle die Farbe durch Anpassen der Tastzyklen ein
            rot.duty_u16(map_value(r, 0, 255, 0, 65535))
            grün.duty_u16(map_value(g, 0, 255, 0, 65535))
            blau.duty_u16(map_value(b, 0, 255, 0, 65535))
    
#. Stelle die gewünschte Farbe ein:

   Rufe ``set_color(255, 165, 0)`` auf, um die RGB-LED auf Orange zu stellen. Du kannst die Werte auf jede RGB-Farbe ändern, die du möchtest.

**Beispiel: Farbzyklus**

Lassen Sie uns den Code erweitern, um verschiedene Farben durchzugehen.

#. Um die RGB-Werte für verschiedene Farben zu finden, können Sie jede Grafiksoftware oder einen Online-Farbwähler verwenden. Zum Beispiel:

   * Rot: (255, 0, 0)
   * Grün: (0, 255, 0)
   * Blau: (0, 0, 255)
   * Weiß: (255, 255, 255)
   * Lila: (128, 0, 128)

#. Schreibe den Code.

   Wir definieren eine Liste von RGB-Tupeln, die verschiedene Farben darstellen.
   Die Schleife ``while True`` durchläuft jede Farbe, stellt die RGB-LED auf diese Farbe ein und wartet 1 Sekunde, bevor sie zur nächsten Farbe übergeht.

   .. code-block:: python
   
       import machine
       import utime
   
       # Initialisiere PWM für die roten, grünen und blauen Pins
       rot = machine.PWM(machine.Pin(13))
       grün = machine.PWM(machine.Pin(14))
       blau = machine.PWM(machine.Pin(15))
   
       # Setze die PWM-Frequenz
       rot.freq(1000)
       grün.freq(1000)
       blau.freq(1000)
   
       def map_value(x, in_min, in_max, out_min, out_max):
           return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
   
       def set_color(r, g, b):
           rot.duty_u16(map_value(r, 0, 255, 0, 65535))
           grün.duty_u16(map_value(g, 0, 255, 0, 65535))
           blau.duty_u16(map_value(b, 0, 255, 0, 65535))
   
       # Liste von Farben, durch die zyklisch gewechselt wird
       colors = [
           (255, 0, 0),     # Rot
           (0, 255, 0),     # Grün
           (0, 0, 255),     # Blau
           (255, 255, 0),   # Gelb
           (0, 255, 255),   # Cyan
           (255, 0, 255),   # Magenta
           (255, 255, 255)  # Weiß
       ]
   
       while True:
           for color in colors:
               set_color(*color)
               utime.sleep(1)

Wenn dieser Code läuft, wird die RGB-LED eine Sequenz von Farben durchlaufen: rot, grün, blau, gelb, cyan, magenta und weiß.

Jede Farbe wird 1 Sekunde lang angezeigt, bevor sie zur nächsten in der Liste übergeht.

**Fazit**

Durch die Steuerung der Intensität der roten, grünen und blauen Komponenten einer RGB-LED mittels PWM können wir eine riesige Palette von Farben erzeugen. Dieses Projekt demonstriert die Prinzipien der additiven Farbmischung und bietet eine Grundlage für das Erstellen farbenfroher Lichtdisplays mit Mikrocontrollern.


**Referenzen**

* |link_mpython_pwm|
