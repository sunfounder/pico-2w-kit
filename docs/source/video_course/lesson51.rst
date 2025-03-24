.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt des Raspberry Pi, Arduino und ESP32 zusammen mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Expertenunterstützung**: Löse Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Promotionen und Gewinnspiele**: Nimm an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicke auf [|link_sf_facebook|] und trete heute bei!

Lektion 51: Das ultimative Neigungsmessgerät für Pitch und Roll mit dem MPU6050
=====================================================================================
Dieses Tutorial behandelt die Erstellung eines präzisen Neigungsmessers mit dem MPU6050-Sensor und dem Raspberry Pi Pico W:

* **Aufbau**: Verbinde den MPU6050 und das OLED 1306 mit dem Raspberry Pi Pico W.
* **Herausforderungen**: Daten von Beschleunigungsmessern sind rauschanfällig, und Daten von Gyroskopen driften über die Zeit.
* **Lösung**: Verwende einen Komplementärfilter, um Daten von Beschleunigungsmesser und Gyroskop zu kombinieren, mit Fehlerkorrektur für gleichbleibende Fehler.
* **Implementierung**: Initialisiere Sensoren und OLED. Sammle und filtere Daten, zeige die Neigung als Blasenwaage und als Gradanzeige auf dem OLED an.
* **Demonstration**: Teste auf stabile Pitch- und Roll-Anzeigen, betrieben mit einem tragbaren Akku.
* **Weitere Verbesserungen**: Betrachte die Möglichkeit der drahtlosen Überwachung oder die Erstellung eines 3D-gedruckten Gehäuses für die Portabilität.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/afQyZl2hkd0?si=4Dg4Uvr5yVC4f60Y" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
