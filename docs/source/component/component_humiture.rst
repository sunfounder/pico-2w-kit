.. note::

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community auf Facebook! Vertiefen Sie gemeinsam mit anderen begeisterten Mitgliedern Ihr Wissen rund um Raspberry Pi, Arduino und ESP32.

    **Why Join?**

    - **Expert Support**: Erhalten Sie Unterstützung bei technischen Fragen und Problemen nach dem Kauf durch unsere Community und unser Team.
    - **Learn & Share**: Tauschen Sie Tipps und Tutorials aus und erweitern Sie Ihre Fähigkeiten.
    - **Exclusive Previews**: Bekommen Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Vorschauen.
    - **Special Discounts**: Profitieren Sie von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festive Promotions and Giveaways**: Nehmen Sie an saisonalen Aktionen und Gewinnspielen teil.

    👉 Bereit, gemeinsam mit uns Neues zu entdecken und kreativ zu werden? Klicken Sie auf [|link_sf_facebook|] und werden Sie noch heute Mitglied!

.. _cpn_dht11:

DHT11 Humiture Sensor
=============================

Der digitale Temperatur- und Luftfeuchtigkeitssensor DHT11 ist ein kombinierter Sensor, der kalibrierte digitale Messwerte für Temperatur und Luftfeuchtigkeit liefert. Er vereint moderne digitale Signalverarbeitung mit zuverlässigen Messverfahren und bietet somit hohe Genauigkeit und langfristige Stabilität.

Der DHT11 kombiniert einen resistiven Feuchtigkeitssensor mit einem NTC-Thermistor zur Temperaturmessung und enthält einen leistungsfähigen 8-Bit-Mikrocontroller für die präzise Verarbeitung der Messdaten.

.. Das Schaltbild des Feuchtigkeits- und Temperatursensormoduls ist wie folgt dargestellt: |img_Hum-sch| 

Es stehen drei Anschlusspins zur Verfügung: VCC, GND und DATA.
Die Kommunikation startet mit einem Startsignal auf der DATA-Leitung 
vom Host zum DHT11. Anschließend sendet der DHT11 ein Antwortsignal zurück. Danach beginnt die Übertragung der 40-Bit-Daten (8 Bit Luftfeuchtigkeit ganzzahlig + 8 Bit Luftfeuchtigkeit dezimal + 8 Bit Temperatur ganzzahlig + 8 Bit Temperatur dezimal + 8 Bit Prüfsumme).

|img_Dht11|

**Features**

    #. Messbereich Luftfeuchtigkeit: 20 – 90 % RH
    #. Messbereich Temperatur: 0 – 60 ℃
    #. Digitale Ausgangssignale für Temperatur und Luftfeuchtigkeit
    #. Betriebsspannung: DC 5 V; PCB-Größe: 2,0 × 2,0 cm
    #. Messgenauigkeit Luftfeuchtigkeit: ±5 % RH
    #. Messgenauigkeit Temperatur: ±2 ℃

* `DHT11 Datenblatt <http://wiki.sunfounder.cc/images/c/c7/DHT11_datasheet.pdf>`_

**Example**

* :ref:`py_dht11` (Für MicroPython-Nutzer)
* :ref:`py_iot_adafruitio` (Für MicroPython-Nutzer)
* :ref:`py_iot_sunfounder_controller_plant` (Für MicroPython-Nutzer)
* :ref:`py_iot_ble_home` (Für MicroPython-Nutzer)
* :ref:`ar_dht11` (Für Arduino-Nutzer)
