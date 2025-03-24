.. note:: 

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche gemeinsam mit anderen Technikbegeisterten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum solltest du beitreten?**

    - **Expertenhilfe**: Löse Probleme nach dem Kauf und technische Herausforderungen mit Unterstützung unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um deine Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugriff auf neue Produktankündigungen und exklusive Einblicke.
    - **Sonderrabatte**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen & Gewinnspiele**: Nimm an Gewinnspielen und saisonalen Aktionen teil.

    👉 Bereit, mit uns gemeinsam zu entdecken und zu entwickeln? Klicke auf [|link_sf_facebook|] und werde noch heute Mitglied!

Kommentare
=============

Kommentare im Code helfen uns dabei, den Code besser zu verstehen, ihn insgesamt lesbarer zu machen und Teile während des Testens gezielt auszukommentieren, sodass diese nicht ausgeführt werden.

Einzeilige Kommentare
----------------------------

Einzeilige Kommentare in MicroPython beginnen mit einem #. Der darauf folgende Text wird bis zum Ende der Zeile als Kommentar behandelt. Kommentare können sowohl vor als auch hinter einer Codezeile stehen.

.. code-block:: python

    print("hello world") # Das ist ein Kommentar

>>> %Run -c $EDITOR_CONTENT
hello world

Kommentare müssen nicht unbedingt erklärenden Text enthalten – du kannst auch Codezeilen auskommentieren, um deren Ausführung in MicroPython zu verhindern.

.. code-block:: python

    #print("Wird nicht ausgeführt!")
    print("hello world") # Das ist ein Kommentar

>>> %Run -c $EDITOR_CONTENT
hello world

Mehrzeilige Kommentare
------------------------------

Wenn du mehrere Zeilen kommentieren möchtest, kannst du einfach mehrere Zeilen mit # schreiben.

.. code-block:: python

    # Das ist ein Kommentar
    # über mehrere
    # Zeilen hinweg
    print("Hello, World!")

>>> %Run -c $EDITOR_CONTENT
Hello, World!

Alternativ kannst du auch mehrzeilige Strings verwenden:

Da MicroPython Zeichenketten ignoriert, die nicht an eine Variable gebunden sind, kannst du durch einfache Einfügung eines mehrzeiligen Strings (mit drei Anführungszeichen) Kommentare erzeugen:

.. code-block:: python

    """
    This is a comment
    written in
    more than just one line
    """
    print("Hello, World!")

>>> %Run -c $EDITOR_CONTENT
Hello, World!

Solange der String nicht einer Variablen zugewiesen wird, ignoriert MicroPython ihn beim Einlesen des Codes – damit kannst du effektiv mehrzeilige Kommentare einfügen.
