.. note:: 

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein und tausche dich mit Gleichgesinnten aus.

    **Warum beitreten?**

    - **Expertenunterstützung**: Erhalte Hilfe von unserer Community und unserem Team, um technische Herausforderungen und Support-Probleme nach dem Kauf zu lösen.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Sonderrabatte**: Profitiere von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nimm an Verlosungen und saisonalen Aktionen teil.

    👉 Bereit, mit uns zu entdecken und zu gestalten? Klicke auf [|link_sf_facebook|] und trete noch heute bei!

.. _ar_lcd:

3.4 Flüssigkristallanzeige (LCD1602)
========================================

In dieser Lektion lernen wir, wie man ein **1602 LCD** mit dem Raspberry Pi Pico 2 W verwendet, um Text anzuzeigen. Das LCD1602 ist ein zeichenbasiertes Flüssigkristalldisplay, das 16 Zeichen auf 2 Zeilen anzeigen kann – ideal für Projekte, die Nachrichten, Sensordaten oder Statusaktualisierungen anzeigen müssen.

Das direkte Anschließen eines LCDs an einen Mikrocontroller erfordert normalerweise viele GPIO-Pins, was die Funktionalität deines Projekts einschränken kann. Um dieses Problem zu lösen, können wir ein LCD1602-Modul mit einer **I2C-Schnittstelle** verwenden. Das I2C-Protokoll benötigt nur zwei Datenleitungen (SDA und SCL), sodass du das LCD mit nur zwei GPIO-Pins steuern kannst. Dadurch bleiben weitere Pins für zusätzliche Sensoren oder Geräte frei.

**I2C auf dem Raspberry Pi Pico 2 W verstehen**

Der Raspberry Pi Pico 2 W unterstützt die I2C-Kommunikation über mehrere GPIO-Pins und bietet damit eine hohe Flexibilität für deine Projekte. Er verfügt über zwei I2C-Busse, I2C0 und I2C1, die jeweils mehreren Pin-Kombinationen zugeordnet werden können.

Hier sind die I2C-fähigen Pins des Pico 2:

|pin_i2c|

Du kannst jedes passende Paar von SDA- und SCL-Pins für I2C0 oder I2C1 wählen. Diese Flexibilität hilft, Pin-Konflikte mit anderen Peripheriegeräten in deinem Projekt zu vermeiden.


**Erforderliche Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten:

Es ist praktisch, ein Komplettset zu kaufen – hier ist der Link: 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ENTHALTENE TEILE IM KIT
        - KAUFLINK
    *   - Pico 2 W Starter Kit	
        - 450+
        - |link_pico2w_kit|

Du kannst sie auch einzeln über die unten stehenden Links erwerben.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - KOMPONENTENBESCHREIBUNG	
        - ANZAHL
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
        - :ref:`cpn_i2c_lcd`
        - 1
        - |link_i2clcd1602_buy|

**Schaltplan**

|sch_lcd_ar|

**Verdrahtung**

|wiring_lcd_ar|

**Code schreiben**

.. note::

    * Du kannst die Datei ``3.4_liquid_crystal_display.ino`` unter dem Pfad ``pico-2w-kit-main/arduino/3.4_liquid_crystal_display`` öffnen. 
    * Oder kopiere diesen Code in die **Arduino IDE**.
    * Wähle die Raspberry Pi Pico-Platine und den richtigen Port aus, bevor du auf den Upload-Button klickst.
    * Die ``LiquidCrystal I2C``-Bibliothek wird hier verwendet. Du kannst sie über den **Library Manager** installieren.

      .. image:: img/lib_i2c_lcd.png

.. code-block:: arduino

  #include <Wire.h>
  #include <LiquidCrystal_I2C.h>

  // LCD I2C-Adresse (normalerweise 0x27 oder 0x3F)
  #define LCD_ADDRESS 0x27
  #define LCD_COLUMNS 16
  #define LCD_ROWS    2

  // Bibliothek mit der I2C-Adresse und Dimensionen initialisieren
  LiquidCrystal_I2C lcd(LCD_ADDRESS, LCD_COLUMNS, LCD_ROWS);

  void setup() {
    // LCD initialisieren
    lcd.init();
    lcd.backlight();  // Hintergrundbeleuchtung aktivieren

    // Nachrichten auf dem LCD anzeigen
    lcd.setCursor(0, 0);  // Spalte 0, Zeile 0
    lcd.print("Hello, World!");
    lcd.setCursor(0, 1);  // Spalte 0, Zeile 1
    lcd.print("LCD1602 mit I2C");
  }

  void loop() {
    // Keine Aktion erforderlich
  }


Nach dem Hochladen des Codes auf den Raspberry Pi Pico sollte das LCD folgende Nachrichten anzeigen:

* In der ersten Zeile: „Hello, World!“
* In der zweiten Zeile: „LCD1602 mit I2C“

Falls nichts auf dem Bildschirm erscheint, versuche, den Kontrast mit dem kleinen Potentiometer auf der Rückseite des LCD-Moduls einzustellen, bis der Text sichtbar wird.

**Code-Verständnis**

#. Einbinden der Bibliotheken:

   * ``Wire.h``: Verwaltet die I2C-Kommunikation.
   * ``LiquidCrystal_I2C.h``: Erleichtert die Interaktion mit dem I2C-LCD.

#. Definition der LCD-Parameter:

   * ``LCD_ADDRESS``: Die I2C-Adresse des LCD-Moduls. Häufige Adressen sind 0x27 oder 0x3F. Falls du unsicher bist, kannst du ein I2C-Scanner-Sketch verwenden, um die Adresse zu ermitteln.

   .. code-block:: arduino

      #define LCD_ADDRESS 0x27
      #define LCD_COLUMNS 16
      #define LCD_ROWS    2

#. Initialisierung des LCDs:

   .. code-block:: arduino

      LiquidCrystal_I2C lcd(LCD_ADDRESS, LCD_COLUMNS, LCD_ROWS);

#. In der ``setup()`` -Funktion:

   .. code-block:: arduino

      lcd.init();         // Initialisiert das LCD
      lcd.backlight();    // Schaltet die Hintergrundbeleuchtung ein

#. Anzeige von Text:

   .. code-block:: arduino

      lcd.setCursor(0, 0);  // Setzt den Cursor auf Spalte 0, Zeile 0
      lcd.print("Hello, World!");

      lcd.setCursor(0, 1);  // Setzt den Cursor auf Spalte 0, Zeile 1
      lcd.print("LCD1602 mit I2C");

**Serielle Eingaben zur Anzeige auf dem LCD nutzen**

Wir können das Programm erweitern, um Eingaben aus dem seriellen Monitor zu lesen und auf dem LCD anzuzeigen.

* Geänderter Code:

  .. code-block:: arduino

    #include <Wire.h>
    #include <LiquidCrystal_I2C.h>

    #define LCD_ADDRESS 0x27
    #define LCD_COLUMNS 16
    #define LCD_ROWS    2

    LiquidCrystal_I2C lcd(LCD_ADDRESS, LCD_COLUMNS, LCD_ROWS);

    void setup() {
      lcd.init();
      lcd.backlight();

      Serial.begin(115200);
      lcd.setCursor(0, 0);
      lcd.print("Gib Text ein:");
    }

    void loop() {
      if (Serial.available() > 0) {
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Du hast eingegeben:");

        String inputText = Serial.readStringUntil('\n');
        lcd.setCursor(0, 1);
        lcd.print(inputText);
      }
    }

  Nach dem Hochladen des Codes kannst du eine Nachricht eingeben und ``Enter`` drücken. Die Nachricht wird auf dem LCD angezeigt.

* Erklärung:

  * Lesen der seriellen Eingabe: Überprüft, ob Daten im seriellen Port verfügbar sind, und liest den Eingabestring bis zum nächsten Zeilenumbruch.

   .. code-block:: arduino

      if (Serial.available() > 0) {
        String inputText = Serial.readStringUntil('\n');
        // ...
      }

  * Anzeige der seriellen Eingabe auf dem LCD:

    .. code-block:: arduino

      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("You typed:");
      lcd.setCursor(0, 1);
      lcd.print(inputText);

**Fehlersuche**

* Keine Anzeige auf dem LCD:

  * Stelle den Kontrast mit dem Potentiometer auf der Rückseite des LCD-Moduls ein.
  * Überprüfe die Verdrahtung.
  * Stelle sicher, dass die richtige I2C-Adresse verwendet wird. Falls nötig, kann ein I2C-Scanner zur Überprüfung genutzt werden. Die Standardadresse ist meist 0x27, kann aber auch 0x3F sein.

  .. code-block:: arduino

      #include <Wire.h>

      void setup() {
          Wire.begin();
          Serial.begin(115200);
          while (!Serial); // Warten, bis die serielle Verbindung hergestellt ist
          Serial.println("\nI2C Scanner");
      }

      void loop() {
          byte error, address;
          int nDevices;

          Serial.println("Scanning...");

          nDevices = 0;
          for (address = 1; address < 127; address++) {
              Wire.beginTransmission(address);
              error = Wire.endTransmission();

              if (error == 0) {
                  Serial.print("I2C device found at address 0x");
                  if (address < 16) {
                      Serial.print("0");
                  }
                  Serial.println(address, HEX);

                  nDevices++;
              }else if (error == 4) {
                  Serial.print("Unknown error at address 0x");
                  if (address < 16) {
                      Serial.print("0");
                  }
                  Serial.println(address, HEX);
              }
          }
          if(nDevices == 0) {
              Serial.println("No I2C devices found\n");
          }else {
              Serial.println("done\n");
          }
          delay(5000); // Warte 5 Sekunden, bevor erneut gescannt wird
      }

* Falsche Zeichen auf dem Display:

  * Überprüfe die Verkabelung.
  * Stelle sicher, dass das LCD korrekt initialisiert wurde.

**Weitere Experimente**

* **Eigene Zeichen erstellen**:

  Entwickle und speichere benutzerdefinierte Zeichen oder Symbole auf dem LCD.

* **Sensorwerte anzeigen**:

  Erfasse und zeige Messwerte von Sensoren (z. B. Temperatur, Luftfeuchtigkeit) auf dem LCD an.

* **Mehrere I2C-Geräte verwalten**:

  Schließe mehrere I2C-Geräte an den Pico an und steuere sie gleichzeitig.

**Fazit**

In dieser Lektion hast du gelernt, wie du ein I2C LCD1602 mit dem Raspberry Pi Pico verwendest, um Text anzuzeigen. Dank der I2C-Schnittstelle benötigt das LCD nur zwei GPIO-Pins, wodurch zusätzliche Pins für weitere Sensoren und Peripheriegeräte frei bleiben. Dies ermöglicht komplexere und vielseitigere Projekte.
