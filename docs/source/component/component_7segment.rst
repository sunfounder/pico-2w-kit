.. note::

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community auf Facebook! Tauschen Sie sich mit Gleichgesinnten aus und vertiefen Sie Ihr Wissen zu Raspberry Pi, Arduino und ESP32.

    **Why Join?**

    - **Expert Support**: Unterstützung bei technischen Herausforderungen und After-Sales-Fragen durch Community-Mitglieder und unser Team.
    - **Learn & Share**: Teilen Sie Tipps und Tutorials und erweitern Sie Ihre Fähigkeiten.
    - **Exclusive Previews**: Erhalten Sie vorab Einblicke und Ankündigungen neuer Produkte.
    - **Special Discounts**: Profitieren Sie von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festive Promotions and Giveaways**: Nehmen Sie an besonderen Aktionen und Gewinnspielen teil.

    👉 Bereit, mit uns zu entdecken und kreativ zu werden? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

.. _cpn_7_segment:

7-Segment-Anzeige
======================

|img_7seg|


Eine 7-Segment-Anzeige ist eine Komponente in Form einer Acht, die aus 7 LEDs besteht, wobei jede LED als Segment bezeichnet wird. Wird ein Segment mit Strom versorgt, leuchtet es auf und stellt somit einen Teil einer Ziffer dar.

Es gibt zwei Typen von Pin-Konfigurationen: Common Cathode (gemeinsame Kathode, CC) und Common Anode (gemeinsame Anode, CA). Wie die Namen bereits andeuten, verbindet ein CC-Display die Kathoden aller sieben LEDs miteinander, während bei einem CA-Display alle Anoden der sieben Segmente verbunden sind.

In diesem Kit verwenden wir eine 7-Segment-Anzeige mit gemeinsamer Kathode. Nachfolgend sehen Sie das zugehörige Schaltsymbol:

|img_7seg_cathode|

Jede LED innerhalb der Anzeige ist einem Segment zugeordnet, und einer ihrer Anschlusspins wird aus dem rechteckigen Kunststoffgehäuse herausgeführt. Diese Pins sind mit Buchstaben von „a“ bis „g“ bezeichnet, um das jeweilige Segment eindeutig zu kennzeichnen. Die übrigen LED-Pins sind intern miteinander verbunden und bilden einen gemeinsamen Pin. Durch gezieltes Ansteuern einzelner Segmente (Vorwärtsspannung anlegen) können bestimmte Segmente aufleuchten, während andere dunkel bleiben, wodurch das gewünschte Zeichen auf der Anzeige dargestellt wird.

* `Seven-segment Display - Wikipedia <https://en.wikipedia.org/wiki/Seven-segment_display>`_

**Display Codes**

Damit Sie nachvollziehen können, wie eine 7-Segment-Anzeige (Common Cathode) Ziffern darstellt, haben wir die folgende Tabelle erstellt. Die Ziffern von 0 bis F werden jeweils durch ein Binärmuster (DP) GFEDCBA repräsentiert, wobei jedes Bit angibt, ob die entsprechende LED ein- (1) oder ausgeschaltet (0) ist. Beispielsweise bedeutet 00111111, dass DP und G ausgeschaltet (0) sind, während alle anderen LEDs eingeschaltet (1) sind. So wird die Ziffer 0 auf der 7-Segment-Anzeige dargestellt. Der HEX-Code entspricht der Hexadezimaldarstellung dieses Binärmusters.

.. list-table:: Glyph Code
    :widths: 20 20 20
    :header-rows: 1

    *   - Numbers	
        - Binary Code
        - Hex Code  
    *   - 0	
        - 00111111	
        - 0x3f
    *   - 1	
        - 00000110	
        - 0x06
    *   - 2	
        - 01011011	
        - 0x5b
    *   - 3	
        - 01001111	
        - 0x4f
    *   - 4	
        - 01100110	
        - 0x66
    *   - 5	
        - 01101101	
        - 0x6d
    *   - 6	
        - 01111101	
        - 0x7d
    *   - 7	
        - 00000111	
        - 0x07
    *   - 8	
        - 01111111	
        - 0x7f
    *   - 9	
        - 01101111	
        - 0x6f
    *   - A	
        - 01110111	
        - 0x77
    *   - B
        - 01111100	
        - 0x7c
    *   - C	
        - 00111001	
        - 0x39
    *   - D	
        - 01011110	
        - 0x5e
    *   - E	
        - 01111001	
        - 0x79
    *   - F	
        - 01110001	
        - 0x71

.. Example
.. -------------------

.. :ref:`LED Segment Display`

**Example**

* :ref:`py_74hc_7seg` (Für MicroPython-Nutzer)
* :ref:`ar_74hc_7seg` (Für Arduino-Nutzer)
