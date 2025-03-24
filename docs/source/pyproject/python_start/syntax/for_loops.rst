.. note:: 

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche gemeinsam mit anderen Technikbegeisterten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum solltest du beitreten?**

    - **Expertenhilfe**: Löse Probleme nach dem Kauf sowie technische Herausforderungen mit Unterstützung unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um dein Wissen zu erweitern.
    - **Exklusive Einblicke**: Erhalte frühzeitigen Zugang zu Produktankündigungen und exklusiven Vorschauen.
    - **Sonderrabatte**: Profitiere von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festliche Aktionen & Gewinnspiele**: Nimm an Verlosungen und saisonalen Aktionen teil.

    👉 Bereit, gemeinsam mit uns zu entdecken und zu gestalten? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _syntax_forloop:

For-Schleifen
================

Die ``for``-Schleife kann durch beliebige Sequenzen iterieren, z. B. Listen oder Zeichenketten.

Die Syntax einer for-Schleife lautet:

.. code-block:: python

    for val in sequence:
        Body of for


Hierbei ist ``val`` eine Variable, die bei jeder Iteration den Wert eines Elements aus der Sequenz erhält.

Die Schleife läuft, bis das letzte Element erreicht wurde. Durch Einrückung wird der Schleifenrumpf vom übrigen Code abgegrenzt.

**Ablaufdiagramm einer for-Schleife**

.. image:: img/for_loop.png




.. code-block:: python

    numbers = [1, 2, 3, 4]
    sum = 0

    for val in numbers:
        sum = sum+val
        
    print("The sum is", sum)

>>> %Run -c $EDITOR_CONTENT
The sum is 10

Die break-Anweisung
-------------------------

Mit der break-Anweisung kann die Schleife vorzeitig abgebrochen werden, ohne alle Elemente zu durchlaufen:



.. code-block:: python

    numbers = [1, 2, 3, 4]
    sum = 0

    for val in numbers:
        sum = sum+val
        if sum == 6:
            break
    print("The sum is", sum)

>>> %Run -c $EDITOR_CONTENT
The sum is 6

Die continue-Anweisung
------------------------------

Mit der ``continue``-Anweisung wird der aktuelle Schleifendurchlauf abgebrochen und mit dem nächsten fortgefahren:



.. code-block:: python

    numbers = [1, 2, 3, 4]

    for val in numbers:
        if val == 3:
            continue
        print(val)

>>> %Run -c $EDITOR_CONTENT
1
2
4

Die range()-Funktion
------------------------------

Mit der range()-Funktion lässt sich eine Zahlenfolge erzeugen. range(6) erzeugt die Werte von 0 bis 5 (also 6 Zahlen).

Optional können auch Start-, Endwert und Schrittweite angegeben werden: range(start, stop, step_size). Wird step_size nicht angegeben, ist sie standardmäßig 1.

Das range-Objekt ist „lazy“ – es erzeugt die Zahlen erst beim Durchlaufen, was speichereffizient ist. Es ist jedoch kein Iterator, da es in, len und ``__getitem__`` unterstützt.

Um alle Werte explizit zu sehen, kann list() verwendet werden:

.. code-block:: python

    print(range(6))

    print(list(range(6)))

    print(list(range(2, 6)))

    print(list(range(2, 10, 2)))

>>> %Run -c $EDITOR_CONTENT
range(0, 6)
[0, 1, 2, 3, 4, 5]
[2, 3, 4, 5]
[2, 4, 6, 8]



``range()`` kann mit einer ``for``-Schleife kombiniert werden, um eine Zahlenreihe zu durchlaufen. Mit len() lässt sich zusätzlich über Indizes iterieren:

.. code-block:: python

    fruits = ['pear', 'apple', 'grape']

    for i in range(len(fruits)):
        print("I like", fruits[i])
        
>>> %Run -c $EDITOR_CONTENT
I like pear
I like apple
I like grape

Else in For-Schleifen
------------------------------

Die ``for``-Schleife kann optional auch einen ``else``-Block enthalten. Wenn alle Elemente der Sequenz durchlaufen wurden, wird der ``else``-Teil ausgeführt.

Mit dem Schlüsselwort ``break`` kann die ``for``-Schleife vorzeitig beendet werden. In diesem Fall wird der ``else``-Block übersprungen.

Wird die Schleife jedoch nicht unterbrochen, wird der ``else``-Teil der ``for``-Schleife ausgeführt.



.. code-block:: python

    for val in range(5):
        print(val)
    else:
        print("Finished")

>>> %Run -c $EDITOR_CONTENT
0
1
2
3
4
Finished


Der else-Block wird nicht ausgeführt, wenn die Schleife durch break beendet wurde:

.. code-block:: python


    for val in range(5):
        if val == 2: break
        print(val)
    else:
        print("Finished")

>>> %Run -c $EDITOR_CONTENT
0
1

