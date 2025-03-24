.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Vertiefen Sie sich in Raspberry Pi, Arduino und ESP32 zusammen mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Sonderangebote**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

Lektion 46: Bau eines 2-Achsen-Neigungsmessers mit Anzeige unter Verwendung des MPU6050
============================================================================================
Dieses Tutorial behandelt die Verwendung des MPU6050-Sensors mit dem Raspberry Pi Pico W zum Erstellen eines Zwei-Achsen-Neigungsmessers:

* **Einrichtung**: Verbinden Sie MPU6050 und OLED 1306 mit dem Raspberry Pi Pico W.
* **Konzept**: Messen der Neigung über Nick- und Rollwinkel, Anzeige der Wasserwaage auf dem OLED.
* **Gleichungen**: 
   - Nickwinkel: \(\arctan\left(\frac{Y}{Z}\right)\)
   - Rollwinkel: \(\arctan\left(\frac{X}{Z}\right)\)
   - Umrechnung von Radiant in Grad.
* **Code**: Einrichten von Bibliotheken, Messen der X-, Y-, Z-Beschleunigung, Berechnen der Winkel und Anzeigen auf dem OLED.
* **Demonstration**: Test der Neigung, Anpassung der Blasenbewegung für Reaktionsfähigkeit.
* **Fortgeschritten**: Stabilisierung der Neigungsmessungen, um Fehler durch Beschleunigung oder Vibrationen zu vermeiden.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/wYv39RMwXvU?si=6gJoFFIa1HSdGIFt" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
