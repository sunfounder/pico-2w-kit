.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Vertiefen Sie sich mit anderen Enthusiasten in die Welt von Raspberry Pi, Arduino und ESP32.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unserem Team.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_tilt:

2.6 Neige es!
=======================

In dieser Lektion lernen wir, wie man einen Neigungsschalter mit dem Raspberry Pi Pico 2 W verwendet, um Änderungen der Ausrichtung zu erkennen. Ein Neigungsschalter ist ein einfaches Gerät, das erkennen kann, ob es aufrecht oder geneigt ist, was es nützlich für Anwendungen wie Bewegungserkennung, Orientierungssensorik oder als Auslöser basierend auf der Position macht.


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


Sie können sie auch einzeln über die untenstehenden Links kaufen.


.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - KOMPONENTENEINFÜHRUNG
        - MENGE
        - KAUF-LINK

    *   - 1
        - :ref:`cpn_pico_2w`
        - 1
        - |link_pico2w_buy|
    *   - 2
        - Micro USB Kabel
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
        - :ref:`cpn_tilt`
        - 1
        - 

**Schaltplan**

|sch_tilt|

* **Im aufrechten Zustand (Schalter geschlossen)**:

  * Der Neigungsschalter verbindet **3.3V** direkt mit **GP14**.
  * Der GPIO-Pin liest **HIGH** (1).

* **Bei Neigung (Schalter geöffnet)**:

  * Der Neigungsschalter trennt **3.3V** von **GP14**.
  * Der Pull-Down-Widerstand zieht **GP14** zu **GND**.
  * Der GPIO-Pin liest **LOW** (0).

**Verdrahtung**

|wiring_tilt|

**Schreiben des Codes**

.. note::

    * Sie können die Datei ``2.6_tilt_it.ino`` unter dem Pfad ``pico-2w-kit-main/arduino/2.4_colorful_light`` öffnen.
    * Oder kopieren Sie diesen Code in die **Arduino IDE**.
    * Vergessen Sie nicht, das Board (Raspberry Pi Pico) und den richtigen Port vor dem Klicken auf den **Upload**-Button auszuwählen.



.. code-block:: Arduino

   const int tiltPin = 14;  // GPIO-Pin, der mit dem Neigungsschalter verbunden ist

   void setup() {
     Serial.begin(115200);       // Serielle Überwachung mit 115200 Baud initialisieren
     pinMode(tiltPin, INPUT);    // Den Neigungsp

   void loop() {
     int tiltState = digitalRead(tiltPin);  // Den Zustand des Neigungsschalters lesen

     if (tiltState == HIGH) {
       Serial.println("The switch works!");
     }
     delay(100);  // Kleine Verzögerung, um die serielle Überwachung nicht zu überfluten
   }

Wenn der Code läuft und die serielle Überwachung offen ist, neigen Sie das Breadboard oder den Neigungsschalter.
Jedes Mal, wenn Sie den Schalter in die aufrechte Position neigen, sollte „Der Schalter funktioniert!“ im seriellen Monitor erscheinen.

**Verständnis des Codes**

#. Initialisierung der seriellen Kommunikation:

   Startet die serielle Kommunikation mit einer Baudrate von 115200. Dies ermöglicht es uns, Nachrichten auf den seriellen Monitor zu drucken.

   .. code-block:: Arduino

        Serial.begin(115200);

#. Einrichten des Neigungspins:

   Konfiguriert ``tiltPin`` (GP14) als Eingang, um den Zustand des Neigungsschalters zu lesen.

   .. code-block:: Arduino

        pinMode(tiltPin, INPUT);


#. Lesen des Zustands des Neigungsschalters:

   Liest den aktuellen Zustand des Neigungsschalters. Er wird ``HIGH`` sein, wenn er aufrecht steht, und ``LOW``, wenn er geneigt ist.

   .. code-block:: Arduino

        int tiltState = digitalRead(tiltPin);

#. Reaktion auf Neigung:

   Wenn der Neigungsschalter aufrecht (geschlossen) ist, wird eine Nachricht auf den seriellen Monitor gedruckt.

   .. code-block:: Arduino

        if (tiltState == HIGH) {
          Serial.println("The switch works!");
        }

**Weiteres Experimentieren**

* **Steuerung einer LED**: Modifizieren Sie den Code, um eine LED einzuschalten, wenn der Neigungsschalter aufrecht ist, und auszuschalten, wenn er geneigt ist.

  .. code-block:: Arduino

        const int tiltPin = 14;   // GPIO-Pin, der mit dem Neigungsschalter verbunden ist
        const int ledPin = 15;    // GPIO-Pin, der mit einer LED verbunden ist

        void setup() {
          Serial.begin(115200);
          pinMode(tiltPin, INPUT);
          pinMode(ledPin, OUTPUT);
        }

        void loop() {
          int tiltState = digitalRead(tiltPin);

          if (tiltState == HIGH) {
            Serial.println("The switch works!");
            digitalWrite(ledPin, HIGH);  // LED einschalten
          } else {
            digitalWrite(ledPin, LOW);   // LED ausschalten
          }
          delay(100);
        }

* **Empfindlichkeit einstellen**: Einige Neigungsschalter haben unterschiedliche Empfindlichkeitsstufen. Experimentieren Sie, indem Sie die Orientierung anpassen, um zu sehen, bei welchem Winkel der Schalter aktiviert wird.

**Fazit**

In dieser Lektion haben Sie gelernt, wie man einen Neigungsschalter mit dem Raspberry Pi Pico verwendet, um Änderungen der Ausrichtung zu erkennen. Diese grundlegende Fähigkeit ermöglicht es Ihnen, Projekte zu erstellen, die auf Bewegungen oder Positionen reagieren, wie Alarmanlagen, automatische Beleuchtung oder interaktive Geräte.

