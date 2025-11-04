.. note:: 

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！仲間たちと一緒にRaspberry Pi、Arduino、ESP32についてさらに深く学んでみましょう。

    **Why Join?**

    - **Expert Support**: 購入後の問題や技術的な課題を、コミュニティとチームのサポートで解決できます。
    - **Learn & Share**: ヒントやチュートリアルを交換して、スキルを向上させましょう。
    - **Exclusive Previews**: 新製品の発表に早期アクセスできます。
    - **Special Discounts**: 最新製品に特別割引を提供します。
    - **Festive Promotions and Giveaways**: プレゼント企画や祝日プロモーションに参加できます。

    👉 一緒に探索し、創造を始めましょう！[|link_sf_facebook|] をクリックして、今すぐ参加しましょう！

.. _install_micropython_on_pico:

1.3 MicroPythonをPico 2 Wにインストール
==========================================


ここでは、Raspberry Pi Pico 2 WにMicroPythonをインストールする方法を紹介します。

.. .. note:: 
..     Raspberry Pi公式の |link_micropython_pi| を使って、ファームウェアファイルをRaspberry Pi Picoにドラッグアンドドロップすることでもインストールできます。
        
.. #. |link_raspberrypi_documention| を開き、ファームウェアファイルをダウンロードします。

..    .. image:: img/download_pico2w_file.jpg

.. #. **BOOTSEL** ボタンを押し続け、Micro USBケーブルでPicoをコンピュータに接続します。Picoが **RPI-RP2350** というMass Storage Deviceとしてマウントされたら、 **BOOTSEL** ボタンを放します。

..    .. image:: img/bootsel_onboard.png

.. #. ファームウェアファイルをRaspberry Pi Pico 2 Wにドラッグアンドドロップします。その後、Pico 2 Wが再起動します。

..    .. image:: img/drag_and_drop.jpg





Thonny IDEは、ワンクリックでインストールできる非常に便利な方法を提供します。
 
#. Thonny IDEを開きます。
 
   .. image:: img/set_pico1.png
        
#. **BOOTSEL** ボタンを押し続け、Micro USBケーブルでPico 2 Wをコンピュータに接続します。Pico 2 Wが **RPI-RP2350** というMass Storage Deviceとしてマウントされたら、 **BOOTSEL** ボタンを放します。
 
   .. image:: img/bootsel_onboard.png
        
#. 画面右下のインタープリタ選択ボタンをクリックし、 **Install Micropython** を選択します。
 
   

    .. note:: 

        Thonnyにこのオプションが表示されない場合は、最新バージョンに更新してください。
        
    .. image:: img/set_pico2.png
        
#. **Target volume**に、先ほど接続したPico 2 Wのボリュームが自動的に表示され、 **Micropython variant** には、 **Raspberry Pi.Pico 2 W/Pico 2 WH** を選択します。
 
   .. image:: img/set_pico2w3.png
        
#. **Install**ボタンをクリックし、インストールが完了するのを待ち、このページを閉じます。
 
   .. image:: img/set_pico2w4.png

おめでとうございます！これで、Raspberry Pi Pico 2 Wが準備完了です。
