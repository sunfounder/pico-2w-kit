.. note::

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community auf Facebook! Vertiefen Sie Ihr Wissen über Raspberry Pi, Arduino und ESP32 gemeinsam mit anderen begeisterten Mitgliedern.

    **Why Join?**

    - **Expert Support**: Lösen Sie technische Herausforderungen und After-Sales-Fragen mit Unterstützung unserer Community und unseres Teams.
    - **Learn & Share**: Tauschen Sie Tipps und Tutorials aus, um Ihre Kenntnisse zu erweitern.
    - **Exclusive Previews**: Erhalten Sie frühzeitig Zugang zu Produktneuheiten und Vorschauen.
    - **Special Discounts**: Profitieren Sie von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festive Promotions and Giveaways**: Nehmen Sie an Sonderaktionen und Gewinnspielen teil.

    👉 Bereit, mit uns zu entdecken und kreativ zu werden? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

.. _cpn_74hc595:

74HC595
===========

|img_74hc595|

Der 74HC595 ist ein integrierter Schaltkreis mit einem 8-Bit-Schieberegister sowie einem Speicherregister mit tri-state Parallel-Ausgängen. Er wandelt serielle Eingangsdaten in parallele Ausgänge um und spart somit wertvolle I/O-Pins des Mikrocontrollers (MCU).

* Wenn MR (Pin 10) auf High-Pegel und OE (Pin 13) auf Low-Pegel gesetzt ist, werden Daten bei steigender Flanke von SHcp in das Schieberegister eingelesen und bei steigender Flanke von STcp in das Speicherregister übertragen.
* Werden beide Taktsignale miteinander verbunden, arbeitet das Schieberegister stets einen Taktimpuls vor dem Speicherregister.
* Das Schieberegister verfügt über einen seriellen Eingangspin (Ds), einen seriellen Ausgangspin (Q7') und einen asynchronen Reset (aktiv bei Low-Pegel).
* Das Speicherregister besitzt einen 8-Bit-Parallelbus mit drei Zuständen (tri-state).
* Wenn OE aktiviert ist (Low-Pegel), werden die im Speicherregister abgelegten Daten an den parallelen Ausgang (Q0–Q7) ausgegeben.

* `74HC595 Datasheet <https://www.ti.com/lit/ds/symlink/cd74hc595.pdf?ts=1617341564801>`_

|img_74jc595_pin|

Pins des 74HC595 und deren Funktionen:

* **Q0–Q7**: 8-Bit-Parallelausgänge, mit denen z.B. 8 LEDs oder Segmente einer 7-Segment-Anzeige direkt angesteuert werden können.
* **Q7'**: Serieller Ausgangspin, der mit dem DS-Eingang eines weiteren 74HC595 verbunden werden kann, um mehrere ICs in Reihe zu schalten.
* **MR**: Reset-Pin, aktiv bei Low-Pegel.
* **SHcp**: Takteingang des Schieberegisters. Bei steigender Flanke werden die Daten im Schieberegister jeweils um ein Bit verschoben (z.B. von Q1 nach Q2). Bei fallender Flanke bleiben die Daten unverändert.
* **STcp**: Takteingang des Speicherregisters. Bei steigender Flanke werden die Daten aus dem Schieberegister in das Speicherregister übertragen.
* **CE**: Ausgangsfreigabepin (Output Enable), aktiv bei Low-Pegel.
* **DS**: Serieller Dateneingang.
* **VCC**: Positive Versorgungsspannung.
* **GND**: Masse.

.. Example
.. -------------------

.. :ref:`Microchip - :ref:`cpn_74hc595``

**Example**

* :ref:`py_74hc_led` (Für MicroPython-Nutzer)
* :ref:`py_74hc_7seg` (Für MicroPython-Nutzer)
* :ref:`py_74hc_4dig` (Für MicroPython-Nutzer)
* :ref:`py_74hc_788bs` (Für MicroPython-Nutzer)
* :ref:`py_passage_counter` (Für MicroPython-Nutzer)
* :ref:`py_10_second` (Für MicroPython-Nutzer)
* :ref:`py_traffic_light` (Für MicroPython-Nutzer)
* :ref:`py_bubble_level` (Für MicroPython-Nutzer)
* :ref:`ar_74hc_led` (Für Arduino-Nutzer)
* :ref:`ar_74hc_7seg` (Für Arduino-Nutzer)
* :ref:`ar_74hc_4dig` (Für Arduino-Nutzer)
* :ref:`ar_74hc_788bs` (Für Arduino-Nutzer)
