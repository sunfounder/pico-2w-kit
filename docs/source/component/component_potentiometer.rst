.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein – zusammen mit Gleichgesinnten.

    **Why Join?**

    - **Expert Support**: Erhalte Unterstützung von unserer Community und unserem Team bei technischen Herausforderungen und Problemen nach dem Kauf.
    - **Learn & Share**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exclusive Previews**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Vorschauen.
    - **Special Discounts**: Profitiere von exklusiven Vergünstigungen auf unsere neuesten Produkte.
    - **Festive Promotions and Giveaways**: Nimm an Verlosungen und Sonderaktionen zu Feiertagen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _cpn_potentiometer:

Potentiometer
===============

|img_pot|

Ein Potentiometer ist ein verstellbarer Widerstand mit drei Anschlüssen, dessen Widerstandswert über einen Mechanismus oder ein Muster angepasst werden kann.

Potentiometer gibt es in verschiedenen Formen, Größen und Widerstandswerten, jedoch haben sie folgende gemeinsame Merkmale:

* Sie verfügen über drei Anschlüsse (Kontaktpunkte).
* Sie besitzen einen Drehknopf, eine Schraube oder einen Schieberegler, mit dem der Widerstand zwischen dem mittleren Anschluss und einem der äußeren Anschlüsse variiert werden kann.
* Der Widerstand zwischen dem mittleren Anschluss und einem der äußeren Anschlüsse ändert sich von 0 Ω bis zum maximalen Widerstandswert des Potentiometers, wenn der Knopf, die Schraube oder der Schieberegler bewegt wird.

Hier ist das Schaltzeichen eines Potentiometers:

|img_pot_symbol|


Die Funktionen des Potentiometers in einer Schaltung sind folgende:

#. Als Spannungsteiler 
   
    Ein Potentiometer ist ein stufenlos einstellbarer Widerstand. Durch Drehen der Achse oder Verschieben des Reglers bewegt sich der Kontakt auf dem Widerstandselement. Je nach angelegter Spannung und der Position des beweglichen Arms kann eine entsprechende Ausgangsspannung erzeugt werden.

#. Als verstellbarer Widerstand (Rheostat)  
   
    Wird das Potentiometer als verstellbarer Widerstand genutzt, verbindet man den mittleren Anschluss mit einem der beiden äußeren Anschlüsse. So lässt sich ein kontinuierlich variabler Widerstandswert innerhalb des gesamten Regelbereichs erzielen.

#. Als Stromregler  
   
    Wenn das Potentiometer als Stromregler fungiert, muss der Gleitkontakt als einer der Ausgangsanschlüsse verwendet werden.

Weitere Informationen über Potentiometer findest du unter: `Potentiometer - Wikipedia <https://en.wikipedia.org/wiki/Potentiometer.>`_

.. Example
.. -------------------

.. * :ref:`Turn the Knob` (Für MicroPython-Nutzer)
.. * :ref:`Table Lamp` (Für C/C++(Arduino)-Nutzer)


**Example**

* :ref:`py_pot` (Für MicroPython-Nutzer)
* :ref:`ar_pot` (Für Arduino-Nutzer)
.. * :ref:`per_swing_servo` (Für Piper Make-Nutzer)
