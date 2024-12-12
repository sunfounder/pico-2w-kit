.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _setup_pico2w_arduino:

1.3 Setting Up the Raspberry Pi Pico 2W (Important)
=====================================================

1. Installing the Board Package
--------------------------------------

To program the Raspberry Pi Pico 2W, you need to install the appropriate board package in the Arduino IDE. Follow these steps to get started:

#. Open the Arduino IDE and navigate to **File** -> **Preferences**.

   .. image:: img/arduino_pico_file.png

#. In the dialog that appears, enter the following URL in the "Additional Boards Manager URLs" field: ``https://github.com/earlephilhower/arduino-pico/releases/download/global/package_rp2040_index.json``.

   .. image:: img/arduino_pico_link.png

#. Open the **Boards Manager** from the menu and search for **pico**. Click the **INSTALL** button to begin the installation. This will install the **Raspberry Pi Pico /RP2040/PR2350** package, including support for Raspberry Pi Pico 2W.

   .. image:: img/arduino_pico_install.png

#. During the installation process, several pop-up prompts may appear requesting you to install specific device drivers. Choose **"Install"**.

   .. image:: img/install_pico_sa.png

#. Once the installation is complete, a notification will appear to confirm the successful setup.

2. Selecting the Board and Port
------------------------------------------

#. Hold down the **BOOTSEL** button, then unplug your Raspberry Pi Pico 2W and quickly plug it back in.

   .. image:: img/led_onboard.png
        :width: 500
        :align: center

   .. warning::
        
      * This step is crucial, especially for first-time users on the Arduino IDE. Skipping this step will result in a failed upload.
      * Once you've successfully uploaded the code, your Pico will be recognized by the computer. For future uploads, simply plug it into the computer without holding the button.

#. To select the appropriate board, go to **Tools** -> **Board** -> **Raspberry Pi Pico /RP2040/PR2350** -> **Raspberry Pi Pico 2W**.

   .. image:: img/arduino_pico_board2.jpg
      :width: 800
      :align: center

2. Next, select the correct port by navigating to **Tools** -> **Port** -> **UF2 Board**.

   .. note::
     
     * For the first connection or when holding the **BOOTSEL** button, choose **UF2 Board**.
     * After successfully uploading the code, your Pico 2W will be recognized by the computer. For future uses, select the corresponding **COMxx (Raspberry Pi Pico 2)**.

   .. image:: img/arduino_pico_port.jpg


3. Uploading Code
--------------------------

Now, let's move on to uploading code to your Raspberry Pi Pico 2w.

#. Open any ``.ino`` file, or use the blank sketch that appears by default. Then, click the **Upload** button.

   .. image:: img/install_pico_upload.jpg

#. Once the upload is complete, a confirmation prompt will appear.

   .. image:: img/install_pico_upload_done2.png

#. Your computer should now recognize the Pico 2w successfully.

   .. image:: img/arduino_pico_port_com2.png

