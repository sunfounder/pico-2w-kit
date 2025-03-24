.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein und tausche dich mit anderen Technikbegeisterten aus.

    **Warum beitreten?**

    - **Expertenunterstützung**: Erhalte Hilfe bei technischen Herausforderungen und Fragen nach dem Kauf von unserer Community und unserem Team.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Previews.
    - **Spezielle Rabatte**: Profitiere von exklusiven Vergünstigungen für unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nimm an Verlosungen und saisonalen Promotions teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _py_motor:

3.5 Steuerung eines kleinen Lüfters (Gleichstrommotor)
==========================================================


In dieser Lektion lernen wir, wie man einen **Gleichstrommotor** 
(z. B. einen kleinen Lüfter) mit dem Raspberry Pi Pico 2 W und 
einem **TA6586-Motortreiber** steuert. Der TA6586 ermöglicht die 
Steuerung der Drehrichtung des Motors – sowohl im Uhrzeigersinn 
als auch gegen den Uhrzeigersinn. 

Da der Gleichstrommotor einen relativ hohen Strom benötigt, verwenden 
wir zur Sicherheit ein separates Stromversorgungsmodul, um den Motor zu betreiben.

* :ref:`cpn_motor`
* :ref:`cpn_ta6586`
* :ref:`cpn_power_module`

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
        - :ref:`cpn_ta6586`
        - 1
        - 
    *   - 6
        - :ref:`cpn_motor`
        - 1
        - |link_motor_buy| 
    *   - 7
        - :ref:`cpn_lipo_charger`
        - 1
        -  
    *   - 8
        - 18650 Batterie
        - 1
        -   



**Schaltplan**

|sch_motor|



**Verkabelung**

.. note::

    * Da Gleichstrommotoren einen hohen Strombedarf haben, verwenden wir hier zur Sicherheit ein Li-po-Lademodul zur Stromversorgung des Motors.
    * Stelle sicher, dass dein Li-po-Lademodul gemäß dem Schaltplan korrekt angeschlossen ist. Andernfalls kann ein Kurzschluss deine Batterie und Schaltung beschädigen.

|wiring_motor|

**Code**

.. note::

    * Öffne die Datei ``3.5_small_fan.py`` aus ``pico-2w-kit-main/micropython`` oder kopiere den Code in Thonny, klicke auf "Run" oder drücke F5.

    * Stelle sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx. 

.. code-block:: python

    import machine
    import utime

    motor1A = machine.Pin(14, machine.Pin.OUT)
    motor2A = machine.Pin(15, machine.Pin.OUT)

    def clockwise():
        motor1A.high()
        motor2A.low()

    def anticlockwise():
        motor1A.low()
        motor2A.high()

    def stopMotor():
        motor1A.low()
        motor2A.low()

    while True:
        clockwise()
        utime.sleep(1)
        stopMotor()
        utime.sleep(1)
        anticlockwise()
        utime.sleep(1)
        stopMotor()
        utime.sleep(1)

Sobald das Programm läuft, dreht sich der Motor in einem regelmäßigen Muster vorwärts und rückwärts.


**Den Code verstehen**

#. **Pins initialisieren**:

   ``motor1A`` und ``motor2A`` sind mit GP14 und GP15 verbunden und steuern die Drehrichtung des Motors.

   .. code-block:: python

     motor1A = machine.Pin(14, machine.Pin.OUT)
     motor2A = machine.Pin(15, machine.Pin.OUT)

#. **Funktionen definieren**:

   * ``rotate_clockwise()``: Setzt ``motor1A`` auf HIGH und ``motor2A`` auf LOW, um den Motor im Uhrzeigersinn zu drehen. 
   * ``rotate_counterclockwise()``: Setzt ``motor1A`` auf LOW und ``motor2A`` auf HIGH, um den Motor gegen den Uhrzeigersinn zu drehen.
   * ``stop_motor()``: Setzt sowohl ``motor1A`` als auch ``motor2A`` auf LOW, um den Motor zu stoppen.

#. Hauptschleife:

   Der Motor dreht sich eine Sekunde im Uhrzeigersinn, stoppt, dreht sich dann eine Sekunde gegen den Uhrzeigersinn und stoppt erneut. Dieser Ablauf wiederholt sich kontinuierlich.

   .. code-block:: python

    while True:
        clockwise()
        utime.sleep(1)
        stopMotor()
        utime.sleep(1)
        anticlockwise()
        utime.sleep(1)
        stopMotor()
        utime.sleep(1)

**Fehlersuche & Tipps**

* Motor läuft weiter, nachdem das Skript gestoppt wurde:

  Falls der Motor nach Beenden des Programms weiterläuft, kann es notwendig sein, den Pico zurückzusetzen. Verbinde dazu kurz den RUN-Pin mit GND, um einen Reset durchzuführen.

  |wiring_run_reset|

* Pico trennt sich oder reagiert nicht mehr:

  Der Motor kann hohe Ströme ziehen, die Spannungsschwankungen verursachen. Stelle sicher, dass du eine separate Stromversorgung für den Motor verwendest und alle Masseleitungen (GND) verbunden sind.

**Fazit**

In dieser Lektion hast du gelernt, wie du einen Gleichstrommotor mit dem TA6586-Motortreiber und dem **Raspberry Pi Pico 2 W** steuerst. Du kannst nun die Drehrichtung des Motors kontrollieren und Projekte wie einen kleinen Lüfter oder ein motorisiertes Gerät realisieren.

**Nächste Schritte**

* **Drehzahlregelung**: Verwende PWM (Pulsweitenmodulation), um die Drehzahl des Motors zu steuern, indem du den EN1-Pin mit einem PWM-fähigen GPIO-Pin verbindest.
* **Mehrere Motoren steuern**: Nutze die zusätzlichen Kanäle des TA6586, um mehrere Motoren gleichzeitig zu betreiben.
* **Sensorintegration**: Kombiniere Sensoren mit dem Motor, um ihn basierend auf Eingaben zu steuern (z. B. Temperatur- oder Lichtsensoren).
