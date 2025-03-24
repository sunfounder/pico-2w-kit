.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Vertiefen Sie sich in Raspberry Pi, Arduino und ESP32 zusammen mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Sonderangebote**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

Lektion 45: Berechnung der Höhe eines im freien Fall fallenden Objekts
=============================================================================
Dieses Tutorial behandelt die Verwendung des MPU6050-Sensors mit dem Raspberry Pi Pico W zur Messung von vertikalen Distanzen:

* **Einrichtung**: Schließen Sie den MPU6050 und das OLED 1306 an den Raspberry Pi Pico W an und stellen Sie sichere Verbindungen her, um Störungen zu minimieren.
* **Konzept**: Messen der vertikalen Distanz durch Berechnen der Fallzeit (T_drop) im freien Fall und Verwendung dieser zur Bestimmung der gefallenen Höhe.
* **Gleichung**: Berechnen der Höhe (H) mit \( H = 16 \times (T_{drop})^2 \), Umrechnung der Zeit von Millisekunden in Sekunden.
* **Code-Implementierung**: Einrichten von Bibliotheken, Messen der Z-Achsen-Beschleunigung zur Erkennung von 0G, Starten eines Timers während des freien Falls und Anzeigen von Höhe und Fallzeit auf dem OLED.
* **Praktische Demonstration**: Testen Sie den Sensor aus bekannten Höhen und passen Sie die Genauigkeit bei Bedarf an.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/xpHDAcdrTF0?si=NdmV4J5G6DhJ4f6M" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
