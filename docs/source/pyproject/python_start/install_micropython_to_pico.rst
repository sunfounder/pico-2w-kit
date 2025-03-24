.. note::
   Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein zusammen mit anderen Begeisterten.

   **Warum beitreten?**

   - **Expertenunterstützung**: Löse Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
   - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um deine Fähigkeiten zu verbessern.
   - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
   - **Sonderangebote**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
   - **Festliche Aktionen und Verlosungen**: Nimm an Verlosungen und Feiertagsaktionen teil.

   👉 Bereit, mit uns zu erkunden und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt heute bei!

.. _install_micropython_on_pico:

1.3 MicroPython auf Ihrem Pico installieren
================================================


Nun kommen wir zur Installation von MicroPython auf dem Raspberry Pi Pico.

.. Die Thonny IDE bietet eine sehr praktische Möglichkeit, dies mit einem Klick zu tun.

   .. note::
       Sie können auch die offizielle Raspberry Pi |link_micropython_pi| verwenden, indem Sie eine Firmware-Datei auf den Raspberry Pi Pico ziehen und ablegen.
       
#. Öffnen Sie die |link_raspberrypi_documention| und laden Sie die Firmware-Datei herunter.

   .. image:: img/download_pico2w_file.jpg

#. Halten Sie die **BOOTSEL**-Taste gedrückt und verbinden Sie dann den Pico über ein Micro-USB-Kabel mit dem Computer. Lassen Sie die **BOOTSEL**-Taste los, nachdem Ihr Pico als Massenspeichergerät namens **RPI-RP2350** erkannt wurde.

   .. image:: img/bootsel_onboard.png

#. Ziehen Sie die Firmware-Datei auf den Raspberry Pi Pico 2 W. Anschließend wird Ihr Pico 2 W neu starten.

   .. image:: img/drag_and_drop.jpg

.. #. Open Thonny IDE.

..    .. image:: img/set_pico1.png

.. #. Press and hold the **BOOTSEL** button and then connect the Pico to computer via a Micro USB cable. Release the **BOOTSEL** button after your Pico is mount as a Mass Storage Device called **RPI-RP2350**.

..    .. image:: img/bootsel_onboard.png

.. #. In the bottom right corner, click the interpreter selection button and select **Install Micropython**.
..
    .. note::
        If your Thonny does not have this option, please update to the latest version.

    .. image:: img/set_pico2.png

.. #. In the **Target volume**, the volume of the Pico you just plugged in will automatically appear, and in the **Micropython variant**, select **Raspberry Pi.Pico 2 W/Pico 2 WH**.

..    .. image:: img/set_pico3.png

.. #. Click the **Install** button, wait for the installation to complete and then close this page.

..    .. image:: img/set_pico4.png


Herzlichen Glückwunsch, jetzt ist Ihr Raspberry Pi Pico einsatzbereit.
