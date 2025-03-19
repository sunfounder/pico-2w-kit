.. note::

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32について、同じ趣味を持つ仲間ともっと深く探求しましょう。

    **参加する理由は？**

    - **専門家のサポート**: 販売後の問題や技術的な課題を、コミュニティやチームのサポートを受けて解決します。
    - **学びと共有**: スキルアップに役立つヒントやチュートリアルを交換しましょう。
    - **独占プレビュー**: 新商品の発表やちら見せに早期アクセスが可能です。
    - **特別割引**: 最新商品を独占的な割引価格でお楽しみいただけます。
    - **祭りプロモーションとギフトの抽選**: ギフトの抽選や祝日のプロモーションに参加しましょう。

    👉 一緒に探索して創造してみませんか？[|link_sf_facebook|]をクリックして今すぐ参加！

FAQ
=========

Arduino
---------------------

#. Arduino IDEでコードのアップロードに失敗した場合は？
    * PicoがArduino IDEに正しく認識されているか確認してください。ポートはCOMXX（Raspberry Pi Pico）でなければなりません。設定方法は :ref:`setup_pico2w_arduino` を参照してください。
    * ボード（Raspberry Pi Pico）やポート（COMXX（Raspberry Pi Pico））が正しく選択されているか確認してください。
    * コードが正しく、正しいボードとポートが選択されているにもかかわらず、アップロードが成功しない場合は、**アップロード** アイコンを再びクリックします。進行状況が「アップロード中...」と表示されたら、USBケーブルを抜いて、**BOOTSEL** ボタンを押しながら再度差し込むと、コードが成功裏にアップロードされます。


MicroPython
------------------

#. コードを開いて実行する方法は？
    詳しいチュートリアルは :ref:`open_run_code_py` を参照してください。

#. Raspberry Pi Pico 2 Wにライブラリをアップロードする方法は？
    詳しいチュートリアルは :ref:`add_libraries_py` を参照してください。

#. Thonny IDEにMicroPython（Raspberry Pi Pico 2 W）インタープリターのオプションがない？
    * Pico 2 WがUSBケーブルでコンピュータに接続されているか確認してください。
    * Pico 2 W用のMicroPythonがインストールされているか確認してください（:ref:`install_micropython_on_pico`）。
    * Raspberry Pi Pico 2 Wのインタープリターは、Thonnyのバージョン3.3.3以降でのみ利用可能です。古いバージョンを使用している場合は、アップデートしてください（:ref:`thonny_ide`）。
    * Li-poチャージャーモジュールがブレッドボードに接続されている場合は、一度それを外してからPico 2 Wをコンピュータに再接続してください。

#. Thonny IDEを使用してPico 2 Wのコードを開くことができない、またはPico 2 Wにコードを保存できない？
    * Pico 2 WがUSBケーブルでコンピュータに接続されているか確認してください。
    * インタープリタとして **MicroPython (Raspberry Pi Pico)**  が選択されているか確認してください。

#. Raspberry Pi Pico2 WをThonnyとArduinoで同時に使用することはできますか？
    いいえ、異なる操作が必要です。

    * Arduinoで使用した後にThonny IDEで使用したい場合は、Picoに :ref:`install_micropython_on_pico` をインストールする必要があります。
    * Thonnyで使用した後にArduino IDEで使用したい場合は、 :ref:`setup_pico2w_arduino` を設定する必要があります。
    
.. #. If your computer is win7 and Pico 2 W cannot be detected.
    * Download the USB CDC driver from http://aem-origin.microchip.com/en-us/mindi-sw-library?swsearch=Atmel%2520USB%2520CDC%2520Virtual%2520COM%2520Driver
    * Unzip the ``amtel_devices_cdc.inf`` file to a folder named ``pico-serial``.
    * Change the name of ``amtel_devices_cdc.inf`` file to ``pico-serial.inf``.
    * Open/edit the ``pico-serial.inf`` in a basic editor like notepad
    * Remove and replace the lines under the following headings:

    .. code-block::

        [DeviceList]
        %PI_CDC_PICO%=DriverInstall, USB\VID_2E8A&PID_0005&MI_00

        [DeviceList.NTAMD64]
        %PI_CDC_PICO%=DriverInstall, USB\VID_2E8A&PID_0005&MI_00

        [DeviceList.NTIA64]
        %PI_CDC_PICO%=DriverInstall, USB\VID_2E8A&PID_0005&MI_00

        [DeviceList.NT]
        %PI_CDC_PICO%=DriverInstall, USB\VID_2E8A&PID_0005&MI_00

        [Strings]
        Manufacturer = "ATMEL, Inc."
        PI_CDC_PICO = "Pi Pico Serial Port"
        Serial.SvcDesc = "Pi Pico Serial Driver"

    #. Close and save and make sure your retain the name as pico-serial.inf
    #. Go to your pc device list, find the pico under Ports, named something like CDC Device. A yellow exclamation mark indicates it.
    #. Right click on the CDC Device and update or install driver choosing the file you created from the location you saved it at.




.. Piper Make
.. ------------------

.. #. How to set up the Pico 2 W on Piper Make?
    For detailed tutorials, please refer to :ref:`per_setup_pico`.

.. #. How to download or import code?
    For detailed tutorials, please refer to :ref:`per_save_import`.

.. #. How to connect to Pico 2 W?
    For detailed tutorials, please refer to :ref:`connect_pico_per`.


