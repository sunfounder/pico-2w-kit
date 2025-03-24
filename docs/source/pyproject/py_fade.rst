.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche gemeinsam mit anderen Technikbegeisterten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum solltest du mitmachen?**

    - **Expertenhilfe**: Erhalte Unterstützung bei technischen Fragen und Problemen nach dem Kauf – durch unser Team und die Community.
    - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um dein Wissen zu erweitern.
    - **Exklusive Einblicke**: Erfahre frühzeitig von Produktneuheiten und erhalte exklusive Vorschauen.
    - **Spezielle Rabatte**: Profitiere von exklusiven Angeboten auf unsere neuesten Produkte.
    - **Feiertagsaktionen & Gewinnspiele**: Nimm an saisonalen Aktionen und Verlosungen teil.

    👉 Bereit, gemeinsam mit uns Neues zu entdecken und zu entwickeln? Klicke auf [|link_sf_facebook|] und werde Teil unserer Community!

.. _py_fade:

2.3 LED sanft ein- und ausblenden
======================================

In dieser Lektion lernen wir, wie man mithilfe von Pulsweitenmodulation (PWM) die Helligkeit einer LED auf dem Raspberry Pi Pico 2 W steuert. Diese Technik ist ein grundlegendes Werkzeug in der Elektronik, mit dem sich beispielsweise LEDs oder Motoren in ihrer Intensität regulieren lassen.

**Was ist PWM?**

**Pulsweitenmodulation (PWM)** ist ein Verfahren zur Steuerung der Leistungszufuhr an ein elektronisches Bauteil, indem die Spannung mit hoher Frequenz ein- und ausgeschaltet wird. Die „Breite“ des Impulses (die Zeit, in der das Signal aktiv ist) bestimmt, wie viel Leistung das Bauteil erhält.

|img_pwm_duty_cycle|

* **Duty Cycle (Tastverhältnis)**: Gibt an, wie viel Prozent eines Zyklus das Signal aktiv ist. 100 % bedeutet, das Signal ist durchgehend an, 0 % heißt, es ist immer aus.
* **Frequenz**: Gibt an, wie oft das Signal pro Sekunde ein- und ausgeschaltet wird.

Durch Anpassen des Tastverhältnisses können wir analoge Ausgaben mit digitalen Signalen simulieren. Wenn eine LED schnell genug ein- und ausgeschaltet wird, nimmt unser Auge unterschiedliche Helligkeitsstufen wahr – abhängig davon, wie lange die LED pro Zyklus leuchtet.

**Warum PWM verwenden?**

* **LED-Helligkeitssteuerung**: Sanftes Regeln der Leuchtkraft.
* **Motorsteuerung**: Geschwindigkeit von Gleichstrommotoren kontrollieren.
* **Effizienz**: PWM ist energieeffizienter als veränderliche Widerstände, da weniger Energie in Wärme umgewandelt wird.

**PWM auf dem Raspberry Pi Pico 2 W**

Der Raspberry Pi Pico 2 W unterstützt PWM auf allen GPIO-Pins. Intern stehen 8 PWM-Slices (PWM0 bis PWM7) zur Verfügung, jeweils mit zwei Kanälen (A und B), was insgesamt 16 unabhängige PWM-Ausgänge ergibt.

|pin_pwm|

.. note::
     Pins, die denselben PWM-Slice verwenden (z. B. GP0 und GP16), können nicht mit unterschiedlichen Frequenzen betrieben werden – jedoch mit unterschiedlichen Duty Cycles.


**Benötigte Komponenten**

Für dieses Projekt brauchst du folgende Bauteile:

Ein Komplett-Kit ist besonders praktisch – hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name
        - ENTHALTENE TEILE
        - LINK
    *   - Pico 2 W Starter Kit
        - 450+
        - |link_pico2w_kit|

Die Komponenten sind auch einzeln erhältlich:


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
        - 1 (220 Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|

**Schaltplan**

|sch_led|

**Verdrahtung**

|wiring_led|


**Den Code schreiben**


.. note::

  * Öffne die Datei ``2.3_fading_led.py`` aus dem Ordner ``pico-2w-kit-main/micropython`` oder kopiere den Code in Thonny und klicke auf „Run“ oder drücke F5.
  
  * Stelle sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico) COMxx.



.. code-block:: python

    import machine
    import utime

    # PWM auf Pin GP15 einrichten
    led = machine.PWM(machine.Pin(15))
    led.freq(1000)  # Frequenz auf 1000 Hz setzen

    # Helligkeit schrittweise erhöhen
    for duty in range(0, 65536, 64):
        led.duty_u16(duty)  # Duty Cycle setzen (16-Bit-Wert)
        utime.sleep(0.01)   # 10 ms warten

    # LED ausschalten
    led.duty_u16(0)

Sobald der Code ausgeführt wird, beginnt die LED an Pin GP15 langsam heller zu leuchten – von ausgeschaltet bis zur vollen Helligkeit.


**Den Code verstehen**

* Bibliotheken importieren:

  * ``machine``: Zugriff auf die Hardware des Pico.
  * ``utime``: Ermöglicht Zeitverzögerungen.

* PWM konfigurieren:

  * ``machine.PWM(machine.Pin(15))``: Initialisiert PWM auf GP15.
  * ``led.freq(1000)``: Setzt die PWM-Frequenz auf 1000 Hz (1 ms pro Zyklus).

* Duty Cycle anpassen:

  * ``for duty in range(0, 65536, 64)``: Schleife von 0 bis 65535 in 64er-Schritten.
  * ``led.duty_u16(duty)``: Legt das Tastverhältnis fest. Der Wert reicht von 0 (0 %) bis 65535 (100 %).
  * ``utime.sleep(0.01)``: Kurze Pause, um den Helligkeitsanstieg sichtbar zu machen.

* LED ausschalten:

  * ``led.duty_u16(0)``: Setzt das Tastverhältnis auf 0 % – die LED ist aus.


**Weitere Experimente**

* **Ein- und Ausblenden**: Erweitere den Code, um die LED auch wieder sanft zu dimmen.
* **Geschwindigkeit ändern**: Passe ``utime.sleep()`` an, um die Geschwindigkeit der Helligkeitsänderung zu steuern.
* **Frequenzen testen**: Experimentiere mit verschiedenen PWM-Frequenzen über ``led.freq()`` und beobachte die Wirkung.

**Fazit**

PWM ist eine leistungsstarke Technik zur Steuerung von Geräten, die analoge Eingänge erwarten – mithilfe digitaler Ausgaben. Wer PWM versteht, kann Projekte wie Motorsteuerungen, Audioanwendungen und vieles mehr realisieren.

Mit den Grundlagen der PWM auf dem Raspberry Pi Pico 2 W bist du bestens gerüstet für komplexere Elektronikprojekte.

**Referenzen**

* |link_mpython_pwm|