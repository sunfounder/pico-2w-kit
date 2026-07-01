.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein – zusammen mit Gleichgesinnten.

    **Why Join?**

    - **Expert Support**: Erhalte Unterstützung von unserer Community und unserem Team bei technischen Herausforderungen und Problemen nach dem Kauf.
    - **Learn & Share**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exclusive Previews**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Vorschauen.
    - **Special Discounts**: Profitiere von exklusiven Vergünstigungen auf unsere neuesten Produkte.
    - **Festive Promotions and Giveaways**: Nimm an Gewinnspielen und Sonderaktionen zu Feiertagen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _cpn_ta6586:

TA6586 - Motortreiber-Chip
=================================

|img_ta6586|

Der TA6586 ist ein monolithischer IC zur Steuerung von bidirektionalen Gleichstrommotoren.  
Er verfügt über zwei Logikeingänge zur Steuerung der Bewegungsrichtung – vorwärts und rückwärts.  
Die Schaltung zeichnet sich durch eine gute Störfestigkeit, einen geringen Ruhestrom und einen 
niedrigen Ausgangssättigungsspannungsabfall aus.  
Eine integrierte Schutzdiode kompensiert die Induktionsströme beim Abschalten der Last, 
wodurch sich der Chip sicher und zuverlässig für den Betrieb von Relais, Gleichstrommotoren, 
Schrittmotoren oder für Schaltsteuerungen eignet.  
Der TA6586 wird häufig in Modellfahrzeugen, ferngesteuerten Flugzeugmotoren, automatischen 
Ventilsteuerungen, elektromagnetischen Schlössern sowie in Präzisionsinstrumenten und anderen 
Steuerungsschaltungen eingesetzt.

**Eigenschaften**

* Niedriger Ruhestrom: ≦2μA
* Weiter Versorgungsspannungsbereich
* Integrierte Bremsfunktion
* Überhitzungsschutz
* Überstrombegrenzung und Kurzschlussschutz
* DIP8 Pb-freies Gehäuse

**Pin-Funktion**

|img_ta6586_pin|


**Wahrheitstabelle der Eingänge**

|img_ta6586_priciple|


**Example**

* :ref:`py_motor` (Für MicroPython-Nutzer)
* :ref:`ar_motor` (Für Arduino-Nutzer)
* :ref:`py_pump` (Für MicroPython-Nutzer)
* :ref:`ar_pump` (Für Arduino-Nutzer)
* :ref:`py_iot_sunfounder_controller_plant` (Für MicroPython-Nutzer)

.. * :ref:`per_smart_fan` (Für Piper Make-Nutzer)
