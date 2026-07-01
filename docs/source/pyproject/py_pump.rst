.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein zusammen mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Tutorials zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nehmen Sie an Giveaways und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie [|link_sf_facebook|] und treten Sie heute bei!

.. _py_pump:

3.6 Pumpen
=======================

In dieser Lektion lernen wir, wie man eine **kleine Wasserpumpe** mit dem 
Raspberry Pi Pico 2 W und einem **TA6586-Motortreiber** steuert. Eine kleine 
Zentrifugalpumpe kann für Projekte wie automatische Bewässerungssysteme für 
Pflanzen oder das Erstellen von Miniaturwassermerkmalen verwendet werden. 
Die Steuerung der Pumpe ähnelt der Steuerung eines Gleichstrommotors, da sie 
denselben Prinzipien folgt.

Ihr Antriebselement ist ein Elektromotor, der genau wie ein normaler Motor 
angetrieben wird.

* :ref:`cpn_pump`
* :ref:`cpn_motor`
* :ref:`cpn_ta6586`
* :ref:`cpn_power_module`

**Wichtige Hinweise bevor Sie beginnen**

* **Pumpeneinrichtung**: Schließen Sie den Schlauch an den Auslass der Pumpe an. Tauchen Sie die Pumpe vor dem Einschalten ins Wasser.
* **Trockenlauf vermeiden**: Stellen Sie sicher, dass die Pumpe immer untergetaucht ist. Trockenlauf kann Überhitzung verursachen und den Motor beschädigen.
* **Verstopfung verhindern**: Wenn Sie die Pumpe zur Bewässerung von Pflanzen verwenden, stellen Sie sicher, dass das Wasser frei von Schmutz ist, um eine Verstopfung zu verhindern.
* **Pumpe entlüften**: Wenn anfangs kein Wasser austritt, könnte Luft im Schlauch eingeschlossen sein. Möglicherweise müssen Sie die Pumpe entlüften, indem Sie Wasser durchfließen lassen, um Luftblasen zu entfernen.


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
        - :ref:`cpn_ta6586`
        - 1
        -
    *   - 6
        - :ref:`cpn_lipo_charger`
        - 1
        -
    *   - 7
        - Power Pack
        - 1
        -
    *   - 8
        - :ref:`cpn_pump`
        - 1
        -

**Wichtige Hinweise bevor Sie beginnen**

* **Pumpeneinrichtung**: Schließen Sie den Schlauch an den Auslass der Pumpe an. Tauchen Sie die Pumpe vor dem Einschalten ins Wasser.
* **Trockenlauf vermeiden**: Stellen Sie sicher, dass die Pumpe immer untergetaucht ist. Trockenlauf kann Überhitzung verursachen und den Motor beschädigen.
* **Verstopfung verhindern**: Wenn Sie die Pumpe zur Bewässerung von Pflanzen verwenden, stellen Sie sicher, dass das Wasser frei von Schmutz ist, um eine Verstopfung zu verhindern.
* **Pumpe entlüften**: Wenn anfangs kein Wasser austritt, könnte Luft im Schlauch eingeschlossen sein. Möglicherweise müssen Sie die Pumpe entlüften, indem Sie Wasser durchfließen lassen, um Luftblasen zu entfernen.

**Schaltplan**

|sch_pump|


**Verdrahtung**

In diesem Schaltkreis sehen Sie, dass der Knopf mit dem RUN-Pin verbunden ist. Dies liegt daran, dass der Motor mit zu viel Strom betrieben wird, was dazu führen kann, dass der Pico sich vom Computer trennt, und der Knopf muss gedrückt werden (damit der RUN-Pin des Pico ein niedriges Signal erhält), um ihn zurückzusetzen.

|wiring_pump|

**Code**

.. note::

    * Öffnen Sie die Datei ``3.6_pumping.py`` im Pfad ``pico-2w-kit-main/micropython`` oder kopieren Sie diesen Code in Thonny, dann klicken Sie auf „Run Current Script“ oder drücken Sie einfach F5, um es auszuführen.

    * Vergessen Sie nicht, den Interpreter „MicroPython (Raspberry Pi Pico)“ in der unteren rechten Ecke auszuwählen.

    * Für detaillierte Tutorials beziehen Sie sich bitte auf :ref:`open_run_code_py`.


.. code-block:: python

    import machine
    import utime

    # Definieren Sie die Steuerpins, die mit dem TA6586 verbunden sind
    motor1A = machine.Pin(14, machine.Pin.OUT)
    motor2A = machine.Pin(15, machine.Pin.OUT)

    # Starten Sie die Pumpe, indem Sie motor1A hoch und motor2A niedrig setzen
    while True:
        motor1A.high()
        motor2A.low()


Wenn der Code läuft, beginnt die Pumpe zu arbeiten und Sie werden sehen, dass Wasser gleichzeitig aus dem Schlauch fließt.

**Verständnis des Codes**

#. Import von Modulen:

   * ``machine``: Zugriff auf hardwarebezogene Funktionen.
   * ``utime``: Zeitbezogene Funktionen für Verzögerungen.

#. Initialisierung der Steuerpins:

   ``motor1A`` und ``motor2A`` steuern die Pumpe über den TA6586.

   .. code-block:: python

      motor1A = machine.Pin(14, machine.Pin.OUT)
      motor2A = machine.Pin(15, machine.Pin.OUT)

#. Starten der Pumpe:

   Setzt die Pumpe in Betrieb, indem ein hohes Signal an motor1A und ein niedriges Signal an motor2A angelegt wird.

   .. code-block:: python

      motor1A.high()
      motor2A.low()



**Fehlerbehebungstipps**

* Pumpe startet nicht:

  * Überprüfen Sie alle Verdrahtungsverbindungen.
  * Stellen Sie sicher, dass die Pumpe im Wasser untergetaucht ist.

* Pico reagiert nicht mehr:

  * Wenn sich der Pico trennt oder das Programm stoppt, müssen Sie ihn möglicherweise zurücksetzen.
  * Verwenden Sie die Reset-Verbindung, indem Sie den RUN-Pin kurz mit GND verbinden.

* Pumpe läuft weiter, nachdem das Skript gestoppt wurde:

  * Der letzte Zustand der GPIO-Pins bleibt nach dem Stoppen des Skripts unverändert.
  * Setzen Sie den Pico zurück, um die Pumpe zu stoppen, indem Sie RUN mit GND verbinden.

  |wiring_run_reset|

**Sicherheitsvorkehrungen**

* Elektrische Sicherheit:

  * Seien Sie vorsichtig beim Umgang mit Wasser und Elektronik.
  * Halten Sie den Pico und andere elektronische Komponenten fern von Wasser, um Schäden oder Verletzungen zu vermeiden.

* Pumpenpflege:

  * Lassen Sie die Pumpe nicht trocken laufen.
  * Reinigen Sie die Pumpe regelmäßig, wenn Sie sie mit Wasser verwenden, das Partikel enthalten könnte.

**Schlussfolgerung**

In dieser Lektion haben Sie gelernt, wie man eine kleine Wasserpumpe mit dem Raspberry Pi Pico 2 W und einem TA6586-Motortreiber steuert. Diese Einrichtung kann die Grundlage für Projekte wie automatische Bewässerungssysteme oder Miniaturbrunnen sein.
