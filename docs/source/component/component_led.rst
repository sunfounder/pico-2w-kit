.. note:: 

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community auf Facebook! Tauchen Sie gemeinsam mit anderen Enthusiasten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Why Join?**

    - **Expert Support**: Unterstützung bei technischen Herausforderungen und Fragen nach dem Kauf durch unsere Community und unser Team.
    - **Learn & Share**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu erweitern.
    - **Exclusive Previews**: Erhalten Sie frühzeitigen Zugang zu Produktneuheiten und exklusive Einblicke.
    - **Special Discounts**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festive Promotions and Giveaways**: Nehmen Sie an Gewinnspielen und saisonalen Aktionen teil.

    👉 Bereit, mit uns gemeinsam Neues zu entdecken und kreativ zu werden? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

.. _cpn_led:

LED
==========

|img_led|

Eine Leuchtdiode (LED) ist ein Halbleiter-Bauelement, das elektrische Energie über einen PN-Übergang in Lichtenergie umwandelt. Je nach Wellenlänge lassen sich LEDs in Laserdioden, Infrarot-LEDs und sichtbare LEDs einteilen.

Aufgrund ihrer unidirektionalen Leitfähigkeit fließt Strom in der Diode in Pfeilrichtung ihres Schaltsymbols. Um eine LED zu betreiben, muss die Anode an eine positive Spannungsquelle und die Kathode an den negativen Anschluss angeschlossen werden, sodass die LED Licht abstrahlt.

|img_led_symbol|

Eine LED hat zwei Anschlüsse. Der längere Anschlussdraht ist die Anode, der kürzere die Kathode. Achten Sie darauf, diese nicht zu verwechseln. Da an einer LED eine bestimmte Durchlassspannung abfällt, darf sie nicht direkt an eine Stromversorgung angeschlossen werden, da sie sonst beschädigt wird. Die Durchlassspannung einer roten, gelben oder grünen LED beträgt etwa 1,8 V, während sie bei einer weißen LED ungefähr 2,6 V beträgt. Die meisten LEDs vertragen maximal 20 mA Strom. Daher ist es notwendig, einen Vorwiderstand in Reihe zu schalten.

Die Formel zur Berechnung des erforderlichen Widerstandswerts lautet:

    R = (Vsupply – VD)/I

Dabei steht **R** für den Wert des Vorwiderstandes, **Vsupply** für die Versorgungsspannung, **VD** für die Durchlassspannung der LED und **I** für den Betriebsstrom.

Ausführlichere Informationen zur LED finden Sie hier: `LED - Wikipedia <https://en.wikipedia.org/wiki/Leuchtdiode>`_.

.. **Example**

.. * :ref:`Hello, Breadboard!` (For MicroPython User)
.. * :ref:`fading_led_micropython` (For MicroPython User)
.. * :ref:`fading_led_arduino` (For C/C++(Arduino) User)
.. * :ref:`hello_led_arduino` (For C/C++(Arduino) User)


**Example**

* :ref:`py_led` (For MicroPython User)
* :ref:`py_fade` (For MicroPython User)
* :ref:`py_alarm_lamp` (For MicroPython User)
* :ref:`py_traffic_light` (For MicroPython User)
* :ref:`py_reversing_aid` (For MicroPython User)
* :ref:`py_iot_read_ble` (For MicroPython User)
* :ref:`py_iot_ble_relay` (For MicroPython User)
* :ref:`ar_led` (For Arduino User)
* :ref:`ar_fade` (For Arduino User)
.. * :ref:`per_blink` (For Piper Make User)
.. * :ref:`per_button` (For Piper Make User)
.. * :ref:`per_service_bell` (For Piper Make User)
.. * :ref:`per_reversing_system` (For Piper Make User)
.. * :ref:`per_reaction_game` (For Piper Make User)