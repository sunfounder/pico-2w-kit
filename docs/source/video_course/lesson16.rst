.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Vertiefen Sie sich in Raspberry Pi, Arduino und ESP32 zusammen mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Sonderangebote**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

Lektion 16: Farbsequenzen in RGB-LEDs mit MicroPython
=============================================================================

Dieses Tutorial behandelt die Verwendung von For-Schleifen in MicroPython am Raspberry Pi Pico W zur Steuerung einer RGB-LED:

* **Einführung**: Überblick über die Nutzung von For-Schleifen und PWM zur Steuerung der Helligkeit und Farbe von RGB-LEDs.
* **Schaltungsaufbau**: Anschluss der RGB-LED an die GPIO-Pins 13, 14 und 15 unter Verwendung von 330 Ohm Widerständen.
* **PWM-Einrichtung**: Einrichtung von PWM auf jedem LED-Kanal mit einer Frequenz von 1000 Hz für sanfte Übergänge.
* **Eingabe der Farbsequenz**: Aufforderung an den Benutzer, eine Farbsequenz einzugeben, die Eingaben werden in einem Array gespeichert.
* **Farbsteuerungslogik**: Verwendung von If-Anweisungen zur Zuweisung von PWM-Werten für Farben wie Rot, Grün, Blau, Cyan, Magenta, Gelb, Orange und Aus.
* **Dauerschleife**: Durchlaufen der Farbsequenz mit einer While-True-Schleife und Sleep-Anweisungen.



**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/VivNlgYg3wY?si=ECUsRAWanIAShyxk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

