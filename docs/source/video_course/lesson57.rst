.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt des Raspberry Pi, Arduino und ESP32 zusammen mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Expertenunterstützung**: Löse Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Promotionen und Gewinnspiele**: Nimm an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicke auf [|link_sf_facebook|] und trete heute bei!

Lektion 57: Kalibrierung eines Joysticks in MicroPython
=============================================================================

Dieses Tutorial behandelt die Kalibrierung eines Joysticks mit dem Raspberry Pi Pico W:

* **Verkabelungsaufbau**: Verbinde den Ground mit Pin 38, 3.3V mit Pin 36, VRX mit GPIO-Pin 27 und VRY mit GPIO-Pin 26.
* **Codeimplementierung**: Importiere ``machine``, ``time``, ``math``; richte den ADC für die Joystickachsen ein; lese und drucke die Joystickwerte.
* **Kalibrierung**: Konvertiere die rohen ADC-Werte in eine Skala von -100 bis +100, unter Berücksichtigung von Rauschen in der Neutralposition.
* **Hausaufgabe**: Schreibe ein Programm, das den Winkel des Joysticks anhand seiner Position berechnet und meldet.




**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/rRHyho4vwIQ?si=cV75rrwEWSYoKhAN" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
