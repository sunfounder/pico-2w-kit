.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Vertiefe dich in Raspberry Pi, Arduino und ESP32 zusammen mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Löse Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Promotionen und Gewinnspiele**: Nimm an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicke auf [|link_sf_facebook|] und trete heute bei!

Lektion 56: Verwendung eines Joysticks mit MicroPython
=============================================================================

Dieses Tutorial behandelt die Verwendung eines Joysticks mit dem Raspberry Pi Pico W:

* **Verkabelungsaufbau**: Verbinde den Ground, 3.3V, VRX mit GPIO-Pin 27 und VRY mit GPIO-Pin 26.
* **Codeimplementierung**: Importiere ``machine``, ``time``, ``math``; richte den ADC für die Joystickachsen ein; lese und drucke die Joystickwerte.
* **Kalibrierung**: Konvertiere die Messwerte in eine intuitive Skala von -100 bis +100.
* **Hausaufgabe**: Schreibe ein Programm zur Kalibrierung des Joysticks, so dass das Zentrum (0,0) liest und die Ränder ±100 anzeigen.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/0W8XSJhGux0?si=DO3JL-oMiMfbXF_e" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
