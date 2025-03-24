.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein – zusammen mit Gleichgesinnten.

    **Why Join?**

    - **Expert Support**: Löse Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Learn & Share**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exclusive Previews**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Vorschauen.
    - **Special Discounts**: Profitiere von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festive Promotions and Giveaways**: Nimm an Gewinnspielen und Sonderaktionen zu Feiertagen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _cpn_transistor:

Transistor
============

|img_NPN&PNP|

Ein Transistor ist ein Halbleiterbauelement, das Strom durch Strom steuert.  
Er verstärkt schwache Signale zu stärkeren Signalen und wird auch als kontaktloser Schalter verwendet.

Ein Transistor besteht aus einer dreischichtigen Struktur aus P- und N-dotierten Halbleitern, die drei interne Regionen bilden.  
Die mittlere, dünnere Region ist die Basis, während die beiden äußeren Regionen entweder N- oder P-dotiert sind.  
Die kleinere Region mit der höheren Konzentration an Ladungsträgern ist der Emitter, während die andere der Kollektor ist.  
Diese Anordnung ermöglicht es dem Transistor, als Verstärker zu funktionieren.  

Aus diesen drei Regionen entstehen die Anschlüsse: Basis (b), Emitter (e) und Kollektor (c).  
Sie bilden zwei P-N-Übergänge: den Emitterübergang und den Kollektorübergang.  
Die Pfeilrichtung im Schaltzeichen des Transistors zeigt die Richtung des Emitterübergangs an.

* `P–N junction - Wikipedia <https://en.wikipedia.org/wiki/P-n_junction>`_

Je nach Halbleitertyp werden Transistoren in zwei Gruppen unterteilt: NPN- und PNP-Transistoren.  
Aus der Abkürzung lässt sich ableiten, dass ein NPN-Transistor aus zwei N-dotierten und einer P-dotierten  
Schicht besteht, während es beim PNP-Transistor genau umgekehrt ist. Siehe Abbildung unten.

.. note::
    Der S8550 ist ein PNP-Transistor und der S8050 ein NPN-Transistor.  
    Da sie sich optisch sehr ähneln, ist es wichtig, ihre Bezeichnung sorgfältig zu überprüfen.

|img_transistor_symbol|

Wenn ein High-Pegel-Signal durch einen NPN-Transistor fließt, wird dieser aktiviert.  
Ein PNP-Transistor hingegen benötigt ein Low-Pegel-Signal, um zu schalten.  
Beide Transistortypen werden häufig als kontaktlose Schalter verwendet – so auch in diesem Experiment.

* `S8050 Transistor Datasheet <https://components101.com/asset/sites/default/files/component_datasheet/S8050%20Transistor%20Datasheet.pdf>`_
* `S8550 Transistor Datasheet <https://www.mouser.com/datasheet/2/149/SS8550-118608.pdf>`_

Wenn die beschriftete Seite des Transistors zu uns zeigt und die Anschlüsse nach unten zeigen,  
sind die Pins von links nach rechts wie folgt angeordnet: Emitter (e), Basis (b) und Kollektor (c).

|img_ebc|

.. note::
    * Die Basis ist die Steuerung für die größere Stromversorgung.  
    * Beim NPN-Transistor ist der Kollektor die größere Stromquelle und der Emitter der Ausgang für diesen Strom. Beim PNP-Transistor verhält es sich genau umgekehrt.

.. Example
.. -------------------

.. :ref:`Two Kinds of Transistors`


**Example**

* :ref:`py_transistor` (Für MicroPython-Nutzer)
* :ref:`py_relay` (Für MicroPython-Nutzer)
* :ref:`py_ac_buz` (Für MicroPython-Nutzer)
* :ref:`py_pa_buz` (Für MicroPython-Nutzer)
* :ref:`py_light_theremin` (Für MicroPython-Nutzer)
* :ref:`py_alarm_lamp` (Für MicroPython-Nutzer)
* :ref:`py_music_player` (Für MicroPython-Nutzer)
* :ref:`py_fruit_piano` (Für MicroPython-Nutzer)
* :ref:`py_reversing_aid` (Für MicroPython-Nutzer)
* :ref:`ar_ac_buz` (Für Arduino-Nutzer)
* :ref:`ar_pa_buz` (Für Arduino-Nutzer)
* :ref:`ar_transistor` (Für Arduino-Nutzer)
* :ref:`ar_relay` (Für Arduino-Nutzer)
.. * :ref:`per_service_bell` (Für Piper Make-Nutzer)
.. * :ref:`per_reversing_system` (Für Piper Make-Nutzer)
.. * :ref:`per_reaction_game` (Für Piper Make-Nutzer)
