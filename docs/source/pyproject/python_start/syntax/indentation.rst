.. note::

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche gemeinsam mit anderen Technikbegeisterten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Löse Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um deine Fähigkeiten weiterzuentwickeln.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und Vorab-Einblicken.
    - **Sonderrabatte**: Profitiere von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nimm an Gewinnspielen und saisonalen Aktionen teil.

    👉 Bereit, gemeinsam mit uns Neues zu entdecken und zu erschaffen? Klicke auf [|link_sf_facebook|] und werde noch heute Mitglied!

Einrückung
=============

Einrückung bezieht sich auf Leerzeichen am Anfang einer Codezeile.  
Wie bei Standard-Python-Programmen wird auch MicroPython-Code normalerweise von oben nach unten ausgeführt:  
Der Interpreter durchläuft Zeile für Zeile, führt sie aus und fährt dann mit der nächsten fort –  
genauso, wie man sie Zeile für Zeile im Shell-Terminal eingibt.  
Ein Programm, das die Befehle nur der Reihe nach abarbeitet, ist allerdings nicht sehr intelligent – daher bietet MicroPython, wie auch Python, eine eigene Methode zur Steuerung des Programmflusses: die Einrückung.

Vor print() muss mindestens ein Leerzeichen stehen, sonst erscheint eine Fehlermeldung wie „Invalid syntax“.  
Es wird empfohlen, die Einrückung einheitlich mit der Tabulatortaste oder vier Leerzeichen vorzunehmen.

.. code-block:: python

    if 8 > 5:
    print("Eight is greater than Five!")

>>> %Run -c $EDITOR_CONTENT
Traceback (most recent call last):
  File "<stdin>", line 2
SyntaxError: invalid syntax

Du musst innerhalb eines Codeblocks dieselbe Anzahl an Leerzeichen verwenden,  
sonst gibt Python einen Fehler aus.

.. code-block:: python

    if 8 > 5:
    print("Eight is greater than Five!")
            print("Eight is greater than Five")
            
>>> %Run -c $EDITOR_CONTENT
Traceback (most recent call last):
  File "<stdin>", line 2
SyntaxError: invalid syntax
