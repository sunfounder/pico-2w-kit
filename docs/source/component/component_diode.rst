.. note::

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community auf Facebook! Vertiefen Sie Ihr Wissen rund um Raspberry Pi, Arduino und ESP32 gemeinsam mit anderen begeisterten Mitgliedern.

    **Why Join?**

    - **Expert Support**: Erhalten Sie Unterstützung bei technischen Problemen und After-Sales-Fragen durch unsere Community und unser Team.
    - **Learn & Share**: Tauschen Sie Ihre Erfahrungen, Tipps und Tutorials aus und verbessern Sie Ihre Fähigkeiten.
    - **Exclusive Previews**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Vorschauen.
    - **Special Discounts**: Profitieren Sie von speziellen Rabatten auf unsere neuesten Produkte.
    - **Festive Promotions and Giveaways**: Nehmen Sie an saisonalen Aktionen und Gewinnspielen teil.

    👉 Bereit, gemeinsam mit uns Neues zu entdecken und kreativ zu werden? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

.. _cpn_diode:

Diode
=================

|img_diode|

Eine Diode ist ein elektronisches Bauteil mit zwei Anschlüssen (Elektroden), 
das den elektrischen Strom nur in einer Richtung durchlässt. Diese Eigenschaft 
wird auch als „Gleichrichterfunktion“ bezeichnet. Daher kann man sich eine 
Diode wie ein elektronisches Rückschlagventil vorstellen.

Die beiden Anschlüsse der Diode sind polarisiert: der positive Anschluss heißt 
Anode, der negative Kathode. Die Kathode ist üblicherweise mit einem silbernen 
oder farbigen Ring gekennzeichnet. Der Strom fließt in einer Diode stets von 
der Anode zur Kathode. Diese Eigenschaft ähnelt der Funktion eines Rückschlagventils. 
Ein wesentliches Merkmal der Diode ist die nichtlineare Strom-Spannungs-Kennlinie. 
Liegt die höhere Spannung an der Anode, fließt Strom (Durchlassrichtung bzw. 
Vorwärtsbetrieb). Liegt die höhere Spannung an der Kathode, sperrt die Diode und 
lässt keinen Strom durch (Sperrrichtung bzw. Rückwärtsbetrieb).

Aufgrund dieser einseitigen Leitfähigkeit wird die Diode in fast allen komplexeren elektronischen Schaltungen verwendet. Sie zählt zu den ältesten Halbleiter-Bauelementen und findet zahlreiche Anwendungen.

In der Praxis verhält sich eine Diode jedoch nicht perfekt leitend oder perfekt isolierend, sondern weist eine komplexe, nichtlineare Strom-Spannungs-Charakteristik auf, welche stark vom verwendeten Diodentyp abhängt.

Technisch gesehen besteht eine Diode aus einer p-n-Übergangsschicht, die durch das Zusammenfügen eines p-dotierten Halbleiters mit einem n-dotierten Halbleiter entsteht. An deren Grenzfläche bildet sich eine Raumladungszone mit einem internen elektrischen Feld. Ohne angelegte Spannung befinden sich Diffusionsstrom und Driftstrom im Gleichgewicht, und es fließt kein Gesamtstrom.

Wird eine Spannung in Durchlassrichtung angelegt, wird das interne elektrische Feld geschwächt, wodurch Ladungsträger über die Grenzfläche diffundieren können, und die Diode leitend wird. Bei Spannung in Sperrrichtung verstärkt sich das interne elektrische Feld, der Stromfluss wird stark eingeschränkt, und es entsteht lediglich ein kleiner, temperaturabhängiger Sperrstrom (Leckstrom). Wird die Spannung in Sperrrichtung jedoch zu groß, tritt eine elektrische Durchbruchspannung auf, wodurch der Strom plötzlich stark ansteigt und die Diode ihre Sperreigenschaft verliert.

**1. Durchlasskennlinie**

Legt man eine kleine Spannung in Durchlassrichtung an, entsteht zunächst kaum 
Stromfluss, da die Spannung zu gering ist, um die Sperrwirkung der Diode zu 
überwinden. Dieser Bereich wird als Totzone bezeichnet, die entsprechende 
Spannung als Schwellenspannung (auch Schleusenspannung). Wird diese überschritten, 
steigt der Stromfluss rasch an, wobei die Spannung über die Diode bei üblicher 
Belastung nahezu konstant bleibt. Diese Spannung bezeichnet man als Durchlassspannung.

**2. Sperrkennlinie**

Bei einer in Sperrrichtung angelegten Spannung innerhalb eines bestimmten 
Bereichs fließt nur ein sehr geringer Sperrstrom, der durch wenige bewegliche 
Ladungsträger verursacht wird. Da dieser Strom äußerst klein ist, gilt die 
Diode praktisch als gesperrt. Der Sperrstrom wird auch als Rückwärtssättigungsstrom 
oder Leckstrom bezeichnet und ist stark temperaturabhängig.

**3. Durchbruch**

Wird die Sperrspannung zu hoch, steigt der Strom abrupt an und verursacht den 
sogenannten elektrischen Durchbruch. Die zugehörige kritische Spannung heißt 
Durchbruchspannung. Ab diesem Punkt verliert die Diode ihre einseitige Leitfähigkeit. 
Aus diesem Grund sollte eine zu hohe Sperrspannung vermieden werden.

Die ersten Dioden waren sogenannte Kristalldetektoren („Cat’s Whisker“) sowie Röhrendioden („Thermionic Valves“). Heutzutage bestehen Dioden meist aus Halbleitermaterialien wie Silizium oder Germanium.

* `P–N junction - Wikipedia <https://en.wikipedia.org/wiki/P-n_junction>`_

* `Diode - Wikipedia <https://en.wikipedia.org/wiki/Diode>`_


