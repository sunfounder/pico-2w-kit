.. note:: 

    こんにちは！FacebookのSunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Raspberry Pi、Arduino、ESP32をさらに深く学び、仲間たちと一緒に楽しんでいきましょう。

    **参加する理由は？**

    - **専門的なサポート**: 購入後の問題や技術的な課題を、コミュニティとチームのサポートで解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **特別な先行公開**: 新製品の発表や先取り情報をいち早くゲットできます。
    - **特別割引**: 最新製品をお得に購入できる割引があります。
    - **季節ごとのプロモーションとプレゼント**: プレゼント企画やホリデープロモーションに参加しましょう。

    👉 さあ、私たちと一緒に探索し、創造を始めましょう！[|link_sf_facebook|] をクリックして、今すぐ参加してください！

.. _py_motor:

3.5 小型ファン（DCモーター）の制御
=========================================

このレッスンでは、Raspberry Pi Pico 2 Wと **TA6586モータードライバ** を使って、 **DCモーター** （小型ファンなど）の制御方法を学びます。
TA6586を使用すると、モーターの回転方向（時計回りおよび反時計回り）を制御できます。
DCモーターは比較的大きな電流を必要とするため、安全のためにモーターに電力を供給するための電源モジュールを使用します。

* :ref:`cpn_motor`
* :ref:`cpn_ta6586`
* :ref:`cpn_power_module`

**必要な部品**

このプロジェクトで必要な部品は以下の通りです。

全ての部品がセットになったキットを購入するのが便利です。こちらのリンクをご参照ください：

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
        - :ref:`cpn_ta6586`
        - 1
        - 
    *   - 6
        - :ref:`cpn_motor`
        - 1
        - |link_motor_buy| 
    *   - 7
        - :ref:`cpn_lipo_charger`
        - 1
        -  
    *   - 8
        - Power Pack
        - 1
        -   



**回路図**

|sch_motor|



**配線**

.. note::

    * DCモーターは高い電流を必要とするため、安全のためにここではモーターに電力を供給するためにLi-po充電モジュールを使用します。
    * Li-po充電モジュールが回路図通りに接続されていることを確認してください。正しく接続されていない場合、ショートサーキットが発生し、バッテリーや回路が損傷する可能性があります。

|wiring_motor|


**コード**

.. note::

    * ``pico-2w-kit-main/micropython`` から ``3.5_small_fan.py`` を開くか、コードをThonnyにコピーして、「実行」をクリックするか、F5を押します。

    * 正しいインタープリターが選択されていることを確認してください：MicroPython（Raspberry Pi Pico）.COMxx。 

.. code-block:: python

    import machine
    import utime

    motor1A = machine.Pin(14, machine.Pin.OUT)
    motor2A = machine.Pin(15, machine.Pin.OUT)

    def clockwise():
        motor1A.high()
        motor2A.low()

    def anticlockwise():
        motor1A.low()
        motor2A.high()

    def stopMotor():
        motor1A.low()
        motor2A.low()

    while True:
        clockwise()
        utime.sleep(1)
        stopMotor()
        utime.sleep(1)
        anticlockwise()
        utime.sleep(1)
        stopMotor()
        utime.sleep(1)


プログラムが実行されると、モーターは規則的なパターンで前後に回転します。


**コードの理解**

#. ピンの初期化：

   ``motor1A`` と ``motor2A`` は、GP14とGP15に接続されており、モーターの回転方向を制御します。

   .. code-block:: python

     motor1A = machine.Pin(14, machine.Pin.OUT)
     motor2A = machine.Pin(15, machine.Pin.OUT)

#. 関数の定義：

   * ``clockwise()``: ``motor1A`` を高、 ``motor2A`` を低に設定し、モーターを時計回りに回転させます。
   * ``anticlockwise()``: ``motor1A`` を低、 ``motor2A`` を高に設定し、反時計回りに回転させます。
   * ``stopMotor()``: ``motor1A`` と ``motor2A`` を両方とも低に設定し、モーターを停止させます。

#. メインループ：

   モーターは時計回りに回転し、停止し、反時計回りに回転し、再び停止します。それぞれ1秒間の動作を繰り返します。

   .. code-block:: python

    while True:
        clockwise()
        utime.sleep(1)
        stopMotor()
        utime.sleep(1)
        anticlockwise()
        utime.sleep(1)
        stopMotor()
        utime.sleep(1)

**トラブルシューティングのヒント**

* スクリプトを停止した後もモーターが回り続ける場合：

  プログラム停止後もモーターが回り続ける場合、Picoをリセットする必要があるかもしれません。RUNピンとGNDを一時的に接続するために、ワイヤーやボタンを使用してください。これによりPicoがリセットされます。

  |wiring_run_reset|

* Picoが切断される、または反応しなくなる場合：

  モーターが過剰な電流を消費していると、電圧の変動が発生することがあります。モーターに別の電源を使用し、すべてのグラウンドが接続されていることを確認してください。

**結論**

このレッスンでは、TA6586モータードライバとRaspberry Pi Pico 2 Wを使ってDCモーターを制御する方法を学びました。これで、モーターの回転方向を制御でき、小型ファンやモーター駆動のデバイスなどのプロジェクトを作成できるようになりました。

**次のステップ**

* **速度制御**: PWM（パルス幅変調）を使用してモーターの速度を制御してみましょう。EN1ピンをPWM対応のGPIOピンに接続します。
* **複数のモーターの制御**: TA6586の他のチャネルを使用して追加のモーターを制御します。
* **センサーの統合**: 入力（例：温度、光）に基づいてモーターを制御するためにセンサーを組み込みます。
