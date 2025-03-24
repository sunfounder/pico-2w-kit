.. note::

   Hallo, willkommen in der Community für SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein mit Gleichgesinnten.
  
   **Warum beitreten?**

   - **Expertenunterstützung**: Löse Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
   - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um deine Fähigkeiten zu verbessern.
   - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
   - **Sonderangebote**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
   - **Festliche Aktionen und Verlosungen**: Nimm an Verlosungen und Feiertagsaktionen teil.

   👉 Bereit, mit uns zu erkunden und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt heute bei!

Operatoren
===========

Operatoren werden verwendet, um Operationen mit Variablen und Werten durchzuführen.

* :ref:`Arithmetische Operatoren`

* :ref:`Zuweisungsoperatoren`

* :ref:`Vergleichsoperatoren`

* :ref:`Logische Operatoren`

* :ref:`Identitätsoperatoren`

* :ref:`Mitgliedschaftsoperatoren`

* :ref:`Bitweise Operatoren`

Arithmetische Operatoren
------------------------------

Arithmetische Operatoren ermöglichen es dir, gängige mathematische Operationen durchzuführen.

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Operator
     - Name
   * - ``+``
     - Addition
   * - ``-``
     - Subtraktion
   * - ``*``
     - Multiplikation
   * - ``/``
     - Division
   * - ``%``
     - Modulus
   * - ``**``
     - Exponentiation
   * - ``//``
     - Ganzzahlige Division

  

.. code-block:: python

   x = 5
   y = 3

   a = x + y
   b = x - y
   c = x * y
   d = x / y
   e = x % y
   f = x ** y
   g = x // y

   print(a)
   print(b)
   print(c)
   print(d)
   print(e)
   print(f)
   print(g)

>>> %Run -c $EDITOR_CONTENT
8
2
15
1.666667
2
125
1
8
2
15
>>> 

Zuweisungsoperatoren
------------------------

Zuweisungsoperatoren werden verwendet, um Werte an Variablen zuzuweisen.

.. list-table::
   :widths: 10 30 30
   :header-rows: 1

   * - Operator
     - Example
     - Same As
   * - ``=``
     - a = 6
     - a =6
   * - ``+=``
     - a += 6
     - a = a + 6
   * - ``-=``
     - a -= 6
     - a = a - 6
   * - ``*=``
     - a \*= 6
     - a = a * 6
   * - ``/=``
     - a /= 6
     - a = a / 6
   * - ``%=``
     - a %= 6
     - a = a % 6
   * - ``**=``
     - a \*\*= 6
     - a = a ** 6
   * - ``//=``
     - a //= 6
     - a = a // 6
   * - ``&=``
     - a &= 6
     - a = a & 6
   * - ``|=``
     - a \|= 6
     - a = a | 6
   * - ``^=``
     - a ^= 6
     - a = a ^ 6
   * - ``>>=``
     - a >>= 6
     - a = a \>\> 6
   * - ``<<=``
     - a <<= 6
     - a = a << 6



.. code-block:: python

   a = 6

   a *= 6
   print(a)

>>> %Run test.py
36
>>> 

Vergleichsoperatoren
------------------------
Vergleichsoperatoren werden verwendet, um zwei Werte miteinander zu vergleichen.

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Operator
     - Name
   * - ``==``
     - Gleich
   * - ``!=``
     - Ungleich
   * - ``<``
     - Kleiner als
   * - ``>``
     - Größer als
   * - ``>=``
     - Größer gleich
   * - ``<=``
     - Kleiner gleich




.. code-block:: python

   a = 6
   b = 8

   print(a>b)

>>> %Run test.py
False
>>>

Gibt **False** zurück, weil **a** kleiner als **b** ist.

Logische Operatoren
-----------------------

Logische Operatoren werden verwendet, um Bedingungsaussagen zu kombinieren.

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Operator
     - Beschreibung
   * - ``and``
     - Gibt True zurück, wenn beide Aussagen wahr sind
   * - ``or``
     - Gibt True zurück, wenn eine der Aussagen wahr ist
   * - ``not``
     - Kehrt das Ergebnis um, gibt False zurück, wenn das Ergebnis wahr ist

.. code-block:: python

   a = 6
   print(a > 2 and a < 8)

>>> %Run -c $EDITOR_CONTENT
True
>>>

Identitätsoperatoren
------------------------

Identitätsoperatoren werden verwendet, um zu prüfen, ob es sich bei den Objekten um dasselbe Objekt handelt, nicht nur ob sie gleich sind, sondern ob sie dieselbe Speicheradresse verwenden.

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Operator
     - Beschreibung
   * - ``is``
     - Gibt True zurück, wenn beide Variablen dasselbe Objekt sind
   * - ``is not``
     - Gibt True zurück, wenn beide Variablen nicht dasselbe Objekt sind

.. code-block:: python

   a = ["hello", "welcome"]
   b = ["hello", "welcome"]
   c = a

   print(a is c)
   # gibt True zurück, weil z dasselbe Objekt wie x ist

   print(a is b)
   # gibt False zurück, weil x nicht dasselbe Objekt wie y ist, auch wenn sie denselben Inhalt haben

   print(a == b)
   # gibt True zurück, weil x gleich y ist

>>> %Run -c $EDITOR_CONTENT
True
False
True
>>>

Mitgliedschaftsoperatoren
------------------------------

Mitgliedschaftsoperatoren werden verwendet, um zu testen, ob eine Sequenz in einem Objekt vorhanden ist.

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Operator
     - Beschreibung
   * - ``in``
     - Gibt True zurück, wenn eine Sequenz mit dem angegebenen Wert im Objekt vorhanden ist
   * - ``not in``
     - Gibt True zurück, wenn eine Sequenz mit dem angegebenen Wert nicht im Objekt vorhanden ist

.. code-block:: python

   a = ["hello", "welcome", "Goodmorning"]

   print("welcome" in a)

>>> %Run -c $EDITOR_CONTENT
True
>>>

Bitweise Operatoren
------------------------

Bitweise Operatoren werden verwendet, um (binäre) Zahlen zu vergleichen.

.. list-table::
   :widths: 10 20 50
   :header-rows: 1

   * - Operator
     - Name
     - Beschreibung
   * - ``&``
     - UND
     - Setzt jedes Bit auf 1, wenn beide Bits 1 sind
   * - ``|``
     - ODER
     - Setzt jedes Bit auf 1, wenn eines der beiden Bits 1 ist
   * - ``^``
     - XOR
     - Setzt jedes Bit auf 1, wenn nur eines der beiden Bits 1 ist
   * - ``~``
     - NICHT
     - Kehrt alle Bits um
   * - ``<<``
     - Linksverschiebung mit Nullauffüllung
     - Verschiebt nach links, indem Nullen von rechts eingeschoben werden und die am weitesten links liegenden Bits herausfallen
   * - ``>>``
     - Signierte Rechtsverschiebung
     - Verschiebt nach rechts, indem Kopien des am weitesten links liegenden Bits von links eingeschoben werden und die am weitesten rechts liegenden Bits herausfallen

.. code-block:: python

   num = 2

   print(num & 1)
   print(num | 1)
   print(num << 1)

>>> %Run -c $EDITOR_CONTENT
0
3
4
>>>