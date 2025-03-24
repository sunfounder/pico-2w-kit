.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in Raspberry Pi, Arduino und ESP32 ein und lerne gemeinsam mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Experten-Support**: Lösche nach dem Verkauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitig Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Sonderrabatte**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nimm an Gewinnspielen und saisonalen Aktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _ar_led:



2.1 - Hallo, LED! 
=======================================

Willkommen zu deinem ersten Hardware-Projekt mit dem Raspberry Pi Pico 2 W! In dieser Lektion lernen wir, wie man eine LED mit MicroPython zum Blinken bringt. Dieses einfache Projekt ist ein großartiger Einstieg in die physische Computertechnik und hilft dir, zu verstehen, wie man Hardware mit Code steuert.


* :ref:`cpn_led`

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
        - 1 (220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|

**Schaltplan**

|sch_led|

Durch Setzen des GPIO-Pins auf hoch oder niedrig steuerst du die Ausgangsspannung dieses Pins. Wenn der Pin hoch ist, fließt Strom durch die LED (begrenzt durch den Widerstand), wodurch sie aufleuchtet. Wenn der Pin niedrig ist, fließt kein Strom und die LED geht aus.

**Verdrahtung**

|wiring_led|


**Code schreiben**

.. note::

    * Du kannst die Datei ``2.1_hello_led.ino`` im Verzeichnis ``pico-2w-kit-main/arduino/2.1_hello_led`` öffnen. 
    * Oder kopiere diesen Code in die **Arduino IDE**.
    * Vergiss nicht, das Board (Raspberry Pi Pico) und den richtigen Port auszuwählen, bevor du auf den **Upload**-Button klickst.

.. code-block:: Arduino

    const int ledPin = 15;  // GPIO-Pin, der mit der LED verbunden ist

    void setup() {
      pinMode(ledPin, OUTPUT);  // Initialisiere den GPIO-Pin als Ausgang
    }

    void loop() {
      digitalWrite(ledPin, HIGH);  // Schalte die LED ein
      delay(1000);                 // Warte 1 Sekunde
      digitalWrite(ledPin, LOW);   // Schalte die LED aus
      delay(1000);                 // Warte 1 Sekunde
    }

Nach dem Hochladen des Codes solltest du sehen, dass die LED 1 Sekunde lang an ist und dann für 1 Sekunde aus geht.

**Code verstehen**

#. Variablendeklaration:

   Deklariere eine konstante Ganzzahl ``ledPin`` und weise ihr den Wert 15 zu, der dem GPIO-Pin 15 entspricht, an den die LED angeschlossen ist.

   .. code-block:: Arduino

        const int ledPin = 15;

#. Setup-Funktion:

   Die Funktion ``setup()`` wird einmal ausgeführt, wenn das Board eingeschaltet oder zurückgesetzt wird. Hier initialisieren wir ``ledPin`` als Ausgangspin mit der Funktion ``pinMode()``.

   .. code-block:: Arduino

        void setup() {
          pinMode(ledPin, OUTPUT);
        }

#. Loop-Funktion:

   * Die Funktion ``loop()`` wird wiederholt ausgeführt, nachdem ``setup()`` abgeschlossen ist.
   * Mit ``digitalWrite()`` setzt du die Spannung des Pins ``ledPin``. Setzt du ihn auf ``HIGH``, erhält der Pin 3,3 V, und die LED leuchtet auf. Setzt du ihn auf ``LOW``, sinkt die Spannung auf 0 V und die LED geht aus. 
   * Die Funktion ``delay(1000)`` sorgt für eine Pause von 1 Sekunde zwischen dem Ein- und Ausschalten der LED.

   .. code-block:: Arduino

        void loop() {
          digitalWrite(ledPin, HIGH);
          delay(1000);
          digitalWrite(ledPin, LOW);
          delay(1000);
        }

**Zusätzliche Tipps**

* **Den Widerstand verstehen**: Der 220Ω-Widerstand begrenzt den Strom, der durch die LED fließt, und verhindert, dass sie durchbrennt.
* **Polarität beachten**: Stelle sicher, dass die LED korrekt angeschlossen ist. Der längere Draht ist die positive Anode und sollte mit dem Widerstand verbunden sein, der zum GPIO-Pin führt.
* **Experimentiere**: Versuche, die Werte in ``delay(1000)`` zu ändern, um die Geschwindigkeit des Blinkens der LED anzupassen.

**Fazit**

Herzlichen Glückwunsch! Du hast dein erstes Hardware-Projekt mit dem Raspberry Pi Pico 2 W gebaut. Dieses einfache LED-Blinkprojekt ist ein grundlegender Schritt in die Welt der physischen Computertechnik. Von hier aus kannst du komplexere Projekte erkunden, indem du Tasten, Sensoren und andere Komponenten hinzufügst.
