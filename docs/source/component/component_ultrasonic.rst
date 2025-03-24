.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein – zusammen mit Gleichgesinnten.

    **Why Join?**

    - **Expert Support**: Löse Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Learn & Share**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exclusive Previews**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Vorschauen.
    - **Special Discounts**: Profitiere von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festive Promotions and Giveaways**: Nimm an Gewinnspielen und Sonderaktionen zu Feiertagen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _cpn_ultrasonic:

Ultraschallmodul
================================

|ultrasonic_pic|

* **TRIG**: Trigger-Puls-Eingang
* **ECHO**: Echo-Puls-Ausgang
* **GND**: Masse
* **VCC**: 5V Versorgungsspannung

Der **HC-SR04** Ultraschall-Distanzsensor ermöglicht berührungslose Entfernungsmessungen im Bereich von 2 cm bis 400 cm mit einer Genauigkeit von bis zu 3 mm.  
Das Modul integriert einen Ultraschallsender, einen Empfänger und eine Steuerschaltung für eine einfache Anwendung.

Es sind nur vier Anschlüsse erforderlich: VCC (Spannung), Trig (Trigger), Echo (Empfang) und GND (Masse), wodurch sich das Modul unkompliziert für Messprojekte einsetzen lässt.

**Eigenschaften**

* Betriebsspannung: DC 5V
* Betriebsstrom: 16mA
* Arbeitsfrequenz: 40Hz
* Maximale Reichweite: 500 cm
* Minimale Reichweite: 2 cm
* Trigger-Eingangssignal: 10 µs TTL-Puls
* Echo-Ausgangssignal: TTL-Pegel, proportional zur Entfernung
* Anschluss: XH2.54-4P
* Abmessungen: 46 x 20.5 x 15 mm

**Funktionsweise**

Das grundlegende Messprinzip lautet:

* Ein IO-Trigger wird für mindestens 10 µs mit einem High-Pegel angesteuert.
* Das Modul sendet eine 8-Zyklen-Ultraschallwelle mit 40 kHz aus und überprüft, ob ein Echo empfangen wird.
* Wenn ein Signal zurückkommt, gibt der Echo-Pin ein High-Signal aus. Die Dauer dieses Signals entspricht der Zeit vom Aussenden bis zur Rückkehr.
* Die Entfernung wird mit folgender Formel berechnet:

  Entfernung = (High-Pegel-Dauer × Schallgeschwindigkeit (340 m/s)) / 2

|ultrasonic_prin|

Berechnungsformeln:

* us / 58 = Entfernung in cm
* us / 148 = Entfernung in Zoll
* Entfernung = (High-Pegel-Dauer × 340 m/s) / 2

.. note::

     Dieses Modul sollte nicht unter Spannung angeschlossen werden. Falls erforderlich, sollte zuerst GND verbunden werden, um eine fehlerfreie Funktion zu gewährleisten.

     Das zu messende Objekt sollte eine Fläche von mindestens 0.5 m² haben und möglichst glatt sein, da unebene oder kleine Objekte das Messergebnis verfälschen können.

**Example**

* :ref:`py_ultrasonic` (Für MicroPython-Nutzer)
* :ref:`py_reversing_aid` (Für MicroPython-Nutzer)
* :ref:`py_iot_sunfounder_controller` (Für MicroPython-Nutzer)
* :ref:`ar_ultrasonic` (Für Arduino-Nutzer)
.. * :ref:`per_reversing_system` (Für Piper Make-Nutzer)
