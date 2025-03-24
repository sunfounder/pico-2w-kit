.. note::
   Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein zusammen mit anderen Begeisterten.

   **Warum beitreten?**

   - **Expertenunterstützung**: Löse Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
   - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um deine Fähigkeiten zu verbessern.
   - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
   - **Sonderangebote**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
   - **Festliche Aktionen und Verlosungen**: Nimm an Verlosungen und Feiertagsaktionen teil.

   👉 Bereit, mit uns zu erkunden und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt heute bei!

1.1 Einführung in MicroPython
======================================

MicroPython ist eine Software-Implementierung einer Programmiersprache, die weitgehend mit Python 3 kompatibel ist, in C geschrieben und optimiert, um auf einem Mikrocontroller zu laufen.

MicroPython besteht aus einem Python-Compiler zu Bytecode und einem Laufzeitinterpreter dieses Bytecodes. Dem Benutzer wird eine interaktive Eingabeaufforderung (das REPL) präsentiert, um unterstützte Befehle sofort auszuführen. Eingeschlossen sind eine Auswahl an Kern-Python-Bibliotheken; MicroPython umfasst Module, die dem Programmierer Zugang zu Hardware auf niedriger Ebene bieten.

* Referenz: `MicroPython - Wikipedia <https://en.wikipedia.org/wiki/MicroPython>`_

Die Geschichte beginnt hier
--------------------------------

Alles änderte sich im Jahr 2013, als Damien George eine Crowdfunding-Kampagne (Kickstarter) startete.

Damien war ein Student der Universität Cambridge und ein begeisterter Robotik-Programmierer. Er wollte die Welt von Python von einer Gigabyte-Maschine auf eine Kilobyte-Maschine reduzieren. Seine Kickstarter-Kampagne sollte seine Entwicklung unterstützen, während er seinen Proof of Concept in eine fertige Implementierung umwandelte.

MicroPython wird von einer vielfältigen Pythonista-Gemeinschaft unterstützt, die ein starkes Interesse daran hat, das Projekt erfolgreich zu sehen.

Neben dem Testen und Unterstützen der Codebasis stellten die Entwickler Tutorials, Code-Bibliotheken und Hardware-Portierungen bereit, sodass Damien sich auf andere Aspekte des Projekts konzentrieren konnte.

* Referenz: `realpython <https://realpython.com/micropython/>`_

Warum MicroPython？
---------------------

Obwohl die ursprüngliche Kickstarter-Kampagne MicroPython als Entwicklungsboard "pyboard" mit STM32F4 herausbrachte, unterstützt MicroPython viele auf ARM basierende Produktarchitekturen. Die hauptsächlich unterstützten Ports sind ARM Cortex-M (viele STM32-Boards, TI CC3200/WiPy, Teensy-Boards, Nordic nRF-Serie, SAMD21 und SAMD51), ESP8266, ESP32, 16-bit PIC, Unix, Windows, Zephyr und JavaScript.
Zweitens ermöglicht MicroPython schnelles Feedback. Dies liegt daran, dass du REPL verwenden kannst, um Befehle interaktiv einzugeben und Antworten zu erhalten. Du kannst sogar Code anpassen und sofort ausführen, anstatt den Code-Kompilieren-Upload-Ausführen-Zyklus zu durchlaufen.

Während Python dieselben Vorteile bietet, sind einige Mikrocontroller-Boards wie das Raspberry Pi Pico klein, einfach und haben wenig Speicher, um die Python-Sprache überhaupt auszuführen. Deshalb hat sich MicroPython entwickelt, indem es die Hauptmerkmale von Python beibehält und eine Reihe neuer Funktionen hinzufügt, um mit diesen Mikrocontroller-Boards zu arbeiten.

Als Nächstes lernst du, MicroPython auf dem Raspberry Pi Pico zu installieren.

* Referenz: `MicroPython - Wikipedia <https://en.wikipedia.org/wiki/MicroPython>`_
* Referenz: `realpython <https://realpython.com/micropython/>`_
