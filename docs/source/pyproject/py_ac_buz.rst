.. note:: 

    Hallo und herzlich willkommen in der SunFounder-Community für Raspberry Pi-, Arduino- und ESP32-Enthusiasten auf Facebook! Tauche gemeinsam mit anderen Technikbegeisterten noch tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum beitreten?**

    - **Expertenunterstützung**: Erhalte Hilfe bei technischen Problemen und Fragen nach dem Kauf – direkt von unserem Team und der Community.
    - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um deine Fähigkeiten zu erweitern.
    - **Exklusive Einblicke**: Erfahre als Erster von neuen Produkten und erhalte exklusive Vorschauen.
    - **Spezielle Rabatte**: Profitiere von exklusiven Angeboten für unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nimm an spannenden Gewinnspielen und saisonalen Aktionen teil.

    👉 Bereit, gemeinsam mit uns Neues zu entdecken und zu entwickeln? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _py_ac_buz:

3.1 Piepen
==================


In dieser Lektion lernst du, wie du einen **Buzzer** mit dem Raspberry Pi Pico 2 W zum Piepen bringst. Ein Buzzer ist – ähnlich wie eine LED – ein digitales Ausgabegerät und lässt sich sehr einfach steuern. Für dieses Projekt verwenden wir einen **aktiven Buzzer**, der bei einem Steuersignal automatisch einen Ton erzeugt.

* :ref:`cpn_buzzer`

**Was ist ein aktiver Buzzer?**

Ein aktiver Buzzer enthält einen integrierten Oszillator, der seine Anwendung vereinfacht. Um einen Ton zu erzeugen, genügt ein einfaches Steuersignal – eine komplexe Frequenzsteuerung ist nicht nötig. Das unterscheidet ihn vom **passiven Buzzer**, der ein externes Signal zur Tonerzeugung benötigt.

|img_buzzer|

**Benötigte Komponenten**

Für dieses Projekt werden die folgenden Bauteile benötigt. 

Ein komplettes Kit ist besonders praktisch – hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ENTHALTENE TEILE
        - LINK
    *   - Pico 2 W Starter Kit	
        - 450+
        - |link_pico2w_kit|

Du kannst die Bauteile alternativ auch einzeln über die folgenden Links beziehen:


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
        - :ref:`cpn_transistor`
        - 1 (S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_resistor`
        - 1 (1KΩ)
        - |link_resistor_buy|
    *   - 7
        - Aktiver :ref:`cpn_buzzer`
        - 1
        - 

**Schaltplan**

|sch_buzzer|

In dieser Schaltung wird der Buzzer über einen Transistor (**S8050**, NPN-Typ) mit Strom versorgt. Der Transistor verstärkt den Stromfluss, wodurch der Ton des Buzzers lauter wird, als wenn er direkt mit dem Pico verbunden wäre.

Das passiert dabei:

* **GP15** gibt ein High-Signal aus, um den Transistor zu schalten.
* Sobald der Transistor aktiviert ist, kann Strom durch den Buzzer fließen – er piept.

Ein **1kΩ-Widerstand** begrenzt den Strom und schützt so den Transistor vor Schäden.

**Verdrahtung**

Stelle sicher, dass du einen **aktiven Buzzer** verwendest. Du erkennst ihn an der versiegelten Rückseite – im Gegensatz zur offenen Leiterplatte eines passiven Buzzers.

|img_buzzer|

Damit der Buzzer funktioniert, wird ein Transistor benötigt – in unserem Fall der S8050 (NPN).

|wiring_beep|


**Programmcode schreiben**

Lass uns ein einfaches MicroPython-Programm schreiben, um den Buzzer zu steuern.

.. note::

    * Öffne die Datei ``3.1_beep.py`` aus dem Ordner ``pico-2w-kit-main/micropython`` oder kopiere den Code in Thonny. Klicke anschließend auf „Run“ oder drücke F5.
    * Achte darauf, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx.


.. code-block:: python

    import machine
    import utime

    # Initialisierung des Buzzer-Pins (GP15)
    buzzer = machine.Pin(15, machine.Pin.OUT)

    while True:
        # Schleife zum Piepen des Buzzers (4 Mal)
        for i in range(4):
            buzzer.value(1)  # Buzzer einschalten
            utime.sleep(0.3)  # 0,3 Sekunden warten
            buzzer.value(0)  # Buzzer ausschalten
            utime.sleep(0.3)  # 0,3 Sekunden warten
        utime.sleep(1)  # Längere Pause vor dem nächsten Durchlauf

Wenn der Code ausgeführt wird, solltest du Folgendes hören:

* Der Buzzer piept 4 Mal hintereinander, jeweils mit einer Pause von 0,3 Sekunden.
* Danach folgt eine längere Pause von 1 Sekunde, bevor die Sequenz erneut beginnt.

**Code-Erklärung**

#. Initialisierung des Buzzers:

   * ``buzzer = machine.Pin(15, machine.Pin.OUT)``: Setzt GP15 als Ausgang, um den Buzzer zu steuern.

#. Hauptschleife:

   * Die Schleife ``while True`` sorgt dafür, dass der Code kontinuierlich läuft.
   * Innerhalb der Schleife wird der Buzzer 4 Mal ein- (``buzzer.value(1)``) und ausgeschaltet (``buzzer.value(0)``), jeweils mit 0,3 Sekunden Pause.
   * Nach den 4 Pieptönen folgt eine 1-sekündige Pause, bevor die nächste Runde startet.

**Weitere Experimente**

* **Piepdauer ändern**: Passe die Werte von ``utime.sleep(0.3)`` an, um längere oder kürzere Töne zu erzeugen.
* **Anzahl der Pieptöne variieren**: Ändere die Anzahl der Schleifendurchläufe für mehr oder weniger Pieptöne.
* **Tastersteuerung einbauen**: Schließe einen Taster an GP14 an und erweitere den Code, sodass der Buzzer nur bei Tastendruck piept.

**Fazit**

In dieser Lektion hast du gelernt, wie man einen aktiven Buzzer mithilfe eines Transistors und des Raspberry Pi Pico 2 W steuert. Du hast damit die Grundlagen zur Nutzung digitaler Ausgabegeräte für Soundeffekte kennengelernt – ein Prinzip, das sich auch auf LEDs, Motoren und andere Komponenten übertragen lässt.
