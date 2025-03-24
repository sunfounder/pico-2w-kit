.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Vertiefen Sie Ihr Wissen über Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Promotionen und Giveaways**: Nehmen Sie an Giveaways und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_photoresistor:


2.12 Lichtempfindung
=========================

In dieser Lektion lernen wir, wie man einen **Fotowiderstand** (auch bekannt als lichtabhängiger Widerstand oder LDR) mit dem Raspberry Pi Pico 2 W verwendet, um die Lichtintensität zu messen. Ein Fotowiderstand ändert seinen Widerstand in Abhängigkeit von der Menge des empfangenen Lichts: je heller das Licht, desto geringer der Widerstand. Dies macht ihn ideal zur Erkennung von Veränderungen im Umgebungslicht.

* :ref:`cpn_photoresistor`

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
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_photoresistor`
        - 1
        - |link_photoresistor_buy|

**Schaltplan**

|sch_photoresistor|

In diesem Schaltkreis sind ein 10K-Widerstand und ein Fotowiderstand in Serie geschaltet und bilden einen Spannungsteiler. GP28 liest die Spannung über den Fotowiderstand, während der 10K-Widerstand als Schutz dient, indem er den Strom begrenzt.

* **Helles Licht**: Der Widerstand des Fotowiderstands verringert sich, was seine Spannung und den GP28-Wert senkt. Bei starkem Licht nähert sich sein Widerstand Null, und GP28 liest nahezu 0. In diesem Moment spielt der 10K-Widerstand eine schützende Rolle, sodass 3,3 V und GND nicht zusammen verbunden werden, was zu einem Kurzschluss führen würde.
* **Dunkelheit**: Der Widerstand des Fotowiderstands erhöht sich, was seine Spannung und den GP28-Wert erhöht. Bei völliger Dunkelheit ist sein Widerstand nahezu unendlich (der 10K-Widerstand ist vernachlässigbar), und GP28 liest nahezu 1023.

Die Berechnungsformel ist unten angegeben.

.. code-block::

  Digitalwert = (Analogspannung/3.3V) * 1023




**Verdrahtung**


|wiring_photoresistor|


**Code schreiben**


.. code-block:: Arduino

   const int sensorPin = 28;   // Fotowiderstand an GP28 (ADC2) angeschlossen

   void setup() {
     Serial.begin(115200);    // Initialisiere Serial Monitor
   }

   void loop() {
     // Lies den Analogwert vom Fotowiderstand
     int sensorValue = analogRead(sensorPin);
     // Drucke den Sensorwert auf den Serial Monitor
     Serial.println(sensorValue);
     delay(500);  // Warte eine halbe Sekunde, bevor erneut gelesen wird
   }

Wenn der Code läuft und der Serial Monitor geöffnet ist:

* Beobachtung der Sensorenwerte:

  Sie sollten eine Reihe von Zahlen sehen, die die analogen Werte vom Fotowiderstand darstellen.

* Interaktion mit dem Fotowiderstand:

  * Leuchte mit einer Taschenlampe oder einer Lampe auf den Fotowiderstand. Die Sensorenwerte sollten sinken (da der Widerstand mit mehr Licht abnimmt).
  * Bedecke den Fotowiderstand mit deiner Hand oder platziere ihn in einem dunklen Bereich. Die Sensorenwerte sollten steigen (da der Widerstand mit weniger Licht zunimmt).

**Code verstehen**

#. Sensor-Pin definieren:

   Weist sensorPin GPIO 28 zu, der mit dem analogen Eingang verbunden ist.

   .. code-block:: arduino

        const int sensorPin = 28;   // Fotowiderstand an GP28 (ADC2) angeschlossen

#. Serielle Kommunikation initialisieren:

   Startet die serielle Kommunikation, die es Ihnen ermöglicht, Nachrichten auf den Serial Monitor zu drucken.

   .. code-block:: arduino

        Serial.begin(115200);

#. Den Analogwert lesen:

   Liest die Analogspannung am sensorPin und gibt einen Wert zwischen 0 und 1023 zurück.

   .. code-block:: arduino

        int sensorValue = analogRead(sensorPin);

#. Sensorwert ausdrucken:

   Gibt den Sensorwert auf den Serial Monitor aus.

   .. code-block:: arduino

        Serial.println(sensorValue);

#. Eine Verzögerung hinzufügen:

   Wartet 500 Millisekunden vor der nächsten Messung.

   .. code-block:: arduino

        delay(500);

**Spannung umrechnen**

Wenn Sie den tatsächlich gelesenen Spannungswert sehen möchten, können Sie den Code wie folgt ändern:

.. code-block:: arduino

   const int sensorPin = 28;   // Fotowiderstand an GP28 (ADC2) angeschlossen

   void setup() {
     Serial.begin(115200);    // Initialisiere Serial Monitor
   }

    void loop() {
      int sensorValue = analogRead(sensorPin);
      // Wandle den Analogwert in Spannung um
      float voltage = sensorValue * (3.3 / 1023.0);
      Serial.print("Sensor Value: ");
      Serial.print(sensorValue);
      Serial.print("  Voltage: ");
      Serial.print(voltage);
      Serial.println(" V");
      delay(500);
    }

**Weitere Erkundungen**

* Ein LED steuern, abhängig vom Licht:

  Verwenden Sie den Fotowiderstand, um die Helligkeit einer LED zu steuern oder sie basierend auf Lichtniveaus ein- und auszuschalten.

* Datenaufzeichnung:

  Zeichnen Sie die Lichtintensität über die Zeit auf, um Änderungen in der Umgebung zu überwachen.

* Nachtlicht bauen:

  Erstellen Sie ein Licht, das sich automatisch einschaltet, wenn es dunkel wird.

**Schlussfolgerung**

In dieser Lektion haben Sie gelernt, wie man einen Fotowiderstand mit dem Raspberry Pi Pico verwendet, um die Lichtintensität zu messen. Indem Sie die analoge Spannung aus einem Spannungsteilerkreis lesen, können Sie Veränderungen in den Lichtverhältnissen erkennen und diese Informationen in Ihren Projekten nutzen.
