.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Expertenunterstützung**: Löse Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Promotionen und Giveaways**: Nimm an Giveaways und Feiertagsaktionen teil.

    👉 Bereit zu erkunden und zu erschaffen mit uns? Klicke auf [|link_sf_facebook|] und tritt heute bei!

.. _py_music_player:

7.8 RFID-Musikspieler
==========================

In diesem Projekt werden wir einen **RFID-Musikspieler** erstellen, der den Raspberry Pi Pico 2 W, einen MFRC522 RFID-Leser, einen passiven Summer und WS2812 RGB-LEDs verwendet. Indem wir musikalische Noten auf RFID-Tags schreiben, werden diese zurückgelesen und der Pico spielt die entsprechende Melodie ab, während farbenfrohe LED-Effekte dargestellt werden. Dieses Projekt verbindet RFID-Technologie mit Musikgenerierung und ermöglicht es dir, Melodien auf RFID-Karten oder Schlüsselanhängern zu speichern und zu teilen.


**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten. 

Es ist definitiv praktisch, ein ganzes Kit zu kaufen, hier ist der Link: 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ARTIKEL IN DIESEM KIT
        - LINK
    *   - Pico 2 W Starter Kit	
        - 450+
        - |link_pico2w_kit|

Du kannst sie auch einzeln über die untenstehenden Links kaufen.


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
        - 1(S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_resistor`
        - 1(1KΩ)
        - |link_resistor_buy|
    *   - 7
        - Passiver :ref:`cpn_buzzer`
        - 1
        - |link_passive_buzzer_buy|
    *   - 8
        - :ref:`cpn_mfrc522`
        - 1
        - |link_rfid_buy|
    *   - 9
        - :ref:`cpn_ws2812`
        - 1
        - |link_ws2812_buy|

**Verständnis der Komponenten**

* **MFRC522 RFID-Lesemodul**: Ein kostengünstiger RFID-Leser, der über SPI kommuniziert. Er kann Daten von RFID-Tags bei 13,56 MHz lesen und schreiben.
* **RFID-Tags/Schlüsselanhänger**: Passive Geräte, die kleine Datenmengen speichern können. Wir werden musikalische Noten auf diese Tags schreiben.
* **Passiver Summer**: Eine elektronische Komponente, die Töne erzeugen kann, wenn sie mit einem PWM-Signal angesteuert wird. Wir werden ihn verwenden, um musikalische Noten zu spielen.
* **WS2812 RGB-LEDs**: Auch bekannt als NeoPixels, diese LEDs können eine breite Palette von Farben anzeigen und können einzeln über eine einzige Datenleitung gesteuert werden.

**Schaltplan**

|sch_music_player|


**Verdrahtung**

|wiring_rfid_music_player| 


**Programmierung**

Wir werden zwei Skripte schreiben:

* ``6.5_rfid_write.py``: Zum Speichern der musikalischen Noten auf dem RFID-Tag.
* ``7.8_rfid_music_player.py``: Zum Lesen der gespeicherten Noten und Abspielen der Melodie.

.. note::

    Hier benötigst du die Bibliotheken im ``mfrc522`` Ordner, bitte überprüfe, ob sie auf den Pico hochgeladen wurden, für eine detaillierte Anleitung siehe :ref:`add_libraries_py`.

#. Öffne die Datei ``6.5_rfid_write.py`` aus ``pico-2w-kit-main/micropython`` oder kopiere diesen Code in Thonny, dann klicke auf „Run Current Script“ oder drücke einfach F5, um es auszuführen.

   .. code-block:: python

        from mfrc522 import SimpleMFRC522
        from machine import Pin, SPI

        # Initialisiere den RFID-Leser
        reader = SimpleMFRC522(spi_id=0, sck=18, mosi=19, miso=16, cs=17, rst=9)

        def write_to_tag():
            try:
                data = input("Enter data to write to the tag: ")
                print("Place your tag near the reader...")
                reader.write(data)
                print("Data written successfully!")
            finally:
                pass

        write_to_tag()

#. Nach dem Start tippe ``EEFGGFEDCCDEEDD EEFGGFEDCCDEDCC`` in die Shell ein, dann bringe das RFID-Tag in die Nähe des Lesers, um eine Partitur von „Ode an die Freude“ zu speichern. Warte auf die Bestätigungsmitteilung: „Daten erfolgreich geschrieben!“

#. Öffne die Datei ``7.8_rfid_music_player.py`` aus ``pico-2w-kit-main/micropython`` oder kopiere diesen Code in Thonny, dann klicke auf „Run Current Script“ oder drücke einfach F5, um es auszuführen.

   .. code-block:: python

        from mfrc522 import SimpleMFRC522
        import machine
        import time
        from ws2812 import WS2812
        import urandom

        # WS2812 LED-Setup
        # Initialisiere einen 8-LED WS2812 Streifen am Pin 0
        ws = WS2812(machine.Pin(0), 8)

        # MFRC522 RFID-Leser-Setup
        # Initialisiere den RFID-Leser mit SPI an spezifischen Pins
        reader = SimpleMFRC522(spi_id=0, sck=18, miso=16, mosi=19, cs=17, rst=9)

        # Frequenzen der Noten für den Summer (in Hertz)
        NOTE_C4 = 262
        NOTE_D4 = 294
        NOTE_E4 = 330
        NOTE_F4 = 349
        NOTE_G4 = 392
        NOTE_A4 = 440
        NOTE_B4 = 494
        NOTE_C5 = 523

        # Initialisiere PWM für den Summer am Pin 15
        buzzer = machine.PWM(machine.Pin(15))

        # Liste der Notenfrequenzen, die den musikalischen Noten entsprechen
        note = [NOTE_C4, NOTE_D4, NOTE_E4, NOTE_F4, NOTE_G4, NOTE_A4, NOTE_B4, NOTE_C5]

        # Funktion zum Abspielen eines Tons auf dem Summer mit einer bestimmten Frequenz und Dauer
        def tone(pin, frequency, duration):
         pin.freq(frequency)  # Setze die Summerfrequenz
         pin.duty_u16(30000)  # Setze den Tastgrad auf 50% (ungefähr)
         time.sleep_ms(duration)  # Spiele den Ton für die angegebene Dauer
         pin.duty_u16(0)  # Stoppe den Ton, indem der Tastgrad auf 0 gesetzt wird

        # Funktion zum Beleuchten einer WS2812 LED an einem bestimmten Index mit einer zufälligen Farbe
        def lumi(index):
         for i in range(8):
             ws[i] = 0x000000  # Schalte alle LEDs aus
         ws[index] = int(urandom.uniform(0, 0xFFFFFF))  # Setze eine zufällige Farbe für die LED am gegebenen Index
         ws.write()  # Schreibe die Farbdaten an die WS2812 LEDs

        # Kodiere musikalischen Text in Indizes und spiele die entsprechenden Noten ab
        words = ["C", "D", "E", "F", "G", "A", "B", "N"]  # Zuordnung von musikalischen Noten zu Textzeichen
        def take_text(text):
         string = text.replace(' ', '').upper()  # Entferne Leerzeichen und konvertiere den Text in Großbuchstaben
         while len(string) > 0:
             index = words.index(string[0])  # Finde den Index der ersten Note im String
             tone(buzzer, note[index], 250)  # Spiele die entsprechende Note auf dem Summer für 250 ms
             lumi(index)  # Beleuchte die LED, die der Note entspricht
             string = string[1:]  # Gehe zum nächsten Zeichen im String

        # Funktion zum Lesen von der RFID-Karte und Abspielen der gespeicherten Partitur
        def read():
         print("Reading...Please place the card...")
         id, text = reader.read()  # Lies die RFID-Karte (ID und gespeicherter Text)
         print("ID: %s\nText: %s" % (id, text))  # Drucke die ID und den Text
         take_text(text)  # Spiele die Partitur aus dem auf der Karte gespeicherten Text ab

        # Starte das Lesen von der RFID-Karte und spiele die entsprechende Partitur ab
        read()



#. Nach dem Start zeigt die Konsole an: „Lege dein Tag in die Nähe des Lesers…“.

   Lege das RFID-Tag in die Nähe des Lesers:
   
   * Der Pico liest die Daten vom Tag.
   * Die Konsole zeigt die Tag-ID und den Text an.
   * Der Summer spielt die Melodie ab, die den auf dem Tag gespeicherten Noten entspricht.
   * Die WS2812 LEDs leuchten mit Effekten synchron zur Musik.

**Verständnis des Codes**

* RFID-Interaktion:

  * Die Klasse ``SimpleMFRC522`` vereinfacht das Lesen und Schreiben von RFID-Tags.
  * **Daten schreiben**: In ``write_to_tag()``, werden Benutzereingaben auf das Tag geschrieben.
  * **Daten lesen**: In ``read_and_play()``, werden Daten gelesen, wenn das Tag in der Nähe des Lesers ist.

* Musikwiedergabe:

  * **Noten-Dictionary**: Ordnet ``note``-Zeichen Frequenzen zu.
  * **Noten parsen**: Der Text vom RFID-Tag wird bereinigt und Zeichen für Zeichen iteriert.
  * **Noten abspielen**: Für jedes Zeichen wird die entsprechende Frequenz auf dem Summer gespielt.

* LED-Effekte:

  * **WS2812 Steuerung**: Das ``ws``-Objekt steuert die RGB-LEDs.
  * **LEDs beleuchten**: Für jede gespielte Note leuchtet eine LED in einer zufälligen Farbe auf.

* Timing:

  * **Notendauer**: Jede Note wird 300 Millisekunden lang gespielt.
  * **Pause zwischen den Noten**: Eine kurze Pause von 100 Millisekunden zwischen den Noten.

**Weiteres Experimentieren**

* Erstelle eigene Melodien:

  * Schreibe verschiedene musikalische Noten auf RFID-Tags.
  * Verwende die Noten C, D, E, F, G, A, B und N (für Pause).
  * Teile deine musikalischen RFID-Tags mit Freunden.

* Erweitere den Notenbereich:

  * Füge weitere Oktaven hinzu, indem du zusätzliche Frequenzen definierst.
  * Aktualisiere das Noten-Dictionary entsprechend.

* Visuelle Verbesserungen:

  * Modifiziere die Funktion `light_led` , um verschiedene LED-Muster zu erstellen.
  * Synchronisiere die LED-Effekte genauer mit der Musik.

* Mehrere Tags für verschiedene Songs:

  * Programmiere mehrere RFID-Tags mit unterschiedlichen Melodien.
  * Baue eine einfache RFID-basierte Musikbibliothek.

**Verständnis der Grenzen**

* Datenspeicher auf RFID-Tags:

  * RFID-Tags haben eine begrenzte Speicherkapazität (typischerweise bis zu 48 Zeichen für den MFRC522).
  * Halte deine musikalischen Sequenzen knapp.

* Audioqualität:

  * Passive Summer erzeugen einfache Töne.
  * Für eine bessere Klangqualität erwäge die Verwendung eines aktiven Lautsprechers mit einem DAC-Ausgang.

* RFID-Tag-Kompatibilität:

  Stelle sicher, dass deine RFID-Tags mit dem MFRC522-Leser kompatibel sind.

**Fazit**

Du hast erfolgreich einen RFID-Musikspieler mit dem Raspberry Pi Pico 2 W erstellt! Dieses Projekt kombiniert RFID-Technologie, Musikgenerierung und LED-Steuerung zu einem interaktiven und unterhaltsamen Erlebnis. Indem du Melodien auf RFID-Tags speicherst, kannst du einfach verschiedene Melodien teilen und abspielen.
