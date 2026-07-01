.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauche tiefer in die Welt des Raspberry Pi, Arduino und ESP32 ein mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Löse Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Tutorials zur Verbesserung deiner Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalte frühen Zugang zu neuen Produktankündigungen und Einblicke.
    - **Sonderangebote**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nimm an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bist du bereit, mit uns zu erkunden und zu kreieren? Klicke auf [|link_sf_facebook|] und trete heute bei!

.. _py_iot_web_server:

8.7 Einrichtung eines Web-Servers
====================================


In diesem Artikel lernst du, wie du den Pico 2 W als Webserver einrichten kannst, der es dir ermöglicht, die Schaltung zu bedienen und Sensorablesungen über einen Browser zu erhalten.

|setup_web|

**1. Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten. 

Es ist definitiv praktisch, ein ganzes Kit zu kaufen, hier ist der Link: 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ITEMS IN THIS KIT
        - LINK
    *   - Pico 2 W Starter Kit	
        - 450+
        - |link_pico2w_kit|

Du kannst sie auch einzeln über die untenstehenden Links kaufen.


.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - COMPONENT	
        - QUANTITY
        - LINK

    *   - 1
        - :ref:`cpn_pico_2w`
        - 1
        - |link_pico2w_buy|
    *   - 2
        - Micro USB Cable
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
        - 4(1-330Ω, 2-220Ω, 1-10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_rgb`
        - 1
        - |link_rgb_led_buy|
    *   - 7
        - :ref:`cpn_thermistor`
        - 1
        - |link_thermistor_buy|
    *   - 8
        - :ref:`cpn_lipo_charger`
        - 1
        -  
    *   - 9
        - 18650 Battery
        - 1
        -  

**2. Den Schaltkreis aufbauen**

    .. warning:: 
        
        Stelle sicher, dass dein Li-po-Ladegerät wie im Diagramm gezeigt angeschlossen ist. Andernfalls könnte ein Kurzschluss deine Batterie und die Schaltung beschädigen.

.. image:: img/wiring/7.web_page_bb.png
    :width: 800


**3. Führe den Code aus**

    .. note::

        Bevor du den Code ausführst, musst du sicherstellen, dass du die Skripte „do_connect.py“ und „secrets.py“ auf deinem Pico 2 W hast. Falls nicht, siehe :ref:`py_iot_access`, um sie zu erstellen.

#. Öffne die Datei „7_web_page.py“ unter dem Pfad „pico-2w-kit-main/micropython/iot“.
#. Klicke auf den Knopf **Run current script** oder drücke F5, um es auszuführen. Nach erfolgreicher Verbindung siehst du die IP des Pico 2 W.

    .. image:: img/7_web_server.png

#. Gib die IP-Adresse des Pico 2 W in deinen Browser ein, um auf die für dieses Projekt erstellte Webseite zuzugreifen. Klicke auf einen beliebigen Button, um die Farbe der RGB-LEDs zu ändern und die Temperatur und Feuchtigkeit zu aktualisieren.

    .. image:: img/web-1.png
        :width: 500

#. Wenn du möchtest, dass dieses Skript beim Booten ausgeführt wird, kannst du es als „main.py“ auf dem Raspberry Pi Pico 2 W speichern.

**Wie funktioniert es?**

Dieses Projekt benötigt eine Netzwerkverbindung. Verwende die Methode :ref:`py_iot_access`, um dich mit dem Netzwerk zu verbinden. 

.. code-block:: python

    from secrets import *
    from do_connect import *
    
from do_connect import * : Dies importiert die Funktion `do_connect()`, die die Logik zum Verbinden mit Wi-Fi mithilfe des `network`-Moduls enthält. Sobald die Funktion `do_connect()` aufgerufen wird, stellt sie eine Verbindung zum in `secrets.py` angegebenen Wi-Fi-Netzwerk her. Scheitert die Verbindung, wird eine Ausnahme ausgelöst; ist sie erfolgreich, geht es mit dem nächsten Schritt weiter.

from secrets include * : Die Datei `secrets.py` ist normalerweise eine separate Datei, die dazu dient, dein Wi-Fi SSID, Passwort und andere sensible Informationen (wie API-Schlüssel) zu speichern. Dies hilft, sensible Informationen nicht direkt in der Hauptcode-Datei einzubetten. 

Die Webseite, die du besuchst, wird tatsächlich auf einem Server gehostet, und der Socket auf dem Server sendet die Webseite an uns, wenn wir sie besuchen.
Ein Socket ist die Art und Weise, wie ein Server auf einen Client hören kann, der sich mit ihm verbinden möchte. 

In diesem Projekt ist Pico 2 W dein Server, und dein Computer greift über einen Browser auf die auf Pico 2 W gehostete Webseite zu.

Zuerst erstellen wir einen Socket, der eine IP-Adresse und einen |link_port| benötigt.
Die Netzwerkverbindung und die Art, die IP zu erhalten, sind in :ref:`py_iot_access` beschrieben. Für den Port verwenden wir 80.
Nachdem der Socket eingerichtet wurde, geben wir ihn zurück und verwenden ihn für den nächsten Schritt.

`socket library - Python Docs <https://docs.python.org/3/library/socket.html>`_ 

.. code-block:: python

    import socket

    def open_socket(ip):
        # Einen Socket öffnen
        address = (ip, 80)
        connection = socket.socket()
        connection.bind(address)
        connection.listen(1)
        print(connection)
        return(connection)

Danach richten wir Ihren Webservice ein, bei dem der zuvor eingerichtete Socket verwendet wird.
Der folgende Code ermöglicht es deinem Pico 2 W, Zugriffsanfragen von deinem Browser zu empfangen.

.. code-block:: python

    def serve(connection):
        while True:
            client = connection.accept()[0]
            request = client.recv(1024)
            client.close()

Als Nächstes benötigst du eine HTML-Seite, um sie dem Besucher zu senden. Dieses Beispiel speichert eine einfache HTML-Seite in Form von Zeichen in der Variablen „html“.

.. note:: 
    Wenn du deine eigene HTML schreiben möchtest, kannst du Hilfe bei |link_html| erhalten.

.. code-block:: python

    def webpage(value):
        html = f"""
                <!DOCTYPE html>
                <html>
                <body>
                <form action="./red">
                <input type="submit" value="red " />
                </form>
                <form action="./green">
                <input type="submit" value="green" />
                </form>
                <form action="./blue">
                <input type="submit" value="blue" />
                </form>
                <form action="./off">
                <input type="submit" value="off" />
                </form>
                <p>Temperature is {value} degrees Celsius</p>
                </body>
                </html>
                """
        return html

Sende die HTML-Seite an den Besucher.

.. code-block:: python
    :emphasize-lines: 5,6

    def serve(connection):
        while True:
            client = connection.accept()[0]
            request = client.recv(1024)
            html=webpage(0)
            client.send(html)
            client.close()


Die Seite kann über deinen Browser aufgerufen werden, wenn du die obigen Teile kombinierst. Wenn du den Effekt sehen möchtest, führe den unten stehenden Code mit Thonny aus.

.. code-block:: python

    import machine
    import socket

    from secrets import *
    from do_connect import *

    def webpage(value):
        html = f"""
                <!DOCTYPE html>
                <html>
                <body>
                <form action="./red">
                <input type="submit" value="red " />
                </form>
                <form action="./green">
                <input type="submit" value="green" />
                </form>
                <form action="./blue">
                <input type="submit" value="blue" />
                </form>
                <form action="./off">
                <input type="submit" value="off" />
                </form>
                <p>Temperature is {value} degrees Celsius</p>
                </body>
                </html>
                """
        return html

    def open_socket(ip):
        # Einen Socket öffnen
        address = (ip, 80)
        connection = socket.socket()
        connection.bind(address)
        connection.listen(1)
        print(connection)
        return(connection)

    def serve(connection):
        while True:
            client = connection.accept()[0]
            request = client.recv(1024)
            html=webpage(0)
            client.send(html)
            client.close()

    try:
        ip=do_connect()
        if ip is not None:
            connection=open_socket(ip)
            serve(connection)
    except KeyboardInterrupt:
        machine.reset()




Wenn du den obigen Code ausführst, wirst du sehen, dass nur eine Webseite angezeigt wird, die es dir nicht ermöglicht, RGB-LEDs zu steuern oder Sensorenablesungen anzuzeigen.
Der Webservice muss weiter verfeinert werden.

Das Erste, was wir wissen müssen, ist, welche Informationen der Server erhält, wenn der Browser die Webseite aufruft. Ändere daher „serve()“ leicht ab, um „request“ zu drucken.

.. code-block:: python
    :emphasize-lines: 5,6

    def serve(connection):
        while True:
            client = connection.accept()[0]
            request = client.recv(1024)
            request = str(request)
            print(request)  
            html=webpage(0)
            client.send(html)
            client.close()

Führe das Skript erneut aus und die Shell wird folgende Nachricht drucken, wenn wir auf der Webseite eine Taste drücken.

.. code-block:: 

    b'GET /red? HTTP/1.1\r\nHost: 192.168.18.162\r\nConnection: keep-alive.......q=0.5\r\n\r\n'
    b'GET /favicon.ico HTTP/1.1\r\nHost: 192.168.18.162\r\nConnection: keep-alive.......q=0.5\r\n\r\n'
    b'GET /blue? HTTP/1.1\r\nHost: 192.168.18.162\r\nConnection: keep-alive.......q=0.5\r\n\r\n'
    b'GET /favicon.ico HTTP/1.1\r\nHost: 192.168.18.162\r\nConnection: keep-alive.......q=0.5\r\n\r\n'

Sie sind zu lang, um sie zu lesen!!!

Aber alles, was wir wirklich brauchen, ist das kleine Stück Information vor ``/red?``, ``/blue?``.
Es sagt uns, welche Taste gedrückt wurde. Also verfeinerten wir ``serve()`` ein wenig, um die Tasteninformationen zu extrahieren.

.. code-block:: python
    :emphasize-lines: 6,7,8,9

    def serve(connection):
        while True:
            client = connection.accept()[0]
            request = client.recv(1024)
            request = str(request)
            try:
                request = request.split()[1]
            except IndexError:
                pass
            print(request)  
            html=webpage(0)
            client.send(html)
            client.close()

Führe das Programm erneut aus und die Shell wird folgende Nachricht drucken, wenn wir auf der Webseite eine Taste drücken.

.. code-block:: 

    /red?
    /favicon.ico
    /blue?
    /favicon.ico
    /off?
    /favicon.ico

Dann müssen wir nur noch die Farbe der RGB-LED entsprechend dem Wert von ``request`` ändern.

.. code-block:: python

    def serve(connection):
        while True:
            client = connection.accept()[0]
            request = client.recv(1024)
            request = str(request)
            try:
                request = request.split()[1]
            except IndexError:
                pass
            
            print(request)
            
            if request == '/off?':
                red.low()
                green.low()
                blue.low()
            elif request == '/red?':
                red.high()
                green.low()
                blue.low()
            elif request == '/green?':
                red.low()
                green.high()
                blue.low()
            elif request == '/blue?':
                red.low()
                green.low()
                blue.high()
 
            html=webpage(0)
            client.send(html)
            client.close()

Das Letzte ist, den Wert des Thermistors auf der Webseite anzuzeigen (siehe :ref:`py_temp` für Details zur Verwendung des Thermistors).
Dieser Teil wird eigentlich durch die Änderung des Textes auf der HTML-Seite durchgeführt.
Wir setzen die Parameter in der Funktion ``webpage(value)`` und ändern einfach die eingehenden Parameter, um die angezeigte Zahl auf der Webseite zu ändern.

.. code-block:: python
    :emphasize-lines: 30,31

    def serve(connection):
        while True:
            client = connection.accept()[0]
            request = client.recv(1024)
            request = str(request)
            try:
                request = request.split()[1]
            except IndexError:
                pass
            
            #print(request)
            
            if request == '/off?':
                red.low()
                green.low()
                blue.low()
            elif request == '/red?':
                red.high()
                green.low()
                blue.low()
            elif request == '/green?':
                red.low()
                green.high()
                blue.low()
            elif request == '/blue?':
                red.low()
                green.low()
                blue.high()

            value='%.2f'%temperature()    
            html=webpage(value)
            client.send(html)
            client.close()





.. https://projects.raspberrypi.org/en/projects/get-started-pico-w/3