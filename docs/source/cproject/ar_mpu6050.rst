.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein, zusammen mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Löse Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Promotionen und Giveaways**: Nimm an Giveaways und Urlaubspromotionen teil.

    👉 Bereit, mit uns zu erkunden und zu erschaffen? Klicke auf [|link_sf_facebook|] und trete heute bei!

.. _ar_mpu6050:

6.3 Lesen vom MPU-6050
===============================

In dieser Lektion werden wir die Anbindung des **MPU-6050 6-Achsen-Bewegungssensors** an den Raspberry Pi Pico 2 W erlernen. Der MPU-6050 kombiniert ein 3-Achsen-Gyroskop und einen 3-Achsen-Beschleunigungssensor, die rohe Sensordaten über das I2C-Kommunikationsprotokoll bereitstellen.

* :ref:`cpn_mpu6050`

**Benötigte Komponenten**

Für dieses Projekt benötigen wir folgende Komponenten:

Es ist definitiv praktisch, ein gesamtes Kit zu kaufen, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ARTIKEL IN DIESEM KIT
        - KAUF-LINK
    *   - Pico 2 W Starter Kit	
        - 450+
        - |link_pico2w_kit|

Du kannst sie auch einzeln über die unten stehenden Links kaufen.


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
        - :ref:`cpn_mpu6050`
        - 1
        - 

**Verständnis des MPU-6050 Sensors**

Der **MPU-6050** Sensor wird weit verbreitet in Projekten verwendet, die Bewegungstracking und Orientierungserkennung benötigen, wie z.B. bei Drohnen, Robotik und Gaming-Geräten.

* **Beschleunigungsmesser**: Misst Beschleunigungskräfte entlang der X-, Y- und Z-Achsen. Dazu gehört auch die Gravitationsbeschleunigung, was es ermöglicht, die Neigung oder Orientierung des Sensors zu bestimmen.
* **Gyroskop**: Misst die Rotationsgeschwindigkeit um die X-, Y- und Z-Achsen, was Informationen darüber liefert, wie schnell der Sensor sich dreht.

**Schaltplan**

|sch_mpu6050_ar|

**Verdrahtung**

|wiring_mpu6050_ar|

**Code schreiben**

Wir werden ein Programm schreiben, das den MPU-6050 Sensor initialisiert, Beschleunigungs- und Gyroskopdaten liest und die Werte im Seriellen Monitor ausgibt.

.. note::

    * Du kannst die Datei ``6.3_6axis_motion_tracking.ino`` im Pfad ``pico-2w-kit-main/arduino/6.3_6axis_motion_tracking`` öffnen. 
    * Oder kopiere diesen Code in die **Arduino IDE**.
    * Wähle dann das Raspberry Pi Pico Board und den richtigen Port aus, bevor du auf den Upload-Button klickst.
    * Die ``Adafruit MPU6050`` Bibliothek wird hier verwendet, du kannst sie aus dem **Library Manager** installieren.

      .. image:: img/lib_mpu6050.png


.. code-block:: arduino

    #include <Adafruit_MPU6050.h>
    #include <Wire.h>

    // Erstelle ein MPU6050 Objekt
    Adafruit_MPU6050 mpu;

    void setup(void) {
      // Initialisiere die serielle Kommunikation
      Serial.begin(115200);

      Serial.println("Adafruit MPU6050 test!");

      // Versuche den MPU6050 zu initialisieren
      if (!mpu.begin()) {
        Serial.println("Failed to find MPU6050 chip");
        while (1) {
          delay(10);
        }
      }
      Serial.println("MPU6050 gefunden!");

      // Stelle den Beschleunigungsmesserbereich ein
      mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
      Serial.print("Accelerometer range set to: ");
      switch (mpu.getAccelerometerRange()) {
        case MPU6050_RANGE_2_G:
          Serial.println("+-2G");
          break;
        case MPU6050_RANGE_4_G:
          Serial.println("+-4G");
          break;
        case MPU6050_RANGE_8_G:
          Serial.println("+-8G");
          break;
        case MPU6050_RANGE_16_G:
          Serial.println("+-16G");
          break;
      }

      // Stelle den Gyroskopbereich ein
      mpu.setGyroRange(MPU6050_RANGE_500_DEG);
      Serial.print("Gyro range set to: ");
      switch (mpu.getGyroRange()) {
        case MPU6050_RANGE_250_DEG:
          Serial.println("+-250 deg/s");
          break;
        case MPU6050_RANGE_500_DEG:
          Serial.println("+-500 deg/s");
          break;
        case MPU6050_RANGE_1000_DEG:
          Serial.println("+-1000 deg/s");
          break;
        case MPU6050_RANGE_2000_DEG:
          Serial.println("+-2000 deg/s");
          break;
      }

      // Stelle die Filterbandbreite ein
      mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);
      Serial.print("Filter bandwidth set to: ");
      switch (mpu.getFilterBandwidth()) {
        case MPU6050_BAND_260_HZ:
          Serial.println("260 Hz");
          break;
        case MPU6050_BAND_184_HZ:
          Serial.println("184 Hz");
          break;
        case MPU6050_BAND_94_HZ:
          Serial.println("94 Hz");
          break;
        case MPU6050_BAND_44_HZ:
          Serial.println("44 Hz");
          break;
        case MPU6050_BAND_21_HZ:
          Serial.println("21 Hz");
          break;
        case MPU6050_BAND_10_HZ:
          Serial.println("10 Hz");
          break;
        case MPU6050_BAND_5_HZ:
          Serial.println("5 Hz");
          break;
      }

      Serial.println("");
      delay(100);
    }

    void loop() {
      // Hole neue Sensorevents mit den Messwerten
      sensors_event_t a, g, temp;
      mpu.getEvent(&a, &g, &temp);

      // Drucke Beschleunigungswerte
      Serial.print("Acceleration X: ");
      Serial.print(a.acceleration.x);
      Serial.print(" m/s^2, Y: ");
      Serial.print(a.acceleration.y);
      Serial.print(" m/s^2, Z: ");
      Serial.print(a.acceleration.z);
      Serial.println(" m/s^2");

      // Print gyroscope values
      Serial.print("Rotation X: ");
      Serial.print(g.gyro.x);
      Serial.print(" rad/s, Y: ");
      Serial.print(g.gyro.y);
      Serial.print(" rad/s, Z: ");
      Serial.print(g.gyro.z);
      Serial.println(" rad/s");

      delay(500); // Passe die Verzögerung bei Bedarf an
    }


Nach dem Hochladen des Codes sollte der Serielle Monitor kontinuierlich die Beschleunigungs- und Rotationswerte anzeigen.

.. code-block::

    Adafruit MPU6050 test!
    MPU6050 Found!
    Accelerometer range set to: +-8G
    Gyro range set to: +-500 deg/s
    Filter bandwidth set to: 21 Hz

    Acceleration X: 0.00 m/s^2, Y: 0.00 m/s^2, Z: 9.81 m/s^2
    Rotation X: 0.02 rad/s, Y: -0.01 rad/s, Z: 0.00 rad/s
    Acceleration X: 0.10 m/s^2, Y: 0.05 m/s^2, Z: 9.76 m/s^2
    Rotation X: 0.15 rad/s, Y: -0.05 rad/s, Z: 0.02 rad/s

Bewege oder drehe das MPU-6050 Sensor-Modul vorsichtig.
Beobachte die Veränderungen in den Beschleunigungs- und Rotationswerten, die den Bewegungen entsprechen.

**Verständnis des Codes**

#. Einbinden der Bibliotheken und Definition der Konstanten:


   * ``Adafruit_MPU6050.h``: Bindet die MPU6050-Bibliothek ein, um die Schnittstelle zu erleichtern.
   * ``Wire.h``: Bindet die I2C-Kommunikationsbibliothek ein.
   * ``mpu``: Erstellt ein MPU6050-Objekt, um mit dem Sensor zu interagieren.

#. Setup-Funktion:

   * MPU6050-Initialisierung:

     Versucht, den MPU6050-Sensor zu initialisieren. Wenn dies nicht erfolgreich ist, wird eine Fehlermeldung ausgegeben und das Programm angehalten.

     .. code-block:: arduino

         Serial.println("Adafruit MPU6050 test!");

         // Versuche den MPU6050 zu initialisieren
         if (!mpu.begin()) {
           Serial.println("Failed to find MPU6050 chip");
           while (1) {
             delay(10);
           }
         }
         Serial.println("MPU6050 Found!");

   * Beschleunigungsmesserbereich:

     Stellt den Beschleunigungsmesserbereich auf ±8G ein und gibt den aktuellen Bereich aus.

     .. code-block:: arduino

         mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
         Serial.print("Accelerometer range set to: ");
         switch (mpu.getAccelerometerRange()) {
           case MPU6050_RANGE_2_G:
             Serial.println("+-2G");
             break;
            ...
           case MPU6050_RANGE_16_G:
             Serial.println("+-16G");
             break;
         }

   * Gyroskopbereich:

     Stellt den Gyroskopbereich auf ±500 Grad pro Sekunde ein und gibt den aktuellen Bereich aus.

     .. code-block:: arduino

         mpu.setGyroRange(MPU6050_RANGE_500_DEG);
         Serial.print("Gyro range set to: ");
         switch (mpu.getGyroRange()) {
           case MPU6050_RANGE_250_DEG:
             Serial.println("+-250 deg/s");
             break;
            ...
           case MPU6050_RANGE_2000_DEG:
             Serial.println("+-2000 deg/s");
             break;
         }

   * Einstellung der Filterbandbreite:

     Konfiguriert die Filterbandbreite auf 21 Hz, um Rauschen zu reduzieren, und gibt die aktuelle Einstellung aus.

     .. code-block:: arduino

         mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);
         Serial.print("Filter bandwidth set to: ");
         switch (mpu.getFilterBandwidth()) {
           case MPU6050_BAND_260_HZ:
             Serial.println("260 Hz");
             break;
            ...
           case MPU6050_BAND_5_HZ:
             Serial.println("5 Hz");
             break;
         }

#. Loop-Funktion:

   * Auslesen der Sensordaten:

     * ``sensors_event_t a, g, temp;``: Erstellt Ereignisobjekte, um Beschleunigungs-, Gyroskop- und Temperaturdaten zu speichern.
     * ``mpu.getEvent(&a, &g, &temp);``: Ruft die neuesten Sensordaten ab.

     .. code-block:: arduino

         sensors_event_t a, g, temp;
         mpu.getEvent(&a, &g, &temp);

   * Ausgabe der Sensordaten:

     * **Beschleunigung**: Gibt Beschleunigungswerte entlang der X-, Y- und Z-Achsen in Metern pro Sekunde im Quadrat (m/s²) aus.
     * **Rotation**: Gibt Gyroskopwerte (Rotationsgeschwindigkeit) um die X-, Y- und Z-Achsen in Radianten pro Sekunde (rad/s) aus.

     .. code-block:: Arduino

       // Drucke Beschleunigungswerte
       Serial.print("Acceleration X: ");
       Serial.print(a.acceleration.x);
       ...
       Serial.print(g.gyro.y);
       Serial.print(" rad/s, Z: ");
       Serial.print(g.gyro.z);
       Serial.println(" rad/s");


**Fehlerbehebung**

* Keine Anzeige von Messwerten:

  * Überprüfe alle Verdrahtungsverbindungen, insbesondere die I2C-Leitungen (SCL und SDA).
  * Stelle sicher, dass der MPU6050-Sensor mit Strom versorgt wird (VCC- und GND-Verbindungen).
  * Überprüfe, ob die richtigen GPIO-Pins im Code definiert sind.

* Falsche Messwerte:

  * Stelle sicher, dass der MPU6050-Sensor richtig im Steckbrett sitzt.
  * Überprüfe, ob die Bereichs- und Filtereinstellungen des Sensors der gewünschten Anwendung entsprechen.
  * Überprüfe auf lose Verbindungen oder Kurzschlüsse in der Verdrahtung.

* Sensorinterferenzen:

  * Vermeide es, den Sensor in der Nähe anderer elektronischer Geräte zu platzieren, die Störungen verursachen könnten.
  * Stelle sicher, dass keine physischen Hindernisse die Bewegung des Sensors blockieren.

**Weitere Erkundungen**

* Kombination mit anderen Sensoren:

  Integriere den MPU6050 mit GPS-Modulen, Magnetometern oder anderen Sensoren, um umfassende Trackingsysteme zu erstellen.

* Bau eines bewegungsbasierten Spielcontrollers:

  Verwende den MPU6050, um Bewegungen und Orientierungen zu erkennen, was die Erstellung von bewegungsgesteuerten Spielgeräten ermöglicht.

* Bau eines selbstbalancierenden Roboters:

  Nutze die Beschleunigungs- und Gyroskopdaten, um Balance und Stabilität in Roboteranwendungen zu gewährleisten.

* Implementierung von Sensorfusionsalgorithmen:

  Kombiniere Beschleunigungs- und Gyroskopdaten, um Orientierungswinkel mithilfe von Algorithmen wie dem Kalman-Filter oder dem Komplementärfilter zu berechnen.

**Fazit**

In dieser Lektion hast du gelernt, wie man den MPU6050 6-Achsen-Bewegungssensor mit dem Raspberry Pi Pico anbindet. Durch die Nutzung der Adafruit MPU6050-Bibliothek kannst du einfach Beschleunigungs- und Gyroskopdaten abrufen und interpretieren, was eine Vielzahl von Bewegungs- und Orientierungsanwendungen ermöglicht. Die optionale LED-Anzeige bietet eine einfache Möglichkeit, visuelles Feedback basierend auf den Sensordaten zu geben, was die Interaktivität deiner Projekte erhöht.
