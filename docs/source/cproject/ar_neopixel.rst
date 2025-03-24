Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 zusammen mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nehmen Sie an Giveaways und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

.. _ar_neopixel:

3.3 Steuerung eines RGB-LED-Streifens
===========================================================

In dieser Lektion lernen wir, wie man einen **RGB-LED-Streifen** (speziell den Typ WS2812) mit dem Raspberry Pi Pico 2 W und MicroPython steuert.

Der WS2812 ist ein intelligenter LED, der einen Steuerkreis und einen RGB-Chip in einem 5050-LED-Gehäuse integriert. Jede LED hat ihren eigenen eingebauten Controller, was uns ermöglicht, jede LED einzeln über eine einzige Datenleitung zu steuern. Das bedeutet, dass wir die Farbe und Helligkeit jeder LED auf dem Streifen unabhängig ändern können.



    * :ref:`cpn_ws2812`

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
        - :ref:`cpn_ws2812`
        - 1
        - |link_ws2812_buy|

**Schaltplan**

|sch_ws2812|

**Verdrahtung**

|wiring_ws2812|

Seien Sie vorsichtig mit dem Stromverbrauch. Während der VBUS-Pin des Pico Strom für eine kleine Anzahl von LEDs (wie 8) liefern kann, kann die Verwendung mehrerer LEDs ein externes Netzteil erforderlich machen, um eine Überlastung des Pico zu vermeiden.


**Schreiben des Codes**

.. note::

    * Sie können die Datei ``3.3_rgb_led_strip.ino`` unter dem Pfad ``pico-2w-kit-main/arduino/3.3_rgb_led_strip`` öffnen.
    * Oder kopieren Sie diesen Code in die **Arduino IDE**.
    * Wählen Sie dann das Raspberry Pi Pico-Board und den richtigen Port, bevor Sie auf den Upload-Button klicken.
    * Die ``Adafruit_NeoPixel``-Bibliothek wird hier verwendet, Sie können sie aus dem **Library Manager** installieren.

      .. image:: img/lib_neopixel.png

.. code-block:: arduino

  #include <Adafruit_NeoPixel.h>

  #define PIXEL_PIN    0    // Digitaler IO-Pin, der mit den NeoPixels verbunden ist
  #define PIXEL_COUNT  8    // Anzahl der NeoPixels

  // Deklariere unser NeoPixel-Streifenobjekt
  Adafruit_NeoPixel strip(PIXEL_COUNT, PIXEL_PIN, NEO_GRB + NEO_KHZ800);

  void setup() {
    strip.begin();           // Initialisiere die NeoPixel-Bibliothek
    strip.show();            // Schalte alle Pixel so schnell wie möglich AUS
  }

  void loop() {
    // Setze die Farbe jedes Pixels
    strip.setPixelColor(0, strip.Color(255, 0, 0));   // Rot
    strip.setPixelColor(1, strip.Color(0, 255, 0));   // Grün
    strip.setPixelColor(2, strip.Color(0, 0, 255));   // Blau
    strip.setPixelColor(3, strip.Color(255, 255, 0)); // Gelb
    strip.setPixelColor(4, strip.Color(0, 255, 255)); // Cyan
    strip.setPixelColor(5, strip.Color(255, 0, 255)); // Magenta
    strip.setPixelColor(6, strip.Color(255, 255, 255)); // Weiß
    strip.setPixelColor(7, strip.Color(0, 0, 0));     // Aus

    strip.show();  // Aktualisiere den Streifen mit neuen Inhalten
    delay(1000);   // Warte eine Sekunde

    // Schalte alle Pixel aus
    strip.clear();
    strip.show();
    delay(1000);   // Warte eine Sekunde
  }

Nach dem Hochladen des Codes sollten Sie sehen, dass die LEDs mit unterschiedlichen Farben aufleuchten, eine Sekunde lang eingeschaltet bleiben und dann eine Sekunde lang ausgeschaltet sind.

**Code verstehen**

#. Bibliothek einbinden:

   .. code-block:: arduino
    
      #include <Adafruit_NeoPixel.h>

#. Konstanten definieren:

   * ``PIXEL_PIN``: Der GPIO-Pin, der mit dem Dateneingang des LED-Streifens verbunden ist (GP0).
   * ``PIXEL_COUNT``: Die Anzahl der LEDs auf dem Streifen.

#. Streifen initialisieren:

   ``NEO_GRB + NEO_KHZ800``: Gibt die Farbreihenfolge und die Kommunikationsgeschwindigkeit an.

   .. code-block:: arduino
    
      Adafruit_NeoPixel strip(PIXEL_COUNT, PIXEL_PIN, NEO_GRB + NEO_KHZ800);
      
#. In der ``setup()``-Funktion:

   * ``strip.begin()``: Initialisiert die NeoPixel-Bibliothek.
   * ``strip.show()``: Stellt sicher, dass alle Pixel ausgeschaltet sind.

#. In der ``loop()`` -Funktion:

   * ``strip.setPixelColor(index, color)``: Stellt die Farbe eines bestimmten Pixels ein.
   * ``strip.Color(r, g, b)``: Erstellt einen 24-Bit-Farbwert aus den Rot-, Grün- und Blaukomponenten (0-255).
   * ``strip.show()``: Sendet die aktualisierten Farbdaten an den Streifen.
   * ``strip.clear()``: Löscht die Pixeldaten im Speicher (schaltet die Pixel beim nächsten ``show()`` aus).

**Fortgeschrittenes Beispiel: Farbwisch-Animation**

Erstellen wir eine einfache Animation, bei der jede LED nacheinander aufleuchtet.

* ``colorWipe()``: Lässt jedes Pixel nacheinander mit der angegebenen Farbe aufleuchten.
* Ruft ``colorWipe()`` mit unterschiedlichen Farben auf, um eine Animation zu erstellen.

.. code-block:: arduino
    
  #include <Adafruit_NeoPixel.h>

  #define PIXEL_PIN    0
  #define PIXEL_COUNT  8

  Adafruit_NeoPixel strip(PIXEL_COUNT, PIXEL_PIN, NEO_GRB + NEO_KHZ800);

  void setup() {
    strip.begin();
    strip.show(); // Initialisiere alle Pixel auf 'aus'
  }

  void loop() {
    colorWipe(strip.Color(255, 0, 0), 50); // Rot
    colorWipe(strip.Color(0, 255, 0), 50); // Grün
    colorWipe(strip.Color(0, 0, 255), 50); // Blau
  }

  void colorWipe(uint32_t color, int wait) {
    for(int i=0; i<strip.numPixels(); i++) {
      strip.setPixelColor(i, color);
      strip.show();
      delay(wait);
    }
  }

Nach dem Hochladen des Codes sollten Sie sehen, wie die LEDs nacheinander in Rot, dann Grün und dann Blau aufleuchten.

**Fortgeschrittenes Beispiel: Regenbogenzyklus-Animation**

* ``rainbowCycle()`` -Funktion: Durchläuft die Farben des Regenbogens über alle Pixel.
* Die verschachtelten Schleifen erzeugen einen sanften Übergang der Farben.
* ``Wheel()`` -Funktion: Erzeugt Regenbogenfarben über 0-255 Positionen.

.. code-block:: arduino
    
  #include <Adafruit_NeoPixel.h>

  #define PIXEL_PIN    0
  #define PIXEL_COUNT  8

  Adafruit_NeoPixel strip(PIXEL_COUNT, PIXEL_PIN, NEO_GRB + NEO_KHZ800);

  void setup() {
    strip.begin();
    strip.show(); // Initialisiere alle Pixel auf 'aus'
  }

  void loop() {
    rainbowCycle(20); // Regenbogenzyklus mit 20 ms Verzögerung pro Schritt
  }

  void rainbowCycle(int wait) {
    uint16_t i, j;

    for(j=0; j<256*5; j++) { // 5 Zyklen aller Farben am Rad
      for(i=0; i< strip.numPixels(); i++) {
        strip.setPixelColor(i, Wheel(((i * 256 / strip.numPixels()) + j) & 255));
      }
      strip.show();
      delay(wait);
    }
  }

  // Eingabewert 0 bis 255, um einen Farbwert zu erhalten.
  // Die Farben sind ein Übergang r - g - b - zurück zu r.
  uint32_t Wheel(byte WheelPos) {
    if(WheelPos < 85) {
      return strip.Color(WheelPos * 3, 255 - WheelPos * 3, 0);
    } else if(WheelPos < 170) {
      WheelPos -= 85;
      return strip.Color(255 - WheelPos * 3, 0, WheelPos * 3);
    } else {
      WheelPos -= 170;
      return strip.Color(0, WheelPos * 3, 255 - WheelPos * 3);
    }
  }

Nach dem Hochladen des Codes sollte der LED-Streifen einen Regenbogen an Farben zeigen, der sich sanft durchläuft.

**Weitere Erkundungen**

* Erstellen Sie benutzerdefinierte Animationen:

  * Experimentieren Sie mit verschiedenen Farben und Animationen.
  * Kombinieren Sie mehrere Animationsfunktionen.

* Reagieren auf Sensoren:

  Nutzen Sie Eingaben von Sensoren, um die LED-Farben oder -Muster zu ändern.

* Erstellen eines Visualisierers:

  Erstellen Sie einen Musikvisualisierer, der die LEDs basierend auf dem Toneingang ändert.

**Leistungsüberlegungen**

* Stromverbrauch:

  * Jede LED kann bei voller Helligkeit bis zu 60mA ziehen.
  * Für 8 LEDs sind das bis zu 480mA.
  * Stellen Sie sicher, dass Ihre Stromquelle den erforderlichen Strom liefern kann.

* Externes Netzteil:

  * Für größere Streifen oder höhere Helligkeit verwenden Sie ein externes 5V-Netzteil.
  * Verbinden Sie den Ground des externen Netzteils mit dem Ground des Pico.

**Schlussfolgerung**

In dieser Lektion haben Sie gelernt, wie man einen WS2812 RGB-LED-Streifen mit dem Raspberry Pi Pico und der Adafruit NeoPixel-Bibliothek steuert. Indem Sie einzelne Pixel manipulieren, können Sie atemberaubende visuelle Effekte für Ihre Projekte erstellen.
