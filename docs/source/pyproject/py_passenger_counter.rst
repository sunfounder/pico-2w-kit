.. note:: 

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche mit Gleichgesinnten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum beitreten?**

    - **Expertenunterstützung**: Erhalte Hilfe von unserer Community und unserem Team bei technischen Herausforderungen und Support-Anfragen nach dem Kauf.
    - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um deine Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Profitiere von exklusiven Vergünstigungen auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nimm an Verlosungen und saisonalen Sonderaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _py_passage_counter:


7.4 Bau eines Passagierzählers
=======================================================

In dieser Lektion erstellen wir einen **Passagierzähler** mit einem Raspberry Pi Pico 2 W, einem PIR-Bewegungssensor (Passive Infrared) und einem 4-stelligen 7-Segment-Display. Dieses Gerät zählt die Anzahl der vom PIR-Sensor erkannten Bewegungen und zeigt die Gesamtzahl auf dem Display an. Es simuliert die Funktionsweise von Zählern, die in öffentlichen Bereichen zur Überwachung des Fußgängerverkehrs verwendet werden.


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
        - 4 (220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_4_dit_7_segment`
        - 1
        - 
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|
    *   - 8
        - :ref:`cpn_pir`
        - 1
        - |link_pir_buy|

**Funktionsweise der Komponenten**

* **PIR-Bewegungssensor**: Erkennt Bewegungen durch Messung der Infrarotstrahlung (IR) von Objekten in seinem Sichtfeld. Sobald Bewegung erkannt wird, gibt er ein HIGH-Signal aus.
* **4-stelliges 7-Segment-Display**: Ermöglicht die Anzeige von Zahlen zwischen 0000 und 9999. Mithilfe eines Schieberegisters steuern wir das Display mit weniger GPIO-Pins.
* **74HC595 Schieberegister**: Ein 8-Bit-Schieberegister mit serieller Eingabe und paralleler Ausgabe. Es ermöglicht die Steuerung mehrerer Ausgänge mit wenigen GPIO-Pins.

**Schaltplan**

|sch_passager_counter| 

* Diese Schaltung basiert auf der :ref:`py_74hc_4dig` mit der Ergänzung eines PIR-Moduls.
* Der PIR-Sensor gibt bei erkannter Bewegung ein ca. 2,8 Sekunden langes HIGH-Signal aus.
* Das PIR-Modul verfügt über zwei Potentiometer: eines zur Einstellung der Empfindlichkeit, das andere zur Anpassung der Erkennungsreichweite. Um die beste Leistung zu erzielen, sollten beide Potentiometer gegen den Uhrzeigersinn bis zum Anschlag gedreht werden.

    |img_PIR_TTE|


**Verdrahtung**


|wiring_passager_counter|

**Code schreiben**

Unser MicroPython-Skript wird:

* Bewegungen mit dem PIR-Sensor erkennen.
* Bei jeder Bewegung den Zähler um eins erhöhen.
* Die aktuelle Zählung auf dem 4-stelligen 7-Segment-Display anzeigen.
* Multiplexing-Techniken verwenden, um das Display effizient zu steuern.

.. note::

    * Öffne die Datei ``7.4_passager_counter.py`` im Verzeichnis ``pico-2w-kit-main/micropython`` oder kopiere den folgenden Code in Thonny. Klicke dann auf "Run" oder drücke **F5**, um es auszuführen.
    * Stelle sicher, dass unten rechts in Thonny der Interpreter "MicroPython (Raspberry Pi Pico).COMxx" ausgewählt ist.

.. code-block:: python

    from machine import Pin
    import utime

    # PIR-Sensor-Pin definieren
    pir_sensor = Pin(16, Pin.IN)

    # Zähler initialisieren
    count = 0

    # Binärcodes für die Anzeige der Ziffern 0-9
    SEGMENT_CODES = [
        0x3F,  # 0
        0x06,  # 1
        0x5B,  # 2
        0x4F,  # 3
        0x66,  # 4
        0x6D,  # 5
        0x7D,  # 6
        0x07,  # 7
        0x7F,  # 8
        0x6F   # 9
    ]

    # Initialisierung der Steuerpins für 74HC595
    SDI = machine.Pin(18, machine.Pin.OUT)   # Serielle Dateneingabe (DS)
    RCLK = machine.Pin(19, machine.Pin.OUT)  # Register-Takt (STCP)
    SRCLK = machine.Pin(20, machine.Pin.OUT) # Schieberegister-Takt (SHCP)

    # Initialisierung der Digit-Auswahlpins (gemeinsame Kathoden)
    digit_pins = [
        machine.Pin(10, machine.Pin.OUT),  # Ziffer 1
        machine.Pin(11, machine.Pin.OUT),  # Ziffer 2
        machine.Pin(12, machine.Pin.OUT),  # Ziffer 3
        machine.Pin(13, machine.Pin.OUT)   # Ziffer 4
    ]

    # Funktion zum Senden von Daten an 74HC595
    def shift_out(data):
        RCLK.low()
        for bit in range(7, -1, -1):
            SRCLK.low()
            bit_val = (data >> bit) & 0x01
            SDI.value(bit_val)
            SRCLK.high()
        RCLK.high()

    # Funktion zur Anzeige einer Ziffer an einer bestimmten Position
    def display_digit(position, digit):
        # Alle Ziffern deaktivieren
        for dp in digit_pins:
            dp.high()
        # Segmentdaten senden
        shift_out(SEGMENT_CODES[digit])
        # Aktivieren der ausgewählten Ziffer (gemeinsame Kathode ist aktiv niedrig)
        digit_pins[position].low()
        # Kleine Verzögerung für die Sichtbarkeit der Ziffer
        utime.sleep_ms(5)
        # Ziffer deaktivieren
        digit_pins[position].high()

    # Funktion zur Anzeige einer Zahl auf dem 4-stelligen Display
    def display_number(number):
        # Einzelne Ziffern extrahieren
        digits = [
            (number // 1000) % 10,
            (number // 100) % 10,
            (number // 10) % 10,
            number % 10
        ]
        # Jede Ziffer schnell nacheinander anzeigen
        for i in range(4):
            display_digit(i, digits[i])

    # Interrupt-Handler für den PIR-Sensor
    def pir_handler(pin):
        global count
        count += 1
        if count > 9999:
            count = 0

    # PIR-Sensor-Interrupt einrichten
    pir_sensor.irq(trigger=Pin.IRQ_RISING, handler=pir_handler)

    # Hauptschleife
    while True:
        # Anzeige kontinuierlich aktualisieren
        display_number(count)

Wenn das Skript läuft, sollte das 7-Segment-Display initialisiert werden und "0000" anzeigen.
Bewege dich vor dem PIR-Sensor.
Die angezeigte Zahl sollte sich jedes Mal um eins erhöhen, wenn eine Bewegung erkannt wird.
Erreicht der Zähler 9999, wird er auf 0000 zurückgesetzt.

**Den Code verstehen**

#. Importe und Pin-Definitionen:

   * ``machine.Pin``: Zur Steuerung der GPIO-Pins.
   * ``utime``: Für Zeitfunktionen.
   * Definition der Steuerpins SDI, SRCLK und RCLK für das Schieberegister.
   * Definition von ``pir_sensor`` auf GP16 als Eingangspin für den PIR-Sensor.

#. Segment-Codes:

   * ``SEGMENT_CODES``: Eine Liste mit den Binärcodes für die Anzeige der Ziffern 0-9 auf einem 7-Segment-Display. Jeder Bytewert bestimmt, welche Segmente leuchten.

   .. code-block:: python

        # 7-Segment-Display Codes für die Ziffern 0-9 (gemeinsame Kathode)
        SEGMENT_CODES = [
            0x3F,  # 0
            0x06,  # 1
            0x5B,  # 2
            0x4F,  # 3
            0x66,  # 4
            0x6D,  # 5
            0x7D,  # 6
            0x07,  # 7
            0x7F,  # 8
            0x6F   # 9
        ]

#. Zähler-Initialisierung:

   * ``count``: Eine globale Variable zur Erfassung der erkannten Bewegungen.

#. Die Funktion ``shift_out`` definieren:

   * Sendet 8 Bit Daten an das 74HC595-Schieberegister.
   * Beginnt mit dem höchstwertigen Bit (MSB).
   * Pulsiert die Schiebe- und Registertaktsignale korrekt.

   .. code-block:: python

        def shift_out(data):
            RCLK.low()
            for bit in range(7, -1, -1):
                SRCLK.low()
                bit_val = (data >> bit) & 0x01
                SDI.value(bit_val)
                SRCLK.high()
            RCLK.high()

#. Die Funktion ``display_digit`` definieren:

   * Deaktiviert alle Ziffern.
   * Sendet die Segmentdaten der gewünschten Ziffer.
   * Aktiviert die gewählte Ziffer, indem ihr Pin auf LOW gesetzt wird.
   * Fügt eine kurze Verzögerung hinzu, um die Ziffer sichtbar zu machen.
   * Deaktiviert die Ziffer danach wieder.

   .. code-block:: python

        def display_digit(position, digit):
            for dp in digit_pins:
                dp.high()
            shift_out(SEGMENT_CODES[digit])
            digit_pins[position].low()
            utime.sleep_ms(5)
            digit_pins[position].high()

#. Die Funktion ``display_number`` definieren:

   * Extrahiert die einzelnen Ziffern einer Zahl.
   * Ruft ``display_digit`` für jede Ziffer schnell auf, um den Multiplexing-Effekt zu erzeugen.

   .. code-block:: python

        def display_number(number):
            # Einzelne Ziffern extrahieren
            digits = [
                (number // 1000) % 10,
                (number // 100) % 10,
                (number // 10) % 10,
                number % 10
            ]
            # Jede Ziffer schnell nacheinander anzeigen
            for i in range(4):
                display_digit(i, digits[i])

#. PIR-Interrupt-Handler:

   * ``pir_handler``: Diese Funktion wird automatisch aufgerufen, wenn der PIR-Sensor eine Bewegung erkennt.
   * Erhöht die count-Variable.
   * Setzt count auf 0 zurück, falls der Wert 9999 überschreitet.

   .. code-block:: python

        def pir_handler(pin):
            global count
            count += 1
            if count > 9999:
                count = 0

#. PIR-Sensor-Interrupt einrichten:

   ``pir_sensor.irq``: Legt eine Unterbrechung fest, um ``pir_handler`` bei einem steigenden Signal vom PIR-Sensor auszulösen.

   .. code-block:: python

        pir_sensor.irq(trigger=Pin.IRQ_RISING, handler=pir_handler)

#. Hauptschleife:

   Ruft kontinuierlich ``display_number(count)`` auf, um das Display mit der aktuellen Zählung zu aktualisieren.

   .. code-block:: python

        while True:
            display_number(count)

**Fehlersuche**

* Anzeigeprobleme:

  * Falls die Anzeige falsche Zahlen zeigt, überprüfe die Segmentcodes und die Verdrahtung.
  * Stelle sicher, dass das Schieberegister korrekt angeschlossen ist und Daten richtig ausgegeben werden.

* Empfindlichkeit des PIR-Sensors:

  * Der PIR-Sensor kann mit Potentiometern für Empfindlichkeit und Verzögerung eingestellt werden.
  * Justiere diese Parameter, um die Bewegungserkennung zu optimieren.
  * Beachte, dass der PIR-Sensor eine kurze Verzögerung nach der Bewegungserkennung haben kann.

* Genauigkeit der Zählung:

  * In Umgebungen mit viel Bewegung kann der Zähler schnell hochzählen.
  * Erwäge eine Entprellung des PIR-Sensors oder begrenze die Zählfrequenz.

**Erweiterungen und Verbesserungen**

* Reset-Taste: 

    Eine zusätzliche Taste hinzufügen, um den Zähler manuell auf 0 zu setzen.

* Bidirektionale Zählung: 

    Zwei PIR-Sensoren zur Erkennung der Bewegungsrichtung (Eintritt/Austritt) nutzen.

* Datenprotokollierung:

    Speichere die Daten lokal oder sende sie an einen Server für Analysen.

* LCD-Anzeige: 
    
    Ersetze das 7-Segment-Display durch ein LCD für mehr Informationen.

* Netzwerkanbindung: 
    
    Daten über WLAN an eine Cloud oder ein Dashboard senden.

**Fazit**

Dieses Projekt zeigt, wie man einen Passagierzähler mit dem Raspberry Pi Pico 2 W, 
einem PIR-Sensor und einem 7-Segment-Display realisiert. Du kannst es als Grundlage für weiterführende Anwendungen nutzen.
