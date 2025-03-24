.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein – gemeinsam mit anderen Technikbegeisterten.

    **Warum beitreten?**

    - **Experten-Support**: Erhalte Hilfe bei technischen Herausforderungen und nach dem Kauf auftretenden Problemen – direkt von unserer Community und unserem Team.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und ersten Einblicken.
    - **Spezielle Rabatte**: Profitiere von exklusiven Vergünstigungen auf unsere neuesten Produkte.
    - **Feiertagsaktionen und Gewinnspiele**: Nimm an besonderen Aktionen und Verlosungen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und trete noch heute bei!

.. _setup_pico2w_arduino:

1.3 Einrichtung des Raspberry Pi Pico 2 W (Wichtig)
======================================================

1. Installation des Board-Pakets
---------------------------------

Um den Raspberry Pi Pico 2 W zu programmieren, musst du das entsprechende Board-Paket in der Arduino IDE installieren. Befolge dazu die folgenden Schritte:

#. Öffne die Arduino IDE und navigiere zu **Datei** -> **Voreinstellungen**.

   .. image:: img/arduino_pico_file.png

#. Gib im erscheinenden Dialogfeld die folgende URL in das Feld "Zusätzliche Boardverwalter-URLs" ein: ``https://github.com/earlephilhower/arduino-pico/releases/download/global/package_rp2040_index.json``.

   .. image:: img/arduino_pico_link.png

#. Öffne den **Boardverwalter** über das Menü und suche nach **pico**. Klicke auf die Schaltfläche **INSTALL**, um die Installation zu starten. Dadurch wird das Paket **Raspberry Pi Pico /RP2040/PR2350** installiert, einschließlich Unterstützung für den Raspberry Pi Pico 2 W.

   .. image:: img/arduino_pico_install.png

#. Während der Installation können mehrere Pop-up-Fenster erscheinen, die dich auffordern, bestimmte Gerätetreiber zu installieren. Wähle **"Install"**.

   .. image:: img/install_pico_sa.png

#. Nach Abschluss der Installation erscheint eine Benachrichtigung zur Bestätigung der erfolgreichen Einrichtung.

2. Auswahl des Boards und des Ports
--------------------------------------

#. Halte die **BOOTSEL**-Taste gedrückt, trenne dann den Raspberry Pi Pico 2 W vom Computer und stecke ihn sofort wieder ein.

   .. image:: img/led_onboard.png
        :width: 500
        :align: center

   .. warning::
        
      * Dieser Schritt ist besonders wichtig, insbesondere für Erstbenutzer der Arduino IDE. Wird dieser Schritt übersprungen, schlägt das Hochladen fehl.
      * Sobald du erfolgreich Code hochgeladen hast, wird dein Pico vom Computer erkannt. Für zukünftige Uploads kannst du ihn einfach anschließen, ohne die Taste gedrückt zu halten.

#. Um das richtige Board auszuwählen, navigiere zu **Werkzeuge** -> **Board** -> **Raspberry Pi Pico /RP2040/PR2350** -> **Raspberry Pi Pico 2 W**.

   .. image:: img/arduino_pico_board2.jpg
      :width: 600
      :align: center

#. Wähle als Nächstes den richtigen Port aus, indem du zu **Werkzeuge** -> **Port** -> **UF2 Board** gehst.

   .. note::
     
     * Bei der ersten Verbindung oder wenn die **BOOTSEL**-Taste gedrückt gehalten wird, wähle **UF2 Board**.
     * Nach einem erfolgreichen Upload wird dein Pico 2 W vom Computer erkannt. Für zukünftige Verbindungen wähle den entsprechenden **COMxx (Raspberry Pi Pico 2)**-Port.

   .. image:: img/arduino_pico_port.jpg


3. Code hochladen
--------------------

Nun geht es darum, Code auf deinen Raspberry Pi Pico 2 W hochzuladen.

#. Öffne eine beliebige ``.ino``-Datei oder verwende das standardmäßig geöffnete leere Sketch. Klicke dann auf die Schaltfläche **Hochladen**.

   .. image:: img/install_pico_upload1.png

#. Nach Abschluss des Uploads erscheint eine Bestätigungsmeldung.

   .. image:: img/install_pico_upload_done2.png

#. Dein Computer sollte den Pico 2 W nun erfolgreich erkennen.

   .. image:: img/arduino_pico_port_com2.png

