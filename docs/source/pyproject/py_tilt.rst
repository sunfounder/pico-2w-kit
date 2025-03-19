.. note::

    こんにちは！FacebookのSunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！仲間たちと一緒にRaspberry Pi、Arduino、ESP32についてさらに深く学びましょう。

    **参加する理由は？**

    - **専門的なサポート**: 当コミュニティとチームの助けを借りて、販売後の問題や技術的な課題を解決できます。
    - **学び・共有**: スキルを向上させるためのヒントやチュートリアルを交換しましょう。
    - **特別なプレビュー**: 新製品の発表やプレビューに早期アクセスできます。
    - **特別割引**: 最新製品の独占的な割引を楽しめます。
    - **フェスティブなプロモーションとプレゼント企画**: プレゼント企画やホリデープロモーションに参加できます。

    👉 私たちと一緒に探索し、創造を始める準備はできましたか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _py_tilt:


2.6 倾斜スイッチ
==========================

|img_tilt|

このレッスンでは、Raspberry Pi Pico 2 Wを使用して、 **傾斜スイッチ** を使い、方向の変化を検出する方法を学びます。傾斜スイッチは、立っているか、傾いているかを感知できるシンプルなデバイスで、動作検出や方向感知、位置に基づいたトリガーとして役立ちます。

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
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_tilt`
        - 1
        - 

**回路図**

|sch_tilt|

* **直立時（スイッチが閉じている場合）**:

  * 傾斜スイッチは **3.3V** を直接 **GP14** に接続します。
  * GPIOピンは **HIGH** （1）を読み取ります。

* **傾いた場合（スイッチが開く）**:

  * 傾斜スイッチは **3.3V** を **GP14** から切り離します。
  * プルダウン抵抗器が **GP14** を **GND** に引きます。
  * GPIOピンは **LOW** （0）を読み取ります。

* :ref:`cpn_tilt`

**配線**

|wiring_tilt|



**コードの作成**

傾斜スイッチの状態を検出し、スイッチが傾いたときにメッセージを表示するシンプルなMicroPythonプログラムを作成します。

.. note::

    * ``2.6_tilt_switch.py`` を ``pico-2w-kit-main/micropython`` から開くか、このコードをThonnyにコピーして「Run」をクリックするか、F5キーを押して実行します。
    * 正しいインタープリターが選択されていることを確認してください：MicroPython（Raspberry Pi Pico）。COMxx。

.. code-block:: python

    import machine
    import utime

    # GP14を入力ピンとして初期化
    tilt_switch = machine.Pin(14, machine.Pin.IN)

    while True:
        if tilt_switch.value() == 0:
            print("Tilt detected!")
            utime.sleep(1)  # 連続して検出されないように遅延を追加

コードが実行されると、次の現象が観察されます：

* 傾斜スイッチを直立させておくと、メッセージは表示されません。
* ブレッドボードやスイッチを傾けると、「傾斜検出！」とコンソールに表示されます。

**コードの理解**

#. モジュールのインポート：

   * ``import machine``: ハードウェアコンポーネントにアクセスするため。
   * ``import utime``: 時間に関連する関数を使用するため。

#. 傾斜スイッチピンの初期化：

   * ``tilt_switch = machine.Pin(14, machine.Pin.IN)``: GP14を入力ピンとして設定します。

#. メインループ：

   * ``while True``: 傾斜スイッチの状態を継続的にチェックする無限ループを作成します。
   * ``if tilt_switch.value() == 0``: GPIOピンがLOW（0）を読み取った場合、スイッチが傾いていることを確認します。
   * ``print("Tilt detected!")``: 傾斜を検出した場合にメッセージを出力します。
   * ``utime.sleep(1)``: スイッチが複数回連続して検出されるのを防ぐために1秒の遅延を加えます。

**代替配線: 内部プルダウン抵抗器の使用**

Raspberry Pi Pico 2 Wでは、内部プルアップまたはプルダウン抵抗器を有効にして、外部の抵抗器を省略できます。

.. code-block:: python

    import machine
    import utime

    # 内部プルダウン抵抗器を使ってGP14を入力ピンとして初期化
    tilt_switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

    while True:
        if tilt_switch.value() == 1:
            print("Tilt detected!")
            utime.sleep(1)

内部プルダウン抵抗器（ ``machine.Pin.PULL_DOWN`` ）を有効にすると、電圧がかかっていないときにGPIOピンはLOWに設定されます。
傾斜スイッチが直立している（閉じている）場合、3.3VがGP14に接続され、ピンはHIGH（1）を読み取ります。

**実用的な応用**

* **方向検出**: デバイスが直立しているか、傾いているかを判定できます。
* **動作トリガーイベント**: 動きが検出されたときにアラームや通知、アクションを起動できます。
* **インタラクティブプロジェクト**: 傾きを感知して、ゲームやインタラクション型のプロジェクトに入力として使用できます。

**さらに実験する**

* LEDインジケーターを追加：

他のGPIOピン（例えば、GP15）に適切な抵抗を介してLEDを接続します。傾斜が検出されたときにLEDを点灯させるようにコードを修正します。

.. code-block:: python

    import machine
    import utime

    tilt_switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
    led = machine.Pin(15, machine.Pin.OUT)

    while True:
        if tilt_switch.value() == 1:
            print("Tilt detected!")
            led.value(1)  # LEDをオンにする
            utime.sleep(1)
        else:
            led.value(0)  # LEDをオフにする

* 他のセンサーと組み合わせて使用：

ボタンや光センサーなど、他のセンサーと組み合わせてさらに複雑なインタラクションを作り出すことができます。

**結論**

Raspberry Pi Pico 2 Wのプロジェクトに傾斜スイッチを組み込むことで、方向や動きに基づいた新しいインタラクションの次元を追加できます。傾斜スイッチのようなセンサーからデジタル入力を読み取る方法を理解することで、動的で反応的な電子機器を作成する能力が広がります。
