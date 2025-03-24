.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in Raspberry Pi, Arduino und ESP32 ein und lerne gemeinsam mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Experten-Support**: Lösche nach dem Verkauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitig Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Sonderrabatte**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nimm an Gewinnspielen und saisonalen Aktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _ar_micro:

2.8 - Drücke sanft
==========================

|img_micro_switch|

In dieser Lektion lernen wir, wie man einen **Mikroschalter** (auch als Endschalter bekannt) mit dem Raspberry Pi Pico 2 W verwendet, um zu erkennen, wann er gedrückt oder losgelassen wird. Mikroschalter werden häufig in Geräten wie Mikrowellentüren, Druckerabdeckungen oder als Endanschläge in 3D-Druckern verwendet, weil sie zuverlässig sind und häufige Betätigungen aushalten können.

* :ref:`cpn_micro_switch`

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


Du kannst die Teile auch einzeln über die folgenden Links kaufen.


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
        - :ref:`cpn_resistor`
        - 1 (10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_capacitor`
        - 1 (104)
        - |link_capacitor_buy|
    *   - 7
        - :ref:`cpn_micro_switch`
        - 1
        - 

**Den Mikroschalter verstehen**

Ein Mikroschalter hat in der Regel drei Pins:

|img_micro_switch|

- **Common (C)**: Der mittlere Pin.
- **Normally Open (NO)**: Wird mit dem Common-Pin verbunden, wenn der Schalter **gedrückt** wird.
- **Normally Closed (NC)**: Wird mit dem Common-Pin verbunden, wenn der Schalter **nicht gedrückt** wird.

Indem der Schalter korrekt angeschlossen wird, können wir erkennen, wann er gedrückt wird, indem wir das Spannungsniveau an einem GPIO-Pin ablesen.

**Schaltplan**

|sch_limit_sw|

Standardmäßig ist GP14 niedrig, und wenn der Schalter gedrückt wird, ist GP14 hoch.

Der Zweck des 10K-Widerstands ist es, GP14 während des Druckens niedrig zu halten.

Wenn du einen mechanischen Schalter drückst, können die Kontakte prellen, was zu mehreren schnellen Übergängen zwischen offenen und geschlossenen Zuständen führt. Der zwischen GP14 und GND geschaltete Kondensator hilft, dieses Rauschen herauszufiltern.

* **Schalter nicht gedrückt**:

  * Der **Common (C)** Pin ist mit dem **NC** Pin verbunden, der mit **GND** verbunden ist.
  * **GP14** liest **LOW** (0V).

* **Schalter gedrückt**:

  * Der **Common (C)** Pin ist mit dem **NO** Pin verbunden, der mit **3.3V** verbunden ist.
  * **GP14** liest **HIGH** (3.3V).

**Verdrahtung**

|wiring_limit_sw|


**Code schreiben**

Wir schreiben ein einfaches Programm, das erkennt, wann der Mikroschalter gedrückt wird und eine Nachricht an den Serial Monitor ausgibt.

.. note::

    * Du kannst die Datei ``2.8_press_gently.ino`` im Verzeichnis ``pico-2w-kit-main/arduino/2.8_press_gently`` öffnen. 
    * Oder kopiere diesen Code in die **Arduino IDE**.
    * Vergiss nicht, das Board (Raspberry Pi Pico) und den richtigen Port auszuwählen, bevor du auf den **Upload**-Button klickst.

    

.. code-block:: Arduino

   const int switchPin = 14;   // GPIO-Pin, der mit dem Mikroschalter verbunden ist
   int switchState = 0;

   void setup() {
     Serial.begin(115200);       // Initialisiere den Serial Monitor mit 115200 Baud
     pinMode(switchPin, INPUT);  // Setze den Schalterpin als Eingang
   }

   void loop() {
     switchState = digitalRead(switchPin);  // Lese den Zustand des Schalters

     if (switchState == HIGH) {
       Serial.println("The switch is pressed!");
     } else {
       Serial.println("The switch is not pressed.");
     }
     delay(200);  // Kleine Verzögerung, um das Überfluten des Serial Monitors zu vermeiden
   }

Wenn der Code läuft und der Serial Monitor geöffnet ist, drücke und lasse den Mikroschalter los.
Der Serial Monitor zeigt "Der Schalter ist gedrückt!" an, wenn du den Schalter drückst, und "Der Schalter ist nicht gedrückt." wenn du ihn loslässt.

**Code verstehen**

#. Initialisierung der seriellen Kommunikation:

   Die serielle Kommunikation wird mit einer Baudrate von 115200 gestartet. Dies ermöglicht es uns, Nachrichten an den Serial Monitor zu senden.

   .. code-block:: Arduino

        Serial.begin(115200);

#. Setup der Schalterpin:

   Konfiguriert switchPin (GP14) als Eingang, um den Zustand des Schalters zu lesen.

   .. code-block:: Arduino

        pinMode(switchPin, INPUT);

#. Ablesen des Schalterzustands:

   Liest den aktuellen Zustand des Schalters. Es wird HIGH sein, wenn er gedrückt wird, und LOW, wenn er nicht gedrückt wird.

   .. code-block:: Arduino

        switchState = digitalRead(switchPin);

#. Reaktion auf den Schalterdruck:

   Gibt eine Nachricht basierend darauf aus, ob der Schalter gedrückt ist oder nicht.

   .. code-block:: Arduino

        if (switchState == HIGH) {
          Serial.println("The switch is pressed!");
        } else {
          Serial.println("The switch is not pressed.");
        }


**Alternative: Verwendung des internen Pull-Up-Widerstands**

Wenn du den Schaltkreis vereinfachen und die Anzahl der Komponenten reduzieren möchtest, kannst du den internen Pull-Up-Widerstand des Pico verwenden.

* GP14 ist mit GND verbunden, wenn der Schalter gedrückt ist, also liest es LOW (0).
* GP14 liest HIGH, wenn der Schalter nicht gedrückt wird, aufgrund des internen Pull-Up-Widerstands.

* Schaltkreis-Modifikationen:

  Entferne den externen 10KΩ-Widerstand und den Kondensator.

* Mikroschalter-Verbindungen:

  * **Common (C)-Terminal**: Verbinde es mit GP14 auf dem Pico.
  * **Normally Open (NO)-Terminal**: Verbinde es mit GND auf dem Pico.
  * **Normally Closed (NC)-Terminal**: Lasse es unverbunden.

* Code-Modifikationen:

  .. code-block:: Arduino

        const int switchPin = 14;   // GPIO-Pin, der mit dem Mikroschalter verbunden ist
        int switchState = 0;

        void setup() {
          Serial.begin(115200);          // Initialisiere den Serial Monitor mit 115200 Baud
          pinMode(switchPin, INPUT_PULLUP);  // Aktiviere den internen Pull-Up-Widerstand
        }

        void loop() {
          switchState = digitalRead(switchPin);  // Lese den Zustand des Schalters

          if (switchState == LOW) {
            Serial.println("The switch is pressed!");
          } else {
            Serial.println("The switch is not pressed.");
          }
          delay(200);  // Kleine Verzögerung, um das Überfluten des Serial Monitors zu vermeiden
        }

**Entprellen des Schalters**

Mechanische Schalter können aufgrund der prellenden Kontakte Rauschen erzeugen. Um die Zuverlässigkeit deiner Messungen zu verbessern, kannst du Software-Entprellung implementieren.

.. code-block:: Arduino

    const int switchPin = 14;   // GPIO-Pin, der mit dem Mikroschalter verbunden ist
    int switchState = 0;        // Aktueller Zustand des Schalters
    int lastSwitchState = HIGH; // Vorheriger Zustand des Schalters
    unsigned long lastDebounceTime = 0;  // Zeit des letzten Zustandswechsels
    unsigned long debounceDelay = 50;    // Entprellzeit in Millisekunden

    void setup() {
      Serial.begin(115200);
      pinMode(switchPin, INPUT_PULLUP);
    }

    void loop() {
      int reading = digitalRead(switchPin);

      if (reading != lastSwitchState) {
        lastDebounceTime = millis();
      }

      if ((millis() - lastDebounceTime) > debounceDelay) {
        if (reading != switchState) {
          switchState = reading;

          if (switchState == LOW) {
            Serial.println("The switch is pressed!");
          } else {
            Serial.println("The switch is not pressed.");
          }
        }
      }

      lastSwitchState = reading;
    }

* Überprüft, ob sich die Lesung vom letzten Zustand geändert hat.
* Wenn ja, wird ``lastDebounceTime`` zurückgesetzt.
* Wenn die Lesung nach der Entprellzeit stabil bleibt, wird der neue Zustand als gültig betrachtet.

**Fazit**

In dieser Lektion hast du gelernt, wie man einen Mikroschalter mit dem Raspberry Pi Pico verwendet, um zu erkennen, wann er gedrückt oder losgelassen wird. Du hast auch gesehen, wie man einen Pull-Down-Widerstand im Schaltkreis implementiert, um zuverlässige Messwerte zu gewährleisten, und wie man den internen Pull-Up-Widerstand verwendet, um den Schaltkreis zu vereinfachen. Außerdem hast du das Entprellen gelernt, um das Rauschen von mechanischen Schaltern zu verarbeiten.

**Weiterführende Exploration**

* **LED steuern**: Ändere den Code, um eine LED einzuschalten, wenn der Schalter gedrückt wird.
* **Mehrere Schalter**: Versuche, mehr Mikroschalter hinzuzufügen, um verschiedene Eingaben zu erkennen.
* **Zähler erstellen**: Zähle, wie oft der Schalter gedrückt wurde, und zeige es an.
