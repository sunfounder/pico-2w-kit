.. note:: 
   
    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein, zusammen mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unserem Team.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_pump:

3.6 Eine Wasserpumpe steuern
================================

In dieser Lektion lernen wir, wie man eine **kleine Wasserpumpe** mit dem Raspberry Pi Pico 2 W und einem **TA6586 Motortreiber** steuert. Eine kleine Zentrifugalpumpe kann für Projekte wie automatische Bewässerungssysteme für Pflanzen oder die Erstellung von Miniaturwassermerkmalen verwendet werden. Die Steuerung der Pumpe ähnelt der Steuerung eines Gleichstrommotors, da dieselben Prinzipien verwendet werden.

* :ref:`cpn_pump`
* :ref:`cpn_motor`
* :ref:`cpn_ta6586`
* :ref:`cpn_power_module`

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
        - :ref:`cpn_ta6586`
        - 1
        - 
    *   - 6
        - :ref:`cpn_lipo_charger`
        - 1
        -  
    *   - 7
        - Power Pack
        - 1
        -  
    *   - 8
        - :ref:`cpn_pump`
        - 1
        -  


**Schaltplan**

|sch_pump|


**Verdrahtung**

.. note::

    * Da die Pumpe einen hohen Strom benötigt, verwenden wir hier aus Sicherheitsgründen ein Li-po-Ladegerät, um den Motor zu betreiben.
    * Stellen Sie sicher, dass Ihr Li-po-Ladegerät wie im Diagramm gezeigt angeschlossen ist, da sonst ein Kurzschluss Ihr Power Pack und die Schaltung beschädigen könnte.


|wiring_pump|

**Code**

.. note::

    * Sie können die Datei ``3.6_pumping.ino`` unter dem Pfad ``pico-2w-kit-main/arduino/3.6_pumping`` öffnen. 
    * Oder kopieren Sie diesen Code in die **Arduino IDE**.
    * Vergessen Sie nicht, das Board (Raspberry Pi Pico) und den richtigen Port auszuwählen, bevor Sie auf den **Hochladen**-Knopf klicken.

    
.. code-block:: Arduino

    const int motor1A = 14; // Motorsteuerungspin 1
    const int motor2A = 15; // Motorsteuerungspin 2

    void setup() {
      // Motorsteuerungspins als OUTPUT festlegen
      pinMode(motor1A, OUTPUT); // Konfigurieren von motor1A als Ausgangspin
      pinMode(motor2A, OUTPUT); // Konfigurieren von motor2A als Ausgangspin
    }

    void loop() {
      // Den Motor in Uhrzeigersinn drehen
      digitalWrite(motor1A, HIGH); // Setze motor1A auf HIGH (aktiviert eine Seite des Motors)
      digitalWrite(motor2A, LOW);  // Setze motor2A auf LOW (deaktiviert die gegenüberliegende Seite des Motors)
    }




Nach dem Start des Codes beginnt die Pumpe zu arbeiten und Sie werden gleichzeitig Wasser aus dem Schlauch fließen sehen.
* Dieser Zyklus wiederholt sich unendlich.
* Wenn zunächst kein Wasser fließt, stellen Sie sicher, dass die Pumpe untergetaucht ist und sich keine Luftblasen im Schlauch befinden.


**Sicherheitsvorkehrungen**

* Wasser und Elektrizität:

  * Seien Sie äußerst vorsichtig, Wasser fern von Pico und anderen elektronischen Komponenten zu halten.
  * Stellen Sie sicher, dass alle Verbindungen sicher und gegebenenfalls isoliert sind.

* Stromversorgung:

  * Verwenden Sie eine Stromquelle, die den Spannungsanforderungen der Pumpe entspricht (typischerweise 3V-6V).
  * Schließen Sie die Pumpe nicht direkt an den 3.3V-Pin des Pico an.

* Stromverbrauch:

  * Pumpen können einen erheblichen Strom ziehen.
  * Stellen Sie sicher, dass Ihre Stromquelle den Strombedarf der Pumpe bewältigen kann.

* Zurücksetzen des Pico:

  Wenn Sie Probleme beim Hochladen von Code nach dem Betrieb der Pumpe haben, können Sie den Pico manuell zurücksetzen, indem Sie den RUN-Pin kurzzeitig mit GND verbinden.

  |wiring_run_reset|

**Weiterführende Erkundungen**

* Automatisierte Pflanzenbewässerung:

  Integrieren Sie Bodenfeuchtigkeitssensoren, um den Bewässerungsprozess basierend auf der Trockenheit des Bodens zu automatisieren.

* PWM-Geschwindigkeitskontrolle:

  Verwenden Sie die Pulsweitenmodulation (PWM), um die Geschwindigkeit der Pumpe durch Veränderung der Spannung zu steuern.

* Zeitsteuerung und Planung:

  Implementieren Sie komplexere Zeitsteuerungen mit Echtzeituhren oder Planern.

**Fazit**

In dieser Lektion haben Sie gelernt, wie man eine kleine Wasserpumpe mit dem Raspberry Pi Pico und dem TA6586 Motortreiber steuert. Diese Technik kann in verschiedenen Projekten wie automatisierten Bewässerungssystemen, Brunnen oder Hydrokulturanlagen verwendet werden.
