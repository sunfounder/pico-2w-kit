.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt des Raspberry Pi, Arduino und ESP32 zusammen mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Expertenunterstützung**: Löse Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Promotionen und Gewinnspiele**: Nimm an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicke auf [|link_sf_facebook|] und trete heute bei!

Lektion 60: Steuerung der NeoPixel-Farben mit einem Joystick in MicroPython
=============================================================================

Dieses Tutorial behandelt die Steuerung eines LED-Streifens mit einem Joystick unter Verwendung des Raspberry Pi Pico W:

* **Verkabelungsaufbau**:

    - Verbinde den Ground des Joysticks mit Pin 38, 3.3V mit Pin 36, VRX mit GPIO-Pin 27, VRY mit GPIO-Pin 26.
    - Verbinde den Ground des NeoPixels mit Pin 38, 5V mit Pin 40, Daten mit GPIO-Pin 0.
    
* **Codeimplementierung**: 

    - Importiere Bibliotheken (``machine``, ``time``, ``math``, ``neopixel``).
    - Richte ADC für den Joystick und NeoPixel ein. Lese Joystick-Werte, berechne Winkel.
    - Konvertiere Winkel in RGB für NeoPixel.

* **Hausaufgabe**: Schreibe ein Programm, um die Farbe und Helligkeit des NeoPixels basierend auf dem Winkel und der Entfernung des Joysticks vom Zentrum zu steuern.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/8UCJHY7uTH4?si=BKJ8lYNz1kF4w9wm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
