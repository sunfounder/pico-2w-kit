.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in Raspberry Pi, Arduino und ESP32 ein und lerne gemeinsam mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Experten-Support**: Lösche nach dem Verkauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitig Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Sonderrabatte**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nimm an Gewinnspielen und saisonalen Aktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _ar_mpr121:

4.3 Elektrotastatur mit MPR121
========================================================

In dieser Lektion lernen wir, wie man den **MPR121 kapazitiven Touch-Sensor** verwendet, um eine touch-sensible Tastatur mit dem Raspberry Pi Pico 2 W zu erstellen. Der MPR121 ermöglicht es dir, Touch-Eingaben auf bis zu 12 Elektroden zu erkennen, die mit leitfähigen Materialien wie Draht, Folie oder sogar Früchten wie Bananen verbunden werden können!

* :ref:`cpn_mpr121`

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
        - :ref:`cpn_mpr121`
        - 1
        - 

**Den MPR121 Sensor verstehen**

Der **MPR121** ist ein kapazitiver Touch-Sensor-Controller, der über die I2C-Schnittstelle kommuniziert. Er kann bis zu 12 Touch-Eingaben verarbeiten, was ihn ideal für interaktive Projekte mit mehreren Touchpunkten macht.

Der MPR121-Sensor erkennt Änderungen der Kapazität an seinen Elektroden. Wenn du eine Elektrode berührst, ändert sich die Kapazität, und der Sensor registriert einen Touch. Diese Informationen werden über I2C an den Raspberry Pi Pico 2 übertragen.

**Schaltplan**

|sch_mpr121_ar|



**Verdrahtung**

|wiring_mpr121_ar|

* Verbinde Drähte oder leitfähige Materialien mit den Elektroden-Pins (bezeichnet mit **E0** bis **E11**) auf dem MPR121.
* Du kannst die anderen Enden der Drähte an leitfähige Objekte wie Früchte, Aluminiumfolienformen oder Touchpads anschließen.

**Code schreiben**

.. note::

    * Du kannst die Datei ``4.3_electrode_keyboard.ino`` im Verzeichnis ``pico-2w-kit-main/arduino/4.3_electrode_keyboard`` öffnen.
    * Oder kopiere diesen Code in die **Arduino IDE**.
    * Wähle dann das Raspberry Pi Pico-Board und den richtigen Port aus, bevor du auf den Upload-Button klickst.
    * Die ``Adafruit MPR121``-Bibliothek wird hier verwendet, du kannst sie über den **Bibliotheks-Manager** installieren.

      .. image:: img/lib_mpr121.png

.. code-block:: arduino

    #include <Wire.h>
    #include <Adafruit_MPR121.h>

    // Erstelle eine Instanz des MPR121-Sensors
    Adafruit_MPR121 cap = Adafruit_MPR121();

    // Array, um den Touch-Status jeder Elektrode zu speichern
    bool touchStates[12] = { false };

    // Variablen zur Speicherung der aktuellen und letzten Touch-Status
    uint16_t currtouched = 0;
    uint16_t lasttouched = 0;

    void setup() {
      Serial.begin(115200); // Initialisiere die serielle Kommunikation mit 115200 Baud
      while (!Serial);    // Warten, bis der Serial Monitor geöffnet ist

      // Initialisiere den MPR121-Sensor mit der I2C-Adresse 0x5A
      if (!cap.begin(0x5A)) {
        Serial.println("MPR121 not found, check wiring?");
        while (1);
      }
      Serial.println("MPR121 found!");
    }

    void loop() {
      // Lese die aktuell berührten Pads
      currtouched = cap.touched();

      // Überprüfe, ob sich der Touch-Status geändert hat
      if (currtouched != lasttouched) {
        // Aktualisiere den letzten Touch-Status
        lasttouched = currtouched;

        // Iteriere durch jede Elektrode
        for (int i = 0; i < 12; i++) {
          // Überprüfe, ob die Elektrode berührt wurde
          if (currtouched & (1 << i)) {
            touchStates[i] = true;
          } else {
            touchStates[i] = false;
          }
        }

        // Gib die Touch-Status als Binärzeichenfolge aus
        for (int i = 0; i < 12; i++) {
          Serial.print(touchStates[i] ? "1" : "0");
        }
        Serial.println();
      }

      delay(100); // Kleine Verzögerung, um die Messwerte zu stabilisieren
    }

Nachdem du den Code hochgeladen hast, berühre die Elektroden, die mit dem MPR121-Sensor verbunden sind.

* Beobachte die binäre Ausgabe im Serial Monitor, die anzeigt, welche Elektroden berührt werden.
* Zum Beispiel wird das Berühren der ersten und elften Elektrode ``100000000010`` anzeigen.

**Code verstehen**

#. Bibliotheken einbinden:


   * ``Wire.h``: Handhabt die I2C-Kommunikation.
   * ``Adafruit_MPR121.h``: Bietet Funktionen zur Interaktion mit dem MPR121-Sensor.

#. Initialisierung des MPR121-Sensors:

   Erstellt eine Instanz des MPR121-Sensors.

   .. code-block:: arduino

      Adafruit_MPR121 cap = Adafruit_MPR121();

#. Setup-Funktion:

   * Startet die serielle Kommunikation zur Fehlerbehebung.
   * Initialisiert den MPR121-Sensor mit der I2C-Adresse 0x5A.
   * Wenn der Sensor nicht gefunden wird, wird eine Fehlermeldung ausgegeben und das Programm angehalten.

   .. code-block:: arduino

      void setup() {
        Serial.begin(115200); // Initialisiere die serielle Kommunikation
        while (!Serial);    // Warten, bis der Serial Monitor geöffnet ist

        // Initialisiere den MPR121-Sensor mit der I2C-Adresse 0x5A
        if (!cap.begin(0x5A)) {
          Serial.println("MPR121 nicht gefunden, Überprüfe die Verkabelung?");
          while (1);
        }
        Serial.println("MPR121 found!");
      }

#. ``loop()``-Funktion: 

   * Holt sich den aktuellen Touch-Status vom MPR121-Sensor. Jedes Bit in der Variable ``currtouched`` repräsentiert den Touch-Status einer Elektrode (1 für berührt, 0 für nicht berührt).

     .. code-block:: arduino
     
        currtouched = cap.touched();

   * Überprüft, ob sich der Touch-Status seit der letzten Schleifeniteration geändert hat.

     .. code-block:: arduino

        if (currtouched != lasttouched) {
          // Aktualisiere die Touch-Status
        }

   * Iteriert durch jede Elektrode und aktualisiert das ``touchStates``-Array basierend darauf, ob die Elektrode berührt wurde oder nicht.

     .. code-block:: arduino

        for (int i = 0; i < 12; i++) {
          if (currtouched & (1 << i)) {
            touchStates[i] = true;
          } else {
            touchStates[i] = false;
          }
        }

   * Gibt die Touch-Status als 12-Bit-Binärzeichenfolge im Serial Monitor aus. Zum Beispiel wird beim Berühren der ersten und elften Elektrode ``100000000010`` angezeigt.

     .. code-block:: arduino

        for (int i = 0; i < 12; i++) {
          Serial.print(touchStates[i] ? "1" : "0");
        }
        Serial.println();

   * Fügt eine kurze Verzögerung hinzu, um die Messwerte zu stabilisieren und die Anzeige im Serial Monitor nicht zu überfluten.

     .. code-block:: arduino

        delay(100);

**Erweiterung der Elektroden**

Du kannst dein Projekt erweitern, indem du die Elektroden mit verschiedenen leitfähigen Materialien verbindest:

* **Früchte**: Schließe Drähte an Bananen, Äpfel oder andere Früchte an, um sie zu touch-sensiblen Eingabegeräten zu machen.
* **Folienformen**: Schneide Formen aus Aluminiumfolie und befestige sie an den Elektroden.
* **Leitfähige Farbe**: Zeichne Muster mit leitfähiger Tinte oder Farbe.

.. note::

    Wenn du die Elektroden änderst (z.B. andere Materialien anschließt), musst du den Sensor möglicherweise zurücksetzen, um die Basiswerte neu zu kalibrieren.

**Weitere Erkundungen**

* Erstellen interaktiver Projekte:

  Baue eine touch-gesteuerte LED-Matrix, bei der jede Elektrode eine einzelne LED steuert.

* Implementierung der Entprellung von Tasten:

  Verbessere die Zuverlässigkeit der Touch-Erkennung durch die Implementierung von Entprell-Techniken, um Fehlberührungen zu filtern.

* Kombination mit anderen Sensoren:

  Integriere den MPR121 mit anderen Sensoren wie Temperatur- oder Lichtsensoren, um komplexere interaktive Systeme zu schaffen.

* Entwicklung eines Touch-basierten Spielecontrollers:

  Verwende die Touch-Eingaben, um Spielelemente wie die Bewegung von Charakteren oder die Auswahl von Optionen zu steuern.

**Fazit**

In dieser Lektion hast du gelernt, wie man den MPR121 kapazitiven Touch-Sensor mit dem Raspberry Pi Pico verwendet, um eine touch-sensible Tastatur zu erstellen. Durch die Erkennung von Touch-Eingaben auf mehreren Elektroden kannst du interaktive Schnittstellen für deine Projekte bauen, wie z.B. benutzerdefinierte Keypads, Bedienfelder oder kreative Eingabegeräte. Zu verstehen, wie man Touch-Eingaben liest und verarbeitet, ist eine wertvolle Fähigkeit, um reaktionsfähige und benutzerfreundliche Elektronikprojekte zu entwickeln.
