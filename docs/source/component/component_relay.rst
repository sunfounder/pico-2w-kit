.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein – zusammen mit Gleichgesinnten.

    **Why Join?**

    - **Expert Support**: Löse Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Learn & Share**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exclusive Previews**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Vorschauen.
    - **Special Discounts**: Profitiere von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festive Promotions and Giveaways**: Nimm an Gewinnspielen und Sonderaktionen zu Feiertagen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _cpn_relay:

Relais
==========================================

|img_relay|

Ein Relais ist ein Bauteil, das zwei oder mehr Punkte oder Geräte in Abhängigkeit von einem Eingangssignal verbindet. Im Wesentlichen dient es als Isolator zwischen dem Steuergerät und dem Verbraucher, da dieser mit Wechselstrom (AC) oder Gleichstrom (DC) betrieben werden kann. Relais sind notwendig, weil Mikrocontroller, die in der Regel mit Gleichstrom arbeiten, eine Schnittstelle benötigen, um Geräte mit unterschiedlichen elektrischen Standards zu steuern.

Relais sind besonders nützlich, um große Ströme oder Spannungen mit kleinen elektrischen Signalen zu schalten, was sie für zahlreiche Anwendungen unverzichtbar macht.

Jedes Relais besteht aus fünf Hauptkomponenten:

**Elektromagnet** – Ein Eisenkern, der mit einer Drahtspule umwickelt ist. Fließt Strom durch die Spule, entsteht ein Magnetfeld, das den Kern in einen Elektromagneten verwandelt.

**Anker** – Der bewegliche Metallstreifen, der auf das Magnetfeld der Spule reagiert. Wird der Elektromagnet aktiviert, zieht er den Anker an, wodurch eine Verbindung an den normalerweise offenen (N/O) oder normalerweise geschlossenen (N/C) Kontaktpunkten hergestellt oder unterbrochen wird. Der Anker kann sowohl mit Gleich- als auch mit Wechselstrom betrieben werden.

**Feder** – Wenn kein Strom durch die Spule fließt, zieht die Feder den Anker zurück und hält den Stromkreis offen.

**Kontaktpaar** – Bestehend aus zwei Schaltpunkten:

- Normally Open (N/O) – Der Kontakt ist im Ruhezustand offen und schließt sich, wenn das Relais aktiviert wird.
- Normally Closed (N/C) – Der Kontakt ist im Ruhezustand geschlossen und öffnet sich, wenn das Relais aktiviert wird.

**Gehäuse** – Das Relais ist durch ein Kunststoffgehäuse geschützt.

Das Funktionsprinzip eines Relais ist einfach: Wird das Relais mit Strom versorgt, fließt ein Strom durch die Steuerspule und aktiviert den Elektromagneten. Dadurch wird der Anker angezogen und der bewegliche Kontakt schließt den normalerweise offenen (N/O) Kontakt, sodass der Laststromkreis aktiviert wird.

Zum Abschalten wird die Stromversorgung entfernt. Die Feder zieht den beweglichen Kontakt in seine ursprüngliche Position zurück, wodurch sich der normalerweise geschlossene (N/C) Kontakt wieder verbindet und der Stromkreis unterbrochen wird. Diese Umschaltfunktion ermöglicht eine effiziente Steuerung des Laststromkreises.

|img_relay_sche|


* `Relay - Wikipedia <https://en.wikipedia.org/wiki/Relay>`_

**Example**

* :ref:`py_relay` (Für MicroPython User)
* :ref:`py_iot_ble_relay` (Für MicroPython User)
* :ref:`ar_relay` (Für Arduino User)
