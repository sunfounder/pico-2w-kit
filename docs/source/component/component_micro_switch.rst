.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein – zusammen mit Gleichgesinnten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Erhalte Hilfe von unserer Community und unserem Team bei technischen Herausforderungen und Problemen nach dem Kauf.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Einblicke**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und Vorschauen.
    - **Spezielle Rabatte**: Profitiere von exklusiven Vergünstigungen auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nimm an Verlosungen und Sonderaktionen zu Feiertagen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _cpn_micro_switch:

Mikroschalter
========================

|img_micro_switch|

Der Aufbau eines Mikroschalters ist recht einfach. Die Hauptbestandteile des Schalters sind:

|img_micro_switch2|

* 1. Betätiger (Plunger)
* 2. Abdeckung
* 3. Bewegliches Element
* 4. Stütze
* 5. Gehäuse
* 6. NO-Anschluss: normalerweise offen
* 7. NC-Anschluss: normalerweise geschlossen
* 8. Kontakt
* 9. Beweglicher Arm

Sobald ein Mikroschalter physischen Kontakt mit einem Objekt herstellt, ändert sich die Position seiner Kontakte. Das grundlegende Funktionsprinzip ist wie folgt:

Wenn sich der Betätiger in der freigegebenen oder Ruhestellung befindet:

* Der normalerweise geschlossene Stromkreis kann Strom führen.
* Der normalerweise offene Stromkreis ist elektrisch isoliert.

Wenn der Betätiger gedrückt oder geschaltet wird:

* Der normalerweise geschlossene Stromkreis wird unterbrochen.
* Der normalerweise offene Stromkreis wird geschlossen.

|img_micro_switch1|

 **Beispiel**

* :ref:`py_micro` (Für MicroPython-Nutzer)
* :ref:`ar_micro` (Für Arduino-Nutzer)

.. * :ref:`per_service_bell` (Für Piper Make-Nutzer)
