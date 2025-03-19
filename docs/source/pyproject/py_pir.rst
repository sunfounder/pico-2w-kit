.. note:: 

    こんにちは！FacebookのSunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Raspberry Pi、Arduino、ESP32を深く学び、仲間たちと一緒に探求していきましょう。

    **なぜ参加するのか？**

    - **専門的なサポート**: コミュニティやチームのサポートで、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換し、スキルを向上させましょう。
    - **独占的な先行公開**: 新製品の発表や先取り情報に早期アクセスできます。
    - **特別割引**: 最新製品の特別割引を楽しめます。
    - **祭りのプロモーションとギブアウェイ**: ギブアウェイやホリデープロモーションに参加できます。

    👉 私たちと一緒に探索し、創造を始めましょう！[|link_sf_facebook|]をクリックして、今すぐ参加してください！

.. _py_pir:

2.10 人間の動きを検出する
========================================

このレッスンでは、Raspberry Pi Pico 2 Wを使用して **パッシブ赤外線（PIR）センサー** を使い、人間の動きを検出する方法を学びます。PIRセンサーは、セキュリティシステム、オートマチックライティング、その他動きの検出が必要な用途でよく使用されます。これらのセンサーは、暖かい物体（人間や動物など）から放射される赤外線を検出します。

:ref:`cpn_pir`

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
        - :ref:`cpn_pir`
        - 1
        - |link_pir_buy|


**回路図**

|sch_pir|

PIRモジュールが人が通り過ぎるのを検出すると、GP14がHIGHになります。それ以外の場合はLOWになります。

.. note::

    PIRセンサーには2つのポテンショメーターがあります：

    * **感度調整**: 検出範囲を制御します。
    * **時間遅延調整**: 動きが検出された後、出力がHIGHのままでいる時間を制御します。

    初期テストでは、両方のポテンショメーターを反時計回りに最小位置に設定してください。これにより、センサーは最も感度が高く、最短の遅延設定になります。これで、すぐに反応を観察できます。

    |img_PIR_TTE|

**配線**

|wiring_pir|

**コードの記述**

動きを検出するために割り込みを使用し、動きが検出されるとメッセージを表示するMicroPythonプログラムを作成します。

.. note::

    * ``pico-2w-kit-main/micropython`` の ``2.10_detect_human_movement.py`` ファイルを開くか、以下のコードをThonnyにコピーします。次に「実行」をクリックするか、F5を押して実行します。


    * Thonnyの右下に「MicroPython（Raspberry Pi Pico）.COMxx」のインタープリタが選択されていることを確認してください。

.. code-block:: python

    import machine
    import utime

    # GP14を入力ピンとして初期化
    pir_sensor = machine.Pin(14, machine.Pin.IN)

    def motion_detected(pin):
        print("Motion detected!")

    # 立ち上がりエッジで割り込みを設定
    pir_sensor.irq(trigger=machine.Pin.IRQ_RISING, handler=motion_detected)

    # メインループは何もしません。割り込みが動作を処理します。
    while True:
        utime.sleep(1)

コードを実行すると、次の現象が観察されます：

* PIRセンサーの前で動きます。
* 動きが検出されると、「Motion detected!」というメッセージがコンソールに表示されます。

**コードの理解**

#. モジュールのインポート：

   * ``import machine``: ハードウェア関連の関数にアクセスします。
   * ``import utime``: 時間関連の関数を使用します。

#. PIRセンサーピンの初期化：

   * ``pir_sensor = machine.Pin(14, machine.Pin.IN)``: GP14を入力ピンとして設定します。

#. 割り込みハンドラの定義：

   * ``def motion_detected(pin)``: 動きが検出されたときに呼ばれる関数。
   * ``print("Motion detected!")``: コンソールにメッセージを出力します。

#. 割り込みの設定：

   * ``pir_sensor.irq(trigger=machine.Pin.IRQ_RISING, handler=motion_detected)``: PIRセンサーの信号の立ち上がりエッジで割り込みを設定します。

#. メインループ：

   * ``while True``: 無限ループを開始します。
   * ``utime.sleep(1)``: ループは1秒間スリープし、割り込みが動作を処理します。

**動作時間を測定するためのコード例**

コードを変更して、動作検出の時間と検出間隔を測定することができます。

.. code-block:: python

    import machine
    import utime

    pir_sensor = machine.Pin(14, machine.Pin.IN)

    last_trigger_time = utime.ticks_ms()

    def pir_triggered(pin):
        global last_trigger_time
        current_time = utime.ticks_ms()
        duration = utime.ticks_diff(current_time, last_trigger_time)
        last_trigger_time = current_time

        if pir_sensor.value():
            print("Motion detected! Duration since last detection: {} ms".format(duration))
        else:
            print("Motion ended. Duration of motion: {} ms".format(duration))

    # 立ち上がりエッジと下降エッジの両方で割り込みを設定
    pir_sensor.irq(trigger=machine.Pin.IRQ_RISING | machine.Pin.IRQ_FALLING, handler=pir_triggered)

    while True:
        utime.sleep(1)

* 両方のエッジでの割り込み： ``machine.Pin.IRQ_RISING`` | ``machine.Pin.IRQ_FALLING`` を使用して、立ち上がりエッジと下降エッジで割り込みを設定します。
* 時間の追跡：

  * ``utime.ticks_ms()`` を使用して、現在の時間をミリ秒単位で取得します。
  * トリガー間の時間を計算して、PIRセンサー出力が ``HIGH`` または ``LOW`` の状態でいる時間を測定します。

**実用的な応用**

* **セキュリティシステム**: 不正侵入者や許可されていない動きを検出します。
* **自動照明**: 動きが検出されたときにライトをオンにします。
* **省エネルギー**: 一定時間動きが検出されない場合にデバイスをオフにします。

**トラブルシューティングのヒント**

* 誤動作：

  * PIRセンサーは温度変化や日光などの環境要因に敏感です。
  * センサーを熱源や窓に向けて設置しないようにしましょう。

* センサーが動きを検出しない：

  * センサーが初期化するまでに時間がかかる場合があります（一部のセンサーでは最大60秒かかることがあります）。
  * 感度ポテンショメーターを調整します。

* 干渉：

  * センサーを電子機器から離して設置し、電磁干渉を避けます。

**結論**

PIRセンサーをRaspberry Pi Pico 2 Wに統合することで、プロジェクトに動作検出機能を追加する方法を学びました。センサー入力を読み取り、割り込みを処理する方法を理解することで、反応的で効率的なプログラムを作成できます。


