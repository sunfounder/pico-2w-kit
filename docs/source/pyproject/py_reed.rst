.. note::

    こんにちは！FacebookのSunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Raspberry Pi、Arduino、ESP32について、仲間たちと一緒にさらに深く学びましょう。

    **なぜ参加するのか？**

    - **専門的なサポート**: コミュニティやチームからのサポートで、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換して、スキルを向上させましょう。
    - **独占的な先行公開**: 新製品の発表や先取り情報に早期アクセスできます。
    - **特別割引**: 最新製品の特別割引を楽しめます。
    - **祭りのプロモーションとギブアウェイ**: ギブアウェイやホリデープロモーションに参加できます。

    👉 私たちと一緒に探索し、創造を始めましょう！[|link_sf_facebook|]をクリックして、今すぐ参加してください！

.. _py_reed:

2.9 磁場を感じる
================================

このレッスンでは、Raspberry Pi Pico 2 Wを使って **リードスイッチ** を使用し、磁場の存在を検出する方法を学びます。リードスイッチは、磁場を利用して動作する単純な電気的スイッチです。磁石がスイッチに近づくと、その内部の接点が閉じ、電気回路が完成します。

* :ref:`cpn_reed`

**必要な部品**

このプロジェクトで必要な部品は以下の通りです。

全ての部品がセットになったキットを購入するのが便利です。こちらのリンクをご覧ください：

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
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_reed`
        - 1
        - 

**リードスイッチの理解**

リードスイッチは、ガラスのカプセル内に密閉された2本の細い金属のリードで構成されています。これらのリードは強磁性の素材でできており、わずかに離れた位置に配置されています。磁場がない場合、リードは離れており、スイッチは **オープン** の状態です。磁石がスイッチに近づくと、リードが磁化され、互いに引き寄せられて回路を閉じます。

* **近くに磁石がない場合**: スイッチは **オープン** で、回路は未完成です。
* **磁石が近くにある場合**: スイッチは **クローズド** で、回路は完成します。

|img_reed_sche|

**回路図**

|sch_reed|

デフォルトでは、GP14は低い状態で、磁石がリードスイッチの近くにあるとGP14は高い状態に変わります。

10KΩの抵抗は、磁石が近くにない場合にGP14を一定の低レベルに保つ役割を果たします。

* **近くに磁石がない場合**:

  * リードスイッチは **オープン** です。
  * **GP14** はプルダウン抵抗を通じて **GND** に接続されます。
  * GPIOピンは **LOW** （0）を読み取ります。

* **磁石が近くにある場合**:

  * リードスイッチは **クローズド** です。
  * **GP14** はリードスイッチを通じて **3.3V** に接続されます。
  * GPIOピンは **HIGH** （1）を読み取ります。

**配線**

|wiring_reed|

**コードの記述**

磁石がリードスイッチの近くにあると検出し、それに応じてメッセージを表示するMicroPythonプログラムを記述します。

.. note::

  * ``pico-2w-kit-main/micropython`` から ``2.9_feel_the_magnetism.py`` ファイルを開くか、以下のコードをThonnyにコピーして、「実行」をクリックするか、F5を押して実行します。
  * 正しいインタープリター「MicroPython（Raspberry Pi Pico）」が右下に選択されていることを確認してください。 

.. code-block:: python

    import machine
    import utime

    # GP14を入力ピンとして初期化
    reed_switch = machine.Pin(14, machine.Pin.IN)

    while True:
        if reed_switch.value() == 1:
            print("Magnet detected!")
            utime.sleep(1)  # 複数回検出されないように遅延を挿入

コードを実行すると、次の現象が観察されます。

* **磁石が近くにない場合**: メッセージは表示されません。
* **磁石を近づけると**: 「磁石が検出されました！」というメッセージがコンソールに表示されます。
* **磁石を遠ざけると**: メッセージは表示されなくなります。

**コードの理解**

#. モジュールのインポート：

   * ``import machine``: ハードウェア関連の関数にアクセスします。
   * ``import utime``: 時間関連の関数を提供します。

#. リードスイッチのピンの初期化：

   * ``reed_switch = machine.Pin(14, machine.Pin.IN)``: GP14を入力ピンとして設定します。

#. メインループ：

   * ``while True``: 無限ループを開始します。
   * ``if reed_switch.value() == 1``: 磁石が近くにあるかどうかを確認します（GPIOピンがHIGHを読み取る）。
   * ``print("Magnet detected!")``: メッセージを表示します。
   * ``utime.sleep(1)``: メッセージが連続して表示されないように遅延を追加します。

**効率的な検出のための割り込みの使用**

リードスイッチをループで常にポーリングする代わりに、割り込みを使用してリードスイッチの状態の変化をより効率的に検出できます。

割り込みを使用すると、リードスイッチの状態を継続的にチェックする必要がなくなり、イベントが発生したときにすぐにハンドラ関数を呼び出すことで、応答性が向上します。

割り込みを使用したコードの修正。磁石をリードスイッチに近づけると、「磁石が検出されました！」というメッセージが表示されます。メインプログラムは他のタスクを実行し続けます。

.. code-block:: python

    import machine

    # GP14を入力ピンとして内部プルダウン抵抗を使用して初期化
    reed_switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

    def magnet_detected(pin):
        print("Magnet detected!")

    # 上昇エッジ（LOWからHIGHへの遷移）で割り込みを設定
    reed_switch.irq(trigger=machine.Pin.IRQ_RISING, handler=magnet_detected)

* ``def magnet_detected(pin)``: この関数は、割り込みがトリガーされたときに自動的に呼び出されます。


  * ``print("Magnet detected!")``: 磁石が検出された時にメッセージを表示します。

* ``reed_switch.irq(trigger=machine.Pin.IRQ_RISING, handler=magnet_detected)``: リードスイッチピンに割り込みを設定します。
  
  * ``trigger=machine.Pin.IRQ_RISING``: 上昇エッジで割り込みがトリガーされます（ピンの値がLOWからHIGHに変わるとき）。
  * ``handler=magnet_detected``: 割り込みが発生したときに呼び出す関数を指定します。

**実践的な応用**

* **セキュリティシステム**: ドアや窓が開いたときの検出。
* **位置検出**: 機械の移動部品の位置を判定する。
* **近接検出**: 磁性の物体が近づいたときにイベントをトリガーする。

**さらなる実験**

* LEDを制御する：

  他のGPIOピン（例：GP15）にLEDを接続し、適切な抵抗を使用します。割り込みハンドラを変更して、磁石が検出されたときにLEDを点灯させます。

  .. code-block:: python
  
      import machine
  
      reed_switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
      led = machine.Pin(15, machine.Pin.OUT)
  
      def magnet_detected(pin):
          led.value(1)  # LEDを点灯
  
      # 上昇エッジで割り込みを設定
      reed_switch.irq(trigger=machine.Pin.IRQ_RISING, handler=magnet_detected)
  
      # メインループ
      while True:
          # 磁石がないときにLEDを消灯
          if reed_switch.value() == 0:
              led.value(0)
          machine.sleep(100)

* 磁石の取り外しを検出：

  磁石が離れたときに割り込みを設定します。

  .. code-block:: python

    def magnet_removed(pin):
        print("Magnet removed!")

    reed_switch.irq(trigger=machine.Pin.IRQ_FALLING, handler=magnet_removed)

**結論**

Raspberry Pi Pico 2 Wでリードスイッチを使用することにより、磁場の存在を検出できるようになり、セキュリティシステムやインタラクティブなプロジェクトなど、幅広い用途に活用できます。リードスイッチを接続し、割り込みを活用する方法を理解することで、効率的で反応の速いプログラムを作成できるようになります。

**参考文献**

* |link_mpython_irq|