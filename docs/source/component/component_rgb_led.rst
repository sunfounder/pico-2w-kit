.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein – zusammen mit Gleichgesinnten.

    **Why Join?**

    - **Expert Support**: Erhalte Unterstützung von unserer Community und unserem Team bei technischen Herausforderungen und Problemen nach dem Kauf.
    - **Learn & Share**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exclusive Previews**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Vorschauen.
    - **Special Discounts**: Profitiere von exklusiven Vergünstigungen auf unsere neuesten Produkte.
    - **Festive Promotions and Giveaways**: Nimm an Gewinnspielen und Sonderaktionen zu Feiertagen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _cpn_rgb:

RGB-LED
=================

|img_rgb|
    
RGB-LEDs können Licht in einer Vielzahl von Farben erzeugen. Jede RGB-LED kombiniert drei einzelne LEDs – Rot, Grün und Blau – in einem transparenten oder halbtransparenten Kunststoffgehäuse. Durch Anpassen der Eingangsspannung an den drei Pins entstehen durch Farbmischung unterschiedliche Farben. Tatsächlich kann eine RGB-LED auf diese Weise bis zu 16.777.216 verschiedene Farbkombinationen erzeugen.

|img_rgb_light|

RGB-LEDs werden in zwei Typen unterteilt: gemeinsame Anode (Common Anode) und gemeinsame Kathode (Common Cathode). In diesem Kit wird die **gemeinsame Kathode** (CC) verwendet. Dies bedeutet, dass die Kathoden der drei LEDs miteinander verbunden sind. Wenn die gemeinsame Kathode mit GND verbunden ist und die anderen Pins angesteuert werden, leuchtet die LED in der jeweiligen Farbe.

Das Schaltsymbol einer RGB-LED ist in der folgenden Abbildung dargestellt.

|img_rgb_symbol| 

Eine RGB-LED verfügt über 4 Pins:  Der längste Pin ist die gemeinsame Kathode, die normalerweise mit GND verbunden wird.  
Der Pin links neben dem längsten ist für Rot, die beiden Pins rechts davon steuern Grün und Blau.

|img_rgb_pin|


**Eigenschaften**

* Farbe: Drei-Farb-LED (Rot/Grün/Blau)
* Gemeinsame Kathode
* 5 mm klares rundes Gehäuse
* Vorwärtsspannung: Rot: DC 2,0 - 2,2V; Blau & Grün: DC 3,0 - 3,2V (IF=20mA)
* 0,06 Watt DIP-RGB-LED
* Bis zu 20 % höhere Leuchtkraft
* Abstrahlwinkel: 30°


.. Example
.. -------------------

.. :ref:`Colorful Light`


**Example**

* :ref:`py_rgb` (Für MicroPython-Nutzer)
* :ref:`py_fruit_piano` (Für MicroPython-Nutzer)
* :ref:`py_iot_web_server` (Für MicroPython-Nutzer)
* :ref:`ar_rgb` (Für Arduino-Nutzer)
.. * :ref:`per_rainbow_light` (Für Piper Make-Nutzer)
