.. note:: 

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein und teile dein Wissen mit Gleichgesinnten.

    **Warum beitreten?**

    - **Experten-Support**: Erhalte Hilfe von unserer Community und unserem Team bei technischen Herausforderungen und nach dem Kauf auftretenden Problemen.
    - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Profitiere von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nimm an Gewinnspielen und saisonalen Aktionen teil.

    👉 Bereit, mit uns zu experimentieren und zu erschaffen? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _ar_ac_buz:

3.1 Den Buzzer zum Piepen bringen!
===================================

In dieser Lektion lernen wir, wie man einen **Buzzer** mit dem Raspberry Pi Pico 2 W zum Piepen bringt. Ein Buzzer ist ein digitales Ausgabegerät, ähnlich wie eine LED, und sehr einfach zu steuern. Für dieses Projekt verwenden wir einen **aktiven Buzzer**, der einen Ton erzeugt, sobald er ein Signal erhält.

**Was ist ein aktiver Buzzer?**

Ein **aktiver Buzzer** verfügt über einen internen Oszillator, der seine Nutzung erleichtert. Es genügt, ein Signal an den Buzzer zu senden, um ihn piepen zu lassen – eine komplexe Frequenzsteuerung ist nicht erforderlich. Dies unterscheidet ihn von einem **passiven Buzzer**, der ein externes Signal zur Tonerzeugung benötigt.

|img_buzzer|

* :ref:`cpn_buzzer`

**Erforderliche Komponenten**

Für dieses Projekt benötigen wir folgende Komponenten:

Ein Komplett-Kit ist besonders praktisch, hier ist der Link: 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ENTHALTENE TEILE
        - KAUFLINK
    *   - Pico 2 W Starter Kit	
        - 450+
        - |link_pico2w_kit|

Alternativ kannst du die Komponenten auch einzeln kaufen:


.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - KOMPONENTENBESCHREIBUNG	
        - MENGE
        - KAUFLINK

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
        - 1 (S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_resistor`
        - 1 (1 kΩ)
        - |link_resistor_buy|
    *   - 7
        - Aktiver :ref:`cpn_buzzer`
        - 1
        - 

**Schaltplan**

|sch_buzzer|

In dieser Schaltung wird der Buzzer über einen Transistor (**S8050** NPN) mit Strom versorgt. Der Transistor verstärkt den Strom, wodurch der Buzzer lauter wird, als wenn er direkt mit dem Pico verbunden wäre.

So funktioniert es:
* **GP15** gibt ein HIGH-Signal aus, um den Transistor zu steuern.
* Wenn der Transistor aktiviert wird, fließt Strom durch den Buzzer, wodurch er piept.

Ein **1-kΩ-Widerstand** begrenzt den Stromfluss und schützt den Transistor.

**Verdrahtung**

Stelle sicher, dass du einen **aktiven Buzzer** verwendest. Dieser hat eine versiegelte Rückseite, während ein **passiver Buzzer** eine offene Leiterplatte besitzt.

|img_buzzer|

|wiring_beep|


**Code schreiben**


.. note::

    * Die Datei ``3.1_beep.ino`` befindet sich unter ``pico-2w-kit-main/arduino/3.1_beep``. 
    * Alternativ kannst du den Code in die **Arduino IDE** kopieren.
    * Vergiss nicht, das Board (Raspberry Pi Pico) und den richtigen Port auszuwählen, bevor du auf **Upload** klickst.

.. code-block:: Arduino

    const int buzzerPin = 15;  // GPIO-Pin, der mit der Basis des Transistors verbunden ist

    void setup() {
      pinMode(buzzerPin, OUTPUT);
    }

    void loop() {
      digitalWrite(buzzerPin, HIGH);  // Buzzer einschalten
      delay(1000);                    // 1 Sekunde warten
      digitalWrite(buzzerPin, LOW);   // Buzzer ausschalten
      delay(1000);                    // 1 Sekunde warten
    }


Nach dem Hochladen des Codes:
Der Buzzer sollte 1 Sekunde lang piepen, dann 1 Sekunde lang stumm sein und dieses Muster kontinuierlich wiederholen.
Falls kein Ton zu hören ist, überprüfe die Verdrahtung und stelle sicher, dass du einen aktiven Buzzer verwendest.

**Den Code verstehen**

#. Definition des Buzzer-Pins:

   Weist ``buzzerPin`` dem GPIO 15 zu, der den Transistor und damit den Buzzer steuert.

   .. code-block:: Arduino

        const int buzzerPin = 15;  // GPIO-Pin für den Transistor

#. Einrichtung des Pin-Modus:

   Konfiguriert ``buzzerPin`` als Ausgang.

   .. code-block:: Arduino

        void setup() {
          pinMode(buzzerPin, OUTPUT);
        }

#. Steuerung des Buzzers: Die Funktion ``loop()`` wiederholt diesen Prozess unendlich oft und lässt den Buzzer jede Sekunde piepen.

   * ``digitalWrite(buzzerPin, HIGH)``: Schaltet ``buzzerPin`` auf ``HIGH``, wodurch der Transistor eingeschaltet wird, der Strom durch den Buzzer fließen lässt und ihn piepen lässt.
   * ``delay(1000)``: Pausiert das Programm für 1000 Millisekunden (1 Sekunde).
   * ``digitalWrite(buzzerPin, LOW)``: Schaltet ``buzzerPin`` auf ``LOW``, wodurch der Transistor ausgeschaltet wird und der Buzzer verstummt.

   .. code-block:: Arduino

        void loop() {
          digitalWrite(buzzerPin, HIGH);  // Buzzer einschalten
          delay(1000);                    // 1 Sekunde warten
          digitalWrite(buzzerPin, LOW);   // Buzzer ausschalten
          delay(1000);                    // 1 Sekunde warten
        }

**Weitere Experimente**

* Veränderung der Piep-Dauer:

  * Ändere die Werte in ``delay()``, um die Länge des Pieptons und der Pausen zu variieren.
  * Experimentiere mit kürzeren oder längeren Zeiten.

* Erstellung von Mustern:

  * Erzeuge komplexe Tonmuster, indem du die Wartezeiten in der ``loop()``-Funktion anpasst.
  * Beispielsweise kann ein SOS-Signal im Morsecode programmiert werden.

* Verwendung eines passiven Buzzers:

  * Versuche, einen passiven Buzzer mit der ``tone()``-Funktion zu verwenden, um unterschiedliche Frequenzen zu erzeugen.
  * Beachte, dass die Verdrahtung und der Code für einen passiven Buzzer anders sind.

**Fazit**

In dieser Lektion hast du gelernt, wie du einen aktiven Buzzer mit dem Raspberry Pi Pico und einem Transistor zum Piepen bringst. Durch die Steuerung des Transistors über einen GPIO-Pin kannst du den Buzzer sicher ein- und ausschalten, ohne die GPIO-Pins des Pico zu überlasten. Dieses grundlegende Konzept kann erweitert werden, um komplexere Töne zu erzeugen oder den Buzzer in Alarmanlagen, Benachrichtigungen und interaktiven Projekten zu nutzen.
