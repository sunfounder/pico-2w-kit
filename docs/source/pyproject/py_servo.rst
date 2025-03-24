.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Vertiefe dich tiefer in Raspberry Pi, Arduino und ESP32 zusammen mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Löse Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Community und unserem Team.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Promotionen und Giveaways**: Nimm an Giveaways und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt heute bei!

.. _py_servo:

3.7 Schwingender Servo
==============================

In dieser Lektion lernen wir, wie man einen **Servomotor** mit dem Raspberry Pi Pico 2 W steuert. Ein Servomotor ist ein Gerät, das sich auf einen spezifischen Winkel zwischen 0° und 180° drehen kann. Er wird häufig in ferngesteuerten Spielzeugen, Robotern und anderen Anwendungen eingesetzt, die präzise Positionssteuerung erfordern.

Lass uns starten und den Servo hin und her schwingen lassen!

* :ref:`cpn_servo`

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
        - Micro USB-Kabel
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

* Das orangefarbene Kabel ist das Signalkabel und ist mit GP15 verbunden.
* Das rote Kabel ist VCC und mit VBUS(5V) verbunden.
* Das braune Kabel ist GND und mit GND verbunden.

Servos können, besonders unter Last, erheblichen Strom ziehen. Da wir einen kleinen Servo verwenden und ihn nicht stark belasten, ist es akzeptabel, ihn für dieses einfache Experiment über den VBUS-Pin des Pico zu versorgen. Für größere Servos oder mehrere Servos sollte eine externe Stromversorgung verwendet werden.

**Einrichten des Servoarms**

* Befestige den Servoarm (auch Horn genannt) auf der Ausgangswelle des Servos.
* Sichere ihn bei Bedarf mit der kleinen Schraube, die mit dem Servo geliefert wurde.

.. 1. Drücke den Servoarm auf die Ausgangswelle des Servos. Falls notwendig, fixiere ihn mit Schrauben.
.. #. Verbinde **VBUS** (nicht 3V3) und GND des Pico 2 W mit der Stromschiene des Breadboards.
.. #. Verbinde das rote Kabel des Servos mit der positiven Stromschiene mit einem Jumper.
.. #. Verbinde das gelbe Kabel des Servos mit dem GP15-Pin mit einem Jumperkabel.
.. #. Verbinde das braune Kabel des Servos mit der negativen Stromschiene mit einem Jumperkabel.

**Programmierung**

Wir schreiben ein MicroPython-Programm, um den Servo zwischen 0° und 180° hin und her schwingen zu lassen.

.. note::

    * Öffne die ``3.7_swinging_servo.py`` aus ``pico-2w-kit-main/micropython`` oder kopiere den Code in Thonny, dann klicke auf "Ausführen" oder drücke F5.
    * Stelle sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx. 
    

.. code-block:: python

    import machine
    import utime

    # Initialisiere PWM auf Pin GP15
    servo = machine.PWM(machine.Pin(15))
    servo.freq(50)  # Setze die Frequenz auf 50Hz

    # Funktion, um Winkel in Tastverhältnis umzurechnen
    def angle_to_duty(angle):
        min_duty = 1638  # Entsprechend einem 0,5ms Impuls (0°)
        max_duty = 8192  # Entsprechend einem 2,5ms Impuls (180°)
        duty = int(min_duty + (angle / 180) * (max_duty - min_duty))
        return duty

    while True:
        # Bewege den Servo von 0° zu 180°
        for angle in range(0, 181, 1):
            servo.duty_u16(angle_to_duty(angle))
            utime.sleep_ms(20)
        # Bewege den Servo von 180° zurück zu 0°
        for angle in range(180, -1, -1):
            servo.duty_u16(angle_to_duty(angle))
            utime.sleep_ms(20)

Wenn das Programm läuft, sollte der Servo reibungslos zwischen 0° und 180° hin und her schwingen.

**Verständnis des Codes**

#. Importiere Module:

   * ``machine``: Bietet Zugang zu hardwarebezogenen Funktionen.
   * ``utime``: Enthält zeitbezogene Funktionen für Verzögerungen.

#. Initialisiere PWM:

   Wir richten PWM auf GP15 ein.
   Die Frequenz ist auf 50Hz eingestellt, was für Servos üblich ist.

   .. code-block:: python

      servo = machine.PWM(machine.Pin(15))
      servo.freq(50)

#. Definiere die Funktion ``angle_to_duty``:

   * Diese Funktion bildet einen Winkel (0° bis 180°) auf den entsprechenden Tastverhältniswert für den Servo ab.
   * Die ``min_duty`` und ``max_duty`` entsprechen den minimalen und maximalen Impulsbreiten für das Servo-Steuersignal.
   * Die Berechnung skaliert den Winkel auf das entsprechende Tastverhältnis.

   .. code-block:: python

      def angle_to_duty(angle):
          min_duty = 1638  # 0,5ms Impulsbreite
          max_duty = 8192  # 2,5ms Impulsbreite
          duty = int(min_duty + (angle / 180) * (max_duty - min_duty))
          return duty
    
#. Hauptschleife zur Bewegung des Servos:

   * Der Servo bewegt sich von 0° bis 180°, wobei der Winkel jedes Mal um 1° erhöht wird.
   * Anschließend bewegt er sich von 180° zurück auf 0°.
   * ``utime.sleep_ms(20)`` fügt eine kleine Verzögerung hinzu, um die Bewegung zu glätten.

   .. code-block:: python

      while True:
          for angle in range(0, 181, 1):
              servo.duty_u16(angle_to_duty(angle))
              utime.sleep_ms(20)
          for angle in range(180, -1, -1):
              servo.duty_u16(angle_to_duty(angle))
              utime.sleep_ms(20)

**Mehr über den Code**

Servos werden durch das Senden eines PWM-Signals mit einer bestimmten Impulsbreite gesteuert.
Ein 50Hz PWM-Signal (Periodendauer von 20ms) ist Standard für Servos.
Die Impulsbreite innerhalb jeder Periode bestimmt den Winkel des Servos:

* 0,5ms Impulsbreite entspricht 0°.
* 1,5ms Impulsbreite entspricht 90°.
* 2,5ms Impulsbreite entspricht 180°.

Durch Anpassen des Tastverhältnisses des PWM-Signals ändern wir die Impulsbreite.

Die Funktion ``duty_u16()`` akzeptiert Werte von 0 bis 65535.
Um das Tastverhältnis für eine gegebene Impulsbreite zu berechnen:

.. code-block::

  Duty cycle = (Pulse Width / Period) * 65535

Beispielsweise für eine Impulsbreite von 0,5ms:

.. code-block::

  Duty cycle = (0.5ms / 20ms) * 65535 ≈ 1638

**Weitere Experimente**

* **Geschwindigkeit ändern**: Passe die Verzögerung ``utime.sleep_ms(20)`` an, um den Servo schneller oder langsamer zu bewegen.
* **Spezifische Winkel einstellen**: Modifiziere den Code, um den Servo auf spezifische Winkel zu bewegen.

  .. code-block:: python

    servo.duty_u16(angle_to_duty(90))  # Bewege auf 90°

* **Steuerung mit Eingabe**: Verbinde ein Potentiometer oder Tasten, um den Winkel des Servos interaktiv zu steuern.

**Wichtige Hinweise**

* **Stromversorgung**: Stelle sicher, dass der Servo ausreichend mit Strom versorgt wird. Wenn du Zittern oder unregelmäßige Bewegungen bemerkst, erwäge die Verwendung einer externen 5V-Stromversorgung für den Servo.
* **Überlastung vermeiden**: Zwinge den Servo nicht über seine physischen Grenzen hinaus (üblicherweise 0° bis 180°), um Schäden zu vermeiden.

**Fazit**

In dieser Lektion hast du gelernt, wie man einen Servomotor mit dem Raspberry Pi Pico 2 W steuert. Du verstehst jetzt, wie man PWM-Signale erzeugt, um den Winkel des Servos einzustellen und ihn sanft zu bewegen. Diese Fähigkeit ist grundlegend für Projekte in der Robotik und Automatisierung, bei denen präzise Bewegungen erforderlich sind.

