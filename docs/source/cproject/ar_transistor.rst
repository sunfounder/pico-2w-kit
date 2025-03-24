.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Vertiefen Sie sich mit anderen Enthusiasten in die Welt von Raspberry Pi, Arduino und ESP32.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unserem Team.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_transistor:

2.15 Zwei Arten von Transistoren: NPN und PNP
================================================

In dieser Lektion erkunden wir zwei Arten von Transistoren: den **S8050 (NPN)** und den **S8550 (PNP)**. Transistoren werden häufig als elektronische Schalter verwendet, und wir werden sehen, wie beide Typen verwendet werden können, um eine LED mit einem Knopf zu steuern.

|img_NPN&PNP|

* **NPN (S8050)**: Dieser Transistortyp ermöglicht den Stromfluss vom **Kollektor** zum **Emitter**, wenn ein hohes Signal am **Basis** angelegt wird.
* **PNP (S8550)**: Bei PNP-Transistoren fließt der Strom vom **Emitter** zum **Kollektor**, wenn ein niedriges Signal an der **Basis** angelegt wird.


Obwohl beide Transistoren ähnliche Zwecke erfüllen, verhalten sie sich gegensätzlich in Bezug auf die Signalsteuerung. Lassen Sie uns diese Transistoren nutzen, um eine LED basierend auf einem Knopfdruck zu steuern.

:ref:`cpn_transistor`

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

Sie können sie auch einzeln über die untenstehenden Links kaufen.


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
        - Micro USB Kabel
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
        - 3 (220Ω, 1KΩ, 10KΩ)
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
        - 1 (S8050/S8550)
        - |link_transistor_buy|

**Verbindungsweg für NPN (S8050) Transistor**

|sch_s8050|

In diesem Schaltkreis sendet das Drücken des Knopfes ein **hohes Signal** zum GP14-Pin. Wenn GP15 ein hohes Signal ausgibt, leitet der NPN-Transistor, wodurch Strom durch die LED fließt und diese aufleuchtet.


|wiring_s8050|

.. 1. Verbinden Sie 3V3 und GND des Pico 2 W mit der Stromschiene des Breadboards.
.. #. Verbinden Sie das Anodenbein der LED über einen 220Ω Widerstand mit der positiven Stromschiene.
.. #. Verbinden Sie das Kathodenbein der LED mit dem **Kollektor**-Bein des Transistors.
.. #. Verbinden Sie das Basis-Bein des Transistors über einen 1kΩ Widerstand mit dem GP15-Pin.
.. #. Verbinden Sie das **Emitter**-Bein des Transistors mit der negativen Stromschiene.
.. #. Verbinden Sie eine Seite des Knopfes mit dem GP14-Pin und verwenden Sie einen 10kΩ Widerstand, um dieselbe Seite mit der negativen Stromschiene zu verbinden. Die andere Seite an die positive Stromschiene.

..     * Der Farbring des 220Ω Widerstands ist rot, rot, schwarz, schwarz und braun.
..     * Der Farbring des 1kΩ Widerstands ist braun, schwarz, schwarz, braun und braun.
..     * Der Farbring des 10kΩ Widerstands ist braun, schwarz, schwarz, rot und braun.

**Verdrahtung des PNP (S8550) Transistors**

|sch_s8550|

Bei der Schaltung des PNP-Transistors startet der Knopf mit einem niedrigen Signal auf GP14 und wechselt zu hoch, wenn gedrückt wird. Wenn GP15 ein **niedriges Signal** ausgibt, leitet der PNP-Transistor, wodurch Strom fließt und die LED aufleuchtet.

|wiring_s8550|

.. 1. Verbinden Sie 3V3 und GND des Pico 2 W mit der Stromschiene des Breadboards.
.. #. Verbinden Sie das Anodenbein der LED über einen 220Ω Widerstand mit der positiven Stromschiene.
.. #. Verbinden Sie das Kathodenbein der LED mit dem **Emitter**-Bein des Transistors.
.. #. Verbinden Sie das Basis-Bein des Transistors über einen 1kΩ Widerstand mit dem GP15-Pin.
.. #. Verbinden Sie das **Kollektor**-Bein des Transistors mit der negativen Stromschiene.
.. #. Verbinden Sie o

**Schreiben des Codes**

.. note::

    * Sie können die Datei ``2.15_transistor.ino`` unter dem Pfad ``pico-2w-kit-main/arduino/2.15_transistor`` öffnen.
    * Oder kopieren Sie diesen Code in die **Arduino IDE**.
    * Vergessen Sie nicht, das Board (Raspberry Pi Pico) und den richtigen Port vor dem Klicken auf den **Upload**-Button auszuwählen.



.. code-block:: arduino

    // Definieren der Pins
    const int buttonPin = 14;  // Knopf an GP14 angeschlossen
    const int transistorPin = 15;  // Transistorbasis an GP15 angeschlossen

    int buttonState = 0;  // Variable zur Speicherung des Knopfzustands

    void setup() {
      pinMode(buttonPin, INPUT);
      pinMode(transistorPin, OUTPUT);
    }

    void loop() {
      // Zustand des Knopfes lesen
      buttonState = digitalRead(buttonPin);

      // den Transistor steuern
      digitalWrite(transistorPin, buttonState);

      delay(10);  // Kleine Verzögerung zur Entprellung
    }

**Ergebnisse**

* Für NPN Transistor (S8050):

  Wenn Sie den Knopf drücken, sollte die LED einschalten.
  Wenn Sie den Knopf loslassen, sollte die LED ausschalten.

* Für PNP Transistor (S8550):

  Wenn Sie den Knopf drücken, sollte die LED ausschalten.
  Wenn Sie den Knopf loslassen, sollte die LED einschalten.

**Verständnis des Codes**

#. Lesen des Knopfzustands:

   Liest den aktuellen Zustand des Knopfes.

   .. code-block:: arduino

        buttonState = digitalRead(buttonPin);

#. Steuerung des Transistors:

   * **Für NPN Transistor**: Wenn der Knopf gedrückt ist (``buttonState`` ist HIGH), wird der Transistor eingeschaltet, sodass Strom fließen kann und die LED aufleuchtet.
   * **Für PNP Transistor**: Wenn der Knopf gedrückt ist (``buttonState`` ist HIGH), wird der Transistor ausgeschaltet (LOW), und wenn der Knopf nicht gedrückt ist, wird der Transistor eingeschaltet.

   .. code-block:: arduino

        digitalWrite(transistorPin, buttonState);


**Weitere Erkundungen**

* Größere Lasten steuern:

  Verwenden Sie Transistoren, um Geräte zu steuern, die mehr Strom benötigen, als der Pico direkt bereitstellen kann, wie Motoren oder Relais.

* Transistor als Verstärker:

  Erkunden Sie, wie Transistoren verwendet werden können, um Signale zu verstärken.

* Experiment mit Darlington-Paar:

  Verwenden Sie zwei Transistoren, um ein Darlington-Paar für einen höheren Stromgewinn zu erstellen.

**Fazit**

In dieser Lektion haben Sie gelernt, wie man sowohl NPN- als auch PNP-Transistoren verwendet, um eine LED mit einem Raspberry Pi Pico und einem Knopf zu steuern. Das Verständnis der Unterschiede zwischen NPN- und PNP-Transistoren ist entscheidend für das Design von Schaltungen, die Schaltvorgänge oder Verstärkungen erfordern.

