.. note:: 
   
    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Vertiefen Sie Ihr Wissen über Raspberry Pi, Arduino und ESP32 zusammen mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unserem Team.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_reed:

2.9 Den Magnetismus spüren
===============================

In dieser Lektion werden wir den Einsatz eines **Reedschalters** mit dem Raspberry Pi Pico 2 W zur Detektion eines Magnetfelds erkunden. Ein Reedschalter ist ein einfacher elektrischer Schalter, der mit einem Magnetfeld betrieben wird. Nähert sich ein Magnet dem Schalter, schließen sich die internen Kontakte und vervollständigen einen elektrischen Stromkreis.

* :ref:`cpn_reed`

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Es ist definitiv praktisch, ein ganzes Kit zu kaufen, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ARTIKEL IN DIESEM KIT
        - KAUF-LINK
    *   - Pico 2 W Starter Kit	
        - 450+
        - |link_pico2w_kit|


Sie können sie auch separat über die untenstehenden Links kaufen.


.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - KOMPONENTEN-EINFÜHRUNG	
        - ANZAHL
        - KAUF-LINK

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
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_reed`
        - 1
        - 

**Verständnis des Reedschalters**

Ein Reedschalter besteht aus zwei dünnen Metallzungen, die in einem Glasgehäuse eingeschlossen sind. Diese Zungen sind aus ferromagnetischem Material und stehen leicht auseinander. In Abwesenheit eines Magnetfelds sind die Zungen getrennt und der Schalter ist **offen**. Nähert sich ein Magnet dem Schalter, werden die Zungen magnetisiert, ziehen sich an und schließen den Stromkreis.

* **Kein Magnet in der Nähe**: Schalter ist **offen**; der Stromkreis ist unterbrochen.
* **Magnet in der Nähe**: Schalter ist **geschlossen**; der Stromkreis ist geschlossen.

|img_reed_sche|

**Schaltplan**

|sch_reed|

Standardmäßig ist GP14 niedrig; er wird hoch, wenn der Magnet in der Nähe des Reedschalters ist.

Der Zweck des 10K-Widerstands besteht darin, den GP14 auf einem stabilen niedrigen Niveau zu halten, wenn kein Magnet in der Nähe ist.

* **Kein Magnet in der Nähe**:

  * Der Reedschalter ist **offen**.
  * **GP14** ist durch den Pull-Down-Widerstand mit **GND** verbunden.
  * Der GPIO-Pin liest **NIEDRIG** (0).

* **Magnet in der Nähe**:

  * Der Reedschalter ist **geschlossen**.
  * **GP14** ist durch den Reedschalter mit **3.3V** verbunden.
  * Der GPIO-Pin liest **HOCH** (1).

**Verdrahtung**


|wiring_reed|

**Code**

.. note::

    * Sie können die Datei ``2.9_feel_the_magnetism.ino`` unter dem Pfad ``pico-2w-kit-main/arduino/2.9_feel_the_magnetism`` öffnen. 
    * Oder kopieren Sie diesen Code in die **Arduino IDE**.
    * Vergessen Sie nicht, das Board (Raspberry Pi Pico) und den richtigen Port auszuwählen, bevor Sie auf den **Hochladen** -Knopf klicken.

.. code-block:: Arduino


   const int reedPin = 14;    // GPIO-Pin, verbunden mit dem Reedschalter
   int reedState = 0;

   void setup() {
     Serial.begin(115200);       // Initialisieren des Serial Monitors mit 115200 Baud
     pinMode(reedPin, INPUT);    // Den Reed-Pin als Eingang setzen
   }

   void loop() {
     reedState = digitalRead(reedPin);  // Den Zustand des Reedschalters lesen

     if (reedState == HIGH) {
       Serial.println("Magnet Detected!");
     } else {
       Serial.println("No Magnet.");
     }
     delay(500);  // Verzögerung, um den Serial Monitor nicht zu überfluten
   }

Wenn der Code läuft und der Serial Monitor geöffnet ist:

* **Kein Magnet in der Nähe**: Der Serial Monitor zeigt "Kein Magnet."
* **Magnet in der Nähe**: Bringen Sie einen Magnet in die Nähe des Reedschalters. Der Serial Monitor zeigt "Magnet erkannt!"

**Verständnis des Codes**

#. Initialisierung der seriellen Kommunikation:

   Startet die serielle Kommunikation mit einer Baudrate von 115200. Dies ermöglicht es uns, Nachrichten auf dem Serial Monitor auszugeben.

   .. code-block:: Arduino

        Serial.begin(115200);

#. Einrichtung des Reed-Pins:
 
   Konfiguriert reedPin (GP14) als Eingang, um den Zustand des Reedschalters zu lesen.

   .. code-block:: Arduino

        pinMode(reedPin, INPUT);

#. Lesen des Zustands des Reedschalters:

   Liest den aktuellen Zustand des Reedschalters. Er ist HOCH, wenn der Magnet in der Nähe ist (Schalter geschlossen) und NIEDRIG, wenn kein Magnet in der Nähe ist (Schalter offen).

   .. code-block:: Arduino

        reedState = digitalRead(reedPin);

#. Reaktion auf die Anwesenheit des Magneten:

   Gibt eine Nachricht aus, je nachdem, ob ein Magnet in der Nähe des Reedschalters ist.

   .. code-block:: Arduino

        if (reedState == HIGH) {
          Serial.println("Magnet Detected!");
        } else {
          Serial.println("No Magnet.");
        }


**Mehr lernen: Verwendung von Unterbrechungen mit dem Reedschalter**

* **Einführung in Unterbrechungen**

  Stellen Sie sich vor, Sie lesen ein Buch, ganz vertieft in die Geschichte. Plötzlich tippt Ihnen jemand auf die Schulter, um eine Frage zu stellen. Sie pausieren Ihr Lesen, beantworten die Frage und kehren dann zu Ihrem Buch zurück. Diese Unterbrechung ähnelt der Funktionsweise von Unterbrechungen in Mikrocontrollern.
  
  Eine Unterbrechung ermöglicht es einem Programm, sofort auf wichtige Ereignisse zu reagieren, indem es den Hauptprogrammablauf pausiert, um eine spezielle Funktion namens Interrupt Service Routine (ISR) auszuführen. Nach der Bearbeitung der Unterbrechung setzt das Programm dort fort, wo es unterbrochen wurde.
  
* **Warum Unterbrechungen verwenden?**

  Die Verwendung von Unterbrechungen mit dem Reedschalter ermöglicht es dem Mikrocontroller, sofort zu reagieren, wenn ein Magnet erkannt wird, anstatt den Reedschalter kontinuierlich in der ``loop()``-Funktion abzufragen. Dies ist effizienter und kann Strom in batteriebetriebenen Anwendungen sparen.

* **Schreiben des Codes mit Unterbrechungen**

  Wir modifizieren unser Programm, um eine Unterbrechung zur Erkennung des Magneten zu verwenden.

  .. code-block:: Arduino

        const int reedPin = 14;            // GPIO-Pin, verbunden mit dem Reedschalter
        volatile bool magnetDetected = false;  // Flag, um anzuzeigen, ob ein Magnet erkannt wurde

        void setup() {
          Serial.begin(115200);               // Serial Monitor initialisieren
          pinMode(reedPin, INPUT);            // Den Reed-Pin als Eingang setzen
          attachInterrupt(digitalPinToInterrupt(reedPin), onMagnetChange, CHANGE);  // Unterbrechung bei jeder Änderung anhängen
        }

        void loop() {
          if (magnetDetected) {
            Serial.println("Magnet Present!");
          } else {
            Serial.println("Waiting for magnet...");
          }
          delay(1000);                         // Verzögerung, um den Serial Monitor nicht zu überfluten
        }

        void onMagnetChange() {
          // Das Flag basierend auf dem aktuellen Zustand des Reed-Pins aktualisieren
          magnetDetected = digitalRead(reedPin) == HIGH;  // Wenn HOCH, ist ein Magnet vorhanden; wenn NIEDRIG, ist kein Magnet vorhanden
        }


  .. code-block:: Arduino

        attachInterrupt(digitalPinToInterrupt(reedPin), onMagnetChange, CHANGE);
    
  * ``digitalPinToInterrupt(reedPin)``: Konvertiert die Pinnummer in die entsprechende Interruptnummer.
  * ``onMagnetChange``: Der Name der ISR-Funktion, die aufgerufen wird, wenn die Unterbrechung eintritt.
  * ``CHANGE``: Die Unterbrechung wird ausgelöst, wenn eine Änderung am Pin auftritt.


**Fazit**

In dieser Lektion haben Sie gelernt, wie man einen Reedschalter mit dem Raspberry Pi Pico verwendet, um die Anwesenheit eines Magnetfelds zu erkennen. Sie haben auch erkundet, wie Unterbrechungen Ihr Programm effizienter machen können, indem sie sofort auf Ereignisse reagieren, ohne den Sensor ständig im Hauptprogramm zu überprüfen. Das Verständnis der Verwendung von Unterbrechungen ist eine wertvolle Fähigkeit in der eingebetteten Programmierung, die es Ihnen ermöglicht, reaktionsfähigere und effizientere Anwendungen zu erstellen.

**Weitere Erkundungen**

* **Türsensor**: Verwenden Sie den Reedschalter, um einen einfachen Türalarm zu erstellen, der auslöst, wenn die Tür geöffnet wird.
* **Umdrehungen zählen**: Befestigen Sie einen Magnet an einem rotierenden Objekt und verwenden Sie den Reedschalter, um die Umdrehungen pro Minute (RPM) zu zählen.
* **Sicherheitssysteme**: Integrieren Sie mehrere Reedschalter, um Fenster und Türen in einem Sicherheitssystem zu überwachen.

**Zusätzliche Ressourcen**

* `attachInterrupt() - Arduino Reference <https://www.arduino.cc/reference/en/language/functions/external-interrupts/attachinterrupt/>`_


