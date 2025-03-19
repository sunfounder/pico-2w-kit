.. note::

    こんにちは！FacebookのSunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！仲間たちと一緒にRaspberry Pi、Arduino、ESP32についてさらに深く学びましょう。

    **参加する理由は？**

    - **専門的なサポート**: 当コミュニティとチームの助けを借りて、販売後の問題や技術的な課題を解決できます。
    - **学び・共有**: スキルを向上させるためのヒントやチュートリアルを交換しましょう。
    - **特別なプレビュー**: 新製品の発表やプレビューに早期アクセスできます。
    - **特別割引**: 最新製品の独占的な割引を楽しめます。
    - **フェスティブなプロモーションとプレゼント企画**: プレゼント企画やホリデープロモーションに参加できます。

    👉 私たちと一緒に探索し、創造を始める準備はできましたか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _py_somato_controller:

7.11 身体感覚コントローラーの作成
============================================

このエキサイティングなプロジェクトでは、Raspberry Pi Pico 2 W、MPU6050加速度計とジャイロスコープモジュール、サーボモーターを使用して **身体感覚コントローラー** を作成します。このデバイスは、人間の動き、特に手の傾きをキャプチャし、それをサーボモーターの動きに変換します。この技術は、手術ロボットやロボットアームなど、ロボット工学や遠隔操作システムで使用されている技術に似ています。

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
        - :ref:`cpn_mpu6050`
        - 1
        - 
    *   - 6
        - :ref:`cpn_servo`
        - 1
        - |link_servo_buy|

**部品の理解**

* **MPU6050加速度計とジャイロスコープ**: X、Y、Z軸に沿った加速度と角速度を測定する6軸運動追跡デバイスです。手の傾きを検出するために使用します。
* **サーボモーター**: 特定の角度に移動できるモーターです。MPU6050で検出した動きを模倣するために使用します。

**回路図**

|sch_somato|

MPU6050は、各方向の加速度値に基づいて姿勢角度を計算します。

プログラムは、姿勢角度が変化するにつれて対応する偏角をサーボに制御させます。

**配線**

|wiring_somatosensory_controller|

**コードの作成**

以下の機能を持つMicroPythonスクリプトを作成します：

* MPU6050から加速度計データを読み取る
* 手の傾き角度を計算する
* サーボモーターを制御して傾きを模倣する

.. note::
 
    * ``7.11_somatosensory_controller.py`` を ``pico-2w-kit-main/micropython`` から開くか、このコードをThonnyにコピーして「Run」をクリックするか、F5キーを押して実行します。
    * 正しいインタープリターが選択されていることを確認してください：MicroPython（Raspberry Pi Pico）。COMxx。
    * ここで使用する ``imu.py`` と ``vector3d.py`` をPicoにアップロードしていることを確認してください。詳細なチュートリアルについては :ref:`add_libraries_py` を参照してください。

.. code-block:: python

    from imu import MPU6050
    from machine import I2C, Pin, PWM
    import utime
    import math

    # MPU6050のI2C通信を初期化
    i2c = I2C(1, scl=Pin(7), sda=Pin(6))
    mpu = MPU6050(i2c)

    # GP15でサーボモーターのPWMを初期化
    servo = PWM(Pin(15))
    servo.freq(50)  # サーボ用に周波数を50Hzに設定

    # 角度をPWMデューティサイクルに変換する関数
    def angle_to_duty(angle):
        # 角度（0-180）をデューティサイクル（0.5ms - 2.5msパルス幅）に変換
        # デューティサイクルの範囲は50Hzで0.5msから2.5msのパルス幅に対応
        duty_cycle = (angle / 18) + 2
        duty_u16 = int(duty_cycle / 100 * 65535)
        return duty_u16

    # 加速度計データから傾き角度を取得する関数
    def get_tilt_angle():
        accel = mpu.accel
        x = accel.x
        y = accel.y
        z = accel.z
        angle = math.atan2(y, z) * (180 / math.pi)
        return angle + 90  # 角度を0から180の範囲に調整

    # メインループ
    try:
        while True:
            angle = get_tilt_angle()
            if angle < 0:
                angle = 0
            elif angle > 180:
                angle = 180
            duty = angle_to_duty(angle)
            servo.duty_u16(duty)
            utime.sleep(0.1)
    except KeyboardInterrupt:
        servo.deinit()
        print("Program stopped.")

プログラムを開始した後、手を上下に傾けてください。
サーボモーターは、手の傾きに応じて同じように動くはずです。
サーボが手の動きにどう反応するかを観察してみてください。

**コードの理解**

#. 初期化：

   * **I2C通信**: MPU6050からデータを読み取るために設定します。
   * **サーボモーターPWM**: GP15で50Hzの周波数でサーボを初期化します。

#. 角度計算：

   * ``get_tilt_angle()``: 加速度計の読み取り値に基づいて傾き角度を計算します。角度は0から180度の範囲に調整されます。

   .. code-block:: python

        def get_tilt_angle():
            accel = mpu.accel
            x = accel.x
            y = accel.y
            z = accel.z
            angle = math.atan2(y, z) * (180 / math.pi)
            return angle + 90  # 角度を0から180の範囲に調整

#. サーボ制御：

   * ``angle_to_duty(angle)``: 角度をサーボモーターの適切なPWMデューティサイクルに変換します。
   * デューティサイクル計算: サーボは50Hzで0.5ms（0度）から2.5ms（180度）の間のパルスを期待します。

   .. code-block:: python

        def angle_to_duty(angle):
            # 角度（0-180）をデューティサイクル（0.5ms - 2.5msパルス幅）に変換
            # デューティサイクルの範囲は50Hzで0.5msから2.5msのパルス幅に対応
            duty_cycle = (angle / 18) + 2
            duty_u16 = int(duty_cycle / 100 * 65535)
            return duty_u16

#. メインループ：

   * 傾き角度を読み取ります。
   * 角度が0から180度の範囲内に収まるように調整します。
   * サーボの位置をそれに応じて設定します。
   * ジッターを防ぐために短い遅延を加えます。
   * キーボード割り込みをキャプチャし、サーボを安全に終了します。

   .. code-block:: python

        try:
            while True:
                angle = get_tilt_angle()
                if angle < 0:
                    angle = 0
                elif angle > 180:
                    angle = 180
                duty = angle_to_duty(angle)
                servo.duty_u16(duty)
                utime.sleep(0.1)
        except KeyboardInterrupt:
            servo.deinit()
            print("Program stopped.")

**トラブルシューティング**

* サーボが動かない：

  * サーボに適切に電源が供給されているか確認します。
  * 信号線がGP15に接続されているか確認します。
  * Picoとサーボ間のグラウンドが接続されているか確認します。

* 動きが不正確：

  * MPU6050がしっかりと固定されており、過度に揺れていないことを確認します。
  * 角度計算を調整します。

* プログラムエラー：

  * imu.pyとvector3d.pyが正しくアップロードされているか確認します。
  * コードにタイプミスやインデントエラーがないか確認します。

**拡張と改善**

* 複数のサーボを制御：

  * 他の軸の動きを制御するためにサーボを追加します。
  * 他の軸周りの回転を処理するようにコードを拡張します。

* ワイヤレス通信：

  BluetoothやWi-Fiモジュールを使用してセンサーのデータを別のデバイスに送信し、サーボを制御します。

* データ平滑化：

  センサーの読み取り値を平滑化するフィルタ（例：カルマンフィルタ）を実装します。

* 視覚的フィードバック：

  リアルタイムの角度データを表示するOLEDまたはLCDディスプレイを追加します。

**結論**

人間の動きをキャプチャして機械的な動きに変換する身体感覚コントローラーを無事に作成しました。このプロジェクトは、センサーとアクチュエータが連携して、ロボット工学や遠隔操作システムで使用されるインタラクティブなシステムを作る方法を示しています。

このプロジェクトをさらに改善して、より多くの機能を追加したり、大規模なシステムに統合したりすることができます。
