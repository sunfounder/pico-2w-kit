.. note::

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche gemeinsam mit anderen Technikbegeisterten tiefer in Raspberry Pi, Arduino und ESP32 ein.

    **Warum solltest du beitreten?**

    - **Expertenunterstützung**: Erhalte Hilfe bei technischen Herausforderungen und Fragen nach dem Kauf – durch unser Team und die Community.
    - **Lernen & Teilen**: Tausche Tipps, Erfahrungen und Anleitungen aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Einblicke**: Erfahre frühzeitig von neuen Produktankündigungen und erhalte spannende Einblicke.
    - **Sonderrabatte**: Profitiere von exklusiven Angeboten auf unsere neuesten Produkte.
    - **Aktionen und Gewinnspiele**: Nimm an saisonalen Events und Verlosungen teil.

    👉 Bereit, gemeinsam mit uns Neues zu entdecken und zu erschaffen? Klicke auf [|link_sf_facebook|] und werde Teil der Community!

Funktionen
==============

In MicroPython ist eine Funktion eine Gruppe zusammenhängender Anweisungen, die eine bestimmte Aufgabe erfüllen.

Funktionen helfen dabei, Programme in kleinere, modularere Blöcke zu unterteilen. Wenn unser Projekt wächst, sorgen Funktionen für mehr Übersicht und Struktur.

Außerdem vermeiden sie Wiederholungen und machen den Code wiederverwendbar.

Funktion erstellen
---------------------

.. code-block::

    def function_name(parameters): 
        """docstring"""
        statement(s)

* Eine Funktion wird mit dem Schlüsselwort ``def`` definiert.

* Der Funktionsname dient zur eindeutigen Identifikation. Die Namensgebung folgt denselben Regeln wie bei Variablen:

   * Nur Buchstaben, Zahlen und Unterstriche sind erlaubt.
   * Das erste Zeichen muss ein Buchstabe oder Unterstrich sein.
   * Groß- und Kleinschreibung wird unterschieden.

* Parameter (Argumente), über die Werte an die Funktion übergeben werden. Diese sind optional.

* Ein Doppelpunkt (:) kennzeichnet das Ende des Funktionskopfs.

* Ein optionaler Docstring beschreibt den Zweck der Funktion, üblicherweise in dreifachen Anführungszeichen, um mehrzeilige Dokumentationen zu ermöglichen.

* Eine oder mehrere gültige MicroPython-Anweisungen bilden den Funktionskörper. Alle Anweisungen müssen dieselbe Einrückungstiefe haben (normalerweise 4 Leerzeichen).

* Jede Funktion benötigt mindestens eine Anweisung. Falls keine benötigt wird, kann ``pass`` verwendet werden, um Fehler zu vermeiden.

* Eine optionale ``return``-Anweisung gibt einen Wert von der Funktion zurück.


Funktion aufrufen
---------------------

Um eine Funktion aufzurufen, fügt man Klammern an den Funktionsnamen an.



.. code-block:: python

    def my_function():
        print("Your first function")

    my_function()

>>> %Run -c $EDITOR_CONTENT
Your first function

Die return-Anweisung
--------------------------

Die return-Anweisung wird verwendet, um eine Funktion zu beenden und an die Aufrufstelle zurückzukehren.

**Syntax von return**

.. code-block:: python

    return [expression_list]

Die Anweisung kann einen Ausdruck enthalten, der ausgewertet wird und dessen Ergebnis zurückgegeben wird. Fehlt der Ausdruck oder die ``return``-Anweisung gänzlich, gibt die Funktion ``None`` zurück.



.. code-block:: python

    def my_function():
            print("Your first function")

    print(my_function())

>>> %Run -c $EDITOR_CONTENT
Your first function
None

Hier ist ``None`` der Rückgabewert, da keine ``return``-Anweisung verwendet wurde.

Argumente
-------------

Informationen können als Argumente an eine Funktion übergeben werden.

Argumente werden in Klammern nach dem Funktionsnamen angegeben. Es können beliebig viele Argumente verwendet werden, getrennt durch Kommata.



.. code-block:: python

    def welcome(name, msg):
        """This is a welcome function for
        the person with the provided message"""
        print("Hello", name + ', ' + msg)

    welcome("Lily", "Welcome to China!")

>>> %Run -c $EDITOR_CONTENT
Hello Lily, Welcome to China!


Anzahl der Argumente
*************************

Standardmäßig muss eine Funktion mit der richtigen Anzahl an Argumenten aufgerufen werden. Wenn zwei Parameter erwartet werden, muss die Funktion auch mit genau zwei Argumenten aufgerufen werden.



.. code-block:: python

    def welcome(name, msg):
        """This is a welcome function for
        the person with the provided message"""
        print("Hello", name + ', ' + msg)

    welcome("Lily", "Welcome to China!")

Hier hat die Funktion welcome() zwei Parameter.

Da wir diese Funktion mit zwei Argumenten aufgerufen haben, läuft sie fehlerfrei und ohne Probleme.

Wird sie jedoch mit einer anderen Anzahl von Argumenten aufgerufen, zeigt der Interpreter eine Fehlermeldung an.

Im Folgenden sehen Sie Funktionsaufrufe mit nur einem beziehungsweise keinem Argument sowie die entsprechenden Fehlermeldungen.

.. code-block::

    welcome("Lily")＃Only one argument

>>> %Run -c $EDITOR_CONTENT
Traceback (most recent call last):
  File "<stdin>", line 6, in <module>
TypeError: function takes 2 positional arguments but 1 were given

.. code-block::

    welcome()＃No arguments

>>> %Run -c $EDITOR_CONTENT
Traceback (most recent call last):
  File "<stdin>", line 6, in <module>
TypeError: function takes 2 positional arguments but 0 were given


Standardargumente
*************************

In MicroPython können wir Standardwerte für Parameter mit dem Gleichheitszeichen (=) definieren.

Wenn beim Funktionsaufruf kein Wert übergeben wird, wird der Standardwert verwendet.

.. code-block:: python

    def welcome(name, msg = "Welcome to China!"):
        """This is a welcome function for
        the person with the provided message"""
        print("Hello", name + ', ' + msg)
    welcome("Lily")

>>> %Run -c $EDITOR_CONTENT
Hello Lily, Welcome to China!

In dieser Funktion hat der Parameter ``name`` keinen Standardwert und muss daher beim Aufruf zwingend angegeben werden.

Der Parameter ``msg`` hingegen besitzt den Standardwert "Welcome to China!". Daher ist dieser beim Funktionsaufruf optional – wird ein anderer Wert übergeben, überschreibt er den Standardwert.

Beliebig viele Parameter einer Funktion können mit einem Standardwert versehen werden. Allerdings gilt: Sobald ein Parameter einen Standardwert besitzt, müssen alle nachfolgenden Parameter ebenfalls einen Standardwert haben.

Das bedeutet, dass kein Pflichtparameter einem Parameter mit Standardwert folgen darf.

Ein Beispiel: Wenn wir den Funktionskopf wie folgt definieren:

.. code-block:: python

    def welcome(name = "Lily", msg):

We will receive the following error message:

>>> %Run -c $EDITOR_CONTENT
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
SyntaxError: non-default argument follows default argument


Schlüsselwortargumente
**************************

Wenn wir eine Funktion mit bestimmten Werten aufrufen, werden diese Werte entsprechend ihrer Reihenfolge den Parametern zugewiesen.

Zum Beispiel in der oben genannten Funktion welcome(): Wenn wir sie mit welcome("Lily", "Welcome to China") aufrufen, wird der Wert "Lily" dem Parameter ``name`` zugewiesen und "Welcome to China" dem Parameter ``msg``.

MicroPython erlaubt auch Funktionsaufrufe mit benannten Argumenten (Keyword Arguments). Wird eine Funktion auf diese Weise aufgerufen, kann die Reihenfolge der Argumente beliebig geändert werden.

.. code-block:: python

    # benannte Argumente
    welcome(name = "Lily", msg = "Welcome to China!")

    # benannte Argumente (Reihenfolge vertauscht)
    welcome(msg = "Welcome to China!", name = "Lily")

    # 1 Positionsargument, 1 benanntes Argument
    welcome("Lily", msg = "Welcome to China!")

Wie man sieht, können Positions- und benannte Argumente beim Funktionsaufruf kombiniert werden. Wichtig ist jedoch, dass benannte Argumente immer nach den Positionsargumenten kommen müssen.

Wird ein Positionsargument nach einem benannten Argument angegeben, führt dies zu einem Fehler.

Beispiel für einen fehlerhaften Aufruf:

.. code-block:: python

    welcome(name="Lily","Welcome to China!")

Erzeugt folgenden Fehler:

>>> %Run -c $EDITOR_CONTENT
Traceback (most recent call last):
  File "<stdin>", line 5, in <module>
SyntaxError: non-keyword arg after keyword arg


Beliebige Anzahl an Argumenten
*********************************

Manchmal ist beim Schreiben einer Funktion im Voraus nicht bekannt, wie viele Argumente übergeben werden. 

In diesem Fall kann im Funktionskopf ein Sternchen (*) vor den Parameternamen gesetzt werden.

.. code-block:: python

    def welcome(*names):
        """This function welcomes all the person
        in the name tuple"""
        # names ist ein Tupel mit allen übergebenen Argumenten
        for name in names:
            print("Welcome to China!", name)

    welcome("Lily","John","Wendy")

>>> %Run -c $EDITOR_CONTENT
Welcome to China! Lily
Welcome to China! John
Welcome to China! Wendy

Hier haben wir die Funktion mit mehreren Argumenten aufgerufen. Diese Argumente werden vor der Übergabe an die Funktion in einem Tupel gebündelt.

Innerhalb der Funktion verwenden wir eine for-Schleife, um alle übergebenen Argumente einzeln abzurufen.



Rekursion
-------------

In Python kann eine Funktion nicht nur andere Funktionen aufrufen – sie kann auch sich selbst aufrufen. Solche Konstruktionen bezeichnet man als rekursive Funktionen.

Der Vorteil der Rekursion besteht darin, dass man damit Daten iterativ durchlaufen kann, um ein Ergebnis zu berechnen.

Beim Einsatz von Rekursion ist jedoch Vorsicht geboten, da man leicht eine Funktion schreiben kann, die nie endet oder sehr viele Ressourcen verbraucht. Richtig eingesetzt ist Rekursion jedoch ein eleganter und effizienter Programmieransatz.


.. code-block:: python

    def rec_func(i):
        if(i > 0):
            result = i + rec_func(i - 1)
            print(result)
        else:
            result = 0
        return result

    rec_func(6)

>>> %Run -c $EDITOR_CONTENT
1
3
6
10
15
21

In diesem Beispiel ruft die Funktion rec_func() sich selbst auf („Rekursion“). Dabei wird die Variable ``i`` bei jedem Aufruf um 1 dekrementiert. Sobald ``i`` den Wert 0 erreicht, endet die Rekursion.

Für Einsteiger ist es manchmal schwierig, das Prinzip zu verstehen. Am besten lernt man es durch Ausprobieren und schrittweises Anpassen des Codes.

**Vorteile der Rekursion**

* Rekursive Funktionen führen zu einem eleganten und aufgeräumten Code.
* Komplexe Aufgaben lassen sich in kleinere Teilprobleme zerlegen.
* Die Erzeugung von Sequenzen ist mit Rekursion oft einfacher als mit verschachtelten Schleifen.

**Nachteile der Rekursion**

* Die Logik ist oft schwer nachzuvollziehen.
* Rekursive Aufrufe benötigen viele Ressourcen (Zeit und Speicher).
* Das Debuggen von rekursiven Funktionen ist komplizierter.
