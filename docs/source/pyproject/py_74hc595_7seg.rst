.. note:: 

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Raspberry Pi、Arduino、ESP32について、他の愛好者と一緒にさらに深く学びましょう。

    **参加する理由**

    - **専門家のサポート**: コミュニティとチームの支援を受けて、販売後の問題や技術的な課題を解決します。
    - **学び、共有**: ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **限定プレビュー**: 新製品の発表やプレビューをいち早くチェックできます。
    - **特別割引**: 最新製品に対する特別な割引を享受できます。
    - **季節限定のプロモーションとプレゼント**: プレゼント企画やホリデープロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできましたか？[|link_sf_facebook|] をクリックして、今すぐ参加しましょう！

.. _py_74hc_7seg:

5.2 数字の表示
========================

このレッスンでは、 **7セグメントディスプレイ** を使用して、Raspberry Pi Pico 2 Wと **74HC595シフトレジスタ** を使って数字を表示する方法を学びます。7セグメントディスプレイは、デジタル時計、計算機、家電製品などのデバイスでよく使用される電子部品で、数値情報を表示するために使われます。

74HC595シフトレジスタと7セグメントディスプレイを組み合わせることで、PicoのGPIOピンを数本で全てのセグメントを制御でき、他の部品のために貴重なI/Oリソースを節約できます。

* :ref:`cpn_7_segment`

**必要な部品**

このプロジェクトでは、以下の部品が必要です。

キットを購入するのが便利です。こちらのリンクから購入できます：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前
        - キットに含まれているアイテム
        - リンク
    *   - Pico 2 W スターターキット
        - 450+
        - |link_pico2w_kit|

以下のリンクから個別に購入することもできます。


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
        - 複数
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_resistor`
        - 1（220Ω）
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_7_segment`
        - 1
        - |link_7segment_buy|
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|

**7セグメントディスプレイの理解**

7セグメントディスプレイは、0から9までの数字を表示するために、8の字型に配置された7つのLED（セグメント）で構成されています。さらに、8番目のLEDは小数点（dp）用です。各セグメントは **a** から **g** 、小数点は **dp** としてラベル付けされています。

ここでは、セグメントのラベリングを示します。

|img_7seg_cathode|

**共通カソード** の7セグメントディスプレイでは、すべてのLEDのカソード（負の端）が共通のグラウンドに接続されています。


**回路図**

|sch_74hc_7seg|

ここでの配線原理は、 :ref:`py_74hc_led` と基本的に同じですが、唯一の違いはQ0-Q7が7セグメントディスプレイのa～gピンに接続されている点です。

.. list-table:: Wiring
    :widths: 15 25
    :header-rows: 1

    *   - :ref:`cpn_74hc595`
        - :ref:`cpn_led` セグメントディスプレイ
    *   - Q0
        - a
    *   - Q1
        - b
    *   - Q2
        - c
    *   - Q3
        - d
    *   - Q4
        - e
    *   - Q5
        - f
    *   - Q6
        - g
    *   - Q7
        - dp

**配線**

.. 1. Pico 2 Wの3V3とGNDをブレッドボードの電源バスに接続します。
.. #. 74HC595をブレッドボードの中央の隙間に挿入します。
.. #. Pico 2 WのGP0ピンを74HC595のDSピン（ピン14）にジャンパーワイヤーで接続します。
.. #. Pico 2 WのGP1ピンを74HC595のSTcpピン（ピン12）に接続します。
.. #. Pico 2 WのGP2ピンを74HC595のSHcpピン（ピン11）に接続します。
.. #. 74HC595のVCCピン（ピン16）とMRピン（ピン10）を正の電源バスに接続します。
.. #. 74HC595のGNDピン（ピン8）とCEピン（ピン13）を負の電源バスに接続します。
.. #. LEDセグメントディスプレイをブレッドボードに挿入し、220Ωの抵抗をGNDピンと負の電源バスの間に直列で接続します。
.. #. 以下の表に従って74HC595とLEDセグメントディスプレイを接続します。

|wiring_74hc_7seg|



**コードの作成**

7セグメントディスプレイに0から9までの数字を表示するMicroPythonプログラムを作成しましょう。

.. note::

    * ``5.2_number_display.py`` を ``pico-2w-kit-main/micropython`` から開くか、コードをThonnyにコピーして、"Run"をクリックするか、F5を押します。
    * 正しいインタープリターを選択してください：MicroPython (Raspberry Pi Pico).COMxx。

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
    SDI = machine.Pin(0, machine.Pin.OUT)   # Serial Data Input (DS)
    RCLK = machine.Pin(1, machine.Pin.OUT)  # Register Clock (STCP)
    SRCLK = machine.Pin(2, machine.Pin.OUT) # Shift Register Clock (SHCP)

    # 74HC595にデータを送信する関数
    def shift_out(data):
        RCLK.low()
        for bit in range(7, -1, -1):
            SRCLK.low()
            bit_val = (data >> bit) & 0x01
            SDI.value(bit_val)
            SRCLK.high()
        RCLK.high()

    # 0から9までの数字を表示するメインループ
    while True:
        for num in range(10):
            shift_out(SEGMENT_CODES[num])
            utime.sleep(0.5)

このコードを実行すると、7セグメントディスプレイは0から9までの数字を順番に表示し、0.5秒ごとに変更されます。これにより、数字が1つずつ増加し、9に達すると表示が0に戻り、サイクルが繰り返されます。

**コードの説明**

#. モジュールのインポート：

   * ``machine``: GPIOピンやハードウェア機能へのアクセスを提供します。
   * ``utime``: 遅延やタイミングに関連する関数を提供します。

#. セグメントコードの定義：

   各エントリは、数字を表示するために点灯させる必要があるセグメントに対応しています。値は可読性のため、16進数形式で表記されています。

   .. code-block:: python

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

   7セグメントディスプレイで「1」を表示する場合、b、cを高レベル、a、d、e、f、g、dgを低レベルに設定する必要があります。

   |img_1_segment|

   つまり、バイナリ値「00000110」を書き込む必要があり、可読性のために16進数では「0x06」と記述します。


#. 制御ピンの初期化：

   PicoのGPIOピンを74HC595の制御用に割り当てます。

   .. code-block:: python

      SDI = machine.Pin(0, machine.Pin.OUT)
      RCLK = machine.Pin(1, machine.Pin.OUT)
      SRCLK = machine.Pin(2, machine.Pin.OUT)

#. ``shift_out`` 関数の定義：

   * 74HC595に8ビットのデータを送信します。
   * 最上位ビット（MSB）からデータをシフトアウトします。
   * シフトおよびレジスタクロックを適切にパルスします。

   .. code-block:: python

        def shift_out(data):
            RCLK.low()
            for bit in range(7, -1, -1):
                SRCLK.low()
                bit_val = (data >> bit) & 0x01
                SDI.value(bit_val)
                SRCLK.high()
            RCLK.high()

#. 数字を表示するメインループ：

   * 0から9までの数字を順番に繰り返し表示します。
   * 対応するセグメントコードでshift_outを呼び出します。
   * 各数字の間に0.5秒の遅延を追加します。

   .. code-block:: python

        while True:
            for num in range(10):
                shift_out(SEGMENT_CODES[num])
                utime.sleep(0.5)

**セグメントコードの理解**

各セグメントコードは、特定の数字を表示するために点灯させるべきセグメントに対応します。セグメントの対応は以下の通りです：

* **0**: セグメントa, b, c, d, e, f（コード 0x3F）
* **1**: セグメントb, c（コード 0x06）
* **2**: セグメントa, b, g, e, d（コード 0x5B）
* **3**: セグメントa, b, c, d, g（コード 0x4F）
* **4**: セグメントb, c, f, g（コード 0x66）
* **5**: セグメントa, c, d, f, g（コード 0x6D）
* **6**: セグメントa, c, d, e, f, g（コード 0x7D）
* **7**: セグメントa, b, c（コード 0x07）
* **8**: セグメントa, b, c, d, e, f, g（コード 0x7F）
* **9**: セグメントa, b, c, d, f, g（コード 0x6F）


**さらに実験する**

* 16進文字の表示：

  ``SEGMENT_CODES`` リストにA～Fの文字を追加して、16進表示を実現します。例えば、'A'を表示する場合、セグメントコードは0x77です。

* カウンターを作成：

  コードを変更して、アップカウンターやダウンカウンターを作成します。ボタン入力を使用して表示された数字を増減させます。

* 複数のディスプレイを制御：

  追加の74HC595シフトレジスタを使用して、複数の7セグメントディスプレイを制御します。GPIOの使用を最小限に抑えつつ、マルチプレクシングを実装して複数のディスプレイを管理します。

**結論**

このレッスンでは、74HC595シフトレジスタを使用して7セグメントディスプレイに数字を表示する方法を学びました。バイナリコードを使って各セグメントを制御し、シフトレジスタを活用することで、限られたGPIOピンで複数の出力を効率的に管理できることがわかりました。
