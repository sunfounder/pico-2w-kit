.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Vertiefen Sie sich in Raspberry Pi, Arduino und ESP32 zusammen mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Sonderangebote**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

Lektion 47: Verbesserung von Sensordaten mit einem Tiefpassfilter
=============================================================================
Dieses Tutorial behandelt die Verwendung des MPU6050-Sensors mit dem Raspberry Pi Pico W zur Erstellung eines stabilen Zwei-Achsen-Neigungsmessers durch Implementierung eines Tiefpassfilters:

* **Einrichtung**: Verbinden Sie den MPU6050 mit dem Raspberry Pi Pico W.
* **Konzept**: Messen der Neigung mithilfe von Beschleunigungssensordaten, unter Berücksichtigung von Fehlern durch Beschleunigung.
* **Tiefpassfilter**: Implementierung zur Glättung der Daten mit der Gleichung: ``\(\text{neuer Wert} = \text{Vertrauen} \times \text{Messung} + (1 - \text{Vertrauen}) \times \text{alter Wert}\)``.
* **Code**: Messen von X, Y, Z, Filtern von Nick- und Rollwinkeln und Anzeigen der Ergebnisse.
* **Hausaufgabe**: Testen Sie den Tiefpassfilter und experimentieren Sie mit Vertrauenswerten.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/3YqGIg4crEk?si=rwiDFcJ98nlj_Sg3" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
