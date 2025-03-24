.. note::
   Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein zusammen mit anderen Begeisterten.

   **Warum beitreten?**

   - **Expertenunterstützung**: Löse Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
   - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um deine Fähigkeiten zu verbessern.
   - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
   - **Sonderangebote**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
   - **Festliche Aktionen und Verlosungen**: Nimm an Verlosungen und Feiertagsaktionen teil.

   👉 Bereit, mit uns zu erkunden und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt heute bei!

.. _thonny_ide:

1.2 Thonny IDE installieren und vorstellen
=============================================

Um den Pico mit MicroPython zu programmieren, benötigst du eine integrierte Entwicklungsumgebung (IDE), hier empfehlen wir Thonny. Python 3.7 ist bereits in Thonny IDE vorinstalliert, du musst es nur installieren.

Download aus dem Web
------------------------

Bevor du anfangen kannst, den Pico mit MicroPython zu programmieren, benötigst du eine integrierte Entwicklungsumgebung (IDE), hier empfehlen wir Thonny. Thonny kommt mit eingebautem Python 3.7, ein einfacher Installer reicht aus und du bist bereit, das Programmieren zu lernen.


.. note::

    Da der Raspberry Pi Pico 2 W Interpreter nur mit Thonny Version 3.3.3 oder später funktioniert, kannst du dieses Kapitel überspringen, wenn du es bereits hast; sonst bitte aktualisiere oder installiere es.


#. Du kannst es herunterladen, indem du die |link_thonny| Website besuchst. Sobald du die Seite öffnest, siehst du oben rechts ein hellgraues Feld, klicke auf den Link, der zu deinem Betriebssystem passt.

   .. image:: img/download_thonny.png
    :width: 400


#. Die Installationsprogramme wurden mit einem neuen Zertifikat signiert, das noch keinen Ruf aufgebaut hat. Möglicherweise musst du eine Browserwarnung durchklicken (z. B. „Behalten“ statt „Verwerfen“ in Chrome wählen) und die Windows Defender Warnung (**Mehr Infos** ⇒ **Trotzdem ausführen**).

   .. image:: img/install_thonny1.png

#. Klicke anschließend auf **Weiter** und **Installieren**, um die Installation von Thonny abzuschließen.

   .. image:: img/install_thonny6.png

Thonny IDE Einführung
----------------------------------

* Ref: `realpython <https://realpython.com/micropython/>`_

.. image:: img/thonny_ide.jpg

* **A**: Die Menüleiste mit Neu, Speichern, Bearbeiten, Ansicht, Ausführen, Debuggen usw.
* **B**: Dieses Papier-Symbol ermöglicht es dir, eine neue Datei zu erstellen.
* **C**: Wenn dein Raspberry Pi Pico 2 W bereits an deinen Computer angeschlossen ist, kannst du vorhandene Dateien auf deinem Computer oder Pico öffnen.
* **D**: Klicke auf das Disketten-Symbol, um den Code zu speichern. Du kannst auch wählen, ob du den Code auf deinem Computer oder dem Raspberry Pi Pico 2 W speichern möchtest.
* **E**: Das Abspiel-Symbol ermöglicht es dir, den Code auszuführen. Bevor du den Code ausführst, speichere ihn, wenn du das noch nicht getan hast.
* **F**: Das Debug-Symbol ermöglicht es dir, deinen Code zu debuggen. Beim Schreiben von Code wirst du unvermeidlich auf Fehler stoßen. Es gibt viele Formen von Fehlern, einschließlich falscher Syntax und logischer Fehler. Debugging ist das Werkzeug, um Fehler zu finden und zu untersuchen.

.. note::

    Wenn MicroPython (Raspberry Pi Pico).COMxx als Interpreter ausgewählt ist, kann das Debug-Tool nicht verwendet werden.
    
    Um deinen Code zu debuggen, wähle den Interpreter als Standardinterpreter und speichere ihn nach dem Debuggen auf deinem Computer.

    Du kannst den debuggten Code nun auf deinem Raspberry Pi Pico 2 W speichern, indem du erneut den MicroPython (Raspberry Pi Pico).COMxx Interpreter auswählst, auf die Schaltfläche „Speichern unter“ klickst und dann erneut auf die Schaltfläche „Speichern“ klickst.

* Wenn du auf das Debug-Symbol klickst, kannst du das Programm schrittweise mit den Pfeil-Icons G, H und I ausführen. Wenn du auf jedes Pfeil klickst, erscheint ein gelb hervorgehobener Balken, der anzeigt, welche Python-Zeile oder welcher Abschnitt gerade ausgewertet wird.

    * **G**: Einen großen Schritt machen, was bedeutet, zur nächsten Zeile oder zum nächsten Codeblock zu springen.
    * **H**: Einen kleinen Schritt machen bedeutet, jedes Element tiefergehend zu verarbeiten.
    * **I**: Aus dem Debugger aussteigen.
* **J**: Klicke darauf, um vom Debug-Modus in den Wiedergabemodus zurückzukehren.
* **K**: Verwende das Stopp-Symbol, um die Codeausführung zu stoppen.
* **L**: Skriptbereich, wo du deinen Python-Code schreiben kannst.
* **M**: Python-Shell, wo du einen einzelnen Befehl eingeben kannst, und wenn du die Eingabetaste drückst, wird der einzelne Befehl ausgeführt und liefert Informationen über das laufende Programm. Dies wird auch als REPL bezeichnet, was für „Read, Evaluate, Print und Loop“ steht.
* **N**: Interpreter, wo die aktuelle Version von Python angezeigt wird, mit der dein Programm ausgeführt wird, kann manuell durch Klicken darauf auf eine andere Version geändert werden.

.. note::

   **Keine MicroPython(Raspberry Pi Pico 2 W) Interpreter-Option?**

   * Stelle sicher, dass dein Pico über ein USB-Kabel mit deinem Computer verbunden ist.
   * Der Raspberry Pi Pico 2 W Interpreter ist nur in Version 3.3.3 oder einer höheren Version von Thonny verfügbar. Wenn du eine ältere Version verwendest, bitte aktualisiere.
