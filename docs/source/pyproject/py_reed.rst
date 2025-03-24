.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein zusammen mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Tutorials zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nehmen Sie an Giveaways und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie [|link_sf_facebook|] und treten Sie heute bei!

.. _py_reed:

2.9 Spüren Sie den Magnetismus
================================

In dieser Lektion werden wir untersuchen, wie man einen **Reedschalter** mit dem Raspberry Pi Pico 2 W verwendet, um die Anwesenheit eines Magnetfelds zu erkennen. Ein Reedschalter ist ein einfacher elektrischer Schalter, der mit einem Magnetfeld betrieben wird. Wenn sich ein Magnet dem Schalter nähert, schließen sich seine internen Kontakte und schließen den elektrischen Kreislauf.
* :ref:`cpn_reed`

**Erforderliche Komponenten**

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


Sie können sie auch einzeln über die untenstehenden Links kaufen.


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
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_reed`
        - 1
        - 

**Verständnis des Reedschalters**

Ein Reedschalter besteht aus zwei dünnen Metallzungen, die in einer Glasampulle eingeschlossen sind. Diese Zungen bestehen aus ferromagnetischem Material und sind leicht voneinander getrennt. In Abwesenheit eines Magnetfelds sind die Zungen getrennt und der Schalter ist **offen**. Wenn sich ein Magnet dem Schalter nähert, werden die Zungen magnetisiert, ziehen sich gegenseitig an und schließen den Stromkreis.

* **Kein Magnet in der Nähe**: Schalter ist **offen**; der Stromkreis ist unvollständig.
* **Magnet in der Nähe**: Schalter ist **geschlossen**; der Stromkreis ist vollständig.

|img_reed_sche|

**Schaltplan**

|sch_reed|

Standardmäßig ist GP14 niedrig; und wird hoch, wenn der Magnet in der Nähe des Reedschalters ist.

Der Zweck des 10K-Widerstands besteht darin, den GP14 auf einem stabilen niedrigen Niveau zu halten, wenn kein Magnet in der Nähe ist.

* **Kein Magnet in der Nähe**:

  * Der Reedschalter ist **offen**.
  * **GP14** ist über den Pull-down-Widerstand mit **GND** verbunden.
  * Der GPIO-Pin liest **LOW** (0).

* **Magnet in der Nähe**:

  * Der Reedschalter ist **geschlossen**.
  * **GP14** ist über den Reedschalter mit **3.3V** verbunden.
  * Der GPIO-Pin liest **HIGH** (1).

**Verdrahtung**

|wiring_reed|

**Schreiben des Codes**

Wir werden ein MicroPython-Programm schreiben, das erkennt, wann ein Magnet in der Nähe des Reedschalters ist und entsprechend eine Nachricht ausgibt.

.. note::

  * Öffnen Sie die Datei ``2.9_feel_the_magnetism.py`` aus ``pico-2w-kit-main/micropython`` oder kopieren Sie den Code in Thonny und klicken Sie auf „Run“ oder drücken Sie F5.
  * Stellen Sie sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx. 

.. code-block:: python

    import machine
    import utime

    # Initialisieren von GP14 als Eingabepin
    reed_switch = machine.Pin(14, machine.Pin.IN)

    while True:
        if reed_switch.value() == 1:
            print("Magnet detected!")
            utime.sleep(1)  # Verzögerung, um mehrfache Erkennungen zu vermeiden

Wenn der Code läuft, werden Sie folgendes Phänomen beobachten:

* **Kein Magnet in der Nähe**: Es sollte keine Nachricht erscheinen.
* **Bringen Sie einen Magnet in die Nähe**: "Magnet erkannt!" sollte in der Konsole erscheinen.
* **Entfernen Sie den Magnet**: Die Nachricht hört auf zu erscheinen.

**Verständnis des Codes**

#. Import von Modulen:

   * ``import machine``: Zugriff auf Hardwarefunktionen.
   * ``import utime``: Zeitbezogene Funktionen.

#. Initialisierung des Reedschalter-Pins:

   * ``reed_switch = machine.Pin(14, machine.Pin.IN)``: Stellt GP14 als Eingabepin ein.

#. Hauptloop:

   * ``while True``: Startet eine unendliche Schleife.
   * ``if reed_switch.value() == 1``: Überprüft, ob ein Magnet in der Nähe ist (GPIO-Pin liest HIGH).
   * ``print("Magnet detected!")``: Gibt eine Nachricht aus.
   * ``utime.sleep(1)``: Fügt eine Verzögerung hinzu, um schnelle wiederholte Nachrichten zu verhindern.

**Verwendung von Interrupts für effiziente Erkennung**

Anstelle des ständigen Pollings des Reedschalters in einer Schleife können wir einen Interrupt verwenden, um Änderungen im Zustand des Reedschalters effizienter zu erkennen.

Die Verwendung von Interrupts steigert die Effizienz, indem sie die Notwendigkeit des kontinuierlichen Überprüfens des Reedschalterzustands beseitigt und die Reaktionsfähigkeit verbessert, indem sofort die Handlerfunktion aufgerufen wird, wenn das Ereignis eintritt.

Modifizierter Code unter Verwendung von Interrupts. Wenn Sie einen Magnet in die Nähe des Reedschalters bringen, erscheint "Magnet erkannt!". Das Hauptprogramm bleibt frei, um andere Aufgaben zu erfüllen.

.. code-block:: python

    import machine

    # Initialisieren von GP14 als Eingabepin mit internem Pull-down-Widerstand
    reed_switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

    def magnet_detected(pin):
        print("Magnet detected!")

    # Einrichten eines Interrupts am steigenden Flankenübergang (Übergang von LOW zu HIGH)
    reed_switch.irq(trigger=machine.Pin.IRQ_RISING, handler=magnet_detected)

* ``def magnet_detected(pin)``: Diese Funktion wird automatisch aufgerufen, wenn der Interrupt ausgelöst wird.
    
  * ``print("Magnet detected!")``: Gibt eine Nachricht aus, wenn ein Magnet erkannt wird.

* ``reed_switch.irq(trigger=machine.Pin.IRQ_RISING, handler=magnet_detected)``: Konfiguriert einen Interrupt am Reedschalter-Pin.
     
  * ``trigger=machine.Pin.IRQ_RISING``: Der Interrupt wird an einer steigenden Flanke ausgelöst (wenn der Pinwert von LOW zu HIGH geht).
  * ``handler=magnet_detected``: Gibt die Funktion an, die aufgerufen wird, wenn der Interrupt auftritt.

**Praktische Anwendungen**

* **Sicherheitssysteme**: Erkennt, wenn eine Tür oder ein Fenster geöffnet wird.
* **Positionserkennung**: Bestimmt die Position von beweglichen Teilen in Maschinen.
* **Näherungserkennung**: Löst Ereignisse aus, wenn sich ein magnetisches Objekt nähert.

**Weiterführende Experimente**

* Steuern einer LED:

  Verbinden Sie eine LED mit einem anderen GPIO-Pin (z.B. GP15) mit einem geeigneten Widerstand. Modifizieren Sie den Interrupt-Handler, um die LED einzuschalten, wenn ein Magnet erkannt wird.
  
  .. code-block:: python
  
      import machine
  
      reed_switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
      led = machine.Pin(15, machine.Pin.OUT)
  
      def magnet_detected(pin):
          led.value(1)  # Schaltet die LED ein
  
      # Einrichten eines Interrupts an der steigenden Flanke
      reed_switch.irq(trigger=machine.Pin.IRQ_RISING, handler=magnet_detected)
  
      # Hauptloop
      while True:
          # Schaltet die LED aus, wenn kein Magnet vorhanden ist
          if reed_switch.value() == 0:
              led.value(0)
          machine.sleep(100)
        
* Erkennen der Magnetentfernung:

  Richten Sie einen weiteren Interrupt für die fallende Flanke ein (wenn der Magnet entfernt wird).

  .. code-block:: python

    def magnet_removed(pin):
        print("Magnet removed!")

    reed_switch.irq(trigger=machine.Pin.IRQ_FALLING, handler=magnet_removed)

**Schlussfolgerung**

Durch die Verwendung eines Reedschalters mit dem Raspberry Pi Pico 2 W können Sie die Anwesenheit eines Magnetfelds erkennen, was eine breite Palette von Anwendungen von Sicherheitssystemen bis zu interaktiven Projekten ermöglicht. Das Verständnis, wie man den Reedschalter verdrahtet und Interrupts nutzt, verbessert Ihre Fähigkeit, effiziente und reaktionsfähige Programme zu erstellen.

**Referenzen**

* |link_mpython_irq|