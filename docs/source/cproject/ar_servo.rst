.. note::
      Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein, zusammen mit Gleichgesinnten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unserem Team.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_servo:

3.7 Schwingender Servo
=======================

In dieser Lektion lernen wir, wie man einen **Servomotor** mit dem Raspberry Pi Pico 2 W steuert. Ein Servomotor ist ein Gerät, das sich auf einen spezifischen Winkel zwischen 0° und 180° drehen kann. Er wird häufig in ferngesteuerten Spielzeugen, Robotern und anderen Anwendungen verwendet, die eine präzise Positionssteuerung erfordern.

Lassen Sie uns beginnen und den Servo hin und her schwingen lassen!

* :ref:`cpn_servo`

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
        - :ref:`cpn_servo`
        - 1
        - |link_servo_buy|

**Schaltplan**

|sch_servo|

**Verdrahtung**

|wiring_servo|

* Orangefarbenes Kabel ist das Signalkabel und verbunden mit GP15.
* Rotes Kabel ist VCC und verbunden mit VBUS(5V).
* Braunes Kabel ist GND und verbunden mit GND.

Servos können, besonders unter Last, erheblichen Strom ziehen. Da wir einen kleinen Servo verwenden und ihn nicht stark belasten, ist es akzeptabel, ihn für dieses einfache Experiment über den VBUS-Pin des Pico mit Strom zu versorgen. Bei größeren Servos oder mehreren Servos verwenden Sie eine externe Stromquelle.

**Einrichten des Servoarms**

* Befestigen Sie den Servoarm (auch als Horn bekannt) auf der Ausgangswelle des Servos.
* Sichern Sie ihn mit der kleinen Schraube, die mit dem Servo geliefert wurde, falls notwendig.

**Schreiben des Codes**


.. note::

    * Sie können die Datei ``3.7_swinging_servo.ino`` unter dem Pfad ``pico-2w-kit-main/arduino/3.7_swinging_servo`` öffnen. 
    * Oder kopieren Sie diesen Code in die **Arduino IDE**.
    * Vergessen Sie nicht, das Board (Raspberry Pi Pico) und den richtigen Port vor dem Klicken auf den **Upload**-Button auszuwählen.


.. code-block:: arduino

    #include <Servo.h>

    Servo myServo;  // Erstellen eines Servo-Objekts

    void setup() {
      myServo.attach(15);  // Befestigen des Servos an GPIO-Pin 15
    }

    void loop() {
      // Bewegen des Servos von 0 bis 180 Grad
      for (int angle = 0; angle <= 180; angle += 1) {
        myServo.write(angle);
        delay(15);  // Warten Sie 15 Millisekunden, bis der Servo die Position erreicht hat
      }
      // Bewegen des Servos von 180 bis 0 Grad
      for (int angle = 180; angle >= 0; angle -= 1) {
        myServo.write(angle);
        delay(15);
      }
    }

Nach dem Hochladen des Codes sollte der Servoarm reibungslos von 0° bis 180° und zurück schwingen.
Wenn sich der Servo nicht bewegt oder unregelmäßig verhält:

* Überprüfen Sie Ihre Verdrahtung.
* Stellen Sie sicher, dass der Servo ordnungsgemäß mit Strom versorgt wird.
* Achten Sie darauf, dass der Servo mechanisch nicht blockiert ist.

**Verständnis des Codes**

#. Einbinden der ``Servo`` -Bibliothek:

   Bindet die ``Servo`` -Bibliothek ein, die Funktionen zur Steuerung des Servomotors bietet.

   .. code-block:: arduino

        #include <Servo.h>

#. Erstellen eines ``Servo``-Objekts:

   Erstellt ein ``Servo``-Objekt namens ``myServo`` zur Steuerung des Servos.

   .. code-block:: arduino

        Servo myServo;

#. Befestigen des Servos an einem Pin:

   Befestigt den Servo an GPIO-Pin 15 am Pico.

   .. code-block:: arduino

        myServo.attach(15);

#. Bewegen des Servos:

   * Bewegt den Servo von 0° bis 180° in 1-Grad-Schritten. Die Verzögerung (15) bietet eine kleine Verzögerung, um dem Servo zu ermöglichen, jede Position reibungslos zu erreichen.
   
   .. code-block:: arduino

        for (int angle = 0; angle <= 180; angle += 1) {
          myServo.write(angle);
          delay(15);
        }

   * Umkehr der Bewegung: Bewegt den Servo zurück von 180° bis 0° und erzeugt eine hin- und her schwingende Bewegung.

   .. code-block:: arduino

        for (int angle = 180; angle >= 0; angle -= 1) {
          myServo.write(angle);
          delay(15);
        }

**Weitere Erkundungen**

* Geschwindigkeit anpassen:

  Ändern Sie den ``delay()``-Wert in den Schleifen, um den Servo schneller oder langsamer zu bewegen.

* Direkte Positionssteuerung:

  Verwenden Sie ``myServo.write(angle);`` mit einem bestimmten Winkel, um den Servo in eine feste Position zu setzen.

* Interaktive Steuerung:

  Schließen Sie ein Potentiometer an, um den Servowinkel interaktiv zu steuern.

**Fazit**

In dieser Lektion haben Sie gelernt, wie man einen Servomotor mit dem Raspberry Pi Pico und der Servo-Bibliothek steuert. Durch Anpassungen im Code können Sie den Servo auf jeden Winkel zwischen 0° und 180° einstellen, was eine präzise Steuerung in Ihren Projekten ermöglicht.
