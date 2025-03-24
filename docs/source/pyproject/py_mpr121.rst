.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein und tausche dich mit anderen Technikbegeisterten aus.

    **Warum beitreten?**

    - **Expertenunterstützung**: Erhalte Hilfe bei technischen Herausforderungen und Fragen nach dem Kauf von unserer Community und unserem Team.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Previews.
    - **Spezielle Rabatte**: Profitiere von exklusiven Vergünstigungen für unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nimm an Verlosungen und saisonalen Promotions teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _py_mpr121:

4.3 Elektroden-Tastatur
================================

In dieser Lektion lernen wir, wie wir den **MPR121 kapazitiven Touchsensor** verwenden, um mit dem Raspberry Pi Pico 2 W eine berührungsempfindliche Tastatur zu erstellen. Der MPR121 ermöglicht die Erkennung von Berührungen an bis zu 12 Elektroden, die mit leitfähigen Materialien wie Drähten, Folie oder sogar Früchten wie Bananen verbunden werden können!

* :ref:`cpn_mpr121`

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
        - :ref:`cpn_mpr121`
        - 1
        - 

**Den MPR121-Sensor verstehen**

Der **MPR121** ist ein kapazitiver Touchsensor-Controller, der über die I2C-Schnittstelle kommuniziert. Er kann bis zu 12 Berührungseingaben erkennen und eignet sich ideal für interaktive Projekte mit mehreren Berührungspunkten.

Der MPR121 erkennt Änderungen in der Kapazität seiner Elektroden. Wenn du eine Elektrode berührst, ändert sich die Kapazität, und der Sensor registriert die Berührung. Diese Information wird dann über I2C an den Raspberry Pi Pico 2 W übermittelt.

**Schaltplan**

|sch_mpr121_ar|

**Verkabelung**

|wiring_mpr121_ar|

* Verbinde Drähte oder leitfähige Materialien mit den Elektroden-Pins (bezeichnet als **E0** bis **E11**) des MPR121.
* Die anderen Enden der Drähte können mit leitfähigen Objekten wie Früchten, Aluminiumfolienformen oder Touchpads verbunden werden.

**Schaltplan für die Verkabelung**

* Verbinde Drähte oder leitfähige Materialien mit den Elektroden-Pins (bezeichnet als **E0** bis **E11**) des MPR121.
* Die anderen Enden der Drähte können mit leitfähigen Objekten wie Früchten, Aluminiumfolienformen oder Touchpads verbunden werden.

**Code schreiben**

Wir schreiben ein MicroPython-Programm, um Berührungseingaben auf den Elektroden zu erkennen und anzuzeigen, welche berührt werden.

.. note::

    * Öffne die Datei ``4.3_electrode_keyboard.py`` aus ``pico-2w-kit-main/micropython`` oder kopiere den Code in Thonny, klicke auf "Run" oder drücke F5.
    * Stelle sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx.
    * Du benötigst die Bibliothek ``mpr121.py`` – überprüfe, ob sie auf den Pico hochgeladen wurde. Eine detaillierte Anleitung findest du unter :ref:`add_libraries_py`.

.. code-block:: python
    
    from mpr121 import MPR121
    from machine import Pin, I2C
    import utime

    i2c = I2C(0, sda=Pin(4), scl=Pin(5))
    mpr = MPR121(i2c)

    # Alle Tasten prüfen
    while True:
        value = mpr.get_all_states()
        if len(value) != 0:
            print(value)
        utime.sleep_ms(100)

Nachdem das Programm ausgeführt wurde, berühre die verbundenen Elektroden oder leitfähigen Objekte. Im Thonny-Shell-Fenster wird angezeigt, welche Elektroden berührt werden.

**Den Code verstehen**

#. Module importieren:

   * ``machine``: Stellt Funktionen für die Hardware-Interaktion bereit.
   * ``mpr121``: Bibliothek zur Ansteuerung des MPR121-Sensors.
   * ``utime``: Enthält zeitbezogene Funktionen für Verzögerungen.

#. I2C-Kommunikation initialisieren:


   * ``i2c = I2C(0, sda=Pin(4), scl=Pin(5))``: Richtet die I2C-Kommunikation über Bus 0 mit GP4 (SDA) und GP5 (SCL) ein.

#. Ein MPR121-Objekt erstellen:

   * ``mpr = MPR121(i2c)``: Initialisiert den MPR121-Sensor über die eingerichtete I2C-Kommunikation.

#. Hauptschleife zur Berührungserkennung:

   * ``get_all_states()``: Gibt eine Liste der aktuell berührten Elektroden zurück.
   * Falls Elektroden berührt werden, werden deren Nummern ausgegeben.
   * Die Schleife läuft kontinuierlich mit einer kurzen Verzögerung von 100 Millisekunden.

   .. code-block:: python

        while True:
            value = mpr.get_all_states()
            if len(value) != 0:
                print(value)
            time.sleep_ms(100)

**Erweiterung der Elektroden**

Du kannst dein Projekt verbessern, indem du die Elektroden mit verschiedenen leitfähigen Materialien verbindest:

* **Früchte**: Verbinde Drähte mit Bananen, Äpfeln oder anderen Früchten, um sie in berührungsempfindliche Eingaben zu verwandeln.
* **Folienformen**: Schneide Formen aus Aluminiumfolie aus und verbinde sie mit den Elektroden.
* **Leitfähige Farbe**: Zeichne Muster mit leitfähiger Tinte oder Farbe.

.. note::
    
    Falls du die Elektroden änderst (z. B. unterschiedliche Materialien anschließt), solltest du den Sensor zurücksetzen, um die Grundwerte neu zu kalibrieren.

**Weitere Experimente**

* Bestimmte Elektrode erkennen:

  Wenn du eine bestimmte Elektrode überwachen möchtest, kannst du die Methode ``is_touched(pin)`` verwenden. Sie gibt True zurück, wenn die angegebene Elektrode berührt wird, andernfalls False.

  .. code-block:: python
  
        from mpr121 import MPR121
        from machine import Pin, I2C
        import utime

        i2c = I2C(0, sda=Pin(4), scl=Pin(5))
        mpr = MPR121(i2c)

        # Alle Tasten prüfen
        while True:
          if mpr.is_touched(0):
              print("Electrode 0 is touched!")
          utime.sleep(0.1)

* **Musikinstrument erstellen**: Weise jeder Elektrode eine Note zu und spiele Töne bei Berührung.
* **Interaktive Kunst**: Erstelle berührungssensitive Kunstwerke mit leitfähiger Farbe.
* **Spielsteuerung**: Entwickle individuelle Touch-Steuerelemente für ein Spiel.

**Fazit**

In dieser Lektion hast du gelernt, wie du den MPR121 kapazitiven Touchsensor mit dem Raspberry Pi Pico 2 W verwendest, um eine berührungsempfindliche Elektroden-Tastatur zu erstellen. Dies eröffnet vielfältige Möglichkeiten für interaktive Projekte, die auf Berührung reagieren.
