.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer ein in Raspberry Pi, Arduino und ESP32 zusammen mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Löse Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Community und unserem Team.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Promotionen und Giveaways**: Nimm an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt heute bei!

.. _py_rfid:


6.5 RFID-Schnittstelle
===========================================

In dieser Lektion werden wir die Nutzung von **Radiofrequenz-Identifikation (RFID)** Technologie mit dem Raspberry Pi Pico 2 W erforschen. RFID ermöglicht eine drahtlose Kommunikation zwischen einem Lesegerät und Tags, die für Identifikation, Authentifizierung und Datenspeicherung verwendet werden können.

* :ref:`cpn_mfrc522`

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
        - :ref:`cpn_mfrc522`
        - 1
        - |link_rfid_buy|

**Verständnis von RFID**

Die RFID-Technologie nutzt elektromagnetische Felder, um automatisch Tags zu identifizieren und zu verfolgen, die an Objekten angebracht sind. Die Tags enthalten elektronisch gespeicherte Informationen, die aus der Ferne ohne direkte Sichtlinie gelesen werden können.

* **RFID-Lesegerät (MFRC522):** Ein Gerät, das Radiowellen aussendet, um mit RFID-Tags zu kommunizieren.
* **RFID-Tag:** Ein kleines Objekt, wie eine Karte oder ein Schlüsselanhänger, das einen Mikrochip und eine Antenne enthält. Es kann passiv (ohne Batterie) oder aktiv (mit Batterie) sein.

**Schaltplan**

|sch_rfid|

**Verdrahtung**

|wiring_rfid|

**Programmierung**

Wir werden zwei separate Skripte schreiben:

.. note::

    Hier benötigst du die Bibliotheken im Ordner ``mfrc522``, bitte überprüfe, ob sie auf den Pico hochgeladen wurden, für eine detaillierte Anleitung siehe :ref:`add_libraries_py`.

1. Daten auf ein RFID-Tag schreiben:

   * Die Klasse ``SimpleMFRC522`` aus der Bibliothek ``mfrc522`` vereinfacht die Interaktionen mit dem RFID-Lesegerät.
   * Das Lesegerät wird mit den angegebenen SPI-Pins initialisiert.
   * Fordert den Benutzer auf, Daten einzugeben, die geschrieben werden sollen.
   * Weist den Benutzer an, das Tag in die Nähe des Lesegeräts zu legen.
   * Schreibt die Daten auf das Tag mit ``reader.write(data)``.

   .. note::

       Öffne die Datei ``6.5_rfid_write.py`` aus ``pico-2w-kit-main/micropython`` oder kopiere diesen Code in Thonny, dann klicke auf „Run Current Script“ oder drücke einfach F5, um es auszuführen.

   .. code-block:: python

        from mfrc522 import SimpleMFRC522
        from machine import Pin, SPI

        # Initialisiere das RFID-Lesegerät
        reader = SimpleMFRC522(spi_id=0, sck=18, mosi=19, miso=16, cs=17, rst=9)

        def write_to_tag():
            try:
                data = input("Enter data to write to the tag: ")
                print("Place your tag near the reader...")
                reader.write(data)
                print("Data written successfully!")
            finally:
                pass  # Bereinigungsaktionen, falls notwendig

        write_to_tag()

   Nach dem Start erfolgt Folgendes:
   
   * Das Programm zeigt an: 
   
     .. code-block::
   
       Enter data to write to the tag:"
   
   * Du gibst den Text ein, den du auf das RFID-Tag schreiben möchtest, und drückst Enter.
   * Das Programm zeigt dann an:
   
     .. code-block::
       
       Place your tag near the reader...
   
   * Du legst das RFID-Tag in die Nähe des Lesemoduls.
   * Nach erfolgreichem Schreiben der Daten wird angezeigt:
   
     .. code-block::
   
       Data written successfully!

2. Daten von einem RFID-Tag lesen:

   * Weist den Benutzer an, das Tag in die Nähe des Lesegeräts zu legen.
   * Liest die ID des Tags und den gespeicherten Text mit ``reader.read()``.
   * Gibt die ID des Tags und die gelesenen Daten aus.

   .. note::

       Öffne die Datei ``6.5_rfid_read.py`` aus ``pico-2w-kit-main/micropython`` oder kopiere diesen Code in Thonny, dann klicke auf „Run Current Script“ oder drücke einfach F5, um es auszuführen.


.. code-block:: python 
   
   from mfrc522 import SimpleMFRC522
   from machine import Pin, SPI

   # Initialisiere das RFID-Lesegerät
   reader = SimpleMFRC522(spi_id=0, sck=18, mosi=19, miso=16, cs=17, rst=9)

   def read_from_tag():
       try:
               print("Place your tag near the reader...")
           id, text = reader.read()
               print("Tag ID: {}".format(id))
               print("Data: {}".format(text.strip()))
       finally:
           pass  # Bereinigungsaktionen falls notwendig

   read_from_tag()

   Nach dem Start druckt das Programm die Nachricht "Place your tag near the reader..." .
   Du musst ein RFID-Tag in die Nähe des MFRC522-Lesemoduls legen, dann druckt das Programm die abgerufenen Informationen auf die Konsole. Die Ausgabe sieht folgendermaßen aus:
   
   .. code-block:: 
   
       Tag ID: 1234567890
       Data: Your stored message

**Verständnis des Codes**

* **RFID-Kommunikation**: Das MFRC522-Modul kommuniziert mittels Radiowellen mit dem RFID-Tag. Wenn das Tag in Reichweite ist, kann der Leser Daten im Speicher des Tags lesen oder schreiben.
* **SPI-Schnittstelle**: Das Modul kommuniziert über das SPI-Protokoll mit dem Pico, was einen schnellen Datentransfer ermöglicht.
* **Datenspeicherung**: RFID-Tags haben eine begrenzte Speicherkapazität, geeignet für das Speichern von kleinen Datenmengen wie IDs oder kurzen Texten.

**Anwendungen**

* **Zugangskontrollsysteme**: Verwende RFID-Tags als Schlüssel, um Türen oder Geräte zu entsperren.
* **Bestandsmanagement**: Verfolge Artikel in einem Lager oder Geschäft, indem du sie mit RFID-Tags versiehst.
* **Anwesenheitssysteme**: Erfasse die Anwesenheit, indem du RFID-Tags scanst, die Personen zugewiesen sind.

**Weiteres Experimentieren**

* **Mehrere Tags**: Versuche, unterschiedliche Daten auf mehrere Tags zu schreiben und sie zurückzulesen.
* **Sicherheitsmaßnahmen**: Implementiere eine grundlegende Authentifizierung, um unbefugten Zugriff zu verhindern.
* **Datenformatierung**: Speichere strukturierte Daten, wie JSON oder CSV, für komplexere Anwendungen.

**Fazit**

In dieser Lektion hast du gelernt, wie man ein RFID-Lesegerät mit dem Raspberry Pi Pico 2 W verbindet, um Daten von und zu RFID-Tags zu lesen und zu schreiben. Diese Technologie eröffnet zahlreiche Möglichkeiten für Anwendungen in Identifikation, Verfolgung und Automatisierung.

