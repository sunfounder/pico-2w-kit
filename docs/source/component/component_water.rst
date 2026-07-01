.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein – zusammen mit Gleichgesinnten.

    **Why Join?**

    - **Expert Support**: Löse Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Learn & Share**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exclusive Previews**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Vorschauen.
    - **Special Discounts**: Profitiere von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festive Promotions and Giveaways**: Nimm an Gewinnspielen und Sonderaktionen zu Feiertagen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _cpn_water_level:

Wasserstandssensor-Modul
=================================

|img_water_sensor|

Der Wasserstandssensor misst den Wasserstand und sendet das Signal an einen Controller.  
Der Controller vergleicht den gemessenen Wasserstand mit einem voreingestellten Wert und berechnet die Abweichung.  
Basierend auf dieser Abweichung gibt er Steuerbefehle aus, um das Zufuhrventil zu öffnen oder zu schließen,  
damit der Wasserstand im Behälter das gewünschte Niveau erreicht.

**Aufbau und Funktionsweise**  
Der Sensor verfügt über zehn freiliegende Kupferbahnen, bestehend aus fünf Versorgungsspuren und fünf Sensorschienen,  
die abwechselnd angeordnet sind.  

Sobald der Sensor in Wasser eingetaucht wird, werden die Bahnen überbrückt und es kann Strom fließen.  
Auf der Leiterplatte befindet sich zudem eine Betriebs-LED, die aufleuchtet, sobald der Sensor mit Strom versorgt wird.

Die Bahnen wirken als variabler Widerstand, dessen Widerstandswert sich je nach Eintauchtiefe ändert:

- Mehr Wasser → Erhöhte Leitfähigkeit → Niedrigerer Widerstand  
- Weniger Wasser → Reduzierte Leitfähigkeit → Höherer Widerstand  

Diese Widerstandsänderung wird in ein Spannungssignal umgewandelt und an einen Mikrocontroller gesendet.  
Der Mikrocontroller verarbeitet das Signal und bestimmt daraus den exakten Wasserstand.

.. warning:: 
    Der Sensor darf nicht vollständig in Wasser eingetaucht werden!  
    Nur der Bereich mit den zehn Messbahnen sollte mit Wasser in Kontakt kommen.  
    Zudem kann die Nutzung des Sensors in feuchter Umgebung die Korrosion der Kontakte beschleunigen  
    und die Lebensdauer verkürzen. Daher empfehlen wir, die Stromversorgung nur bei Messvorgängen zu aktivieren.

**Example**

* :ref:`py_water` (Für MicroPython-Nutzer)
* :ref:`py_iot_sunfounder_controller_plant` (Für MicroPython-Nutzer)
* :ref:`ar_water` (Für Arduino-Nutzer)

.. * :ref:`per_water_tank` (Für Piper Make-Nutzer)
