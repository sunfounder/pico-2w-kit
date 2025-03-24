.. note::

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche gemeinsam mit anderen Technikbegeisterten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Löse Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um deine Fähigkeiten weiterzuentwickeln.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und Vorab-Einblicken.
    - **Sonderrabatte**: Profitiere von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nimm an Gewinnspielen und saisonalen Aktionen teil.

    👉 Bereit, gemeinsam mit uns Neues zu entdecken und zu erschaffen? Klicke auf [|link_sf_facebook|] und werde noch heute Mitglied!

.. _syntax_list:

Listen
===================

Listen werden verwendet, um mehrere Elemente in einer einzigen Variablen zu speichern, und werden mit eckigen Klammern erstellt:

.. code-block:: python

    B_list = ["Blossom", "Bubbles","Buttercup"]
    print(B_list)

Listenelemente sind veränderbar, geordnet und erlauben doppelte Werte.  
Die Elemente in der Liste sind indiziert, wobei das erste Element den Index [0], das zweite den Index [1] usw. hat.

.. code-block:: python

    C_list = ["Red", "Blue", "Green", "Blue"]
    print(C_list)            # Duplikat
    print(C_list[0]) 
    print(C_list[1])         # geordnet
    C_list[2] = "Purple"     # veränderbar
    print(C_list)

>>> %Run -c $EDITOR_CONTENT
['Red', 'Blue', 'Green', 'Blue']
Red
Blue
['Red', 'Blue', 'Purple', 'Blue']

Eine Liste kann verschiedene Datentypen enthalten:

.. code-block:: python

    A_list = ["Banana", 255, False, 3.14]
    print(A_list)

>>> %Run -c $EDITOR_CONTENT
['Banana', 255, False, 3.14]


Länge der Liste
------------------
Um die Anzahl der Elemente in einer Liste zu ermitteln, verwende die Funktion len().

.. code-block:: python

    A_list = ["Banana", 255, False, 3.14]
    print(len(A_list))

>>> %Run -c $EDITOR_CONTENT
4

Listenelemente überprüfen
-----------------------------

Das zweite Element der Liste ausgeben:

.. code-block:: python

    A_list = ["Banana", 255, False, 3.14]
    print(A_list[1])

>>> %Run -c $EDITOR_CONTENT
[255]

Das letzte Element der Liste ausgeben:

.. code-block:: python

    A_list = ["Banana", 255, False, 3.14]
    print(A_list[-1])

>>> %Run -c $EDITOR_CONTENT
[3.14]

Das zweite und dritte Element ausgeben:

.. code-block:: python

    A_list = ["Banana", 255, False, 3.14]
    print(A_list[1:3])

>>> %Run -c $EDITOR_CONTENT
[255, False]


Listenelemente ändern
-------------------------------
Das zweite und dritte Element ändern:

.. code-block:: python

    A_list = ["Banana", 255, False, 3.14]
    A_list[1:3] = [True,"Orange"] 
    print(A_list)

>>> %Run -c $EDITOR_CONTENT
['Banana', True, 'Orange', 3.14]

Den zweiten Wert durch zwei neue Werte ersetzen:

.. code-block:: python

    A_list = ["Banana", 255, False, 3.14]
    A_list[1:2] = [True,"Orange"] 
    print(A_list)

>>> %Run -c $EDITOR_CONTENT
['Banana', True, 'Orange', False, 3.14]


Elemente zur Liste hinzufügen
-------------------------------------

Ein Element mit der append()-Methode hinzufügen:

.. code-block:: python

    C_list = ["Red", "Blue", "Green"]
    C_list.append("Orange")
    print(C_list)

>>> %Run -c $EDITOR_CONTENT
['Red', 'Blue', 'Green', 'Orange']

Ein Element an zweiter Stelle einfügen:

.. code-block:: python

    C_list = ["Red", "Blue", "Green"]
    C_list.insert(1, "Orange")
    print(C_list)

>>> %Run -c $EDITOR_CONTENT
['Red', 'Orange', 'Blue', 'Green']



Listenelemente entfernen
-----------------------------

Die remove()-Methode entfernt ein bestimmtes Element:

.. code-block:: python

    C_list = ["Red", "Blue", "Green"]
    C_list.remove("Blue")
    print(C_list)

>>> %Run -c $EDITOR_CONTENT
['Red', 'Green']

Die pop()-Methode entfernt den angegebenen Index. Wenn kein Index angegeben wird, wird das letzte Element entfernt:

.. code-block:: python

    A_list = ["Banana", 255, False, 3.14, True,"Orange"]
    A_list.pop(1)
    print(A_list)
    A_list.pop()
    print(A_list)

>>> %Run -c $EDITOR_CONTENT
255
['Banana', False, 3.14, True, 'Orange']
'Orange'
['Banana', False, 3.14, True]

Das Schlüsselwort ``del`` entfernt ebenfalls ein Element an einem bestimmten Index:

.. code-block:: python

    C_list = ["Red", "Blue", "Green"]
    del C_list[1]
    print(C_list)

>>> %Run -c $EDITOR_CONTENT
['Red', 'Green']

Die clear()-Methode leert die Liste. Die Liste existiert weiterhin, enthält jedoch keine Elemente mehr:

.. code-block:: python

    C_list = ["Red", "Blue", "Green"]
    C_list.clear()
    print(C_list)

>>> %Run -c $EDITOR_CONTENT
[]