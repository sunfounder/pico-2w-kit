.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche gemeinsam mit anderen Technikbegeisterten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum solltest du mitmachen?**

    - **Expertenhilfe**: Erhalte Unterstützung bei technischen Fragen und Problemen nach dem Kauf – durch unser Team und die Community.
    - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um dein Wissen zu erweitern.
    - **Exklusive Einblicke**: Erfahre frühzeitig von Produktneuheiten und erhalte exklusive Vorschauen.
    - **Spezielle Rabatte**: Profitiere von exklusiven Angeboten auf unsere neuesten Produkte.
    - **Feiertagsaktionen & Gewinnspiele**: Nimm an saisonalen Aktionen und Verlosungen teil.

    👉 Bereit, gemeinsam mit uns Neues zu entdecken und zu entwickeln? Klicke auf [|link_sf_facebook|] und werde Teil unserer Community!

.. _py_bubble_level:

7.12 Bau einer digitalen Wasserwaage
==========================================

In diesem Projekt erstellen wir eine **digitale Wasserwaage** mithilfe des Raspberry Pi Pico 2 W, eines MPU6050-Beschleunigungs- und Gyroskopsensors sowie einer 8x8-LED-Matrix, die über zwei 74HC595-Schieberegister gesteuert wird. Dieses Gerät funktioniert ähnlich wie eine klassische Wasserwaage und zeigt die Neigung einer Oberfläche an. Wenn der MPU6050 geneigt wird, bewegt sich eine „Blase“ auf der LED-Matrix entsprechend, sodass die Ausrichtung der Oberfläche visualisiert werden kann.

**Benötigte Komponenten**

Für dieses Projekt werden folgende Bauteile benötigt:

Ein Komplett-Kit ist besonders praktisch – hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name
        - ENTHALTENE TEILE
        - LINK
    *   - Pico 2 W Starter Kit
        - 450+
        - |link_pico2w_kit|

Die Komponenten sind auch einzeln erhältlich:


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
        - :ref:`cpn_dot_matrix`
        - 1
        - 
    *   - 6
        - :ref:`cpn_74hc595`
        - 2
        - |link_74hc595_buy|
    *   - 7
        - :ref:`cpn_mpu6050`
        - 1
        - 

**Verständnis der Komponenten**

* **MPU6050-Beschleunigungsmesser und Gyroskop**: Liefert Beschleunigungs- und Winkelgeschwindigkeitsdaten entlang der drei Achsen (X, Y, Z), mit denen wir die Neigungswinkel berechnen.
* **8x8-LED-Matrix**: Eine Anordnung aus 8 Reihen und 8 Spalten von LEDs, mit der sich Muster oder Bilder darstellen lassen.
* **74HC595-Schieberegister**: Ermöglicht die Steuerung mehrerer Ausgänge (hier: Reihen und Spalten der LED-Matrix) mit weniger GPIO-Pins des Pico.

**Schaltplan**

|sch_bubble_level|

Der MPU6050 misst die Beschleunigung in jeder Richtung und berechnet daraus den Neigungswinkel.

Das Programm zeichnet daraufhin einen 2x2-Punkt auf die LED-Matrix basierend auf den Daten der beiden 74HC595-Chips.

Wenn sich der Neigungswinkel ändert, sendet das Programm aktualisierte Daten an die 74HC595-Chips, wodurch sich die Position der „Blase“ verändert.

**Verdrahtung**


|wiring_digital_bubble_level|


**Code schreiben**

Wir schreiben ein MicroPython-Skript, das:

* Beschleunigungsdaten vom MPU6050 ausliest,
* die Neigungswinkel entlang der X- und Y-Achse berechnet,
* diese Werte auf Positionen in der 8x8-LED-Matrix abbildet,
* eine „Blase“ (2x2-Pixel) anzeigt, die sich entsprechend der Neigung bewegt.

.. note::

    * Öffne die Datei ``7.12_digital_bubble_level.py`` aus dem Ordner ``pico-2w-kit-main/micropython`` oder kopiere den Code in Thonny und klicke auf „Run“ oder drücke F5.
    * Stelle sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico) COMxx.
    * Es werden die Bibliotheken ``imu.py`` und ``vector3d.py`` benötigt. Überprüfe, ob sie auf den Pico hochgeladen wurden. Eine Anleitung dazu findest du unter :ref:`add_libraries_py`.

.. code-block:: python
      
    import machine
    from machine import I2C, Pin
    import time
    import math
    from imu import MPU6050

    # I2C-Kommunikation mit dem MPU6050-Sensor initialisieren
    i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)
    mpu = MPU6050(i2c)

    # Funktion zur Berechnung der Distanz zwischen zwei Punkten
    def dist(a, b):
        return math.sqrt((a * a) + (b * b))

    # Funktion zur Berechnung der Rotation entlang der Y-Achse
    def get_y_rotation(x, y, z):
        radians = math.atan2(x, dist(y, z))
        return -math.degrees(radians)

    # Funktion zur Berechnung der Rotation entlang der X-Achse
    def get_x_rotation(x, y, z):
        radians = math.atan2(y, dist(x, z))
        return math.degrees(radians)

    # Funktion zur Ermittlung der aktuellen Winkelwerte des MPU6050-Sensors
    def get_angle():
        y_angle = get_y_rotation(mpu.accel.x, mpu.accel.y, mpu.accel.z)
        x_angle = get_x_rotation(mpu.accel.x, mpu.accel.y, mpu.accel.z)
        return x_angle, y_angle

    # Pins für das Schieberegister zur Steuerung der LED-Matrix initialisieren
    sdi = machine.Pin(18, machine.Pin.OUT)
    rclk = machine.Pin(19, machine.Pin.OUT)
    srclk = machine.Pin(20, machine.Pin.OUT)

    # Funktion zum Laden von Daten in das Schieberegister
    def hc595_in(dat):
        for bit in range(7, -1, -1):
            srclk.low()
            time.sleep_us(30)
            sdi.value(1 & (dat >> bit))
            time.sleep_us(30)
            srclk.high()

    # Funktion zur Ausgabe der Daten vom Schieberegister an die LED-Matrix
    def hc595_out():
        rclk.high()
        time.sleep_us(200)
        rclk.low()

    # Funktion zur Darstellung eines 8x8-Glyphs auf der LED-Matrix
    def display(glyph):
        for i in range(0, 8):
            hc595_in(glyph[i])
            hc595_in(0x80 >> i)
            hc595_out()

    # Umwandlung einer 2D-Matrix in ein darstellbares Glyph für die LED-Matrix
    def matrix_2_glyph(matrix):
        glyph = [0 for i in range(8)]
        for i in range(8):
            for j in range(8):
                glyph[i] += matrix[i][j] << j
        return glyph

    # Begrenzung eines Werts auf ein definiertes Minimum und Maximum
    def clamp_number(val, min_val, max_val):
        return min_val if val < min_val else max_val if val > max_val else val

    # Umrechnung eines Werts von einem Bereich in einen anderen
    def interval_mapping(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    # Berechnung der Position der Blase in der Matrix basierend auf den MPU6050-Daten
    sensitivity = 4  # Empfindlichkeit der Blasenbewegung
    matrix_range = 7  # Matrixgröße ist 8x8, daher Bereich 0-7
    point_range = matrix_range - 1  # Position der Blase sollte zwischen 0 und 6 liegen

    # Funktion zur Bestimmung der Blasenposition basierend auf Sensordaten
    def bubble_position():
        y, x = get_angle()  # Aktuelle Rotationswinkel abrufen
        x = int(clamp_number(interval_mapping(x, 90, -90, 0 - sensitivity, point_range + sensitivity), 0, point_range))
        y = int(clamp_number(interval_mapping(y, -90, 90, point_range + sensitivity, 0 - sensitivity), 0, point_range))
        return [x, y]

    # Darstellung der Blase (Ausschalten von 2x2 LEDs) in der Matrix
    def drop_bubble(matrix, bubble):
        matrix[bubble[0]][bubble[1]] = 0
        matrix[bubble[0] + 1][bubble[1]] = 0
        matrix[bubble[0]][bubble[1] + 1] = 0
        matrix[bubble[0] + 1][bubble[1] + 1] = 0
        return matrix

    # Hauptschleife
    while True:
        matrix = [[1 for i in range(8)] for j in range(8)]  # Leere Matrix erstellen (alle LEDs an)
        bubble = bubble_position()  # Aktuelle Blasenposition anhand der Sensordaten ermitteln
        matrix = drop_bubble(matrix, bubble)  # Blase in die Matrix einfügen
        display(matrix_2_glyph(matrix))  # Matrix auf der LED-Anzeige darstellen
        time.sleep(0.1)  # Kleine Verzögerung, um die Aktualisierungen zu verlangsamen

Wenn der Code ausgeführt wird, platziere die Schaltung auf einer ebenen Fläche.  
Die Blase (ein 2x2-Pixel-Bereich) sollte sich in der Mitte der LED-Matrix befinden.  
Neige das Breadboard oder das MPU6050-Modul.  
Beobachte, wie sich die Blase auf der LED-Matrix in die Richtung der Neigung bewegt und so eine echte Wasserwaage simuliert.

**Den Code verstehen**

Dieses Skript liest Daten von einem MPU6050-Beschleunigungs- und Gyroskopsensor aus, um die Neigung zu bestimmen, und zeigt eine „Blase“ auf einer 8x8-LED-Matrix an.

#. Importe und Initialisierungen:

   * ``machine``: Zugriff auf die Hardware des Mikrocontrollers.
   * ``I2C``, ``Pin``: Für I2C-Kommunikation und GPIO-Steuerung.
   * ``time``: Verzögerungsfunktionen.
   * ``math``: Mathematische Berechnungen.
   * ``MPU6050`` aus ``imu``: Bibliothek für die Kommunikation mit dem MPU6050-Sensor.

#. I2C-Initialisierung:

   * Kommunikation über Bus 1 mit SDA auf Pin 6 und SCL auf Pin 7.
   * Frequenz auf 400 kHz für schnelle Datenübertragung.
   * Erstellung eines ``mpu``-Objekts zur Interaktion mit dem MPU6050.

#. Mathematische Funktionen:

   * ``dist(a, b)`` Funktion:

     * Berechnet die euklidische Distanz zwischen zwei Werten.
     * Wird zur Bestimmung der Magnitude-Komponente in Winkelberechnungen verwendet.

   * ``get_y_rotation(x, y, z)``:
     
     * Berechnet die Rotation um die Y-Achse in Grad.
     * Verwendet ``math.atan2``, um den Arkustangens von x und die Distanz zwischen y und z zu berechnen.
     * Das Ergebnis wird negiert, um die gewünschte Ausrichtung zu erhalten.

   * ``get_x_rotation(x, y, z)``:

     * Berechnet die Rotation um die X-Achse in Grad.
     * Ähnlich wie ``get_y_rotation``, jedoch wird der Arkustangens von y und die Distanz zwischen x und z berechnet.

   * ``get_angle()``:

     * Ruft die aktuellen Beschleunigungsdaten vom MPU6050-Sensor ab.
     * Berechnet die Rotationswinkel für X und Y basierend auf den Beschleunigungswerten.

#. Funktionen für das Schieberegister:

   * Pin-Definitionen:

     * ``sdi``: Serieller Dateneingang für das Schieberegister (Pin 18).
     * ``rclk``: Registertakt (Latch) für das Schieberegister (Pin 19).
     * ``srclk``: Schieberegister-Taktpin (Pin 20).

   * ``hc595_in(dat)`` Funktion:

     * Überträgt ein 8-Bit-Datenbyte in das Schieberegister.
     * Durchläuft jedes Bit von MSB zu LSB.
     * Steuert ``srclk`` und ``sdi``, um die Datenbits einzulesen.

   * ``hc595_out()``:

     * Latcht die übertragenen Daten auf die Ausgabepins des Schieberegisters.
     * Kippt den ``rclk``-Pin, um die Daten vom Schieberegister in das Speicheregister zu übertragen.

#. Funktionen für die LED-Matrix-Anzeige:

   * ``display(glyph)`` Funktion:

     * Zeigt ein 8x8-Glyph auf der LED-Matrix an.
     * Durchläuft jede Zeile des Glyphs.
     * Überträgt die Zeilendaten und den entsprechenden Spaltenselektor.
     * Ruft ``hc595_out()`` auf, um die Anzeige zu aktualisieren.

   * ``matrix_2_glyph(matrix)`` Funktion:

     * Konvertiert eine 8x8-2D-Matrix aus 0en und 1en in ein 8-Byte-Glyph.
     * Jedes Byte im Glyph repräsentiert eine Zeile in der LED-Matrix.
     * Die Bits in jedem Byte entsprechen den LEDs in der jeweiligen Zeile.

#. Hilfsfunktionen:

   * ``clamp_number(val, min_val, max_val)`` Funktion:

     * Stellt sicher, dass ``val`` innerhalb des angegebenen Bereichs ``min_val`` und ``max_val`` bleibt.
     * Verhindert, dass sich die Blase außerhalb der LED-Matrix bewegt.

   * ``interval_mapping(x, in_min, in_max, out_min, out_max)`` Funktion:

     * Ordnet einen Wert ``x`` von einem numerischen Bereich in einen anderen um.
     * Wird zur Umrechnung von Winkelmessungen auf Matrixpositionen verwendet.

#. Berechnung der Blasenposition:

   * Empfindlichkeitseinstellungen:

     * ``sensitivity = 4``: Bestimmt, wie empfindlich die Blase auf Neigungsänderungen reagiert.
     * ``matrix_range = 7``: Der maximale Index für die 8x8-Matrix (0 bis 7).
     * ``point_range = matrix_range - 1``: Anpassung des Bereichs, um die Blase innerhalb der Matrix zu halten (0 bis 6).

   * ``bubble_position()`` Funktion:

     * Ruft die aktuellen Rotationswinkel für X und Y ab.
     * Ordnet die Winkel mit ``interval_mapping`` den Positionen auf der LED-Matrix zu.
     * Begrenzung der Positionen, damit sie innerhalb der Matrix bleiben.

#. Blasenanzeigefunktion:

   * ``drop_bubble(matrix, bubble)`` Funktion:

     * Ändert die LED-Matrix, um die Blase an der angegebenen Position darzustellen.
     * Schaltet einen 2x2-Bereich von LEDs an den Blasenkoordinaten aus.
     * Aktualisiert die Matrix, um den visuellen Effekt einer bewegenden Blase zu erzeugen.

#. Hauptschleife:

   * Läuft kontinuierlich, um die Anzeige basierend auf den Sensordaten zu aktualisieren.
   * Initialisiert eine frische 8x8-Matrix mit allen eingeschalteten LEDs (Wert ``1``).
   * Ermittelt die aktuelle Blasenposition mit ``bubble_position()``.
   * Aktualisiert die Matrix mit ``drop_bubble()``, um die neue Position der Blase darzustellen.
   * Wandelt die Matrix mit ``matrix_2_glyph()`` in ein Glyph um.
   * Zeigt das Glyph mit ``display()`` auf der LED-Matrix an.
   * Wartet 0,1 Sekunden, bevor die nächste Aktualisierung erfolgt.

**Fehlersuche**

* LED-Matrix zeigt keine Anzeige:

  * Überprüfe alle Verbindungen zwischen den Schieberegistern und der LED-Matrix.
  * Stelle sicher, dass die Schieberegister korrekt mit dem Pico verbunden sind.
  * Prüfe, ob die Konfiguration der gemeinsamen Anode oder Kathode deiner LED-Matrix mit dem Code übereinstimmt.

* Blasenbewegung ist fehlerhaft:

  * Stelle sicher, dass der MPU6050 korrekt angeschlossen und funktionsfähig ist.
  * Überprüfe, ob der MPU6050 korrekt ausgerichtet ist.

* Programmfehler:

  * Stelle sicher, dass ``imu.py`` und ``vector3d.py`` korrekt hochgeladen wurden.
  * Prüfe den Code auf Tippfehler oder Einrückungsfehler.

**Weitere Experimente**

* Empfindlichkeit anpassen:

  Ändere die Zuordnung der Winkel zu den Positionen, um die Empfindlichkeit der Blasenbewegung anzupassen.

* Anzeigeverbesserungen:

  * Ändere die Größe oder Form der Blase.
  * Füge visuelle Effekte hinzu, z. B. Nachzieheffekte oder unterschiedliche Muster.

* Kalibrierung:

  Implementiere eine Kalibrierungsroutine, um den Nullpunkt zu setzen, wenn das Gerät auf einer unebenen Oberfläche platziert wird.

* Alternative Anzeigen:

  Verwende ein OLED- oder LCD-Display, um numerische Winkelwerte zusätzlich zur visuellen Blase anzuzeigen.

**Fazit**

Du hast erfolgreich eine digitale Wasserwaage mit dem Raspberry Pi Pico 2 W gebaut! Dieses Projekt zeigt, wie Beschleunigungssensordaten genutzt werden können, um Orientierung und Neigung zu visualisieren, sowie die Steuerung einer LED-Matrix mit Schieberegistern.

Erweitere dieses Projekt mit zusätzlichen Funktionen oder integriere es in größere Systeme!
