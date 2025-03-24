.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein zusammen mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Tutorials zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nehmen Sie an Giveaways und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie [|link_sf_facebook|] und treten Sie heute bei!

.. _py_pot:

2.11 Den Drehregler bedienen
===============================

In dieser Lektion werden wir untersuchen, wie man analoge Eingaben mit dem eingebauten Analog-Digital-Umsetzer (ADC) des Raspberry Pi Pico 2 W liest und diese Eingaben verwendet, um die Helligkeit einer LED zu steuern. Insbesondere verwenden wir einen Potenziometer—einen variablen Widerstand—als analoges Eingabegerät. Durch Drehen des Knopfes des Potenziometers justieren wir die Spannungsebene, die der Pico liest, welche wir dann nutzen, um die Helligkeit der LED mittels Pulsweitenmodulation (PWM) zu steuern.

**Verständnis von Analogeingaben**

Bisher haben wir mit digitalen Eingaben und Ausgaben gearbeitet, die entweder EIN (hohe Spannung) oder AUS (niedrige Spannung) sind. Viele reale Signale sind jedoch analog, das heißt, sie können kontinuierlich über einen Bereich von Werten variieren. Beispiele hierfür sind Lichtintensität, Temperatur und Schallpegel.

Der Raspberry Pi Pico 2 W verfügt über einen eingebauten ADC, der es ihm ermöglicht, analoge Spannungen zu lesen und sie in digitale Werte umzuwandeln, die im Code verarbeitet werden können.

Der ADC wandelt die analoge Spannung vom Potenziometer in einen digitalen Wert um, der mit der Formel berechnet wird:

.. code-block::

  Digital Value = (Analog Voltage/3.3V) * 65535


**ADC-Pins des Pico**

|pin_adc|

Der Pico hat drei GPIO-Pins, die für analoge Eingaben verwendet werden können:

* **GP26** (ADC0)
* **GP27** (ADC1)
* **GP28** (ADC2)

Zusätzlich gibt es einen vierten ADC-Kanal, der intern mit einem Temperatursensor verbunden ist (ADC4), den wir in späteren Lektionen erkunden werden.

* :ref:`cpn_potentiometer`

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
        - :ref:`cpn_resistor`
        - 1(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 7
        - :ref:`cpn_potentiometer`
        - 1
        - |link_potentiometer_buy|


**Schaltplan**

|sch_pot|

Das Potentiometer ist ein analoges Gerät und wenn Sie es in 2 verschiedene Richtungen drehen.

Verbinden Sie den mittleren Pin des Potentiometers mit dem analogen Pin GP28. Der Raspberry Pi Pico 2 W enthält einen mehrkanaligen, 16-Bit-Analog-Digital-Umsetzer. Dies bedeutet, dass er die Eingangsspannung zwischen 0 und der Betriebsspannung (3.3V) einer ganzzahligen Wert zwischen 0 und 65535 zuordnet, so dass der GP28-Wert von 0 bis 65535 reicht.

Die Berechnungsformel wird unten gezeigt.

    (Vp/3.3V) x 65535 = Ap

Programmieren Sie dann den Wert von GP28 (Potentiometer) als den PWM-Wert von GP15 (LED).
Auf diese Weise werden Sie feststellen, dass sich durch Drehen des Potentiometers die Helligkeit der LED gleichzeitig ändert.

**Verdrahtung**



|wiring_pot|


**Schreiben des Codes**

.. note::

  * Öffnen Sie die Datei ``2.11_turn_the_knob.py`` im Pfad ``pico-2w-kit-main/micropython`` oder kopieren Sie den unten stehenden Code in Thonny. Dann klicken Sie auf "Run Current Script" oder drücken Sie **F5** um es auszuführen.
  * Stellen Sie sicher, dass der "MicroPython (Raspberry Pi Pico).COMxx" Interpreter in der unteren rechten Ecke von Thonny ausgewählt ist.
  * Für detaillierte Anweisungen beziehen Sie sich bitte auf :ref:`open_run_code_py`.

.. code-block:: python

  import machine
  import utime

  # Initialisieren des ADC auf GP28
  potentiometer = machine.ADC(28)

  # Initialisieren des PWM auf GP15
  led = machine.PWM(machine.Pin(15))
  led.freq(1000)  # PWM-Frequenz auf 1000Hz setzen

  while True:
      # Den analogen Wert lesen (0-65535)
      value = potentiometer.read_u16()
      print("Potentiometer value:", value)

      # Die LED-Helligkeit einstellen
      led.duty_u16(value)

      # Kleine Verzögerung, um die Messwerte zu stabilisieren
      utime.sleep_ms(200)

Wenn Sie das Programm ausführen, ändert sich die Helligkeit der LED, wenn Sie am Potentiometer drehen. Zusätzlich wird der aktuelle analoge Wert, der vom Potentiometer gelesen wird, in der Konsole angezeigt.

**Verständnis des Codes**

#. Analoge Messung:

   * ``potentiometer = machine.ADC(28)`` initialisiert den ADC am Pin GP28.
   * ``value = potentiometer.read_u16()`` liest die analoge Spannung vom Potentiometer und gibt eine 16-Bit-Ganzzahl zwischen **0** und **65535** zurück.
     
     * **0** entspricht **0V**.
     * **65535** entspricht **3.3V** (die Betriebsspannung des Pico).

#. Steuerung der LED mit PWM:

   * ``led = machine.PWM(machine.Pin(15))`` richtet PWM am Pin GP15 ein.
   * ``led.freq(1000)`` stellt die PWM-Frequenz auf 1000Hz ein.
   * ``led.duty_u16(value)`` stellt das Tastverhältnis des PWM-Signals basierend auf der Lesung des Potentiometers ein.

     * Ein höherer ``value`` erhöht das Tastverhältnis und macht die LED heller.
     * Ein niedrigerer ``value`` verringert das Tastverhältnis und dimmt die LED.

#. Ausgabe des Wertes:

   * ``print("Potentiometer value:", value)`` gibt den aktuellen analogen Wert zur Überwachung in die Konsole aus.


**Weiterführende Experimente**

* **PWM-Frequenz ändern**: Probieren Sie verschiedene Frequenzen mit ``led.freq()`` aus und beobachten Sie die Auswirkung auf die LED.
  
* **ADC-Wert umrechnen**: Führen Sie einen Skalierungsfaktor ein oder ordnen Sie den ADC-Wert einem anderen Bereich zu, um zu sehen, wie dies die LED-Helligkeit beeinflusst.

* **Andere ADC-Pins verwenden**: Verbinden Sie das Potentiometer mit GP26 oder GP27 und passen Sie den Code entsprechend an.

**Fehlerbehebungstipps**

* LED ändert nicht die Helligkeit:

  * Stellen Sie sicher, dass die LED und der Widerstand korrekt verbunden sind.
  * Überprüfen Sie, ob das Potentiometer richtig verdrahtet ist.

* Falsche ADC-Werte:

  * Überprüfen Sie die Verbindungen zu GP28.
  * Stellen Sie sicher, dass die äußeren Pins des Potentiometers mit 3.3V und GND verbunden sind.

**Schlussfolgerung**

Durch die Integration von analogem Eingang mit PWM-Ausgang haben wir eine einfache, aber leistungsfähige Möglichkeit geschaffen, die Helligkeit einer LED mit einem Potentiometer zu steuern. Dieses Projekt demonstriert, wie man analoge Signale liest und verwendet, um andere Komponenten zu steuern, eine grundlegende Fähigkeit in der Elektronik und der Mikrocontroller-Programmierung.

**Referenzen**

* |link_wiki_pwm|
* |link_mpython_adc|