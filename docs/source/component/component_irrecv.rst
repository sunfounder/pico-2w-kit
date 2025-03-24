.. note::

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community auf Facebook! Entdecken Sie gemeinsam mit anderen begeisterten Mitgliedern die vielfältigen Möglichkeiten rund um Raspberry Pi, Arduino und ESP32.

    **Why Join?**

    - **Expert Support**: Erhalten Sie Hilfe bei technischen Problemen und Fragen nach dem Kauf durch unsere Community und unser Team.
    - **Learn & Share**: Tauschen Sie Erfahrungen, Tipps und Tutorials aus und erweitern Sie Ihr Wissen.
    - **Exclusive Previews**: Bekommen Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Vorschauen.
    - **Special Discounts**: Profitieren Sie von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festive Promotions and Giveaways**: Nehmen Sie an saisonalen Aktionen und Gewinnspielen teil.

    👉 Bereit, mit uns Neues zu entdecken und kreativ zu werden? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

.. _cpn_ir_receiver:

Infrared Receiver
=================================

IR Receiver
----------------------------

|img_irrecv|

* S: Signalausgang
* +: VCC
* -: GND

Ein Infrarot-Empfänger (IR-Receiver) ist eine elektronische Komponente, die IR-Signale empfängt und diese in TTL-kompatible Signale umwandelt. Äußerlich ähnelt er einem Kunststoff-Transistorgehäuse und eignet sich optimal für Anwendungen im Bereich der Infrarot-Fernsteuerung und Signalübertragung.

Die IR-Kommunikation ist eine weit verbreitete, kostengünstige und benutzerfreundliche kabellose Technologie. Infrarotstrahlung hat eine etwas größere Wellenlänge als sichtbares Licht und ist somit für das menschliche Auge unsichtbar – ideal für drahtlose Anwendungen. Eine häufig verwendete Modulationsfrequenz bei IR-Kommunikation ist 38 kHz.

* HX1838 IR-Empfängersensor mit hoher Empfindlichkeit
* Ideal für Fernsteuerungsanwendungen
* Betriebsspannung: 3,3–5 V
* Schnittstelle: digital
* Modulationsfrequenz: 38 kHz


Remote Control
-------------------------

|img_controller|

Dies ist eine kompakte Infrarot-Fernbedienung mit 21 Funktionstasten und einer Reichweite von bis zu 8 Metern. Sie eignet sich hervorragend für die Bedienung verschiedenster Geräte, z. B. im Kinderzimmer.

* Größe: 85 × 39 × 6 mm
* Reichweite: 8–10 m
* Batterie: 3-V-Lithium-Mangan-Knopfzelle
* Infrarot-Trägerfrequenz: 38 kHz
* Oberflächenmaterial: 0,125 mm PET-Folie
* Lebensdauer: über 20.000 Tastenbetätigungen


**Example**

* :ref:`py_irremote` (Für MicroPython-Nutzer)
* :ref:`ar_irremote` (Für Arduino-Nutzer)
