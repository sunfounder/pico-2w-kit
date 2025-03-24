.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Vertiefen Sie sich in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Unterstützung unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_rgb:


2.4 Farbenfrohes Licht
======================

In dieser Lektion werden wir untersuchen, wie man verschiedene Farben mit einer RGB-LED und dem Raspberry Pi Pico 2 W erzeugt. Durch die Anpassung der Intensität der Rot-, Grün- und Blaukomponenten können wir Licht mischen, um eine breite Palette von Farben zu erzeugen. Dieses Konzept basiert auf der additiven Methode der Farbmischung.

**Was ist additive Farbmischung?**

Die additive Farbmischung besteht darin, verschiedene Lichtfarben zu kombinieren, um neue Farben zu erzeugen. Wenn Rot, Grün und Blau in verschiedenen Intensitäten kombiniert werden, können sie jede Farbe im sichtbaren Spektrum erzeugen. Zum Beispiel:

* **Rot + Grün = Gelb**
* **Rot + Blau = Magenta**
* **Grün + Blau = Cyan**
* **Rot + Grün + Blau = Weiß**

|img_rgb_mix|

* :ref:`cpn_rgb`

**Erforderliche Komponenten**

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
        - 3(1-330Ω, 2-220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_rgb`
        - 1
        - |link_rgb_led_buy|

**Schaltplan**

|sch_rgb|

Die PWM-Pins GP13, GP14 und GP15 steuern die Rot-, Grün- und Blaupins der RGB-LED und verbinden den gemeinsamen Kathodenpin mit GND. Dadurch kann die RGB-LED eine spezifische Farbe anzeigen, indem Licht auf diesen Pins mit unterschiedlichen PWM-Werten überlagert wird.



**Verdrahtung**

|img_rgb_pin|

Die RGB-LED hat 4 Pins: der längste Pin ist der gemeinsame Kathodenpin, der normalerweise mit GND verbunden wird; der linke Pin neben dem längsten Pin ist Rot; und die beiden Pins rechts sind Grün und Blau.

Wir verwenden einen höheren Widerstand für die rote LED, da sie typischerweise heller als die grünen und blauen LEDs bei gleichem Strom ist.


|wiring_rgb|


**Schreiben des Codes**

Hier können wir unsere Lieblingsfarbe in Zeichensoftware (wie Paint) wählen und sie mit der RGB-LED anzeigen.

.. note::

    * Sie können die Datei ``2.4_colorful_light.ino`` unter dem Pfad ``pico-2w-kit-main/arduino/2.4_colorful_light`` öffnen. 
    * Oder kopieren Sie diesen Code in die **Arduino IDE**.
    * Vergessen Sie nicht, das Board (Raspberry Pi Pico) und den richtigen Port vor dem Klicken auf den **Hochladen**-Knopf auszuwählen.




.. code-block:: Arduino

   // Definieren der GPIO-Pins, die mit der RGB-LED verbunden sind
   const int redPin = 13;   // Roter Pin
   const int greenPin = 14; // Grüner Pin
   const int bluePin = 15;  // Blauer Pin

   void setup() {
     // Initialisieren jedes RGB-LED-Pins als Ausgang
     pinMode(redPin, OUTPUT);
     pinMode(greenPin, OUTPUT);
     pinMode(bluePin, OUTPUT);
   }

   // Funktion zum Einstellen der Farbe
   void setColor(unsigned char red, unsigned char green, unsigned char blue) {
     analogWrite(redPin, red);
     analogWrite(greenPin, green);
     analogWrite(bluePin, blue);
   }

   void loop() {
     // Rote Farbe
     setColor(255, 0, 0);
     delay(1000);

     // Grüne Farbe
     setColor(0, 255, 0);
     delay(1000);

     // Blaue Farbe
     setColor(0, 0, 255);
     delay(1000);

     // Gelbe Farbe (Rot + Grün)
     setColor(255, 255, 0);
     delay(1000);

     // Cyan color (Green + Blue)
     setColor(0, 255, 255);
     delay(1000);

     // Magenta color (Red + Blue)
     setColor(255, 0, 255);
     delay(1000);

     // White color (Red + Green + Blue)
     setColor(255, 255, 255);
     delay(1000);

     // Turn off
     setColor(0, 0, 0);
     delay(1000);
   }

Nach dem Hochladen des Codes sollte die RGB-LED nacheinander rot, grün, blau, gelb, cyan, magenta, weiß durchlaufen und dann ausschalten, wobei jede Farbe eine Sekunde lang angezeigt wird.

**Verständnis des Codes**

#. Definition der Pins:

   Weisen Sie die GPIO-Pins zu, die mit den RGB-LED-Komponenten verbunden sind.

   .. code-block:: Arduino

        const int redPin = 13;
        const int greenPin = 14;
        const int bluePin = 15;

#. Initialisierung der Pins:

   Stellen Sie die RGB-LED-Pins als Ausgänge ein.

   .. code-block:: Arduino

        void setup() {
          pinMode(redPin, OUTPUT);
          pinMode(greenPin, OUTPUT);
          pinMode(bluePin, OUTPUT);
        }

#. Einstellen der Farbe:

   Die Funktion ``setColor`` verwendet PWM (Pulsweitenmodulation), um die Helligkeit jeder Farbkomponente anzupassen.

   .. code-block:: Arduino

        void setColor(unsigned char red, unsigned char green, unsigned char blue) {
          analogWrite(redPin, red);
          analogWrite(greenPin, green);
          analogWrite(bluePin, blue);
        }

#. Durchlaufen der Farben:

   In der Funktion ``loop()`` rufen wir ``setColor()`` mit verschiedenen Werten auf, um verschiedene Farben anzuzeigen, jede gefolgt von einer Verzögerung von 1 Sekunde.


   .. code-block:: Arduino

        void loop() {
          // Rote Farbe
          setColor(255, 0, 0);
          delay(1000);
          ...

          // Turn off
          setColor(0, 0, 0);
          delay(1000);
        }


**Experimentieren mit Farben**

Sie können Ihre eigenen Farben erstellen, indem Sie die Werte, die an ``setColor()`` übergeben werden, anpassen. Die Werte reichen von 0 (aus) bis 255 (volle Helligkeit). Zum Beispiel:

* Orange: setColor(255, 165, 0);
* Purple: setColor(128, 0, 128);

Um RGB-Werte für spezifische Farben zu finden, können Sie ein Farbauswahltool oder Software wie **Paint** verwenden.

**Fazit**

In dieser Lektion haben Sie gelernt, wie man eine RGB-LED mit dem Raspberry Pi Pico steuert und wie man verschiedene Farben durch Mischen von Rot, Grün und Blau erzeugt. Dieses Wissen ist grundlegend für Projekte, die LED-Anzeigen, Stimmungslichter oder jede Anwendung, die Farbsteuerung erfordert, involvieren.

