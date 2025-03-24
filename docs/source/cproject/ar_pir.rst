.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Vertiefen Sie Ihr Wissen über Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Promotionen und Giveaways**: Nehmen Sie an Giveaways und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_pir:

2.10 Menschliche Bewegung erkennen
=======================================

In dieser Lektion lernen wir, wie man einen passiven Infrarot (PIR)-Sensor mit dem Raspberry Pi Pico 2 W verwendet, um menschliche Bewegungen zu erkennen. PIR-Sensoren werden häufig in Sicherheitssystemen, automatischer Beleuchtung und anderen Anwendungen verwendet, bei denen Bewegungserkennung erforderlich ist. Sie detektieren die von warmen Objekten wie Menschen oder Tieren abgegebene Infrarotstrahlung in ihrem Sichtfeld.

:ref:`cpn_pir`

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
        - :ref:`cpn_pir`
        - 1
        - |link_pir_buy|


**Schaltplan**

|sch_pir|

Wenn das PIR-Modul eine vorbeigehende Person erkennt, ist GP14 hoch, sonst ist es niedrig.

.. note::

    Der PIR-Sensor verfügt über zwei Potentiometer:

    * **Empfindlichkeitseinstellung**: Steuert den Erfassungsbereich.
    * **Zeitverzögerungseinstellung**: Steuert, wie lange der Ausgang nach der Bewegungserkennung HOCH bleibt.

    Für erste Tests drehen Sie beide Potentiometer gegen den Uhrzeigersinn auf ihre Mindestpositionen. Dies stellt den Sensor auf seine höchste Empfindlichkeit und die kürzeste Verzögerungseinstellung ein, sodass Sie sofortige Reaktionen beobachten können.

    |img_PIR_TTE|

**Verdrahtung**

|wiring_pir|

**Code schreiben**

.. note::

    * Sie können die Datei ``2.10_detect_human_movement.ino`` im Verzeichnis ``pico-2w-kit-main/arduino/2.10_detect_human_movement`` öffnen.
    * Oder kopieren Sie diesen Code in die **Arduino IDE**.
    * Vergessen Sie nicht, das Board (Raspberry Pi Pico) und den richtigen Port auszuwählen, bevor Sie auf den **Upload**-Button klicken.

.. code-block:: python

   const int pirPin = 14;     // PIR-Sensorausgangspin verbunden mit GP14
   int pirState = LOW;        // Aktueller Zustand des PIR-Sensors
   int val = 0;               // Variable zum Speichern des PIR-Wertes

   void setup() {
     Serial.begin(115200);    // Initialisieren des Serial Monitors
     pinMode(pirPin, INPUT);  // Setzen des PIR-Pins als Eingang
     Serial.println("PIR Sensor Test");
     delay(2000);             // Dem PIR-Sensor Zeit geben, sich zu stabilisieren
   }

   void loop() {
     val = digitalRead(pirPin);  // Lesen des PIR-Sensors

     if (val == HIGH) {
       if (pirState == LOW) {
         Serial.println("Motion detected!");
         pirState = HIGH;
       }
     } else {
       if (pirState == HIGH) {
         Serial.println("Motion ended!");
         pirState = LOW;
       }
     }
     delay(500);  // Eine halbe Sekunde warten, bevor erneut geprüft wird
   }

Wenn der Code läuft und der Serial Monitor offen ist:

* Bewegen Sie sich vor dem PIR-Sensor. Der Serial Monitor sollte "Bewegung erkannt!" anzeigen.
* Hören Sie auf sich zu bewegen oder bewegen Sie sich aus dem Erfassungsbereich des Sensors. Nach einer kurzen Verzögerung sollte der Serial Monitor "Bewegung beendet!" anzeigen.

**Verständnis des Codes**

#. Lesen des PIR-Sensors:

   Liest den aktuellen Zustand des PIR-Sensors. Er wird HIGH sein, wenn Bewegung erkannt wird und LOW, wenn keine Bewegung erkannt wird.

   .. code-block:: Arduino

      val = digitalRead(pirPin);

#. Bewegung erkennen:

   * Wenn Bewegung erkannt wird und es die erste Erkennung ist, wird "Bewegung erkannt!" gedruckt und pirState aktualisiert.
   * Wenn die Bewegung endet, wird "Bewegung beendet!" gedruckt und pirState aktualisiert.
  
   .. code-block:: Arduino

      if (val == HIGH) {
        if (pirState == LOW) {
          Serial.println("Motion detected!");
          pirState = HIGH;
        }
      } else {
        if (pirState == HIGH) {
          Serial.println("Motion ended!");
          pirState = LOW;
        }
      }


**Praktische Anwendungen**

* **Sicherheitssysteme**: Eindringlinge oder unbefugte Bewegungen erkennen.
* **Automatische Beleuchtung**: Lichter einschalten, wenn Bewegung erkannt wird.
* **Energieeinsparung**: Geräte abschalten, wenn für eine bestimmte Zeit keine Bewegung erkannt wird.

**Fehlerbehebungstipps**

* Falsche Auslösungen:

  * PIR-Sensoren können empfindlich auf Umweltfaktoren wie Temperaturänderungen oder Sonnenlicht reagieren.
  * Vermeiden Sie es, den Sensor direkt auf Wärmequellen oder Fenster zu richten.

* Sensor erkennt keine Bewegung:

  * Stellen Sie sicher, dass der Sensor Zeit zum Initialisieren hatte (einige Sensoren benötigen bis zu 60 Sekunden).
  * Stellen Sie den Empfindlichkeitspotentiometer ein.

* Interferenzen: 

  * Halten Sie den Sensor fern von Elektronik, die elektromagnetische Störungen verursachen könnte.

**Fazit**

In dieser Lektion haben Sie gelernt, wie Sie einen PIR-Sensor mit dem Raspberry Pi Pico verwenden, um menschliche Bewegungen zu erkennen. Sie haben die Hardware eingerichtet, Code geschrieben, um die Ausgabe des Sensors zu lesen, und ihn getestet, um auf Bewegungen zu reagieren. Das Verständnis, wie man die Einstellungen des PIR-Sensors anpasst, ermöglicht es Ihnen, ihn für Ihre spezifische Anwendung anzupassen, sei es für Sicherheit, Automatisierung oder interaktive Projekte.
