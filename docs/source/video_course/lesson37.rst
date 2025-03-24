.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Vertiefen Sie sich in Raspberry Pi, Arduino und ESP32 zusammen mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Sonderangebote**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

Lektion 37: Steuerung eines Servomotors mit einem Potentiometer in MicroPython
==================================================================================
Dieses Tutorial behandelt die Steuerung eines Servomotors mit einem Potentiometer mit dem Raspberry Pi Pico W:

* **Servomotorsteuerung**: Schließen Sie den SG90-Servomotor an den Raspberry Pi Pico W an, mit Erdung, Stromversorgung (5V) und Steuerung an GPIO-Pin 15.
* **Verkabelungseinrichtung**: Verbinden Sie das Potentiometer mit 3,3V, Erdung und dem Signal an GPIO-Pin 26.
* **Grundlagen zu PWM**: Verwenden Sie PWM bei 50 Hz, um die Position des Servos zu steuern.
* **Code-Erklärung**: Richten Sie PWM auf GPIO 15 ein und konvertieren Sie Potentiometereingaben in Servowinkel.
* **Praktische Demonstration**: Führen Sie den Code aus, um den Servo mit dem Potentiometer zu steuern, und vermeiden Sie manuelle Drehungen am Servohorn.
* **Anwendungsideen**: Verwenden Sie externe Stromversorgung, um größere Servos für fortgeschrittene Projekte zu steuern.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/iiJasGsLTrQ?si=f-avwQIJNypRuh4t" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
