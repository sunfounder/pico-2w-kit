.. note:: 

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche mit Gleichgesinnten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum mitmachen?**

    - **Expertenhilfe**: Erhalte Unterstützung bei Problemen nach dem Kauf und technischen Herausforderungen durch unser Team und unsere Community.
    - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um deine Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und Vorabinfos.
    - **Sonderrabatte**: Nutze exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen & Gewinnspiele**: Nimm an Verlosungen und saisonalen Aktionen teil.

    👉 Bereit, gemeinsam mit uns zu entdecken und zu gestalten? Klicke auf [|link_sf_facebook|] und tritt der Community bei!

.. _py_iot_ble_home:

8.13 Bluetooth-Umweltsensor
==========================================

In diesem Projekt wird eine Android-App verwendet, die mit |link_appinventor| erstellt wurde, um Umweltdaten von einem Raspberry Pi Pico 2 W zu empfangen und anzuzeigen. Der Pico 2 W erfasst Temperatur- und Feuchtigkeitswerte mithilfe eines DHT11-Sensors. Diese Daten werden per Bluetooth übertragen und anschließend von der App auf dem Bildschirm dargestellt.

Die Android-App wird mit |link_appinventor| entwickelt – einer kostenlosen Online-Plattform, die sich ideal für Einsteiger in die Android-Entwicklung eignet. Dieses Projekt bietet eine ausgezeichnete Möglichkeit, die Kommunikation zwischen Mikrocontroller und Smartphone kennenzulernen.

1. Schaltung aufbauen
+++++++++++++++++++++++++++++++++

**Benötigte Komponenten**

Für dieses Projekt benötigen wir folgende Bauteile:

Ein Komplett-Kit ist sehr praktisch – hier der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ENTHALTENE TEILE
        - LINK
    *   - Pico 2 W Starter Kit	
        - 450+
        - |link_pico2w_kit|

Alternativ können die Bauteile auch einzeln über die folgenden Links erworben werden:

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
        - :ref:`cpn_dht11`
        - 1
        - \-

.. image:: img/wiring/8.13_bb.png
   :width: 90%

.. raw:: html

   <br/>

2. Android-App erstellen
+++++++++++++++++++++++++++++++++

Die App wird mit |link_appinventor| entwickelt – einer kostenlosen Webanwendung mit einer intuitiven Drag-and-Drop-Oberfläche für funktionale Android-Anwendungen.

So startest du:

#. Gehe zu |link_appinventor_login| und klicke auf „Online Tool“, um dich anzumelden. Du benötigst ein Google-Konto für den Zugang zum MIT App Inventor.

   .. image:: img/13-ai-signup.png
       :width: 90%
       :align: center

#. Nach dem Login navigierst du zu **Projects** → **Import project (.aia) from my computer** und lädst die Datei ``ble_environmental_monitor_picow.aia`` aus dem Pfad ``pico-2w-kit/micropython/iot/8.13-environmental_monitor`` hoch.

   Alternativ kannst du die Datei direkt hier herunterladen: :download:`ble_environmental_monitor_picow.aia</_static/other/ble_environmental_monitor_picow.aia>`

   .. image:: img/13-ai-import.png
        :align: center

#. Nach dem Hochladen erscheint die App-Vorlage im MIT App Inventor. Diese vorgefertigte Vorlage kann nach Belieben angepasst werden.

#. Der MIT App Inventor besteht aus zwei Hauptbereichen: **Designer** und **Blocks**. Du kannst oben rechts zwischen diesen Bereichen wechseln.

   .. image:: img/13-ai-intro-1.png

#. Der **Designer**-Bereich ermöglicht es dir, Buttons, Texte, Bildschirme und das Layout deiner App zu gestalten.

   .. image:: img/13-ai-intro-2.png
      :width: 100%

#. Im **Blocks**-Bereich kannst du die Logik und Funktionalität der App durch grafisches Programmieren definieren.

   .. image:: img/13-ai-intro-3.png
      :width: 100%

#. Um die App auf deinem Smartphone zu installieren, wechsle zum Reiter **Build**.

   .. image:: img/13-ai-intro-4.png
      :width: 60%
      :align: center

   * Erzeuge eine ``.apk``-Datei. Nach der Auswahl erscheint eine Seite, auf der du die Datei herunterladen oder per QR-Code installieren kannst. Folge der Anleitung zur App-Installation.

     Alternativ kannst du die vorgefertigte APK hier herunterladen: :download:`ble_environmental_monitor.apk</_static/other/ble_environmental_monitor_picow.apk>`

   * Wenn du die App im Google Play Store veröffentlichen möchtest, kannst du eine ``.aab``-Datei erstellen.

3. Code ausführen
+++++++++++++++++++++++++++++++++

Öffne die Datei ``8.13-environmental_monitor.py`` unter dem Pfad ``pico-2w-kit/micropython/iot/8.13-environmental_monitor`` oder kopiere den Code in deine Entwicklungsumgebung.

.. note:: 
   Dieser Code benötigt die Datei ``ble_advertising.py``. Lade sie vor dem Starten auf das Pico-Board hoch.

.. code-block:: python

   [Code unverändert]

4. App- und Bluetooth-Verbindung
++++++++++++++++++++++++++++++++++++++++++

Stelle sicher, dass die zuvor erstellte **Environmental Monitor BLE** App auf deinem Smartphone installiert ist.

#. Aktiviere Bluetooth auf deinem Smartphone.

#. Öffne die App **Environmental Monitor BLE**.

   .. image:: img/13_app_2.png
      :width: 25%
      :align: center

#. Beim ersten Start der App werden dir zwei aufeinanderfolgende Berechtigungsanfragen angezeigt. Diese sind notwendig für die Bluetooth-Funktion.

   .. image:: img/13_app_3.png
      :width: 100%
      :align: center

#. Tippe in der App auf den **Connect**-Button, um die Verbindung zum Pico 2 W herzustellen.

   .. image:: img/13_app_4.png
      :width: 55%
      :align: center

#. Auf der folgenden Seite werden alle Bluetooth-Geräte angezeigt. Wähle ``xx.xx.xx.xx.xx.xx pico2w`` aus der Liste. Die Gerätenamen werden zusammen mit ihrer MAC-Adresse angezeigt.

   .. image:: img/13_app_5.png
      :width: 60%
      :align: center

#. Falls keine Geräte angezeigt werden, aktiviere die Standortfunktion auf deinem Smartphone. (Bei manchen Android-Versionen ist Bluetooth daran gekoppelt.)

#. Nach erfolgreicher Verbindung wirst du zum Hauptbildschirm weitergeleitet, auf dem Temperatur- und Luftfeuchtigkeitswerte angezeigt werden.

   .. image:: img/13_app_7.png
      :width: 60%
      :align: center
