.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein – zusammen mit Gleichgesinnten.

    **Why Join?**

    - **Expert Support**: Erhalte Unterstützung von unserer Community und unserem Team bei technischen Herausforderungen und Problemen nach dem Kauf.
    - **Learn & Share**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exclusive Previews**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Vorschauen.
    - **Special Discounts**: Profitiere von exklusiven Vergünstigungen auf unsere neuesten Produkte.
    - **Festive Promotions and Giveaways**: Nimm an Verlosungen und Sonderaktionen zu Feiertagen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _cpn_reed:

Reed-Schalter
======================

|img_reed|

Ein Reed-Schalter ist ein elektrischer Schalter, der auf ein angelegtes Magnetfeld reagiert. Er wurde 1936 von Walter B. Ellwood in den Bell Telephone Laboratories erfunden und am 27. Juni 1940 in den USA unter der Patentnummer 2264746 patentiert.

**Funktionsprinzip**

Der Reed-Schalter basiert auf einem einfachen Prinzip. Zwei Metallkontakte (Reed-Kontakte), meist aus Eisen und Nickel, sind in einem Glasröhrchen hermetisch verschlossen. Sie überlappen an ihren Enden, bleiben jedoch durch einen mikroskopisch kleinen Spalt getrennt. Das Glasröhrchen ist mit einem hochreinen Inertgas wie Stickstoff gefüllt oder in einigen Fällen vakuumversiegelt, um die Hochspannungseigenschaften zu verbessern.

Die Reed-Kontakte fungieren als Leiter für magnetischen Fluss. Ohne ein äußeres Magnetfeld bleiben die Kontakte getrennt. Wird ein Magnetfeld von einem Permanentmagneten oder einer elektromagnetischen Spule angelegt, entsteht an den Enden der Reed-Kontakte eine entgegengesetzte Magnetpolarität. Sobald die magnetische Anziehungskraft die natürliche Federkraft der Kontakte überwindet, schließen sich diese und der Stromkreis wird geschlossen. Verschwindet das Magnetfeld, sorgt die Eigenelastizität der Reed-Kontakte dafür, dass sie sich wieder trennen und den Stromkreis unterbrechen.

Dank dieses einfachen, aber effektiven Mechanismus ist der Reed-Schalter eine äußerst zuverlässige Lösung für Anwendungen, die eine magnetfeldgesteuerte Schaltfunktion erfordern.

|img_reed_sche|

* `Reed-Schalter - Wikipedia <https://en.wikipedia.org/wiki/Reed_switch>`_

**Example**

* :ref:`py_reed` (For MicroPython User)
* :ref:`ar_reed` (For Arduino User)