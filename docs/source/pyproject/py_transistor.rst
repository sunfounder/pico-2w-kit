.. note::
    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein zusammen mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Löse Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Promotionen und Gewinnspiele**: Nimm an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt heute bei!

.. _py_transistor:

2.15 Zwei Arten von Transistoren
==========================================

In dieser Lektion erkunden wir zwei Arten von Transistoren: den **S8050 (NPN)** und den **S8550 (PNP)**. Transistoren werden häufig als elektronische Schalter verwendet, und wir werden sehen, wie beide Typen verwendet werden können, um eine LED mit einem Knopf zu steuern.

|img_NPN&PNP|

* **NPN (S8050)**: Diese Art von Transistor ermöglicht es dem Strom, vom **Kollektor** zum **Emitter** zu fließen, wenn ein hohes Signal an der **Basis** angelegt wird.
* **PNP (S8550)**: Bei PNP-Transistoren fließt der Strom vom **Emitter** zum **Kollektor**, wenn ein niedriges Signal an der **Basis** angelegt wird.


Obwohl beide Transistoren ähnliche Zwecke erfüllen, verhalten sie sich gegenüber der Signalsteuerung entgegengesetzt. Lassen Sie uns diese Transistoren verwenden, um eine LED basierend auf der Eingabe eines Knopfes zu steuern.


:ref:`cpn_transistor`

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
        - :ref:`cpn_resistor`
        - 3(220Ω, 1KΩ, 10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 7
        - :ref:`cpn_button`
        - 1
        - |link_button_buy|
    *   - 8
        - :ref:`cpn_transistor`
        - 1(S8050/S8550)
        - |link_transistor_buy|


**Verbindungsweg für NPN (S8050) Transistor**

|sch_s8050|

In diesem Schaltkreis sendet das Drücken des Knopfes ein **hohes Signal** an den GP14-Pin. Wenn GP15 ein hohes Signal ausgibt, leitet der NPN-Transistor und lässt Strom durch die LED fließen, die dadurch aufleuchtet.


|wiring_s8050|

**Verbindungsweg für PNP(S8550) Transistor**

|sch_s8550|

Im Schaltkreis des PNP-Transistors beginnt der Knopf mit einem niedrigen Signal auf GP14 und wechselt zu hoch, wenn er gedrückt wird. Wenn GP15 ein **niedriges Signal** ausgibt, leitet der PNP-Transistor und lässt Strom fließen, wodurch die LED aufleuchtet.

|wiring_s8550|



**Schreiben des Codes**

Sowohl der NPN- als auch der PNP-Transistor können mit demselben Code gesteuert werden. Der Status des Knopfes wird gelesen und je nachdem, ob er gedrückt wird oder nicht, gibt der Pico ein hohes oder niedriges Signal an GP15 aus.

.. note::

    * Öffne die Datei ``2.15_transistor.py`` aus ``pico-2w-kit-main/micropython`` oder kopiere den Code in Thonny, dann klicke auf "Ausführen" oder drücke F5.
    * Stelle sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx.
    

.. code-block:: python

    import machine

    # Initialisiere den Knopf und die Signalpins
    button = machine.Pin(14, machine.Pin.IN)
    signal = machine.Pin(15, machine.Pin.OUT)

    while True:
        button_status = button.value()
        if button_status == 1:
            signal.value(1)  # Sende hohes Signal an den Transistor
        else:
            signal.value(0)  # Sende niedriges Signal an den Transistor


**Ergebnisse**

* NPN-Schaltung (S8050):

  Die LED leuchtet auf, wenn der Knopf gedrückt wird, da der NPN-Transistor leitet, wenn ein hohes Signal an seine Basis angelegt wird.

* PNP-Schaltung (S8550):

  Die LED leuchtet auf, wenn der Knopf losgelassen wird, da der PNP-Transistor leitet, wenn ein niedriges Signal an seine Basis angelegt wird.

Beide Schaltungen demonstrieren, wie Transistoren verwendet werden können, um den Stromfluss basierend auf verschiedenen Arten von Signalen zu steuern.

**Fazit**

Durch das Experimentieren mit diesen beiden Transistoren erhältst du ein besseres Verständnis dafür, wie NPN- und PNP-Transistoren funktionieren und wie sie in Schaltkreisen verwendet werden können, um elektronische Geräte zu steuern.
