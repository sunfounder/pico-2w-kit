.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Vertiefen Sie sich in Raspberry Pi, Arduino und ESP32 zusammen mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Sonderangebote**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

Lektion 32: Projekt einer mobilen Wetterstation
=============================================================================

Dieses Tutorial behandelt die Erstellung einer tragbaren Wetterstation mit dem Raspberry Pi Pico W:

* **Verbindung zu WiFi**: Importieren von Bibliotheken, Erstellen eines WLAN-Objekts und Verbindung zu WiFi.
* **Wetterdaten abrufen**: Verwendung der OpenWeatherMap-API, um Echtzeit-Wetterdaten abzurufen, benötigt einen API-Schlüssel.
* **JSON-Daten parsen**: Extrahieren von Temperatur, Luftfeuchtigkeit, Druck, Sonnenaufgang und Sonnenuntergangszeiten aus der JSON-Antwort.
* **Daten auf OLED anzeigen**: Einrichten und Verbinden eines OLED-Displays, Verwendung der ``ssd1306``-Bibliothek und Aktualisieren der Wetterdaten auf dem Bildschirm in einer Schleife.
* **Stromversorgung des Geräts**: Betreiben des Raspberry Pi Pico W mit einer Batterie für Mobilität.
* **Code-Erklärung**: Initialisieren des OLED, Verbinden mit WiFi, Abrufen und Anzeigen von Wetterdaten und Einrichten einer Schleife für periodische Updates.
* **Hausaufgabe**: Hinzufügen einer RGB-LED, um Wetterbedingungen basierend auf Temperatur, Luftfeuchtigkeit oder Windgeschwindigkeit anzuzeigen.



**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/zovC4CvR1Hw?si=d_lhJvfzTC3pR5cS" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
