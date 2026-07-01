.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Vertiefe dich in Raspberry Pi, Arduino und ESP32 zusammen mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Löse Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Promotionen und Gewinnspiele**: Nimm an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicke auf [|link_sf_facebook|] und trete heute bei!

Elektronische Schaltungen
============================

Viele alltägliche Geräte, wie die Beleuchtung in deinem Zuhause oder der Computer, auf dem du dies liest, werden durch Elektrizität angetrieben.

Um Elektrizität zu nutzen, muss ein elektrischer Stromkreis erstellt werden. Ein elektrischer Stromkreis besteht aus Metallleitern und elektrischen sowie elektronischen Komponenten.

Stromkreise benötigen eine Stromquelle. In deinem Zuhause werden die meisten Geräte (z.B. Fernseher, Lichter) durch Steckdosen mit Strom versorgt. Viele kleinere, tragbare Schaltkreise (z.B. elektronisches Spielzeug, Handys) werden jedoch durch ein Power Pack betrieben. Ein Power Pack hat zwei Pole, wovon einer als positiver Pol bezeichnet und mit einem Pluszeichen (+) markiert ist. Negative Pole werden durch Minuszeichen (-) symbolisiert, sind aber meist nicht auf dem Power Pack gedruckt.

Damit Strom fließen kann, muss ein leitfähiger Pfad den positiven Pol des Power Pack mit dem negativen Pol verbinden, was als geschlossener Stromkreis bezeichnet wird (wird er getrennt, spricht man von einem offenen Stromkreis). Der elektrische Strom fließt dann durch Geräte wie Lampen, um sie zu betreiben (z.B. zum Leuchten zu bringen).

|bc1|


Ein Pico 2 W verfügt über einige Stromausgangspins (positiv) und einige Erdungspins (negativ).
Diese Pins kannst du als positive und negative Seiten der Stromversorgung nutzen, indem du den Pico 2 W an eine Stromquelle anschließt.

|bc2| 

Mit Elektrizität kannst du Werke mit Licht, Ton und Bewegung erschaffen.
Du kannst eine LED zum Leuchten bringen, indem du den längeren Pin an den positiven Pol und den kürzeren Pin an den negativen Pol anschließt.
Die LED wird sehr schnell kaputtgehen, wenn du dies tust, daher musst du einen 220* Widerstand in den Stromkreis einbauen, um sie zu schützen.

Der Stromkreis, den sie bilden, ist unten dargestellt.

|bc2.5| 

Vielleicht fragst du dich jetzt: Wie baue ich diesen Stromkreis auf? Halte ich die Drähte mit der Hand, oder klebe ich die Pins und Drähte?

In dieser Situation werden steckbare Breadboards deine stärksten Verbündeten sein.

.. _bc_bb:

Hallo, Breadboard!
------------------------------

Ein Breadboard ist eine rechteckige Kunststoffplatte mit vielen kleinen Löchern.
Diese Löcher ermöglichen es uns, elektronische Komponenten leicht einzusetzen und elektronische Schaltungen zu bauen.
Breadboards fixieren elektronische Komponenten nicht dauerhaft, sodass wir einen Schaltkreis leicht reparieren und neu beginnen können, wenn etwas schiefgeht.

.. note::
    Für die Verwendung von Breadboards sind keine speziellen Werkzeuge erforderlich. Allerdings sind viele elektronische Komponenten sehr klein, und eine Pinzette kann uns helfen, kleine Teile besser aufzuheben.

Im Internet können wir viele Informationen über Breadboards finden.

* `How to Use a Breadboard - Science Buddies <https://www.sciencebuddies.org/science-fair-projects/references/how-to-use-a-breadboard#pth-smd>`_

* `What is a BREADBOARD? - Makezine <https://cdn.makezine.com/uploads/2012/10/breadboardworkshop.pdf>`_


Hier sind einige Dinge, die du über Breadboards wissen solltest.

#. Jede Halbreihe (z. B. Spalte A-E in Reihe 1 oder Spalte F-J in Reihe 3) ist verbunden. Daher kann, wenn ein elektrisches Signal von A1 eingeht, es von B1, C1, D1, E1 ausgehen, aber nicht von F1 oder A2.

#. In den meisten Fällen werden beide Seiten des Breadboards als Stromschienen verwendet, und die Löcher in jeder Spalte (etwa 50 Löcher) sind miteinander verbunden. In der Regel werden positive Stromversorgungen an die Löcher in der Nähe des roten Drahts angeschlossen, und negative Stromversorgungen an die Löcher in der Nähe des blauen Drahts.

#. In einem Stromkreis fließt der Strom vom positiven Pol zum negativen Pol, nachdem er durch die Last geflossen ist. In diesem Fall kann ein Kurzschluss auftreten.

|bc3| 


Lass uns der Stromrichtung folgen, um den Schaltkreis aufzubauen!

1. In diesem Schaltkreis verwenden wir den 3V3-Pin des Pico 2 W-Boards, um die LED zu versorgen. Verwende ein männlich-zu-männlich (M2M) Jumperkabel, um es mit der roten Stromschiene zu verbinden.
#. Um die LED zu schützen, muss der Strom durch einen 220-Ohm-Widerstand fließen. Verbinde ein Ende (beliebiges Ende) des Widerstands mit der roten Stromschiene und das andere Ende mit der freien Reihe des Breadboards (Reihe 24 in meinem Schaltkreis).

    .. note::
        Der Farbring des 220-Ohm-Widerstands ist rot, rot, schwarz, schwarz und braun.

#. Wenn du die LED aufnimmst, wirst du sehen, dass einer ihrer Anschlüsse länger als der andere ist. Verbinde den längeren Anschluss mit derselben Reihe wie der Widerstand und den kürzeren Anschluss mit derselben Reihe über die mittlere Lücke auf dem Breadboard.

    .. note::
        Der längere Anschluss ist die Anode, die die positive Seite des Schaltkreises darstellt; der kürzere Anschluss ist die Kathode, die die negative Seite darstellt. 

        Die Anode muss über einen Widerstand mit dem GPIO-Pin verbunden werden; die Kathode muss mit dem GND-Pin verbunden werden.

#. Verbinde mit einem männlich-zu-männlich (M2M) Jumperkabel den kurzen Pin der LED mit der negativen Stromschiene des Breadboards.
#. Verbinde den GND-Pin des Pico 2 W mit der negativen Stromschiene mit einem Jumper.

Vorsicht vor Kurzschlüssen
------------------------------
Kurzschlüsse können auftreten, wenn zwei Komponenten, die nicht verbunden sein sollten, "versehentlich" verbunden werden.
Dieses Kit enthält Widerstände, Transistoren, Kondensatoren, LEDs usw., die lange Metallstifte haben, die aneinanderstoßen und einen Kurzschluss verursachen können. Einige Schaltkreise funktionieren einfach nicht richtig, wenn ein Kurzschluss auftritt. Gelegentlich kann ein Kurzschluss Komponenten dauerhaft beschädigen, insbesondere zwischen der Stromversorgung und der Erdungsschiene, wodurch der Schaltkreis sehr heiß wird, das Plastik auf dem Breadboard schmilzt und sogar die Komponenten verbrennen!

Daher stelle immer sicher, dass die Stifte aller Elektronik auf dem Breadboard sich nicht berühren.

Richtung des Schaltkreises
-------------------------------
Schaltkreise haben eine Orientierung, und die Orientierung spielt eine wichtige Rolle bei bestimmten elektronischen Komponenten. Es gibt einige Geräte mit Polarität, was bedeutet, dass sie korrekt basierend auf ihren positiven und negativen Polen angeschlossen werden müssen. Schaltkreise, die mit der falschen Orientierung aufgebaut sind, funktionieren nicht richtig.

|bc3| 

Wenn du die LED in diesem einfachen Schaltkreis, den wir früher gebaut haben, umkehrst, wirst du feststellen, dass sie nicht mehr funktioniert.

Im Gegensatz dazu haben einige Geräte keine Richtung, wie die Widerstände in diesem Schaltkreis, sodass du sie umkehren kannst, ohne die normale Funktion der LEDs zu beeinträchtigen.

Die meisten Komponenten und Module mit Bezeichnungen wie "+", "-", "GND", "VCC" oder mit Stiften unterschiedlicher Länge müssen auf eine bestimmte Weise mit dem Schaltkreis verbunden werden.


Schutz des Schaltkreises
-------------------------------------

Strom ist die Rate, mit der Elektronen an einem Punkt in einem vollständigen elektrischen Schaltkreis vorbeifließen. Im einfachsten Fall entspricht Strom = Fluss. Ein Ampere (AM-pir) oder Amp ist die internationale Einheit zur Messung des Stroms. Es drückt die Menge der Elektronen (manchmal als "elektrische Ladung" bezeichnet) aus, die über einen bestimmten Zeitraum an einem Punkt in einem Schaltkreis vorbeifließen.

Die treibende Kraft (Spannung) hinter dem Stromfluss wird als Spannung bezeichnet und in Volt (V) gemessen.

Widerstand (R) ist die Eigenschaft des Materials, die den Stromfluss einschränkt, und wird in Ohm (Ω) gemessen.

Nach dem Ohmschen Gesetz (solange die Temperatur konstant bleibt) sind Strom, Spannung und Widerstand proportional.
Der Strom eines Schaltkreises ist proportional zu seiner Spannung und umgekehrt proportional zu seinem Widerstand.

Daher ist Strom (I) = Spannung (V) / Widerstand (R).

* `Ohm's law - Wikipedia <https://en.wikipedia.org/wiki/Ohm%27s_law>`_

Zum Ohmschen Gesetz können wir ein einfaches Experiment durchführen.

|bc3| 

Indem du den Draht, der 3V3 mit 5V (d.h. VBUS, der 40. Pin des Pico 2 W) verbindet, wechselst, wird die LED heller.
Wenn du den Widerstand von 220 Ohm auf 1000 Ohm wechselst (Farbring: braun, schwarz, schwarz, braun und braun), wirst du feststellen, dass die LED dunkler wird als zuvor. Je größer der Widerstand, desto dunkler die LED.

.. note::
    Für eine Einführung in Widerstände und wie man Widerstandswerte berechnet, siehe :ref:`cpn_resistor`.

Die meisten verpackten Module benötigen nur Zugang zur richtigen Spannung (normalerweise 3,3V oder 5V), wie das Ultraschallmodul.

In deinen selbstgebauten Schaltkreisen musst du jedoch die Versorgungsspannung und die Verwendung von Widerständen für elektrische Geräte beachten.


Als Beispiel verbrauchen LEDs normalerweise 20 mA Strom, und ihr Spannungsabfall beträgt etwa 1,8 V. Nach dem Ohmschen Gesetz benötigen wir bei Verwendung einer 5V-Stromversorgung einen Widerstand von mindestens 160 Ohm ((5-1.8)/20mA), um die LED nicht durchzubrennen.


