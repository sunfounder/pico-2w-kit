.. note::

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community auf Facebook! Vertiefen Sie gemeinsam mit anderen begeisterten Mitgliedern Ihre Kenntnisse rund um Raspberry Pi, Arduino und ESP32.

    **Why Join?**

    - **Expert Support**: Erhalten Sie Unterstützung bei technischen Problemen und Fragen nach dem Kauf durch unsere Community und unser Team.
    - **Learn & Share**: Teilen Sie Tipps und Tutorials, um Ihre Fähigkeiten weiter auszubauen.
    - **Exclusive Previews**: Bekommen Sie frühzeitig Zugang zu Produktankündigungen und exklusiven Vorschauen.
    - **Special Discounts**: Profitieren Sie von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festive Promotions and Giveaways**: Nehmen Sie an saisonalen Aktionen und Gewinnspielen teil.

    👉 Bereit, mit uns Neues zu entdecken und kreativ zu werden? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

.. _cpn_i2c_lcd:

I2C LCD1602
==============

|i2c_lcd1602|

* **GND**: Masseanschluss.
* **VCC**: Versorgungsspannung, 5 V.
* **SDA**: Serielle Datenleitung; wird über einen Pull-up-Widerstand mit VCC verbunden.
* **SCL**: Serielle Taktleitung; wird über einen Pull-up-Widerstand mit VCC verbunden.

LCD-Displays verbessern die Interaktion zwischen Mensch und Maschine erheblich. Ein gemeinsamer Nachteil ist jedoch, dass diese Displays meist viele I/O-Pins des Controllers beanspruchen. Dies schränkt die verfügbare Anzahl der Pins für andere Anwendungen deutlich ein.

Zur Lösung dieses Problems wurde das LCD1602 mit einem I2C-Modul entwickelt. Das integrierte PCF8574-Modul wandelt I2C-Seriendaten in parallele Daten um. Dadurch wird der Anschluss des LCDs stark vereinfacht und die Anzahl der benötigten I/O-Pins reduziert.

* `PCF8574 Datasheet <https://www.ti.com/lit/ds/symlink/pcf8574.pdf?ts=1627006546204&ref_url=https%253A%252F%252Fwww.google.com%252F>`_

**I2C Address**

Die Standardadresse lautet meistens 0x27; in wenigen Fällen wird 0x3F verwendet.

Anhand der Standardadresse 0x27 als Beispiel erklärt, lässt sich die Geräteadresse durch Kurzschließen der Lötpads A0/A1/A2 ändern. Standardmäßig sind A0/A1/A2 auf „1“ gesetzt; durch Kurzschließen des jeweiligen Pads wird der Wert auf „0“ gesetzt.

|i2c_address|

**Backlight/Contrast**

Die Hintergrundbeleuchtung kann mithilfe einer Steckbrücke aktiviert werden; entfernen Sie diese Brücke, um die Beleuchtung zu deaktivieren. Das blaue Potentiometer auf der Rückseite dient zur Einstellung des Kontrasts (Helligkeitsverhältnis zwischen hellstem Weiß und dunkelstem Schwarz).

|back_lcd1602|

* **Shorting Cap**: Aktiviert oder deaktiviert die Hintergrundbeleuchtung durch Aufstecken oder Entfernen.
* **Potentiometer**: Dient zur Anpassung des Kontrasts (Klarheit der dargestellten Zeichen); im Uhrzeigersinn wird der Kontrast erhöht, gegen den Uhrzeigersinn verringert.




**Example**

* :ref:`py_lcd` (Für MicroPython-Nutzer)
* :ref:`py_room_temp` (Für MicroPython-Nutzer)
* :ref:`py_guess_number` (Für MicroPython-Nutzer)
* :ref:`py_iot_openweather` (Für MicroPython-Nutzer)
* :ref:`ar_lcd` (Für Arduino-Nutzer)
