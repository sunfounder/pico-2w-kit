.. note::

    こんにちは！FacebookのSunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！仲間たちと一緒にRaspberry Pi、Arduino、ESP32についてさらに深く学びましょう。

    **参加する理由は？**

    - **専門的なサポート**: 当コミュニティとチームの助けを借りて、販売後の問題や技術的な課題を解決できます。
    - **学び・共有**: スキルを向上させるためのヒントやチュートリアルを交換しましょう。
    - **特別なプレビュー**: 新製品の発表やプレビューに早期アクセスできます。
    - **特別割引**: 最新製品の独占的な割引を楽しめます。
    - **フェスティブなプロモーションとプレゼント企画**: プレゼント企画やホリデープロモーションに参加できます。

    👉 私たちと一緒に探索し、創造を始める準備はできましたか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _py_rfid:


6.5 RFIDインターフェース
===========================================

このレッスンでは、 **無線周波数識別（RFID）** 技術をRaspberry Pi Pico 2 Wで使用する方法について学びます。RFIDは、リーダーとタグ間での無線通信を可能にし、識別、認証、データ保存に利用できます。

* :ref:`cpn_mfrc522`

**必要な部品**

このプロジェクトでは、以下の部品が必要です。

キット一式を購入するのが便利です。こちらがリンクです：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名称	
        - このキットに含まれる部品
        - リンク
    *   - Pico 2 Wスターターキット	
        - 450+
        - |link_pico2w_kit|

また、以下のリンクから個別に購入することもできます。


.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - 部品	
        - 数量
        - リンク

    *   - 1
        - :ref:`cpn_pico_2w`
        - 1
        - |link_pico2w_buy|
    *   - 2
        - Micro USBケーブル
        - 1
        - 
    *   - 3
        - :ref:`cpn_breadboard`
        - 1
        - |link_breadboard_buy|
    *   - 4
        - :ref:`cpn_wire`
        - 数本
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_mfrc522`
        - 1
        - |link_rfid_buy|

**RFIDの理解**

RFID技術は、電磁場を利用してタグを自動的に識別・追跡します。タグには電子的に保存された情報が含まれており、視線を合わせずに距離を置いて読み取ることができます。

* **RFIDリーダー（MFRC522）**: RFIDタグと通信するためにラジオ波を発するデバイスです。
* **RFIDタグ**: マイクロチップとアンテナを内蔵した小さなオブジェクトで、カードやキーフォブとして使用されます。パッシブ（バッテリーなし）またはアクティブ（バッテリー駆動）である場合があります。

**回路図**

|sch_rfid|

**配線**

|wiring_rfid|

**コードの作成**

二つのスクリプトを作成します：

.. note::

    ここでは ``mfrc522`` フォルダ内のライブラリを使用する必要があります。Picoにアップロードされているか確認してください。詳細なチュートリアルについては :ref:`add_libraries_py` を参照してください。

1. RFIDタグにデータを書き込む:

   * ``mfrc522`` ライブラリの ``SimpleMFRC522`` クラスを使用して、RFIDリーダーとのインタラクションを簡略化します。
   * リーダーは指定されたSPIピンで初期化されます。
   * ユーザーに書き込むデータの入力を促します。
   * タグをリーダーの近くに置くよう指示します。
   * ``reader.write(data)`` を使用してデータをタグに書き込みます。

   .. note::

       ``pico-2w-kit-main/micropython`` から ``6.5_rfid_write.py`` ファイルを開くか、このコードをThonnyにコピーして「Run Current Script」をクリックするか、F5キーを押して実行します。

   .. code-block:: python

        from mfrc522 import SimpleMFRC522
        from machine import Pin, SPI

        # RFIDリーダーの初期化
        reader = SimpleMFRC522(spi_id=0, sck=18, mosi=19, miso=16, cs=17, rst=9)

        def write_to_tag():
            try:
                data = input("Enter data to write to the tag: ")
                print("Place your tag near the reader...")
                reader.write(data)
                print("Data written successfully!")
            finally:
                pass  # 必要ならクリーンアップ処理

        write_to_tag()

   実行後、以下の操作が行われます：
   
   * プログラムは次のように表示します：
   
     .. code-block::
   
       タグに書き込むデータを入力してください:
   
   * RFIDタグに書き込みたいテキストを入力し、Enterを押します。
   * プログラムは次のように表示します：
   
     .. code-block::
       
       タグをリーダーの近くに置いてください...
   
   * RFIDタグをリーダーモジュールの近くに置きます。
   * データが正常に書き込まれた後、次のように表示されます：
   
     .. code-block::
   
       データが正常に書き込まれました！

2. RFIDタグからデータを読み取る:

   * ユーザーにタグをリーダーの近くに置くよう指示します。
   * ``reader.read()`` を使用してタグのIDと保存されたテキストを読み取ります。
   * タグのIDとタグから読み取ったデータを表示します。

   .. note::

       ``pico-2w-kit-main/micropython`` から ``6.5_rfid_read.py`` ファイルを開くか、このコードをThonnyにコピーして「Run Current Script」をクリックするか、F5キーを押して実行します。


   .. code-block:: python
       
       from mfrc522 import SimpleMFRC522
       from machine import Pin, SPI
       
       # RFIDリーダーの初期化
       reader = SimpleMFRC522(spi_id=0, sck=18, mosi=19, miso=16, cs=17, rst=9)
       
       def read_from_tag():
           try:
               print("Place your tag near the reader...")
               id, text = reader.read()
               print("Tag ID: {}".format(id))
               print("Data: {}".format(text.strip()))
           finally:
               pass  # 必要ならクリーンアップ処理
       
       read_from_tag()

   実行後、プログラムは「タグをリーダーの近くに置いてください...」というメッセージを表示します。
   RFIDタグをMFRC522リーダーモジュールの近くに置くと、プログラムは取得した情報をコンソールに表示します。出力は次のようになります：
   
   .. code-block:: 
   
       Tag ID: 1234567890
       Data: Your stored message

**コードの理解**

* **RFID通信**: MFRC522モジュールはラジオ波を使用してRFIDタグと通信します。タグが範囲内にあると、リーダーはタグのメモリにデータを読み書きできます。
* **SPIインターフェース**: モジュールはSPIプロトコルを介してPicoと通信し、高速なデータ転送を可能にします。
* **データ保存**: RFIDタグには限られたストレージ容量があり、IDや短いテキストなどの小さなデータを保存するのに適しています。

**応用例**

* **アクセス制御システム**: RFIDタグを鍵として使用し、ドアやデバイスを解除します。
* **在庫管理**: RFIDタグを使って倉庫や店舗でアイテムを追跡します。
* **出席システム**: RFIDタグを個人に割り当て、出席を記録します。

**さらに実験する**

* **複数のタグ**: 複数のタグに異なるデータを書き込んで、それらを読み取る実験をしてみましょう。
* **セキュリティ対策**: 不正アクセスを防ぐために基本的な認証を実装します。
* **データのフォーマット**: より複雑なアプリケーションのために、JSONやCSVなどの構造化データを保存します。

**結論**

このレッスンでは、Raspberry Pi Pico 2 Wを使用してRFIDリーダーとインターフェースし、RFIDタグにデータを読み書きする方法を学びました。この技術は、識別、追跡、自動化など、さまざまなアプリケーションに役立ちます。
