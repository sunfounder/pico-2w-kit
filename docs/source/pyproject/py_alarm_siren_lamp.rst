.. note::

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche gemeinsam mit anderen Technikbegeisterten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum solltest du beitreten?**

    - **Kompetente Unterstützung**: Erhalte Hilfe bei Fragen nach dem Kauf oder bei technischen Problemen durch unsere Community und unser Team.
    - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um deine Fähigkeiten zu erweitern.
    - **Exklusive Einblicke**: Erfahre als Erster von neuen Produktankündigungen und Vorschauen.
    - **Spezielle Rabatte**: Profitiere von exklusiven Angeboten auf unsere neuesten Produkte.
    - **Aktionen & Verlosungen**: Nimm an saisonalen Gewinnspielen und Sonderaktionen teil.

    👉 Bereit, gemeinsam mit uns zu entdecken und zu gestalten? Klicke auf [|link_sf_facebook|] und werde Teil der Community!

.. _py_alarm_lamp:

7.3 Bau einer Alarm-Sirenen-Lampe
=======================================================

In diesem Projekt bauen wir eine **Alarm-Sirenen-Lampe** mit dem Raspberry Pi Pico 2 W. Das Gerät simuliert das blinkende Licht und den Sirenenton eines Polizeiwagens oder Einsatzfahrzeugs. Eine unterhaltsame Art, um mehr über PWM (Pulsweitenmodulation), Interrupts und die Ansteuerung mehrerer Komponenten wie LEDs und Summer zu lernen.



**Erforderliche Komponenten**

Für dieses Projekt benötigen wir die folgenden Bauteile.

Es ist auf jeden Fall praktisch, ein Komplettset zu kaufen. Hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ENTHALTENE TEILE IM KIT
        - LINK
    *   - Pico 2 W Starter Kit	
        - 450+
        - |link_pico2w_kit|

Alternativ kannst du die Bauteile auch einzeln über die folgenden Links erwerben.


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
        - Einige
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
        - |link_passive_buzzer_buy|
    *   - 9
        - :ref:`cpn_capacitor`
        - 1 (104)
        - |link_capacitor_buy|
    *   - 10
        - :ref:`cpn_slide_switch`
        - 1
        - 

**Verständnis der Komponenten**

* **Passiver Summer**: Benötigt ein externes Signal zur Tonerzeugung. Über PWM erzeugen wir wechselnde Frequenzen für den Sireneneffekt.
* **LED**: Simuliert das Blinken einer Sirene durch variierende Helligkeit.
* **Schiebeschalter**: Dient als Ein-/Ausschalter für den Alarm.
* **NPN-Transistor (S8050)**: Treibt den Summer an, da die GPIO-Pins des Pico nicht genügend Strom liefern können.
* **Widerstand und Kondensator**: Entprellen den Schiebeschalter, um stabile Signale zu gewährleisten.

**Schaltplan**

|sch_alarm_siren_lamp|

* GP17 ist mit dem mittleren Pin des Schalters verbunden sowie mit einem 10K-Widerstand und einem Kondensator (Filter) parallel zu GND. Dadurch kann der Schalter beim Umschalten zuverlässig ein stabiles High- oder Low-Signal liefern.
* Sobald GP15 auf High geht, leitet der NPN-Transistor, und der passive Summer beginnt zu tönen. Der Summer wird so angesteuert, dass die Frequenz allmählich ansteigt und so ein Sirenengeräusch erzeugt.
* Eine LED ist an GP16 angeschlossen und wird so programmiert, dass sie ihre Helligkeit periodisch ändert – ebenfalls zur Simulation der Sirene.



**Verdrahtung**

|wiring_alarm_siren_lamp|


**Writing the Code**

Wir schreiben ein MicroPython-Skript, das den Summer und die LED abhängig von der Stellung des Schalters steuert.

.. note::

    * Öffne ``7.3_alarm_siren_lamp.py`` im Verzeichnis ``pico-2w-kit-main/micropython`` oder kopiere den Code in Thonny und klicke auf "Run" bzw. drücke F5.
    * Stelle sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx.

.. code-block:: python 

    import machine
    import utime

    # Initialisierung von PWM für Summer und LED
    buzzer = machine.PWM(machine.Pin(15))
    led = machine.PWM(machine.Pin(16))
    led.freq(1000)  # PWM-Frequenz für die LED setzen

    # Initialisierung des Schalters
    switch = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_DOWN)

    # Funktion zur Abbildung von Werten aus einem Bereich in einen anderen
    def interval_mapping(x, in_min, in_max, out_min, out_max):
        # Sicherstellen, dass in_min != in_max ist, um Division durch Null zu vermeiden
        if in_max - in_min == 0:
            return out_min
        return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

    # Hauptschleife
    try:
        while True:
            if switch.value() == 1:
                # Alarm EIN
                # Frequenz und Helligkeit erhöhen
                for i in range(0, 100, 2):
                    # 'i' auf LED-Helligkeit und Summerfrequenz abbilden
                    brightness = interval_mapping(i, 0, 100, 0, 65535)
                    frequency = interval_mapping(i, 0, 100, 500, 2000)
                    
                    # LED-Helligkeit setzen
                    led.duty_u16(brightness)
                    
                    # Summerfrequenz und Tastverhältnis setzen
                    buzzer.freq(frequency)
                    buzzer.duty_u16(32768)  # 50 % Tastverhältnis
                    
                    utime.sleep(0.01)
                    
                # Frequenz und Helligkeit verringern
                for i in range(100, 0, -2):
                    brightness = interval_mapping(i, 0, 100, 0, 65535)
                    frequency = interval_mapping(i, 0, 100, 500, 2000)
                    
                    led.duty_u16(brightness)
                    buzzer.freq(frequency)
                    buzzer.duty_u16(32768)
                    
                    utime.sleep(0.01)
            else:
                # Alarm AUS
                # LED und Summer ausschalten
                led.duty_u16(0)
                buzzer.duty_u16(0)
                utime.sleep(0.1)
    except KeyboardInterrupt:
        # Aufräumen
        buzzer.deinit()
        led.deinit()
        print("Program stopped.")

Sobald der Code läuft, schalten Sie den Schiebeschalter in die ON-Position.  
Der Summer sollte ein Sirenengeräusch erzeugen und die LED entsprechend blinken.  
Schalten Sie den Schalter auf OFF, um den Alarm zu stoppen.


**Verständnis des Codes**

#. Initialisierung:

   * **buzzer**: PWM-Objekt an GP15.
   * **led**: PWM-Objekt an GP16 mit 1kHz Frequenz zur weichen Helligkeitssteuerung.
   * **switch**: Eingang an GP17 mit internem Pull-down-Widerstand.

#. Intervall-Mapping-Funktion:

   Ordnet einen Wert von einem Wertebereich einem anderen zu – nützlich, um Schleifenwerte auf Frequenz- und Helligkeitsbereiche zu skalieren.

   .. code-block:: python

        # Function to map values from one range to another
        def interval_mapping(x, in_min, in_max, out_min, out_max):
            # Ensure in_min != in_max to avoid division by zero
            if in_max - in_min == 0:
                return out_min
            return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

#. Hauptschleife:

   * Überprüft den Zustand des Schalters.
   * Wenn der Schalter EIN ist (``switch.value() == 1``):

     * Zwei Schleifen erzeugen den Sireneneffekt:
     * Frequenz und Helligkeit werden erhöht.
     * Frequenz und Helligkeit werden wieder reduziert.
     * Die Frequenz des Summers variiert zwischen 500 Hz und 2000 Hz.
     * Die LED-Helligkeit wechselt von aus bis maximale Helligkeit und zurück.

     .. code-block:: python

        if switch.value() == 1:
            # Alarm is ON
            # Increase frequency and brightness
            for i in range(0, 100, 2):
                # Map 'i' to LED brightness and buzzer frequency
                brightness = interval_mapping(i, 0, 100, 0, 65535)
            ...
                
                utime.sleep(0.01)

   * Wenn der Schalter AUS ist: LED und Summer werden deaktiviert.

     .. code-block:: python

            else:
                # Alarm is OFF
                # Turn off LED and buzzer
                led.duty_u16(0)
                buzzer.duty_u16(0)
                utime.sleep(0.1)

   * Ausnahmebehandlung: Fängt eine Tastenkombination (Strg+C) ab, um PWM-Objekte sauber zu deaktivieren.

     .. code-block:: python
    
        except KeyboardInterrupt:
            # Clean up
            buzzer.deinit()
            led.deinit()
            print("Program stopped.")

**Weitere Experimente**

* Anpassung des Sireneneffekts:

  * Ändere den Frequenzbereich in der ``interval_mapping`` -Funktion, um die Tonhöhe zu verändern.
  * Passe die Verzögerung in den Schleifen (``utime.sleep(0.01)``) an, um den Ablauf zu beschleunigen oder zu verlangsamen.

* Weitere LEDs hinzufügen:

  * Ergänze zusätzliche LEDs in unterschiedlichen Farben für ein dynamischeres Lichtspiel.
  * Nutze mehrere GPIO-Pins und PWM-Kanäle.

* Bewegungserkennung:

  Ersetze den Schalter durch einen Bewegungssensor (z. B. PIR), um den Alarm bei erkannter Bewegung auszulösen.

* Fernbedienung:

  Integriere einen IR-Empfänger, um den Alarm per Fernbedienung zu steuern.

**Conclusion**

Du hast erfolgreich eine Alarm-Sirenen-Lampe mit dem Raspberry Pi Pico 2 W gebaut! Dieses Projekt zeigt, wie man mehrere Komponenten steuern und interaktive Effekte erzeugen kann. Es bildet eine hervorragende Grundlage für komplexere Projekte wie Alarmsysteme, Notfallanzeigen oder kreative Lichtinstallationen.
