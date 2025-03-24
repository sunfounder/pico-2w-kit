.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Vertiefe dich tiefer in Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Löse Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unserem Team.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Promotionen und Giveaways**: Nimm an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt heute bei!

.. _py_slide:

2.7 Umschalten Links und Rechts
====================================

|img_slide|

In dieser Lektion lernen wir, wie man einen **Schiebeschalter** mit dem Raspberry Pi Pico 2 W verwendet, um seine Position (links oder rechts) zu erkennen und darauf basierende Aktionen auszuführen. Ein Schiebeschalter ist ein einfaches mechanisches Gerät, das den gemeinsamen (mittleren) Pin je nach Position mit einem der beiden äußeren Pins verbindet.

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
        - 1 (10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_capacitor`
        - 1 (104)
        - |link_capacitor_buy|
    *   - 7
        - :ref:`cpn_slide_switch`
        - 1
        - 

**Schaltplan**

|img_slide|

Ein Schiebeschalter hat drei Pins:

- **Pin 1**: Verbunden, wenn der Schalter auf eine Seite umgelegt wird (z. B. links)
- **Pin 2**: Gemeinsamer Pin (Mittelpin)
- **Pin 3**: Verbunden, wenn der Schalter auf die andere Seite umgelegt wird (z. B. rechts)

Durch das Lesen der Spannung am gemeinsamen Pin können wir die Position des Schalters bestimmen.

**Schaltbild**

|sch_slide|

GP14 erhält ein unterschiedliches Signal, wenn du den Schiebeschalter nach rechts oder links umlegst.

Der Zweck des 10K-Widerstands besteht darin, GP14 während des Umschaltens niedrig zu halten (nicht ganz links und nicht ganz rechts umgeschaltet).

Wenn du den Schalter umlegst, können die mechanischen Kontakte schnelle, störende Signale verursachen, die als "Prellen" bekannt sind. Der zwischen GP14 und GND angeschlossene Kondensator hilft, diese schnellen Schwankungen herauszufiltern und liefert ein saubereres Signal.

* Schalter nach rechts umgelegt:

  * Pin 2 (GP14) ist durch Pin 1 mit **3.3V** verbunden.
  * Der GPIO-Pin liest **HOCH** (1).

* Schalter nach links umgelegt:

  * Pin 2 (GP14) ist durch Pin 3 mit **GND** verbunden.
  * Der GPIO-Pin liest **NIEDRIG** (0).

* Schalter in Mittelposition:

  * Pin 2 (GP14) ist nicht mit **3.3V** oder **GND** verbunden.
  * Der Pull-Down-Widerstand hält den GPIO-Pin auf **NIEDRIG** (0).
  * Der Kondensator hilft, das Schalterprellen zu reduzieren (Geräusche durch mechanische Bewegung).


**Verdrahtung**

|wiring_slide|

**Programmierung**

Wir werden ein MicroPython-Programm schreiben, das die Position des Schiebeschalters erkennt und entsprechend eine Nachricht ausgibt.

.. note::

  * Öffne die ``2.7_slide_switch.py`` aus ``pico-2w-kit-main/micropython`` oder kopiere den Code in Thonny, dann klicke auf "Ausführen" oder drücke F5.

  * Stelle sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx. 

  

.. code-block:: python

  import machine
  import utime

  # Initialisiere GP14 als Eingang
  slide_switch = machine.Pin(14, machine.Pin.IN)

  while True:
      switch_state = slide_switch.value()
      if switch_state == 1:
          print("Switch is toggled to the LEFT!")
      else:
          print("Switch is toggled to the RIGHT!")
      utime.sleep(0.5)

Wenn der Code läuft, wirst du folgendes Phänomen beobachten:

* **Umschalten nach rechts**: Du solltest "Schalter ist nach RECHTS umgelegt!" in der Konsole sehen.
* **Umschalten nach links**: Du solltest "Schalter ist nach LINKS umgelegt!" in der Konsole sehen.


**Verständnis des Codes**

#. Importiere Module:

   * ``import machine``: Zugriff auf Hardwarefunktionen.
   * ``import utime``: Verwende zeitbezogene Funktionen.

#. Initialisiere den Schiebeschalter-Pin:

   * ``slide_switch = machine.Pin(14, machine.Pin.IN)``: Richtet GP14 als Eingangspin ein.

#. Hauptschleife:

   * ``while True``: Erstellt eine unendliche Schleife, um kontinuierlich den Schalterzustand zu überprüfen.
   * ``switch_state = slide_switch.value()``: Liest den aktuellen Zustand des Schalters.
   * ``if switch_state == 1``: Überprüft, ob der GPIO-Pin HOCH ist (Schalter nach links umgelegt).
   * ``print("Switch is toggled to the RIGHT!")``: Gibt eine Nachricht aus.
   * ``else``: Wenn der GPIO-Pin NIEDRIG ist (Schalter nach rechts oder in der Mitte umgelegt).
   * ``print("Switch is toggled to the LEFT!")``: Gibt eine Nachricht aus.
   * ``utime.sleep(0.5)``: Fügt eine kurze Verzögerung hinzu, um den Schalter zu entprellen und die Konsole nicht zu überfluten.


**Alternative: Verwendung eines internen Pull-Down-Widerstands**

Der Raspberry Pi Pico 2 W ermöglicht es uns, interne Pull-Down-Widerstände zu aktivieren, was den Bedarf an einem externen Widerstand eliminiert.

* Schaltkreis ändern:

  Entferne den externen 10 kΩ Widerstand und den 0.1 µF Kondensator.

* Modifizierter Code:

  .. code-block:: python

    import machine
    import utime

    # Initialisiere GP14 als Eingang mit internem Pull-Down-Widerstand
    slide_switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

    while True:
        switch_state = slide_switch.value()
        if switch_state == 1:
            print("Switch is toggled to the LEFT!")
        else:
            print("Switch is toggled to the RIGHT!")
        utime.sleep(0.5)
  
**Praktische Anwendungen**

* **Modusauswahl**: Verwende den Schalter, um zwischen verschiedenen Modi in deinem Programm umzuschalten.
* **Stromsteuerung**: Steuere die Stromzufuhr zu bestimmten Teilen deiner Schaltung.
* **Benutzereingabe**: Biete einfache Benutzersteuerungen für deine Projekte.

**Weiteres Experimentieren**

* Füge eine LED-Anzeige hinzu:

  Verbinde eine LED mit einem anderen GPIO-Pin (z. B. GP15) mit einem geeigneten Widerstand. Modifiziere den Code, um die LED ein- oder auszuschalten, basierend auf der Schalterposition.

  .. code-block:: python

    import machine
    import utime

    slide_switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
    led = machine.Pin(15, machine.Pin.OUT)

    while True:
        if slide_switch.value() == 1:
            led.value(1)  # Schalte die LED ein
        else:
            led.value(0)  # Schalte die LED aus
        utime.sleep(0.1)

* Mittelposition erkennen:

  Um zu erkennen, wenn der Schalter in der Mitte ist (weder links noch rechts), musst du die Verdrahtung und den Code ändern, um alle drei Zustände zu lesen.

**Fazit**

Die Verwendung eines Schiebeschalters mit dem Raspberry Pi Pico 2 W ermöglicht es dir, physische Eingabesteuerungen in deine Projekte einzubinden. Durch das Verständnis, wie man den Zustand des Schalters liest und potenzielle Probleme wie Schalterprellen handhabt, kannst du interaktivere und benutzerfreundlichere Anwendungen erstellen.
