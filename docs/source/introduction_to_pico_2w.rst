.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche mit Gleichgesinnten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum solltest du beitreten?**

    - **Expertenunterstützung**: Erhalte Hilfe von unserer Community und unserem Team bei technischen Herausforderungen und nach dem Kauf.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Profitiere von exklusiven Vergünstigungen auf unsere neuesten Produkte.
    - **Festliche Aktionen & Gewinnspiele**: Nimm an Verlosungen und Sonderaktionen zu Feiertagen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und trete noch heute bei!

.. _cpn_pico_2w:

Einführung in den Pico 2 W
=======================================

|pico_2w_side|

Der Raspberry Pi Pico 2 W bietet eine 2,4-GHz-802.11n-WLAN-Schnittstelle sowie Bluetooth 5.2 und erweitert damit die Möglichkeiten für IoT- und Smart-Produkt-Designs. Dies ermöglicht eine noch flexiblere Integration in deine Projekte. 

Er kann sowohl im Station- als auch im Access-Point-Modus betrieben werden. Entwicklern in C und MicroPython steht die vollständige Netzwerkintegration zur Verfügung. Der Raspberry Pi Pico 2 W kombiniert den RP2350-Mikrocontroller mit 4 MB Flash-Speicher und einem integrierten Stromversorgungs-Chip, der Eingangsspannungen von 1,8–5,5 V unterstützt. 

Er verfügt über 26 GPIO-Pins, von denen drei als analoge Eingänge genutzt werden können. Alle Pins sind als 0,1"-Durchkontaktierungen mit gestanzten Rändern ausgeführt. Der Raspberry Pi Pico 2 W ist sowohl einzeln als auch in 480er-Großpackungen für automatisierte Bestückung erhältlich.

Eigenschaften
----------------

* RP2350-Mikrocontroller mit 4 MB Flash-Speicher.
* Integrierte 2,4-GHz-Wireless-Schnittstellen. (802.11n, Bluetooth 5.2)
  - Unterstützung für Bluetooth LE Central- und Peripheral-Modi.
  - Unterstützung für Bluetooth Classic.
* Micro-USB-B-Anschluss für Stromversorgung und Datenübertragung (auch zur Flash-Neuprogrammierung).
* 40-polige 21 mm × 51 mm "DIP"-Platine mit 1 mm Dicke und 0,1"-Lötkontakten, einschließlich Randverzinnung.
  - 26 multifunktionale 3,3-V-GPIOs.
  - 23 GPIOs sind ausschließlich digital, drei unterstützen zusätzlich analoge Eingänge (ADC).
  - Kann als SMD-Modul direkt auf Platinen gelötet werden.
* 3-poliger Arm Serial Wire Debug (SWD)-Port.
* Einfache, aber flexible Stromversorgungsarchitektur.
  - Verschiedene Optionen zur einfachen Stromversorgung über Micro-USB, externe Spannungsquellen oder ein Power Pack.
* 1 × USB 1.1-Controller und PHY mit Host- und Geräteunterstützung.
* 3 x Programmierbare I/O (PIO)-Blöcke mit insgesamt 12 Zustandsautomaten.
  - Flexible, benutzerprogrammierbare Hochgeschwindigkeitsschnittstellen.
  - Kann Schnittstellen wie SD-Karten und VGA emulieren.
* Unterstützte Eingangsspannung: 1,8–5,5 V DC.
* Betriebstemperaturbereich: -20 °C bis +85 °C.
* Randverzinnung ermöglicht direktes Löten auf Trägerplatinen.
* Drag-and-Drop-Programmierung über USB-Massenspeicher.
* Präziser On-Chip-Taktgeber.
* Integrierter Temperatursensor.
* Beschleunigte Integer- und Floating-Point-Bibliotheken direkt auf dem Chip.

Pico's Pins
------------

|pico2w_pin|


.. list-table::
    :widths: 3 5 10
    :header-rows: 1

    *   - Name
        - Beschreibung
        - Funktion
    *   - GP0-GP28
        - Allgemeine digitale Ein-/Ausgabe-Pins (GPIO)
        - Können als Ein- oder Ausgang genutzt werden, ohne eine festgelegte Standardfunktion.
    *   - GND
        - 0-Volt-Masse
        - Mehrere GND-Pins um den Pico 2 W erleichtern die Verdrahtung.
    *   - RUN
        - Aktivierung/Deaktivierung des Pico
        - Startet oder stoppt den Pico 2 W über einen externen Mikrocontroller.
    *   - GPxx_ADCx
        - GPIO oder Analog-Eingang
        - Kann als analoger Eingang oder als digitaler Ein-/Ausgang genutzt werden (aber nicht beides gleichzeitig).
    *   - ADC_VREF
        - Referenzspannung für den Analog-Digital-Wandler (ADC)
        - Spezieller Eingangspin zur Festlegung einer Referenzspannung für analoge Eingänge.
    *   - AGND
        - Masse für den Analog-Digital-Wandler (ADC)
        - Spezielle Masseverbindung zur Verwendung mit dem ADC_VREF-Pin.
    *   - 3V3(O)
        - 3,3-V-Spannungsausgang
        - 3,3-V-Stromquelle, dieselbe Spannung, mit der der Pico 2 W intern arbeitet (aus VSYS erzeugt).
    *   - 3V3(E)
        - Aktiviert oder deaktiviert die 3,3-V-Versorgung
        - Ermöglicht das Ein- und Ausschalten der 3V3(O)-Stromversorgung.
    *   - VSYS
        - 2–5 V Stromversorgung
        - Direkte Verbindung zur internen Stromversorgung des Pico, nicht abschaltbar ohne den gesamten Pico 2 W auszuschalten.
    *   - VBUS
        - 5-V-Stromversorgung
        - 5-V-Quelle aus dem Micro-USB-Anschluss des Pico zur Versorgung von Peripheriegeräten mit mehr als 3,3 V.

Die beste Anlaufstelle für alle Informationen zum Raspberry Pi Pico 2 W ist `hier <https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html>`_.

Oder folge den untenstehenden Links:

* `Raspberry Pi Pico 2 Produktübersicht <https://datasheets.raspberrypi.com/pico/pico-2-product-brief.pdf>`_
* `Raspberry Pi Pico 2 W Datenblatt <https://datasheets.raspberrypi.com/picow/pico-2-w-datasheet.pdf>`_
* `Erste Schritte mit Raspberry Pi Pico: C/C++ Entwicklung <https://datasheets.raspberrypi.org/pico/getting-started-with-pico.pdf>`_
* `Raspberry Pi Pico C/C++ SDK <https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-c-sdk.pdf>`_
* `API-Dokumentation für das Raspberry Pi Pico C/C++ SDK <https://raspberrypi.github.io/pico-sdk-doxygen/>`_
* `Raspberry Pi Pico Python SDK <https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-python-sdk.pdf>`_
* `Raspberry Pi RP2350 Datenblatt <https://datasheets.raspberrypi.com/rp2350/rp2350-datasheet.pdf>`_
* `Hardware-Design mit RP2350 <https://datasheets.raspberrypi.com/rp2350/hardware-design-with-rp2350.pdf>`_
* `Raspberry Pi Pico W Design-Dateien <https://datasheets.raspberrypi.com/picow/RPi-PicoW-PUBLIC-20220607.zip>`_
* `Raspberry Pi Pico W STEP-Datei <https://datasheets.raspberrypi.com/picow/PicoW-step.zip>`_
