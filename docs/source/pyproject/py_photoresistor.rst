.. note:: 

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche mit Gleichgesinnten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum beitreten?**

    - **Expertenunterstützung**: Erhalte Hilfe von unserer Community und unserem Team bei technischen Herausforderungen und Support-Anfragen nach dem Kauf.
    - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um deine Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Profitiere von exklusiven Vergünstigungen auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nimm an Verlosungen und saisonalen Sonderaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _py_photoresistor:

2.12 Licht wahrnehmen
=============================

In dieser Lektion lernen wir, wie man einen **Fotowiderstand** (auch lichtabhängiger Widerstand oder LDR genannt) mit dem Raspberry Pi Pico 2 W verwendet, um die Lichtintensität zu messen. Ein Fotowiderstand verändert seinen Widerstand in Abhängigkeit von der einfallenden Lichtmenge: Je heller das Licht, desto geringer der Widerstand. Dadurch eignet er sich ideal zur Erkennung von Veränderungen im Umgebungslicht.


* :ref:`cpn_photoresistor`

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
        - :ref:`cpn_resistor`
        - 1 (10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_photoresistor`
        - 1
        - |link_photoresistor_buy|


**Schaltplan**

|sch_photoresistor|

In dieser Schaltung sind ein 10KΩ-Widerstand und ein Fotowiderstand in Reihe geschaltet und bilden einen Spannungsteiler. GP28 misst die Spannung über dem Fotowiderstand, während der 10KΩ-Widerstand den Strom begrenzt und somit Schutz bietet.

* **Helles Licht**: Der Widerstand des Fotowiderstands sinkt, wodurch auch die gemessene Spannung und der GP28-Wert fallen. Bei starker Beleuchtung nähert sich der Widerstand nahezu null, sodass GP28 einen Wert nahe 0 ausgibt. In diesem Fall sorgt der 10KΩ-Widerstand dafür, dass 3,3V und GND nicht direkt verbunden werden, um einen Kurzschluss zu vermeiden.
* **Dunkelheit**: Der Widerstand des Fotowiderstands steigt, wodurch die gemessene Spannung und der GP28-Wert zunehmen. In völliger Dunkelheit wird der Widerstand nahezu unendlich groß (der 10KΩ-Widerstand wird vernachlässigbar), sodass GP28 einen Wert nahe 65535 ausgibt.

Die Berechnungsformel lautet:

.. code-block::

  Digital Value = (Analog Voltage/3.3V) * 65535



**Verdrahtung**

|wiring_photoresistor|

**Code schreiben**

Wir schreiben ein MicroPython-Programm, um den analogen Wert des Fotowiderstands zu lesen und auszugeben.

.. note::

  * Öffne die Datei ``2.12_feel_the_light.py`` im Verzeichnis ``pico-2w-kit-main/micropython`` oder kopiere den folgenden Code in Thonny. Klicke dann auf "Run Current Script" oder drücke **F5**, um es auszuführen.
  * Stelle sicher, dass unten rechts in Thonny der Interpreter "MicroPython (Raspberry Pi Pico).COMxx" ausgewählt ist.
  * Ausführliche Anweisungen findest du unter :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    # ADC an GP28 initialisieren
    photoresistor = machine.ADC(28)

    while True:
        # Analogen Wert lesen (0-65535)
        light_value = photoresistor.read_u16()
        print("Light value:", light_value)
        utime.sleep(0.5)

Während das Skript läuft, kannst du die ausgegebenen Werte in der Konsole beobachten.

* Decke den Fotowiderstand mit deiner Hand ab, um Dunkelheit zu simulieren – der Wert sollte steigen.
* Beleuchte den Fotowiderstand mit einer Taschenlampe – der Wert sollte sinken.

**Den Code verstehen**

#. Module importieren:

   * ``machine``: Zugriff auf hardwarebezogene Funktionen.
   * ``utime``: Zeitbezogene Funktionen wie Sleep.

#. ADC-Pin initialisieren:

   * ``photoresistor = machine.ADC(28)``: Setzt GP28 als analogen Eingang zur Spannungsmessung.

#. Hauptschleife:

   ``while True``: Startet eine Endlosschleife.
   ``light_value = photoresistor.read_u16()``: Liest den analogen Wert des Fotowiderstands (0V = 0, 3,3V = 65535).
   ``print("Light value:", light_value)``: Gibt den Lichtwert in der Konsole aus.
   ``utime.sleep(0.5)``: Wartet 0,5 Sekunden, bevor die nächste Messung erfolgt.


**Weitere Experimente**

* Messwerte kalibrieren: 

  Die analogen Werte können in Prozent oder eine andere sinnvolle Skala umgerechnet werden.

  .. code-block:: python
  
      import machine
      import utime
  
      photoresistor = machine.ADC(28)
  
      while True:
          light_value = photoresistor.read_u16()
          light_percentage = (light_value / 65535) * 100
          print("Light level: {:.2f}%".format(light_percentage))
          utime.sleep(0.5)

* Eine LED je nach Lichtintensität steuern: 

  Das Lichtsensor-Signal kann verwendet werden, um eine LED in dunkler Umgebung einzuschalten und bei Helligkeit auszuschalten.

  .. code-block:: python

    import machine
    import utime

    photoresistor = machine.ADC(28)
    led = machine.Pin(15, machine.Pin.OUT)

    while True:
        light_value = photoresistor.read_u16()
        if light_value > 50000:
            led.value(1)  # LED bei Dunkelheit einschalten
        else:
            led.value(0)  # LED bei Helligkeit ausschalten
        utime.sleep(0.5)

* Ein lichtgesteuertes Alarmsystem erstellen: Eine Aktion auslösen, wenn sich die Lichtverhältnisse erheblich ändern.

**Fazit**

Durch die Verwendung eines Fotowiderstands mit dem Raspberry Pi Pico 2 W hast du gelernt, analoge Eingaben zu erfassen und auf Änderungen im Umgebungslicht zu reagieren. Dieses Wissen kann für verschiedene Projekte genutzt werden, z. B. für automatische Beleuchtungssysteme, lichtgesteuerte Roboter oder Sicherheitsgeräte, die auf Helligkeitsänderungen reagieren.


