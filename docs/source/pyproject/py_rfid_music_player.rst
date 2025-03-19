.. note::

    こんにちは！FacebookのSunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！仲間たちと一緒にRaspberry Pi、Arduino、ESP32についてさらに深く学びましょう。

    **参加する理由は？**

    - **専門的なサポート**: 当コミュニティとチームの助けを借りて、販売後の問題や技術的な課題を解決できます。
    - **学び・共有**: スキルを向上させるためのヒントやチュートリアルを交換しましょう。
    - **特別なプレビュー**: 新製品の発表やプレビューに早期アクセスできます。
    - **特別割引**: 最新製品の独占的な割引を楽しめます。
    - **フェスティブなプロモーションとプレゼント企画**: プレゼント企画やホリデープロモーションに参加できます。

    👉 私たちと一緒に探索し、創造を始める準備はできましたか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _py_music_player:

7.8 RFID音楽プレーヤー
==========================

このプロジェクトでは、Raspberry Pi Pico 2 W、MFRC522 RFIDリーダー、パッシブブザー、WS2812 RGB LEDを使用して、 **RFID音楽プレーヤー** を作成します。RFIDタグに音符を書き込んで、それを読み取り、Picoが対応するメロディを再生し、カラフルなLEDエフェクトを表示します。このプロジェクトは、RFID技術と音楽生成を組み合わせ、RFIDカードやキーフォブにメロディを保存・共有できるようにします。


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
        - :ref:`cpn_transistor`
        - 1(S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_resistor`
        - 1(1KΩ)
        - |link_resistor_buy|
    *   - 7
        - パッシブ :ref:`cpn_buzzer`
        - 1
        - |link_passive_buzzer_buy|
    *   - 8
        - :ref:`cpn_mfrc522`
        - 1
        - |link_rfid_buy|
    *   - 9
        - :ref:`cpn_ws2812`
        - 1
        - |link_ws2812_buy|

**部品の理解**

* **MFRC522 RFIDリーダーモジュール**: SPIで通信する低価格のRFIDリーダー。13.56 MHzで動作するRFIDタグへのデータの読み書きが可能です。
* **RFIDタグ/キーフォブ**: 小さなデータを保存できるパッシブデバイス。音符をこれらのタグに書き込みます。
* **パッシブブザー**: PWM信号で駆動すると音を出す電子部品。音符を再生するために使用します。
* **WS2812 RGB LED**: NeoPixelとも呼ばれ、幅広い色を表示でき、1本のデータ線で個別に制御可能なLEDです。

**回路図**

|sch_music_player|


**配線**

|wiring_rfid_music_player|


**コードの作成**

二つのスクリプトを作成します：

* ``6.5_rfid_write.py``: RFIDタグに音符を保存するスクリプト
* ``7.8_rfid_music_player.py``: 保存された音符を読み取り、メロディを再生するスクリプト

.. note::

    ここでは ``mfrc522`` フォルダ内のライブラリを使用する必要があります。Picoにアップロードされているか確認してください。詳細なチュートリアルについては :ref:`add_libraries_py` を参照してください。

#. ``6.5_rfid_write.py`` ファイルを ``pico-2w-kit-main/micropython`` から開くか、このコードをThonnyにコピーして、「Run Current Script」をクリックするか、F5キーを押して実行します。

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
                pass

        write_to_tag()

#. 実行後、シェルに ``EEFGGFEDCCDEEDD EEFGGFEDCCDEDCC`` と入力し、RFIDタグをリーダーの近くに持っていくと「喜びの歌」の楽譜が保存されます。確認メッセージ「データが正常に書き込まれました！」が表示されます。

#. ``7.8_rfid_music_player.py`` ファイルを ``pico-2w-kit-main/micropython`` から開くか、このコードをThonnyにコピーして、「Run Current Script」をクリックするか、F5キーを押して実行します。

   .. code-block:: python

        from mfrc522 import SimpleMFRC522
        import machine
        import time
        from ws2812 import WS2812
        import urandom

        # WS2812 LEDのセットアップ
        # ピン0に8個のLEDを接続
        ws = WS2812(machine.Pin(0), 8)

        # MFRC522 RFIDリーダーのセットアップ
        # SPI通信を使用してRFIDリーダーを初期化
        reader = SimpleMFRC522(spi_id=0, sck=18, miso=16, mosi=19, cs=17, rst=9)

        # ブザー音符周波数（Hz）
        NOTE_C4 = 262
        NOTE_D4 = 294
        NOTE_E4 = 330
        NOTE_F4 = 349
        NOTE_G4 = 392
        NOTE_A4 = 440
        NOTE_B4 = 494
        NOTE_C5 = 523

        # ピン15でPWMを使用してブザーを初期化
        buzzer = machine.PWM(machine.Pin(15))

        # 音符に対応する周波数のリスト
        note = [NOTE_C4, NOTE_D4, NOTE_E4, NOTE_F4, NOTE_G4, NOTE_A4, NOTE_B4, NOTE_C5]

        # 指定された周波数と継続時間でブザーを鳴らす関数
        def tone(pin, frequency, duration):
         pin.freq(frequency)  # ブザーの周波数を設定
         pin.duty_u16(30000)  # デューティ比を50%に設定
         time.sleep_ms(duration)  # 指定された時間だけ音を鳴らす
         pin.duty_u16(0)  # 音を止める

        # 指定されたインデックスのWS2812 LEDをランダムな色で点灯させる関数
        def lumi(index):
         for i in range(8):
             ws[i] = 0x000000  # 全てのLEDを消灯
         ws[index] = int(urandom.uniform(0, 0xFFFFFF))  # 指定したインデックスのLEDにランダムな色を設定
         ws.write()  # WS2812 LEDに色データを書き込む

        # 音符のテキストをインデックスにエンコードし、対応する音符を再生する関数
        words = ["C", "D", "E", "F", "G", "A", "B", "N"]  # 音符と文字をマッピング
        def take_text(text):
         string = text.replace(' ', '').upper()  # 空白を削除し、テキストを大文字に変換
         while len(string) > 0:
             index = words.index(string[0])  # テキストの最初の音符をインデックスとして取得
             tone(buzzer, note[index], 250)  # 250ミリ秒間、対応する音符を再生
             lumi(index)  # 対応する音符のLEDを点灯
             string = string[1:]  # 次の文字に進む

        # RFIDカードからデータを読み取り、保存されたメロディを再生する関数
        def read():
         print("Reading...Please place the card...")
         id, text = reader.read()  # RFIDカードからIDと保存されたテキストを読み取る
         print("ID: %s\nText: %s" % (id, text)) # IDとテキストを表示
         take_text(text)  # カードに保存されたメロディを再生

        # RFIDカードを読み取り、対応するメロディを再生
        read()


#. 実行後、コンソールには「タグをリーダーの近くに置いてください...」と表示されます。

   RFIDタグをリーダーの近くに置くと：
   
   * Picoがタグからデータを読み取ります。
   * コンソールにタグのIDとテキストが表示されます。
   * ブザーがタグに保存された音符に対応するメロディを再生します。
   * WS2812 LEDが音楽に合わせてエフェクトを点灯させます。



**コードの理解**

* RFIDとのやり取り：

  * ``SimpleMFRC522`` クラスはRFIDタグの読み書きを簡素化します。
  * **データの書き込み**: ``write_to_tag()`` ではユーザー入力をタグに書き込みます。
  * **データの読み取り**: ``read_and_play()`` ではリーダーの近くにタグを置くとデータを読み取ります。

* 音楽の再生:

  * **音符辞書**: ``note`` 文字列を周波数にマッピングします。
  * **音符の解析**: RFIDタグから取得したテキストを整形し、1文字ずつ処理します。
  * **音符の再生**: 各文字に対応する周波数がブザーで再生されます。

* LEDエフェクト：

  * **WS2812の制御**: ``ws`` オブジェクトでRGB LEDを制御。
  * **LEDの点灯**: 音符に合わせて対応するLEDを点灯させます。

* タイミング：

  * **音符の継続時間**: 各音符は300ミリ秒間再生されます。
  * **音符間の休止**: 音符の間には100ミリ秒の短い休止があります。

**さらに実験する**

* 自分だけのメロディを作成：

  * RFIDタグに異なる音符を記録。
  * C、D、E、F、G、A、B、N（休符）の音符を使用。
  * 作成した音符のRFIDタグを友達と共有。

* 音符の範囲を拡張:

  * 追加の周波数を定義することで、さらに多くのオクターブを追加します。
  * それに応じて音符辞書を更新します。

* ビジュアルの強化:

  * light_led関数を変更して、異なるLEDパターンを作成します。
  * LEDエフェクトと音楽の同期をより密にします。

* 異なる曲のための複数のタグ:

  * 異なるメロディを持つ複数のRFIDタグをプログラムします。
  * シンプルなRFIDベースの音楽ライブラリを構築します。

**制限事項の理解**

* RFIDタグのデータ保存：

  * RFIDタグの保存容量には制限があります（通常、MFRC522の場合、最大48文字）。
  * 音楽のシーケンスは簡潔に保ちましょう。

* 音質：

  * パッシブブザーは単純な音を出します。
  * より良い音質を求めるなら、DAC出力を持つアクティブスピーカーの使用を検討してください。

* RFIDタグの互換性：

  MFRC522リーダーと互換性のあるRFIDタグを使用してください。

**結論**

Raspberry Pi Pico 2 Wを使ってRFID音楽プレーヤーを作成しました！このプロジェクトは、RFID技術、音楽生成、LED制御を組み合わせて、インタラクティブで楽しい体験を提供します。RFIDタグにメロディを保存すれば、簡単に異なる曲を共有・再生できます。
