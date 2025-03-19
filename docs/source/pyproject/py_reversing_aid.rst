.. note::

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Raspberry Pi、Arduino、ESP32について、他の愛好者とともにさらに深く学びましょう。

    **なぜ参加するのか？**

    - **専門的サポート**: コミュニティとチームのサポートで、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換して、スキルを向上させましょう。
    - **独占的先行公開**: 新製品の発表や先取り情報を早期に手に入れましょう。
    - **特別割引**: 最新製品の特別割引を享受できます。
    - **祭りのプロモーションとギブアウェイ**: ギブアウェイやホリデープロモーションに参加できます。

    👉 私たちと一緒に探索し、創造を始めましょう！[|link_sf_facebook|]をクリックして、今すぐ参加してください！

.. _py_reversing_aid:

7.10 リバースアシストシステムの構築
=====================================

このプロジェクトでは、Raspberry Pi Pico 2 W、超音波センサー、LED、ブザーを使用して **リバースアシストシステム** を作成します。
このシステムは、実際の駐車センサーがどのように機能するかをシミュレートし、障害物との距離を測定し、近づくにつれて変化する音と視覚的フィードバックを提供します。
このセットアップをリモートコントロールカーに取り付けて、ガレージにバックする体験を模倣できます。

**必要な部品**

このプロジェクトに必要な部品は以下の通りです。

キットを購入するのが非常に便利です。こちらのリンクをご覧ください：


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
        - :ref:`cpn_transistor`
        - 1(S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_resistor`
        - 2(1KΩ, 220Ω)
        - |link_resistor_buy|
    *   - 7
        - アクティブ :ref:`cpn_buzzer`
        - 1
        - 
    *   - 8
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 9
        - :ref:`cpn_ultrasonic`
        - 1
        - |link_ultrasonic_buy|

**コンポーネントの理解**

* **超音波センサー（HC-SR04）**: 超音波波を発信し、その反射が帰ってくるまでの時間を測定することで、物体までの距離を測ります。
* **ブザー**: 音でフィードバックを提供します。物体が近づくと、より頻繁に音を鳴らします。
* **LED**: 視覚的なフィードバックを提供します。物体が近づくにつれて、点滅速度が速くなります。

**回路図**

|sch_reversing_aid|


**配線**

|wiring_reversing_aid|

**コードの作成**

以下のMicroPythonスクリプトを作成します：

* 超音波センサーを使用して距離を測定します。
* 距離に応じてブザーの音の頻度とLEDの点滅速度を調整します。
* 物体が近づいたり遠ざかったりする際に、連続的にフィードバックを提供します。

.. note::

    * ``pico-2w-kit-main/micropython`` から ``7.10_reversing_aid.py`` ファイルを開くか、このコードをThonnyにコピーして、「実行」をクリックするか、F5を押して実行します。
    * 正しいインタープリター「MicroPython（Raspberry Pi Pico）」が右下に選択されていることを確認してください。

.. code-block:: python

    import machine
    import utime

    # ピンの設定
    trigger = machine.Pin(17, machine.Pin.OUT)
    echo = machine.Pin(16, machine.Pin.IN)
    buzzer = machine.Pin(15, machine.Pin.OUT)
    led = machine.Pin(14, machine.Pin.OUT)

    # 距離を測定する関数
    def measure_distance():
        # トリガーを低く設定
        trigger.low()
        utime.sleep_us(2)
        # トリガーに10usパルスを送信
        trigger.high()
        utime.sleep_us(10)
        trigger.low()

        # エコーパルスの期間を測定
        while echo.value() == 0:
            signaloff = utime.ticks_us()
        while echo.value() == 1:
            signalon = utime.ticks_us()

        timepassed = utime.ticks_diff(signalon, signaloff)
        distance = (timepassed * 0.0343) / 2  # cmに変換
        return distance

    # ブザーとLEDを制御する関数
    def alert(interval):
        buzzer.high()
        led.high()
        utime.sleep(0.1)
        buzzer.low()
        led.low()
        utime.sleep(interval)

    # メインループ
    try:
        while True:
            dist = measure_distance()
            print("Distance: {:.2f} cm".format(dist))
            if dist < 0:
                print("Out of range")
                utime.sleep(1)
            elif dist <= 10:
                alert(0.2)  # 非常に近い場合、速くアラート
            elif dist <= 20:
                alert(0.5)  # 近い場合、適度にアラート
            elif dist <= 50:
                alert(1)    # それほど近くない場合、ゆっくりアラート
            else:
                alert(2)    # 遠い場合、稀にアラート
    except KeyboardInterrupt:
        print("Measurement stopped by User")

コードが実行されると、物体を超音波センサーから異なる距離に置いたときの変化を観察できます。
ブザーの音の頻度とLEDの点滅速度の変化を確認してください。
コンソールには測定された距離が表示されます。

**コードの理解**

#. 距離の測定：

   * ``measure_distance()`` 関数はTRIGピンに10マイクロ秒のパルスを送信します。
   * その後、ECHOピンがHIGHに変わるまでの時間を測定し、再びLOWになるまでの時間を計測します。
   * 超音波パルスが帰ってくるまでの時間を基に距離を計算します。

   .. code-block:: python

        def measure_distance():
            # トリガーを低く設定
            trigger.low()
            utime.sleep_us(2)
            # トリガーに10usパルスを送信
            trigger.high()
            utime.sleep_us(10)
            trigger.low()

            # エコーパルスの期間を測定
            while echo.value() == 0:
                signaloff = utime.ticks_us()
            while echo.value() == 1:
                signalon = utime.ticks_us()

            timepassed = utime.ticks_diff(signalon, signaloff)
            distance = (timepassed * 0.0343) / 2  # cmに変換
            return distance


#. アラート機能：

   * ``alert(interval)`` 関数はブザーとLEDを0.1秒間オンにし、その後オフにします。
   * intervalパラメータは距離に基づいてアラート間の待機時間を調整します。

   .. code-block:: python

        def measure_distance():
            # Ensure trigger is low
            trigger.low()
            utime.sleep_us(2)
            # Send 10us pulse to trigger
            trigger.high()
            utime.sleep_us(10)
            trigger.low()

            # Measure the duration of the echo pulse
            while echo.value() == 0:
                signaloff = utime.ticks_us()
            while echo.value() == 1:
                signalon = utime.ticks_us()

            timepassed = utime.ticks_diff(signalon, signaloff)
            distance = (timepassed * 0.0343) / 2  # Convert to cm
            return distance

#. メインループ：

   * 距離を継続的に測定します。
   * 事前に設定された距離の閾値に基づいてアラートの頻度を調整します。

   .. code-block:: python

        try:
            while True:
                dist = measure_distance()
                print("Distance: {:.2f} cm".format(dist))
                if dist < 0:
                    print("Out of range")
                    utime.sleep(1)
                elif dist <= 10:
                    alert(0.2)  # 非常に近い場合、速くアラート
                elif dist <= 20:
                    alert(0.5)  # 近い場合、適度にアラート
                elif dist <= 50:
                    alert(1)    # それほど近くない場合、ゆっくりアラート
                else:
                    alert(2)    # 遠い場合、稀にアラート
        except KeyboardInterrupt:
            print("Measurement stopped by User")
        
**安全に関する考慮事項**

* 電圧レベル：

  * 超音波センサーのECHOピンの電圧（5V使用時）には注意してください。
  * PicoのGPIOピンを保護するために、電圧分割器やレベルシフターを使用してください。

* 電源供給：

  すべてのコンポーネントの電流要求を処理できる電源を使用してください。

**さらに実験してみよう**

* 視覚的な表示：

  LCDやOLEDディスプレイを追加して、距離を視覚的に表示しましょう。

* 複数のセンサー：

  追加の超音波センサーを使用して、より多くの方向をカバーしましょう。

* 高度なアラート：

  距離に応じて異なるトーンやパターンのブザーを実装してみましょう。

**結論**

Raspberry Pi Pico 2 Wを使用してリバースアシストシステムを作成しました！このプロジェクトは、センサーを使ってリアルタイムでフィードバックを提供する方法を示しており、ロボティクスや自動化の基本概念を学べます。
