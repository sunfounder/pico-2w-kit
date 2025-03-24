.. note:: 

    Hallo, willkommen in der Community für Raspberry Pi, Arduino und ESP32-Enthusiasten von SunFounder auf Facebook! Vertiefen Sie Ihr Wissen über Raspberry Pi, Arduino und ESP32 zusammen mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_relay:


2.16 Einen weiteren Stromkreis mit einem Relais steuern
==========================================================

In dieser Lektion lernen wir, wie man mit einem **Relais** und dem Raspberry Pi Pico 2 W einen anderen Stromkreis steuert. Ein Relais fungiert wie ein Schalter, der durch einen Niederspannungsstromkreis (wie den Pico) einen Hochspannungsstromkreis steuert. Zum Beispiel können Sie ein Relais verwenden, um eine Lampe oder ein anderes Gerät einzuschalten, was die Automatisierung elektrischer Geräte ermöglicht.

.. warning::
    Das Modifizieren von elektrischen Geräten birgt große Gefahren. Versuchen Sie dies nicht leichtfertig und führen Sie es nur unter Anleitung von Fachleuten durch.

* :ref:`cpn_relay`

Hier verwenden wir nur einen einfachen, durch ein Steckbrett-Stromversorgungsmodul gespeisten Schaltkreis als Beispiel, um zu zeigen, wie man ihn mit einem Relais steuert.

* :ref:`cpn_power_module`

**Erforderliche Komponenten**

Für dieses Projekt benötigen wir folgende Komponenten.

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

Sie können diese auch einzeln über die untenstehenden Links kaufen.


.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - KOMPONENTENVORSTELLUNG	
        - MENGE
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
        - :ref:`cpn_transistor`
        - 1 (S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_diode`
        - 1
        - 
    *   - 7
        - :ref:`cpn_relay`
        - 1
        - |link_relay_buy|

**Schaltplan**

|sch_relay_1|

* Relaisaktivierung:

  * Die Spule des Relais wird durch den Transistor aktiviert, wenn der Pico ein **hohes Signal** (3,3V) an GP15 ausgibt.
  * Der Transistor ermöglicht den Stromfluss durch das Relais, was den Schalter im Inneren aktiviert.
  * Das Relais macht ein "Klick"-Geräusch beim Schalten, was die Kontrolle über den Laststromkreis anzeigt.

* Freilaufdiode:

  * Die Diode wird über die Relaisspule platziert, um den Transistor vor Spannungsspitzen zu schützen, die auftreten, wenn das Relais abgeschaltet wird.

**Verdrahtungsplan**

|wiring_relay_1|

**Code**


.. note::

    * Sie können die Datei ``2.16_relay.ino`` unter dem Pfad ``pico-2w-kit-main/arduino/2.16_relay`` öffnen.
    * Oder kopieren Sie diesen Code in die **Arduino IDE**.
    * Vergessen Sie nicht, das Board (Raspberry Pi Pico) und den richtigen Port vor dem Klicken auf den **Hochladen**-Knopf auszuwählen.

.. code-block:: arduino

   const int relayPin = 15;  // GPIO-Pin verbunden mit der Basis des Transistors

   void setup() {
     pinMode(relayPin, OUTPUT);
     digitalWrite(relayPin, LOW);  // Stellen Sie sicher, dass das Relais beim Start ausgeschaltet ist
   }

   void loop() {
     // Schalten Sie das Relais ein
     digitalWrite(relayPin, HIGH);
     Serial.println("Relay ON");
     delay(2000);  // Warten Sie 2 Sekunden

     // Schalten Sie das Relais aus
     digitalWrite(relayPin, LOW);
     Serial.println("Relay OFF");
     delay(2000);  // Warten Sie 2 Sekunden
   }

Nach dem Hochladen des Codes sollten Sie alle 2 Sekunden ein "Klick"-Geräusch vom Relais hören, wenn es ein- und ausschaltet.

**Verständnis des Codes**

#. Definition des Relais-Pins:

   Weist ``relayPin`` GPIO 15 zu, der den Transistor und damit das Relais steuert.

   .. code-block:: arduino

        const int relayPin = 15;  // GPIO-Pin verbunden mit der Basis des Transistors

#. Einrichten der Pin-Modi:

   Stellt ``relayPin`` als Ausgang ein. Initialisiert das Relais im AUS-Zustand.

   .. code-block:: arduino

        void setup() {
          pinMode(relayPin, OUTPUT);
          digitalWrite(relayPin, LOW);  // Stellen Sie sicher, dass das Relais beim Start ausgeschaltet ist
        }

#. Steuerung des Relais:

   * Setzt ``relayPin`` auf ``HIGH``, um den Transistor einzuschalten, wodurch die Relaisspule aktiviert wird.
   * Wartet 2 Sekunden.
   * Setzt ``relayPin`` auf ``LOW``, um den Transistor auszuschalten, wodurch die Relaisspule deaktiviert wird.
   * Wartet weitere 2 Sekunden.
   * Wiederholt den Zyklus unbegrenzt.

   .. code-block:: arduino

        // Schalten Sie das Relais ein
        digitalWrite(relayPin, HIGH);
        Serial.println("Relais EIN");
        delay(2000);  // Warten Sie 2 Sekunden

        // Schalten Sie das Relais aus
        digitalWrite(relayPin, LOW);
        Serial.println("Relay OFF");
        delay(2000);  // Warten Sie 2 Sekunden

**Weitere Experimente**

* **Stellen Sie einen Timer ein**: Modifizieren Sie den Code, um das Relais 10 Minuten lang einzuschalten und dann automatisch auszuschalten.
* **Steuerung von Haushaltsgeräten**: Mit angemessener Anleitung können Sie Hochspannungsgeräte an das Relais anschließen, um Automatisierungsaufgaben wie das Ein- und Ausschalten von Lichtern oder Ventilatoren zu übernehmen.

  * Der Schaltkreis sollte folgendermaßen aussehen: Um zu demonstrieren, wie man einen externen Stromkreis sicher steuert, fügen wir eine externe 5V-Stromquelle (über ein Steckbrett-Stromversorgungsmodul) hinzu, um eine LED zu betreiben. Dies simuliert, wie Sie mit dem Relais höhere Spannungsgeräte (wie Haushaltsgeräte) steuern könnten. So modifizieren Sie den Schaltkreis:

    |sch_relay_2|
  
    |wiring_relay_2|

* Code zur Steuerung des Relais:

    .. code-block:: arduino
    
       const int relayPin = 15;  // GPIO-Pin verbunden mit der Basis des Transistors

       void setup() {
         pinMode(relayPin, OUTPUT);
         digitalWrite(relayPin, LOW);  // Stellen Sie sicher, dass das Relais beim Start ausgeschaltet ist
       }

       void loop() {
         // Schalten Sie das Relais ein
         digitalWrite(relayPin, HIGH);
         Serial.println("Relay ON");
         delay(2000);  // Warten Sie 2 Sekunden

         // Schalten Sie das Relais aus
         digitalWrite(relayPin, LOW);
         Serial.println("Relay OFF");
         delay(2000);  // Warten Sie 2 Sekunden
       }

    Wenn das Relais aktiviert wird (GP15 gibt ein hohes Signal aus), verbinden sich die Normally Open (NO) und Common (C) Pins des Relais, wodurch der externe 5V-Strom durch die LED fließen kann. Die LED leuchtet auf und simuliert, wie ein Relais ein externes Gerät steuern kann.

    Wenn das Relais deaktiviert wird (GP15 gibt ein niedriges Signal aus), trennt sich der Normally Open (NO) Pin vom Common (C) Pin, was die externe Stromzufuhr unterbricht und die LED ausschaltet.


**Sicherheitsüberlegungen für die Steuerung echter Geräte**

Dieses Beispiel verwendet eine LED und eine 5V-Stromquelle, um die Relaissteuerung zu demonstrieren. Wenn Sie höhere Spannungsgeräte (wie Haushaltsgeräte) steuern, stellen Sie sicher:

* **Richtige Spannungsbewertung**: Verwenden Sie ein Relais, das für die angemessene Spannung und Stromstärke Ihres Geräts ausgelegt ist.
* **Isolierung**: Achten Sie aus Sicherheitsgründen auf eine angemessene Isolierung zwischen dem Niederspannungssteuerkreis (wie dem Pico) und dem Hochspannungsgerätekreis.
* **Sicherungsschutz**: Erwägen Sie das Hinzufügen von Sicherungen oder Leitungsschutzschaltern, um gegen Kurzschlüsse oder Überlastungen zu schützen.
* **Fachliche Anleitung**: Suchen Sie immer professionelle Beratung, wenn Sie mit Hochspannungsstromkreisen arbeiten, um einen sicheren Betrieb zu gewährleisten.

Dieses Projekt kann als Grundlage für die Hausautomatisierung dienen, wie zum Beispiel die Steuerung von Lampen, Ventilatoren oder anderen Geräten, die auf Zeitgeber oder Sensoren basieren, die mit dem Raspberry Pi Pico 2 W verbunden sind.

**Verwendung des NC-Terminals**

* Wenn Sie Ihren gesteuerten Stromkreis zwischen COM und NC anschließen:

  * Der Stromkreis wird geschlossen (EIN) sein, wenn das Relais nicht aktiviert ist.
  * Der Stromkreis wird geöffnet (AUS) sein, wenn das Relais aktiviert ist.
  * Beispiel: Steuerung eines externen Geräts
  * Warnung: Versuchen Sie nicht, Hochspannungsgeräte ohne angemessene Kenntnisse und Sicherheitsvorkehrungen zu steuern.

* Wenn Sie einen kleinen Gleichstrommotor oder ein anderes Gerät steuern möchten:

  * Ersetzen Sie die LED durch das Gerät, das Sie steuern möchten.
  * Stellen Sie sicher, dass die Spannungs- und Stromanforderungen des Geräts kompatibel sind.
  * Stellen Sie eine geeignete Stromversorgung für das Gerät bereit.
  * Schließen Sie das Gerät in Serie mit den COM- und NO- (oder NC-)Klemmen des Relais an.

**Fazit**

In dieser Lektion haben Sie gelernt, wie Sie einen anderen Stromkreis mit einem Relais und dem Raspberry Pi Pico steuern können. Durch die Verwendung eines Transistors zum Schalten der Relaisspule haben Sie einen Stromkreis mit höherem Strom sicher gesteuert, ohne die GPIO-Pins des Pico zu überlasten. Das Verständnis der Verwendung von Relais eröffnet viele Möglichkeiten zur Steuerung verschiedener Geräte und Haushaltsgeräte in Ihren Projekten.
