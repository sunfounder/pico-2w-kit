.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein und tausche dich mit anderen Technikbegeisterten aus.

    **Warum beitreten?**

    - **Expertenunterstützung**: Erhalte Hilfe bei technischen Herausforderungen und Fragen nach dem Kauf von unserer Community und unserem Team.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Previews.
    - **Spezielle Rabatte**: Profitiere von exklusiven Vergünstigungen für unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nimm an Verlosungen und saisonalen Promotions teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _py_mpu6050:

6.3 6-Achsen-Bewegungserfassung
=====================================


In dieser Lektion lernen wir, wie der **MPU-6050** 6-Achsen-Bewegungssensor mit dem Raspberry Pi Pico 2 W verbunden wird. Der MPU-6050 kombiniert ein 3-Achsen-Gyroskop und einen 3-Achsen-Beschleunigungssensor und überträgt die Rohsensordaten über das I2C-Kommunikationsprotokoll.

* :ref:`cpn_mpu6050`


**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Es ist praktisch, ein komplettes Kit zu kaufen – hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ENTHALTENE ARTIKEL IM KIT
        - LINK
    *   - Pico 2 W Starter Kit	
        - 450+
        - |link_pico2w_kit|

Alternativ kannst du die Komponenten auch einzeln über die unten stehenden Links erwerben.


.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - KOMPONENTE	
        - MENGE
        - LINK

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

**Den MPU-6050-Sensor verstehen**

Der **MPU-6050**-Sensor wird häufig in Projekten zur Bewegungserfassung und Lagebestimmung eingesetzt, z. B. in Drohnen, Robotern und Gaming-Controllern.

* **Beschleunigungssensor**: Misst die Beschleunigungskräfte entlang der X-, Y- und Z-Achsen, einschließlich der Gravitationsbeschleunigung, um Neigung und Ausrichtung des Sensors zu bestimmen.
* **Gyroskop**: Misst die Rotationsgeschwindigkeit um die X-, Y- und Z-Achsen und liefert Informationen darüber, wie schnell sich der Sensor dreht.

**Schaltplan**

|sch_mpu6050_ar|


**Verkabelung**

|wiring_mpu6050_ar|

**Code schreiben**

Wir schreiben ein MicroPython-Skript, um Beschleunigungs- und Gyroskopdaten vom MPU-6050-Sensor auszulesen.

.. note::

    * Öffne die Datei ``6.3_6axis_motion_tracking.py`` aus ``pico-2w-kit-main/micropython`` oder kopiere den Code in Thonny, klicke auf "Run" oder drücke F5.

    * Stelle sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx.
    
    * Du benötigst die Dateien ``imu.py`` und ``vector3d.py`` – überprüfe, ob sie auf den Pico hochgeladen wurden. Eine detaillierte Anleitung findest du unter :ref:`add_libraries_py`.

.. code-block:: python

   from machine import I2C, Pin
   import utime
   from imu import MPU6050

   # Initialisierung der I2C-Schnittstelle (I2C0) mit SDA auf GP4 und SCL auf GP5
   i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)

   # Initialisierung des MPU-6050-Sensors
   mpu = MPU6050(i2c)

   def read_accelerometer():
      """Reads accelerometer data and returns it as a tuple (x, y, z)."""
      accel = mpu.accel
      return accel.x, accel.y, accel.z

   def read_gyroscope():
      """Reads gyroscope data and returns it as a tuple (x, y, z)."""
      gyro = mpu.gyro
      return gyro.x, gyro.y, gyro.z

   def main():
      """Main loop to read and print sensor data."""
      while True:
         # Beschleunigungsdaten lesen
         ax, ay, az = read_accelerometer()
         print("Accelerometer (g) - X: {:.3f}, Y: {:.3f}, Z: {:.3f}".format(ax, ay, az))
         
         # Pause for readability
         utime.sleep(0.5)
         
         # Gyroskopdaten lesen
         gx, gy, gz = read_gyroscope()
         print("Gyroscope (°/s) - X: {:.3f}, Y: {:.3f}, Z: {:.3f}".format(gx, gy, gz))
         
         # Pause before the next set of readings
         utime.sleep(0.5)

   # Hauptfunktion ausführen
   if __name__ == "__main__":
      main()


Das Skript gibt alle 0,5 Sekunden die Beschleunigungs- und Gyroskopwerte aus.

**Sensor-Daten verstehen**

* **Beschleunigungsausgabe**:

  .. code-block::

     Accelerometer (g) - X: 0.000, Y: 0.000, Z: 1.000

  Im Ruhezustand sollten X- und Y-Werte nahe 0 g liegen, während der Z-Wert aufgrund der Erdanziehung etwa 1 g beträgt.

* Gyroskopausgabe:

  .. code-block::

     Gyroscope (°/s) - X: 0.000, Y: 0.000, Z: 0.000

  Im Stillstand sollten die Gyroskopwerte nahe 0 °/s liegen. Beim Drehen des Sensors ändern sich die Werte entsprechend der Winkelgeschwindigkeit.


**Code verstehen**

#. Importe und Setup:

   * ``machine.I2C`` und ``machine.Pin``: Hardware-Schnittstelle
   * ``utime``: Zeitfunktionen
   * ``MPU6050``: Sensor-Klasse aus der ``imu.py``-Bibliothek

#. I2C-Initialisierung:

   Konfiguration des I2C-Busses 0 mit SDA auf GP4 und SCL auf GP5 bei einer Frequenz von 400 kHz.

   .. code-block:: python 

      i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)


#. Sensorinitialisierung:

   Erstellt eine Instanz des MPU-6050-Sensors über die I2C-Schnittstelle.

   .. code-block:: python

      mpu = MPU6050(i2c)

#. Beschleunigungssensordaten auslesen:

   Greift auf die Beschleunigungswerte zu und gibt die X-, Y- und Z-Werte zurück.

   .. code-block:: python

      def read_accelerometer():
         accel = mpu.accel
         return accel.x, accel.y, accel.z


#. Gyroskopdaten auslesen:
   
   Greift auf die Gyroskopwerte zu und gibt die X-, Y- und Z-Werte zurück.

   .. code-block:: python

      def read_gyroscope():
         gyro = mpu.gyro
         return gyro.x, gyro.y, gyro.z


#. Hauptschleife:

   * Liest die Beschleunigungsdaten aus und gibt sie aus.
   * Wartet 0,5 Sekunden.
   * Liest die Gyroskopdaten aus und gibt sie aus.
   * Wartet weitere 0,5 Sekunden und wiederholt den Vorgang.

   .. code-block:: python

      def main():
         while True:
            # Beschleunigungsdaten auslesen und ausgeben
            ax, ay, az = read_accelerometer()
            print("Accelerometer (g) - X: {:.3f}, Y: {:.3f}, Z: {:.3f}".format(ax, ay, az))
            
            utime.sleep(0.5)
            
            # Gyroskopdaten auslesen und ausgeben
            gx, gy, gz = read_gyroscope()
            print("Gyroscope (°/s) - X: {:.3f}, Y: {:.3f}, Z: {:.3f}".format(gx, gy, gz))
            
            utime.sleep(0.5)


#. Programmeinstiegspunkt:

   Stellt sicher, dass ``main()`` ausgeführt wird, wenn das Skript direkt gestartet wird.

   .. code-block:: python

      if __name__ == "__main__":
         main()


**Weitere Experimente**

* **Fokus auf einen Sensor**: Um entweder den Beschleunigungssensor oder das Gyroskop zu analysieren, kannst du die entsprechenden print-Anweisungen auskommentieren.
* **Datenvisualisierung**: Nutze Tools oder Software, um die Sensordaten in Echtzeit zu plotten und besser zu analysieren.
* **Orientierungsberechnung**: Implementiere Algorithmen zur Berechnung von Neigungs- und Rollbewegungen anhand der Beschleunigungsdaten.
* **Bewegungserkennung**: Entwickle ein Programm, das bei Überschreiten bestimmter Bewegungsschwellen eine Aktion ausführt.

**Sensordaten verstehen**

* Beschleunigungssensor:

  * Misst Beschleunigungskräfte in g (Gravitationskraft).
  * Nützlich zur Erkennung von Ausrichtung, Neigung und linearer Bewegung.

* Gyroskop:

  * Misst die Rotationsgeschwindigkeit in Grad pro Sekunde (°/s).
  * Nützlich zur Erfassung von Drehbewegungen und Winkelgeschwindigkeiten.

**Fehlersuche & Tipps**

* Keine Ausgabe oder Fehler:

  * Überprüfe die Verkabelung, insbesondere die SDA- und SCL-Leitungen.
  * Stelle sicher, dass der Sensor korrekt mit Strom versorgt wird.

* Statische Werte:

  * Falls sich die Werte beim Bewegen des Sensors nicht ändern, prüfe die Kabelverbindungen.
  * Vergewissere dich, dass die korrekte I2C-Adresse verwendet wird.

* Inkonsistente Messwerte:

  * Umgebungserschütterungen können die Sensorwerte beeinflussen.
  * Stelle den Sensor auf eine stabile Oberfläche während der Messungen.

**Fazit**

In dieser Lektion hast du gelernt, wie der MPU-6050-Beschleunigungs- und Gyroskopsensor mit dem Raspberry Pi Pico 2 W verbunden wird. Durch das Auslesen der Rohsensordaten kannst du eine Vielzahl von Anwendungen zur Bewegungserfassung und Orientierungserkennung entwickeln.
