.. note:: 

    こんにちは！FacebookのSunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Raspberry Pi、Arduino、ESP32を深く学び、仲間たちと一緒に探求していきましょう。

    **なぜ参加するのか？**

    - **専門的なサポート**: コミュニティやチームのサポートで、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換し、スキルを向上させましょう。
    - **独占的な先行公開**: 新製品の発表や先取り情報に早期アクセスできます。
    - **特別割引**: 最新製品の特別割引を楽しめます。
    - **祭りのプロモーションとギブアウェイ**: ギブアウェイやホリデープロモーションに参加できます。

    👉 私たちと一緒に探索し、創造を始めましょう！[|link_sf_facebook|]をクリックして、今すぐ参加してください！

.. _py_passage_counter:

7.4 乗客カウンターの作成
=======================================================

このレッスンでは、Raspberry Pi Pico 2 W、PIR（受動型赤外線）モーションセンサー、および4桁の7セグメントディスプレイを使用して **乗客カウンター** を作成します。このデバイスは、PIRセンサーで動きを検出するたびにカウントを増加させ、7セグメントディスプレイにそのカウントを表示します。これは、公共の場所で人の流れを監視するために使用されるカウンターの動作を模倣します。


**必要な部品**

このプロジェクトに必要な部品は以下の通りです。

全ての部品がセットになったキットを購入するのが便利です。こちらのリンクをご参照ください：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前    
        - このキットのアイテム
        - リンク
    *   - Pico 2 Wスターターキット    
        - 450+
        - |link_pico2w_kit|

また、以下のリンクから部品を個別に購入することもできます。


.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - コンポーネント    
        - 数量
        - リンク

    *   - 1
        - :ref:`cpn_pico_2w`
        - 1
        - |link_pico2w_buy|
    *   - 2
        - マイクロUSBケーブル
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
        - :ref:`cpn_resistor`
        - 4(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_4_dit_7_segment`
        - 1
        - 
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|
    *   - 8
        - :ref:`cpn_pir`
        - 1
        - |link_pir_buy|

**コンポーネントの理解**

* **PIRモーションセンサー**: センサーの視野内の物体から放射される赤外線（IR）を測定して動きを検出します。動きを検出すると、HIGH信号を出力します。
* **4桁7セグメントディスプレイ**: 0000から9999までの数字を表示できます。シフトレジスタを使用して、GPIOピンを少なくしてディスプレイを制御します。
* **74HC595シフトレジスタ**: 8ビットのシリアルイン・パラレルアウトシフトレジスタで、出力ラッチを備えています。これにより、少ないGPIOピンで複数の出力を制御できます。

**回路図**

|sch_passager_counter| 

* この回路は :ref:`py_74hc_4dig` を基に、PIRモジュールを追加したものです。
* PIRは、誰かが通過すると約2.8秒間の高信号を送ります。
* PIRモジュールには2つのポテンショメーターがあります：1つは感度を調整し、もう1つは検出距離を調整します。PIRモジュールがより良く動作するように、両方のポテンショメーターを反時計回りに最大まで回してください。

    |img_PIR_TTE|


**配線**


|wiring_passager_counter|

**コードの記述**

MicroPythonスクリプトを作成し、以下の機能を実装します：

* PIRセンサーを使用して動きを検出します。
* 動きが検出されるたびにカウントを増加させます。
* 現在のカウントを4桁の7セグメントディスプレイに更新します。
* マルチプレクシングを使用してディスプレイを制御します。

.. note::

    * ``pico-2w-kit-main/micropython`` から ``7.4_passager_counter.py`` を開くか、コードをThonnyにコピーして、「実行」をクリックするか、F5を押します。
    * 正しいインタープリターが選択されていることを確認してください：MicroPython（Raspberry Pi Pico）.COMxx。 

.. code-block:: python

    from machine import Pin
    import utime

    # PIRセンサーのピンを定義
    pir_sensor = Pin(16, Pin.IN)

    # カウントの初期化
    count = 0

    # 各桁（0-9）の2進コードを定義
    SEGMENT_CODES = [
        0x3F,  # 0
        0x06,  # 1
        0x5B,  # 2
        0x4F,  # 3
        0x66,  # 4
        0x6D,  # 5
        0x7D,  # 6
        0x07,  # 7
        0x7F,  # 8
        0x6F   # 9
    ]

    # 74HC595の制御ピンを初期化
    SDI = machine.Pin(18, machine.Pin.OUT)   # シリアルデータ入力（DS）
    RCLK = machine.Pin(19, machine.Pin.OUT)  # レジスタクロック（STCP）
    SRCLK = machine.Pin(20, machine.Pin.OUT) # シフトレジスタクロック（SHCP）

    # 7セグメントディスプレイの桁選択ピン（共通カソード）
    digit_pins = [
        machine.Pin(10, machine.Pin.OUT),  # 桁1
        machine.Pin(11, machine.Pin.OUT),  # 桁2
        machine.Pin(12, machine.Pin.OUT),  # 桁3
        machine.Pin(13, machine.Pin.OUT)   # 桁4
    ]

    # 74HC595にデータを送信する関数
    def shift_out(data):
        RCLK.low()
        for bit in range(7, -1, -1):
            SRCLK.low()
            bit_val = (data >> bit) & 0x01
            SDI.value(bit_val)
            SRCLK.high()
        RCLK.high()

    # 特定の位置に数字を表示する関数
    def display_digit(position, digit):
        # すべての桁をオフにする
        for dp in digit_pins:
            dp.high()
        # セグメントデータを送信
        shift_out(SEGMENT_CODES[digit])
        # 選択した桁をアクティブにする（共通カソードはアクティブロー）
        digit_pins[position].low()
        # 桁が見えるように小さな遅延
        utime.sleep_ms(5)
        # 桁をオフにする
        digit_pins[position].high()

    # 4桁のディスプレイに番号を表示する関数
    def display_number(number):
        # 各桁を抽出
        digits = [
            (number // 1000) % 10,
            (number // 100) % 10,
            (number // 10) % 10,
            number % 10
        ]
        # 各桁を迅速に表示
        for i in range(4):
            display_digit(i, digits[i])

    # PIRセンサーの割り込みハンドラ
    def pir_handler(pin):
        global count
        count += 1
        if count > 9999:
            count = 0

    # PIRセンサーの割り込み設定
    pir_sensor.irq(trigger=Pin.IRQ_RISING, handler=pir_handler)

    # メインループ
    while True:
        # ディスプレイを継続的に更新
        display_number(count)

このコードが実行されると、7セグメントディスプレイは初期化され、0000が表示されます。
PIRセンサーの前で動くと、カウントが1ずつ増加し、9999に達すると0000にリセットされます。



**コードの理解**

#. インポートとピン定義：

   * ``machine.Pin``: GPIOピンを制御するためのモジュール。
   * ``utime``: 時間関連の関数。
   * 74HC595を制御するためにSDI、SRCLK、RCLKピンを定義。
   * ``pir_sensor`` をGP16に設定してPIRセンサーの入力ピンとして使用。

#. セグメントコード：

   * ``SEGMENT_CODES``: 7セグメントディスプレイに数字0-9を表示するための2進コードを格納したリストです。各バイトは点灯すべきセグメントを表します。

   .. code-block:: python

        # 7セグメントディスプレイのセグメントコード（共通カソード）
        SEGMENT_CODES = [
            0x3F,  # 0
            0x06,  # 1
            0x5B,  # 2
            0x4F,  # 3
            0x66,  # 4
            0x6D,  # 5
            0x7D,  # 6
            0x07,  # 7
            0x7F,  # 8
            0x6F   # 9
        ]

#. カウントの初期化：

   * ``count``: 動きが検出されるたびに増加するカウントを追跡するグローバル変数です。

#. ``shift_out`` 関数の定義：

   * 8ビットのデータを74HC595に送信します。
   * 最上位ビット（MSB）からデータをシフトします。
   * シフトクロックとレジスタクロックを適切にパルスさせます。

   .. code-block:: python

        def shift_out(data):
            RCLK.low()
            for bit in range(7, -1, -1):
                SRCLK.low()
                bit_val = (data >> bit) & 0x01
                SDI.value(bit_val)
                SRCLK.high()
            RCLK.high()

#. ``display_digit`` 関数の定義：

   * すべての桁をオフにします。
   * 数字のセグメントコードを送信します。
   * 選択した桁をアクティブにして表示します。
   * 小さな遅延を追加して、桁が見えるようにします。
   * 表示後に桁をオフにします。

   .. code-block:: python

        def display_digit(position, digit):
            for dp in digit_pins:
                dp.high()
            shift_out(SEGMENT_CODES[digit])
            digit_pins[position].low()
            utime.sleep_ms(5)
            digit_pins[position].high()

#. ``display_number`` 関数の定義：

   * 数字から各桁を抽出します。
   * 各桁を迅速に表示するために ``display_digit`` を呼び出します。

   .. code-block:: python

        def display_number(number):
            # Extract individual digits
            digits = [
                (number // 1000) % 10,
                (number // 100) % 10,
                (number // 10) % 10,
                number % 10
            ]
            # Display each digit rapidly
            for i in range(4):
                display_digit(i, digits[i])

#. PIR割り込みハンドラ：

   * ``pir_handler``: PIRセンサーが動きを検出すると自動的に呼び出されます。
   * カウント変数をインクリメントします。
   * カウントが9999を超えると、カウントを0にリセットします。

   .. code-block:: python

        def pir_handler(pin):
            global count
            count += 1
            if count > 9999:
                count = 0

#. PIRセンサー割り込みの設定：

   ``pir_sensor.irq``: PIRセンサーからの立ち上がりエッジ信号（動きを検出したとき）で ``pir_handler`` を呼び出すように設定します。

   .. code-block:: python

        pir_sensor.irq(trigger=Pin.IRQ_RISING, handler=pir_handler)

#. メインループ：

   ``display_number(count)`` を継続的に呼び出して、現在のカウントをディスプレイに表示します。

   .. code-block:: python

        while True:
            display_number(count)

**トラブルシューティング**

* 表示の問題：

  * 表示が正しくない場合、セグメントコードや配線接続を確認してください。
  * シフトレジスタが正しく接続され、データが正しい順序でシフトアウトされているか確認してください。

* PIRセンサーの感度：

  * PIRセンサーには感度や遅延を調整するためのポテンショメーターがあるかもしれません。
  * これらを調整して、環境に最適な動作を得てください。
  * PIRセンサーは動きを検出した後、再度検出するまで短い遅延があります。

* カウントの精度：

  * 動きが多い環境では、カウントが急激に増加することがあります。
  * 必要に応じて、PIRセンサーのデバウンスやカウント頻度の制限を追加することを検討してください。

**拡張と改善**

* リセットボタン：

  別のGPIOピンに接続されたプッシュボタンを追加し、ボタンを押すとカウントがゼロにリセットされるようにします。

* 双方向カウント：

  2つのPIRセンサーを戦略的に配置し、動きの方向（入退室）を検出して、カウントを増減させます。

* データログ：

  時間ごとにカウントを記録するプログラムを拡張し、Picoにデータを保存するか、コンピュータに送信して分析します。

* 表示の改善：

  LCDディスプレイを使用して、タイムスタンプ、総カウント、メッセージなどの追加情報を表示します。

* ネットワーク接続：

  Picoをネットワークに接続（ESP8266のようなWi-Fiモジュールを使用）し、データをサーバーやクラウドサービスに送信してリモート監視を行います。

**結論**

このレッスンでは、Raspberry Pi Pico 2 W、PIRモーションセンサー、および4桁の7セグメントディスプレイを使用して実用的な乗客カウンターを作成する方法を学びました。このプロジェクトは、マイクロコントローラーがセンサーや出力デバイスと連携して、リアルタイムでデータを収集・表示する方法を示しています。

コードとハードウェアを使って新しい機能を追加したり、機能を改善したりして、実験を楽しんでください。このプロジェクトは、データ分析、リモート監視、他のセンサーやデバイスとの統合を含む、より複雑なシステムの基盤として活用できます。
