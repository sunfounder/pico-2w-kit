.. note:: 

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche gemeinsam mit anderen Technikbegeisterten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum solltest du beitreten?**

    - **Expertenunterstützung**: Erhalte Hilfe von unserer Community und unserem Team, um technische Herausforderungen und Probleme nach dem Kauf zu lösen.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und ersten Einblicken.
    - **Spezielle Rabatte**: Profitiere von exklusiven Vergünstigungen auf unsere neuesten Produkte.
    - **Feiertagsaktionen und Gewinnspiele**: Nimm an Verlosungen und Sonderaktionen teil.

    👉 Bereit, mit uns zu experimentieren und zu kreieren? Klicke auf [|link_sf_facebook|] und trete noch heute bei!

.. _ar_keypad:

4.2 Verwendung eines 4x4-Keypads
=================================================

In dieser Lektion lernen wir, wie man ein **4x4-Matrix-Keypad** mit dem Raspberry Pi Pico 2 W verbindet, um zu erkennen, welche Tasten gedrückt werden. Matrix-Keypads werden häufig in Geräten wie Taschenrechnern, Telefonen, Verkaufsautomaten und Sicherheitssystemen zur numerischen Eingabe verwendet.

* :ref:`cpn_keypad`


**Erforderliche Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten:

Ein komplettes Kit zu kaufen ist definitiv praktisch, hier ist der Link: 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ENTHALTENE ARTIKEL
        - KAUFLINK
    *   - Pico 2 W Starter Kit	
        - 450+
        - |link_pico2w_kit|

Alternativ kannst du die Komponenten auch einzeln über die folgenden Links erwerben:

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
        - 4 (10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_keypad`
        - 1
        - |link_keypad_buy|

**Funktionsweise des 4x4-Keypads**

Ein 4x4-Keypad besteht aus:

* **16 Tasten**, angeordnet in 4 Reihen und 4 Spalten.
* **8 Pins**, wobei 4 mit den Reihen und 4 mit den Spalten verbunden sind.

Wenn eine Taste gedrückt wird, verbindet sie eine bestimmte Reihe mit einer bestimmten Spalte, sodass wir die gedrückte Taste anhand der Zeilen- und Spaltennummer identifizieren können.

So sind die Tasten angeordnet:

|img_keypad|

**Schaltplan**

|sch_keypad_ar|

Die Reihen des Keypads (G2 ~ G5) werden auf HIGH gesetzt. Wenn einer der Pins G6 ~ G9 auf HIGH gelesen wird, wissen wir, welche Taste gedrückt wurde.

Beispiel: Wenn G6 auf HIGH gelesen wird, wurde die Taste „1“ gedrückt. Das liegt daran, dass die Steuerpins der Taste „1“ G2 und G6 sind. Wird die Taste gedrückt, verbindet sie G2 mit G6, wodurch G6 ebenfalls auf HIGH gesetzt wird.


**Verkabelung**

|wiring_keypad_ar|

**Code schreiben**


.. note::

    * Die Datei ``4.2_4x4_keypad.ino`` findest du unter dem Pfad ``pico-2w-kit-main/arduino/4.2_4x4_keypad``.
    * Alternativ kannst du den Code in die **Arduino IDE** kopieren.
    * Wähle das Board (Raspberry Pi Pico) und den richtigen Port, bevor du auf Hochladen klickst.
    * Die ``Adafruit Keypad``-Bibliothek wird hier verwendet, sie kann über den **Bibliotheksverwalter** installiert werden.

      .. image:: img/lib_ad_keypad.png

.. code-block:: arduino

    #include "Adafruit_Keypad.h"

    // Anzahl der Reihen und Spalten definieren
    const byte ROWS = 4;
    const byte COLS = 4;

    // Keymap für das Keypad definieren
    char keys[ROWS][COLS] = {
      { '1', '2', '3', 'A' },
      { '4', '5', '6', 'B' },
      { '7', '8', '9', 'C' },
      { '*', '0', '#', 'D' }
    };

    // Pins für die Reihen des Keypads
    byte rowPins[ROWS] = { 2, 3, 4, 5 };

    // Pins für die Spalten des Keypads
    byte colPins[COLS] = { 6, 7, 8, 9 };

    // Keypad-Objekt erstellen
    Adafruit_Keypad myKeypad = Adafruit_Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

    void setup() {
      // Initialize Serial communication
      Serial.begin(115200);

      // Initialize the keypad
      myKeypad.begin();
    }

    void loop() {
      // Update the state of keys
      myKeypad.tick();

      // Check if there are any new keypad events
      while (myKeypad.available()) {
        // Read the keypad event
        keypadEvent e = myKeypad.read();

        // Check if the event is a key press
        if (e.bit.EVENT == KEY_JUST_PRESSED) {
          // Print the key value to the Serial Monitor
          Serial.println((char)e.bit.KEY);
        }
      }

      delay(10); // Kurze Verzögerung für Stabilität
    }

Nach dem Hochladen des Codes kannst du eine beliebige Taste auf dem Keypad drücken. Das entsprechende Zeichen (z. B. '1', 'A') sollte im Seriellen Monitor erscheinen.

Stelle sicher, dass jeder Tastendruck korrekt erkannt und angezeigt wird. Teste alle Tasten, um die einwandfreie Funktionalität zu bestätigen.

**Code-Verständnis**

#. Einbinden der Bibliothek:

   Diese Zeile bindet die Adafruit Keypad-Bibliothek ein, die Funktionen zur Interaktion mit dem Keypad bereitstellt.

   .. code-block:: arduino

      #include "Adafruit_Keypad.h"

#. Definition des Keypad-Layouts:

   ``ROWS`` und ``COLS`` legen die Abmessungen des Keypads fest. ``keys`` ist ein zweidimensionales Array, das die Belegung der einzelnen Tasten speichert.

   .. code-block:: arduino

      const byte ROWS = 4;
      const byte COLS = 4;

      char keys[ROWS][COLS] = {
        { '1', '2', '3', 'A' },
        { '4', '5', '6', 'B' },
        { '7', '8', '9', 'C' },
        { '*', '0', '#', 'D' }
      };

#. Verbindung des Keypads mit den GPIO-Pins:

   ``rowPins`` und ``colPins`` sind Arrays, die die GPIO-Pins speichern, die mit den Reihen bzw. Spalten des Keypads verbunden sind.

   .. code-block:: arduino

      byte rowPins[ROWS] = { 2, 3, 4, 5 };
      byte colPins[COLS] = { 6, 7, 8, 9 };

#. Initialisierung des Keypad-Objekts:

   Diese Zeile erstellt eine Instanz der Klasse ``Adafruit_Keypad`` und initialisiert sie mit der Tastenzuordnung und den Pin-Konfigurationen.

   .. code-block:: arduino

      Adafruit_Keypad myKeypad = Adafruit_Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

#. Setup-Funktion:

   Initialisiert die serielle Kommunikation zur Fehlerbehebung und startet das Keypad.

   .. code-block:: arduino

      void setup() {
        Serial.begin(115200);    // Serielle Kommunikation mit 115200 Baud starten
        myKeypad.begin();        // Keypad initialisieren
      }

#. Loop-Funktion:

   * Überprüft kontinuierlich Tasteneingaben.
   * Gibt die gedrückte Taste im Seriellen Monitor aus.

   .. code-block:: arduino

      void loop() {
        myKeypad.tick(); // Status der Tasten aktualisieren

        while (myKeypad.available()) {
          keypadEvent e = myKeypad.read(); // Keypad-Ereignis lesen

          if (e.bit.EVENT == KEY_JUST_PRESSED) {
            Serial.println((char)e.bit.KEY); // Gedrückte Taste ausgeben
          }
        }
        delay(10); // Kurze Verzögerung zur Stabilisierung
      }

**Weitere Experimente**

* Implementierung von Key-Debouncing:

  Erhöhe die Zuverlässigkeit der Tastenabfrage durch die Implementierung von Debouncing-Techniken, um Fehlauslösungen durch mechanische Störungen zu vermeiden.

* Erstellung eines Passwort-Eingabesystems:

  Verwende das Keypad zur Eingabe eines Passworts, um den Zugriff auf bestimmte Funktionen in deinem Projekt zu steuern.

* Integration mit anderen Komponenten:

  Kombiniere das Keypad mit LCD-Displays, LEDs oder Buzzern, um komplexere Benutzeroberflächen zu erstellen.

* Bau eines einfachen Taschenrechners:

  Nutze das Keypad zur Eingabe von Zahlen und zur Durchführung grundlegender mathematischer Operationen, die auf einem LCD-Display angezeigt werden.

**Fazit**

In dieser Lektion hast du gelernt, wie du ein 4x4-Matrix-Keypad mit dem Raspberry Pi Pico unter Verwendung der Adafruit Keypad-Bibliothek verbindest. Durch die Erkennung von Tasteneingaben kannst du interaktive Projekte wie numerische Eingabesysteme, Passwortschutzmechanismen und mehr erstellen. Das Verständnis der Tastenerfassung und -verarbeitung ist entscheidend für den Aufbau benutzerfreundlicher Schnittstellen in Elektronikprojekten.
