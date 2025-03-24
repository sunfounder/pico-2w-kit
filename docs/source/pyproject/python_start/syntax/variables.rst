.. note::
   Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein zusammen mit anderen Begeisterten.

   **Warum beitreten?**

   - **Expertenunterstützung**: Löse Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
   - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um deine Fähigkeiten zu verbessern.
   - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
   - **Sonderangebote**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
   - **Festliche Aktionen und Verlosungen**: Nimm an Verlosungen und Feiertagsaktionen teil.

   👉 Bereit, mit uns zu erkunden und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt heute bei!

Variablen
==============

Variablen sind Behälter, die verwendet werden, um Datenwerte zu speichern.

Das Erstellen einer Variablen ist sehr einfach. Du musst ihr lediglich einen Namen geben und einen Wert zuweisen. Es ist nicht nötig, den Datentyp der Variablen bei der Zuweisung anzugeben, da die Variable eine Referenz ist und über die Zuweisung auf Objekte verschiedener Datentypen zugreift.

Beim Benennen von Variablen müssen die folgenden Regeln eingehalten werden:

* Variablennamen dürfen nur Zahlen, Buchstaben und Unterstriche enthalten.
* Das erste Zeichen des Variablennamens muss ein Buchstabe oder ein Unterstrich sein.
* Variablennamen sind groß- und kleinschreibungssensitiv.

Variable erstellen
----------------------

In MicroPython gibt es keinen Befehl zum Deklarieren von Variablen. Variablen werden erstellt, indem ihnen zum ersten Mal ein Wert zugewiesen wird. Es ist keine spezifische Typdeklaration notwendig, und du kannst sogar den Typ nach dem Setzen der Variablen ändern.

.. code-block:: python

    x = 8       # x ist vom Typ int
    x = "lily"  # x ist jetzt vom Typ str
    print(x)

>>> %Run -c $EDITOR_CONTENT
lily


Casting
-------------

Wenn du den Datentyp für die Variable festlegen möchtest, kannst du dies durch Casting tun.

.. code-block:: python

    x = int(5)    # x wird 5 sein
    y = str(5)    # y wird '5' sein
    z = float(5)  # z wird 5.0 sein
    print(x, y, z)

>>> %Run -c $EDITOR_CONTENT
5 5 5.0

Typ abfragen
-------------------

Du kannst den Datentyp einer Variablen mit der Funktion `type()` abfragen.

.. code-block:: python

    x = 5
    y = "hello"
    z = 5.0
    print(type(x),type(y),type(z))

>>> %Run -c $EDITOR_CONTENT
<class 'int'> <class 'str'> <class 'float'>

Einzelne oder doppelte Anführungszeichen?
---------------------------------------------

In MicroPython können sowohl einfache als auch doppelte Anführungszeichen verwendet werden, um Zeichenkettenvariablen zu definieren.



.. code-block:: python

    x = "hello"
    # ist dasselbe wie
    x = 'hello'

Groß- und Kleinschreibung
----------------------------


Variablennamen sind groß- und kleinschreibungsempfindlich.

.. code-block:: python

    a = 5
    A = "lily"
    # A wird a nicht überschreiben
    print(a, A)

>>> %Run -c $EDITOR_CONTENT
5 lily


