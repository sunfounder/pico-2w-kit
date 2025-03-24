.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche mit Gleichgesinnten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum solltest du beitreten?**

    - **Expertenunterstützung**: Erhalte Unterstützung bei technischen Herausforderungen und nach dem Kauf durch unsere Community und unser Team.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Profitiere von exklusiven Vergünstigungen auf unsere neuesten Produkte.
    - **Festliche Aktionen & Gewinnspiele**: Nimm an Verlosungen und Sonderaktionen zu Feiertagen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und trete noch heute bei!

FAQ
=========

Arduino
---------------------

#. Code-Upload in der Arduino IDE fehlgeschlagen?
    * Überprüfe, ob dein Pico von der Arduino IDE korrekt erkannt wird. Der Port sollte als COMXX (Raspberry Pi Pico) angezeigt werden. Anleitungen dazu findest du unter :ref:`setup_pico2w_arduino`.
    * Stelle sicher, dass das richtige Board (Raspberry Pi Pico) und der richtige Port (COMXX (Raspberry Pi Pico)) ausgewählt sind.
    * Falls dein Code korrekt ist und die richtigen Einstellungen vorgenommen wurden, der Upload aber trotzdem fehlschlägt, kannst du Folgendes versuchen: Klicke erneut auf das **Upload**-Symbol. Sobald unten „Upload...“ angezeigt wird, ziehe das USB-Kabel ab, halte die **BOOTSEL**-Taste gedrückt und stecke das Kabel wieder ein. Der Code sollte nun erfolgreich hochgeladen werden.


MicroPython
------------------

#. Wie öffne und starte ich den Code?
    Für eine detaillierte Anleitung siehe :ref:`open_run_code_py`.

#. Wie lade ich eine Bibliothek auf den Raspberry Pi Pico 2 W hoch?
    Eine ausführliche Anleitung findest du unter :ref:`add_libraries_py`.

#. Keine MicroPython (Raspberry Pi Pico 2 W) Interpreter-Option in Thonny IDE?
    * Überprüfe, ob dein Pico 2 W über ein USB-Kabel mit dem Computer verbunden ist.
    * Stelle sicher, dass du MicroPython für den Pico 2 W installiert hast (:ref:`install_micropython_on_pico`).
    * Die Interpreter-Option für den Raspberry Pi Pico 2 W ist erst ab Version 3.3.3 von Thonny verfügbar. Falls du eine ältere Version nutzt, führe ein Update durch (:ref:`thonny_ide`).
    * Falls das Li-Po-Ladegerät-Modul an das Breadboard angeschlossen ist, entferne es zunächst und stecke dann den Pico 2 W erneut an den Computer.

#. Pico 2 W Code kann nicht geöffnet oder auf den Pico 2 W gespeichert werden (Thonny IDE)?
    * Überprüfe, ob dein Pico 2 W über ein USB-Kabel mit dem Computer verbunden ist.
    * Stelle sicher, dass der Interpreter als **MicroPython (Raspberry Pi Pico)** eingestellt ist.

#. Kann der Raspberry Pi Pico 2 W gleichzeitig mit Thonny und Arduino verwendet werden?
    NEIN, für den Wechsel zwischen beiden Plattformen sind bestimmte Schritte erforderlich.

    * Falls du den Pico zuvor mit der Arduino IDE verwendet hast und ihn jetzt mit Thonny nutzen möchtest, musst du :ref:`install_micropython_on_pico`.
    * Falls du den Pico zuvor mit Thonny genutzt hast und nun mit der Arduino IDE arbeiten möchtest, musst du :ref:`setup_pico2w_arduino` durchführen.

.. #. Pico 2 W wird unter Windows 7 nicht erkannt?
    * Lade den USB-CDC-Treiber von http://aem-origin.microchip.com/en-us/mindi-sw-library?swsearch=Atmel%2520USB%2520CDC%2520Virtual%2520COM%2520Driver herunter.
    * Entpacke die Datei ``amtel_devices_cdc.inf`` in einen Ordner mit dem Namen ``pico-serial``.
    * Benenne die Datei ``amtel_devices_cdc.inf`` in ``pico-serial.inf`` um.
    * Öffne die Datei ``pico-serial.inf`` mit einem einfachen Editor (z. B. Notepad).
    * Ersetze die folgenden Zeilen:

    .. code-block:: 

        [DeviceList]
        %PI_CDC_PICO%=DriverInstall, USB\VID_2E8A&PID_0005&MI_00

        [DeviceList.NTAMD64]
        %PI_CDC_PICO%=DriverInstall, USB\VID_2E8A&PID_0005&MI_00

        [DeviceList.NTIA64]
        %PI_CDC_PICO%=DriverInstall, USB\VID_2E8A&PID_0005&MI_00

        [DeviceList.NT]
        %PI_CDC_PICO%=DriverInstall, USB\VID_2E8A&PID_0005&MI_00

        [Strings]
        Manufacturer = "ATMEL, Inc."
        PI_CDC_PICO = "Pi Pico Serial Port"
        Serial.SvcDesc = "Pi Pico Serial Driver"

    #. Speichere die Datei und stelle sicher, dass sie weiterhin ``pico-serial.inf`` heißt.
    #. Öffne die Geräteverwaltung deines PCs, suche nach dem Pico unter "Anschlüsse (COM & LPT)" – er sollte als „CDC Device“ erscheinen (ggf. mit einem gelben Warnsymbol).
    #. Klicke mit der rechten Maustaste auf das CDC-Gerät, wähle "Treiber aktualisieren" und gib den Speicherort der geänderten Datei an.

.. Piper Make
.. ------------------

.. #. Wie richte ich den Pico 2 W in Piper Make ein?
    Für eine detaillierte Anleitung siehe :ref:`per_setup_pico`.

.. #. Wie kann ich Code herunterladen oder importieren?
    Eine ausführliche Anleitung findest du unter :ref:`per_save_import`.

.. #. Wie verbinde ich mich mit dem Pico 2 W?
    Eine ausführliche Anleitung findest du unter :ref:`connect_pico_per`.
