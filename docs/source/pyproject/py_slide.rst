.. note::

    こんにちは！FacebookのSunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！仲間たちと一緒にRaspberry Pi、Arduino、ESP32についてさらに深く学びましょう。

    **参加する理由は？**

    - **専門的なサポート**: 当コミュニティとチームの助けを借りて、販売後の問題や技術的な課題を解決できます。
    - **学び・共有**: スキルを向上させるためのヒントやチュートリアルを交換しましょう。
    - **特別なプレビュー**: 新製品の発表やプレビューに早期アクセスできます。
    - **特別割引**: 最新製品の独占的な割引を楽しめます。
    - **フェスティブなプロモーションとプレゼント企画**: プレゼント企画やホリデープロモーションに参加できます。

    👉 私たちと一緒に探索し、創造を始める準備はできましたか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _py_slide:

2.7 左右切り替えスイッチ
====================================

|img_slide|

このレッスンでは、Raspberry Pi Pico 2 Wを使用して **スライドスイッチ** を使い、スイッチの位置（左または右）を検出し、それに基づいてアクションを実行する方法を学びます。スライドスイッチは、スイッチの位置に応じて共通ピン（中央のピン）を2つの外部ピンのいずれかに接続するシンプルな機械的なデバイスです。

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
        - :ref:`cpn_capacitor`
        - 1(104)
        - |link_capacitor_buy|
    *   - 7
        - :ref:`cpn_slide_switch`
        - 1
        - 

**回路図**

|img_slide|

スライドスイッチには3つのピンがあります：

- **ピン1**: スイッチが一方の側（例えば左側）に切り替わったときに接続される
- **ピン2**: 共通ピン（中央のピン）
- **ピン3**: スイッチがもう一方の側（例えば右側）に切り替わったときに接続される

共通ピンの電圧を読み取ることで、スイッチの位置を判別できます。

**回路図**

|sch_slide|

スイッチを左または右に切り替えると、GP14のピンが異なるレベルになります。

10KΩの抵抗の目的は、スイッチを切り替えてもGP14が低い状態（端まで切り替えていない状態）を維持することです。

スイッチを切り替えると、機械的な接点により急速で騒がしい信号（バウンス）が発生することがあります。GP14とGNDの間に接続されたコンデンサは、これらの急激な変動をフィルタリングし、よりクリーンな信号を提供します。

* スイッチを右に切り替えた場合：

  * ピン2（GP14）はピン1を介して **3.3V** に接続されます。
  * GPIOピンは **HIGH** （1）を読み取ります。

* スイッチを左に切り替えた場合：

  * ピン2（GP14）はピン3を介して **GND** に接続されます。
  * GPIOピンは **LOW** （0）を読み取ります。

* スイッチが中央にある場合：

  * ピン2（GP14）は **3.3V** や **GND** のいずれにも接続されません。
  * プルダウン抵抗によりGPIOピンは **LOW** （0）に保たれます。
  * コンデンサはスイッチのバウンス（機械的動作によるノイズ）を減少させるのに役立ちます。

**配線**

|wiring_slide|

**コードの作成**

スライドスイッチの位置を検出し、それに応じてメッセージを表示するMicroPythonプログラムを作成します。

.. note::

  * ``2.7_slide_switch.py`` を ``pico-2w-kit-main/micropython`` から開くか、このコードをThonnyにコピーして「Run」をクリックするか、F5キーを押して実行します。

  * 正しいインタープリターが選択されていることを確認してください：MicroPython（Raspberry Pi Pico）。COMxx。 
  

.. code-block:: python

  import machine
  import utime

  # GP14を入力ピンとして初期化
  slide_switch = machine.Pin(14, machine.Pin.IN)

  while True:
      switch_state = slide_switch.value()
      if switch_state == 1:
          print("Switch is toggled to the LEFT!")
      else:
          print("Switch is toggled to the RIGHT!")
      utime.sleep(0.5)

コードを実行すると、次の現象が観察されます：

* **右に切り替えた場合**: コンソールに「スイッチは右に切り替わっています！」と表示されます。
* **左に切り替えた場合**: コンソールに「スイッチは左に切り替わっています！」と表示されます。

**コードの理解**

#. モジュールのインポート：

   * ``import machine``: ハードウェア関連の機能にアクセスします。
   * ``import utime``: 時間関連の関数を使用します。

#. スライドスイッチピンの初期化：

   * ``slide_switch = machine.Pin(14, machine.Pin.IN)``: GP14を入力ピンとして設定します。

#. メインループ：

* ``while True``: スイッチの状態を継続的に確認する無限ループを作成します。
* ``switch_state = slide_switch.value()``: スイッチの現在の状態を読み取ります。
* ``if switch_state == 1``: GPIOピンがHIGH（スイッチが左に切り替わった）かどうかを確認します。
* ``print("Switch is toggled to the RIGHT!")``: メッセージを表示します。
* ``else``: GPIOピンがLOW（スイッチが右に切り替わったか、中央にある）場合。
* ``print("Switch is toggled to the LEFT!")``: メッセージを表示します。
* ``utime.sleep(0.5)``: スイッチのデバウンス処理を行い、コンソールがフラッドしないように短い遅延を加えます。


**代替案：内部プルダウン抵抗を使用**

Raspberry Pi Pico 2 Wでは、内部プルダウン抵抗を有効にすることで外部抵抗が不要になります。

* 回路の変更：

  外部の10 kΩ抵抗と0.1 µFコンデンサを取り外します。

* 修正コード：

  .. code-block:: python

    import machine
    import utime

    # 内部プルダウン抵抗を使用してGP14を入力として初期化
    slide_switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

    while True:
        switch_state = slide_switch.value()
        if switch_state == 1:
            print("Switch is toggled to the LEFT!")
        else:
            print("Switch is toggled to the RIGHT!")
        utime.sleep(0.5)

**実際の応用**

* **モード選択**: プログラム内で異なるモードを切り替えるためにスイッチを使用します。
* **電源制御**: 回路の特定の部分に電源を供給する制御を行います。
* **ユーザー入力**: プロジェクトでシンプルなユーザーコントロールを提供します。

**さらに実験する**

* LEDインジケーターの追加：

  他のGPIOピン（例：GP15）にLEDを接続し、スイッチの位置に基づいてLEDをオンまたはオフにするようにコードを変更します。

  .. code-block:: python

    import machine
    import utime

    slide_switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
    led = machine.Pin(15, machine.Pin.OUT)

    while True:
        if slide_switch.value() == 1:
            led.value(1)  # LEDをオンにする
        else:
            led.value(0)  # LEDをオフにする
        utime.sleep(0.1)

* 中央位置の検出：

  スイッチが中央にある（左でも右でもない）場合を検出するには、配線とコードを変更して、すべての3つの状態を読み取るようにします。

**結論**

Raspberry Pi Pico 2 Wを使ってスライドスイッチを使用することで、プロジェクトに物理的な入力制御を追加できます。スイッチの状態を読み取る方法や、スイッチのバウンスなどの問題を処理する方法を理解することで、よりインタラクティブでユーザーフレンドリーなアプリケーションを作成することができます。
