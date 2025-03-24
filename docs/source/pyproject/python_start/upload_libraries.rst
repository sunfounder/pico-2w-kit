
.. note::

   Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein zusammen mit anderen Begeisterten.

   **Warum beitreten?**

   - **Expertenunterstützung**: Löse Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
   - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um deine Fähigkeiten zu verbessern.
   - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
   - **Sonderangebote**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
   - **Festliche Aktionen und Verlosungen**: Nimm an Verlosungen und Feiertagsaktionen teil.

   👉 Bereit, mit uns zu erkunden und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt heute bei!

.. _add_libraries_py:

1.4 Bibliotheken auf den Pico hochladen
=============================================

In einigen Projekten benötigst du zusätzliche Bibliotheken. Deshalb laden wir diese Bibliotheken zuerst auf den Raspberry Pi Pico 2 W hoch, damit wir später den Code direkt ausführen können.

#. Lade den relevanten Code über den unten stehenden Link herunter.


   * :download:`SunFounder Pico 2 W Starter Kit <https://github.com/sunfounder/pico-2w-kit/archive/refs/heads/main.zip>`


#. Öffne die Thonny IDE und verbinde den Pico mit deinem Computer über ein Micro-USB-Kabel. Klicke dann in der rechten unteren Ecke auf den Interpreter "MicroPython (Raspberry Pi Pico).COMXX".

    .. image:: img/sec_inter.png

#. Klicke in der oberen Navigationsleiste auf **Ansicht** -> **Dateien**.

    .. image:: img/th_files.png

#. Wechsle den Pfad zu dem Ordner, in dem du das `Codepaket <https://github.com/sunfounder/pico-2w-kit/archive/refs/heads/main.zip>`_ heruntergeladen hast, und gehe dann zum Ordner ``pico-2w-kit-main/micropython/libs``.

    .. image:: img/th_path.png

#. Wähle alle Dateien oder Ordner im Ordner ``libs/`` aus, klicke mit der rechten Maustaste und klicke auf **Hochladen auf**, es dauert eine Weile, bis der Upload abgeschlossen ist.

    .. image:: img/th_upload.png

#. Jetzt siehst du die Dateien, die du gerade in deinem Laufwerk ``Raspberry Pi Pico`` hochgeladen hast.

    .. image:: img/th_done.png