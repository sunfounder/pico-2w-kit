.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein und tausche dich mit anderen Technikbegeisterten aus.

    **Warum beitreten?**

    - **Expertenunterstützung**: Erhalte Hilfe bei technischen Herausforderungen und Fragen nach dem Kauf von unserer Community und unserem Team.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Previews.
    - **Spezielle Rabatte**: Profitiere von exklusiven Vergünstigungen für unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nimm an Verlosungen und saisonalen Promotions teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _py_lcd:

3.4 Flüssigkristallanzeige (LCD)
==================================

In dieser Lektion lernen wir, wie man ein **1602 LCD** mit dem Raspberry Pi Pico 2 W verwendet, um Text anzuzeigen. Das LCD1602 ist ein zeichenbasiertes Flüssigkristalldisplay, das 16 Zeichen auf zwei Zeilen darstellen kann. Dadurch eignet es sich ideal für Projekte, die Informationen wie Nachrichten, Sensordaten oder Statusmeldungen anzeigen müssen.

Ein direktes Anschließen eines LCDs an einen Mikrocontroller erfordert normalerweise viele GPIO-Pins, was die Funktionalität deines Projekts einschränken kann. Um dieses Problem zu lösen, verwenden wir ein LCD1602-Modul mit einer **I2C-Schnittstelle**. Das I2C-Protokoll nutzt nur zwei Datenleitungen (SDA und SCL), sodass das Display mit nur zwei GPIO-Pins gesteuert werden kann, wodurch weitere Pins für zusätzliche Sensoren oder Geräte frei bleiben.

* :ref:`cpn_i2c_lcd`


**Verständnis der I2C-Kommunikation auf dem Raspberry Pi Pico 2 W**

Der Raspberry Pi Pico 2 W unterstützt die I2C-Kommunikation über mehrere GPIO-Pins, wodurch Projekte flexibler gestaltet werden können. Er verfügt über zwei I2C-Busse, I2C0 und I2C1, die jeweils auf verschiedene Pin-Kombinationen gemappt werden können.

Hier ist eine Übersicht der I2C-fähigen Pins des Pico:

|pin_i2c|

Du kannst jedes passende Paar von SDA- und SCL-Pins für I2C0 oder I2C1 auswählen. Diese Flexibilität hilft, Konflikte mit anderen Peripheriegeräten in deinem Projekt zu vermeiden.

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
        - :ref:`cpn_i2c_lcd`
        - 1
        - |link_i2clcd1602_buy|

**Schaltplan**

|sch_lcd|

**Verdrahtung**

|wiring_lcd|

**Code schreiben**

Lass uns ein MicroPython-Programm schreiben, um Nachrichten auf dem LCD1602 anzuzeigen.

.. note::

   * Öffne die Datei ``3.4_liquid_crystal_display.py`` aus ``pico-2w-kit-main/micropython`` oder kopiere den Code in Thonny. Klicke dann auf "Run" oder drücke F5.
   * Stelle sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx.  
   * Du benötigst die Bibliothek ``lcd1602.py``. Überprüfe, ob sie auf den Pico hochgeladen wurde. Eine detaillierte Anleitung findest du unter :ref:`add_libraries_py`.

.. code-block:: python

   from machine import I2C, Pin
   from lcd1602 import LCD
   import utime

   # I2C-Kommunikation initialisieren (I2C0)
   i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)

   # LCD-Objekt erstellen
   lcd = LCD(i2c)

   # Erste Nachricht anzeigen
   lcd.clear()
   lcd.message("Hello, World!")
   utime.sleep(2)

   # Zur zweiten Zeile wechseln und eine weitere Nachricht anzeigen
   lcd.write(0, 1,"LCD1602 with I2C")  # Column 0, Line 1
   utime.sleep(5)

   # Display löschen
   lcd.clear()

Wenn der Code ausgeführt wird, siehst du:

* Die LCD-Anzeige zeigt „Hello, World!“ in der ersten Zeile.
* Nach 2 Sekunden wird in der zweiten Zeile „LCD1602 mit I2C“ angezeigt.
* Nach weiteren 5 Sekunden wird das Display gelöscht.

**Den Code verstehen**

#. **Module importieren:**

   * ``machine``: Ermöglicht den Zugriff auf die Hardware.
   * ``lcd1602``: Benutzerdefinierte Bibliothek zur Steuerung des LCDs.
   * ``utime``: Zeitbezogene Funktionen für Verzögerungen.

#. I2C-Kommunikation initialisieren:

   .. code-block:: python
   
      i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)
   
   * ``I2C(0, ...)``: Verwendet den I2C0-Bus.
   * ``sda=Pin(4)``: Setzt GP4 als SDA.
   * ``scl=Pin(5)``: Setzt GP5 als SCL.
   * ``freq=400000``: Setzt die I2C-Frequenz auf 400 kHz.

#. LCD-Objekt erstellen:

   * ``lcd = LCD(i2c)``: Erstellt eine Instanz der LCD-Klasse mit dem I2C-Objekt.

#. Nachrichten anzeigen:

   * ``lcd.clear()``: Löscht vorhandenen Text auf dem Display.
   * ``lcd.message("Hello, World!")``: Zeigt den Text „Hello, World!“ auf dem LCD an.
   * ``utime.sleep(2)``: Wartet 2 Sekunden.

#. Cursor bewegen und weitere Zeichen ausgeben:

   * ``lcd.write(0, 1,"LCD1602 with I2C")``: Wechselt zur ersten Spalte der zweiten Zeile und zeigt die Nachricht dort an.

#. Abschließende Verzögerung und Löschen des Displays:

   * ``utime.sleep(5)``: Wartet 5 Sekunden.
   * ``lcd.clear()``: Löscht das Display.

**Weitere Experimente**

* **Eigene Nachrichten anzeigen**: Ändere die Zeichenfolgen in ``lcd.message()``, um eigene Texte auf dem Display auszugeben.
* **Zeilenumbrüche nutzen**: Da das LCD1602 über zwei Zeilen verfügt, kannst du den Cursor mit ``(0, 1, message[i:i+16])`` in die zweite Zeile verschieben.
* **Lauftext erstellen**: Ein Scroll-Effekt kann erzeugt werden, indem das Display kontinuierlich in einer Schleife aktualisiert wird.

  .. code-block:: python

      from machine import I2C, Pin
      from lcd1602 import LCD
      import utime

      # I2C-Kommunikation initialisieren (I2C0)
      i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)

      # LCD-Objekt erstellen
      lcd = LCD(i2c)

      message = "Scrolling Text Demo "
      lcd.clear()
      while True:
         for i in range(len(message)):
            lcd.write(0, 0, message[i:i+16])  # Jeweils 16 Zeichen anzeigen
            utime.sleep(0.3)

**Fehlersuche**

* Falsche Zeichen oder keine Anzeige:
  * Überprüfe die Verdrahtung, insbesondere SDA- und SCL-Verbindungen.
  * Stelle sicher, dass die I2C-Adresse des LCDs korrekt ist (häufig 0x27 oder 0x3F).

* Kontrasteinstellung:
  Falls nichts auf dem Display erscheint, justiere das Kontrastpotentiometer des LCD-Moduls.

* Stromversorgung:

  Stelle sicher, dass das LCD ausreichend mit Strom versorgt wird. Wenn du 5V verwendest, verbinde es entweder mit dem VSYS-Pin des Pico (bei USB-Stromversorgung) oder mit einer externen 5V-Quelle.

* I2C-Adressen verstehen

  Falls dein LCD keine Texte anzeigt, könnte es eine andere I2C-Adresse verwenden. Du kannst die angeschlossenen Geräte im I2C-Bus scannen:

  .. code-block:: python
  
      from machine import I2C, Pin
      i2c = I2C(0, sda=Pin(4), scl=Pin(5))
      devices = i2c.scan()

      # I2C-Adressen im Hexadezimalformat ausgeben
      print("I2C addresses found:", [hex(device) for device in devices])

  Dieser Code gibt die Adressen der mit dem I2C-Bus verbundenen Geräte aus. Aktualisiere die ``lcd1602.py``-Bibliothek oder passe deinen Code an, um die korrekte Adresse zu verwenden.

**Fazit**

Du hast erfolgreich gelernt, wie du ein LCD1602-Display mit der I2C-Schnittstelle am Raspberry Pi Pico 2 steuerst! Diese Fähigkeit ermöglicht es dir, visuelle Ausgaben in deine Projekte zu integrieren und sie interaktiver sowie informativer zu gestalten.
