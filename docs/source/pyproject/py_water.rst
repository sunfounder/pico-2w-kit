.. note::
    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Vertiefe dich mit Gleichgesinnten in die Welt von Raspberry Pi, Arduino und ESP32.

    **Warum beitreten?**

    - **Expertenunterstützung**: Löse Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Tutorials, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Promotionen und Gewinnspiele**: Nimm an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt heute bei!

.. _py_water:

2.14 Den Wasserstand fühlen
=====================================

In dieser Lektion lernen wir, wie man einen **Wassersensor** mit dem Raspberry Pi Pico 2 W verwendet, um das Vorhandensein von Wasser oder den Wasserstand zu erkennen. Dieser Sensor wird häufig in Projekten zur Regenfallerkennung, Wasserstandsüberwachung und Leckagealarmierung eingesetzt.

**Funktionsweise des Wassersensors**

Der Wassersensor verfügt über eine Reihe von freiliegenden parallelen Drahtspuren, die Wassertropfen erkennen oder das Wasservolumen messen. Wenn Wasser mit diesen Spuren in Kontakt kommt, gibt der Sensor ein analoges Signal aus. Je mehr Wasser mit dem Sensor in Kontakt kommt, desto höher ist der Ausgabewert, der vom Analog-Digital-Umsetzer (ADC) des Raspberry Pi Pico 2 W gelesen werden kann.

|img_water_sensor|

* Tauche den Sensor nicht vollständig ins Wasser. Nur der Bereich mit den freiliegenden Spuren sollte mit Wasser in Kontakt kommen.
* Die Verwendung des Sensors in einer feuchten Umgebung bei eingeschaltetem Zustand kann zu einer schnelleren Korrosion der Sonde führen, daher wird empfohlen, den Sensor nur zum Ablesen einzuschalten.

* :ref:`cpn_water_level`

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
        - :ref:`cpn_water_level`
        - 1
        - 



**Schaltplan**

|sch_water|


**Verdrahtung**


|wiring_water|

**Schreiben des Codes**

Wir werden ein einfaches MicroPython-Programm schreiben, um den Analogwert vom Wassersensor zu lesen und ihn auf die Konsole zu drucken. Wenn der Wassersensor eingetaucht wird, erhöht sich der vom GP28 gelesene Wert.

.. note::

    * Öffne die Datei ``2.14_feel_the_water_level.py`` aus ``pico-2w-kit-main/micropython`` oder kopiere den Code in Thonny, dann klicke auf "Ausführen" oder drücke F5.
    * Stelle sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx.

.. code-block:: python

    import machine
    import utime

    # Initialisiere ADC an GP28
    sensor = machine.ADC(28)

    while True:
        # Lese den Analogwert vom Sensor
        value = sensor.read_u16()
        print("Water level reading:", value)
        utime.sleep(0.2)  # Verzögerung, um die Konsole nicht mit Daten zu überfluten


Wenn der Code läuft, tauche den Wassersensor langsam ins Wasser, während du die Werte beobachtest, die auf der Konsole ausgegeben werden. Wenn der Sensor mehr Wasser erkennt, erhöht sich der ausgegebene Wert.

**Mehr erfahren: Einsatz des Sensors zur Leckageerkennung**

Wir können den Wassersensor auch zur Erkennung von Flüssigkeitsleckagen verwenden, indem wir ihn wie einen digitalen Sensor behandeln. So geht's:

#. Baseline-Wert messen:

   * Zuerst nimm eine Messung vom Wassersensor in einer völlig trockenen Umgebung vor. Verwende diesen Wert als Schwellenwert.
   * Wenn der Messwert des Sensors über diesen Baseline-Schwellenwert steigt, können wir davon ausgehen, dass der Sensor mit Wasser in Kontakt kommt, was auf eine mögliche Leckage hinweist.

#. Code zur Leckageerkennung:

   In diesem Beispiel überprüfen wir, ob der Messwert des Sensors den Schwellenwert übersteigt (den du basierend auf deiner Umgebung festlegen musst).

   .. code-block:: python

      import machine
      import utime
  
      # Initialisiere ADC an GP28
      sensor = machine.ADC(28)
  
      # Setze einen Schwellenwert basierend auf trockenen Messungen (nach Bedarf anpassen)
      threshold = 30000
  
      while True:
          # Lese den Analogwert vom Sensor
          value = sensor.read_u16()
          
          # Prüfe, ob der Wert den Schwellenwert übersteigt, was auf Wasserkontakt hinweist
          if value > threshold:
              print("Liquid leakage detected!")
          
          utime.sleep(0.2)  # Verzögerung für bessere Lesbarkeit


   Das Programm überprüft, ob der Wert des Sensors einen vordefinierten Schwellenwert übersteigt. Wenn der Wert höher ist, wird eine Meldung ausgegeben, die auf Wasser- oder Flüssigkeitsleckagen hinweist.

**Praktische Anwendungen**

* **Leckageerkennung**: Platziere den Sensor in der Nähe von Wasserleitungen, und er kann dich alarmieren, wenn eine Leitung undicht wird.
* **Wasserstandsüberwachung**: Verwende den Sensor in Tanks oder Behältern, um den Wasserstand zu überwachen und Alarme oder Aktionen auszulösen.
* **Regenerkennung**: Installiere den Sensor im Freien (mit entsprechendem Schutz), um Regenfall zu erkennen.

**Fazit**

Der Wassersensor ist ein einfaches, aber mächtiges Werkzeug zur Erkennung von Wasserständen oder potenziellen Flüssigkeitsleckagen. Durch die Integration mit dem Raspberry Pi Pico 2 W kannst du reaktionsschnelle und nützliche Wasserdetektionssysteme für eine Vielzahl von Anwendungen erstellen.
