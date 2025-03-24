.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in Raspberry Pi, Arduino und ESP32 ein und lerne zusammen mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Experten-Support**: Lösche nach dem Verkauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und des Teams.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitig Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Sonderrabatte**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nimm an Gewinnspielen und saisonalen Aktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _ar_led_bar:

2.2 - Anzeige des Levels
=============================

In dieser Lektion lernen wir, wie man ein LED-Bar-Graph mit dem Raspberry Pi Pico 2 W steuert. Ein LED-Bar-Graph besteht aus 10 LEDs, die in einer Reihe angeordnet sind und typischerweise verwendet werden, um Werte wie Lautstärke, Signalstärke oder andere Messungen darzustellen. Wir werden die LEDs der Reihe nach einschalten, um einen Level-Anzeigeeffekt zu erzeugen.

|img_led_bar_pin|

* :ref:`cpn_led_bar`

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten. 

Es ist definitiv praktisch, ein ganzes Kit zu kaufen. Hier ist der Link: 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name    
        - ARTIKEL IN DIESEM KIT
        - KAUF-LINK
    *   - Pico 2 W Starter Kit    
        - 450+    
        - |link_pico2w_kit|

Sie können die Teile auch einzeln über die untenstehenden Links kaufen.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - KOMPLEMENTEINLIEFERUNG    
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
        - 10(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led_bar`
        - 1
        - 

**Schaltplan**

|sch_ledbar|

Der LED-Bar-Graph enthält 10 LEDs, die jeweils einzeln steuerbar sind. Hierbei ist die Anode jeder der 10 LEDs mit GP6 bis GP15 verbunden, während die Kathode an einen 220-Ohm-Widerstand und dann an GND angeschlossen ist.


**Verdrahtung**

|wiring_ledbar|

**Code schreiben**

.. note::

    * Du kannst die Datei ``2.2_display_the_level.ino`` unter dem Pfad ``pico-2w-kit-main/arduino/2.2_display_the_level`` öffnen. 
    * Oder kopiere diesen Code in die **Arduino IDE**.
    * Vergiss nicht, das Board (Raspberry Pi Pico) und den richtigen Port auszuwählen, bevor du auf den **Upload**-Button klickst.

.. code-block:: Arduino

    // Definiere die GPIO-Pins, die mit dem LED-Bar-Graph verbunden sind
    const int ledPins[] = {6, 7, 8, 9, 10, 11, 12, 13, 14, 15};

    void setup() {
      // Initialisiere jeden Pin als Ausgang
      for (int i = 0; i < 10; i++) {
        pinMode(ledPins[i], OUTPUT);
      }
    }

    void loop() {
      // Schalte die LEDs der Reihe nach ein
      for (int i = 0; i < 10; i++) {
        digitalWrite(ledPins[i], HIGH); // LED einschalten
        delay(500);                     // Warte 500 Millisekunden
        digitalWrite(ledPins[i], LOW);  // LED ausschalten
        delay(500);                     // Warte 500 Millisekunden
      }
    }    

Nach dem Hochladen des Codes sollten die LEDs auf dem Bar-Graph nacheinander aufleuchten und so einen Level-Anzeigeeffekt erzeugen. Jede LED wird für eine halbe Sekunde eingeschaltet und dann ausgeschaltet, bevor die nächste LED aufleuchtet.

**Code verstehen**

#. Definition der LED-Pins:

   Erstelle ein Array ``ledPins``, das die GPIO-Pinnummern speichert, die mit jeder LED auf dem Bar-Graph verbunden sind.

   .. code-block:: Arduino

      const int ledPins[] = {6, 7, 8, 9, 10, 11, 12, 13, 14, 15};

#. Initialisierung der Pins:

   In der Funktion ``setup()`` setzen wir jeden Pin im Array ``ledPins`` als Ausgang.

   .. code-block:: Arduino

      void setup() {
        for (int i = 0; i < 10; i++) {
          pinMode(ledPins[i], OUTPUT);
        }
      }

#. Steuern der LEDs:

   In der Funktion ``loop()`` verwenden wir eine ``for``-Schleife, um jede LED der Reihe nach zu steuern. Wir schalten sie ein, warten 500 Millisekunden, schalten sie aus und warten weitere 500 Millisekunden, bevor die nächste LED eingeschaltet wird.

   .. code-block:: Arduino

      void loop() {
        for (int i = 0; i < 10; i++) {
          digitalWrite(ledPins[i], HIGH);
          delay(500);
          digitalWrite(ledPins[i], LOW);
          delay(500);
        }
      }

**Weitere Experimente**

* **Reihenfolge umkehren**: Ändere den Code, um die LEDs in umgekehrter Reihenfolge einzuschalten.

* **Bounce-Effekt erstellen**: Nachdem die letzte LED erreicht ist, lass die Reihenfolge zurück zur ersten LED umkehren.

  .. code-block:: Arduino
    
      void loop() {
        // Aufsteigende Reihenfolge
        for (int i = 0; i < 10; i++) {
          digitalWrite(ledPins[i], HIGH);
          delay(200);
          digitalWrite(ledPins[i], LOW);
        }
        // Absteigende Reihenfolge
        for (int i = 8; i >= 0; i--) {
          digitalWrite(ledPins[i], HIGH);
          delay(200);
          digitalWrite(ledPins[i], LOW);
        }
      }

* **Geschwindigkeit anpassen**: Ändere die Verzögerungszeiten, um die Geschwindigkeit der LEDs zu erhöhen oder zu verringern.



**Fazit**

In dieser Lektion hast du gelernt, wie man mehrere LEDs mit dem Raspberry Pi Pico steuert und visuelle Effekte mithilfe einfacher Programmierkonstrukte wie Schleifen und Verzögerungen erstellt. Dieses grundlegende Wissen ist entscheidend für fortgeschrittene Projekte, die LED-Displays und Indikatoren verwenden.
