.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Sonderangebote**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nehmen Sie an Giveaways und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie [|link_sf_facebook|] und treten Sie heute bei!

.. _py_relay:

2.16 Steuerung eines anderen Stromkreises
=============================================

In dieser Lektion lernen wir, wie man mit einem **Relais** und dem Raspberry Pi Pico 2 W einen anderen Stromkreis steuert. Ein Relais funktioniert wie ein durch einen Niederspannungsstromkreis (wie Pico) gesteuerter Schalter, um einen Hochspannungsstromkreis zu betreiben. Beispielsweise können Sie ein Relais verwenden, um eine Lampe oder ein anderes Gerät einzuschalten, was die Automatisierung elektrischer Geräte ermöglicht.

.. warning::
    Der Umbau elektrischer Geräte birgt große Gefahren, versuchen Sie dies nicht leichtfertig und bitte nur unter Anleitung von Fachleuten.

* :ref:`cpn_relay`

Hier verwenden wir nur einen einfachen Stromkreis, der von einem Steckbrett-Strommodul gespeist wird, als Beispiel, um zu zeigen, wie man ihn mit einem Relais steuert.

* :ref:`cpn_power_module`

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
        - :ref:`cpn_transistor`
        - 1(S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_diode`
        - 1
        -
    *   - 7
        - :ref:`cpn_relay`
        - 1
        - |link_relay_buy|


**Verdrahtung**

Zuerst bauen Sie einen Niederspannungsstromkreis, um ein Relais zu steuern.
Das Antrieben des Relais benötigt einen hohen Strom, daher wird ein Transistor benötigt, und hier verwenden wir den S8050.

|sch_relay_1|

* Relaisaktivierung:

  * Die Spule des Relais wird durch den Transistor energisiert, wenn der Pico ein **hohes Signal** (3,3V) an GP15 ausgibt.
  * Der Transistor ermöglicht den Stromfluss durch das Relais, was den Schalter im Inneren aktiviert.
  * Das Relais macht ein „Klick“-Geräusch beim Schalten, was die Steuerung des Laststromkreises anzeigt.

* Freilaufdiode:

  * Die Diode wird über die Relaisspule platziert, um den Transistor vor Spannungsspitzen zu schützen, die auftreten, wenn das Relais abgeschaltet wird.

**Schaltplan**

|wiring_relay_1|



Der folgende Code steuert das Relais und schaltet den angeschlossenen Stromkreis alle zwei Sekunden ein und aus.

.. note::

    * Öffnen Sie die Datei ``2.16_control_another_circuit.py`` aus ``pico-2w-kit-main/micropython`` oder kopieren Sie den Code in Thonny und klicken Sie auf „Run“ oder drücken Sie F5.
    * Stellen Sie sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx.

.. code-block:: python

    import machine
    import utime

    # Initialisieren des Relaispins an GP15
    relay = machine.Pin(15, machine.Pin.OUT)

    while True:
        relay.value(1)  # Das Relais einschalten
        utime.sleep(2)  # 2 Sekunden warten
        relay.value(0)  # Das Relais ausschalten
        utime.sleep(2)  # 2 Sekunden warten

Wenn der Code läuft, sollten Sie alle zwei Sekunden ein „Klick“-Geräusch vom Relais hören, was darauf hinweist, dass der Stromkreis ein- und ausgeschaltet wird.

**Weiterführende Experimente**

* **Zeitschaltuhr einstellen**: Ändern Sie den Code, um das Relais 10 Minuten lang einzuschalten und dann automatisch auszuschalten.
* **Hausgeräte steuern**: Mit entsprechender Anleitung können Sie Hochspannungsgeräte an das Relais anschließen, um Automatisierungsaufgaben wie das Ein- und Ausschalten von Lichtern oder Ventilatoren durchzuführen.

  * Der Schaltkreis sollte so aussehen: Um die Steuerung eines externen Stromkreises sicher zu demonstrieren, fügen wir ein Li-po-Ladegerätmodul hinzu, um eine LED zu betreiben. Dies simuliert, wie Sie höhere Spannungsgeräte (wie Haushaltsgeräte) steuern könnten. Hier ist, wie Sie den Schaltkreis ändern:

    |sch_relay_2|

    |wiring_relay_2|

  * Code zur Steuerung des Relais:

    .. code-block:: python

        import machine
        import utime

        # Initialisieren des Relaispins an GP15
        relay = machine.Pin(15, machine.Pin.OUT)

        while True:
            relay.value(1)  # Das Relais einschalten
            utime.sleep(2)  # 2 Sekunden warten
            relay.value(0)  # Das Relais ausschalten
            utime.sleep(2)  # 2 Sekunden warten

    Wenn das Relais aktiviert wird (GP15 gibt ein hohes Signal aus), verbinden sich die Normally Open (NO) und Common (C) Pins des Relais, was den externen Li-po-Ladegerätmodul durch die LED fließen lässt. Die LED leuchtet auf und simuliert, wie ein Relais ein externes Gerät steuern kann.

    Wenn das Relais deaktiviert wird (GP15 gibt ein niedriges Signal aus), trennt sich der Normally Open (NO) Pin vom Common (C) Pin, was die externe Stromversorgung unterbricht und die LED ausschaltet.

**Sicherheitsüberlegungen für die Steuerung echter Geräte**

Dieses Beispiel verwendet eine LED und ein Li-po-Ladegerätmodul, um die Relaissteuerung zu demonstrieren. Wenn Sie höhere Spannungsgeräte (wie Haushaltsgeräte) steuern, stellen Sie sicher:

* **Angemessene Spannungsbewertung**: Verwenden Sie ein Relais, das für die entsprechende Spannung und den Strom Ihrer Geräte geeignet ist.
* **Isolation**: Sorgen Sie für eine sichere Isolation zwischen dem Niederspannungssteuerkreis (wie dem Pico) und dem Hochspannungsgerätekreis.
* **Sicherungsschutz**: Erwägen Sie, Sicherungen oder Leistungsschalter hinzuzufügen, um gegen Kurzschlüsse oder Überlastungen zu schützen.
* **Fachliche Anleitung**: Wenn Sie mit Hochspannungskreisen arbeiten, suchen Sie immer fachliche Anleitung, um einen sicheren Betrieb zu gewährleisten.

Dieses Projekt kann als Grundlage für die Heimautomatisierung dienen, wie die Steuerung von Lampen, Ventilatoren oder anderen Geräten basierend auf Zeitgebern oder Sensoren, die mit dem Raspberry Pi Pico 2 W verbunden sind.

**Verwendung des NC-Terminals**

* Wenn Sie Ihren gesteuerten Stromkreis zwischen COM und NC anschließen:

  * Der Stromkreis ist geschlossen (ON), wenn das Relais nicht energisiert ist.
  * Der Stromkreis ist offen (OFF), wenn das Relais energisiert wird.
  * Beispiel: Steuerung eines externen Geräts
  * Warnung: Versuchen Sie nicht, Hochspannungsgeräte zu steuern, ohne angemessenes Wissen und Sicherheitsvorkehrungen.

* Wenn Sie einen kleinen Gleichstrommotor oder ein anderes Gerät steuern möchten:

  * Ersetzen Sie die LED durch das Gerät, das Sie steuern möchten.
  * Stellen Sie sicher, dass die Spannungs- und Stromanforderungen des Geräts kompatibel sind.
  * Stellen Sie eine angemessene Stromversorgung für das Gerät bereit.
  * Schließen Sie das Gerät in Reihe mit den COM- und NO- (oder NC-)Klemmen des Relais an.


**Schlussfolgerung**

Durch die Verwendung des Relais zur Steuerung eines externen Stromkreises haben Sie gelernt, wie man externe Geräte wie LEDs oder sogar Hochspannungsgeräte ein- und ausschaltet. Dies öffnet die Tür zur Schaffung automatisierter intelligenter Geräte, die durch Code gesteuert werden können, und bietet endlose Möglichkeiten für die Heimautomatisierung und andere Projekte.
