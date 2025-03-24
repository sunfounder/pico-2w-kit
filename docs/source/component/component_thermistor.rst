.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein – zusammen mit Gleichgesinnten.

    **Why Join?**

    - **Expert Support**: Löse Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Learn & Share**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exclusive Previews**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Vorschauen.
    - **Special Discounts**: Profitiere von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festive Promotions and Giveaways**: Nimm an Gewinnspielen und Sonderaktionen zu Feiertagen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _cpn_thermistor:

Thermistor
===============

|img_thermistor|

Ein Thermistor ist eine Art Widerstand, dessen Widerstand stark temperaturabhängig ist – deutlich mehr als bei Standardwiderständen.  
Der Begriff setzt sich aus den Wörtern "Thermal" und "Resistor" zusammen.  
Thermistoren werden häufig als Einschaltstrombegrenzer, Temperatursensoren (typischerweise NTC-Typ),  
selbstrückstellende Überstromschutzvorrichtungen und selbstregulierende Heizelemente (typischerweise PTC-Typ) verwendet.

* `Thermistor - Wikipedia <https://en.wikipedia.org/wiki/Thermistor>`_

Hier ist das Schaltsymbol eines Thermistors:

|img_thermistor_symbol|

Thermistoren gibt es in zwei entgegengesetzten Grundtypen: 

* Mit NTC-Thermistoren nimmt der Widerstand mit steigender Temperatur ab, was in der Regel auf eine Zunahme der Leitungselektronen zurückzuführen ist, die durch thermische Anregung aus dem Valenzband in das Leitungsband übergehen. Ein NTC wird häufig als Temperatursensor oder in Serie mit einer Schaltung als Einschaltstrombegrenzer verwendet.

* Mit PTC-Thermistoren steigt der Widerstand mit zunehmender Temperatur, üblicherweise aufgrund verstärkter thermischer Gitterbewegungen, insbesondere durch Verunreinigungen und Materialfehler. PTC-Thermistoren werden häufig in Serie mit einer Schaltung eingesetzt und dienen als Überstromschutz, ähnlich wie rückstellbare Sicherungen.

In diesem Kit wird ein NTC-Thermistor verwendet. Jeder Thermistor hat einen spezifischen Nennwiderstand. Hier beträgt er 10 kΩ, gemessen bei 25°C.

Hier ist die Beziehung zwischen Widerstand und Temperatur:

    RT = RN * expB(1/TK - 1/TN)   

* **RT** ist der Widerstand des NTC-Thermistors bei der Temperatur TK.  
* **RN** ist der Widerstand des NTC-Thermistors bei der Referenztemperatur TN. Hier beträgt RN 10 kΩ.  
* **TK** ist die absolute Temperatur in Kelvin (K). Sie ergibt sich aus: TK = 273.15 + Temperatur in °C.  
* **TN** ist die Referenztemperatur in Kelvin. Hier gilt: TN = 273.15 + 25.  
* **B (Beta)** ist die Materialkonstante des NTC-Thermistors, auch Wärmesensitivitätsindex genannt, mit einem Wert von 3950.  
* **exp** steht für die Exponentialfunktion, wobei die Basis e die natürliche Zahl (≈ 2.7) ist.  

Um die Temperatur TK in Kelvin zu berechnen, kann die Formel umgestellt werden: TK = 1 / (ln(RT/RN) / B + 1/TN)  

Die Temperatur in Grad Celsius ergibt sich dann als: T(°C) = TK - 273.15  

Diese Beziehung ist eine empirische Formel und liefert präzise Ergebnisse nur innerhalb des effektiven Temperatur- und Widerstandsbereichs.

.. Example
.. -------------------

.. :ref:`Thermometer`


**Example**

* :ref:`py_temp` (Für MicroPython User)
* :ref:`py_room_temp` (Für MicroPython User)
* :ref:`ar_temp` (Für Arduino User)
