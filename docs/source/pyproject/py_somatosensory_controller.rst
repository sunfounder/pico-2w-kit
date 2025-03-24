.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt des Raspberry Pi, Arduino und ESP32 ein mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Löse Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Tutorials zur Verbesserung deiner Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Promotionen und Giveaways**: Nimm an Giveaways und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt heute bei!

.. _py_somato_controller:


7.11 Aufbau eines somatosensorischen Controllers
===================================================

In diesem spannenden Projekt werden wir einen **Somatosensorischen Controller** mit dem Raspberry Pi Pico 2 W, einem MPU6050-Beschleunigungsmesser und Gyroskopmodul sowie einem Servomotor erstellen. Dieses Gerät erfasst menschliche Bewegungen — speziell die Neigung deiner Hand — und übersetzt diese in Bewegungen des Servomotors. Diese Technologie ähnelt der, die in Robotik und Fernbedienungssystemen, wie chirurgischen Robotern oder Roboterarmen, verwendet wird.

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Es ist definitiv praktisch, ein ganzes Kit zu kaufen, hier ist der Link: 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ARTIKEL IN DIESEM KIT
        - LINK
    *   - Pico 2 W Starter Kit	
        - 450+
        - |link_pico2w_kit|

Du kannst sie auch einzeln über die untenstehenden Links kaufen.


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
    *   - 6
        - :ref:`cpn_servo`
        - 1
        - |link_servo_buy|

**Verständnis der Komponenten**

* **MPU6050 Beschleunigungsmesser und Gyroskop**: Ein 6-Achsen-Bewegungssensor, der Beschleunigung und Winkelgeschwindigkeit entlang der X-, Y- und Z-Achsen misst. Wir werden ihn verwenden, um die Neigung deiner Hand zu erkennen.
* **Servomotor**: Ein Motor, der gesteuert werden kann, um auf einen bestimmten Winkel zu bewegen. Wir werden ihn verwenden, um die Bewegung, die durch den MPU6050 erkannt wurde, nachzuahmen.

**Schaltplan**

|sch_somato|

Der MPU6050 berechnet den Einstellungswinkel basierend auf den Beschleunigungswerten in jeder Richtung.

Das Programm wird den Servo steuern, um den entsprechenden Ablenkwinkel als Einstellungswinkel zu machen.

**Verdrahtung**

|wiring_somatosensory_controller| 


**Schreiben des Codes**

Wir werden ein MicroPython-Skript schreiben, das:

* Beschleunigungsdaten vom MPU6050 liest.
* Den Neigungswinkel deiner Hand berechnet.
* Den Servomotor steuert, um die Neigung nachzuahmen.

.. note::

    * Öffne die ``7.11_somatosensory_controller.py`` aus ``pico-2w-kit-main/micropython`` oder kopiere den Code in Thonny, dann klicke auf "Ausführen" oder drücke F5.
    * Stelle sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx. 
    * Hier musst du die ``imu.py`` und ``vector3d.py`` verwenden, bitte überprüfe, ob sie auf den Pico hochgeladen wurden, für ein detailliertes Tutorial siehe :ref:`add_libraries_py`.

.. code-block:: python

    from imu import MPU6050
    from machine import I2C, Pin, PWM
    import utime
    import math

    # Initialisiere die I2C-Kommunikation für MPU6050
    i2c = I2C(1, scl=Pin(7), sda=Pin(6))
    mpu = MPU6050(i2c)

    # Initialisiere PWM für den Servomotor auf GP15
    servo = PWM(Pin(15))
    servo.freq(50)  # Setze Frequenz auf 50Hz für den Servo

    # Funktion, um den Winkel in PWM-Duty-Zyklus umzuwandeln
    def angle_to_duty(angle):
        # Wandle Winkel (0-180) in Duty-Zyklus um (0.5ms - 2.5ms Pulsbreite)
        # Duty-Zyklus-Bereich ist von 2% bis 12% für 0.5ms bis 2.5ms bei 50Hz
        duty_cycle = (angle / 18) + 2
        duty_u16 = int(duty_cycle / 100 * 65535)
        return duty_u16

    # Funktion, um den Neigungswinkel aus Beschleunigungsdaten zu bekommen
    def get_tilt_angle():
        accel = mpu.accel
        x = accel.x
        y = accel.y
        z = accel.z
        angle = math.atan2(y, z) * (180 / math.pi)
        return angle + 90  # Justiere Winkel von 0 bis 180

    # Hauptschleife
    try:
        while True:
            angle = get_tilt_angle()
            if angle < 0:
                angle = 0
            elif angle > 180:
                angle = 180
            duty = angle_to_duty(angle)
            servo.duty_u16(duty)
            utime.sleep(0.1)
    except KeyboardInterrupt:
        servo.deinit()
        print("Program stopped.")

Nachdem das Programm gestartet wurde, neige deine Hand auf und ab.
Der Servomotor sollte die Neigung nachahmen, indem er entsprechend bewegt wird.
Beobachte, wie der Servo auf deine Handbewegungen reagiert.

**Verständnis des Codes**

#. Initialisierung:

   * **I2C-Kommunikation**: Eingerichtet, um Daten vom MPU6050 zu lesen.
   * **Servomotor PWM**: Initialisiert auf GP15 mit einer Frequenz von 50Hz.

#. Winkelberechnung:

   * ``get_tilt_angle()``: Berechnet den Neigungswinkel basierend auf den Beschleunigungsmessungen. Der Winkel wird angepasst, um zwischen 0 und 180 Grad zu liegen.

   .. code-block:: python

        def get_tilt_angle():
            accel = mpu.accel
            x = accel.x
            y = accel.y
            z = accel.z
            angle = math.atan2(y, z) * (180 / math.pi)
            return angle + 90  # Justiere Winkel von 0 bis 180

#. Servosteuerung:

   * ``angle_to_duty(angle)``: Wandelt den Winkel in den entsprechenden PWM-Duty-Zyklus für den Servomotor um.
   * Duty-Zyklus-Berechnung: Der Servo erwartet Impulse zwischen 0.5ms (0 Grad) und 2.5ms (180 Grad) bei 50Hz.

   .. code-block:: python

        def angle_to_duty(angle):
            # Wandle Winkel (0-180) in Duty-Zyklus um (0.5ms - 2.5ms Pulsbreite)
            # Duty-Zyklus-Bereich ist von 2% bis 12% für 0.5ms bis 2.5ms bei 50Hz
            duty_cycle = (angle / 18) + 2
            duty_u16 = int(duty_cycle / 100 * 65535)
            return duty_u16

#. Hauptschleife:

   * Liest den Neigungswinkel.
   * Justiert den Winkel, um sicherzustellen, dass er zwischen 0 und 180 Grad liegt.
   * Stellt die Servoposition entsprechend ein.
   * Beinhaltet eine kurze Verzögerung, um Zittern zu vermeiden.
   * Erfasst eine Tastaturunterbrechung, um den Servo sicher zu deinitialisieren.

   .. code-block:: python

        try:
            while True:
                angle = get_tilt_angle()
                if angle < 0:
                    angle = 0
                elif angle > 180:
                    angle = 180
                duty = angle_to_duty(angle)
                servo.duty_u16(duty)
                utime.sleep(0.1)
        except KeyboardInterrupt:
            servo.deinit()
            print("Program stopped.")

**Fehlerbehebung**

* Servo bewegt sich nicht:

  * Überprüfe, ob der Servo korrekt mit Strom versorgt wird.
  * Stelle sicher, dass das Signalkabel an GP15 angeschlossen ist.
  * Überprüfe, ob die Masseverbindungen zwischen dem Pico und dem Servo verbunden sind.

* Ungenaue Bewegungen:

  * Stelle sicher, dass der MPU6050 sicher befestigt ist und nicht übermäßig wackelt.
  * Justiere die Winkelberechnungen bei Bedarf.

* Programmfehler:

  * Stelle sicher, dass imu.py und vector3d.py korrekt hochgeladen wurden.
  * Überprüfe auf Tippfehler oder Einrückungsfehler im Code.

**Erweiterungen und Verbesserungen**

* Steuerung mehrerer Servos:

  * Füge weitere Servos hinzu, um zusätzliche Bewegungsachsen zu steuern.
  * Erweitere den Code, um die Rotation um andere Achsen zu handhaben.

* Drahtlose Kommunikation:

  Verwende Bluetooth- oder WLAN-Module, um Sensordaten an ein anderes Gerät zu übertragen, das die Servos steuert.

* Daten Glättung:

  Implementiere Filter (z. B. Kalman-Filter), um die Sensordaten zu glätten.

* Visuelles Feedback:

  Füge ein OLED- oder LCD-Display hinzu, um Echtzeit-Winkeldaten anzuzeigen.

**Fazit**

Du hast erfolgreich einen Somatosensorischen Controller gebaut, der menschliche Bewegungen erfasst und in mechanische Bewegungen übersetzt. Dieses Projekt zeigt, wie Sensoren und Aktoren zusammenarbeiten können, um interaktive Systeme zu erstellen, ähnlich wie sie in der Robotik und bei Fernbedienungen verwendet werden.

Fühle dich frei, dieses Projekt durch Hinzufügen weiterer Funktionen oder die Integration in größere Systeme zu erweitern.
