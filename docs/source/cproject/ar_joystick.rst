.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein – gemeinsam mit anderen Technikbegeisterten.

    **Warum solltest du beitreten?**

    - **Fachkundige Unterstützung**: Erhalte Hilfe von unserer Community und unserem Team bei technischen Herausforderungen und Fragen nach dem Kauf.
    - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Sonderrabatte**: Profitiere von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festtagsaktionen und Gewinnspiele**: Nimm an Verlosungen und Sonderaktionen zu Feiertagen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und trete der Community noch heute bei!

.. _ar_joystick:

4.1 Werte eines Joysticks auslesen
=====================================

In dieser Lektion lernen wir, wie man einen **Joystick** mit dem Raspberry Pi Pico 2 W verwendet, um analoge Werte auszulesen und Tastenbetätigungen zu erkennen. Ein Joystick ist ein weit verbreitetes Eingabegerät, das Bewegungen entlang zweier Achsen (X und Y) ermöglicht und oft eine zusätzliche Taste bietet, wenn er nach unten gedrückt wird (Z-Achse).

* :ref:`cpn_joystick`

**Benötigte Komponenten**

Für dieses Projekt benötigen wir folgende Komponenten.

Es ist auf jeden Fall praktisch, ein komplettes Kit zu kaufen. Hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ENTHALTENE TEILE
        - KAUFLINK
    *   - Pico 2 W Starter Kit	
        - 450+
        - |link_pico2w_kit|

Alternativ kannst du die Komponenten auch einzeln über die folgenden Links kaufen.

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
        - :ref:`cpn_resistor`
        - 1 (10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_joystick`
        - 1
        - 

**Funktionsweise des Joysticks**

Ein typisches Joystick-Modul besteht aus zwei Potentiometern, die senkrecht zueinander angeordnet sind:

* **X-Achsen-Potentiometer**: Misst die Bewegung nach links und rechts.
* **Y-Achsen-Potentiometer**: Misst die Bewegung nach oben und unten.
* **Z-Achse (Schalter)**: Eine digitale Taste, die aktiviert wird, wenn der Joystick nach unten gedrückt wird.

Durch das Auslesen der analogen Werte der X- und Y-Achse kann die Position des Joysticks bestimmt werden. Der Z-Achsen-Schalter ermöglicht es, das Drücken des Joysticks zu erkennen.

**Schaltplan**

|sch_joystick|

Der SW-Pin ist mit einem 10KΩ-Pull-up-Widerstand verbunden, um einen stabilen High-Zustand sicherzustellen, wenn der Joystick nicht gedrückt wird. Andernfalls könnte der SW-Pin in einem undefinierten Zustand sein und zufällige Werte zwischen 0 und 1 liefern.

**Verdrahtung**

|wiring_joystick|

**Code schreiben**

.. note::

    * Du kannst die Datei ``4.1_toggle_the_joystick.ino`` im Verzeichnis ``pico-2w-kit-main/arduino/4.1_toggle_the_joystick`` öffnen. 
    * Oder kopiere diesen Code in die **Arduino IDE**.
    * Vergiss nicht, das Board (Raspberry Pi Pico) und den richtigen Port auszuwählen, bevor du auf die **Upload**-Schaltfläche klickst.

.. code-block:: arduino

   // Pins definieren
   const int joystickX = 26;  // GP26 (ADC0) verbunden mit VRx
   const int joystickY = 27;  // GP27 (ADC1) verbunden mit VRy
   const int joystickSW = 22; // GP22 verbunden mit SW (Taste)

   void setup() {
     // Serielle Kommunikation mit 115200 Baud starten
     Serial.begin(115200);

     // Joystick-Taste als Eingang mit internem Pull-up-Widerstand setzen
     pinMode(joystickSW, INPUT_PULLUP);
   }

   void loop() {
     // Analoge Werte des Joysticks auslesen
     int xValue = analogRead(joystickX);
     int yValue = analogRead(joystickY);

     // Zustand der Joystick-Taste auslesen
     int buttonState = digitalRead(joystickSW);

     // Werte im seriellen Monitor ausgeben
     Serial.print("X: ");
     Serial.print(xValue);
     Serial.print(" | Y: ");
     Serial.print(yValue);
     Serial.print(" | Button: ");
     Serial.println(buttonState == LOW ? "Gedrückt" : "Nicht gedrückt");

     delay(500); // 500 ms warten, bevor die nächste Messung erfolgt
   }

Beim Ausführen des Codes und geöffnetem seriellen Monitor:

* Bewege den Joystick in verschiedene Richtungen (links, rechts, oben, unten) und beobachte, wie sich die X- und Y-Werte entsprechend ändern.
* Drücke die Joystick-Taste (Z-Achse) und überprüfe, ob sich der Status von "Nicht gedrückt" auf "Gedrückt" ändert.


**Verständnis des Codes**

#. Pins definieren:

   * ``joystickX`` und ``joystickY``: Analoge Pins, die mit den X- und Y-Achsen des Joysticks verbunden sind.
   * ``joystickSW``: Digitaler Pin, der mit der Joystick-Taste (Z-Achse) verbunden ist.

#. Setup-Funktion:

   * Initialisiert die serielle Kommunikation für Debugging und Monitoring.
   * Setzt den Joystick-Tasten-Pin als Eingang mit internem Pull-up-Widerstand zur Stabilisierung des Signals.

   .. code-block:: arduino

        void setup() {
          Serial.begin(115200);
          pinMode(joystickSW, INPUT_PULLUP);
        }

#. ``loop()``-Funktion:

   * Analoge Werte auslesen:
     
     Die aktuelle Position des Joysticks auf der X- und Y-Achse wird ausgelesen. Die Werte reichen von 0 bis 1023 und entsprechen den analogen Spannungspegeln.

     .. code-block:: arduino

           int xValue = analogRead(joystickX);
           int yValue = analogRead(joystickY);

   * Tastenstatus auslesen:

     Prüft, ob der Joystick gedrückt ist (``LOW`` = gedrückt, ``HIGH`` = nicht gedrückt).

     .. code-block:: arduino

           int buttonState = digitalRead(joystickSW);

   * Daten im seriellen Monitor ausgeben:

     Gibt die aktuellen X- und Y-Werte sowie den Tastenstatus aus.

     .. code-block:: arduino

       Serial.print("X: ");
       Serial.print(xValue);
       Serial.print(" | Y: ");
       Serial.print(yValue);
       Serial.print(" | Button: ");
       Serial.println(buttonState == LOW ? "Pressed" : "Released");

**Weitere Erkundungen** 

* Zuordnung analoger Werte zu Aktionen:
  
  * Nutze die Position des Joysticks, um Servos, LEDs oder andere Aktuatoren entsprechend der Bewegungsrichtung und -stärke zu steuern.

* Implementierung einer Totzone:
  
  * Implementiere eine Totzone um die Mittelstellung, um unbeabsichtigte Bewegungen aufgrund kleiner Joystick-Schwankungen zu verhindern.

* Kombination mit anderen Sensoren:
  
  * Integriere den Joystick mit anderen Sensoren (z. B. Beschleunigungssensoren, Abstandssensoren), um komplexere Interaktionen zu ermöglichen.

* Erstellung eines Game-Controllers:
  
  * Verwende mehrere Joysticks und Tasten, um einen individuell angepassten Game-Controller für einfache Spiele oder die Steuerung von Robotern zu entwickeln.

**Fazit**

In dieser Lektion hast du gelernt, wie man einen Joystick mit dem Raspberry Pi Pico verbindet, um analoge Werte der X- und Y-Achsen auszulesen und Tastenbetätigungen auf der Z-Achse zu erkennen. Diese Konfiguration kann als Eingabemethode für verschiedene Projekte genutzt werden, darunter Fernsteuerungen, Robotik und interaktive Installationen. Durch das Verständnis der Joystick-Werte und deren Interpretation kannst du reaktionsschnelle und dynamische Anwendungen erstellen.
