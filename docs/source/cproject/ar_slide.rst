.. note::
      Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Vertiefen Sie sich mit anderen Enthusiasten in die Welt von Raspberry Pi, Arduino und ESP32.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unserem Team.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_slide:

2.7 Umschalten Links und Rechts
=====================================

In dieser Lektion lernen wir, wie man mit dem Raspberry Pi Pico 2 W einen **Schiebeschalter** verwendet, um dessen Position (links oder rechts) zu erkennen und darauf basierend Aktionen durchzuführen. Ein Schiebeschalter ist ein einfaches mechanisches Gerät, das den gemeinsamen (mittleren) Pin je nach Position mit einem der beiden äußeren Pins verbindet.

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
        - 1 (10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_capacitor`
        - 1 (104)
        - |link_capacitor_buy|
    *   - 7
        - :ref:`cpn_slide_switch`
        - 1
        - 

**Verständnis des Schiebeschalters**

|img_slide|

Ein Schiebeschalter hat drei Pins:

- **Pin 1**: Verbunden, wenn der Schalter nach einer Seite (z. B. links) umgelegt wird
- **Pin 2**: Gemeinsamer Pin (mittlerer Pin)
- **Pin 3**: Verbunden, wenn der Schalter nach der anderen Seite (z. B. rechts) umgelegt wird

Durch das Lesen der Spannung am gemeinsamen Pin können wir die Position des Schalters bestimmen.

**Schaltplan**

|sch_slide|

GP14 erhält ein unterschiedliches Niveau, wenn Sie den Schiebeschalter nach rechts oder links umlegen.

Der Zweck des 10K-Widerstands besteht darin, GP14 während des Umschaltens niedrig zu halten (nicht ganz nach links und nicht ganz nach rechts umgelegt).

Wenn Sie den Schalter umlegen, können die mechanischen Kontakte schnelle, verrauschte Signale verursachen, bekannt als "Prellen". Der zwischen GP14 und GND angeschlossene Kondensator hilft, diese schnellen Schwankungen zu filtern und ein saubereres Signal bereitzustellen.

* Schalter nach rechts umgelegt:

  * Pin 2 (GP14) ist über Pin 1 mit **3.3V** verbunden.
  * Der GPIO-Pin liest **HIGH** (1).

* Schalter nach links umgelegt:

  * Pin 2 (GP14) ist über Pin 3 mit **GND** verbunden.
  * Der GPIO-Pin liest **LOW** (0).

* Schalter in Mittelposition:

  * Pin 2 (GP14) ist nicht mit **3.3V** oder **GND** verbunden.
  * Der Pull-Down-Widerstand hält den GPIO-Pin auf **LOW** (0).
  * Der Kondensator hilft, das Schalterprellen zu reduzieren (Geräusche durch mechanische Bewegung).



**Verdrahtung**

|wiring_slide|

**Schreiben des Codes**

.. note::

    * Sie können die Datei ``2.7_toggle_left_right.ino`` unter dem Pfad ``pico-2w-kit-main/arduino/2.7_toggle_left_right`` öffnen.
    * Oder kopieren Sie diesen Code in die **Arduino IDE**.
    * Vergessen Sie nicht, das Board (Raspberry Pi Pico) und den richtigen Port vor dem Klicken auf den **Upload**-Button auszuwählen.

.. code-block:: Arduino

   const int switchPin = 14;   // GPIO-Pin, der mit dem Schiebeschalter verbunden ist
   int switchState = 0;

   void setup() {
     Serial.begin(115200);       // Serielle Überwachung mit 115200 Baud initialisieren
     pinMode(switchPin, INPUT);  // Den Schalterpin als Eingang setzen
   }

   void loop() {
     switchState = digitalRead(switchPin);  // Den Zustand des Schalters lesen

     if (switchState == HIGH) {
       Serial.println("ON");   // Schalter nach links umgelegt
     } else {
       Serial.println("OFF");  // Schalter nach rechts umgelegt
     }
     delay(200);  // Kleine Verzögerung, um die serielle Überwachung nicht zu überfluten
   }

Wenn der Code ausgeführt wird und die serielle Überwachung offen ist:

Druckt "ON", wenn der Schalter nach links umgelegt wird und "OFF", wenn er nach rechts umgelegt wird.


**Verständnis des Codes**

#. Initialisierung der seriellen Kommunikation:

   Startet die serielle Kommunikation mit einer Baudrate von 115200. Dies ermöglicht es uns, Nachrichten auf den Seriellen Monitor zu drucken.

   .. code-block:: Arduino

        Serial.begin(115200);


#. Einrichten des Schalterpins:

   Konfiguriert den Schalterpin (GP14) als Eingang, um den Schalterzustand zu lesen.

   .. code-block:: Arduino

        pinMode(switchPin, INPUT);


#. Lesen des Schalterzustands:

   Liest den aktuellen Zustand des Schalters. Er ist HIGH, wenn nach rechts umgelegt, und LOW, wenn nach links oder in der Mittelposition umgelegt, wegen des Pull-Down-Widerstands.

   .. code-block:: Arduino

        switchState = digitalRead(switchPin);


#. Reaktion auf die Schalterposition:

   Druckt "ON", wenn der Schalter nach links (GP14 liest HIGH) und "OFF", wenn nach rechts (GP14 liest LOW) umgelegt wird.

   .. code-block:: Arduino

        if (switchState == HIGH) {
          Serial.println("ON");
        } else {
          Serial.println("OFF");
        }

**Alternative: Verwendung des internen Pull-Up-Widerstands**

Wenn Sie den Schaltkreis vereinfachen und die Anzahl der Komponenten reduzieren möchten, können Sie den internen Pull-Up-Widerstand des Pico verwenden. Bitte beachten Sie jedoch, dass traditionelle Arduino-Boards keine internen Pull-Down-Widerstände unterstützen, sondern nur interne Pull-Up-Widerstände. Der Raspberry Pi Pico unterstützt INPUT_PULLDOWN, aber in der Arduino-Umgebung kann die Unterstützung variieren. Für dieses Beispiel verwenden wir INPUT_PULLUP.

* Schaltkreisänderungen:

  * Entfernen Sie den externen 10KΩ-Widerstand und Kondensator.
  * Schiebeschalterverbindungen:

    * Pin 1: Verbinden Sie mit GND am Pico.
    * Pin 2: Verbinden Sie mit GP14 am Pico.
    * Pin 3: Lassen Sie unverbunden oder verbinden Sie mit GND (da wir den internen Pull-Up verwenden).

* Codeänderungen:

  .. code-block:: Arduino

        const int switchPin = 14;   // GPIO-Pin, der mit dem Schiebeschalter verbunden ist
        int switchState = 0;

        void setup() {
          Serial.begin(115200);          // Serielle Überwachung mit 115200 Baud initialisieren
          pinMode(switchPin, INPUT_PULLUP);  // Internen Pull-Up-Widerstand aktivieren
        }

        void loop() {
          switchState = digitalRead(switchPin);  // Den Zustand des Schalters lesen

          if (switchState == LOW) {
            Serial.println("ON");    // Schalter mit GND verbunden, nach rechts umgelegt
          } else {
            Serial.println("OFF");   // Schalter nicht verbunden, liest HIGH wegen Pull-Up
          }
          delay(200);  // Kleine Verzögerung, um die serielle Überwachung nicht zu überfluten
        }

**Fazit**

In dieser Lektion haben Sie gelernt, wie man einen Schiebeschalter mit dem Raspberry Pi Pico verwendet, um dessen Position zu erkennen und darauf basierende Aktionen durchzuführen. Sie haben auch gesehen, wie man einen Pull-Down-Widerstand im Schaltkreis implementiert, um zuverlässige Ablesungen zu gewährleisten, und wie man den internen Pull-Up-Widerstand verwendet, um den Schaltkreis zu vereinfachen.

**Weitere Erkundungen**

* **Steuerung einer LED**: Modifizieren Sie den Code, um eine LED basierend auf der Schalterposition ein- oder auszuschalten.
* **Mehrere Schalter**: Versuchen Sie, mehr Schalter hinzuzufügen, um verschiedene Aktionen zu steuern.
* **Entprellen**: Implementieren Sie eine Software-Entprellung, um eventuelles restliches Schalterprellen zu handhaben.
