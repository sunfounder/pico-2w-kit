.. note:: 

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32について、仲間たちと一緒にさらに深く学んでいきましょう。

    **参加する理由は？**

    - **専門的なサポート**：販売後の問題や技術的な課題を、コミュニティとチームのサポートを受けて解決できます。
    - **学びと共有**：スキルを高めるために、ヒントやチュートリアルを交換できます。
    - **限定プレビュー**：新製品の発表を早期に知り、先行して情報を得ることができます。
    - **特別割引**：最新製品の独占割引をお楽しみいただけます。
    - **フェスティブプロモーションとプレゼント**：プレゼント企画やホリデープロモーションに参加できます。

    👉 私たちと一緒に探索し、創造する準備はできましたか？[|link_sf_facebook|]をクリックして、今すぐ参加してください！

.. _py_button:

2.5 ボタン値の読み取り
==============================================

このレッスンでは、Raspberry Pi Pico 2 Wを使って、押しボタンの入力を読み取る方法を学びます。これまでGPIOピンを主に出力（LEDの点灯など）に使用してきましたが、今回はGPIOピンを入力として使用し、ボタンが押されたことを検出します。これはインタラクティブなプロジェクトを作成するための基本的な技術です。

* :ref:`cpn_button`

**必要な部品**

このプロジェクトで必要な部品は以下の通りです。

一式を購入するのが非常に便利です。こちらからリンクを確認してください：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前
        - このキットに含まれる部品
        - リンク
    *   - Pico 2 W スターターキット
        - 450+
        - |link_pico2w_kit|

下記のリンクから個別に購入することもできます。


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
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_button`
        - 1
        - |link_button_buy|

**回路図**

|sch_button|

ボタンの片側ピンが3.3Vに接続され、もう片側のピンがGP14に接続されている場合、ボタンが押されるとGP14は高信号（HIGH）になります。しかし、ボタンが押されていないとき、GP14は浮動状態にあり、高または低になる可能性があります。ボタンが押されていないときに安定した低レベル（LOW）を得るために、GP14は10Kのプルダウン抵抗を介してGNDに再接続する必要があります。

* **ボタンが押されていないとき**：GP14ピンは抵抗を通じてGNDに接続されているため、 **LOW（0）** と読み取られます。
* **ボタンが押されたとき**：GP14ピンはボタンを通じて3.3Vに接続されるため、 **HIGH（1）** と読み取られます。

**配線図**

.. Let's follow the direction of the circuit to build the circuit!

.. 1. Connect the 3V3 pin of Pico 2 W to the positive power bus of the breadboard.
.. #. Insert the button into the breadboard and straddle the central dividing line.

.. note:: 
    4ピンのボタンはHの形をしています。左右の2ピンまたは右側の2ピンが接続されており、中央のギャップを越えると、同じ行番号の2つの半分の行が接続されることを意味します。（例えば、私の回路では、E23とF23はすでに接続されており、E25とF25も同様です）。

    ボタンが押されるまで、左側と右側のピンは独立しており、片方の側からもう片方の側に電流が流れることはありません。

.. #. Use a jumper wire to connect one of the button pins to the positive bus (mine is the pin on the upper right).
.. #. Connect the other pin (upper left or lower left) to GP14 with a jumper wire.
.. #. Use a 10K resistor to connect the pin on the upper left corner of the button and the negative bus.
.. #. Connect the negative power bus of the breadboard to Pico's GND.

|wiring_button|

**コードの作成**

ボタンが押されたときにメッセージを表示する簡単なプログラムを書きます。

.. note::

  * ``pico-2w-kit-main/micropython`` の ``2.5_read_button_value.py`` を開くか、コードをThonnyにコピーして、「Run」をクリックするか、F5を押してください。
  * 正しいインタープリタが選択されていることを確認してください：MicroPython（Raspberry Pi Pico）。COMxx。

.. code-block:: python

    import machine
    import utime

    # GP14を入力ピンとして初期化
    button = machine.Pin(14, machine.Pin.IN)

    while True:
        if button.value() == 1:
            print("Button pressed!")
            utime.sleep(0.2)  # デバウンスのための遅延

コードが実行されると、次の現象が観察されます：

* **押されていないとき**：メッセージは表示されません。
* **押されたとき**：「ボタンが押されました！」というメッセージがコンソールに表示されます。



**コードの理解**

#. モジュールのインポート：

   * ``machine``：ハードウェア機能にアクセスするためのモジュール。
   * ``utime``：遅延などの時間関連の関数を使用するためのモジュール。

#. ボタンピンの設定：

   * ``button = machine.Pin(14, machine.Pin.IN)``：GPIOピン14を入力として初期化。

#. メインループ：

   * ``while True``：無限ループを作成します。
   * ``if button.value() == 1``：ボタンが押されたかどうかを確認します。
   * ``button.value()`` はボタンが押されていると1を返します（HIGH）。
   * ``print("Button pressed!")``：メッセージをコンソールに表示します。
   * ``utime.sleep(0.2)``：ボタンのデバウンスを行うために200ミリ秒の待機時間を設定します。

**代替配線：プルアップ抵抗**

ボタンをプルアップ抵抗を使用した設定で配線することもできます。

#. 10kΩの抵抗をGP14と3.3Vレールの間に接続します。これにより、ボタンが押されていないときにピンが高くなります。

    |sch_button_pullup|

    |wiring_button_pullup|

   * **ボタンが押されていないとき**：GP14ピンは抵抗を通じて3.3Vに接続されているため、 **HIGH（1）** と読み取られます。
   * **ボタンが押されたとき**：GP14ピンはボタンを通じてGNDに接続されるため、 **LOW（0）** と読み取られます。

#. プルアップ設定のための修正コード。

   .. code-block:: python
   
       import machine
       import utime
       
       # GP14を入力ピンとして初期化
       button = machine.Pin(14, machine.Pin.IN)
       
       while True:
           if button.value() == 0:
               print("Button pressed!")
               utime.sleep(0.2)

**内部プルアップ/プルダウン抵抗の使用**

Raspberry Pi Pico 2 Wでは、内部プルアップ抵抗またはプルダウン抵抗を有効にすることができ、外部抵抗が不要になります。

内部抵抗を使用することで配線が簡素化され、ブレッドボード上で追加の外部抵抗を省略できます。

* 内部プルダウン抵抗の有効化：

  .. code-block:: python
  
      import machine
      import utime
  
      # 内部プルダウン抵抗を使用してGP14を入力として初期化
      button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
  
      while True:
          if button.value() == 1:
              print("Button pressed!")
              utime.sleep(0.2)

* 内部プルアップ抵抗の有効化：

  .. code-block:: python

    import machine
    import utime

    # 内部プルアップ抵抗を使用してGP14を入力として初期化
    button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)

    while True:
        if button.value() == 0:
            print("Button pressed!")
            utime.sleep(0.2)

**さらに実験してみましょう**

* **複数のボタン**：他のGPIOピンに追加のボタンを接続し、コードを変更して複数の入力を処理します。
* **LED制御**：ボタン入力とLED出力を組み合わせて、ボタンが押されたときにLEDの状態を切り替えます。

.. code-block:: python

    import machine
    import utime

    button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
    led = machine.Pin(15, machine.Pin.OUT)
    led_state = False

    while True:
        if button.value() == 1:
            led_state = not led_state  # LEDの状態を切り替える
            led.value(led_state)
            utime.sleep(0.2)

**結論**

ボタンからの入力を読み取ることは、マイクロコントローラプログラミングの基本的な技術です。これにより、プロジェクトをインタラクティブにし、ユーザー入力に反応させることができます。プルアップおよびプルダウン抵抗を使う方法を理解することで、入力デバイスからの信頼性の高い安定した読み取りが保証されます。
