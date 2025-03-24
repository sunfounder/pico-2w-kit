.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein – zusammen mit Gleichgesinnten.

    **Why Join?**

    - **Expert Support**: Erhalte Unterstützung von unserer Community und unserem Team bei technischen Herausforderungen und Problemen nach dem Kauf.
    - **Learn & Share**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exclusive Previews**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Vorschauen.
    - **Special Discounts**: Profitiere von exklusiven Vergünstigungen auf unsere neuesten Produkte.
    - **Festive Promotions and Giveaways**: Nimm an Gewinnspielen und Sonderaktionen zu Feiertagen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _cpn_servo:

Servo
===========

|img_servo|

Ein Servomotor besteht typischerweise aus folgenden Komponenten: einem Gehäuse, einer Welle, einem Getriebesystem, einem Potentiometer, einem Gleichstrommotor und einer integrierten Steuerplatine.

**Funktionsweise**
- Der Mikrocontroller sendet PWM-Signale über den Signaldraht an das Servo.
- Die integrierte Steuerplatine im Servo interpretiert diese Signale und passt den Betrieb des Motors entsprechend an.
- Der Motor treibt das Getriebesystem an, das die Drehzahl reduziert und das Drehmoment erhöht, wodurch die Welle gedreht wird.
- Die Welle ist mechanisch mit dem Potentiometer verbunden. Während sich die Welle dreht, bewegt sich das Potentiometer und erzeugt ein Spannungssignal, das proportional zur Position der Welle ist.
- Dieses Rückmeldesignal wird an die Steuerplatine gesendet, die die aktuelle Position mit der Zielposition vergleicht.
- Basierend auf diesem Vergleich passt die Steuerung die Drehrichtung und Geschwindigkeit des Motors an, sodass das Servo präzise stoppt und die gewünschte Position hält.
- Dieses geschlossene Regelungssystem gewährleistet eine hohe Genauigkeit und Stabilität in der Bewegung des Servos.

|img_servo_i|

Der Drehwinkel des Servos wird durch die Dauer eines auf den Steuerdraht angelegten Impulses bestimmt. Dieses Verfahren nennt sich Pulsweitenmodulation (PWM).  
Das Servo erwartet alle 20 ms einen Impuls. Die Länge des Impulses bestimmt, wie weit sich der Motor dreht.  
Ein Impuls von 1,5 ms bringt den Motor in die 90-Grad-Position (Neutralstellung).  
Wird ein Impuls von weniger als 1,5 ms gesendet, dreht sich das Servo gegen den Uhrzeigersinn aus der Neutralposition.  
Ein Impuls, der breiter als 1,5 ms ist, bewirkt das Gegenteil.  
Die minimale und maximale Impulsbreite, die eine gültige Position steuert, hängt vom jeweiligen Servo ab.  
Typischerweise liegt die minimale Impulsbreite bei etwa 0,5 ms und die maximale bei 2,5 ms.

|img_servo_duty|


.. Example
.. -------------------

.. :ref:`Swinging Servo`

**Example**

* :ref:`py_servo` (Für MicroPython-Nutzer)
* :ref:`py_somato_controller` (Für MicroPython-Nutzer)
* :ref:`py_iot_sunfounder_controller` (Für MicroPython-Nutzer)
* :ref:`py_iot_ble_lock` (Für MicroPython-Nutzer)
* :ref:`ar_servo` (Für Arduino-Nutzer)
.. * :ref:`per_water_tank` (Für Piper Make-Nutzer)
.. * :ref:`per_swing_servo` (Für Piper Make-Nutzer)
.. * :ref:`per_lucky_cat` (Für Piper Make-Nutzer)
