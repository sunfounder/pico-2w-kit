.. note:: 

    SunFounderのRaspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32について、他の愛好者と共にさらに深く学びましょう。

    **参加する理由は？**

    - **専門家サポート**: 購入後の問題や技術的な課題を、コミュニティやチームの支援で解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **限定プレビュー**: 新製品の発表や先行公開に早期アクセスできます。
    - **特別割引**: 最新製品に対する独占的な割引を享受できます。
    - **フェスティブプロモーションとプレゼント**: プレゼント企画やホリデープロモーションに参加できます。

    👉 一緒に探求し、創造しましょう！[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _py_10_second:

7.5 「10秒ゲーム」の作成
======================================================

この面白いプロジェクトでは、Raspberry Pi Pico 2 W、傾斜スイッチ、4桁の7セグメントディスプレイを使用して **「10秒ゲーム」** を作成します。このゲームの目的は、魔法の杖（棒に取り付けた傾斜スイッチで模擬）の動作を使ってタイマーを開始し、もう一度振って、 **10.00秒** にできるだけ近い時間でタイマーを停止することです。タイミングスキルをテストし、友達と真のタイムウィザードを競いましょう！

**必要なコンポーネント**

このプロジェクトに必要なコンポーネントは次の通りです。

全セットを購入するのが便利です。リンクはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前	
        - セットに含まれるアイテム
        - リンク
    *   - Pico 2 Wスターターキット	
        - 450+
        - |link_pico2w_kit|

個別に購入することもできます。以下のリンクから購入できます。


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
        - 複数
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_resistor`
        - 5(4-220Ω, 1-10KΩ)
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
        - :ref:`cpn_tilt`
        - 1
        - 

**コンポーネントの理解**

* **傾斜スイッチ**: 物体の傾きを検出するセンサー。傾けると回路が完成したり切れたりして、振動や動きを検出できます。
* **4桁の7セグメントディスプレイ**: 0000から9999までの数字を表示できます。ディスプレイを制御するためにシフトレジスタを使用し、GPIOピンの数を減らします。
* **74HC595シフトレジスタ**: 8ビットのシリアル入力、並列出力のシフトレジスタ。少ないGPIOピンで複数の出力を制御できます。

**回路図**

|sch_10_second|


* この回路は :ref:`py_74hc_4dig` に傾斜スイッチを追加したものです。
* 傾斜スイッチが垂直のとき、GP16はハイに、傾けるとローになります。

**配線**

|wiring_game_10_second|

**コードの作成**

MicroPythonスクリプトを作成して、以下の動作を行います：

* 傾斜スイッチを使用して振動を検出します。
* 傾斜スイッチを基にタイマーを開始および停止します。
* 4桁の7セグメントディスプレイに経過時間を表示します。
* マルチプレクシングとシフトレジスタを使用してディスプレイを制御します。

.. code-block:: python

    from machine import Pin
    import utime

    # 74HC595の制御ピンを初期化
    SDI = machine.Pin(18, machine.Pin.OUT)   # シリアルデータ入力 (DS)
    RCLK = machine.Pin(19, machine.Pin.OUT)  # レジスタクロック (STCP)
    SRCLK = machine.Pin(20, machine.Pin.OUT) # シフトレジスタクロック (SHCP)

    # 7セグメントディスプレイのセグメントコード（共通カソード）
    SEGMENT_CODES = [0x3F,  # 0
                    0x06,  # 1
                    0x5B,  # 2
                    0x4F,  # 3
                    0x66,  # 4
                    0x6D,  # 5
                    0x7D,  # 6
                    0x07,  # 7
                    0x7F,  # 8
                    0x6F]  # 9

    # 桁選択ピンを初期化（共通カソード）
    digit_pins = [
        machine.Pin(10, machine.Pin.OUT),  # 桁1
        machine.Pin(11, machine.Pin.OUT),  # 桁2
        machine.Pin(12, machine.Pin.OUT),  # 桁3
        machine.Pin(13, machine.Pin.OUT)   # 桁4
    ]


    # 傾斜スイッチを初期化
    tilt_switch = Pin(16, Pin.IN, Pin.PULL_DOWN)

    # タイミング用の変数
    start_time = 0
    elapsed_time = 0
    counting = False

    # シフトレジスタにデータをシフトアウトする関数
    def shift_out(data):
        RCLK.low()
        for bit in range(7, -1, -1):
            SRCLK.low()
            bit_val = (data >> bit) & 0x01
            SDI.value(bit_val)
            SRCLK.high()
        RCLK.high()

    # 指定した位置に数字を表示する関数
    def display_digit(position, digit):
        # すべての桁を消灯
        for dp in digit_pins:
            dp.high()
        # セグメントデータを送信
        shift_out(SEGMENT_CODES[digit])
        # 選択した桁をアクティブに（共通カソードはアクティブロー）
        digit_pins[position].low()
        # 数字が見えるように短い遅延を挿入
        utime.sleep_ms(5)
        # 桁を消灯
        digit_pins[position].high()

    # 経過時間を表示する関数
    def display_time(time_ms):
        # 時間をセンチ秒（0.01秒単位）に変換
        centiseconds = int(time_ms / 10)
        # 9999を超えないように制限
        if centiseconds > 9999:
            centiseconds = 9999

        # 各桁を抽出
        digits = [
            (centiseconds // 1000) % 10,
            (centiseconds // 100) % 10,
            (centiseconds // 10) % 10,
            centiseconds % 10
        ]
        # 各桁を素早く表示
        for i in range(4):
            display_digit(i, digits[i])

    # 傾斜スイッチの割り込みハンドラー
    def tilt_handler(pin):
        global counting, start_time, elapsed_time
        if not counting:
            # カウント開始
            counting = True
            start_time = utime.ticks_ms()
        else:
            # カウント停止
            counting = False
            elapsed_time = utime.ticks_diff(utime.ticks_ms(), start_time)

    # 傾斜スイッチの割り込み設定
    tilt_switch.irq(trigger=Pin.IRQ_RISING, handler=tilt_handler)

    # メインループ
    while True:
        if counting:
            # 経過時間を計算
            current_time = utime.ticks_diff(utime.ticks_ms(), start_time)
            display_time(current_time)
        else:
            # 最終的な時間を表示
            display_time(elapsed_time)



コードが実行されると、4桁の7セグメントディスプレイは初期化され、00.00が表示されます。

* タイマー開始：

  * 杖を振るか、傾斜スイッチを傾けて割り込みを発生させます。
  * タイマーが00.00からカウントアップを開始します。

* タイマー停止：

  * もう一度杖を振るか、スイッチを傾けます。
  * タイマーが停止し、最終時間が表示されます。

* 目標：

  * できるだけ10.00秒に近い時間でタイマーを止めてみましょう。
  * 友達と誰が最も近いタイムを出せるか挑戦してみてください！

**コードの理解**

#. インポートとピン定義：

   * ``machine.Pin``: GPIOピンを制御するためのクラス。
   * ``utime``: タイミング関数を使用します。
   * SDI、SRCLK、RCLKピンをシフトレジスタ制御用に定義します。
   * GP16にプルダウン抵抗を使って傾斜スイッチを初期化します。

#. セグメントと数字コード：

   * ``SEGMENT_CODES``: 7セグメントディスプレイに数字0-9を表示するためのバイナリコードのリスト。
   * ``digit_pins``: ディスプレイの各桁を選択するためのピン。共通カソード表示の場合、アクティブはLOWです。

   .. code-block:: python

        # 7セグメントディスプレイのセグメントコード（共通カソード）
        SEGMENT_CODES = [0x3F,  # 0
                        0x06,  # 1
                        0x5B,  # 2
                        0x4F,  # 3
                        0x66,  # 4
                        0x6D,  # 5
                        0x7D,  # 6
                        0x07,  # 7
                        0x7F,  # 8
                        0x6F]  # 9

        # 桁選択ピンを初期化（共通カソード）
        digit_pins = [
            machine.Pin(10, machine.Pin.OUT),  # 桁1
            machine.Pin(11, machine.Pin.OUT),  # 桁2
            machine.Pin(12, machine.Pin.OUT),  # 桁3
            machine.Pin(13, machine.Pin.OUT)   # 桁4
        ]

#. タイミング用の変数：

   * ``start_time``: タイマーが開始された時間を記録します。
   * ``elapsed_time``: タイマー停止時に経過した時間を記録します。
   * ``counting``: タイマーが動作しているかどうかを示すブール値フラグ。

#. ``shift_out`` 関数の定義：

   * シフトレジスタに8ビットのデータを送信します。
   * 最上位ビット（MSB）からデータをシフトアウトします。
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

   * すべての桁を消灯します。
   * 数字に対応するセグメントコードを送信します。
   * 選択された桁をアクティブにします（共通カソード表示はLOWがアクティブ）。
   * 数字を表示するための短い遅延を追加します。
   * 表示後に桁を消灯します。

   .. code-block:: python

        def display_digit(position, digit):
            for dp in digit_pins:
                dp.high()
            shift_out(SEGMENT_CODES[digit])
            digit_pins[position].low()
            utime.sleep_ms(5)
            digit_pins[position].high()

#. ``display_time`` 関数：

   * ミリ秒単位の経過時間をセンチ秒（0.01秒単位）に変換します。
   * 経過時間を個別の数字に分解します。
   * 各桁を素早く表示するためにマルチプレクシングを使用します。

   .. code-block:: python

        def display_time(time_ms):
            # 時間をセンチ秒（0.01秒単位）に変換
            centiseconds = int(time_ms / 10)
            # 9999を超えないように制限
            if centiseconds > 9999:
                centiseconds = 9999

            # 各桁を抽出
            digits = [
                (centiseconds // 1000) % 10,
                (centiseconds // 100) % 10,
                (centiseconds // 10) % 10,
                centiseconds % 10
            ]
            # 各桁を素早く表示
            for i in range(4):
                display_digit(i, digits[i])

#. ``tilt_handler`` 関数：

   * 傾斜スイッチの割り込みによってトリガーされます。
   * カウント状態を切り替えます。
   * カウント開始時に ``start_time`` を記録します。
   * カウント停止時に ``elapsed_time`` を計算します。

   .. code-block:: python

        def tilt_handler(pin):
            global counting, start_time, elapsed_time
            if not counting:
                # カウント開始
                counting = True
                start_time = utime.ticks_ms()
            else:
                # カウント停止
                counting = False
                elapsed_time = utime.ticks_diff(utime.ticks_ms(), start_time)

#. メインループ：

   * ``counting`` が ``True`` の場合、現在の経過時間を表示し続けます。
   * ``counting`` が ``False`` の場合、最終的な ``elapsed_time`` を表示します。

   .. code-block:: python

        while True:
            if counting:
                # 経過時間を計算
                current_time = utime.ticks_diff(utime.ticks_ms(), start_time)
                display_time(current_time)
            else:
                # 最終的な時間を表示
                display_time(elapsed_time)

**トラブルシューティング**

* ディスプレイの問題：

  * 数字が正しく表示されない場合は、セグメントコードと桁コード、配線接続を確認してください。
  * シフトレジスタが適切に接続されていること、およびデータが正しい順序でシフトされていることを確認してください。

* 傾斜スイッチの感度：

  * 傾斜スイッチが敏感すぎる、または敏感すぎない場合は、その向きを調整するか、他の種類に交換してください。
  * 誤動作を防ぐためにプルダウン抵抗が正しく接続されているか確認してください。

* タイミング精度：

  * タイマーはシステムクロックに依存していますが、若干の誤差があるかもしれません。
  * 精度を向上させるために、外部のリアルタイムクロック（RTC）モジュールを使用することができます。

**拡張と強化**

* ビジュアル効果：

  * タイマーが停止したときに点滅するLEDや色を変更するLEDを追加します。
  * タイマーの開始と停止時に音声フィードバックを提供するためにブザーを使用します。

* ハイスコアの追跡：

  * 最も近いタイム（10.00に最も近い時間）を記録するようにコードを変更します。
  * 新しいハイスコアに対して、お祝いのメッセージやアニメーションを表示します。

* マルチプレイヤーモード：

  * 複数のプレイヤーが順番にプレイできるようにし、各プレイヤーのタイムを記録します。
  * プレイヤーの番号とそのタイムを表示します。

* 難易度のレベル：

  * 異なるターゲット時間（例：5.00秒、15.00秒）を設定してチャレンジを増やします。
  * ターゲット時間をランダムにし、各ラウンドの開始時に表示します。

* 代替入力方法：

  * 傾斜スイッチをボタンや他のセンサーに置き換え、タイマーの開始と停止を行います。
  * 動作センサーを使って特定のジェスチャーを検出します。

**結論**

Raspberry Pi Pico 2 Wを使って「10秒ゲーム」を成功裏に作成しました！このプロジェクトでは、センサー入力、タイミング機能、およびディスプレイ制御を組み合わせて、インタラクティブで楽しいゲームを作成しました。これは、マイクロコントローラーを使用して楽しさとエンターテイメントを提供する素晴らしい例です。

このプロジェクトをカスタマイズして拡張することができます。新しい機能を追加したり、デザインを改善したり、追加のコンポーネントを統合したりすることで、可能性は無限大です。
