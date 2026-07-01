.. note::
    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Vertiefe dein Wissen über Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Löse Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Anleitungen zur Verbesserung deiner Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Promotionen und Gewinnspiele**: Nimm an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt heute bei!

.. _py_iot_cheerlights:

8.2 Folge den @CheerLights
=======================================

Dies ist ein romantisches Projekt, trete der |link_cheerlights| LED-Farbwechsel-Community bei, die es ermöglicht, dass LEDs weltweit gleichzeitig die Farben wechseln.

Du kannst es in eine Ecke deines Büros stellen, um dich daran zu erinnern, dass du nicht allein bist.

Du kannst @cheerlights tweeten und den Farbnamen im Tweet erwähnen. Dies wird die LEDs weltweit in die von dir angegebene Farbe ändern.

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
        - :ref:`cpn_ws2812`
        - 1
        - |link_ws2812_buy|
    *   - 6
        - :ref:`cpn_lipo_charger`
        - 1
        -  
    *   - 7
        - Power Pack
        - 1
        -  


**Schritte**

#. Baue den Schaltkreis.

    Das hier verwendete Li-po-Ladegerät versorgt deinen Schaltkreis mit Strom, sodass du das USB-Kabel abkoppeln und dein Projekt woandershin mitnehmen kannst, um zu spielen!

    .. warning:: 
        
        Stelle sicher, dass dein Li-po-Ladegerät wie im Diagramm gezeigt angeschlossen ist. Andernfalls könnte ein Kurzschluss dein Power Pack und die Schaltung beschädigen.

    .. image:: img/wiring/2.cheerlights_bb.png
        :width: 800



#. Wechsle in den Ordner, in dem du das `Codepaket <https://github.com/sunfounder/pico-2w-kit/archive/refs/heads/main.zip>`_ heruntergeladen hast, und öffne die Datei ``8.2_cheer_light.py`` unter dem Pfad ``pico-2w-kit-main/micropython/iot``.

#. Um das Skript auszuführen, klicke auf die Schaltfläche **Aktuelles Skript ausführen** oder drücke F5. Dann siehst du die verbundene Aufforderung, die IP und die Farbe (0xff0000 ist rot) in der Shell.
    .. note::

        Bevor du den Code ausführst, musst du die Skripte ``do_connect.py`` und ``secrets.py`` auf deinem Pico 2 W erstellen. Bitte beziehe dich auf :ref:`py_iot_access`, um sie zu erstellen.

    .. image:: img/2_cheerlight1.png


#. Steuere globale @CheerLights-Geräte

   - Tritt dem |link_discord_server| bei und nutze den CheerLights-Bot, um die Farbe einzustellen. Tippe einfach ``/cheerlights`` in einem der Kanäle auf dem **CheerLights Discord Server**, um den Bot zu aktivieren.

   .. image:: img/05_iot_cheerlights_1.png

   - Befolge die Anweisungen des Bots, um die Farbe einzustellen. Dies ermöglicht es dir, CheerLights-Geräte weltweit zu steuern.

   .. image:: img/05_iot_cheerlights_2.png
    
5. Nachdem das Skript ausgeführt wurde, zeigt der WS2812 RGB-Streifen eine Farbe an, manchmal ändert sich die Farbe.

6. Wenn du dieses Skript beim Start ausführen möchtest, musst du es als ``main.py`` auf dem Raspberry Pi Pico 2 W speichern, wie folgt.

    * Stoppe das laufende Skript und klicke auf **Datei** -> **Speichern unter**.

        .. image:: img/2_cheerlight2.png

    * Wähle **Raspberry Pi Pico** im aufpoppenden Fenster aus.

        .. image:: img/2_cheerlight3.png

    * Setze den Dateinamen auf ``main.py``. Ein Hinweis erscheint, wenn dieselbe Datei bereits auf deinem Pico 2 W vorhanden ist.

        .. image:: img/2_cheerlight4.png
    
    * Du kannst nun das USB-Kabel abziehen und das Li-po-Ladegerät verwenden, um den Raspberry Pi Pico 2 W zu betreiben. Stelle ihn in eine Ecke, und er wird automatisch funktionieren.


**Wie funktioniert es?**

Dieses Projekt benötigt eine Netzwerkverbindung, verwende das `network` -Modul, um dich mit dem Netzwerk zu verbinden.
Du kannst lernen, wie man das Netzwerkmodul verwendet, indem du dich auf :ref:`py_iot_access` beziehst.

.. code-block:: python

    from secrets import *
    from do_connect import *
    do_connect()

from do_connect import * : Dies importiert die Funktion `do_connect()`, die die Logik zum Verbinden mit Wi-Fi unter Verwendung des `network`-Moduls enthält. Sobald die Funktion `do_connect()` aufgerufen wird, stellt sie eine Verbindung zum in `secrets.py` angegebenen Wi-Fi-Netzwerk her. Wenn die Verbindung fehlschlägt, wird eine Ausnahme ausgelöst; wenn sie erfolgreich ist, geht es weiter.

from secrets import * : Die Datei `secrets.py` ist typischerweise eine separate Datei, die dazu dient, deine Wi-Fi-SSID, das Passwort und andere sensible Informationen (wie API-Schlüssel) zu speichern. Dies hilft, sensible Informationen nicht direkt im Hauptcode einzubetten.

Setze den WS2812 RGB-Streifen, bitte beziehe dich auf :ref:`py_neopixel` für die Nutzungsdetails.

.. code-block:: python

    import machine
    from ws2812 import WS2812
    ws = WS2812(machine.Pin(18), 8)

Jetzt benötigen wir eine Möglichkeit, die Farbe von @CheerLights zu erhalten. Es gibt ein Backend-System, das die Farbänderungen von Twitter entnimmt und sie im JSON-Format auf die URL: http://api.thingspeak.com/channels/1417/field/2/last.json postet.

Wenn du diese URL direkt in deinem Browser öffnest, siehst du etwas wie das Folgende. Alles, was wir benötigen, sind die Daten von ``field2``, die eine hexadezimale Farbkodierung als String enthalten.

.. code-block:: 

    {"created_at":"2022-08-16T06:12:44Z","entry_id":870488,"field2":"#ff00ff"}

Wir müssen das Modul ``urequests`` verwenden, um diese Daten zu erhalten, und das Modul ``json``, um diese Zeichen in ein Python-Wörterbuch umzuwandeln. 
Der folgende Code holt die neueste @CheerLights-Farbe von der URL und gibt einen Farbwert zurück, der von WS2812 verwendet werden kann.

.. code-block:: python

    def get_colour():
        url = "http://api.thingspeak.com/channels/1417/field/2/last.json"
        try:
            r = urequests.get(url)
            if r.status_code > 199 and r.status_code < 300:
                cheerlights = json.loads(r.content.decode('utf-8'))
                print(cheerlights['field2'])
                colour = int('0x'+cheerlights['field2'][1:7])#Umwandlung von String zu Integer
                r.close()
                return colour
            else:
                return None
        except Exception as e:
            print(e)
            return None

Schließlich verwenden wir eine Schleife, um den WS2812 alle 5 Sekunden arbeiten zu lassen.

.. code-block:: python

    while True:
        colour = get_colour()
        if colour is not None:
            ws.write_all(colour)
        time.sleep(5)

