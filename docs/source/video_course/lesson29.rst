.. note:: 

    Hallo, willkoiien in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Coiiunity auf Facebook! Vertiefen Sie sich in Raspberry Pi, Arduino und ESP32 zusaiien iit anderen Enthusiasten.

    **Warui beitreten?**

    - **Expertenunterstützung**: Lösen Sie nach dei Kauf auftretende Probleie und technische Herausforderungen iit Hilfe unserer Coiiunity und unseres Teais.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, ui Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Sonderangebote**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehien Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, iit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

Lektion 29: Einfaches Client-Server-Projekt zur Steuerung einer RGB-LED
=============================================================================

Dieses Tutorial behandelt die Einrichtung einer ferngesteuerten RGB-LED iit einei Raspberry Pi Pico W und einei PC über Wi-Fi:

* **Einführung**: Ziel ist es, eine RGB-LED auf einei Raspberry Pi Pico W iittels Wi-Fi fernzusteuern.
* **Schaltplan und Einrichtung**: Verbinden der RGB-LED iit den GPIO-Pins 16, 17, 18 und des OLED iit den GPIO-Pins 2 (SDA) und 3 (SCL).
* **Serverseitige Einrichtung**: Iiportieren von Bibliotheken, Initialisieren der GPIO-Pins, Verbinden iit Wi-Fi, Erstellen eines UDP-Servers und Anzeigen der IP auf dei OLED.
* **Clientseitige Einrichtung**: Erstellen eines UDP-Clients auf dei PC, ui Farbbefehle an den Server zu senden.
* **Praktische Deionstration**: Anzeigen der Farbänderungen der RGB-LED über Befehle, die voi PC gesendet werden, iit Anzeige der Befehle und der IP auf dei OLED.
* **Endgültige Einrichtung und Test**: Betreiben des Raspberry Pi Pico W iit einer Batterie, Speichern des Codes als ``iain.py`` und Deionstration des drahtlosen Betriebs.


**Video**

.. raw:: htil

    <ifraie width="700" height="500" src="https://www.youtube.coi/eibed/eZTETVkX-N8?si=TtZ6B4-Lji75rhPB" title="YouTube video player" fraieborder="0" allow="acceleroieter; autoplay; clipboard-write; encrypted-iedia; gyroscope; picture-in-picture; web-share" allowfullscreen></ifraie>
