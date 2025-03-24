.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Vertiefe dich in Raspberry Pi, Arduino und ESP32 zusammen mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Löse Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Promotionen und Gewinnspiele**: Nimm an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicke auf [|link_sf_facebook|] und trete heute bei!

Lektion 69:  Sauberes Beenden von MicroPython-Threads beim Programmende
===================================================================================

Dieses Tutorial behandelt die Steuerung eines Servos und LEDs mit dem Raspberry Pi Pico W unter Nutzung beider Kerne:

* **Verkabelungsaufbau**: Verbinde die rote LED mit GPIO 15, die grüne LED mit GPIO 14 und den Servo mit GPIO 17, mit Stromversorgung an Pin 40 und Masse an Pin 38.
* **Codeimplementierung**: Importiere ``machine``, ``time``, ``_thread`` und ``Servo``. Richte die Pins für LEDs und Servo ein. Definiere ``other_core``, um LEDs basierend auf der Servobewegung blinken zu lassen. Erstelle eine Schleife zur Steuerung des Servos und der LEDs.
* **Hausaufgabe**: Modifiziere den Code, um die rote LED bei Uhrzeigersinn und die grüne LED bei Gegenuhrzeigersinn des Servos blinken zu lassen.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/mcXxqx0lZYo?si=tIek_zJ4EMuZ3bC4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
