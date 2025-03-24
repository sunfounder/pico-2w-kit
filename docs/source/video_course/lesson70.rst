.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Vertiefe dich in Raspberry Pi, Arduino und ESP32 zusammen mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Löse Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Promotionen und Gewinnspiele**: Nimm an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicke auf [|link_sf_facebook|] und trete heute bei!

Lektion 70:  Beispiel für das saubere Beenden eines Dual-Core-Programms in MicroPython
==========================================================================================

Dieses Tutorial behandelt die Verwendung von Threading zur Steuerung eines Servos und eines Buttons mit dem Raspberry Pi Pico W:

* **Verkabelungsaufbau**: Verbinde die Servosteuerung mit GPIO 17, die Stromversorgung an Pin 40 und Masse an Pin 38. Verbinde den Button mit GPIO 16 und Masse.
* **Codeimplementierung**: Importiere ``machine``, ``time``, ``_thread``, ``Servo``. Richte die Pins für Button und Servo ein. Implementiere einen Umschalter zur Steuerung der Servoposition. Verwende Threading für Servobewegungen und sauberes Beenden des Programms.
* **Hausaufgabe**: Modifiziere das Programm so, dass es sauber beendet wird, auch wenn es während einer Servobewegung unterbrochen wird.



**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/UHbboCxIOYE?si=eDDi-2mYO0LSWSLJ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
