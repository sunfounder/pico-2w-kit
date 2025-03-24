.. note::

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community auf Facebook! Tauchen Sie gemeinsam mit anderen begeisterten Mitgliedern tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Why Join?**

    - **Expert Support**: Erhalten Sie Unterstützung bei technischen Fragen und Problemen nach dem Kauf durch unsere Community und unser Team.
    - **Learn & Share**: Teilen Sie Tipps, Tutorials und Erfahrungen, um Ihre Kenntnisse zu erweitern.
    - **Exclusive Previews**: Sichern Sie sich vorzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Special Discounts**: Nutzen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festive Promotions and Giveaways**: Nehmen Sie an Gewinnspielen und besonderen Aktionen teil.

    👉 Bereit, mit uns gemeinsam Neues zu entdecken und kreativ zu werden? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

.. _cpn_buzzer:

Buzzer
=======


Buzzer sind elektronische Bauelemente mit integrierter Struktur, die üblicherweise mit Gleichstrom (DC) betrieben werden. Sie kommen in vielen Geräten zum Einsatz, darunter Computer, Drucker, Kopierer, Alarme, elektronisches Spielzeug, Fahrzeugelektronik, Telefone, Timer und andere elektronische Produkte oder Audiosignaleinrichtungen.

Grundsätzlich unterscheidet man zwei Typen von Buzzern: aktive und passive Buzzer (siehe Abbildung unten). Um den Typ zu bestimmen, drehen Sie den Buzzer so, dass die Pins nach oben zeigen. Ein passiver Buzzer besitzt eine grüne Platine, während ein aktiver Buzzer typischerweise mit schwarzem Klebeband umhüllt ist.

|img_buzzer|

Unterschied zwischen aktivem und passivem Buzzer:

Ein aktiver Buzzer verfügt über eine integrierte Oszillatorschaltung, die bereits beim Anlegen einer Gleichspannung einen Ton erzeugt. Im Gegensatz dazu besitzt ein passiver Buzzer keinen eingebauten Oszillator und erzeugt daher bei Anlegen einer reinen Gleichspannung keinen Ton. Um einen Ton zu erzeugen, muss ein passiver Buzzer mit einem Rechtecksignal zwischen 2 kHz und 5 kHz angesteuert werden. Aufgrund der zusätzlichen internen Schaltung sind aktive Buzzer in der Regel teurer als passive Modelle.

Das folgende Symbol zeigt das Schaltzeichen eines Buzzers. Es verfügt über zwei Pins: eine Anode (positiver Pol), die mit „+“ markiert ist, und eine Kathode (negativer Pol).

|img_buzzer_symbol|

Um die Pins des Buzzers korrekt zu identifizieren, achten Sie darauf, dass der längere Pin die Anode und der kürzere Pin die Kathode ist. Vertauschen Sie die Anschlüsse nicht, da der Buzzer ansonsten keinen Ton erzeugt.

Weitere Informationen: `Buzzer – Wikipedia <https://en.wikipedia.org/wiki/Buzzer>`_

.. Example
.. -------------------

.. :ref:`Intruder Alarm`

.. :ref:`Custom Tone`

**Example**

* :ref:`py_ac_buz` (Für MicroPython-Nutzer)
* :ref:`py_pa_buz` (Für MicroPython-Nutzer)
* :ref:`py_light_theremin` (Für MicroPython-Nutzer)
* :ref:`py_alarm_lamp` (Für MicroPython-Nutzer)
* :ref:`py_music_player` (Für MicroPython-Nutzer)
* :ref:`py_fruit_piano` (Für MicroPython-Nutzer)
* :ref:`py_reversing_aid` (Für MicroPython-Nutzer)
* :ref:`py_iot_mqtt_subscribe` (Für MicroPython-Nutzer)
* :ref:`py_iot_ble_piano` (Für MicroPython-Nutzer)
* :ref:`ar_ac_buz` (Für Arduino-Nutzer)
* :ref:`ar_pa_buz` (Für Arduino-Nutzer)
.. * :ref:`per_service_bell` (Für Piper Make-Nutzer)
.. * :ref:`per_reversing_system` (Für Piper Make-Nutzer)
.. * :ref:`per_reaction_game` (Für Piper Make-Nutzer)
