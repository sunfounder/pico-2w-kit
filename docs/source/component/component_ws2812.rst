.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein – zusammen mit Gleichgesinnten.

    **Why Join?**

    - **Expert Support**: Löse Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Learn & Share**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exclusive Previews**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Vorschauen.
    - **Special Discounts**: Profitiere von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festive Promotions and Giveaways**: Nimm an Gewinnspielen und Sonderaktionen zu Feiertagen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _cpn_ws2812:

WS2812 RGB 8 LEDs Strip
============================

|img_ws2812|

Der WS2812 RGB 8 LEDs Strip besteht aus 8 RGB-LEDs.  
Zur Steuerung aller LEDs wird nur ein einziger Pin benötigt. Jede RGB-LED enthält einen WS2812-Chip, der individuell gesteuert werden kann.  
Er ermöglicht eine 256-stufige Helligkeitssteuerung sowie eine vollständige Farbdarstellung mit 16.777.216 Farben.  

Zudem verfügt jedes Pixel über eine digitale Schnittstelle, ein Daten-Latch-Signal, eine Verstärkerschaltung und eine integrierte Signalformung,  
die eine gleichbleibende Farbwiedergabe über alle Pixel hinweg sicherstellt.

Der Streifen ist flexibel, koppelbar, biegbar und nach Bedarf zuschneidbar.  
Auf der Rückseite befindet sich ein selbstklebendes Band, mit dem er auf unebenen Oberflächen befestigt werden kann.  
Dadurch eignet er sich für Installationen in engen Räumen.

**Features**

* Work Voltage: DC5V
* IC: One IC drives one RGB LED
* Consumption: 0.3w each LED
* Working Temperature: -15-50
* Color: Full color RGB
* RGB Type: 5050RGB(Built-in IC WS2812B)
* Light Strip Thickness: 2mm
* Each LED can be controlled individually

**WS2812B Introduction**

* `WS2812B Datasheet <https://cdn-shop.adafruit.com/datasheets/WS2812B.pdf>`_

Der WS2812B ist eine intelligente LED-Lichtquelle, die eine Steuerschaltung und einen RGB-Chip in einem 5050-Gehäuse integriert.  
Er verfügt über ein digitales Daten-Latch, eine Signalverstärkerschaltung, einen internen Oszillator  
und eine programmierbare Konstantstromsteuerung für eine 12V-Spannungsversorgung.  
Diese Eigenschaften gewährleisten eine gleichmäßige und präzise Farbdarstellung über alle Pixel hinweg.

Die Datenübertragung erfolgt über ein NZR-Kommunikationsprotokoll.  
Nach dem Einschalten empfängt der DIN-Port Daten vom Controller.  
Das erste Pixel verarbeitet die ersten 24 Bit der Daten und speichert sie in seinem internen Latch.  
Die verbleibenden Daten werden von der internen Verstärkerschaltung aufbereitet und über den DO-Port an das nächste Pixel weitergeleitet.  
Mit jeder weiteren LED reduziert sich das Datensignal um 24 Bit.  
Dank der automatischen Signalregeneration können beliebig viele Pixel in Reihe geschaltet werden,  
die einzige Begrenzung liegt in der Signalübertragungsgeschwindigkeit.

Die LED bietet zahlreiche Vorteile: niedrige Betriebsspannung, energieeffizienter Betrieb, lange Lebensdauer, hohe Helligkeit,  
weiter Abstrahlwinkel, gute Farbkonsistenz, geringer Stromverbrauch sowie eine einfache Installation durch die Integration des Steuerchips in der LED.

.. Example
.. -------------------

.. :ref:`RGB LED Strip`


**Example**

* :ref:`py_neopixel` (For MicroPython User)
* :ref:`py_music_player` (For MicroPython User)
* :ref:`py_iot_cheerlights` (For MicroPython User)
* :ref:`ar_neopixel` (For Arduino User)
.. * :ref:`per_flowing_leds` (For Piper Make User)
