.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in Raspberry Pi, Arduino und ESP32 ein und lerne gemeinsam mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Experten-Support**: Lösche nach dem Verkauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitig Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Sonderrabatte**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nimm an Gewinnspielen und saisonalen Aktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _ar_motor:

3.5 Steuerung eines kleinen Lüfters (DC-Motor)
=================================================

In dieser Lektion lernen wir, wie man einen **DC-Motor** (wie einen kleinen Lüfter) mit dem Raspberry Pi Pico 2 W und einem **TA6586 Motorsteuerung** steuert. Der TA6586 ermöglicht es uns, die Drehrichtung des Motors zu steuern – sowohl im Uhrzeigersinn als auch gegen den Uhrzeigersinn. Da DC-Motoren mehr Strom benötigen, als der Pico direkt liefern kann, verwenden wir eine externe Stromversorgung, um den Motor sicher zu betreiben.


* :ref:`cpn_motor`
* :ref:`cpn_ta6586`
* :ref:`cpn_power_module`

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten. 

Es ist definitiv praktisch, ein komplettes Kit zu kaufen, hier ist der Link: 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ARTIKEL IN DIESEM KIT
        - KAUF-LINK
    *   - Pico 2 W Starter Kit	
        - 450+ 
        - |link_pico2w_kit|

Du kannst sie auch einzeln über die folgenden Links kaufen.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - KOMPONENTENBESCHREIBUNG	
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

**Verdrahtung**

|wiring_motor|



**Code**

.. note::

    * Du kannst die Datei ``3.5_small_fan.ino`` im Verzeichnis ``pico-2w-kit-main/arduino/3.5_small_fan`` öffnen. 
    * Oder kopiere diesen Code in die **Arduino IDE**.
    * Vergiss nicht, das Board (Raspberry Pi Pico) und den richtigen Port auszuwählen, bevor du auf den **Upload** -Button klickst.


.. code-block:: arduino

    // Definiere die Pins, die mit der Motorsteuerung verbunden sind
    const int motor1A = 14; // Motorsteuerung Pin 1
    const int motor2A = 15; // Motorsteuerung Pin 2

    void setup() {
      // Initialisiere die Motorsteuerpins als AUSGANG
      pinMode(motor1A, OUTPUT); 
      pinMode(motor2A, OUTPUT); 
    }

    void loop() {
         // Drehe den Motor im Uhrzeigersinn
         clockwise();
         delay(1000); // Lass den Motor 1 Sekunde lang im Uhrzeigersinn drehen
    
        // Stoppe den Motor
        stopMotor();
        delay(1000); // Pause von 1 Sekunde
    
        // Drehe den Motor gegen den Uhrzeigersinn
        anticlockwise();
        delay(1000); // Lass den Motor 1 Sekunde lang gegen den Uhrzeigersinn drehen
    
        // Stoppe den Motor
        stopMotor();
        delay(1000); // Pause von 1 Sekunde
    }

        // Funktion, um den Motor im Uhrzeigersinn zu drehen
    void clockwise()
    {
        digitalWrite(motor1A, HIGH); // Setze motor1A auf HIGH
        digitalWrite(motor2A, LOW);  // Setze motor2A auf LOW
       // Diese Kombination lässt den Motor im Uhrzeigersinn drehen
    }

    // Funktion, um den Motor gegen den Uhrzeigersinn zu drehen
    void anticlockwise()
    {
        digitalWrite(motor1A, LOW);  // Setze motor1A auf LOW
        digitalWrite(motor2A, HIGH); // Setze motor2A auf HIGH
    // Diese Kombination lässt den Motor gegen den Uhrzeigersinn drehen
    }

    // Funktion, um den Motor zu stoppen
    void stopMotor()
    {
        digitalWrite(motor1A, LOW);  // Setze motor1A auf LOW
        digitalWrite(motor2A, LOW);  // Setze motor2A auf LOW
    // Das Setzen beider Pins auf LOW stoppt den Motor
    }

Nach dem Hochladen des Codes wird der Motor hin und her in einem regelmäßigen Muster rotieren.


**Code verstehen**

#. Steuerpins definieren:

   .. code-block:: arduino

        const int motor1A = 14; // Motorsteuerung Pin 1
        const int motor2A = 15; // Motorsteuerung Pin 2

#. Pin-Modi setzen:

   .. code-block:: arduino

        void setup() {
          pinMode(motor1A, OUTPUT); 
          pinMode(motor2A, OUTPUT); 
        }

#. Steuerung der Drehrichtung des Motors:

   * **Drehung im Uhrzeigersinn**: Setzt motor1 auf HIGH und motor2A auf LOW, wodurch der Motor im Uhrzeigersinn dreht.

   .. code-block:: arduino

        digitalWrite(motor1A, HIGH); // Setze motor1A auf HIGH
        digitalWrite(motor2A, LOW);  // Setze motor2A auf LOW

   * **Drehung gegen den Uhrzeigersinn**: Setzt motor1A auf LOW und motor2A auf HIGH, wodurch der Motor gegen den Uhrzeigersinn dreht.

   .. code-block:: arduino

        digitalWrite(motor1A, LOW);
        digitalWrite(motor2A, HIGH);

   * Lasse den Motor 1 Sekunde lang im Uhrzeigersinn laufen

   .. code-block:: arduino

        anticlockwise();
        delay(1000); 

   * Lasse den Motor 1 Sekunde lang gegen den Uhrzeigersinn laufen

   .. code-block:: arduino

        anticlockwise();
        delay(1000); 

   #. Den Motor stoppen:

   Setzt beide Eingänge auf LOW, um den Motor zu stoppen.

   .. code-block:: arduino

        digitalWrite(motor1A, LOW);  // Setze motor1A auf LOW
        digitalWrite(motor2A, LOW);  // Setze motor2A auf LOW
    
   Pause für 1 Sekunde

      .. code-block:: arduino

        stopMotor();
        delay(1000); 

**Weitere Erkundung**

* Geschwindigkeitssteuerung:

  Verwende Pulsweitenmodulation (PWM), um die Geschwindigkeit des Motors zu steuern, indem du den EN1 Pin an einen PWM-fähigen GPIO-Pin anschließt und den Tastgrad variierst.

* Sensoreinbindung:

  Integriere Sensoren (z.B. Endschalter, Encoder), um fortschrittlichere Motorsteuerungssysteme zu erstellen.

**Sicherheitsvorkehrungen**

* Stromversorgung:

  * Stelle sicher, dass die Spannung der externen Stromversorgung mit der Nennspannung des Motors übereinstimmt.
  * Versorge den Motor nicht direkt über den 3.3V Pin des Pico.

* Stromverbrauch:

  * Motoren können erheblichen Strom ziehen, insbesondere beim Starten oder bei einem Stillstand.
  * Stelle sicher, dass deine Stromversorgung den Strombedarf des Motors decken kann.

* Zurücksetzen des Pico:

  * In einigen Fällen kann der hohe Stromverbrauch des Motors zu Spannungseinbrüchen führen, die den Pico zum Zurücksetzen oder Trennen bringen.
  * Wenn du Probleme beim Hochladen von Code nach dem Betreiben des Motors hast, kannst du den Pico manuell zurücksetzen, indem du den RUN-Pin kurz mit GND verbindest.

  |wiring_run_reset|


**Fazit**

In dieser Lektion hast du gelernt, wie man einen DC-Motor mit dem Raspberry Pi Pico und dem TA6586 Motorsteuergerät steuert. Indem du die Eingänge des TA6586 steuerst, kannst du die Drehrichtung des Motors ändern. Dieses grundlegende Konzept ist in der Robotik, Automatisierung und vielen anderen Anwendungen, die Motoren betreffen, von entscheidender Bedeutung.
