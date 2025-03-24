.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein – zusammen mit Gleichgesinnten.

    **Why Join?**

    - **Expert Support**: Erhalte Unterstützung von unserer Community und unserem Team bei technischen Herausforderungen und Problemen nach dem Kauf.
    - **Learn & Share**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exclusive Previews**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Vorschauen.
    - **Special Discounts**: Profitiere von exklusiven Vergünstigungen auf unsere neuesten Produkte.
    - **Festive Promotions and Giveaways**: Nimm an Verlosungen und Sonderaktionen zu Feiertagen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _cpn_pir:

PIR-Bewegungssensor-Modul
==================================

|img_pir|

Der PIR-Sensor (Passive Infrared) erkennt Infrarotstrahlung und kann somit die Anwesenheit von wärmeemittierenden Lebewesen erfassen.

Der Sensor besitzt zwei Erfassungselemente, die mit einem Differenzverstärker verbunden sind. Befindet sich ein stationäres Objekt vor dem Sensor, empfangen beide Elemente eine gleiche Menge an Infrarotstrahlung, sodass der Ausgang 0 bleibt. Bewegt sich jedoch ein Objekt vor dem Sensor, nimmt ein Erfassungselement mehr Strahlung auf als das andere, wodurch ein Ungleichgewicht entsteht. Dies führt zu einer schwankenden Ausgangsspannung, die auf eine Bewegung hinweist.

|img_PIR_working_principle|

Nach dem Anschluss des Sensormoduls erfolgt eine etwa einminütige Initialisierung. Während dieser Zeit gibt das Modul in unregelmäßigen Abständen für 0–3 Zyklen ein Signal aus. Danach wechselt es in den Standby-Modus. Um Fehlfunktionen durch Störsignale zu vermeiden, sollte das Modul nicht direktem Licht oder anderen Störquellen ausgesetzt werden. Auch starke Luftströmungen können die Erkennung beeinträchtigen.

|img_pir_back|

**Entfernungseinstellung**

Durch Drehen des Potentiometers zur Einstellung der Reichweite im Uhrzeigersinn erhöht sich der Erfassungsbereich auf maximal 0–7 Meter. Dreht man es gegen den Uhrzeigersinn, wird der Bereich verkleinert, mit einer minimalen Reichweite von etwa 0–3 Metern.

**Verzögerungseinstellung**

Das Potentiometer für die Verzögerungseinstellung kann ebenfalls angepasst werden. Dreht man den Knopf im Uhrzeigersinn, erhöht sich die Verzögerungszeit auf maximal 300 Sekunden. Dreht man ihn gegen den Uhrzeigersinn, kann die Verzögerung auf ein Minimum von 5 Sekunden reduziert werden.

**Zwei Auslösemodi**

Der gewünschte Modus kann durch Setzen des Jumper-Käppchens ausgewählt werden.

* **H**: Wiederholbarer Auslösemodus – nach Erfassung eines Körpers gibt das Modul ein High-Signal aus. Bleibt eine Person während der Verzögerungszeit im Erfassungsbereich, bleibt das Signal auf High.
* **L**: Nicht wiederholbarer Auslösemodus – das Modul gibt ein High-Signal aus, sobald eine Bewegung erkannt wird. Nach Ablauf der Verzögerungszeit wechselt das Signal automatisch von High auf Low.

.. Example 
.. -------------------

.. :ref:`Intruder Alarm`


**Example**

* :ref:`py_pir` (Für MicroPython-Nutzer)
* :ref:`py_passage_counter` (Für MicroPython-Nutzer)
* :ref:`ar_pir` (Für Arduino-Nutzer)
.. * :ref:`per_lucky_cat` (Für Piper Make-Nutzer)
