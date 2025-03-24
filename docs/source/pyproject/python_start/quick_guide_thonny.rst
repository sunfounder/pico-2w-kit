.. note::
   Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein zusammen mit anderen Begeisterten.

   **Warum beitreten?**

   - **Expertenunterstützung**: Löse Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
   - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um deine Fähigkeiten zu verbessern.
   - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
   - **Sonderangebote**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
   - **Festliche Aktionen und Verlosungen**: Nimm an Verlosungen und Feiertagsaktionen teil.

   👉 Bereit, mit uns zu erkunden und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt heute bei!

1.5 Schnellführer für Thonny
==================================

.. _open_run_code_py:

Code direkt öffnen und ausführen
---------------------------------------------

Der Codeabschnitt in den Projekten zeigt genau an, welcher Code verwendet wird, also doppelklicke auf die ``.py``-Datei mit der Seriennummer im Pfad ``pico-2w-kit-main/micropython/``, um sie zu öffnen.

Zuvor musst du jedoch das Paket herunterladen und die Bibliothek hochladen, wie in :ref:`add_libraries_py` beschrieben.

#. Code öffnen.

    Zum Beispiel ``2.1_hello_led.py``.

    Wenn du darauf doppelklickst, öffnet sich ein neues Fenster rechts. Du kannst mehr als einen Code gleichzeitig öffnen.

    |open_code|

#. Richtigen Interpreter auswählen

    Verbinde den Pico 2 W mit deinem Computer über ein Micro-USB-Kabel und wähle den "MicroPython (Raspberry Pi Pico)"-Interpreter.

    |sec_inter|

#. Code ausführen

    Um das Skript auszuführen, klicke auf den **Run current script**-Knopf oder drücke F5.

    |run_it|

    Wenn der Code Informationen enthält, die gedruckt werden müssen, erscheinen diese in der Shell; ansonsten erscheint nur die folgende Information.

    Klicke auf **Ansicht** -> **Bearbeiten**, um das Shell-Fenster zu öffnen, falls es nicht auf deinem Thonny erscheint.

        .. code-block::

            MicroPython vx.xx on xxxx-xx-xx; Raspberry Pi Pico 2 W  With RP2350

            Type "help()" for more information.
            >>> %Run -c $EDITOR_CONTENT

    * Die erste Zeile zeigt die Version von MicroPython, das Datum und deine Geräteinformationen.
    * Die zweite Zeile fordert dich auf, "help()" einzugeben, um Hilfe zu erhalten.
    * Die dritte Zeile ist ein Befehl von Thonny, der den MicroPython-Interpreter auf deinem Pico 2 W anweist, den Inhalt des Skriptbereichs - "EDITOR_CONTENT" - auszuführen.
    * Wenn nach der dritten Zeile eine Nachricht erscheint, ist es normalerweise eine Nachricht, die du MicroPython zum Drucken gegeben hast, oder eine Fehlermeldung für den Code.


#. Ausführung stoppen

    |stop_it|

    Um den laufenden Code zu stoppen, klicke auf den **Stop/Restart backend**-Knopf. Der **%RUN -c $EDITOR_CONTENT**-Befehl verschwindet nach dem Stoppen.

#. Speichern oder Speichern unter

    Du kannst Änderungen, die du an dem geöffneten Beispiel vorgenommen hast, durch Drücken von **Ctrl+S** oder durch Klicken auf den **Speichern**-Knopf auf Thonny speichern.

    Der Code kann als separate Datei innerhalb des Raspberry Pi Pico 2 W gespeichert werden, indem du auf **Datei** -> **Speichern unter** klickst.

    |save_as|

    Wähle **Raspberry Pi Pico** aus.

    |sec_pico|

    Dann klicke auf **OK** nachdem du den Dateinamen und die Erweiterung **.py** eingegeben hast. Auf dem Laufwerk des Raspberry Pi Pico 2 W siehst du deine gespeicherte Datei.

    |sec_name|

    .. note::
        Unabhängig davon, welchen Namen du deinem Code gibst, ist es am besten, zu beschreiben, welche Art von Code es ist, und ihm keinen bedeutungslosen Namen wie ``abc.py`` zu geben.
        Wenn du den Code als ``main.py`` speicherst, wird er automatisch ausgeführt, wenn das Gerät eingeschaltet wird.


Datei erstellen und ausführen
-------------------------------


Der Code wird direkt im Codeabschnitt gezeigt. Du kannst ihn in Thonny kopieren und wie folgt ausführen.

#. Neue Datei erstellen

    Öffne Thonny IDE, klicke auf die **Neu**-Schaltfläche, um eine neue leere Datei zu erstellen.

    |new_file|

#. Code kopieren

    Kopiere den Code aus dem Projekt in die Thonny IDE.

    |copy_file|

#. Richtigen Interpreter auswählen

    Stecke den Pico 2 W mit einem Micro-USB-Kabel in deinen Computer und wähle den "MicroPython (Raspberry Pi Pico)"-Interpreter in der rechten unteren Ecke.

    |sec_inter|

#. Code ausführen und speichern

    Du musst auf **Run Current Script** klicken oder einfach F5 drücken, um ihn auszuführen. Wenn dein Code noch nicht gespeichert wurde, erscheint ein Fenster, das fragt, ob du auf **Diesem Computer** oder **Raspberry Pi Pico** speichern möchtest.

    |where_save|

    .. note::
        Thonny speichert dein Programm auf dem Raspberry Pi Pico 2 W, wenn du es ihm sagst, also wenn du den Pico 2 W aussteckst und in einen anderen Computer steckst, bleibt dein Programm intakt.

    Klicke auf OK, nachdem du den Speicherort ausgewählt, den Dateinamen eingegeben und die Erweiterung **.py** hinzugefügt hast.

    |sec_name|

    .. note::
        Unabhängig davon, welchen Namen du deinem Code gibst, ist es am besten, zu beschreiben, welche Art von Code es ist, und ihm keinen bedeutungslosen Namen wie ``abc.py`` zu geben.
        Wenn du den Code als ``main.py`` speicherst, wird er automatisch ausgeführt, wenn das Gerät eingeschaltet wird.

    Sobald dein Programm gespeichert ist, wird es automatisch ausgeführt und du siehst die folgenden Informationen im Shell-Bereich.

    Klicke auf **Ansicht** -> **Bearbeiten**, um das Shell-Fenster zu öffnen, falls es auf deinem Thonny nicht erscheint.

    .. code-block::

        MicroPython vx.xx.x am xxxx-xx-xx; Raspberry Pi Pico 2 W mit RP2350

        Gib "help()" ein für mehr Informationen.
        >>> %Run -c $EDITOR_CONTENT

    * Die erste Zeile zeigt die Version von MicroPython, das Datum und deine Geräteinformationen.
    * Die zweite Zeile fordert dich auf, "help()" einzugeben, um Hilfe zu erhalten.
    * Die dritte Zeile ist ein Befehl von Thonny, der den MicroPython-Interpreter auf deinem Pico 2 W anweist, den Inhalt des Skriptbereichs - "EDITOR_CONTENT" - auszuführen.
    * Wenn nach der dritten Zeile eine Nachricht erscheint, ist es normalerweise eine Nachricht, die du MicroPython zum Drucken gegeben hast, oder eine Fehlermeldung für den Code.

#. Ausführung stoppen

    |stop_it|

    Um den laufenden Code zu stoppen, klicke auf den **Stop/Restart backend**-Knopf. Der **%RUN -c $EDITOR_CONTENT**-Befehl verschwindet nach dem Stoppen.

#. Datei öffnen

    Hier sind zwei Möglichkeiten, eine gespeicherte Code-Datei zu öffnen.

    * Die erste Methode besteht darin, das Öffnen-Symbol in der Thonny-Toolbar zu klicken, genau wie beim Speichern eines Programms, wirst du gefragt, ob du es von **diesem Computer** oder **Raspberry Pi Pico** öffnen möchtest, zum Beispiel, klicke auf **Raspberry Pi Pico** und du siehst eine Liste aller Programme, die du auf dem Pico 2 W gespeichert hast.
    * Die zweite ist, die Dateivorschau direkt zu öffnen, indem du auf **Ansicht** -> **Datei** klickst und dann auf die entsprechende ``.py``-Datei doppelklickst, um sie zu öffnen.
