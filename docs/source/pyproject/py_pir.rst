.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein zusammen mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Tutorials zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nehmen Sie an Giveaways und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie [|link_sf_facebook|] und treten Sie heute bei!

.. _py_pir:

2.10 Menschliche Bewegungen erkennen
========================================

In dieser Lektion lernen wir, wie man einen Passiv-Infrarot (PIR) Sensor mit dem Raspberry Pi Pico 2 W verwendet, um menschliche Bewegungen zu erkennen. PIR-Sensoren werden häufig in Sicherheitssystemen, automatischer Beleuchtung und anderen Anwendungen eingesetzt, wo Bewegungserkennung erforderlich ist. Sie detektieren die von warmen Objekten wie Menschen oder Tieren ausgehende Infrarotstrahlung in ihrem Sichtfeld.

:ref:`cpn_pir`

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
        - Micro USB Cable
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
        - :ref:`cpn_pir`
        - 1
        - |link_pir_buy|


**Schaltplan**

|sch_pir|

Wenn der PIR-Modul jemanden vorbeigehen erkennt, ist GP14 hoch, ansonsten ist es niedrig.

.. note::

    Der PIR-Sensor hat zwei Potentiometer:

    * **Empfindlichkeitseinstellung**: Regelt den Erfassungsbereich.
    * **Zeitverzögerungseinstellung**: Steuert, wie lange der Ausgang nach der Bewegungserkennung HOCH bleibt.

    Für erste Tests drehen Sie beide Potentiometer gegen den Uhrzeigersinn auf ihre minimale Position. Dies stellt den Sensor auf die empfindlichste und kürzeste Verzögerungseinstellung ein, sodass Sie sofortige Reaktionen beobachten können.

    |img_PIR_TTE|

**Verdrahtung**

|wiring_pir|

**Schreiben des Codes**

Wir werden ein MicroPython-Programm schreiben, das einen Interrupt verwendet, um Bewegungen zu erkennen und eine Nachricht ausgibt, wenn eine Bewegung erkannt wird.

.. note::

    * Öffnen Sie die Datei ``2.10_detect_human_movement.py`` aus ``pico-2w-kit-main/micropython`` oder kopieren Sie den Code in Thonny, dann klicken Sie auf "Run" oder drücken Sie F5.

    * Stellen Sie sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx. 

    

.. code-block:: python

    import machine
    import utime

    # Initialisieren von GP14 als Eingabepin
    pir_sensor = machine.Pin(14, machine.Pin.IN)

    def motion_detected(pin):
        print("Motion detected!")

    # Einrichten eines Interrupts am steigenden Flankenübergang
    pir_sensor.irq(trigger=machine.Pin.IRQ_RISING, handler=motion_detected)

    # Hauptloop macht nichts, Interrupt kümmert sich um Bewegungserkennung
    while True:
        utime.sleep(1)

Wenn der Code läuft, werden Sie folgendes Phänomen beobachten:

* Bewegen Sie sich vor dem PIR-Sensor.
* Wenn eine Bewegung erkannt wird, sollte "Bewegung erkannt!" in der Konsole erscheinen.

**Verständnis des Codes**

#. Import von Modulen:

   * ``import machine``: Zugriff auf Hardwarefunktionen.
   * ``import utime``: Zeitbezogene Funktionen.

#. Initialisierung des PIR-Sensor-Pins:

   * ``pir_sensor = machine.Pin(14, machine.Pin.IN)``: Stellt GP14 als Eingabepin ein.

#. Definition des Interrupt-Handlers:

   * ``def motion_detected(pin)``: Funktion, die aufgerufen wird, wenn eine Bewegung erkannt wird.
   * ``print("Motion detected!")``: Gibt eine Nachricht in der Konsole aus.

#. Einrichten des Interrupts:

   * ``pir_sensor.irq(trigger=machine.Pin.IRQ_RISING, handler=motion_detected)``: Konfiguriert einen Interrupt, der am steigenden Flankenübergang des Signals vom PIR-Sensor ausgelöst wird.

#. Hauptschleife:

   * ``while True``: Eine Endlosschleife.
   * ``utime.sleep(1)``: Die Schleife pausiert in jeder Iteration für 1 Sekunde. Die Hauptschleife selbst muss nichts tun, da die Unterbrechung die Bewegungserkennung übernimmt.

**Beispielcode zur Messung der Dauer**

Der Code kann angepasst werden, um die Dauer der Bewegungserkennung sowie die Intervalle zwischen den Erkennungen zu messen.

.. code-block:: python

    import machine
    import utime

    pir_sensor = machine.Pin(14, machine.Pin.IN)

    last_trigger_time = utime.ticks_ms()

    def pir_triggered(pin):
        global last_trigger_time
        current_time = utime.ticks_ms()
        duration = utime.ticks_diff(current_time, last_trigger_time)
        last_trigger_time = current_time

        if pir_sensor.value():
            print("Motion detected! Duration since last detection: {} ms".format(duration))
        else:
            print("Motion ended. Duration of motion: {} ms".format(duration))

    # Interrupts für steigende und fallende Flanken einrichten
    pir_sensor.irq(trigger=machine.Pin.IRQ_RISING | machine.Pin.IRQ_FALLING, handler=pir_triggered)

    while True:
        utime.sleep(1)

* Interrupts für beide Flanken: Die Unterbrechung wird so eingerichtet, dass sie sowohl bei einer steigenden als auch einer fallenden Flanke mit ``machine.Pin.IRQ_RISING`` | ``machine.Pin.IRQ_FALLING`` ausgelöst wird.
* Zeitverfolgung:

  * Verwende ``utime.ticks_ms()``, um die aktuelle Zeit in Millisekunden zu erfassen.
  * Berechne die Dauer zwischen den Unterbrechungen, um zu messen, wie lange das PIR-Sensorsignal ``HIGH`` oder ``LOW`` bleibt.

**Praktische Anwendungen**

* **Sicherheitssysteme**: Erkennung von Eindringlingen oder unbefugten Bewegungen.
* **Automatische Beleuchtung**: Licht einschalten, wenn eine Bewegung erkannt wird.
* **Energieeinsparung**: Geräte ausschalten, wenn über einen bestimmten Zeitraum keine Bewegung erkannt wird.

**Fehlerbehebungstipps**

* Falsche Auslösungen:

  * PIR-Sensoren können empfindlich auf Umwelteinflüsse wie Temperaturschwankungen oder Sonnenlicht reagieren.
  * Vermeide es, den Sensor direkt auf Wärmequellen oder Fenster auszurichten.

* Sensor erkennt keine Bewegung:

  * Stelle sicher, dass der Sensor genügend Zeit zur Initialisierung hatte (einige Sensoren benötigen bis zu 60 Sekunden).
  * Justiere das Empfindlichkeitspotentiometer.

* Störungen:

  * Halte den Sensor von elektronischen Geräten fern, die elektromagnetische Interferenzen verursachen könnten.

**Fazit**

Durch die Integration eines PIR-Sensors mit dem Raspberry Pi Pico 2 W hast du deinem Projekt eine Bewegungserkennungsfunktion hinzugefügt. Das Verständnis der Sensor-Eingaben und der Umgang mit Interrupts ermöglichen es dir, reaktionsfähige und effiziente Programme zu erstellen.
