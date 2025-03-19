.. note:: 

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！ Raspberry Pi、Arduino、ESP32について、他の愛好者と一緒に深く学びましょう。

    **なぜ参加するべきか？**

    - **専門家サポート**: 購入後の問題や技術的な課題をコミュニティやチームのサポートで解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換し、スキルを向上させましょう。
    - **限定プレビュー**: 新製品の発表や先行情報をいち早くチェックできます。
    - **特別割引**: 最新製品の限定割引をお楽しみいただけます。
    - **お得なプロモーションやプレゼント**: プレゼント企画やホリデープロモーションに参加しましょう。

    👉 一緒に探求し、創造を始めませんか？ [|link_sf_facebook|] をクリックして、今すぐ参加しましょう！

.. _py_ultrasonic:

6.1 距離測定
======================================

このレッスンでは、 **超音波センサーモジュール** を使ってRaspberry Pi Pico 2 Wで物体までの距離を測定する方法を学びます。超音波センサーは、ロボティクスや自動化システムで物体検出や距離測定によく使用されます。

* :ref:`cpn_ultrasonic`

**必要な部品**

このプロジェクトでは、以下の部品が必要です。

キットを購入するのが便利です。こちらから購入できます：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前	
        - このキットに含まれるアイテム
        - リンク
    *   - Pico 2 W スターターキット	
        - 450以上
        - |link_pico2w_kit|

また、以下のリンクから部品を個別に購入することもできます。


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
        - :ref:`cpn_ultrasonic`
        - 1
        - |link_ultrasonic_buy|

**超音波センサーの仕組み**

超音波センサーは、 **Trig** ピンから短い超音波パルスを発信し、 **Echo** ピンで反射音を受信することで動作します。エコーが戻ってくるまでの時間を測定し、音速を使って物体までの距離を計算します。

|ultrasonic_prin|

* **トリガーパルス**: Trigピンで10マイクロ秒の高いパルスを送信して、測定を開始します。
* **超音波バースト**: センサーは40kHzで8サイクルの超音波バーストを発信します。
* **エコー受信**: Echoピンが高くなり、エコーが返ってくるまで高い状態を維持します。
* **時間測定**: Echoピンが高い状態で保持されている時間を測定することで、距離を計算します。

**回路図**

|sch_ultrasonic|

**配線**

|wiring_ultrasonic|

**コードの記述**

超音波センサーを使用して距離を測定するMicroPythonプログラムを作成しましょう。

.. note::

    * ``6.1_measuring_distance.py`` を ``pico-2w-kit-main/micropython`` フォルダから開くか、コードをThonnyにコピーして「実行」ボタンをクリックするか、F5キーを押してください。
    * 正しいインタプリタ（MicroPython（Raspberry Pi Pico）.COMxx）が選択されていることを確認してください。


.. code-block:: python

    import machine
    import utime

    # センサーに接続されたピンを定義
    TRIG = machine.Pin(17, machine.Pin.OUT)
    ECHO = machine.Pin(16, machine.Pin.IN)

    def measure_distance():
        # トリガーピンが低いことを確認
        TRIG.low()
        utime.sleep_us(2)
        # 10µsのパルスを送信して測定を開始
        TRIG.high()
        utime.sleep_us(10)
        TRIG.low()
        
        # エコーピンが高くなるまで待機（エコーパルスの開始）
        while ECHO.value() == 0:
            pass
        start_time = utime.ticks_us()
        
        # エコーピンが低くなるまで待機（エコーパルスの終了）
        while ECHO.value() == 1:
            pass
        end_time = utime.ticks_us()
        
        # エコーパルスの時間を計算
        duration = utime.ticks_diff(end_time, start_time)
        
        # 距離を計算（音速は34300 cm/s）
        distance = (duration * 0.0343) / 2
        return distance

    while True:
        dist = measure_distance()
        print("Distance: {:.2f} cm".format(dist))
        utime.sleep(0.5)

コードを実行すると、Thonnyシェルにセンチメートル単位での距離測定結果が表示されます。物体をセンサーから近づけたり遠ざけたりすると、測定値が変化するのが確認できます。

**コードの理解**

#. 必要なモジュールをインポートし、トリガーとエコーピンを設定：

   .. code-block:: python
       
       import machine
       import utime
       
       TRIG = machine.Pin(17, machine.Pin.OUT)
       ECHO = machine.Pin(16, machine.Pin.IN)


#. 距離測定:

   * 測定を開始するためにトリガーパルスを送信。
   * エコー応答を待機。
   * エコーパルスの時間を計算。
   * 音速を使って距離を計算。

   .. code-block:: python

       def measure_distance():
           # トリガーが低いことを確認
           TRIG.low()
           utime.sleep_us(2)
           # 10µsパルスを送信
           TRIG.high()
           utime.sleep_us(10)
           TRIG.low()
           
           # エコー開始を待機
           while ECHO.value() == 0:
               pass
           start_time = utime.ticks_us()
           
           # エコー終了を待機
           while ECHO.value() == 1:
               pass
           end_time = utime.ticks_us()
           
           # 時間を計算
           duration = utime.ticks_diff(end_time, start_time)
           # 距離を計算
           distance = (duration * 0.0343) / 2
           return distance


#. メインループ:

   * 距離を継続的に測定し、結果を表示。
   * 測定の間に0.5秒の間隔をおく。

   .. code-block:: python
       
       while True:
           dist = measure_distance()
           print("Distance: {:.2f} cm".format(dist))
           utime.sleep(0.5)

**制限事項の理解**

* ブロッキングコード:

  * エコーを待機するwhileループは、他のコードが実行されるのをブロックします。
  * より高度なアプリケーションでは、割り込みや非同期プログラミングを使用してブロッキングを避けることを検討してください。

* 測定範囲:

  * HC-SR04センサーは通常、2cmから400cmの範囲を測定できます。
  * 2cm未満または400cmを超える物体は正確に検出できない場合があります。

* 環境要因:

  * 温度や湿度は音速に影響を与えます。
  * 正確な測定を行うためには、環境条件に基づいて音速を調整する必要があります。

**結論**

超音波センサーを使用して、Raspberry Pi Pico 2 Wで距離を測定する方法を成功裏に習得しました。この基本的なスキルは、ロボティクス、自動化、インタラクティブなプロジェクトに広く応用できます。
