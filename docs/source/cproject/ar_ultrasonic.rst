.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Vertiefen Sie sich mit anderen Enthusiasten in die Welt von Raspberry Pi, Arduino und ESP32.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unserem Team.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_ultrasonic:

6.1 Distanzmessung mit einem Ultraschallsensor
================================================

In dieser Lektion lernen wir, wie man ein **Ultraschallsensormodul** mit dem Raspberry Pi Pico 2 W verwendet, um die Distanz zu einem Objekt zu messen. Ultraschallsensoren werden häufig in der Robotik und in Automatisierungssystemen für die Objekterkennung und Distanzmessung verwendet.

* :ref:`cpn_ultrasonic`

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

Sie können sie auch einzeln über die untenstehenden Links kaufen.


.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - KOMPONENTENEINFÜHRUNG
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
        - :ref:`cpn_ultrasonic`
        - 1
        - |link_ultrasonic_buy|

**Verständnis des Ultraschallsensors**

Der Ultraschallsensor funktioniert, indem er einen kurzen Ultraschallimpuls vom **Trig**-Pin aussendet und das Echo am **Echo**-Pin empfängt. Indem die Zeit gemessen wird, die das Echo für die Rückkehr benötigt, können wir die Distanz zu einem Objekt unter Verwendung der Schallgeschwindigkeit berechnen.

|ultrasonic_prin|

* **Triggerimpuls**: Ein 10-Mikrosekunden langer hoher Impuls am Trig-Pin initiiert die Messung.
* **Ultraschallburst**: Der Sensor sendet einen 8-Zyklus-Ultraschallburst mit 40 kHz aus.
* **Echorezeption**: Der Echo-Pin wird hochgeschaltet und bleibt hoch, bis das Echo zurück empfangen wird.
* **Zeitmessung**: Indem die Zeit gemessen wird, in der der Echo-Pin hoch bleibt, können wir die Distanz berechnen.

**Schaltplan**

|sch_ultrasonic|

**Verdrahtung**

|wiring_ultrasonic|

**Schreiben des Codes**

Wir werden ein Programm schreiben, das den Ultraschallsensor auslöst, die Echozeit misst und die Distanz zu einem Objekt berechnet. Die Distanz wird auf dem seriellen Monitor angezeigt.

.. note::

    * Sie können die Datei ``6.1_ultrasonic.ino`` unter dem Pfad ``pico-2w-kit-main/arduino/6.1_ultrasonic`` öffnen.
    * Oder kopieren Sie diesen Code in die **Arduino IDE**.
    * Vergessen Sie nicht, das Board (Raspberry Pi Pico) und den richtigen Port vor dem Klicken auf den **Upload**-Button auszuwählen.


.. code-block:: arduino

    // Definieren der Anschlusspins
    const int trigPin = 17;  // GPIO 17 -> Trig
    const int echoPin = 16;  // GPIO 16 -> Echo

    void setup() {
      // Serielle Kommunikation mit 115200 Baud starten
      Serial.begin(115200);

      // Sensorpins initialisieren
      pinMode(trigPin, OUTPUT);
      pinMode(echoPin, INPUT);
    }

    void loop() {
      long duration;
      float distance;

      // Den Sensor durch Setzen von Trig auf HIGH für 10 Mikrosekunden auslösen
      digitalWrite(trigPin, HIGH);
      delayMicroseconds(10);
      digitalWrite(trigPin, LOW);

      // Den Echo-Pin lesen, gibt die Dauer in Mikrosekunden zurück
      duration = pulseIn(echoPin, HIGH);

      // Die Distanz in Zentimetern berechnen
      distance = duration * 0.034 / 2;

      // Die Distanz auf dem seriellen Monitor ausgeben
      Serial.print("Distance: ");
      Serial.print(distance);
      Serial.println(" cm");

      delay(500); // Eine halbe Sekunde warten, bevor die nächste Messung erfolgt
    }

Nach dem Hochladen des Codes sollte der serielle Monitor die Distanzmessungen in Zentimetern anzeigen.

.. code-block:: 

    Distance: 25.3 cm
    Distance: 24.8 cm
    Distance: 24.5 cm

Platzieren Sie ein Objekt in verschiedenen Entfernungen vom Sensor.
Bewegen Sie das Objekt näher und weiter weg, um Änderungen in den Distanzmessungen zu beobachten.

**Verständnis des Codes**

#. Definieren der Anschlusspins:

   * ``trigPin``: Sendet den Ultraschallimpuls.
   * ``echoPin``: Empfängt das Echo des Ultraschallimpulses.

   .. code-block:: arduino

        const int trigPin = 17;  // GPIO 17 -> Trig
        const int echoPin = 16;  // GPIO 16 -> Echo

#. Setup-Funktion:

   * **Serielle Kommunikation**: Ermöglicht die Kommunikation zwischen dem Pico und dem Computer zur Fehlerbehebung.
   * **Pinmodi**: Setzt den ``Trig``-Pin als ``OUTPUT`` und den ``Echo``-Pin als ``INPUT``.

   .. code-block:: arduino

        void setup() {
          // Serielle Kommunikation mit 115200 Baud starten
          Serial.begin(115200);

          // Sensorpins initialisieren
          pinMode(trigPin, OUTPUT);
          pinMode(echoPin, INPUT);
        }

#. Loop-Funktion:

   * **Sensor auslösen**: Setzt den ``Trig``-Pin ``HIGH`` für 10 Mikrosekunden, um den Ultraschallimpuls zu senden. Setzt den ``Trig``-Pin ``LOW``, um den Impuls zu beenden.

     .. code-block:: arduino

        digitalWrite(trigPin, HIGH);
        delayMicroseconds(10);
        digitalWrite(trigPin, LOW);

   * **Echo lesen**: Misst die Dauer (in Mikrosekunden), die der ``Echo``-Pin ``HIGH`` bleibt, was die Zeit für die Rückkehr des Echos anzeigt.

     .. code-block:: arduino

        duration = pulseIn(echoPin, HIGH);

   * **Distanz berechnen**: Wandelt die Zeit in Distanz (cm/Mikrosekunde) um. Dividiert durch 2, um den Hin- und Rückweg des Impulses zu berücksichtigen.

     .. code-block:: arduino

        distance = duration * 0.034 / 2;

   * **Serielle Ausgabe**: Gibt die berechnete Distanz auf dem seriellen Monitor zur Echtzeitüberwachung aus.

     .. code-block:: arduino

        Serial.print("Distance: ");
        Serial.print(distance);
        Serial.println(" cm");

   * **Verzögerung**: Fügt eine 500-Millisekunden-Verzögerung hinzu, um den seriellen Monitor nicht zu überfluten und Zeit zwischen den Messungen zu lassen.

**Fehlerbehebung**

* Keine Anzeigen:

  * Stellen Sie sicher, dass die Trig- und Echo-Pins korrekt verbunden sind.
  * Überprüfen Sie, ob der Sensor Strom erhält (VCC- und GND-Verbindungen).
  * Überprüfen Sie, ob der serielle Monitor auf die richtige Baudrate eingestellt ist.

* Falsche Messungen:

  * Stellen Sie sicher, dass die Berechnungen im Code korrekt sind.
  * Überprüfen Sie, ob die Schallgeschwindigkeitskonstante (0.034) für Ihre Umgebung geeignet ist (Feuchtigkeit und Temperatur können die Schallgeschwindigkeit beeinflussen).


* Sensorinterferenzen:

  * Stellen Sie sicher, dass keine Hindernisse oder reflektierenden Flächen vorhanden sind, die die Ultraschallimpulse stören könnten.
  * Vermeiden Sie es, den Sensor in der Nähe anderer Ultraschallgeräte zu platzieren, die falsche Ablesungen verursachen könnten.


**Weiterführende Untersuchungen**

* Integration mit LEDs oder Displays:

  * Verwenden Sie mehrere LEDs, um einen visuellen Distanzindikator zu erstellen.
  * Integrieren Sie ein 7-Segment- oder LCD-Display, um die Distanz numerisch anzuzeigen.

* Erstellen eines Näherungsalarm-Systems:

  Setzen Sie Schwellenwerte, um Alarme auszulösen (z. B. Klangalarme, wenn Objekte zu nahe kommen).

* Bau eines einfachen hindernisvermeidenden Roboters:

  Nutzen Sie den Ultraschallsensor, um Hindernisse zu erkennen und sie zu umfahren.

**Fazit**

In dieser Lektion haben Sie gelernt, wie man ein Ultraschallsensormodul mit dem Raspberry Pi Pico zur Messung der Distanz zu einem Objekt verwendet. Durch das Auslösen von Ultraschallimpulsen und das Messen der Echozeit können Sie die Distanz zu nahen Objekten genau bestimmen. Dieses Projekt dient als Grundlage für komplexere Anwendungen in der Robotik, Automatisierung und interaktiven Systemen.
