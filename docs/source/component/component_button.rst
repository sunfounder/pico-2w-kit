.. note::

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community auf Facebook! Vertiefen Sie gemeinsam mit anderen begeisterten Mitgliedern Ihr Wissen rund um Raspberry Pi, Arduino und ESP32.

    **Why Join?**

    - **Expert Support**: Erhalten Sie Unterstützung bei technischen Herausforderungen und Fragen nach dem Kauf durch unsere Community und unser Team.
    - **Learn & Share**: Teilen Sie Ihre Erfahrungen, tauschen Sie Tipps und Tutorials aus und verbessern Sie Ihre Fähigkeiten.
    - **Exclusive Previews**: Erhalten Sie frühzeitig Zugriff auf neue Produktankündigungen und exklusive Einblicke.
    - **Special Discounts**: Profitieren Sie von speziellen Rabatten auf unsere neuesten Produkte.
    - **Festive Promotions and Giveaways**: Nehmen Sie an saisonalen Aktionen und Gewinnspielen teil.

    👉 Bereit, mit uns Neues zu entdecken und kreativ zu werden? Klicken Sie auf [|link_sf_facebook|] und werden Sie noch heute Mitglied!

.. _cpn_button:

Button
==========

|img_button|

Buttons (auch Taster genannt) sind häufig eingesetzte Bauelemente zur Steuerung elektronischer Geräte und dienen typischerweise dazu, Stromkreise zu öffnen oder zu schließen. Sie sind in unterschiedlichen Größen und Formen erhältlich; in diesem Kit wird ein 6-mm-Mini-Drucktaster verwendet, wie unten dargestellt.

Innerhalb dieses Tasters sind Pin 1 und Pin 2 miteinander verbunden, ebenso Pin 3 und Pin 4. Um einen Stromkreis zu schließen, genügt es daher, entweder Pin 1 oder Pin 2 mit Pin 3 oder Pin 4 zu verbinden.

Die folgende Abbildung zeigt die interne Struktur eines Tasters. Das rechts abgebildete Symbol wird üblicherweise zur Darstellung eines Buttons in Schaltplänen verwendet.

|img_button_symbol|

Da Pin 1 mit Pin 2 und Pin 3 mit Pin 4 verbunden ist, werden beim Drücken des Tasters alle vier Pins miteinander verbunden und der Stromkreis geschlossen.

|img_button2|

.. Examples
.. -------------------

.. :ref:`Reading Button Value`

**Example**

* :ref:`py_button` (Für MicroPython-Nutzer)
* :ref:`py_iot_mqtt_publish` (Für MicroPython-Nutzer)
* :ref:`ar_button` (Für Arduino-Nutzer)
.. * :ref:`per_button` (Für Piper Make-Nutzer)
.. * :ref:`per_rainbow_light` (Für Piper Make-Nutzer)
.. * :ref:`per_drum_kit` (Für Piper Make-Nutzer)
.. * :ref:`per_reaction_game` (Für Piper Make-Nutzer)
