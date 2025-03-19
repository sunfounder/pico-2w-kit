.. note:: 

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Raspberry Pi、Arduino、ESP32について、他の愛好者と一緒にさらに深く学びましょう。

    **参加する理由**

    - **専門家サポート**: 購入後の問題や技術的な課題を、コミュニティとチームのサポートで解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **限定プレビュー**: 新製品の発表や先行情報をいち早くチェックできます。
    - **特別割引**: 新しい製品に対する独占的な割引が利用できます。
    - **季節限定キャンペーンとプレゼント**: プレゼントやホリデープロモーションに参加しましょう。

    👉 私たちと一緒に探求し、創造する準備はできましたか？[|link_sf_facebook|] をクリックして、今すぐ参加しましょう！

.. _add_libraries_py:

1.4 Picoにライブラリをアップロード
===================================

一部のプロジェクトでは、追加のライブラリが必要です。そこで、まずこれらのライブラリをRaspberry Pi Pico 2 Wにアップロードし、その後直接コードを実行できるようにします。

#. 以下のリンクから関連するコードをダウンロードします。


   * :download:`SunFounder Pico 2 W Starter Kit <https://github.com/sunfounder/pico-2w-kit/archive/refs/heads/main.zip>`


#. Thonny IDEを開き、PicoをマイクロUSBケーブルでコンピュータに接続し、右下の「MicroPython (Raspberry Pi Pico).COMXX」インタプリタを選択します。

    .. image:: img/sec_inter.png

#. 上部のナビゲーションバーで、 **View** -> **Files** をクリックします。

    .. image:: img/th_files.png

#. 前にダウンロードした`コードパッケージ `code package <https://github.com/sunfounder/pico-2w-kit/archive/refs/heads/main.zip>`_ のフォルダにパスを切り替え、次に ``pico-2w-kit-main/micropython/libs`` フォルダに移動します。

    .. image:: img/th_path.png

#. ``libs/`` フォルダ内のすべてのファイルまたはフォルダを選択し、右クリックして **Upload to** をクリックします。アップロードには少し時間がかかります。

    .. image:: img/th_upload.png

#. これで、アップロードしたファイルが ``Raspberry Pi Pico`` ドライブ内に表示されるようになります。

    .. image:: img/th_done.png