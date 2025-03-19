.. note::

    こんにちは！FacebookのSunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！仲間たちと一緒にRaspberry Pi、Arduino、ESP32についてさらに深く学びましょう。

    **参加する理由は？**

    - **専門的なサポート**: 当コミュニティとチームの助けを借りて、販売後の問題や技術的な課題を解決できます。
    - **学び・共有**: スキルを向上させるためのヒントやチュートリアルを交換しましょう。
    - **特別なプレビュー**: 新製品の発表やプレビューに早期アクセスできます。
    - **特別割引**: 最新製品の独占的な割引を楽しめます。
    - **フェスティブなプロモーションとプレゼント企画**: プレゼント企画やホリデープロモーションに参加できます。

    👉 私たちと一緒に探索し、創造を始める準備はできましたか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _py_traffic_light:

7.6 信号機制御の作成
==============================================================

このプロジェクトでは、Raspberry Pi Pico 2 W、3つのLED（赤、黄、緑）、および4桁の7セグメントディスプレイを使用して、 **信号機制御装置** を作成します。このシステムは、実際の信号機のシーケンスをシミュレートし、各信号の残り時間を7セグメントディスプレイに表示します。

* **赤信号**: 点滅している赤信号は、車両が停止する必要があることを示します。
* **黄信号**: 赤信号に変わる準備ができていることを警告します。黄信号は国（地域）によって異なる解釈があります。
* **緑信号**: 指定された方向に車両が進むことができます。

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
        - :ref:`cpn_resistor`
        - 7(220Ω)
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
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|


**部品の理解**

* **LED**: 信号機を表すLEDを制御し、標準的な信号機シーケンスをシミュレートします。
* **4桁7セグメントディスプレイ**: 各信号のカウントダウンタイマーを表示します。
* **74HC595シフトレジスタ**: PicoのGPIOピンを節約し、ディスプレイのセグメントや数字を制御します。

**回路図**

|sch_traffic_light|


* この回路は、 :ref:`py_74hc_4dig` に3つのLEDを追加したものです。
* 3つの赤、黄、緑のLEDはそれぞれGP7~GP9に接続されています。

**配線**


|wiring_traffic_light|


**コードの作成**

MicroPythonのスクリプトを作成します：

* 信号機のシーケンスを制御します。
* 7セグメントディスプレイにカウントダウンタイマーを表示します。
* シフトレジスタを使用してディスプレイを制御します。

.. note::

    * ``7.6_traffic_light.py`` を ``pico-2w-kit-main/micropython`` から開くか、このコードをThonnyにコピーして「Run」をクリックするか、F5キーを押して実行します。
    * 正しいインタープリターが選択されていることを確認してください：MicroPython（Raspberry Pi Pico）。COMxx。

.. code-block:: python

    import machine
    import utime
    from machine import Timer

    # LEDピンの初期化
    led_pins = [7, 8, 9]  # 緑、黄、赤LEDがそれぞれGP7、GP8、GP9に接続されています
    leds = [machine.Pin(pin, machine.Pin.OUT) for pin in led_pins]

    # 各信号の時間（秒単位）[緑、黄、赤]
    light_time = [30, 5, 30]  # [緑、黄、赤]

    # 各数字の2進コード（0-9）
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

    # 74HC595の制御ピンの初期化
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

    # 指定した位置に数字を表示する関数
    def display_digit(position, digit):
        # 全桁をオフにする
        for dp in digit_pins:
            dp.high()
        # セグメントデータを送信
        shift_out(SEGMENT_CODES[digit])
        # 選択した桁をアクティブにする（共通カソードはアクティブロー）
        digit_pins[position].low()
        # 小さな遅延を入れて桁が見えるようにする
        utime.sleep_ms(5)
        # 桁をオフにする
        digit_pins[position].high()

    # 4桁のディスプレイに数字を表示する関数
    def display_number(number):
        # 数字を個々の桁に分解
        digits = [
            (number // 1000) % 10,
            (number // 100) % 10,
            (number // 10) % 10,
            number % 10
        ]
        # 各桁を迅速に表示
        for i in range(4):
            display_digit(i, digits[i])

    # 現在の状態に基づいてLEDを更新する関数
    def update_leds(state):
        # 状態：0 = 緑、1 = 黄、2 = 赤
        for i in range(3):
            leds[i].value(0)
        leds[state].value(1)

    # タイマー変数
    counter = light_time[0]  # 緑信号の時間から開始
    current_state = 0  # 0 = 緑、1 = 黄、2 = 赤

    # タイマー割り込みコールバック関数（交通信号の状態とカウントダウンを更新）
    def timer_callback(t):
        global counter, current_state
        counter -= 1
        if counter <= 0:
            current_state = (current_state + 1) % 3  # 状態を循環
            counter = light_time[current_state]  # 新しい状態のためにカウンターをリセット
            update_leds(current_state)

    # タイマーの初期化
    timer = Timer(period=1000, mode=Timer.PERIODIC, callback=timer_callback)

    # 初期LED状態
    update_leds(current_state)

    # メインループ
    try:
        while True:
            display_number(counter)
    except KeyboardInterrupt:
        timer.deinit()
        print("Program stopped.")


コードが実行されると、緑のLEDが最初に点灯し、ディスプレイに30からのカウントダウンが表示されます。
30秒後、黄のLEDが点灯し、5秒からカウントダウンが始まります。
その後、赤のLEDが点灯し、30秒からカウントダウンが始まります。
サイクルは無限に繰り返されます。

**コードの理解**

#. インポートと初期化：

   * ``machine``: ハードウェア関連の関数にアクセスします。
   * ``utime``: 時間関連の関数を使用します。
   * ``Timer``: ハードウェアタイマーを作成するために使用します。

#. LEDの初期化：

   赤、黄、緑のLEDのGPIOピンを定義し、各ピンを出力として初期化します。

   .. code-block:: python

        led_pins = [7, 8, 9]  # 緑、黄、赤LEDがそれぞれGP7、GP8、GP9に接続されています
        leds = [machine.Pin(pin, machine.Pin.OUT) for pin in led_pins]

#. 信号機のタイミング：

   各信号の状態の時間（秒単位）を指定します。

   .. code-block:: python

        light_time = [30, 5, 30]  # [緑、黄、赤]

#. ディスプレイ関数：

   * ``display_digit(digit)``: 特定の桁をディスプレイに表示します。
   * ``shift_out(data)``: シフトレジスタにデータを送信します。
   * ``display_number(num)``: 数字を分解して、マルチプレクシングを使用してディスプレイします。

#. ``update_leds(state)`` 関数：

   * 現在の信号機の状態に基づいてLEDを更新します。
   * すべてのLEDをオフにし、現在の状態に対応するLEDをオンにします。

   .. code-block:: python

        def update_leds(state):
            # 状態：0 = 緑、1 = 黄、2 = 赤
            for i in range(3):
                leds[i].value(0)
            leds[state].value(1)

#. ``timer_callback(t)`` 関数：

   * タイマー割り込みコールバック関数。
   * 毎秒カウントを減らします。
   * カウントがゼロになると、次の信号機の状態に循環し、カウントをリセットします。

   .. code-block:: python

        def timer_callback(t):
            global counter, current_state
            counter -= 1
            if counter <= 0:
                current_state = (current_state + 1) % 3  # 状態を循環
                counter = light_time[current_state]  # 新しい状態のためにカウントをリセット
                update_leds(current_state)

#. 実行：

   * 初期状態の設定：緑に設定し、カウントダウンを開始します。

     .. code-block:: python

        counter = light_time[0]  # 緑信号の時間から開始
        current_state = 0  # 0 = 緑、1 = 黄、2 = 赤

   * タイマーの初期化：1秒ごとに割り込みを発生させる周期タイマーを作成し、 timer_callbackを呼び出します。

     .. code-block:: python

        timer = Timer(period=1000, mode=Timer.PERIODIC, callback=timer_callback)

   * 初期LED状態の設定：最初に正しいLEDが点灯していることを確認します。

     .. code-block:: python

        update_leds(current_state)

   * メインループ：カウントダウンタイマーを表示し、キーボードの割り込み（Ctrl+Cなど）で安全にタイマーを終了します。


     .. code-block:: python

        try:
            while True:
                display_number(counter)
        except KeyboardInterrupt:
            timer.deinit()
            print("Program stopped.")



**さらに実験する**

* タイミングを調整：

  ``light_time`` リストを変更して、各信号の時間を調整します。

* 歩行者用信号を追加：

  ボタンや追加のLEDを実装して、歩行者用信号をシミュレートします。

* ディスプレイを改善：

  LEDがタイマー終了間近に点滅するような機能を追加します。

* 実際の信号機をシミュレート：

  左折信号や交差点ごとの複雑なシーケンスを追加します。

**結論**

Raspberry Pi Pico 2 Wを使用して信号機制御装置を作成しました！このプロジェクトは、マイコンを使用してLEDやディスプレイなどのハードウェアコンポーネントを制御し、タイマーや割り込みを使ってリアルタイムアプリケーションを作成する方法を示しています。

このプロジェクトを拡張して新しい機能を追加したり、より大きなシステムに統合したりできます。
