.. note::
   Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein zusammen mit anderen Begeisterten.

   **Warum beitreten?**

   - **Expertenunterstützung**: Löse Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
   - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um deine Fähigkeiten zu verbessern.
   - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
   - **Sonderangebote**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
   - **Festliche Aktionen und Verlosungen**: Nimm an Verlosungen und Feiertagsaktionen teil.

   👉 Bereit, mit uns zu erkunden und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt heute bei!

Print()
=====================

Die Funktion ``print()`` gibt die angegebene Nachricht auf dem Bildschirm oder einem anderen Standardausgabegerät aus.
Die Nachricht kann eine Zeichenkette oder ein anderes Objekt sein; das Objekt wird vor der Ausgabe in eine Zeichenkette umgewandelt.



Mehrere Objekte ausgeben:

.. code-block:: python

    print("Welcome!", "Enjoy yourself!")

>>> %Run -c $EDITOR_CONTENT
Welcome! Enjoy yourself!

Print tuples:



.. code-block:: python

    x = ("pear", "apple", "grape")
    print(x)

>>> %Run -c $EDITOR_CONTENT
('pear', 'apple', 'grape')


Zwei Nachrichten ausgeben und Trennzeichen angeben:

.. code-block:: python

    print("Hello", "how are you?", sep="---")

>>> %Run -c $EDITOR_CONTENT
Hello---how are you?