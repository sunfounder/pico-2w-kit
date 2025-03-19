.. note:: 

    こんにちは、SunFounderのRaspberry Pi、Arduino、ESP32愛好者コミュニティへようこそ！ Raspberry Pi、Arduino、ESP32について、他の愛好者と一緒にさらに深く学んでいきましょう。

    **なぜ参加するべきか？**

    - **専門家サポート**：コミュニティやチームから、販売後の問題や技術的な課題の解決をサポートします。
    - **学びと共有**：ヒントやチュートリアルを交換し、スキルを向上させましょう。
    - **限定プレビュー**：新製品の発表や先行情報をいち早くゲットできます。
    - **特別割引**：最新製品に対する限定割引を楽しめます。
    - **フェスティブプロモーションとプレゼント企画**：プレゼント企画や祝祭プロモーションに参加しましょう。

    👉 一緒に探求し、創造してみませんか？ [|link_sf_facebook|] をクリックして今すぐ参加しましょう！

.. _setup_pico2w_arduino:

1.3 Raspberry Pi Pico 2 Wの設定（重要）
=====================================================

1. ボードパッケージのインストール
--------------------------------------

Raspberry Pi Pico 2 Wをプログラムするためには、Arduino IDEに適切なボードパッケージをインストールする必要があります。以下の手順で開始しましょう：

#. Arduino IDEを開き、 **ファイル** -> **環境設定** を選択します。

   .. image:: img/arduino_pico_file.png

#. 表示されたダイアログで、「追加のボードマネージャのURL」フィールドに以下のURLを入力します: ``https://github.com/earlephilhower/arduino-pico/releases/download/global/package_rp2040_index.json`` 。

   .. image:: img/arduino_pico_link.png

#. メニューから **ボードマネージャ** を開き、 **pico** を検索します。 **インストール** ボタンをクリックしてインストールを開始します。これにより、 **Raspberry Pi Pico /RP2040/PR2350** パッケージがインストールされ、Raspberry Pi Pico 2 Wのサポートも含まれます。

   .. image:: img/arduino_pico_install.png

#. インストール中に、特定のデバイスドライバをインストールするよう求められることがあります。 **「インストール」** を選択してください。

   .. image:: img/install_pico_sa.png

#. インストールが完了すると、セットアップが成功したことを確認する通知が表示されます。

2. ボードとポートの選択
------------------------------------------

#. **BOOTSEL** ボタンを押し続け、Raspberry Pi Pico 2 Wの電源を一度抜いてから素早く再接続します。

   .. image:: img/led_onboard.png
        :width: 500
        :align: center

   .. warning::

      * このステップは、Arduino IDEを初めて使用する方にとって非常に重要です。このステップを省略すると、アップロードに失敗する可能性があります。
      * コードのアップロードに成功すると、Picoはコンピュータによって認識されます。次回以降はボタンを押さずにコンピュータに接続するだけで大丈夫です。

#. 適切なボードを選択するために、 **ツール** -> **ボード** -> **Raspberry Pi Pico /RP2040/PR2350** -> **Raspberry Pi Pico 2 W** を選択します。

   .. image:: img/arduino_pico_board2.jpg
      :width: 600
      :align: center

2. 次に、正しいポートを選択するために、 **ツール** -> **ポート** -> **UF2ボード** を選択します。

   .. note::

     * 初回接続時や **BOOTSEL** ボタンを押し続けている場合は、 **UF2ボード** を選択してください。
     * コードのアップロードに成功すると、Pico 2 Wはコンピュータによって認識されます。次回以降は、対応する **COMxx (Raspberry Pi Pico 2)** を選択してください。

   .. image:: img/arduino_pico_port.jpg


3. コードのアップロード
--------------------------

それでは、Raspberry Pi Pico 2 Wにコードをアップロードしましょう。

#. 任意の ``.ino`` ファイルを開くか、デフォルトで表示される空白のスケッチを使用します。そして、 **アップロード** ボタンをクリックします。

   .. image:: img/install_pico_upload1.png

#. アップロードが完了すると、確認のメッセージが表示されます。

   .. image:: img/install_pico_upload_done2.png

#. あなたのコンピュータは、Pico 2 Wを正常に認識するはずです。

   .. image:: img/arduino_pico_port_com2.png
      
