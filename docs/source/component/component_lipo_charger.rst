.. note::

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community auf Facebook! Tauchen Sie gemeinsam mit anderen Enthusiasten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Why Join?**

    - **Expert Support**: Erhalten Sie Unterstützung bei technischen Fragen und Herausforderungen nach dem Kauf von unserer Community und unserem Team.
    - **Learn & Share**: Tauschen Sie Erfahrungen, Tipps und Tutorials aus, um Ihre Fähigkeiten zu erweitern.
    - **Exclusive Previews**: Erhalten Sie frühzeitigen Zugang zu Produktankündigungen und exklusiven Vorschauen.
    - **Special Discounts**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festive Promotions and Giveaways**: Nehmen Sie an saisonalen Aktionen und Gewinnspielen teil.

    👉 Sind Sie bereit, gemeinsam mit uns Neues zu entdecken und kreativ zu werden? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

.. _cpn_lipo_charger:

Li-Po Charger Module
=================================================


|lipo_module|

Dieses Li-Po-Lademodul wurde speziell für die Verwendung mit dem Raspberry Pi Pico entwickelt. Zum Einsatz stecken Sie einfach den Pico und das Modul, wie unten dargestellt, auf ein Breadboard und verbinden einen Li-Po-Akku mit dem Modul – schon ist Ihr Setup einsatzbereit.

Sobald der Pico 2 W über ein USB-Kabel mit einem Computer oder einer Stromquelle verbunden ist, leuchtet die Ladeanzeige auf dem Li-Po-Lademodul auf und signalisiert damit, dass der Akku geladen wird. Wird das USB-Kabel entfernt, wechselt der Pico 2 W automatisch in den Akkubetrieb, sodass Ihr Projekt unterbrechungsfrei weiterlaufen kann.

.. note::
    Bei manchen Computern kann es vorkommen, dass der Pico 2 W nicht erkannt wird, wenn gleichzeitig das 
    Li-Po-Modul mit angeschlossenem Akku verwendet wird. Grund hierfür ist, dass die USB-Spannung während des Ladevorgangs leicht absinken kann und der Pico dadurch nicht ausreichend mit Strom versorgt wird, um vom Computer erkannt zu werden.

    In diesem Fall entfernen Sie zunächst das Li-Po-Lademodul und verbinden dann den Pico 2 W erneut mit dem Computer.

|lipo_wire|

**Features**

* Eingangsspannung: 5 V
* Ausgangsspannung: 3,3 V
* Größe: 20 mm x 7 mm
* Schnittstellenmodell: PH2.0


**Schematic**

|sch_lipo_charger|