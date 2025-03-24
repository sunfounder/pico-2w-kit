.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt des Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Expertenunterstützung**: Löse Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Werbegeschenke**: Nimm an Werbegeschenken und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu erschaffen? Klicke auf [|link_sf_facebook|] und trete heute bei!

.. _py_reversing_aid:

7.10 Bau eines Rückfahrhilfesystems
===========================================

In diesem Projekt werden wir ein **Rückfahrhilfesystem** mit dem Raspberry Pi Pico 2 W, 
einem Ultraschallsensor, einer LED und einem Summer erstellen. Dieses System simuliert die 
Funktionsweise von realen Parksensoren, indem es die Entfernung zu einem Hindernis erkennt 
und audiovisuelles Feedback gibt, das sich je nach Nähe ändert. Du kannst dieses Setup an 
ein ferngesteuertes Auto anbringen, um die Erfahrung des Rückwärtsfahrens in eine Garage nachzuahmen.

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

Du kannst sie auch separat über die untenstehenden Links kaufen.


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
        - :ref:`cpn_resistor`
        - 2(1KΩ, 220Ω)
        - |link_resistor_buy|
    *   - 7
        - Aktiver :ref:`cpn_buzzer`
        - 1
        -
    *   - 8
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 9
        - :ref:`cpn_ultrasonic`
        - 1
        - |link_ultrasonic_buy|

**Verständnis der Komponenten**

* **Ultraschallsensor (HC-SR04):** Misst die Entfernung zu einem Objekt, indem er Ultraschallwellen aussendet und die Zeit misst, die das Echo zur Rückkehr benötigt.
* **Summer:** Gibt akustisches Feedback; piept häufiger, je näher das Objekt kommt.
* **LED:** Gibt visuelles Feedback; blinkt schneller, je näher das Objekt kommt.

**Schaltplan**

|sch_reversing_aid|


**Verdrahtung**

|wiring_reversing_aid| 

**Code schreiben**

Wir schreiben ein MicroPython-Skript, das:

* Die Entfernung mit dem Ultraschallsensor misst.
* Die Piepfrequenz des Summers und die Blinkrate der LED je nach Entfernung anpasst.
* Kontinuierliches Feedback gibt, wenn sich das Objekt nähert oder entfernt.

.. note::

    * Öffne die Datei ``7.10_reversing_aid.py`` aus ``pico-2w-kit-main/micropython`` oder kopiere den Code in Thonny, dann klicke auf "Ausführen" oder drücke F5.

    * Stelle sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx. 

.. code-block:: python

    import machine
    import utime

    # Pin-Einstellungen
    trigger = machine.Pin(17, machine.Pin.OUT)
    echo = machine.Pin(16, machine.Pin.IN)
    buzzer = machine.Pin(15, machine.Pin.OUT)
    led = machine.Pin(14, machine.Pin.OUT)

    # Funktion zur Entfernungsmessung
    def measure_distance():
        # Stelle sicher, dass der Trigger niedrig ist
        trigger.low()
        utime.sleep_us(2)
        # Sende ein 10µs-Signal zum Auslösen
        trigger.high()
        utime.sleep_us(10)
        trigger.low()

        # Messe die Dauer des Echo-Signals
        while echo.value() == 0:
            signaloff = utime.ticks_us()
        while echo.value() == 1:
            signalon = utime.ticks_us()

        timepassed = utime.ticks_diff(signalon, signaloff)
        distance = (timepassed * 0.0343) / 2  # Umrechnung in cm
        return distanz

    # Funktion zur Steuerung von Summer und LED
    def alert(interval):
        buzzer.high()
        led.high()
        utime.sleep(0.1)
        buzzer.low()
        led.low()
        utime.sleep(interval)

    # Hauptprogrammschleife
    try:
        while True:
            dist = measure_distance()
            print("Distance: {:.2f} cm".format(dist))
            if dist < 0:
                print("Out of range")
                utime.sleep(1)
            elif dist <= 10:
                alert(0.2)  # Sehr nahe, schnell warnen
            elif dist <= 20:
                alert(0.5)  # Nah, mäßig warnen
            elif dist <= 50:
                alert(1)    # Nicht zu nah, langsam warnen
            else:
                alert(2)    # Weit entfernt, selten warnen
    except KeyboardInterrupt:
        print("Measurement stopped by User")


Sobald das Skript läuft, platziere ein Objekt in verschiedenen Entfernungen vor dem Ultraschallsensor.
Beobachte die Veränderungen in der Piepfrequenz und der Blinkrate der LED.
Die Konsole zeigt die gemessene Entfernung an.

**Verständnis des Codes**

#. Entfernungsmessung:

   * Die Funktion ``measure_distance()`` sendet einen 10-Mikrosekunden-Impuls an den TRIG-Pin.
   * Anschließend wird die Zeit gemessen, bis der ECHO-Pin aktiv wird und dann wieder deaktiviert.
   * Die Entfernung wird auf Basis der Zeit berechnet, die der Ultraschallimpuls für die Rückkehr benötigt.

   .. code-block:: python

        def measure_distance():
            # Sicherstellen, dass der Trigger deaktiviert ist
            trigger.low()
            utime.sleep_us(2)
            # 10us Impuls an Trigger senden
            trigger.high()
            utime.sleep_us(10)
            trigger.low()

            # Dauer des Echoimpulses messen
            while echo.value() == 0:
                signaloff = utime.ticks_us()
            while echo.value() == 1:
                signalon = utime.ticks_us()

            timepassed = utime.ticks_diff(signalon, signaloff)
            distance = (timepassed * 0.0343) / 2  # Umrechnung in cm
            return distance


#. Alarmfunktion:

   * Die Funktion ``alert(interval)`` aktiviert den Summer und die LED für 0,1 Sekunden und schaltet sie dann aus.
   * Der Parameter `interval` passt die Pause zwischen den Alarmen basierend auf der Entfernung an.

   .. code-block:: python

        def measure_distance():
            # Ensure trigger is low
            trigger.low()
            utime.sleep_us(2)
            # Send 10us pulse to trigger
            trigger.high()
            utime.sleep_us(10)
            trigger.low()

            # Measure the duration of the echo pulse
            while echo.value() == 0:
                signaloff = utime.ticks_us()
            while echo.value() == 1:
                signalon = utime.ticks_us()

            timepassed = utime.ticks_diff(signalon, signaloff)
            distance = (timepassed * 0.0343) / 2  # Convert to cm
            return distance

#. Hauptzyklus:

   * Misst kontinuierlich die Entfernung.
   * Passt die Alarmfrequenz gemäß vordefinierten Entfernungsschwellen an.

   .. code-block:: python

        try:
            while True:
                dist = measure_distance()
                print("Distance: {:.2f} cm".format(dist))
                if dist < 0:
                    print("Out of range")
                    utime.sleep(1)
                elif dist <= 10:
                    alert(0.2)  # Sehr nah, häufiger Alarm
                elif dist <= 20:
                    alert(0.5)  # Nah, mäßig häufiger Alarm
                elif dist <= 50:
                    alert(1)    # Nicht zu nah, langsamer Alarm
                else:
                    alert(2)    # Weit entfernt, selten Alarm
        except KeyboardInterrupt:
            print("Measurement stopped by User")
        
**Sicherheitsüberlegungen**

* Spannungsniveaus:

  * Seien Sie vorsichtig mit der Spannung am ECHO-Pin des Ultraschallsensors, wenn Sie 5V verwenden.
  * Verwenden Sie einen Spannungsteiler oder Pegelwandler, um die GPIO-Pins des Pico zu schützen.

* Stromversorgung:

  Stellen Sie sicher, dass die Stromversorgung die Stromanforderungen aller Komponenten bewältigen kann.

**Weiterführende Experimente**

* Visuelle Anzeige:

  Fügen Sie ein LCD- oder OLED-Display hinzu, um die Entfernung visuell darzustellen.

* Mehrere Sensoren:

  Verwenden Sie zusätzliche Ultraschallsensoren, um mehr Richtungen abzudecken.

* Fortgeschrittene Alarme:

  Implementieren Sie unterschiedliche Töne oder Muster am Summer für verschiedene Entfernungen.

**Schlussfolgerung**

Sie haben erfolgreich ein Rückfahrunterstützungssystem mit dem Raspberry Pi Pico 2 W gebaut! Dieses Projekt demonstriert, wie Sensoren verwendet werden können, um Echtzeit-Feedback zu liefern, ein grundlegendes Konzept in der Robotik und Automatisierung.



