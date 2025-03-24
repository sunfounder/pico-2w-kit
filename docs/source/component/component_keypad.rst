.. note::

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community auf Facebook! Entdecken Sie gemeinsam mit anderen begeisterten Mitgliedern die vielfältigen Möglichkeiten rund um Raspberry Pi, Arduino und ESP32.

    **Why Join?**

    - **Expert Support**: Erhalten Sie Unterstützung bei technischen Fragen und After-Sales-Problemen durch unsere Community und unser Team.
    - **Learn & Share**: Tauschen Sie Ihre Erfahrungen, Tipps und Tutorials aus, um Ihre Kenntnisse zu erweitern.
    - **Exclusive Previews**: Bekommen Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Vorschauen.
    - **Special Discounts**: Profitieren Sie von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festive Promotions and Giveaways**: Nehmen Sie an saisonalen Aktionen und Gewinnspielen teil.

    👉 Bereit, gemeinsam mit uns Neues zu entdecken und kreativ zu werden? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

.. _cpn_keypad:

4x4 Keypad
========================


In Mikrocontrollersystemen werden häufig Matrix-Keypads verwendet, um Geräte mit vielen Tasten – wie elektronische Schlösser oder Telefon-Tastaturen – anzusteuern, insbesondere wenn 12 bis 16 Tasten benötigt werden.

Ein Matrix-Keypad (auch als Zeilen-Spalten-Tastatur bezeichnet) besteht aus vier I/O-Leitungen für die Zeilen und vier weiteren für die Spalten. Jeder Schnittpunkt zwischen einer Zeile und einer Spalte entspricht einer einzelnen Taste, sodass insgesamt 4×4 Tasten zur Verfügung stehen. Diese Anordnung optimiert effizient die Nutzung von I/O-Ports eines Mikrocontrollers.

Die Kontakte des Keypads sind normalerweise über einen Steckverbinder zugänglich, der an ein Flachbandkabel angeschlossen oder direkt in eine Leiterplatte gesteckt werden kann. Bei manchen Keypads besitzt jede Taste einen eigenen Anschluss am Steckverbinder, wobei alle Tasten einen gemeinsamen Masseanschluss haben.


|img_keypad|

Meist sind die Tasten jedoch in einer Matrix verschaltet, wobei jede Taste 
eine spezifische Verbindung zwischen einer Zeilen- und einer Spaltenleitung 
herstellt. Ein Mikrocontroller kann diese Tastenmatrix durch zyklisches 
Abtasten (Polling) auswerten, indem er nacheinander jeder der vier horizontalen 
Leitungen ein Ausgangssignal gibt und gleichzeitig die vier vertikalen Leitungen 
überprüft. So lässt sich feststellen, welche Taste gedrückt wurde. Pull-up- oder 
Pull-down-Widerstände sollten an den Eingängen verwendet werden, um undefinierte 
Zustände des Mikrocontrollers zu verhindern, wenn kein Signal vorhanden ist.

* `Keypad - Wikipedia <https://en.wikipedia.org/wiki/Keypad>`_

**Example**

* :ref:`py_keypad` (Für MicroPython-Nutzer)
* :ref:`py_guess_number` (Für MicroPython-Nutzer)
* :ref:`ar_keypad` (Für Arduino-Nutzer)
