.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein und tausche dich mit anderen Technikbegeisterten aus.

    **Warum beitreten?**

    - **Expertenunterstützung**: Erhalte Hilfe bei technischen Herausforderungen und Fragen nach dem Kauf von unserer Community und unserem Team.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Previews.
    - **Spezielle Rabatte**: Profitiere von exklusiven Vergünstigungen für unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nimm an Verlosungen und saisonalen Promotions teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _py_micro:

2.8 Sanft drücken
==========================

|img_micro_switch|

In dieser Lektion lernen wir, wie ein **Mikroschalter** (auch als Endschalter bekannt) mit dem Raspberry Pi Pico 2 W verwendet wird, um zu erkennen, ob er gedrückt oder losgelassen wird. Mikroschalter werden häufig in Geräten wie Mikrowellentüren, Druckerdeckeln oder als Endanschläge in 3D-Druckern eingesetzt, da sie zuverlässig sind und häufige Betätigungen problemlos bewältigen können.

* :ref:`cpn_micro_switch`

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Es ist praktisch, ein komplettes Kit zu kaufen – hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ENTHALTENE ARTIKEL IM KIT
        - LINK
    *   - Pico 2 W Starter Kit	
        - 450+
        - |link_pico2w_kit|


Alternativ kannst du die Komponenten auch einzeln über die unten stehenden Links erwerben.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - KOMPONENTE	
        - MENGE
        - LINK

    *   - 1
        - :ref:`cpn_pico_2w`
        - 1
        - |link_pico2w_buy|
    *   - 2
        - Micro-USB-Kabel
        - 1
        - 
    *   - 3
        - :ref:`cpn_breadboard`
        - 1
        - |link_breadboard_buy|
    *   - 4
        - :ref:`cpn_wire`
        - Mehrere
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_resistor`
        - 1 (10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_capacitor`
        - 1 (104)
        - |link_capacitor_buy|
    *   - 7
        - :ref:`cpn_micro_switch`
        - 1
        - 

**Den Mikroschalter verstehen**

Ein Mikroschalter verfügt typischerweise über drei Pins:

|img_micro_switch|

- **Common (C)**: Der mittlere Pin.
- **Normally Open (NO)**: Wird mit dem **Common (C)**-Pin verbunden, wenn der Schalter **gedrückt** wird.
- **Normally Closed (NC)**: Wird mit dem **Common (C)**-Pin verbunden, wenn der Schalter **nicht gedrückt** wird.

Durch die entsprechende Verdrahtung des Schalters können wir erkennen, wann er gedrückt wird, indem wir den Spannungspegel an einem GPIO-Pin auslesen.

**Schaltplan**

|sch_limit_sw|

Standardmäßig ist GP14 auf LOW, und beim Drücken wechselt er auf HIGH.

Der 10KΩ-Widerstand sorgt dafür, dass GP14 auf LOW bleibt, solange der Schalter nicht gedrückt wird.

Beim Drücken eines mechanischen Schalters kann es zu Kontaktprellen kommen, wodurch der Schalter kurzzeitig zwischen geöffnetem und geschlossenem Zustand wechselt. Der Kondensator zwischen GP14 und GND hilft, dieses Rauschen zu filtern.

* **Schalter nicht gedrückt**:

  * Der **Common (C)**-Pin ist mit dem **NC**-Pin verbunden, der wiederum mit **GND** verbunden ist.
  * **GP14** liest **LOW** (0V).

* **Schalter gedrückt**:

  * Der **Common (C)**-Pin ist mit dem **NO**-Pin verbunden, der mit **3.3V** verbunden ist.
  * **GP14** liest **HIGH** (3,3V).


**Verdrahtung**

|wiring_limit_sw|


**Code schreiben**

Wir schreiben ein MicroPython-Programm, das erkennt, wann der Mikroschalter gedrückt wird, und eine entsprechende Meldung ausgibt.

.. note::

  * Öffne die Datei ``2.8_micro_switch.py`` aus ``pico-2w-kit-main/micropython`` oder kopiere den Code in Thonny, klicke auf "Run" oder drücke F5.

  * Stelle sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx. 

.. code-block:: python

    import machine
    import utime

    # Initialisierung von GP14 als Eingangspin
    switch = machine.Pin(14, machine.Pin.IN)

    while True:
        if switch.value() == 1:
            print("The switch is pressed!")
            utime.sleep(0.5)  # Entprellzeit

Wenn das Programm läuft, kannst du folgendes beobachten:

* **Nicht gedrückt**: Es erscheint keine Meldung.
* **Gedrückt**: „Der Schalter wurde gedrückt!“ erscheint in der Konsole jedes Mal, wenn der Schalter betätigt wird.

**Den Code verstehen**

#. Module importieren:

   * ``import machine``: Zugriff auf Hardware-Funktionen.
   * ``import utime``: Zeitfunktionen.

#. Schalter-Pin initialisieren:

   * ``switch = machine.Pin(14, machine.Pin.IN)``: Setzt GP14 als Eingangspin.

#. Hauptschleife:

   * ``while True``: Startet eine Endlosschleife.
   * ``if switch.value() == 1``: Prüft, ob der Schalter gedrückt ist (GP14 liest HIGH).
   * ``print("The switch is pressed!")``: Gibt eine Meldung in der Konsole aus.
   * ``utime.sleep(0.5)``: Fügt eine Verzögerung hinzu, um Prellen zu vermeiden.


**Alternative Verdrahtung: Verwendung eines internen Pull-Down-Widerstands**

Falls du die Schaltung noch weiter vereinfachen möchtest, kannst du den internen Pull-Down-Widerstand nutzen:

* **Schaltungsänderung**:

  * Entferne den externen 10KΩ-Widerstand und den 0,1-µF-Kondensator.
  * Mikroschalter-Anschlüsse:

    * **Common (C) Terminal**: Mit GP14 am Pico verbinden.
    * **Normally Open (NO) Terminal**: Mit 3,3V am Pico verbinden.
    * **Normally Closed (NC) Terminal**: Nicht verbinden.

* **Geändertes Codebeispiel**:

  .. code-block:: python

      import machine
      import utime

      # Initialisierung von GP14 als Eingang mit internem Pull-Down-Widerstand
      switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

      while True:
          if switch.value() == 1:
              print("The switch is pressed!")
              utime.sleep(0.5)  # Entprellzeit


**Praktische Anwendungen**

* **Endschalter in CNC-Maschinen oder 3D-Druckern**: Erkennung der Bewegungsgrenze.
* **Sicherheitsverriegelungen**: Sicherstellen, dass ein Gerät nur bei bestimmten Bedingungen funktioniert (z. B. wenn eine Tür geschlossen ist).
* **Benutzereingaben**: Nutzung als robuster und zuverlässiger Taster.

**Weitere Experimente** 

* Eine LED steuern:

  Verbinde eine LED mit einem anderen GPIO-Pin (z. B. GP15) und verwende einen geeigneten Widerstand. Ändere den Code so, dass die LED leuchtet, wenn der Schalter gedrückt wird.
  
  .. code-block:: python
    
    import machine
    import utime

    switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
    led = machine.Pin(15, machine.Pin.OUT)

    while True:
        if switch.value() == 1:
            led.value(1)  # LED einschalten
            print("The switch is pressed!")
            utime.sleep(0.5)
        else:
            led.value(0)  # LED ausschalten

* Tastendrücke zählen:

  Ändere den Code so, dass gezählt wird, wie oft der Schalter gedrückt wurde.

  * Eine LED steuern:

   .. code-block:: python

      import machine
      import utime

      switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
      count = 0

      while True:
          if switch.value() == 1:
              count += 1
              print("Switch pressed {} times".format(count))
              utime.sleep(0.5)

**Fazit**

Die Verwendung eines Mikroschalters mit dem Raspberry Pi Pico 2 W ermöglicht eine zuverlässige Erkennung physischer Interaktionen. Das Verständnis der Verkabelung und das korrekte Auslesen des Schalterzustands im Code sind essenziell für die Erstellung reaktionsschneller und interaktiver Projekte.

