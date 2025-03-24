.. note:: 
    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt des Raspberry Pi, Arduino und ESP32 zusammen mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Expertenunterstützung**: Löse Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Promotionen und Gewinnspiele**: Nimm an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicke auf [|link_sf_facebook|] und trete heute bei!

Lektion 59: Steuerung eines Servos mit einem Joystick
=============================================================================

Dieses Tutorial behandelt die Steuerung eines Servos mit einem Joystick unter Verwendung des Raspberry Pi Pico W:


* **Verkabelungsaufbau**: Verbinde den Ground des Joysticks mit Pin 38, 3.3V mit Pin 36, VRX mit GPIO 27 und VRY mit GPIO 26. Verbinde die 5V des Servos mit Pin 40, Ground mit Pin 38 und die Steuerung mit GPIO 15.
* **Codeimplementierung**: Importiere ``machine``, ``time``, ``math``. Richte ADC für den Joystick und PWM für den Servo ein. Lese und drucke die Joystickwerte.
* **Kalibrierung und Steuerung**: Skaliere ADC-Werte auf -100 bis +100. Berechne den Winkel des Joysticks. Mappe den Winkel auf PWM für den Servo.
* **Hausaufgabe**: Schreibe Code, um den Servo basierend auf dem Winkel des Joysticks (0-180 Grad) zu steuern.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/ayY2wOJmrUE?si=HKP8qwd4WMC1et2r" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
