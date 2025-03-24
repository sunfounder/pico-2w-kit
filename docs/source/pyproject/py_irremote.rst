.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein – gemeinsam mit anderen Technikbegeisterten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Erhalte Hilfe bei technischen Problemen und Fragen nach dem Kauf durch unsere Community und unser Team.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und Vorschauen.
    - **Spezielle Rabatte**: Profitiere von exklusiven Vergünstigungen auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nimm an Verlosungen und Sonderaktionen zu Feiertagen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _py_irremote:


6.4 Verwendung einer Infrarot-Fernbedienung
==========================================================

In dieser Lektion lernen wir, wie man eine **Infrarot-(IR)-Fernbedienung** und ein **IR-Empfängermodul** mit dem Raspberry Pi Pico 2 W verwendet. Damit können wir Signale von einer IR-Fernbedienung empfangen und dekodieren, um unsere Projekte drahtlos zu steuern.

* :ref:`cpn_ir_receiver`

**Benötigte Komponenten**

Für dieses Projekt benötigen wir folgende Komponenten.

Es ist besonders praktisch, ein komplettes Kit zu erwerben. Hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ENTHALTENE TEILE IM KIT
        - LINK
    *   - Pico 2 W Starter Kit	
        - 450+
        - |link_pico2w_kit|

Die Komponenten können auch einzeln über die folgenden Links erworben werden.


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
        - :ref:`cpn_ir_receiver`
        - 1
        - |link_receiver_buy|

**Grundlagen der Infrarot-Kommunikation**

Die Infrarot-Kommunikation ermöglicht die drahtlose Übertragung von Daten mittels Infrarotlicht. Geräte wie Fernseher oder DVD-Player nutzen IR-Fernbedienungen zur Steuerung.

* **IR-Sender (Fernbedienung):** Sendet moduliertes Infrarotlicht aus, wenn eine Taste gedrückt wird.
* **IR-Empfängermodul:** Erkennt das modulierte IR-Licht und wandelt es in elektrische Signale um, die dekodiert werden können.

**Schaltplan**

|sch_irrecv|

**Verdrahtung**

|wiring_irrecv|


**Code schreiben**


Nun schreiben wir ein MicroPython-Skript, um IR-Signale von der Fernbedienung zu empfangen und zu dekodieren.

.. note::

    * Öffne die Datei ``6.4_ir_remote_control.py`` aus ``pico-2w-kit-main/micropython`` oder kopiere den Code in Thonny, dann klicke auf "Run" oder drücke F5.
    * Stelle sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx.
    * Die benötigten Bibliotheken befinden sich im ``ir_rx``-Ordner. Überprüfe, ob sie auf den Pico hochgeladen wurden. Eine detaillierte Anleitung findest du unter :ref:`add_libraries_py`.

.. code-block:: python

    import time
    from machine import Pin
    from ir_rx.nec import NEC_8  # Anpassung je nach Protokoll der Fernbedienung
    from ir_rx.print_error import print_error

    # Initialisierung des IR-Empfänger-Pins
    ir_pin = Pin(17, Pin.IN)

    # Callback-Funktion zur Verarbeitung empfangener Daten
    def ir_callback(data, addr, ctrl):
        if data < 0:  # Wiederholungscode oder Fehler
            pass
        else:
            key = decode_key(data)
            print("Received Key:", key)

    # Funktion zur Dekodierung der empfangenen Daten
    def decode_key(data):
        key_codes = {
            0x45: "POWER",
            0x46: "MODE",
            0x47: "MUTE",
            0x44: "PLAY/PAUSE",
            0x40: "BACKWARD",
            0x43: "FORWARD",
            0x07: "EQ",
            0x15: "-",
            0x09: "+",
            0xD: "U/SD",
            0x16: "0",
            0x19: "cycle",
            0xC: "1",
            0x5E: "3",
            0x18: "2",
            0x8: "4",
            0x1C: "5",
            0x5A: "6",
            0x42: "7",
            0x52: "8",
            0x4A: "9",
            0x0: "ERROR",
            # Weitere Codes je nach Fernbedienung hinzufügen
        }
        return key_codes.get(data, "UNKNOWN")

    # Initialisierung des IR-Empfängers
    ir = NEC_8(ir_pin, ir_callback)
    ir.error_function(print_error)  # Optional: Fehler ausgeben

    try:
        while True:
            time.sleep(1)  # Hauptprogramm am Leben halten
    except KeyboardInterrupt:
        ir.close()
        print("Program terminated")

Beim Ausführen dieses Codes und Drücken einer Taste auf der Infrarot-Fernbedienung wird in der Thonny-Shell (oder einem anderen seriellen Monitor) die entsprechende Tastenbezeichnung angezeigt. Drückst du beispielsweise die "PLAY"-Taste, wird "Empfangene Taste: PLAY" ausgegeben.

**Code-Verständnis**

#. Module importieren:
   
   * ``ir_rx.nec.NEC_8``: Der NEC-Protokoll-Decoder für 8-Bit-Adressen.
   * ``print_error``: Funktion zur Fehlerausgabe.

   .. code-block:: python

        import time
        from machine import Pin
        from ir_rx.nec import NEC_8
        from ir_rx.print_error import print_error

#. IR-Empfänger-Pin initialisieren:

   .. code-block:: python

        ir_pin = Pin(17, Pin.IN)

#. Callback-Funktion definieren:

   Diese Funktion wird automatisch aufgerufen, wenn ein Signal empfangen wird. Die Variable data enthält den Tasten-Code.

   .. code-block:: python

        def ir_callback(data, addr, ctrl):
            if data < 0:
                pass  # Wiederholungscodes ignorieren
            else:
                key = decode_key(data)
                print("Received Key:", key)

#. Dekodierungsfunktion für Tasten:

   Zuordnung der empfangenen Tasten-Codes zu lesbaren Bezeichnungen.

   .. code-block:: python

        def decode_key(data):
            key_codes = {
            0x45: "POWER",
            0x46: "MODE",
            0x47: "MUTE",
            0x44: "PLAY/PAUSE",
            0x40: "BACKWARD",
            0x43: "FORWARD",
            0x07: "EQ",
            0x15: "-",
            0x09: "+",
            0xD: "U/SD",
            0x16: "0",
            0x19: "cycle",
            0xC: "1",
            0x5E: "3",
            0x18: "2",
            0x8: "4",
            0x1C: "5",
            0x5A: "6",
            0x42: "7",
            0x52: "8",
            0x4A: "9",
            0x0: "ERROR",
            # Add more key codes based on your remote
            }
            return key_codes.get(data, "UNKNOWN")

#. IR-Empfänger initialisieren:

   Richtet den IR-Empfänger mit der Callback-Funktion ein.

   .. code-block:: python

        ir = NEC_8(ir_pin, ir_callback)
        ir.error_function(print_error)


#. Hauptschleife:

   Hält das Programm am Laufen, um IR-Signale zu empfangen. Sorgt für eine saubere Beendigung des Programms.

   .. code-block:: python

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            ir.close()
            print("Program terminated")

**Anwendungen**

* **Drahtlose Steuerung von Projekten:** Steuere LEDs, Motoren oder andere Komponenten per IR.
* **Universelle Fernbedienung:** Passe den Code an, um verschiedene Fernbedienungen oder Protokolle zu unterstützen.

**Fazit**

Diese Lektion zeigt, wie man mit einem IR-Empfänger am Raspberry Pi Pico 2 W Signale einer Infrarot-Fernbedienung dekodiert, um drahtlose Steuerungsmöglichkeiten für eigene Projekte zu schaffen.

* `Callback Function - Wikipedia <https://en.wikipedia.org/wiki/Callback_(computer_programming)>`_

