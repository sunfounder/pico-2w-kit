.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein – gemeinsam mit anderen Technikbegeisterten.

    **Warum beitreten?**

    - **Experten-Support**: Erhalte Hilfe bei technischen Herausforderungen und nach dem Kauf auftretenden Problemen – direkt von unserer Community und unserem Team.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und ersten Einblicken.
    - **Spezielle Rabatte**: Profitiere von exklusiven Vergünstigungen auf unsere neuesten Produkte.
    - **Feiertagsaktionen und Gewinnspiele**: Nimm an besonderen Aktionen und Verlosungen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und trete noch heute bei!

.. _setup_pico_arduino:

1.3 Einrichtung des Raspberry Pi Pico W (Wichtig)
====================================================

1. Installation der UF2-Firmware
------------------------------------

Wenn du den Raspberry Pi Pico W zum ersten Mal anschließt oder die **BOOTSEL**-Taste beim Einstecken gedrückt hältst, erscheint das Gerät als Laufwerk, ohne dass ihm ein COM-Port zugewiesen wird. Dadurch ist es nicht möglich, Code hochzuladen.

Um dieses Problem zu lösen, musst du die UF2-Firmware installieren. Diese Firmware unterstützt MicroPython und ist auch mit der Arduino IDE kompatibel.

1. Lade die UF2-Firmware über den folgenden Link herunter:

    * :download:`Raspberry Pi Pico W UF2 Firmware <https://micropython.org/download/rp2-pico-w/rp2-pico-w-latest.uf2>`

2. Verbinde deinen Raspberry Pi Pico W mit einem Micro-USB-Kabel mit deinem Computer. Der Pico W wird als Massenspeichergerät mit dem Namen **RPI-RP2** angezeigt.

    .. image:: img/install_pico_plugin.png

3. Ziehe die heruntergeladene UF2-Firmware per Drag & Drop in das **RPI-RP2**-Laufwerk.

    .. image:: img/install_pico_uf2.png

4. Nach dem Kopiervorgang verschwindet das **RPI-RP2**-Laufwerk, und du kannst mit den nächsten Schritten fortfahren.


2. Installation des Board-Pakets
-----------------------------------

Um den Raspberry Pi Pico W zu programmieren, musst du das entsprechende Board-Paket in der Arduino IDE installieren. Folge dieser Schritt-für-Schritt-Anleitung:

1. Öffne das **Boardverwalter**-Fenster, suche nach **pico** und klicke auf **Install**, um die Installation zu starten. Dadurch wird das Paket **Arduino Mbed OS RP2040 Boards** installiert, das die Unterstützung für den Raspberry Pi Pico W beinhaltet.

    .. image:: img/install_pico.png

2. Während der Installation erscheinen einige Pop-up-Fenster zur Installation spezifischer Gerätetreiber. Wähle **"Install"**.

    .. image:: img/install_pico_sa.png

3. Nach Abschluss der Installation erscheint eine Benachrichtigung zur Bestätigung.

3. Auswahl des Boards und des Ports
--------------------------------------

1. Wähle das entsprechende Board über **Werkzeuge** -> **Board** -> **Arduino Mbed OS RP2040 Boards** -> **Raspberry Pi Pico**.

    .. image:: img/install_pico_tool_board.png

2. Falls dein Raspberry Pi Pico W mit dem Computer verbunden ist, stelle den richtigen Port über **Werkzeuge** -> **Port** ein.

    .. image:: img/install_pico_tool_port.png

3. Arduino 2.0 bietet eine neue Schnellwahl-Funktion. Da der Raspberry Pi Pico W in der Regel nicht automatisch erkannt wird, klicke auf **Anderes Board und anderen Port auswählen**.

    .. image:: img/install_pico_select.png

4. Gib **Raspberry Pi Pico** in das Suchfeld ein, wähle ihn aus, sobald er erscheint, wähle den entsprechenden Port und klicke auf **OK**.

    .. image:: img/install_pico_board.png

5. Später kannst du diese Auswahl bequem über das Schnellzugriffsfenster erneut aufrufen.

    .. image:: img/install_pico_quick.png

6. Mit diesen Methoden kannst du das richtige Board und den richtigen Port auswählen. Nun bist du bereit, Code auf den Raspberry Pi Pico W hochzuladen.

4. Hochladen von Code
---------------------

Nun sehen wir uns an, wie du Code auf deinen Raspberry Pi Pico W hochladen kannst.

1. Öffne eine beliebige ``.ino``-Datei oder verwende den standardmäßig angezeigten leeren Sketch. Klicke dann auf die **Hochladen**-Schaltfläche.

    .. image:: img/install_pico_upload.png

2. Warte, bis die Upload-Meldung erscheint, wie unten gezeigt.

    .. image:: img/install_pico_upload_dot.png

3. Halte die **BOOTSEL**-Taste gedrückt, trenne den Raspberry Pi Pico W kurz vom Computer und stecke ihn dann sofort wieder ein.

    .. image:: img/led_onboard.png 

    .. note::
        
        * Dieser Schritt ist besonders wichtig, insbesondere für Erstbenutzer der Arduino IDE. Wird dieser Schritt übersprungen, schlägt das Hochladen fehl.

        * Nach einem erfolgreichen ersten Upload wird dein Pico W vom Computer erkannt. Für zukünftige Uploads kannst du ihn einfach anschließen.

4. Eine Bestätigungsmeldung zeigt an, dass der Upload erfolgreich war.

    .. image:: img/install_pico_upload_done.png
