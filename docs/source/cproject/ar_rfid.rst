.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Vertiefen Sie Ihr Wissen über Raspberry Pi, Arduino und ESP32 zusammen mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_rfid:


6.5 Verwendung von RFID
===========================================

In dieser Lektion werden wir die Nutzung von **Radiofrequenz-Identifikation (RFID)** Technologie mit dem Raspberry Pi Pico 2 W erkunden. RFID ermöglicht eine drahtlose Kommunikation zwischen einem Lesegerät und Tags, die zur Identifikation, Authentifizierung und Datenspeicherung verwendet werden können.

* :ref:`cpn_mfrc522`

**Erforderliche Komponenten**

Für dieses Projekt benötigen wir folgende Komponenten.

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
        - :ref:`cpn_mfrc522`
        - 1
        - |link_rfid_buy|

**Verständnis von RFID**

RFID-Technologie nutzt elektromagnetische Felder zur automatischen Identifikation und Verfolgung von Tags, die an Objekten angebracht sind. Die Tags enthalten elektronisch gespeicherte Informationen, die aus der Ferne ohne direkte Sichtlinie gelesen werden können.

* **RFID-Lesegerät (MFRC522):** Ein Gerät, das Radiowellen aussendet, um mit RFID-Tags zu kommunizieren.
* **RFID-Tag:** Ein kleines Objekt, wie eine Karte oder ein Schlüsselanhänger, das einen Mikrochip und eine Antenne enthält. Es kann passiv (ohne Batterie) oder aktiv (batteriebetrieben) sein.

**Schaltplan**

|sch_rfid|


**Verdrahtung**

|wiring_rfid|

**Schreiben des Codes**

Wir werden zwei Programme schreiben, die den MFRC522 RFID-Leser initialisieren, auf RFID-Tags hören und deren eindeutige Kennungen (UID) lesen.

**Code**

.. note::

   * Die ``MFRC522`` Bibliothek wird hier verwendet, Sie können sie aus dem **Bibliotheksmanager** installieren.

      .. image:: img/lib_mfrc522.png


1. Schreiben von Informationen auf RFID-Tags:

   .. note::
   
      * Sie können die Datei ``6.5_rfid_read.ino`` von ``pico-2w-kit-main/arduino/6.5_rfid_read`` öffnen. 
      * Oder kopieren Sie diesen Code in die **Arduino IDE**.
      * Wählen Sie das **Raspberry Pi Pico 2 W** Board und den richtigen Port, dann klicken Sie auf "Hochladen".
   
   .. code-block:: arduino
   
       #include <SPI.h>
       #include <MFRC522.h>
   
       // Definieren der Anschlusspins für das RFID-Modul
       #define SS_PIN 17    // SDA-Pin verbunden mit GPIO 17 (SPI SS)
       #define RST_PIN 9    – RST-Pin verbunden mit GPIO 9
   
       MFRC522 mfrc522(SS_PIN, RST_PIN); // Erstellen einer MFRC522-Instanz
   
       void setup() {
         // Initialisieren der seriellen Kommunikation
         Serial.begin(115200);
         while (!Serial); // Warten, bis der serielle Port verbunden ist
   
         // SPI-Bus initialisieren
         SPI.begin();
   
         // RFID-Lesegerät initialisieren
         mfrc522.PCD_Init();
         Serial.println("RFID Writer Initialized!");
   
       }
   
       void loop() {
         // Überprüfen, ob Daten im seriellen Puffer verfügbar sind
         if (Serial.available() > 0) {
           String data = Serial.readStringUntil('#'); // Lesen, bis '#' empfangen wird
           data.trim(); // Entfernen von nachfolgenden Leerzeichen
   
           // Warten auf eine neue RFID-Karte
           Serial.println("Place your RFID tag near the reader...");
           if ( ! mfrc522.PICC_IsNewCardPresent()) {
             return;
           }
   
           // Eine der Karten auswählen
           if ( ! mfrc522.PICC_ReadCardSerial()) {
             return;
           }
   
           // Authentifizieren mit Schlüssel A
           MFRC522::MIFARE_Key key;
           for (byte i = 0; i < 6; i++) {
             key.keyByte[i] = 0xFF;
           }
   
           byte block = 4; // Beispielblock zum Beschreiben
           byte sector = mfrc522.PICC_GetUid()->uidByte[0] % 32; // Sektor berechnen
   
           MFRC522::StatusCode status;
           status = mfrc522.PCD_Authenticate(MFRC522::PICC_CMD_MF_AUTH_KEY_A, block, &key, &(mfrc522.uid));
           if (status != MFRC522::STATUS_OK) {
             Serial.print("Authentication failed: ");
             Serial.println(mfrc522.GetStatusCodeName(status));
             return;
           }
   
           // Daten zum Schreiben vorbereiten (16 Bytes)
           byte buffer[18];
           data.getBytes(buffer, sizeof(buffer));
           buffer[16] = 0x00; // Auffüllen
           buffer[17] = 0x00; // Auffüllen
   
           // Daten in den Block schreiben
           status = mfrc522.MIFARE_Write(block, buffer, 16);
           if (status != MFRC522::STATUS_OK) {
             Serial.print("Write failed: ");
             Serial.println(mfrc522.GetStatusCodeName(status));
             return;
           }
   
           Serial.println("Data written successfully!");
         }
       }

   Nach dem Hochladen des Codes passiert Folgendes:
   
   * Im Seriellen Monitor sehen Sie:
   
     .. code-block::
   
        RFID Reader Initialized!
        Place your RFID tag near the reader...
   
   * Geben Sie die Daten ein, die Sie auf das RFID-Tag schreiben möchten, und enden Sie mit dem Zeichen „#“. Zum Beispiel:
   
     .. code-block::
   
        Hallo Welt#
   
   * Legen Sie das RFID-Tag in die Nähe des Lesers. Beachten Sie die Bestätigungsnachricht im Seriellen Monitor:
   
     .. code-block::
       
        Data written successfully!

2. Lesen von RFID-Tags:

   .. note::
   
      * Sie können die Datei ``6.5_rfid_read.ino`` von ``pico-2w-kit-main/arduino/6.5_rfid_read`` öffnen. 
      * Oder kopieren Sie diesen Code in die **Arduino IDE**.
      * Wählen Sie das **Raspberry Pi Pico 2 W** Board und den richtigen Port, dann klicken Sie auf "Hochladen".
   
   .. code-block:: arduino

        #include <SPI.h>
        #include <MFRC522.h>

        // Definieren der Anschlusspins für das RFID-Modul
        #define SS_PIN 17    – SDA-Pin verbunden mit GPIO 17 (SPI SS)
        #define RST_PIN 9    – RST-Pin verbunden mit GPIO 9

        MFRC522 mfrc522(SS_PIN, RST_PIN); // Erstellen einer MFRC522-Instanz

        void setup() {
          // Initialisieren der seriellen Kommunikation
          Serial.begin(115200);
          while (!Serial); // Warten, bis der serielle Port verbunden ist

          // SPI-Bus initialisieren
          SPI.begin();

          //  RFID-Lesegerät initialisieren
          mfrc522.PCD_Init();
          Serial.println("RFID Reader Initialized!");
        }

        void loop() {
          //  Nach neuen RFID-Karten suchen
          if ( ! mfrc522.PICC_IsNewCardPresent()) {
            return;
          }

          //  Eine der Karten auswählen
          if ( ! mfrc522.PICC_ReadCardSerial()) {
            return;
          }

          //  Die UID der Karte lesen
          Serial.print("UID-Tag :");
          String content= "";
          byte letter;
          for (byte i = 0; i < mfrc522.uid.size; i++) {
             content.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " "));
             content.concat(String(mfrc522.uid.uidByte[i], HEX));
          }
          Serial.println(content);

          //  Die zugehörigen Benutzerdaten drucken
          if (userData.length() > 0) {
            Serial.print("Associated Data: ");
            Serial.println(userData);
          } else {
            Serial.println("No data associated with this UID.");
          }
        }

   Nach dem Hochladen des Codes passiert Folgendes:
   
   * Im Seriellen Monitor sehen Sie:
   
     .. code-block::
   
        RFID Reader Initialized!
   
   * Legen Sie ein RFID-Tag (z. B. einen Schlüsselanhänger oder eine Karte) in die Nähe des MFRC522 RFID-Moduls. Der Serielle Monitor sollte sowohl die UID als auch die auf dem Tag gespeicherten Daten anzeigen:
   
     .. code-block::
   
        UID tag : 04 A3 1B 7C 3E
        Data on tag: HelloWorld

**Fehlerbehebung**

* Keine Anzeige von Messwerten:

  * Überprüfen Sie alle Verdrahtungsverbindungen, insbesondere die SPI-Leitungen (SCK, MOSI, MISO, SS).
  * Stellen Sie sicher, dass das RFID-Modul mit Strom versorgt wird (VCC- und GND-Verbindungen).
  * Überprüfen Sie, ob die richtigen GPIO-Pins im Code definiert sind.

* Falsche Messwerte:

  * Stellen Sie sicher, dass die RFID-Tags mit dem MFRC522-Modul kompatibel sind.
  * Verwenden Sie ein anderes RFID-Tag, um tag-spezifische Probleme auszuschließen.

* Schreibfehler:

  * Stellen Sie sicher, dass das RFID-Tag nicht gesperrt oder schreibgeschützt ist.
  * Überprüfen Sie, ob der Authentifizierungsschlüssel mit dem Schlüssel des Tags übereinstimmt.
  * Überprüfen Sie, ob der Datenpuffer korrekt formatiert ist und 16 Bytes nicht überschreitet.

* Signalstörungen:

  * Platzieren Sie das RFID-Modul nicht in der Nähe anderer elektronischer Geräte, die Störungen verursachen könnten.
  * Stellen Sie sicher, dass keine physischen Hindernisse die Kommunikation zwischen dem RFID-Tag und dem Lesegerät blockieren.

**Weitere Erkundungen**

* Zugangskontrollsysteme: 

  Implementieren Sie Türschlossmechanismen, die durch RFID-Tags gesteuert werden.

* Bestandsmanagement: 

  Verfolgen und verwalten Sie Bestandsgegenstände mit RFID-Tags für automatisiertes Zählen und Überwachen.

* RFID-basierte Authentifizierung:
  Erstellen Sie sichere Authentifizierungssysteme für Benutzeranmeldungen oder Gerätezugriffe.

* Kombination mit anderen Sensoren:

  Integrieren Sie RFID mit anderen Sensoren wie Temperatur- oder Bewegungssensoren für umfassende Überwachungssysteme.

**Fazit**

In dieser Lektion haben Sie gelernt, wie Sie ein RFID-System unter Verwendung des MFRC522 RFID-Moduls mit dem Raspberry Pi Pico anbinden. Durch die Nutzung des SPI-Kommunikationsprotokolls und der MFRC522-Bibliothek können Sie mühelos Daten auf RFID-Tags lesen und schreiben, was eine Vielzahl von Anwendungen wie Zugangskontrollsysteme, Bestandsmanagement und interaktive Projekte ermöglicht.
