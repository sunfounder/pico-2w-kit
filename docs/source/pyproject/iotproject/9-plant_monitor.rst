.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community auf Facebook! Vertiefen Sie Ihr Wissen über Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Tutorials zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühen Zugang zu neuen Produktankündigungen und Einblicke.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie [|link_sf_facebook|] und treten Sie heute bei!

.. _py_iot_sunfounder_controller_plant:

8.9 Pflanzenüberwachung in @SunFounder Controller
=====================================================

Mit diesem Projekt lernen Sie, wie man ein Bewässerungssystem für Pflanzen mit der SunFounder Controller APP baut.

In der APP können Sie die aktuelle Temperatur und Luftfeuchtigkeit der Umgebung sowie den Wasserstand in Topfpflanzen überprüfen.
Um die Pflanzen zu bewässern, können Sie auch auf den Button in der APP klicken.


**Erforderliche Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Es ist definitiv praktisch, ein komplettes Kit zu kaufen, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ARTIKEL IN DIESEM KIT
        - LINK
    *   - Pico 2 W Starter Kit	
        - 450+
        - |link_pico2w_kit|

Sie können sie auch einzeln über die unten stehenden Links kaufen.

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
        - :ref:`cpn_dht11`
        - 1
        - |link_dht22_buy|
    *   - 6
        - :ref:`cpn_water_level`
        - 1
        - 
    *   - 7
        - :ref:`cpn_ta6586`
        - 1
        - 
    *   - 8
        - :ref:`cpn_lipo_charger`
        - 1
        -  
    *   - 9
        - 18650 Batterie
        - 1
        -  
    *   - 10
        - :ref:`cpn_pump`
        - 1
        -  

**Schritte**

.. note::
    Es wird empfohlen, das vorherige Projekt :ref:`py_iot_sunfounder_controller` abzuschließen, da dies Ihnen hilft, die Grundlagen der Nutzung des SunFounder Controllers zu verstehen.

#. Bauen Sie den Schaltkreis.

    .. image:: img/wiring/10.sc_2_bb.png

#. Erstellen Sie einen neuen Controller, fügen Sie die folgenden Widgets hinzu und ändern Sie deren Namen.

    .. image:: img/10_plant2.jpg
        :width: 800

#. Öffnen Sie die ``10_plant_monitor.py`` unter dem Pfad ``pico-2w-kit-main/micropython/iot``. Klicken Sie auf den **Run current script**-Button oder drücken Sie F5, um es auszuführen. Nach erfolgreicher Verbindung sehen Sie die IP von Pico 2 W.

    .. image:: img/10_plant_monitor.png


#. Kehren Sie zur SunFounder APP zurück, klicken Sie nach der Verbindung mit PicoW auf Ausführen. In der APP können Sie die Temperatur und Luftfeuchtigkeit der Umgebung sowie den Wasserstand der Topfpflanze sehen. Sie können den Button klicken, um die Topfpflanze fünf Sekunden lang zu gießen, wenn Sie denken, dass sie zu wenig Wasser hat.

    .. image:: img/10_plant2.jpg
        :width: 800

#. Wenn Sie möchten, dass dieses Skript beim Hochfahren ausgeführt wird, können Sie es als ``main.py`` auf dem Raspberry Pi Pico 2 W speichern.



**Wie funktioniert es?**

Dieses Projekt funktioniert grundsätzlich genauso wie :ref:`py_iot_sunfounder_controller`.

Zusätzlich verwendet das Projekt auch DHT11, Pumpe und Wasserstandmodul, die Details zur Verwendung dieser Komponenten finden Sie in :ref:`py_dht11`, :ref:`py_pump`, :ref:`py_water`.
