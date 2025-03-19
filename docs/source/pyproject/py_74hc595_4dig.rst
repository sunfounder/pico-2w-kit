.. note:: 

     こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Raspberry Pi、Arduino、ESP32を使って、他のエンスージアストと一緒にさらに深く学びましょう。

     **参加する理由**

     - **専門家のサポート**: 購入後の問題や技術的な課題を、コミュニティやチームのサポートを受けて解決できます。
     - **学びと共有**: ヒントやチュートリアルを交換してスキルを向上させましょう。
     - **限定プレビュー**: 新製品の発表や先行公開をいち早く見ることができます。
     - **特別割引**: 最新の製品に特別割引が適用されます。
     - **季節のプロモーションやプレゼント**: プレゼント企画やホリデープロモーションに参加できます。

👉 一緒に探求し、創造する準備はできましたか？[|link_sf_facebook|]をクリックして、今日から参加しましょう！

.. _py_74hc_4dig:

5.3 タイムカウンター
================================

このレッスンでは、Raspberry Pi Pico 2 Wを使って **4桁の7セグメントディスプレイ** を使用し、シンプルなタイムカウンターを作成する方法を学びます。
このディスプレイは、毎秒カウントアップし、経過時間を秒単位で表示します。


**必要なコンポーネント**

このプロジェクトには、以下のコンポーネントが必要です。

キット全体を購入するのが便利です。こちらから購入できます：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前    
        - このキットのアイテム
        - リンク
    *   - Pico 2 W スターターキット
        - 450+
        - |link_pico2w_kit|

以下のリンクから個別に購入することもできます。


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
        - Micro USBケーブル
        - 1
        - 
    *   - 3
        - :ref:`cpn_breadboard`
        - 1
        - |link_breadboard_buy|
    *   - 4
        - :ref:`cpn_wire`
        - Several
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

**4桁の7セグメントディスプレイの理解**

4桁の7セグメントディスプレイは、4つの個別の7セグメントディスプレイが1つのモジュールに組み合わさっています。各桁は同じセグメント制御線（ **a** から **g** と **dp**）を共有しますが、各桁には独自の **共通カソード** 制御があります。この構成により、どの桁がアクティブであるかを制御できます。

各桁に異なる数字を表示するために、 **多重化** と呼ばれる技術を使用します。数字を切り替えながら、1桁ずつ更新しますが、視覚的に全桁が同時に表示されているように見えるのは、残像効果によるものです。

|4digit_control_pins|

**回路図**

|sch_4dig|

ここでの配線原則は、基本的に :ref:`py_74hc_led` と同じで、唯一の違いはQ0-Q7が4桁の7セグメントディスプレイのa〜gピンに接続されている点です。

その後、G10〜G13がどの7セグメントディスプレイを選択するかを決定します。

**配線**

|wiring_4dig|

* **セグメント接続（220Ωの抵抗を通して）**:

  * **Q0** → セグメント **a**
  * **Q1** → セグメント **b**
  * **Q2** → セグメント **c**
  * **Q3** → セグメント **d**
  * **Q4** → セグメント **e**
  * **Q5** → セグメント **f**
  * **Q6** → セグメント **g**
  * **Q7** → セグメント **dp** （小数点）

* **共通カソード接続（桁選択ピン）**:

  * **桁1（最左の桁）**: **GP10** に接続
  * **桁2**: **GP11** に接続
  * **桁3**: **GP12** に接続
  * **桁4（最右の桁）**: **GP13** に接続

**コードの作成**

1秒ごとに増加するタイムカウンターを作成し、そのカウントを4桁の7セグメントディスプレイに表示するMicroPythonプログラムを作成しましょう。

.. note::

    * ``5.3_time_counter.py`` を ``pico-2w-kit-main/micropython`` から開くか、コードをThonnyにコピーして、「Run」をクリックするか、F5を押して実行します。
    * 正しいインタプリタが選択されていることを確認してください：MicroPython（Raspberry Pi Pico）。COMxx。

.. code-block:: python

    import machine
    import utime

    # 各数字（0-9）のバイナリコードを定義
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

    # 桁選択ピン（共通カソード）
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
        # 全ての桁を消灯
        for dp in digit_pins:
            dp.high()
        # セグメントデータを送信
        shift_out(SEGMENT_CODES[digit])
        # 選択した桁をアクティブにする（共通カソードはアクティブロー）
        digit_pins[position].low()
        # 小さな遅延を入れて桁を表示
        utime.sleep_ms(5)
        # 桁を消灯
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

    # メインループ
    counter = 0
    last_update = utime.ticks_ms()

    while True:
        # 1000ms（1秒）ごとにカウンタを更新
        current_time = utime.ticks_ms()
        if utime.ticks_diff(current_time, last_update) >= 1000:
            counter += 1
            if counter > 9999:
                counter = 0
            last_update = current_time

        # ディスプレイを継続的に更新
        display_number(counter)

このコードを実行すると、4桁の7セグメントディスプレイはカウンターとして機能し、表示される数字が毎秒1ずつ増加します。0から9999まで表示され、その後0にリセットされ、サイクルが繰り返されます。

**コードの理解**

#. モジュールをインポート:

   * ``machine``: GPIOピンとハードウェア機能にアクセスします。
   * ``utime``: 遅延やタイミング関連の関数を提供します。

#. セグメントコードを定義:

   各エントリは数字を表示するために点灯する必要があるセグメントに対応します。値は16進数形式です。

    .. code-block:: python

        # Define the binary codes for each digit (0-9)
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

#. 制御ピンを初期化:

   74HC595を制御するためにPicoのGPIOピンを割り当てます。

   .. code-block:: python

        SDI = machine.Pin(18, machine.Pin.OUT)
        RCLK = machine.Pin(19, machine.Pin.OUT)
        SRCLK = machine.Pin(20, machine.Pin.OUT)


#. 桁選択ピンを初期化:

   どの桁がアクティブであるかを制御します。アクティブロー（共通カソード）。

   .. code-block:: python

        digit_pins = [
            machine.Pin(10, machine.Pin.OUT),
            machine.Pin(11, machine.Pin.OUT),
            machine.Pin(12, machine.Pin.OUT),
            machine.Pin(13, machine.Pin.OUT)
        ]

#. ``shift_out`` 関数を定義:

   * 74HC595に8ビットのデータを送信します。
   * 最上位ビット（MSB）からデータをシフトアウトします。
   * シフトクロックとレジスタクロックを適切にパルスします。

   .. code-block:: python

        def shift_out(data):
            RCLK.low()
            for bit in range(7, -1, -1):
                SRCLK.low()
                bit_val = (data >> bit) & 0x01
                SDI.value(bit_val)
                SRCLK.high()
            RCLK.high()

#. ``display_digit`` 関数を定義:

   * すべての桁を消灯します。
   * 数字のセグメントコードを送信します。
   * 指定された桁をアクティブにするためにピンをローに設定します。
   * 数字が見えるように小さな遅延を加えます。
   * 表示後、桁を消灯します。

   .. code-block:: python

        def display_digit(position, digit):
            for dp in digit_pins:
                dp.high()
            shift_out(SEGMENT_CODES[digit])
            digit_pins[position].low()
            utime.sleep_ms(5)
            digit_pins[position].high()

#. ``display_number`` 関数を定義:

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

#. メインループ:

   * 毎秒カウントを増やします。
   * 9999に達した後、カウンターをリセットします。
   * ``display_number`` を継続的に呼び出してディスプレイを更新します。

   .. code-block:: python

        counter = 0
        last_update = utime.ticks_ms()

        while True:
            current_time = utime.ticks_ms()
            if utime.ticks_diff(current_time, last_update) >= 1000:
                counter += 1
                if counter > 9999:
                    counter = 0
                last_update = current_time

            display_number(counter)


**さらなる実験**



* リセットボタンを追加:

  Picoにボタンを接続して、押すとカウンターがリセットされるようにします。

* 異なるデータを表示:

  温度や光レベルなどのセンサーデータを表示するようにコードを変更します。

* 表示の明るさを調整:

  ``display_digit`` 関数内の ``utime.sleep_ms(5)`` 遅延を変更して、各桁が表示される時間を調整し、明るさに影響を与えます。

* ストップウォッチを作成:

  スタート、ストップ、リセット機能を実装して、ディスプレイをストップウォッチとして使用します。

**結論**

このレッスンでは、74HC595シフトレジスタを使用して4桁の7セグメントディスプレイでタイムカウンターを作成する方法を学びました。多重化と効率的なタイミングを理解することで、GPIOピンを最小限に使用して、複数桁のディスプレイに動的な情報を表示することができます。
