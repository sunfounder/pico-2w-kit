.. note:: 

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein – gemeinsam mit anderen Technikbegeisterten.

    **Warum solltest du beitreten?**

    - **Expertenunterstützung**: Erhalte Hilfe bei Problemen nach dem Kauf und bei technischen Herausforderungen – durch unsere Community und unser Team.
    - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um deine Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugriff auf Produktneuheiten und exklusive Einblicke.
    - **Sonderrabatte**: Profitiere von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festliche Aktionen & Gewinnspiele**: Nimm an Gewinnspielen und saisonalen Aktionen teil.

    👉 Bereit, gemeinsam mit uns Neues zu entdecken und zu gestalten? Klicke auf [|link_sf_facebook|] und werde noch heute Teil der Community!

Datentypen
===========

Eingebaute Datentypen
---------------------
MicroPython stellt folgende Datentypen bereit:

* Texttyp: str  
* Numerische Typen: int, float, complex  
* Sequenztypen: list, tuple, range  
* Mapping-Typ: dict  
* Mengentypen: set, frozenset  
* Boolescher Typ: bool  
* Binäre Typen: bytes, bytearray, memoryview  

Den Datentyp ermitteln
-----------------------------
Du kannst den Datentyp eines Objekts mit der Funktion ``type()`` ermitteln:

.. code-block:: python

    a = 6.8
    print(type(a))

>>> %Run -c $EDITOR_CONTENT
<class 'float'>

Den Datentyp setzen
----------------------
In MicroPython musst du den Datentyp nicht explizit festlegen – er wird automatisch beim Zuweisen eines Wertes bestimmt.



.. code-block:: python

    x = "welcome"
    y = 45
    z = ["apple", "banana", "cherry"]

    print(type(x))
    print(type(y))
    print(type(z))

>>> %Run -c $EDITOR_CONTENT
<class 'str'>
<class 'int'>
<class 'list'>
>>> 

Einen bestimmten Datentyp zuweisen
--------------------------------------

Wenn du einen bestimmten Datentyp explizit setzen möchtest, kannst du folgende Konstruktorfunktionen verwenden:

.. list-table:: 
    :widths: 25 10
    :header-rows: 1

    *   - Beispiel
        - Datentyp
    *   - x = int(20)
        - int
    *   - x = float(20.5)
        - float
    *   - x = complex(1j)
        - complex
    *   - x = str("Hello World")
        - str
    *   - x = list(("apple", "banana", "cherry"))
        - list
    *   - x = tuple(("apple", "banana", "cherry"))
        - tuple
    *   - x = range(6)
        - range
    *   - x = dict(name="John", age=36)
        - dict
    *   - x = set(("apple", "banana", "cherry"))
        - set
    *   - x = frozenset(("apple", "banana", "cherry"))
        - frozenset
    *   - x = bool(5)
        - bool
    *   - x = bytes(5)
        - bytes
    *   - x = bytearray(5)
        - bytearray
    *   - x = memoryview(bytes(5))
        - memoryview

Du kannst einige davon ausgeben lassen, um das Ergebnis zu sehen:



.. code-block:: python

    a = float(20.5)
    b = list(("apple", "banana", "cherry"))
    c = bool(5)

    print(a)
    print(b)
    print(c)

>>> %Run -c $EDITOR_CONTENT
20.5
['apple', 'banana', 'cherry']
True
>>> 

Typumwandlung
----------------
Du kannst Typen mit den Funktionen int(), float() und complex() umwandeln. 
Casting in Python erfolgt über Konstruktorfunktionen:

* int() – erstellt eine Ganzzahl aus einem Integer-, Float- oder String-Literal (sofern der String eine ganze Zahl darstellt)
* float() – erstellt eine Gleitkommazahl aus einem Integer-, Float- oder String-Literal (sofern der String eine Zahl darstellt)
* str() – erstellt einen String aus verschiedenen Datentypen, z. B. aus Zahlen oder bereits bestehenden Strings



.. code-block:: python

    a = float("5")
    b = int(3.7)
    c = str(6.0)

    print(a)
    print(b)
    print(c)

Hinweis: Komplexe Zahlen können nicht in andere numerische Typen umgewandelt werden.