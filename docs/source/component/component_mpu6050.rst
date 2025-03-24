.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein – zusammen mit Gleichgesinnten.

    **Why Join?**

    - **Expert Support**: Erhalte Unterstützung von unserer Community und unserem Team bei technischen Herausforderungen und Problemen nach dem Kauf.
    - **Learn & Share**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exclusive Previews**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Vorschauen.
    - **Special Discounts**: Profitiere von exklusiven Vergünstigungen auf unsere neuesten Produkte.
    - **Festive Promotions and Giveaways**: Nimm an Verlosungen und Sonderaktionen zu Feiertagen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _cpn_mpu6050:

MPU6050 Module
===========================

**MPU6050**

|img_mpu6050|

Der MPU-6050 ist ein 6-Achsen-Bewegungssensor, der ein 3-Achsen-Gyroskop und einen 3-Achsen-Beschleunigungssensor integriert.

Das Koordinatensystem des MPU-6050 ist wie folgt definiert:

Lege den MPU-6050 flach auf einen Tisch, mit der beschrifteten Oberfläche nach oben, sodass der Punkt in der oberen linken Ecke liegt. In dieser Ausrichtung:
- Die vertikale Aufwärtsrichtung ist die Z-Achse.
- Die Links-nach-Rechts-Richtung ist die X-Achse.
- Die Vorwärts-nach-Rückwärts-Richtung ist die Y-Achse.

|img_mpu6050_a| 


**3-axis Accelerometer**

Der Beschleunigungssensor basiert auf dem piezoelektrischen Effekt – der Fähigkeit 
bestimmter Materialien, unter mechanischer Belastung elektrische Ladung zu erzeugen.

Stelle dir eine rechteckige Box mit einer kleinen Kugel im Inneren vor, ähnlich wie 
in der obigen Abbildung. Die Wände dieser Box bestehen aus piezoelektrischen 
Kristallen. Wenn die Box geneigt wird, bewegt sich die Kugel aufgrund der 
Schwerkraft in die Richtung der Neigung. Die Wand, mit der die Kugel kollidiert, 
erzeugt dabei winzige piezoelektrische Ströme. Da die Box drei Paare gegenüberliegender 
Wände besitzt, entspricht jedes Paar einer Achse im 3D-Raum: X-, Y- und Z-Achse. 
Durch die Messung der erzeugten Ströme kann die Richtung und Stärke der Neigung 
bestimmt werden.

|img_mpu6050_a2|


Mit dem MPU6050 kann die Beschleunigung entlang jeder Koordinatenachse erfasst werden. 
Im stationären Zustand auf einem Tisch beträgt die Z-Achsen-Beschleunigung 1 Gravitationskraft (g), 
während die X- und Y-Achsen 0 g anzeigen. Bei einer Neigung oder einer Schwerelosigkeit-/Überlastungsbedingung 
ändern sich die entsprechenden Werte.

Es gibt vier programmierbare Messbereiche: ±2g, ±4g, ±8g und ±16g (Standard: ±2g). 
Die Messwerte liegen im Bereich von -32768 bis 32767.

Die Umrechnung eines Rohwertes des Beschleunigungssensors in eine tatsächliche 
Beschleunigung erfolgt nach folgender Formel:

Acceleration = (Beschleunigungssensor-Rohwert / 65536 \* voller Messbereich) g

Beispiel für die X-Achse: Wenn der Rohwert der X-Achse 16384 beträgt und der 
Messbereich auf ±2g eingestellt ist:

**Acceleration entlang der X-Achse = (16384 / 65536 \* 4) g**  **=1g**

**3-axis Gyroscope**

Gyroskope basieren auf dem Prinzip der Coriolis-Kraft. Stell dir eine gabelartige 
Struktur vor, die sich kontinuierlich vor- und zurückbewegt. Diese ist durch 
piezoelektrische Kristalle fixiert. Wenn du diese Anordnung kippst, erfahren die 
Kristalle eine Kraft in Richtung der Neigung. Dies geschieht aufgrund der Trägheit 
der beweglichen Gabel. Die Kristalle erzeugen dabei elektrische Ladung gemäß dem 
piezoelektrischen Effekt, welche anschließend verstärkt wird.

|img_mpu6050_g|

Das Gyroskop verfügt über vier programmierbare Messbereiche: ±250, ±500, ±1000 
und ±2000. Die Berechnungsmethode entspricht im Wesentlichen der für die 
Beschleunigung.

Die Umrechnung eines Rohwertes des Gyroskops in eine Winkelgeschwindigkeit 
erfolgt nach folgender Formel:

Angular velocity = (Gyroskop-Rohwert / 65536 \* voller Messbereich) °/s

Beispiel für die X-Achse: Wenn der Rohwert der X-Achse 16384 beträgt und der 
Messbereich auf ±250°/s eingestellt ist:

**Angular velocity entlang der X-Achse = (16384 / 65536 \* 500)°/s** **=125°/s**

**Example**

* :ref:`py_mpu6050` (Für MicroPython-Nutzer)
* :ref:`py_somato_controller` (Für MicroPython-Nutzer)
* :ref:`py_bubble_level` (Für MicroPython-Nutzer)
* :ref:`ar_mpu6050` (Für Arduino-Nutzer)
