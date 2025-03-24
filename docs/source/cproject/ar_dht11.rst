.. note:: 

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein und tausche dich mit anderen Technikbegeisterten aus.

    **Warum beitreten?**

    - **Expertenunterstützung**: Erhalte Hilfe von unserer Community und unserem Team bei technischen Herausforderungen und nach dem Kauf auftretenden Problemen.
    - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Sonderrabatte**: Profitiere von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nimm an Verlosungen und Sonderaktionen während der Feiertage teil.

    👉 Bereit, mit uns zu experimentieren und kreativ zu werden? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _ar_dht11:


6.2 Temperatur und Luftfeuchtigkeit mit dem DHT11 messen
===========================================================

In dieser Lektion lernen wir, wie man einen **DHT11 Temperatur- und Luftfeuchtigkeitssensor** mit dem Raspberry Pi Pico 2 W verwendet. Der DHT11 ist ein kostengünstiger digitaler Sensor, der Umgebungstemperatur und Luftfeuchtigkeit misst und die Werte als kalibriertes Digitalsignal ausgibt.

|img_Dht11|

* :ref:`cpn_dht11`

**Benötigte Komponenten**

Für dieses Projekt werden die folgenden Komponenten benötigt.

Es ist praktisch, ein komplettes Kit zu kaufen. Hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ENTHALTENE TEILE
        - KAUFLINK
    *   - Pico 2 W Starter Kit	
        - 450+
        - |link_pico2w_kit|

Alternativ kannst du die Bauteile einzeln über die untenstehenden Links kaufen.


.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - KOMPONENTE	
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
        - :ref:`cpn_dht11`
        - 1
        - |link_dht22_buy|

**Funktionsweise des DHT11 Sensors**

Der **DHT11** Sensor nutzt einen kapazitiven Feuchtigkeitssensor und einen Thermistor, um die Umgebungsluft zu messen. Die Messwerte werden als digitales Signal über den Datenpin ausgegeben. Die Nutzung des Sensors ist relativ einfach, er erfordert jedoch eine präzise Zeitsynchronisation zur Datenübertragung.

* Temperaturbereich: 0–50 °C mit einer Genauigkeit von ±2 °C
* Luftfeuchtigkeitsbereich: 20–80 % RH mit einer Genauigkeit von ±5 %
* Abtastrate: 1 Hz (eine Messung pro Sekunde)

**Schaltplan**

|sch_dht11|

**Verdrahtung**

|wiring_dht11|


**Code schreiben**

Wir schreiben ein Programm, das Temperatur- und Luftfeuchtigkeitswerte vom DHT11-Sensor ausliest und auf dem Seriellen Monitor anzeigt.


.. note::

    * Du kannst die Datei ``6.2_dht11.ino`` unter dem Pfad ``pico-2w-kit-main/arduino/6.2_dht11`` öffnen.
    * Oder kopiere den Code in die **Arduino IDE**.
    * Wähle die Raspberry Pi Pico-Platine und den richtigen Port aus, bevor du auf die Upload-Schaltfläche klickst.
    * Die ``DHT sensor library`` wird benötigt. Installiere sie über den **Bibliotheksverwalter**.

      .. image:: img/lib_dht.png



.. code-block:: arduino

    #include <DHT.h>

    // Pin-Definition
    #define DHTPIN 16       // GPIO 16 -> Datenpin des DHT11
    #define DHTTYPE DHT11    // Sensortyp definieren

    // DHT-Objekt erstellen
    DHT dht(DHTPIN, DHTTYPE);

    unsigned long previousMillis = 0; // Speichert die letzte Aktualisierungszeit
    const long interval = 2000;        // Messintervall in Millisekunden

    void setup() {
      // Serielle Kommunikation initialisieren
      Serial.begin(115200);
      Serial.println(F("DHT11 Sensor Test!"));
    
      // DHT-Sensor initialisieren
      dht.begin();
   
    }

    void loop() {
      unsigned long currentMillis = millis();

      // Sensorwerte alle 2 Sekunden auslesen
      if (currentMillis - previousMillis >= interval) {
        previousMillis = currentMillis;

        // Luftfeuchtigkeit und Temperatur auslesen
        float humidity = dht.readHumidity();
        float temperatureC = dht.readTemperature();
        float temperatureF = dht.readTemperature(true);

        // Prüfen, ob die Messung fehlgeschlagen ist
        if (isnan(humidity) || isnan(temperatureC) || isnan(temperatureF)) {
          Serial.println(F("Failed to read from DHT sensor!"));
          return;
        }

        // Hitzeindex berechnen
        float heatIndexC = dht.computeHeatIndex(temperatureC, humidity, false);
        float heatIndexF = dht.computeHeatIndex(temperatureF, humidity);

        // Ergebnisse auf dem Seriellen Monitor ausgeben
        Serial.print(F("Humidity: "));
        Serial.print(humidity);
        Serial.print(F("%  Temperature: "));
        Serial.print(temperatureC);
        Serial.print(F("°C "));
        Serial.print(temperatureF);
        Serial.print(F("°F  Heat index: "));
        Serial.print(heatIndexC);
        Serial.print(F("°C "));
        Serial.print(heatIndexF);
        Serial.println(F("°F"));
      }
    }

Nach dem Hochladen des Codes werden Temperatur- und Luftfeuchtigkeitswerte alle zwei Sekunden im Seriellen Monitor angezeigt.

.. code-block::

    DHT11 Sensor Test!
    Humidity: 45.00%  Temperature: 25.00°C 77.00°F  Heat index: 25.00°C 77.00°F
    Humidity: 46.00%  Temperature: 25.50°C 78.00°F  Heat index: 25.50°C 78.00°F
    Humidity: 47.00%  Temperature: 26.00°C 79.00°F  Heat index: 26.00°C 79.00°F

* **Luftfeuchtigkeit**: Setze den Sensor unterschiedlichen Luftfeuchtigkeitswerten aus, um Veränderungen in den Messwerten zu beobachten. 
* **Temperatur**: Verändere die Umgebungstemperatur des Sensors, um die Temperaturmessungen zu beobachten.

**Den Code verstehen**

#. Bibliotheken einbinden und Konstanten definieren:

   * ``DHT.h``: Bindet die DHT-Sensorbibliothek ein, um die Kommunikation mit dem Sensor zu vereinfachen.
   * ``DHTPIN``: Gibt den GPIO-Pin an, der mit dem Datenpin des DHT11 verbunden ist.
   * ``DHTTYPE``: Definiert den verwendeten Sensortyp (in diesem Fall DHT11).

   .. code-block:: arduino

        #include <DHT.h>
        #define DHTPIN 16       // GPIO 16 -> Datenpin des DHT11
        #define DHTTYPE DHT11    // Sensortyp definieren

#. Das ``DHT`` -Objekt erstellen:

   Erstellt ein ``DHT`` -Objekt mit dem angegebenen Datenpin und Sensortyp.

   .. code-block:: arduino

        DHT dht(DHTPIN, DHTTYPE);

#. Setup-Funktion:

   * **Serielle Kommunikation**: Startet die serielle Kommunikation zur Datenanzeige und zum Debugging.
   * **Initialisierung des DHT-Sensors**: Bereitet den DHT11-Sensor für die Datenerfassung vor.

   .. code-block:: arduino

        void setup() {
          // Serielle Kommunikation mit 115200 Baud starten
          Serial.begin(115200);
          Serial.println(F("DHT11 Sensor Test!"));

          // DHT-Sensor initialisieren
          dht.begin();
        }

#. Loop-Funktion:

   * Zeitsteuerung mit ``millis()``: 
   
     Verwendet eine nicht-blockierende Zeitsteuerung, um den Sensor alle 2 Sekunden auszulesen (Intervall = 2000 Millisekunden).
   
     .. code-block:: arduino
   
        if (currentMillis - previousMillis >= interval) {
          previousMillis = currentMillis;
          ...
        }
   
   * Sensorwerte auslesen:
   
     * ``dht.readHumidity()``: Liest die aktuelle Luftfeuchtigkeit aus.
     * ``dht.readTemperature()``: Liest die aktuelle Temperatur in Celsius aus.
     * ``dht.readTemperature(true)``: Liest die aktuelle Temperatur in Fahrenheit aus.
   
   * Fehlerbehandlung:
   
     Überprüft, ob eine Messung fehlgeschlagen ist (NaN-Wert zurückgegeben) und gibt im Fehlerfall eine Meldung aus.
   
     .. code-block:: arduino
   
        if (isnan(humidity) || isnan(temperatureC) || isnan(temperatureF)) {
          Serial.println(F("Failed to read from DHT sensor!"));
          return;
        }
   
   * Hitzeindex berechnen:
   
     * ``dht.computeHeatIndex(temperatureC, humidity, false)``: Berechnet den Hitzeindex in Celsius.
     * ``dht.computeHeatIndex(temperatureF, humidity)``: Berechnet den Hitzeindex in Fahrenheit.
   
   * Daten ausgeben:
   
     Gibt die Luftfeuchtigkeit, die Temperatur in Celsius und Fahrenheit sowie den Hitzeindex auf dem Seriellen Monitor aus.
   
     .. code-block:: arduino
   
        Serial.print(F("Humidity: "));
        Serial.print(humidity);
        Serial.print(F("%  Temperature: "));
        Serial.print(temperatureC);
        Serial.print(F("°C "));
        Serial.print(temperatureF);
        Serial.print(F("°F  Heat index: "));
        Serial.print(heatIndexC);
        Serial.print(F("°C "));
        Serial.print(heatIndexF);
        Serial.println(F("°F"));

**Fehlersuche**

* Keine Messwerte angezeigt:

  * Überprüfe alle Verkabelungen.
  * Stelle sicher, dass der DHT11-Sensor mit Strom versorgt wird.
  * Kontrolliere, ob die richtigen GPIO-Pins im Code definiert sind.

* Falsche Messwerte:

  * Prüfe, ob der DHT11-Sensor beschädigt ist.
  * Überprüfe das Datenblatt des Sensors auf richtige Timing-Anforderungen.

* Störungen durch andere Geräte:

  * Platziere den Sensor nicht in der Nähe anderer elektronischer Geräte, die Störungen verursachen könnten.
  * Stelle sicher, dass keine Hindernisse die Messung des Sensors beeinflussen.

**Weiterführende Experimente**

* Integration mit Displays:

  Verbinde ein LCD- oder OLED-Display, um Temperatur- und Luftfeuchtigkeitswerte ohne den Seriellen Monitor anzuzeigen.

* Warnsysteme erstellen:

  Implementiere einen Summer oder eine Benachrichtigungsfunktion, die ausgelöst wird, wenn Temperatur oder Luftfeuchtigkeit einen bestimmten Schwellenwert überschreiten.

* Kombination mit anderen Sensoren:

  Kombiniere den DHT11 mit Bewegungssensoren, Lichtsensoren oder anderen Umweltsensoren, um ein umfassendes Überwachungssystem zu erstellen.

* Bau einer Wetterstation:

  Erweitere das Projekt durch zusätzliche Sensoren wie Barometer, Regenmesser und Windmesser, um eine vollwertige Wetterstation zu realisieren.

**Fazit**

In dieser Lektion hast du gelernt, wie du mit dem DHT11-Temperatur- und Luftfeuchtigkeitssensor den Raspberry Pi Pico zur Erfassung und Anzeige von Umgebungswerten nutzen kannst. Durch die DHT-Bibliothek kannst du Umweltdaten einfach in deine Projekte integrieren. Eine optionale LED-Anzeige bietet zudem eine visuelle Rückmeldung basierend auf den Sensormesswerten und erhöht so die Interaktivität deines Systems.
