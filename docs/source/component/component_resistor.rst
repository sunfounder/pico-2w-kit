.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein – zusammen mit Gleichgesinnten.

    **Why Join?**

    - **Expert Support**: Löse Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Learn & Share**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exclusive Previews**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Vorschauen.
    - **Special Discounts**: Profitiere von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festive Promotions and Giveaways**: Nimm an Gewinnspielen und Sonderaktionen zu Feiertagen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _cpn_resistor:

Widerstand
============

|img_res|

Ein Widerstand ist ein elektronisches Bauelement, das den Stromfluss in einem Zweig begrenzen kann.  
Ein Festwiderstand ist ein Widerstandstyp mit festem Widerstandswert, während ein Potentiometer oder ein variabler Widerstand verstellbar ist.

Es gibt zwei gängige Schaltsymbole für Widerstände, und der Widerstandswert ist normalerweise direkt auf dem Bauelement angegeben.  
Diese Symbole in einem Schaltplan stehen für einen Widerstand.

|img_res_symbol|

**Ω** ist die Einheit des Widerstands, größere Einheiten sind KΩ, MΩ usw.  
Ihr Verhältnis ist wie folgt: 1 MΩ = 1000 KΩ, 1 KΩ = 1000 Ω.  
Der Widerstandswert ist in der Regel auf dem Bauteil markiert.

Beim Einsatz eines Widerstands ist es notwendig, seinen Wert zu bestimmen.  
Dafür gibt es zwei Methoden: Entweder man liest den Farbcode auf dem Widerstand oder misst ihn mit einem Multimeter.  
Die erste Methode ist schneller und praktischer.

|img_res_card|

Wie in der Karte dargestellt, steht jede Farbe für eine Zahl.

.. list-table::

   * - Schwarz
     - Braun
     - Rot
     - Orange
     - Gelb
     - Grün
     - Blau
     - Violett
     - Grau
     - Weiß
     - Gold
     - Silber
   * - 0
     - 1
     - 2
     - 3
     - 4
     - 5
     - 6
     - 7
     - 8
     - 9
     - 0.1
     - 0.01

Widerstände mit 4 oder 5 Farbringen werden häufig verwendet. Sie sind mit jeweils vier oder fünf farbigen Bändern versehen.

Oft ist es schwierig zu bestimmen, von welchem Ende aus die Farbcodierung gelesen werden soll.  
Ein hilfreicher Tipp: Der Abstand zwischen dem 4. und 5. Farbring ist in der Regel größer als die anderen Abstände.

Daher kann man das Ende des Widerstands betrachten, an dem sich zwei Farbringe befinden.  
Ist der Abstand zwischen diesen größer als bei den anderen, sollte die Farbcodierung von der gegenüberliegenden Seite abgelesen werden.

Sehen wir uns nun an, wie der Widerstandswert eines 5-Band-Widerstands ermittelt wird.

|img_220ohm|

Der Widerstandswert wird von links nach rechts gelesen.  
Das Format lautet: 1. Band 2. Band 3. Band x 10^Multiplikator (Ω), mit einer Toleranz von ±Toleranz%.  
Für diesen Widerstand ergibt sich:

2 (Rot) 2 (Rot) 0 (Schwarz) x 10^0 (Schwarz) Ω = 220 Ω, mit einer Toleranz von ±1% (Braun).

.. list-table:: Common resistor color band
    :header-rows: 1

    * - :ref:`cpn_resistor` 
      - Farbcode  
    * - 10Ω   
      - Braun Schwarz Schwarz Silber Braun
    * - 100Ω   
      - Braun Schwarz Schwarz Schwarz Braun
    * - 220Ω 
      - Rot Rot Schwarz Schwarz Braun
    * - 330Ω 
      - Orange Orange Schwarz Schwarz Braun
    * - 1kΩ 
      - Braun Schwarz Schwarz Braun Braun
    * - 2kΩ 
      - Rot Schwarz Schwarz Braun Braun
    * - 5.1kΩ 
      - Grün Braun Schwarz Braun Braun
    * - 10kΩ 
      - Braun Schwarz Schwarz Rot Braun 
    * - 100kΩ 
      - Braun Schwarz Schwarz Orange Braun 
    * - 1MΩ 
      - Braun Schwarz Schwarz Grün Braun 

Mehr Informationen über Widerstände findest du hier: `Resistor - Wikipedia <https://en.wikipedia.org/wiki/Resistor>`_.

