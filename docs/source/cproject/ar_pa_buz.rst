.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein, zusammen mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unserem Team.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_pa_buz:


3.2 Eigene Melodien mit einem passiven Summer spielen
=======================================================

In dieser Lektion lernen wir, wie man einen **passiven Summer** mit dem Raspberry Pi Pico 2 W verwendet, um verschiedene Töne und sogar einfache Melodien zu spielen! Im Gegensatz zu einem aktiven Summer benötigt ein passiver Summer ein sich änderndes elektrisches Signal, um Töne zu erzeugen, was bedeutet, dass wir die Tonhöhe des Sounds durch Ändern der Signalfrequenz steuern können.

* :ref:`Buzzer`

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Es ist definitiv praktisch, ein ganzes Kit zu kaufen, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ARTIKEL IN DIESEM KIT
        - KAUF-LINK
    *   - Pico 2 W Starter Kit	
        - 450+
        - |link_pico2w_kit|

Sie können sie auch separat über die untenstehenden Links kaufen.


.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - KOMPONENTENEINFÜHRUNG	
        - MENGE
        - KAUF-LINK

    *   - 1
        - :ref:`cpn_pico_2w`
        - 1
        - |link_pico2w_buy|
    *   - 2
        - Micro USB-Kabel
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
        - Passive :ref:`cpn_buzzer`
        - 1
        - |link_passive_buzzer_buy|

**Verständnis des passiven Summers**

Ein passiver Summer funktioniert wie ein kleiner Lautsprecher. Er erzeugt keinen Ton von selbst; stattdessen benötigt er ein oszillierendes Signal, um Geräusche zu machen. Indem wir Signale verschiedener Frequenzen bereitstellen, können wir den Summer dazu bringen, unterschiedliche Tonhöhen zu erzeugen, was uns ermöglicht, Noten und Melodien zu spielen.

|img_buzzer|

**Schaltplan**

|sch_buzzer|

In diesem Schaltkreis wird der passive Summer über einen Transistor (**S8050** NPN) mit Strom versorgt. Der Transistor verstärkt den Strom, was den Summer lauter klingen lässt, als wäre er direkt mit dem Pico verbunden.

Hier ist, was passiert:

* **GP15** gibt ein hohes Signal aus, um den Transistor zu steuern.
* Wenn der Transistor aktiviert ist, ermöglicht er den Stromfluss durch den Summer, was ihn piepen lässt.

Ein **1kΩ Widerstand** wird verwendet, um den Strom zu begrenzen und den Transistor zu schützen.

**Verdrahtung**

|img_buzzer|

Stellen Sie sicher, dass Sie den **passiven Summer** verwenden. Sie können erkennen, dass es der richtige ist, wenn Sie die freiliegende PCB sehen (im Gegensatz zur versiegelten Rückseite, die ein aktiver Summer ist).

|wiring_buzzer|

**Code schreiben**


.. note::

    * Sie können die Datei ``3.2_custom_tone.ino`` im Pfad ``pico-2w-kit-main/arduino/3.2_custom_tone`` öffnen. 
    * Oder kopieren Sie diesen Code in die **Arduino IDE**.
    * Vergessen Sie nicht, das Board (Raspberry Pi Pico) und den richtigen Port auszuwählen, bevor Sie auf den **Upload**-Button klicken.




.. code-block:: arduino

    const int buzzerPin = 15;  // GPIO-Pin, der mit der Basis des Transistors verbunden ist

    void setup() {
      pinMode(buzzerPin, OUTPUT);
    }

    void loop() {
      // Spielt einen Ton mit 440 Hz (A4-Note) für 1 Sekunde
      tone(buzzerPin, 440, 1000);
      delay(1000);  // Warte, bis der Ton beendet ist
      // Warte 1 Sekunde, bevor erneut gespielt wird
      delay(1000);
    }

Der Code spielt einen Ton von 440 Hz (Standard-A-Note) für 1 Sekunde, wartet 1 Sekunde und wiederholt sich dann.

* ``tone(pin, frequency, duration)``:

  * ``pin``: Der GPIO-Pin, der mit dem Summer verbunden ist (über den Transistor).
  * ``frequency``: Die Frequenz des Tons in Hertz (Hz). Höhere Frequenzen erzeugen höhere Tonhöhen.
  * ``duration (optional)``: Die Dauer, in der der Ton in Millisekunden gespielt wird.


**Eine Melodie spielen**

Erweitern wir den Code, um eine einfache Melodie zu spielen, indem wir die Noten und ihre entsprechenden Frequenzen definieren.

* Ein Array ``melody[]`` hält die Sequenz der zu spielenden Noten.
* Ein Array ``noteDurations[]`` definiert die Dauer jeder Note. Eine Dauer von 4 repräsentiert eine Viertelnote.
* Die ``for``-Schleife iteriert durch jede Note in der Melodie.

  * Berechnet die Notendauer in Millisekunden.
  * Verwendet ``tone()`` zum Spielen jeder Note.
  * Verwendet ``delay()`` zum Pausieren zwischen den Noten.
  * Ruft ``noTone()`` auf, um den Ton zu stoppen, bevor zur nächsten Note übergegangen wird.

.. code-block:: arduino

        // Definiere den Summer-Pin
        const int buzzerPin = 15;

        // Definiere Notenfrequenzen
        #define NOTE_C4  262
        #define NOTE_D4  294
        #define NOTE_E4  330
        #define NOTE_F4  349
        #define NOTE_G4  392
        #define NOTE_A4  440
        #define NOTE_B4  494
        #define NOTE_C5  523

        // Melodienoten
        int melody[] = {
          NOTE_C4, NOTE_D4, NOTE_E4, NOTE_F4,
          NOTE_G4, NOTE_A4, NOTE_B4, NOTE_C5
        };

        // Notendauern: 4 = Viertelnote, 8 = Achtelnote usw.
        int noteDurations[] = {
          4, 4, 4, 4,
          4, 4, 4, 4
        };

        void setup() {
          pinMode(buzzerPin, OUTPUT);
        }

        void loop() {
          // Iteriere über die Noten der Melodie
          for (int thisNote = 0; thisNote < 8; thisNote++) {
            int noteDuration = 1000 / noteDurations[thisNote];
            tone(buzzerPin, melody[thisNote], noteDuration);
            // Pause zwischen den Noten
            int pauseBetweenNotes = noteDuration * 1.30;
            delay(pauseBetweenNotes);
            // Stoppe den Ton
            noTone(buzzerPin);
          }
          // Füge eine Verzögerung hinzu, bevor die Melodie wiederholt wird
          delay(2000);
        }

Nach dem Hochladen des Codes sollten Sie den Summer die Melodie spielen hören. Wenn der Ton zu leise ist, stellen Sie sicher, dass alle Verbindungen sicher sind. Denken Sie daran, dass passive Summer möglicherweise keine sehr lauten Töne erzeugen.


**Mehr erfahren**

* Eigene Melodien erstellen:

  Sie können eigene Melodien erstellen, indem Sie die Arrays ``melody[]`` und ``noteDurations[]`` ändern.

* Verwendung der ``pitches.h``-Bibliothek:

  Zur Vereinfachung können Sie eine Bibliotheksdatei ``pitches.h`` einschließen, die Definitionen für viele Noten enthält.
  Erstellen Sie eine Datei namens ``pitches.h`` und fügen Sie sie in Ihr Skizzenbuch ein.
  
  .. code-block:: arduino

    #include "pitches.h"

**Weitere Erkundungen**

* Ein Lied komponieren:

  Versuchen Sie, Ihr eigenes Lied zu komponieren, indem Sie eine neue Sequenz von Noten und Dauern definieren.

* Interaktive Musik:

  Fügen Sie Tasten oder Sensoren hinzu, um die Wiedergabe der Melodie zu steuern.

* Visuelles Feedback:

  Integrieren Sie LEDs, die im Takt der gespielten Noten leuchten.

**Schlussfolgerung**

In dieser Lektion haben Sie gelernt, wie man einen passiven Summer mit dem Raspberry Pi Pico verwendet, um unterschiedliche Töne und Melodien zu spielen. Indem Sie die Frequenz des an den Summer gesendeten Signals steuern, können Sie verschiedene Tonhöhen erzeugen und Musik in Ihren Projekten erstellen.
