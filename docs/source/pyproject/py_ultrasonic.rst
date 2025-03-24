.. note::
    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Vertiefe dich mit anderen Enthusiasten in Raspberry Pi, Arduino und ESP32.

    **Warum beitreten?**

    - **Expertenunterstützung**: Löse Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühen Zugang zu neuen Produktankündigungen und Einblicken.
    - **Spezielle Rabatte**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Promotionen und Gewinnspiele**: Nimm an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt heute bei!

.. _py_ultrasonic:

6.1 Distanzmessung
======================================

In dieser Lektion lernen wir, wie man ein **Ultraschallsensormodul** mit dem Raspberry Pi Pico 2 W verwendet, um die Distanz zu einem Objekt zu messen. Ultraschallsensoren werden häufig in der Robotik und in Automatisierungssystemen für die Objekterkennung und Distanzmessung eingesetzt.

* :ref:`cpn_ultrasonic`

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
        - :ref:`cpn_ultrasonic`
        - 1
        - |link_ultrasonic_buy|

**Verständnis des Ultraschallsensors**

Der Ultraschallsensor funktioniert, indem er einen kurzen Ultraschallimpuls vom **Trig**-Pin aussendet und das Echo am **Echo**-Pin empfängt. Indem die Zeit gemessen wird, die das Echo zur Rückkehr benötigt, können wir die Distanz zu einem Objekt unter Verwendung der Schallgeschwindigkeit berechnen.

|ultrasonic_prin|

* **Triggerimpuls**: Ein 10-Mikrosekunden hoher Impuls am Trig-Pin startet die Messung.
* **Ultraschallburst**: Der Sensor sendet einen 8-Zyklen-Ultraschallburst bei 40 kHz aus.
* **Echoempfang**: Der Echo-Pin wird hoch und bleibt hoch, bis das Echo zurückkommt.
* **Zeitmessung**: Durch Messung der Zeit, die der Echo-Pin hoch bleibt, können wir die Distanz berechnen.

**Schaltplan**

|sch_ultrasonic|

**Verdrahtung**

|wiring_ultrasonic|

**Schreiben des Codes**

Lass uns ein MicroPython-Programm schreiben, um die Distanz mit dem Ultraschallsensor zu messen.

.. note::

    * Öffne die Datei ``6.1_measuring_distance.py`` aus ``pico-2w-kit-main/micropython`` oder kopiere den Code in Thonny, dann klicke auf "Ausführen" oder drücke F5.
    * Stelle sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx.

.. code-block:: python

    import machine
    import utime

    # Definiere die Pins, die mit dem Sensor verbunden sind
    TRIG = machine.Pin(17, machine.Pin.OUT)
    ECHO = machine.Pin(16, machine.Pin.IN)

    def measure_distance():
        # Stelle sicher, dass der Trigger-Pin niedrig ist
        TRIG.low()
        utime.sleep_us(2)
        # Sende einen 10µs-Impuls, um die Messung zu starten
        TRIG.high()
        utime.sleep_us(10)
        TRIG.low()
        
        # Warte darauf, dass der Echo-Pin hoch geht (Start des Echo-Impulses)
        while ECHO.value() == 0:
            pass
        start_time = utime.ticks_us()
        
        # Warte darauf, dass der Echo-Pin niedrig geht (Ende des Echo-Impulses)
        while ECHO.value() == 1:
            pass
        end_time = utime.ticks_us()
        
        # Berechne die Dauer des Echo-Impulses
        duration = utime.ticks_diff(end_time, start_time)
        
        # Berechne die Distanz (Schallgeschwindigkeit ist 34300 cm/s)
        distance = (duration * 0.0343) / 2
        return distance

    while True:
        dist = measure_distance()
        print("Distance: {:.2f} cm".format(dist))
        utime.sleep(0.5)

Sobald der Code läuft, sollte die Thonny-Konsole die Distanzmessungen in Zentimetern anzeigen. Bewege ein Objekt näher oder weiter vom Sensor entfernt, um zu sehen, wie sich die Messwerte ändern.

**Verständnis des Codes**

#. Importiere notwendige Module und richte die Trigger- und Echo-Pins ein:

   .. code-block:: python
   
       import machine
       import utime
   
       TRIG = machine.Pin(17, machine.Pin.OUT)
       ECHO = machine.Pin(16, machine.Pin.IN)


#. Messung der Distanz:

   * Sendet einen Triggerimpuls, um die Messung zu starten.
   * Wartet auf die Echoantwort.
   * Berechnet die Dauer des Echoimpulses.
   * Berechnet die Distanz unter Verwendung der Schallgeschwindigkeit.

   .. code-block:: python

       def measure_distance():
           # Stelle sicher, dass der Trigger niedrig ist
           TRIG.low()
           utime.sleep_us(2)
           # Löse einen 10µs-Impuls aus
           TRIG.high()
           utime.sleep_us(10)
           TRIG.low()
           
           # Warte auf den Beginn des Echos
           while ECHO.value() == 0:
               pass
           start_time = utime.ticks_us()
           
           # Warte auf das Ende des Echos
           while ECHO.value() == 1:
               pass
           end_time = utime.ticks_us()
           
           # Berechne die Dauer
           duration = utime.ticks_diff(end_time, start_time)
           # Berechne die Distanz
           distance = (duration * 0.0343) / 2
           return distance


#. Hauptprogrammschleife:

   * Misst kontinuierlich und gibt die Distanz aus.
   * Pausiert eine halbe Sekunde zwischen den Messungen.

   .. code-block:: python
   
       while True:
           dist = measure_distance()
           print("Distance: {:.2f} cm".format(dist))
           utime.sleep(0.5)

**Verständnis der Einschränkungen**



* Blockierender Code:

  * Die While-Schleifen, die auf das Echo warten, können andere Codeausführungen blockieren.
  * Für fortgeschrittenere Anwendungen sollten Interrupts oder asynchrone Programmierung in Betracht gezogen werden, um Blockierungen zu vermeiden.

* Messbereich:

  * Der HC-SR04-Sensor hat typischerweise einen Bereich von 2 cm bis 400 cm.
  * Objekte, die näher als 2 cm oder weiter als 400 cm sind, werden möglicherweise nicht genau erkannt.

* Umweltfaktoren:

  * Temperatur und Luftfeuchtigkeit können die Schallgeschwindigkeit beeinflussen.
  * Für präzise Messungen sollte die Schallgeschwindigkeit basierend auf den Umgebungsbedingungen angepasst werden.

**Fazit**

Du hast erfolgreich einen Ultraschallsensor verwendet, um mit dem Raspberry Pi Pico 2 W Distanzen zu messen. Diese grundlegende Fähigkeit ist weit verbreitet in der Robotik, Automatisierung und bei interaktiven Projekten anwendbar.
