.. note::

    こんにちは！FacebookのSunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！仲間たちと一緒にRaspberry Pi、Arduino、ESP32についてさらに深く学びましょう。

    **参加する理由は？**

    - **専門的なサポート**: 購入後の問題や技術的な課題を、コミュニティやチームのサポートで解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換して、スキルを向上させましょう。
    - **特別な先行公開**: 新しい製品の発表や先取り情報をいち早く手に入れましょう。
    - **特別割引**: 最新製品をお得に購入できる割引を提供します。
    - **フェスティブプロモーションとプレゼント**: プレゼント企画や季節のプロモーションに参加しましょう。

    👉 さあ、私たちと一緒に探索と創造を始めませんか？ [|link_sf_facebook|] をクリックして、今すぐ参加しましょう！

.. _py_micro:

2.8 優しく押す
==========================

|img_micro_switch|

このレッスンでは、 **マイクロスイッチ** （リミットスイッチとも呼ばれる）をRaspberry Pi Pico 2 Wで使用し、押されたときや放されたときにそれを検出する方法を学びます。マイクロスイッチは、電子レンジの扉やプリンターのカバー、3Dプリンターのエンドストップなどのデバイスに一般的に使用されており、信頼性が高く、頻繁に作動を扱うことができます。

* :ref:`cpn_micro_switch`

**必要な部品**

このプロジェクトでは、以下の部品が必要です。

キットを購入するのが便利なので、こちらのリンクをご参照ください：

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
        - 数個
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_resistor`
        - 1（10KΩ）
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_capacitor`
        - 1（104）
        - |link_capacitor_buy|
    *   - 7
        - :ref:`cpn_micro_switch`
        - 1
        - 

**マイクロスイッチの理解**

マイクロスイッチには通常、3つのピンがあります：

|img_micro_switch|

- **コモン（C）**: 中央のピン。
- **ノーマリーオープン（NO）**: スイッチが **押されたとき** にコモンピンに接続されます。
- **ノーマリークローズド（NC）**: スイッチが **押されていないとき** にコモンピンに接続されます。

スイッチを適切に接続することで、GPIOピンの電圧レベルを読み取ることでスイッチが押されたかどうかを検出できます。

**回路図**

|sch_limit_sw|

デフォルトでは、GP14は低レベルで、押すとGP14は高レベルになります。

10KΩの抵抗の目的は、押されたときにGP14を低レベルに保つことです。

機械式スイッチを押すと、接点がバウンスし、開閉状態が急激に切り替わることがあります。GP14とGNDの間に接続されたコンデンサは、このノイズを除去するのに役立ちます。

* **スイッチが押されていない場合**：

  * **コモン（C）**ピンは、 **NC** ピンに接続され、 **GND** に接続されます。
  * **GP14** は **LOW** （0V）を読み取ります。

* **スイッチが押された場合**：

  * **コモン（C）**ピンは、 **NO** ピンに接続され、 **3.3V** に接続されます。
  * **GP14** は **HIGH** （3.3V）を読み取ります。


**配線**

|wiring_limit_sw|


**コードの作成**

マイクロスイッチが押されたときに、それを検出してメッセージを表示するMicroPythonプログラムを作成します。

.. note::

  * ``pico-2w-kit-main/micropython`` から ``2.8_micro_switch.py`` を開くか、コードをThonnyにコピーして、「実行」をクリックするか、F5を押します。

  * 正しいインタープリターが選択されていることを確認してください：MicroPython（Raspberry Pi Pico）.COMxx。 

  

.. code-block:: python

    import machine
    import utime

    # GP14を入力ピンとして初期化
    switch = machine.Pin(14, machine.Pin.IN)

    while True:
        if switch.value() == 1:
            print("The switch is pressed!")
            utime.sleep(0.5)  # デバウンス遅延

コードが実行されると、次の現象が観察されます：

* **押されていない場合**: メッセージは表示されません。
* **押された場合**: スイッチを押すたびに「スイッチが押されました！」というメッセージがコンソールに表示されます。

**コードの理解**

#. モジュールのインポート：

   * ``import machine``: ハードウェア関数へのアクセス。
   * ``import utime``: 時間関連の関数。

#. スイッチピンの初期化：

   * ``switch = machine.Pin(14, machine.Pin.IN)``: GP14を入力ピンとして設定。

#. メインループ：

   * ``while True``: 無限ループを開始。
   * ``if switch.value() == 1``: スイッチが押されたかどうかを確認（GP14がHIGHを読み取る）。
   * ``print("スイッチが押されました！")``: コンソールにメッセージを表示。
   * ``utime.sleep(0.5)``: スイッチのデバウンスを防ぐために遅延を追加。

**内部プルダウン抵抗を使用した代替配線**

さらに配線を簡素化したい場合は、内部プルダウン抵抗を使用することができます：

* 回路の変更：

  * 外部の10 kΩ抵抗と0.1 µFコンデンサを取り外します。
  * マイクロスイッチ接続：

    * **コモン（C）端子**: GP14に接続。
    * **ノーマリーオープン（NO）端子**: 3.3Vに接続。
    * **ノーマリークローズド（NC）端子**: 接続しない。

* 修正されたコード：

  .. code-block:: python

      import machine
      import utime

      # 内部プルダウン抵抗を使用してGP14を入力ピンとして初期化
      switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

      while True:
          if switch.value() == 1:
              print("The switch is pressed!")
              utime.sleep(0.5)  # デバウンス遅延
     

**実用的な応用**

* **リミット検出**: CNC機械や3Dプリンターで、動きの限界を検出するためにマイクロスイッチを使用します。
* **安全インターロック**: 特定の条件が満たされたときのみデバイスが動作するようにします（例：ドアが閉まっている場合）。
* **ユーザー入力**: 頑丈で信頼性のあるボタンが必要なプロジェクトに組み込みます。

**さらに実験する**

* LEDの制御：

  別のGPIOピン（例：GP15）にLEDを接続し、適切な抵抗を使用します。コードを変更して、スイッチが押されたときにLEDを点灯させます。
  
  .. code-block:: python
    
    import machine
    import utime

    switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
    led = machine.Pin(15, machine.Pin.OUT)

    while True:
        if switch.value() == 1:
            led.value(1)  # LEDを点灯
            print("The switch is pressed!")
            utime.sleep(0.5)
        else:
            led.value(0)  # LEDを消灯

* プレス回数のカウント：

  コードを変更して、スイッチが押された回数をカウントします。

  * LEDを制御：

   .. code-block:: python

      import machine
      import utime

      switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
      count = 0

      while True:
          if switch.value() == 1:
              count += 1
              print("Switch pressed {} times".format(count))
              utime.sleep(0.5)

**結論**

Raspberry Pi Pico 2 Wでマイクロスイッチを使用することで、物理的なインタラクションを信頼性高く検出できます。スイッチをどのように配線し、その状態をコードで読み取るかを理解することは、反応性の高いインタラクティブなプロジェクトを作成するために重要です。

