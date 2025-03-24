.. note::

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community auf Facebook! Erkunden Sie gemeinsam mit anderen begeisterten Mitgliedern die vielfältigen Möglichkeiten rund um Raspberry Pi, Arduino und ESP32.

    **Why Join?**

    - **Expert Support**: Erhalten Sie Unterstützung bei technischen Herausforderungen und Fragen nach dem Kauf durch unsere Community und unser Team.
    - **Learn & Share**: Teilen Sie Ihre Erfahrungen und tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten weiter auszubauen.
    - **Exclusive Previews**: Erhalten Sie exklusive Vorabinformationen zu Produktneuheiten und Vorschauen.
    - **Special Discounts**: Profitieren Sie von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festive Promotions and Giveaways**: Nehmen Sie an Gewinnspielen und saisonalen Aktionen teil.

    👉 Bereit, gemeinsam mit uns Neues zu entdecken und kreativ zu werden? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

.. _cpn_motor:

DC Motor
===================

|img_dc_motor|

Dies ist ein 3-V-Gleichstrommotor (DC-Motor). Er dreht sich, sobald an einem seiner Anschlüsse eine höhere Spannung (High) und am anderen eine niedrigere Spannung (Low) anliegt.

* **Size**: 25 × 20 × 15 mm
* **Operation Voltage**: 1–6 V
* **Free-run Current** (3 V): 70 mA
* **Free-run Speed** (3 V): 13.000 U/min
* **Stall Current** (3 V): 800 mA
* **Shaft Diameter**: 2 mm

Ein Gleichstrommotor ist ein Aktor, der kontinuierlich elektrische Energie in mechanische Bewegung umwandelt. 
DC-Motoren treiben Pumpen, Lüfter, Kompressoren, Rotoren und andere Geräte an, indem sie eine fortlaufende Drehbewegung erzeugen.

Ein DC-Motor besteht im Wesentlichen aus zwei Teilen: dem feststehenden äußeren Teil (**stator**) und dem 
drehbaren inneren Teil (**rotor** oder **armature**). Entscheidend für die Drehbewegung ist, dass sich der 
Rotor im Magnetfeld eines Dauermagneten befindet, dessen Feldlinien vom Nord- zum Südpol verlaufen. 
Durch das Zusammenwirken des Magnetfeldes mit den bewegten elektrischen Ladungen im stromführenden 
Rotor entsteht ein Drehmoment, das den Rotor in Bewegung versetzt.

|img_dc_motor_sche|

Der elektrische Strom fließt vom Pluspol der Batterie durch die 
Kupferbürsten und den Kommutator in den Rotor (Anker). 
Da der Kommutator zwei isolierende Zwischenräume besitzt, kehrt 
sich der Stromfluss nach jeder halben Umdrehung um. Diese ständige 
Umpolung bewirkt, dass der Rotor immer in dieselbe Richtung gedreht 
wird und die Drehbewegung kontinuierlich bleibt.

* `DC Motor - MagLab <https://nationalmaglab.org/education/magnet-academy/watch-play/interactive/dc-motor>`_
* `Fleming's left-hand rule for motors - Wikipedia <https://en.wikipedia.org/wiki/Fleming%27s_left-hand_rule_for_motors>`_



**Example**

* :ref:`py_motor` (Für MicroPython-Nutzer)
* :ref:`ar_motor` (Für Arduino-Nutzer)
.. * :ref:`per_smart_fan` (Für Piper Make-Nutzer)
