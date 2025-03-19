.. note:: 

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32について、他の愛好者と一緒にさらに深く学びましょう。

    **なぜ参加するのか？**

    - **専門的なサポート**：コミュニティとチームのサポートで、販売後の問題や技術的な課題を解決します。
    - **学びと共有**：チップやチュートリアルを交換し、スキルを向上させましょう。
    - **独占プレビュー**：新製品の発表や先行情報に早期アクセスできます。
    - **特別割引**：最新製品の特別割引を享受できます。
    - **祝祭シーズンのプロモーションとプレゼント**：プレゼント企画やホリデープロモーションに参加できます。

    👉 探索して一緒に創造したいですか？[|link_sf_facebook|]をクリックして、今日参加しましょう！

.. _py_74hc_led:

5.1 74HC595シフトレジスタの使用
=======================================

このレッスンでは、 **74HC595シフトレジスタ** を使用して、Raspberry Pi Pico 2 WのGPIOピンをいくつかだけで複数のLEDを制御する方法を学びます。74HC595は、シリアル入力を使用してデジタル出力の数を拡張できるIC（集積回路）です。GPIOピンが限られている場合でも、多くの出力を制御するのに非常に便利です。

* :ref:`74HC595`

**必要なコンポーネント**

このプロジェクトには、次のコンポーネントが必要です。

キットを購入するのが便利です。リンクはここです：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前  
        - このキットに含まれるアイテム
        - リンク
    *   - Pico 2 W スターターキット  
        - 450+
        - |link_pico2w_kit|

これらのコンポーネントを個別に購入することもできます。リンクは以下の通りです。


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
        - 8(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 8
        - |link_led_buy|
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|

**74HC595シフトレジスタの理解**

**74HC595** は、8ビットのシリアルイン、パラレルアウトのシフトレジスタで、出力ラッチを備えています。シリアルデータ入力を受け取り、それをパラレル出力に変換することができ、PicoのGPIOピン3本だけで8つの出力を制御できます。

**74HC595の主なピン:**

|img_74jc595_pin|

* **DS（ピン14）**: シリアルデータ入力
* **SHCP（ピン11）**: シフトレジスタクロック入力
* **STCP（ピン12）**: ストレージレジスタクロック入力（ラッチピン）
* **OE（ピン13）**: 出力有効（アクティブロー、GNDに接続）
* **MR（ピン10）**: マスタリセット（アクティブロー、3.3Vに接続）
* **Q0〜Q7（ピン15、1-7）**: パラレル出力
* **VCC（ピン16）**: 3.3Vに接続
* **GND（ピン8）**: GNDに接続

**回路図**

|sch_74hc_led|



**配線**

.. The 74HC595 is a 16-pin IC with a semi-circular notch on one side (usually the left side of the label). With the notch facing upwards, its pins are shown in the diagram below.


.. Refer to the figure below to build the circuit.


|wiring_74hc_led|

.. 1. Pico 2 Wの3V3とGNDをブレッドボードの電源バスに接続します。
.. #. 74HC595をブレッドボードの中央の隙間に挿入します。
.. #. Pico 2 WのGP0ピンを74HC595のDSピン（ピン14）にジャンパーワイヤーで接続します。
.. #. Pico 2 WのGP1ピンを74HC595のSTcpピン（ピン12）に接続します。
.. #. Pico 2 WのGP2ピンを74HC595のSHcpピン（ピン11）に接続します。
.. #. 74HC595のVCCピン（ピン16）とMRピン（ピン10）をプラスの電源バスに接続します。
.. #. 74HC595のGNDピン（ピン8）とCEピン（ピン13）をマイナスの電源バスに接続します。
.. #. 8つのLEDをブレッドボードに挿入し、それぞれのアノード端子を74HC595のQ0〜Q7ピン（ピン15, 1, 2, 3, 4, 5, 6, 7）に接続します。
.. #. LEDのカソード端子を220Ωの抵抗とともにマイナス電源バスに接続します。

**コードの作成**

次に、74HC595シフトレジスタを使ってLEDを制御するMicroPythonプログラムを作成します。

.. note::

    * ``pico-2w-kit-main/micropython`` から ``5.1_microchip_74hc595.py`` を開くか、コードをThonnyにコピーして、「実行」をクリックするか、F5を押してください。

    * 正しいインタープリタが選択されていることを確認してください：MicroPython（Raspberry Pi Pico）。COMxx。


.. code-block:: python

    import machine
    import utime

    # 74HC595に接続されているピンを定義
    SDI = machine.Pin(0, machine.Pin.OUT)   # シリアルデータ入力（DS）
    RCLK = machine.Pin(1, machine.Pin.OUT)  # レジスタクロック（STCP）
    SRCLK = machine.Pin(2, machine.Pin.OUT) # シフトレジスタクロック（SHCP）

    # 74HC595にデータを送信する関数
    def shift_out(data):
        for bit in range(8):
            # 最上位ビットを取り出して最初に送信
            bit_val = (data & 0x80) >> 7
            SDI.value(bit_val)
            # シフトレジスタクロックをパルスさせる
            SRCLK.high()
            utime.sleep_us(1)
            SRCLK.low()
            utime.sleep_us(1)
            # 次のビットのためにデータを1ビット左にシフト
            data = data << 1
        # レジスタクロックをパルスさせてデータをラッチ
        RCLK.high()
        utime.sleep_us(1)
        RCLK.low()
        utime.sleep_us(1)

    # LEDの点灯パターンをデモンストレーションするメインループ
    while True:
        # LEDをQ0からQ7まで1つずつ点灯
        for i in range(8):
            data = 1 << i
            shift_out(data)
            utime.sleep(0.2)
        # LEDをQ7からQ0まで逆順に点灯
        for i in range(7, -1, -1):
            data = 1 << i
            shift_out(data)
            utime.sleep(0.2)
        # 動くバーの効果を作成
        for i in range(9):
            data = (1 << i) - 1
            shift_out(data)
            utime.sleep(0.2)
        # 全てのLEDを消灯
        shift_out(0x00)
        utime.sleep(0.5)

コードを実行すると、74HC595シフトレジスタに接続されたLEDは動的な光のパターンを表示します：

* **最初のシーケンス**: LEDが左から右へ順番に点灯します。各LEDが順番に点灯し、光が横に移動する効果が得られます。
* **2番目のシーケンス**: LEDが右から左へ順番に点灯し、移動方向が逆転します。
* **3番目のシーケンス**: LEDが累積的に点灯して、左から右にバーが成長していく効果を作ります。
* **最終ステップ**: 全てのLEDが短時間で消灯し、その後シーケンスが繰り返されます。

これにより、光が左右に動き、バーが成長する視覚的に魅力的なディスプレイが得られ、シーケンスは連続して繰り返されます。

**コードの理解**

#. モジュールのインポート：

   * ``machine``: GPIOピンへのアクセスを提供します。
   * ``utime``: 時間に関連する関数を含んでいます。

#. 制御ピンの定義：

   74HC595に接続されたGPIOピンを定義します。

   .. code-block:: python

      SDI = machine.Pin(0, machine.Pin.OUT)   # データ入力
      RCLK = machine.Pin(1, machine.Pin.OUT)  # ラッチクロック
      SRCLK = machine.Pin(2, machine.Pin.OUT) # シフトクロック

#. シフトアウト関数：

   * この関数は8ビットのデータをシフトレジスタに送信します。
   * 最上位ビット（MSB）から送信します。
   * 各ビットをシフトするためにシフトレジスタクロック（SRCLK）をパルスさせます。
   * すべてのビットがシフトされた後、レジスタクロック（RCLK）をパルスさせてデータを出力にラッチします。

   .. code-block:: python

      def shift_out(data):
          for bit in range(8):
              bit_val = (data & 0x80) >> 7
              SDI.value(bit_val)
              SRCLK.high()
              utime.sleep_us(1)
              SRCLK.low()
              utime.sleep_us(1)
              data = data << 1
          RCLK.high()
          utime.sleep_us(1)
          RCLK.low()
          utime.sleep_us(1)

#. メインループ：

   * Q0からQ7まで各LEDを1つずつ点灯させます。

   .. code-block:: python

      for i in range(8):
          data = 1 << i
          shift_out(data)
          utime.sleep(0.2)


   * Q7からQ0まで各LEDを1つずつ逆順に点灯させます。

   .. code-block:: python

      for i in range(7, -1, -1):
          data = 1 << i
          shift_out(data)
          utime.sleep(0.2)

   * 徐々にLEDを点灯させて、Q0からQ7に向かってバーが成長する効果を作ります。

   .. code-block:: python

      for i in range(9):
          data = (1 << i) - 1
          shift_out(data)
          utime.sleep(0.2)

   * 0x00を送信して、すべてのLEDを消灯します。

   .. code-block:: python

     shift_out(0x00)
     utime.sleep(0.5)

**さらなる実験**

* カスタムパターンの作成：

  送信するデータを変更して、さまざまなLEDパターンを作成します。たとえば、交互のLEDを点滅させる場合：

  .. code-block:: python

    shift_out(0b10101010)

* より多くのLEDの制御：

  複数の74HC595チップをチェーン接続して、より多くの出力を制御します。最初のチップのQ7'（ピン9）を2番目のチップのDS（ピン14）に接続します。

* センサーとの統合：

  センサーやボタンの入力を使用して、LEDパターンを動的に変更します。

**結論**

このレッスンでは、74HC595シフトレジスタを使用してRaspberry Pi Pico 2 Wの出力機能を拡張する方法を学びました。この技術は、限られたGPIOピンで多くの出力を制御する必要があるプロジェクトに非常に役立ちます。

