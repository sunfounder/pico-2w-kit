.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Vertiefen Sie sich in Raspberry Pi, Arduino und ESP32 zusammen mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Sonderangebote**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

Lektion 29: Einfaches Client-Server-Projekt zur Steuerung einer RGB-LED
=============================================================================

Dieses Tutorial behandelt die Einrichtung einer ferngesteuerten RGB-LED mit einem Raspberry Pi Pico W und einem PC über Wi-Fi:

* **Einführung**: Ziel ist es, eine RGB-LED auf einem Raspberry Pi Pico W mittels Wi-Fi fernzusteuern.
* **Schaltplan und Einrichtung**: Verbinden der RGB-LED mit den GPIO-Pins 16, 17, 18 und des OLED mit den GPIO-Pins 2 (SDA) und 3 (SCL).
* **Serverseitige Einrichtung**: Importieren von Bibliotheken, Initialisieren der GPIO-Pins, Verbinden mit Wi-Fi, Erstellen eines UDP-Servers und Anzeigen der IP auf dem OLED.
* **Clientseitige Einrichtung**: Erstellen eines UDP-Clients auf dem PC, um Farbbefehle an den Server zu senden.
* **Praktische Demonstration**: Anzeigen der Farbänderungen der RGB-LED über Befehle, die vom PC gesendet werden, mit Anzeige der Befehle und der IP auf dem OLED.
* **Endgültige Einrichtung und Test**: Betreiben des Raspberry Pi Pico W mit einer Batterie, Speichern des Codes als ``main.py`` und Demonstration des drahtlosen Betriebs.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/eZTETVkX-N8?si=TtZ6B4-Ljm75rhPB" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
