.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein – zusammen mit Gleichgesinnten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Erhalte Unterstützung von unserer Community und unserem Team bei technischen Herausforderungen und Fragen nach dem Kauf.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu erweitern.
    - **Exklusive Einblicke**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Vorschauen.
    - **Spezielle Rabatte**: Profitiere von exklusiven Vergünstigungen auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nimm an Verlosungen und Sonderaktionen zu Feiertagen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _cpn_mpr121:

MPR121-Modul
===========================

|img_mpr121|

* **3.3V**: Spannungsversorgung
* **IRQ**: Open-Collector-Interrupt-Ausgang, aktiv niedrig
* **SCL**: I2C-Takt (Clock)
* **SDA**: I2C-Daten (Data)
* **ADD**: I2C-Adressauswahl-Pin. Durch Verbinden des ADDR-Pins mit VSS, VDD, SDA oder SCL ergeben sich die I2C-Adressen 0x5A, 0x5B, 0x5C und 0x5D.
* **GND**: Masse (Ground)
* **0~11**: Elektroden 0~11, jede Elektrode fungiert als kapazitiver Berührungssensor. Typischerweise kann eine Elektrode einfach ein Metallstück oder ein Draht sein. Abhängig von der Länge des Drahtes oder dem Material, auf dem sich die Elektrode befindet, kann die Empfindlichkeit des Sensors jedoch variieren. Daher ermöglicht der MPR121 eine individuelle Konfiguration der Trigger- und Deaktivierungswerte für jede Elektrode.

**MPR121 ÜBERSICHT**

Der MPR121 ist ein kapazitiver Berührungssensor-Controller der zweiten Generation und der Nachfolger der MPR03x-Serie. Er bietet erweiterte interne Funktionen und zahlreiche neue Features, darunter:

- Unterstützung für eine größere Anzahl von Elektroden
- Hardware-konfigurierbare I2C-Adresse
- Verbesserte Filtermechanismen mit integrierter Entprellungsfunktion
- Vollständig unabhängige Elektroden mit automatischer Konfigurationsfähigkeit

Zusätzlich verfügt der MPR121 über einen 13. simulierten Sensorkanal, der speziell für die Erkennung von Objekten in unmittelbarer Nähe entwickelt wurde und die multiplexierten Sensoreingänge nutzt.

* `MPR121 Datasheet <https://cdn-shop.adafruit.com/datasheets/MPR121.pdf>`_

**Eigenschaften**

* Energiesparender Betrieb
    • Betriebsspannung von 1,71 V bis 3,6 V
    • 29 μA Stromverbrauch bei einer Abtastrate von 16 ms
    • 3 μA Stromverbrauch im Stop-Modus
* 12 kapazitive Sensoreingänge
    • 8 davon können zusätzlich als LED-Treiber oder GPIO genutzt werden
* Vollständige Berührungserkennung
    • Automatische Konfiguration für jeden Sensoreingang
    • Automatische Kalibrierung für jeden Sensoreingang
    • Einstellbare Schwellwerte für Berührungs- und Loslassereignisse mit Entprellungsfunktion
* I2C-Schnittstelle mit Interrupt-Ausgang
* 3 mm x 3 mm x 0,65 mm QFN-Gehäuse mit 20 Pins
* Betriebstemperaturbereich von -40 °C bis +85 °C



**Beispiel**

* :ref:`py_mpr121` (Für MicroPython-Nutzer)
* :ref:`py_fruit_piano` (Für MicroPython-Nutzer)
* :ref:`ar_mpr121` (Für Arduino-Nutzer)
