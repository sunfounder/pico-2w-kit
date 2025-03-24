.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein und tausche dich mit anderen Technikbegeisterten aus.

    **Warum beitreten?**

    - **Expertenunterstützung**: Erhalte Hilfe bei technischen Problemen und Fragen nach dem Kauf durch unsere Community und unser Team.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Previews.
    - **Spezielle Rabatte**: Profitiere von exklusiven Vergünstigungen für unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nimm an Verlosungen und saisonalen Promotions teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _py_led:

2.1 Hallo, LED! 
=======================================

Willkommen zu deinem ersten Hardware-Projekt mit dem Raspberry Pi Pico! In dieser Lektion lernen wir, wie man eine LED mithilfe von MicroPython zum Blinken bringt. Dieses einfache Projekt ist ein idealer Einstieg in das Physical Computing und hilft dir zu verstehen, wie du Hardware mit Code steuerst.

* :ref:`cpn_led`

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
        - 1 (220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|


**Schaltplan**

|sch_led|

Durch das Setzen des GPIO-Pins auf HIGH oder LOW steuerst du die Spannungsausgabe dieses Pins. Wenn der Pin auf HIGH gesetzt wird, fließt Strom durch die LED (begrenzt durch den Widerstand), wodurch sie aufleuchtet. Wird der Pin auf LOW gesetzt, fließt kein Strom und die LED erlischt.

**Verdrahtungsdiagramm**

|wiring_led|

**Code schreiben**

.. note::

    * Öffne die Datei ``2.1_hello_led.py`` unter dem Pfad ``pico-2w-kit-main/micropython`` oder kopiere diesen Code in Thonny, klicke dann auf "Run Current Script" oder drücke F5, um ihn auszuführen.

    * Stelle sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx. 

    * Für detaillierte Anleitungen siehe :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime
    
    led = machine.Pin(15, machine.Pin.OUT)
    while True:
        led.value(1)      # LED einschalten
        utime.sleep(2)    # 2 Sekunden warten
        led.value(0)      # LED ausschalten
        utime.sleep(2)    # 2 Sekunden warten

Sobald der Code ausgeführt wird, leuchtet die LED für 2 Sekunden auf und erlischt dann für 2 Sekunden.



**Den Code verstehen**

#. Bibliotheken importieren:

   * ``machine``: Ermöglicht den Zugriff auf die Hardware-Komponenten.
   * ``utime``: Enthält Zeitfunktionen wie Verzögerungen.

#. Initialisierung des LED-Pins:

   * ``led = machine.Pin(15, machine.Pin.OUT)``: Initialisiert GP15 als Ausgangspin und weist ihn der Variable ``led`` zu.

#. Erstellen einer Endlosschleife:

   * ``while True``: Startet eine Schleife, die den Code kontinuierlich ausführt.

#. Steuern der LED:

   * ``led.value(1)``: Setzt den Pin auf HIGH (3,3V) und schaltet die LED ein.
   * ``utime.sleep(2)``: Hält das Programm für 2 Sekunden an.
   * ``led.value(0)``: Setzt den Pin auf LOW (0V) und schaltet die LED aus.
   * ``utime.sleep(2)``: Hält das Programm für weitere 2 Sekunden an.

**Weitere Experimente**

* **Blinkfrequenz ändern**: Passe die ``utime.sleep(2)``-Werte an, um die Blinkgeschwindigkeit zu erhöhen oder zu verringern.
* **Andere Pins nutzen**: Verbinde die LED mit einem anderen GPIO-Pin und aktualisiere den Code entsprechend.
* **Mehrere LEDs steuern**: Füge weitere LEDs an verschiedene Pins hinzu und steuere sie im Code.

**Fehlersuche**

* LED leuchtet nicht:

  * Überprüfe die Orientierung der LED. Stelle sicher, dass Anode und Kathode korrekt angeschlossen sind.
  * Prüfe, ob alle Verbindungen sicher sind.
  * Stelle sicher, dass der Widerstand in Reihe mit der LED verbunden ist.

* Fehlermeldungen in Thonny:

  * Stelle sicher, dass du den richtigen Interpreter ausgewählt hast.
  * Überprüfe den Code auf Tippfehler.

**Fazit**

Glückwunsch! Du hast erfolgreich eine LED mit dem Raspberry Pi Pico und MicroPython zum Blinken gebracht. Dieses grundlegende Projekt führt dich in die Steuerung von Hardware mit Code ein und bildet die Basis für komplexere Projekte.


**Referenzen**

* |link_mpython_machine_pin|
* |link_mpython_machine|
* |link_mpython_utime|
* |link_python_while|