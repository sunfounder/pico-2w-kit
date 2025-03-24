.. note:: 

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche mit Gleichgesinnten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum beitreten?**

    - **Expertenunterstützung**: Erhalte Hilfe von unserer Community und unserem Team bei technischen Herausforderungen und Problemen nach dem Kauf.
    - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um deine Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und ersten Einblicken.
    - **Spezielle Rabatte**: Profitiere von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nimm an Gewinnspielen und saisonalen Aktionen teil.

    👉 Bereit, mit uns zu experimentieren und zu erschaffen? Klicke auf [|link_sf_facebook|] und werde Teil unserer Community!

.. _ar_irremote:


6.4 Verwendung einer Infrarot-Fernbedienung
==========================================================

In dieser Lektion lernen wir, wie man eine **Infrarot-(IR)-Fernbedienung** und einen **IR-Empfänger** mit dem Raspberry Pi Pico 2 W verwendet. Damit können wir Signale von einer IR-Fernbedienung empfangen und decodieren, um unsere Projekte drahtlos zu steuern.

* :ref:`cpn_ir_receiver`

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Es ist definitiv praktisch, ein komplettes Kit zu kaufen. Hier ist der Link: 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ENTHALTENE TEILE
        - KAUFLINK
    *   - Pico 2 W Starter Kit	
        - 450+
        - |link_pico2w_kit|

Die Komponenten können auch einzeln über die folgenden Links erworben werden:


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
        - :ref:`cpn_ir_receiver`
        - 1
        - |link_receiver_buy|


**Grundlagen der Infrarotkommunikation**

Die Infrarotkommunikation überträgt Daten drahtlos mithilfe von Infrarotlicht. Viele Haushaltsgeräte wie Fernseher oder DVD-Player nutzen IR-Fernbedienungen zur Steuerung.


* **IR-Sender (Fernbedienung):** Sendet moduliertes Infrarotlicht aus, wenn eine Taste gedrückt wird.
* **IR-Empfänger:** Erkennt das modulierte IR-Licht und wandelt es in elektrische Signale um, die dekodiert werden können.

**Schaltplan**

|sch_irrecv|

**Verdrahtung**

|wiring_irrecv|

**Code schreiben**

Wir schreiben ein Programm, das den IR-Empfänger initialisiert, eingehende IR-Signale empfängt, diese dekodiert und die erkannten Tastendrücke im seriellen Monitor anzeigt.

.. note::

    * Die Datei ``6.4_ir_remote_control.ino`` kann im Verzeichnis ``pico-2w-kit-main/arduino/6.4_ir_remote_control`` geöffnet werden.
    * Alternativ kann der Code in die **Arduino IDE** kopiert werden.
    * Wähle vor dem Hochladen die Raspberry Pi Pico-Platine und den richtigen Port aus.
    * Die Bibliothek ``IRremote`` wird hier verwendet und kann über den **Bibliotheksmanager** installiert werden.

      .. image:: img/lib_ir.png

.. code-block:: arduino

    #define SEND_PWM_BY_TIMER

    #include <IRremote.hpp>  // Einbinden der IRremote-Bibliothek

    const int receiverPin = 17;  // Pin-Nummer für den IR-Sensor definieren

    void setup() {
      // Starte die serielle Kommunikation mit einer Baudrate von 115200
      Serial.begin(115200);
      // Initialisiere den IR-Empfänger am angegebenen Pin mit LED-Feedback
      IrReceiver.begin(receiverPin, ENABLE_LED_FEEDBACK);
    }

    void loop() {
      if (IrReceiver.decode()) {  // Check if the IR receiver has received a signal
        bool result = 0;
        String key = decodeKeyValue(IrReceiver.decodedIRData.command);
        if (key != "ERROR") {
          Serial.println(key);  // Den erkannten Befehl ausgeben
          delay(100);
        }
        IrReceiver.resume();  // IR-Empfänger für das nächste Signal vorbereiten
      }
    }

    // Funktion zur Zuordnung empfangener IR-Signale zu Tastenwerten
    String decodeKeyValue(long result) {
      switch (result) {
        case 0x45: return "POWER";
        case 0x47: return "MUTE";
        case 0x46: return "MODE";
        case 0x44: return "PLAY/PAUSE";
        case 0x40: return "BACKWARD";
        case 0x43: return "FORWARD";
        case 0x7: return "EQ";
        case 0x15: return "-";
        case 0x9: return "+";
        case 0x19: return "CYCLE";
        case 0xD: return "U/SD";
        case 0x16: return "0";
        case 0xC: return "1";
        case 0x18: return "2";
        case 0x5E: return "3";
        case 0x8: return "4";
        case 0x1C: return "5";
        case 0x5A: return "6";
        case 0x42: return "7";
        case 0x52: return "8";
        case 0x4A: return "9";
        case 0x0: return "ERROR";
        default: return "ERROR";
      }
    }

Nach dem Hochladen des Codes kannst du die Tasten auf der IR-Fernbedienung drücken und die entsprechenden Befehle im seriellen Monitor beobachten.

.. code-block:: arduino

    BACKWARD
    CYCLE
    POWER
    MODE
    EQ
    5
    9

.. note::

  Eine neue Fernbedienung könnte eine Plastiklasche enthalten, die die Batterie isoliert. Ziehe sie heraus, um die Fernbedienung zu aktivieren.


**Verständnis des Codes** 

#. Header und Konstanten:

   * ``#define SEND_PWM_BY_TIMER``: Diese Zeile definiert offenbar ein Makro zum Senden von PWM-Signalen mit einem Timer. Allerdings wird es im Code nicht verwendet, sodass es sich um einen Überrest oder Platzhalter handeln könnte.
   * ``#include <IRremote.hpp>``: Bindet die Bibliothek ``IRremote`` ein, die Funktionen zum Senden und Empfangen von IR-Signalen bereitstellt.
   * ``const int receiverPin = 17;``: Definiert den Pin (17), an den das IR-Empfangsmodul auf dem Arduino angeschlossen ist.

#. Setup-Funktion:

   * ``Serial.begin(115200);``: Initialisiert die serielle Kommunikation mit einer Baudrate von 115200, sodass der Arduino zur Fehleranalyse mit einem Computer kommunizieren kann.
   * ``IrReceiver.begin(receiverPin, ENABLE_LED_FEEDBACK);``: Initialisiert den IR-Empfänger am ``receiverPin`` und aktiviert die LED-Rückmeldung, sodass eine LED aufleuchtet, wenn ein Signal empfangen wird.

   .. code-block:: arduino

      void setup() {
        Serial.begin(115200);
        IrReceiver.begin(receiverPin, ENABLE_LED_FEEDBACK);
      }

#. Loop-Funktion: 

   * ``if (IrReceiver.decode())``: Überprüft, ob der IR-Empfänger ein gültiges IR-Signal empfangen hat. Falls ja, wird das Signal dekodiert.
   * ``decodeKeyValue(IrReceiver.decodedIRData.command)``: Ruft eine Funktion auf, um das empfangene IR-Signal in eine lesbare Taste (z. B. "POWER" oder "MUTE") umzuwandeln.
   * ``Serial.println(key);``: Gibt die dekodierte Taste im seriellen Monitor aus.
   * ``delay(100);``: Fügt eine kurze Verzögerung hinzu, um zu verhindern, dass das gleiche Signal mehrfach gedruckt wird.
   * ``IrReceiver.resume();``: Bereitet den IR-Empfänger darauf vor, das nächste Signal zu empfangen, indem das vorherige gelöscht wird.

   .. code-block:: arduino

      void loop() {
        if (IrReceiver.decode()) {
          bool result = 0;
          String key = decodeKeyValue(IrReceiver.decodedIRData.command);
          if (key != "ERROR") {
            Serial.println(key);
            delay(100);
          }
          IrReceiver.resume();
        }
      }

#. ``decodeKeyValue``-Funktion:

   * Diese Funktion nimmt einen long-Wert (das rohe IR-Signal) entgegen und verwendet eine switch-Anweisung, um ihn einer bestimmten Taste zuzuordnen. Jeder Fall entspricht einer anderen Taste auf der Fernbedienung.
   * Zum Beispiel wird 0x45 der Taste "POWER" zugeordnet, während 0x47 für "MUTE" steht.
   * Falls das empfangene Signal keiner bekannten Taste entspricht, gibt die Funktion "ERROR" zurück.

   .. code-block:: arduino

      String decodeKeyValue(long result) {
        switch (result) {
          case 0x45: return "POWER";
          case 0x47: return "MUTE";
          case 0x46: return "MODE";
          ...
          case 0x4A: return "9";
          case 0x0: return "ERROR";
          default: return "ERROR";
        }
      }

**Fehlersuche**

* Keine Werte werden angezeigt:

  * Überprüfe, ob der IR-Empfänger korrekt an GPIO 17 angeschlossen ist.
  * Stelle sicher, dass der IR-Empfänger mit Strom versorgt wird (VCC und GND korrekt verbunden).
  * Prüfe, ob der richtige GPIO-Pin im Code definiert ist (``receiverPin``).

* Falsche Werte oder unerwartete Signale:

  * Stelle sicher, dass die Fernbedienung mit dem IR-Empfänger kompatibel ist.
  * Überprüfe, ob die ``decodeKeyValue``-Funktion die richtigen IR-Codes für deine Fernbedienung enthält.
  * Teste eine Universalfernbedienung, um sicherzustellen, dass das Signal korrekt verarbeitet wird.

* Unbekannte Befehle:

  * Ergänze die ``decodeKeyValue``-Funktion um die spezifischen IR-Codes deiner Fernbedienung.
  * Verwende ein IR-Dekodierungswerkzeug oder eine Referenzliste, um die richtigen Codes deiner Fernbedienung zu ermitteln.

* Signalstörungen:

  * Achte darauf, dass keine Hindernisse zwischen der Fernbedienung und dem IR-Empfänger liegen.
  * Vermeide es, den Sensor in der Nähe anderer IR-Quellen zu platzieren, um Interferenzen zu minimieren.

**Weitere Experimente**

* Steuerung von Geräten mit IR-Signalen:

  Verwende die dekodierten IR-Signale, um LEDs, Motoren, Servos oder andere Aktoren entsprechend der Fernbedienungseingaben zu steuern.

* Eine universelle Fernbedienung erstellen:

  Erweitere die ``decodeKeyValue()``-Funktion, um mehrere Fernbedienungen zu unterstützen, indem du eine breitere Palette von IR-Codes zuweist.

* Feedback-Mechanismen hinzufügen:

  Implementiere ein LCD- oder OLED-Display, um den aktuellen Status oder die empfangenen Befehle anzuzeigen.

**Fazit**

In dieser Lektion hast du gelernt, wie du eine Infrarot-(IR)-Fernbedienung mit dem Raspberry Pi Pico verwendest, um IR-Signale zu empfangen und zu dekodieren. Durch die Integration der IRremote -Bibliothek kannst du Fernbedienungseingaben einfach interpretieren und zur Steuerung deiner Projekte nutzen. Dieses Wissen ist die Grundlage für die Entwicklung fernsteuerbarer Geräte, automatisierter Systeme und benutzerfreundlicher Schnittstellen für eine Vielzahl von Anwendungen.
