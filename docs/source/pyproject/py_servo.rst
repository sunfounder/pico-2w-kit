.. note::

    こんにちは！FacebookのSunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！仲間たちと一緒にRaspberry Pi、Arduino、ESP32についてさらに深く学びましょう。

    **参加する理由は？**

    - **専門的なサポート**: 当コミュニティとチームの助けを借りて、販売後の問題や技術的な課題を解決できます。
    - **学び・共有**: スキルを向上させるためのヒントやチュートリアルを交換しましょう。
    - **特別なプレビュー**: 新製品の発表やプレビューに早期アクセスできます。
    - **特別割引**: 最新製品の独占的な割引を楽しめます。
    - **フェスティブなプロモーションとプレゼント企画**: プレゼント企画やホリデープロモーションに参加できます。

    👉 私たちと一緒に探索し、創造を始める準備はできましたか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _py_servo:

3.7 サーボモーターの振動
========================

このレッスンでは、Raspberry Pi Pico 2 Wを使用して **サーボモーター** を制御する方法を学びます。サーボモーターは0°から180°の特定の角度に回転できるデバイスで、リモートコントロールのおもちゃやロボット、正確な位置制御が必要な他のアプリケーションで広く使用されています。

さあ、サーボを前後に振らせてみましょう！

* :ref:`cpn_servo`

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
        - :ref:`cpn_servo`
        - 1
        - |link_servo_buy|


**回路図**

|sch_servo|

**配線**

|wiring_servo|

* オレンジ色の線は信号線で、GP15に接続されています。
* 赤色の線はVCCで、VBUS(5V)に接続されています。
* 茶色の線はGNDで、GNDに接続されています。

サーボは特に負荷がかかると大きな電流を消費します。ここでは小型のサーボを使用しており、重い負荷をかけないため、PicoのVBUSピンから電源を供給するのはこの簡単な実験では許容されます。より大きなサーボや複数のサーボを使用する場合は、外部電源を使用してください。

**サーボアームの設定**

* サーボの出力軸にサーボアーム（ホーンとも呼ばれます）を取り付けます。
* 必要に応じてサーボに付属の小さなネジで固定します。

.. 1. Press the Servo Arm into the Servo output shaft. If necessary, fix it with screws.
.. #. Connect **VBUS** (not 3V3) and GND of Pico 2 W to the power bus of the breadboard.
.. #. Connect the red lead of the servo to the positive power bus with a jumper.
.. #. Connect the yellow lead of the servo to the GP15 pin with a jumper wire.
.. #. Connect the brawn lead of the servo to the negative power bus with a jumper wire.

**コードの作成**

0°から180°の間でサーボを前後に振るMicroPythonプログラムを書きます。

.. note::

    * ``3.7_swinging_servo.py`` を ``pico-2w-kit-main/micropython`` から開くか、このコードをThonnyにコピーして「Run」をクリックするか、F5キーを押して実行します。
    * 正しいインタープリターが選択されていることを確認してください：MicroPython（Raspberry Pi Pico）。COMxx。
    

.. code-block:: python

    import machine
    import utime

    # GP15ピンでPWMを初期化
    servo = machine.PWM(machine.Pin(15))
    servo.freq(50)  # 周波数を50Hzに設定

    # 角度をデューティーサイクルに変換する関数
    def angle_to_duty(angle):
        min_duty = 1638  # 0.5msのパルス（0°）
        max_duty = 8192  # 2.5msのパルス（180°）
        duty = int(min_duty + (angle / 180) * (max_duty - min_duty))
        return duty

    while True:
        # 0°から180°までサーボを動かす
        for angle in range(0, 181, 1):
            servo.duty_u16(angle_to_duty(angle))
            utime.sleep_ms(20)
        # 180°から0°までサーボを戻す
        for angle in range(180, -1, -1):
            servo.duty_u16(angle_to_duty(angle))
            utime.sleep_ms(20)

コードが実行されると、サーボはスムーズに0°から180°まで前後に振れるはずです。


**コードの理解**

#. モジュールのインポート：

   * ``machine``: ハードウェア関連の機能にアクセスするため。
   * ``utime``: 遅延のための時間関連の関数を含んでいます。

#. PWMの初期化：

   GP15でPWMを設定します。
   サーボの標準である周波数50Hzに設定します。

   .. code-block:: python

      servo = machine.PWM(machine.Pin(15))
      servo.freq(50)

#. ``angle_to_duty`` 関数の定義：

   * この関数は角度（0°から180°）をサーボの対応するデューティーサイクル値にマッピングします。
   * ``min_duty`` と ``max_duty`` はサーボ制御信号の最小および最大パルス幅に対応します。
   * 角度を適切なデューティーサイクルにスケールする計算を行います。

   .. code-block:: python

      def angle_to_duty(angle):
          min_duty = 1638  # 0.5msのパルス幅
          max_duty = 8192  # 2.5msのパルス幅
          duty = int(min_duty + (angle / 180) * (max_duty - min_duty))
          return duty

#. メインループでサーボを動かす:

   * サーボは0°から180°まで、毎回1°ずつ角度を増加させながら動きます。
   * 次に、180°から0°まで戻ります。
   * ``utime.sleep_ms(20)`` は動きをスムーズにするための小さな遅延を加えます。

   .. code-block:: python

      while True:
          for angle in range(0, 181, 1):
              servo.duty_u16(angle_to_duty(angle))
              utime.sleep_ms(20)
          for angle in range(180, -1, -1):
              servo.duty_u16(angle_to_duty(angle))
              utime.sleep_ms(20)

**コードの詳細**

サーボは、特定のパルス幅を持つPWM信号を送ることで制御されます。
サーボ用の標準的な50HzのPWM信号（20msの周期）が使用されます。
各周期内でのパルス幅がサーボの角度を決定します：

* 0.5msのパルス幅は0°に対応します。
* 1.5msのパルス幅は90°に対応します。
* 2.5msのパルス幅は180°に対応します。

PWM信号のデューティーサイクルを調整することによって、パルス幅を変更します。

``duty_u16()`` 関数は、0から65535の範囲の値を受け取ります。
パルス幅に対応するデューティーサイクルを計算する方法は以下の通りです：

.. code-block::

  Duty cycle = (Pulse Width / Period) * 65535

例えば、0.5msのパルス幅の場合：

.. code-block::

  Duty cycle = (0.5ms / 20ms) * 65535 ≈ 1638

**さらに実験する**

* **速度を変更**: ``utime.sleep_ms(20)`` の遅延を調整して、サーボの動作を速くしたり遅くしたりできます。
* **特定の角度に設定**: コードを変更して、サーボを特定の角度に動かします。

  .. code-block:: python

    servo.duty_u16(angle_to_duty(90))  # 90°に移動

* **入力で制御**: ポテンショメーターやボタンを接続して、サーボの角度をインタラクティブに制御します。

**重要な注意点**

* **電源供給**: サーボに十分な電源が供給されていることを確認してください。もしジッターや不安定な動きが見られる場合は、サーボ用に外部の5V電源を使用することを検討してください。
* **過負荷の回避**: サーボを物理的な制限（通常は0°から180°）以上に無理に動かさないようにしてください。損傷を防ぐためです。

**結論**

このレッスンでは、Raspberry Pi Pico 2 Wを使用してサーボモーターを制御する方法を学びました。サーボの角度を設定するためにPWM信号を生成し、スムーズに動かす方法を理解しました。このスキルは、ロボット工学や自動化プロジェクトで精密な動きが必要な場合に非常に重要です。
