.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein – zusammen mit Gleichgesinnten.

    **Why Join?**

    - **Expert Support**: Löse Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Learn & Share**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exclusive Previews**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Vorschauen.
    - **Special Discounts**: Profitiere von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festive Promotions and Giveaways**: Nimm an Gewinnspielen und Sonderaktionen zu Feiertagen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _cpn_tilt:

Neigungsschalter
=============================

|img_tilt| 

Der hier verwendete Neigungsschalter ist ein Kugelschalter, der eine Metallkugel im Inneren enthält. Er ist speziell dafür ausgelegt, kleine Neigungswinkel zu erkennen.

**Funktionsprinzip**

Die Funktionsweise des Neigungsschalters ist einfach:

- Wird der Schalter um einen bestimmten Winkel geneigt, rollt die Metallkugel im Inneren und stellt eine Verbindung zwischen zwei Anschlüssen her. Dadurch wird der Stromkreis geschlossen und das angeschlossene System ausgelöst.
- Ist der Schalter nicht geneigt, bleibt die Kugel von den Kontakten entfernt, wodurch der Stromkreis unterbrochen und inaktiv bleibt.

Dieses einfache, aber effektive Mechanismus macht den Neigungsschalter ideal für die Erkennung von Änderungen in der Orientierung oder Neigung.

|img_tilt_symbol|

* `SW520D Tilt Switch Datasheet <https://www.tme.com/Document/f1e6cedd8cb7feeb250b353b6213ec6c/SW-520D.pdf>`_

.. * :ref:`Reading Button Value`


**Example**

* :ref:`py_tilt` (Für MicroPython-Nutzer)
* :ref:`py_10_second` (Für MicroPython-Nutzer)
* :ref:`ar_tilt` (Für Arduino-Nutzer)

.. * :ref:`per_flowing_leds` (Für Piper Make-Nutzer)
