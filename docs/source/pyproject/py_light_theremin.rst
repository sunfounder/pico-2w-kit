.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein und tausche dich mit anderen Technikbegeisterten aus.

    **Warum beitreten?**

    - **Expertenunterstützung**: Erhalte Hilfe bei technischen Herausforderungen und Fragen nach dem Kauf von unserer Community und unserem Team.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Previews.
    - **Spezielle Rabatte**: Profitiere von exklusiven Vergünstigungen für unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nimm an Verlosungen und saisonalen Promotions teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _py_light_theremin:

7.1 Ein Licht-Theremin bauen
====================================================

In diesem spannenden Projekt bauen wir ein **Licht-Theremin** mit einem Raspberry Pi Pico 2 W, einem Fotoresistor und einem passiven Summer. Ein Theremin ist ein einzigartiges Musikinstrument, das ohne physische Berührung gespielt wird und verschiedene Töne erzeugt, abhängig von der Position der Hände des Spielers. Während wir ein traditionelles Theremin nicht vollständig nachbilden können, können wir seine Funktionsweise simulieren, indem wir die Lichtintensität zur Steuerung der Tonfrequenz nutzen.

* `Theremin - Wikipedia <https://en.wikipedia.org/wiki/Theremin>`_

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
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 6
        - :ref:`cpn_transistor`
        - 1 (S8050)
        - |link_transistor_buy|
    *   - 7
        - :ref:`cpn_resistor`
        - 3 (1KΩ, 220Ω, 10KΩ)
        - |link_resistor_buy|
    *   - 8
        - Passiver :ref:`cpn_buzzer`
        - 1
        - 
    *   - 9
        - :ref:`cpn_photoresistor`
        - 1
        - |link_photoresistor_buy|

**Funktionsweise**

* **Fotoresistor**: Ein Sensor, dessen Widerstand sich je nach Lichtintensität ändert. Mehr Licht verringert den Widerstand, weniger Licht erhöht ihn.
* **Passiver Summer**: Er benötigt ein externes Signal zur Klangerzeugung. Die Frequenz kann über Pulsweitenmodulation (PWM) gesteuert werden.
* **Transistor (S8050)**: Verstärkt den Strom, sodass der Summer effizient vom Pico angesteuert werden kann.

Indem wir die Werte des Fotoresistors auslesen, können wir die Lichtintensität einer bestimmten Tonfrequenz zuordnen. Das bedeutet, dass das Bewegen der Hand über den Fotoresistor die Tonhöhe des Summers verändert – ähnlich wie bei einem Theremin.

**Schaltplan**

|sch_light_theremin|

Bevor das Projekt gestartet wird, bewege deine Hand über den Fotoresistor, um den Bereich der Lichtintensität zu kalibrieren. Die LED an GP16 dient als Indikator für die Kalibrierung. Sie leuchtet während des Kalibriervorgangs und erlischt, sobald dieser abgeschlossen ist.

Wenn GP15 ein HIGH-Signal ausgibt, schaltet der NPN-Transistor (S8050) durch und der Summer beginnt zu tönen.

Je stärker das Licht, desto kleiner ist der Wert von GP28; je schwächer das Licht, desto größer ist der Wert.

Durch das Programmieren einer Verbindung zwischen dem Fotoresistor und der Frequenz des Summers kann ein lichtsensitives Musikinstrument simuliert werden.


**Verdrahtung**

|wiring_light_theremin|

**Code schreiben**

Wir schreiben ein MicroPython-Programm, das die Lichtintensität des Fotoresistors ausliest, diese in eine Frequenz umwandelt und diese über den Summer ausgibt.

.. note::

    * Öffne die Datei ``7.1_light_theremin.py`` aus ``pico-2w-kit-main/micropython`` oder kopiere den Code in Thonny, klicke auf "Run" oder drücke F5.
    * Stelle sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx. 

.. code-block:: python

    import machine
    import utime

    # Komponenten initialisieren
    led = machine.Pin(16, machine.Pin.OUT)  # LED an GP16
    photoresistor = machine.ADC(28)         # Fotoresistor an ADC0 (GP28)
    buzzer = machine.PWM(machine.Pin(15))   # Summer an GP15

    # Variablen für die Kalibrierung
    light_low = 65535
    light_high = 0

    # Funktion zur Skalierung von Werten
    def interval_mapping(x, in_min, in_max, out_min, out_max):
        # Ensure in_min != in_max to avoid division by zero
        if in_max - in_min == 0:
            return out_min
        return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

    # Funktion zur Klangerzeugung
    def play_tone(pin, frequency):
        if frequency <= 0:
            pin.duty_u16(0)
        else:
            pin.freq(frequency)
            pin.duty_u16(32768)  # 50 % Tastverhältnis

    # Kalibrierung
    def calibrate():
        global light_low, light_high
        print("Calibrating... Move your hand over the sensor.")
        led.value(1)  # Turn on LED to indicate calibration
        start_time = utime.ticks_ms()
        while utime.ticks_diff(utime.ticks_ms(), start_time) < 5000:  # 5 seconds calibration
            light_value = photoresistor.read_u16()
            if light_value > light_high:
                light_high = light_value
            if light_value < light_low:
                light_low = light_value
            utime.sleep_ms(10)
        led.value(0)  # Turn off LED after calibration 
        print("Calibration complete.")
        print("Light Low:", light_low)
        print("Light High:", light_high)

    # Hauptfunktion
    def main():
        calibrate()
        try:
            while True:
                light_value = photoresistor.read_u16()
                # Map the light value to a frequency range (e.g., 200 Hz to 2000 Hz)
                frequency = interval_mapping(light_value, light_low, light_high, 200, 2000)
                play_tone(buzzer, frequency)
                utime.sleep_ms(20)
        except KeyboardInterrupt:
            buzzer.deinit()
            print("Program stopped.")

    # Run the main function
    if __name__ == "__main__":
        main()

Wenn der Code ausgeführt wird, leuchtet die LED auf und signalisiert damit die Kalibrierungsphase.

* Kalibrierung:

  * Bewege deine Hand während der 5-sekündigen Kalibrierung über den Fotoresistor.
  * Dadurch kann das Programm den Bereich der Lichtverhältnisse erfassen.

* Das Theremin spielen:

  * Nach der Kalibrierung erlischt die LED.
  * Bewege deine Hand über den Fotoresistor.
  * Der Summer gibt Töne aus, deren Tonhöhe sich je nach Lichtintensität verändert.
  * Experimentiere mit verschiedenen Handpositionen und -bewegungen, um unterschiedliche Klänge zu erzeugen.


**Den Code verstehen**

#. Initialisierung:

   * **LED-Anzeige**: Zeigt an, wenn die Kalibrierung läuft.
   * **Fotoresistor**: Liest analoge Werte aus, die der Lichtintensität entsprechen.
   * **Summer**: Wird mittels PWM gesteuert, um Töne mit unterschiedlichen Frequenzen zu erzeugen.

#. Kalibrierungsfunktion (``calibrate()``):

   * Läuft 5 Sekunden und speichert dabei die minimalen und maximalen Lichtwerte.
   * Fordert den Benutzer auf, die Hand über den Sensor zu bewegen, um den Messbereich festzulegen.
   * Die LED dient als visuelles Signal.

   .. code-block:: python

        # Kalibrierungsprozess
        def calibrate():
            global light_low, light_high
            print("Calibrating... Move your hand over the sensor.")
            led.value(1)  # LED einschalten zur Anzeige der Kalibrierung
            start_time = utime.ticks_ms()
            while utime.ticks_diff(utime.ticks_ms(), start_time) < 5000:  # 5 Sekunden Kalibrierung
                light_value = photoresistor.read_u16()
                if light_value > light_high:
                    light_high = light_value
                if light_value < light_low:
                    light_low = light_value
                utime.sleep_ms(10)
            led.value(0)  # LED ausschalten nach der Kalibrierung
            print("Calibration complete.")
            print("Light Low:", light_low)
            print("Light High:", light_high)

#. Intervall-Mapping-Funktion (``interval_mapping()``):

   * Wandelt die Werte des Lichtsensors in einen für den Summer geeigneten Frequenzbereich um.
   * Verhindert Division durch Null.

   .. code-block:: python

        # Funktion zur Skalierung von Werten
        def interval_mapping(x, in_min, in_max, out_min, out_max):
            # Ensure in_min != in_max to avoid division by zero
            if in_max - in_min == 0:
                return out_min
            return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

#. Ton abspielen (``play_tone()``):

   * Setzt die Frequenz des Summers mittels PWM.
   * Falls die Frequenz null oder negativ ist, wird der Summer ausgeschaltet.

   .. code-block:: python

        # Funktion zum Abspielen eines Tons auf dem Summer
        def play_tone(pin, frequency):
            if frequency <= 0:
                pin.duty_u16(0)
            else:
                pin.freq(frequency)
                pin.duty_u16(32768)  # 50 % Tastverhältnis

#. Hauptschleife:

   * Liest kontinuierlich die Lichtwerte vom Fotoresistor aus.
   * Wandelt diese Werte in eine Frequenz um.
   * Gibt den entsprechenden Ton über den Summer aus.
   * Enthält eine Fehlerbehandlung zur Bereinigung beim Beenden.

   .. code-block:: python

        # Hauptfunktion
        def main():
            calibrate()
            try:
                while True:
                    light_value = photoresistor.read_u16()
                    # Wertebereich von 200 Hz bis 2000 Hz skalieren
                    frequency = interval_mapping(light_value, light_low, light_high, 200, 2000)
                    play_tone(buzzer, frequency)
                    utime.sleep_ms(20)
            except KeyboardInterrupt:
                buzzer.deinit()
                print("Program stopped.")

**Weitere Experimente**

* Frequenzbereich anpassen:

  Ändere die Werte in ``interval_mapping()``, um den Tonhöhenbereich zu variieren. Beispiel: Ersetze 200, 2000 durch 100, 5000 für einen erweiterten Bereich.

* Visuelles Feedback:

  Verwende zusätzliche LEDs, um optische Signale entsprechend der Tonhöhe anzuzeigen.

* Einen zweiten Sensor hinzufügen:

  Integriere einen weiteren Fotoresistor, um die Lautstärke oder eine andere Funktion zu steuern.

* Ein Musikinstrument entwickeln:

  Kombiniere verschiedene Sensoren oder Eingaben, um ein komplexeres Instrument zu erschaffen.

**Einschränkungen verstehen**

* Umgebungslicht:

  Änderungen in der Umgebungsbeleuchtung können die Leistung beeinflussen. Stelle eine konstante Lichtquelle sicher oder führe regelmäßig eine Neukalibrierung durch.

* Sensorempfindlichkeit:

  Der Fotoresistor reagiert möglicherweise nicht schnell genug auf schnelle Handbewegungen.

* Klangqualität:

  Passive Summer haben eine begrenzte Klangqualität. Für eine bessere Audioausgabe kann ein aktiver Lautsprecher mit DAC-Ausgang verwendet werden.

**Fazit**

Du hast erfolgreich ein Licht-Theremin mit dem Raspberry Pi Pico 2 W gebaut! Dieses Projekt zeigt, wie Sensoren und Aktoren kombiniert werden können, um interaktive und unterhaltsame Experimente zu erstellen. Experimentiere weiter und modifiziere das Projekt, um dein Verständnis und deine Kreativität zu erweitern.
