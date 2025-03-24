.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein und vernetze dich mit Gleichgesinnten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Löse nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Sonderrabatte**: Profitiere von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nimm an Gewinnspielen und saisonalen Promotions teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und werde noch heute Mitglied!

.. _cpn_4_dit_7_segment:

4-stelliges 7-Segment-Display
==================================

Ein 4-stelliges 7-Segment-Display besteht aus vier einzelnen 7-Segment-Anzeigen, die gemeinsam betrieben werden.

|img_4-digit-sche|

Das 4-stellige 7-Segment-Display arbeitet unabhängig und nutzt das Prinzip der visuellen Persistenz, um die einzelnen Ziffern in schneller Abfolge zu durchlaufen und so die Illusion einer durchgängigen Zeichenanzeige zu erzeugen.

Wenn beispielsweise "1234" dargestellt wird, leuchtet zunächst die erste 7-Segment-Ziffer auf und zeigt "1", während die anderen drei dunkel bleiben. Kurz darauf wird die zweite Ziffer aktiviert und zeigt "2", während die erste, dritte und vierte Ziffer ausgeschaltet sind. Dieser Vorgang wiederholt sich für alle vier Ziffern in schneller Folge (typischerweise innerhalb von 5 Millisekunden). Durch das Phänomen des optischen Nachbildes und der visuellen Persistenz nimmt das menschliche Auge alle vier Zeichen als gleichzeitig angezeigt wahr.

|img_4-digit-sche-ca| 

**Anzeige-Codes** 

Um das Funktionsprinzip von 7-Segment-Anzeigen (gemeinsame Kathode) zu verdeutlichen, haben wir die folgende Tabelle erstellt. Die Zahlen stellen die Zeichen von 0 bis F dar, die auf dem 7-Segment-Display angezeigt werden können. (DP) GFEDCBA gibt an, welche LEDs auf 0 oder 1 gesetzt sind. Zum Beispiel bedeutet der Code `00111111`, dass DP und G auf 0 gesetzt sind, während die übrigen Segmente auf 1 stehen. Dadurch wird die Zahl 0 auf dem Display dargestellt, während der HEX-Code der entsprechenden hexadezimalen Zahl entspricht.

.. list-table:: Glyph Code
    :widths: 20 20 20
    :header-rows: 1

    *   - Zahl	
        - Binärcode
        - Hexadezimalcode  
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

**Beispiele**

* :ref:`py_74hc_4dig` (Für MicroPython-Nutzer)
* :ref:`py_passage_counter` (Für MicroPython-Nutzer)
* :ref:`py_10_second` (Für MicroPython-Nutzer)
* :ref:`py_traffic_light` (Für MicroPython-Nutzer)
* :ref:`ar_74hc_4dig` (Für Arduino-Nutzer)
