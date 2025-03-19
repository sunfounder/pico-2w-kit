.. note:: 
    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！Facebookで仲間と一緒に、Raspberry Pi、Arduino、ESP32について深く学んでいきましょう。

    **なぜ参加するべきか？**

    - **専門家のサポート**: コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び・シェア**: ヒントやチュートリアルを交換して、スキルを向上させましょう。
    - **限定プレビュー**: 新製品の発表や先取り情報をいち早くゲットできます。
    - **特別割引**: 最新製品を特別価格でお得に購入できます。
    - **お祭りプロモーションとプレゼント**: プレゼントやホリデープロモーションに参加できます。

    👉 一緒に探求して、創造していきませんか？[|link_sf_facebook|]をクリックして、今すぐ参加しよう！

.. _py_bubble_level:

7.12 デジタル水準器の作成
==========================================

このプロジェクトでは、Raspberry Pi Pico 2 W、MPU6050加速度センサーおよびジャイロスコープモジュール、そして2つの74HC595シフトレジスタで制御される8x8のLEDマトリックスディスプレイを使用して **デジタル水準器** を作成します。このデバイスは、従来の水準器と似た機能を持ち、表面の傾きを示します。MPU6050を傾けると、マトリックス上のLEDで表現された「気泡」がそれに従って移動し、表面の水平状態を視覚的に確認することができます。

**必要な部品**

このプロジェクトに必要な部品は以下の通りです。

一式購入するのが便利です。リンクはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名称
        - このキットに含まれる部品
        - リンク
    *   - Pico 2 Wスターターキット
        - 450+
        - |link_pico2w_kit|

以下のリンクから個別に購入することもできます。


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
        - :ref:`cpn_dot_matrix`
        - 1
        - 
    *   - 6
        - :ref:`cpn_74hc595`
        - 2
        - |link_74hc595_buy|
    *   - 7
        - :ref:`cpn_mpu6050`
        - 1
        - 

**部品の理解**

* **MPU6050加速度センサーおよびジャイロスコープ**: 3軸（X、Y、Z）で加速度と角速度のデータを提供し、これを使って傾き角度を計算します。
* **8x8 LEDマトリックスディスプレイ**: 8行8列に並んだLEDの配列で、個々のLEDを制御することでパターンや画像を表示します。
* **74HC595シフトレジスタ**: PicoのGPIOピンを少なくしながら、複数の出力（この場合、LEDマトリックスの行と列）を制御することができます。

**回路図**

|sch_bubble_level|

MPU6050は各方向の加速度値を取り、姿勢角度を計算します。

その結果、プログラムは2つの74HC595チップからのデータに基づいて、マトリックス上に2x2の点を描画します。

姿勢角度が変化することで、プログラムは異なるデータを74HC595チップに送信し、点の位置が変わり、気泡効果を生み出します。

**配線**


|wiring_digital_bubble_level| 

**コードの記述**

以下のことを行うMicroPythonスクリプトを作成します：

* MPU6050から加速度データを読み取ります。
* X軸およびY軸に沿った傾斜角度を計算します。
* 傾斜角度を8x8のLEDマトリックス上の位置にマッピングします。
* 傾きに応じて移動する「気泡」（2x2ピクセルの表現）を表示します。

.. note::

    * ``7.12_digital_bubble_level.py`` を ``pico-2w-kit-main/micropython`` から開くか、コードをThonnyにコピーして、「実行」ボタンをクリックするか、F5を押してください。
    * 正しいインタプリタが選択されていることを確認してください：MicroPython (Raspberry Pi Pico).COMxx。
    * ``imu.py`` および ``vector3d.py`` を使用する必要があります。これがPicoにアップロードされているか確認し、詳細なチュートリアルについては :ref:`add_libraries_py` を参照してください。

.. code-block:: python

    import machine
    from machine import I2C, Pin
    import time
    import math
    from imu import MPU6050
    
    # MPU6050センサーとのI2C通信の初期化
    i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)
    mpu = MPU6050(i2c)
    
    # 2点間の距離を計算する関数
    def dist(a, b):
        return math.sqrt((a * a) + (b * b))
    
    # y軸に沿った回転角度を計算する関数
    def get_y_rotation(x, y, z):
        radians = math.atan2(x, dist(y, z))
        return -math.degrees(radians)
    
    # x軸に沿った回転角度を計算する関数
    def get_x_rotation(x, y, z):
        radians = math.atan2(y, dist(x, z))
        return math.degrees(radians)
    
    # MPU6050センサーから現在の角度を取得する関数
    def get_angle():
        y_angle = get_y_rotation(mpu.accel.x, mpu.accel.y, mpu.accel.z)
        x_angle = get_x_rotation(mpu.accel.x, mpu.accel.y, mpu.accel.z)
        return x_angle, y_angle
    
    # LEDマトリックスを制御するためのシフトレジスタのピンの初期化
    sdi = machine.Pin(18, machine.Pin.OUT)
    rclk = machine.Pin(19, machine.Pin.OUT)
    srclk = machine.Pin(20, machine.Pin.OUT)
    
    # シフトレジスタにデータをシフトインする関数
    def hc595_in(dat):
        for bit in range(7, -1, -1):
            srclk.low()
            time.sleep_us(30)
            sdi.value(1 & (dat >> bit))
            time.sleep_us(30)
            srclk.high()
    
    # シフトレジスタからLEDマトリックスにデータを出力する関数
    def hc595_out():
        rclk.high()
        time.sleep_us(200)
        rclk.low()
    
    # LEDマトリックスにグリフ（8x8マトリックス）を表示する関数
    def display(glyph):
        for i in range(0, 8):
            hc595_in(glyph[i])
            hc595_in(0x80 >> i)
            hc595_out()
    
    # 2DマトリックスをLEDマトリックスに表示できるグリフに変換する関数
    def matrix_2_glyph(matrix):
        glyph = [0 for i in range(8)]
        for i in range(8):
            for j in range(8):
                glyph[i] += matrix[i][j] << j
        return glyph
    
    # 値を指定された最小値と最大値の間に制限する関数
    def clamp_number(val, min_val, max_val):
        return min_val if val < min_val else max_val if val > max_val else val
    
    # 値を別の範囲にマッピングする関数
    def interval_mapping(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    
    # MPU6050の読み取りデータに基づいて気泡の位置を計算する関数
    sensitivity = 4  # 気泡の動きの感度
    matrix_range = 7  # マトリックスのサイズは8x8なので、範囲は0-7
    point_range = matrix_range - 1  # 気泡の位置は0から6の間でなければならない
    
    # センサーのデータに基づいて気泡の位置を計算する関数
    def bubble_position():
        y, x = get_angle()  # 現在の回転角度を取得
        x = int(clamp_number(interval_mapping(x, 90, -90, 0 - sensitivity, point_range + sensitivity), 0, point_range))
        y = int(clamp_number(interval_mapping(y, -90, 90, point_range + sensitivity, 0 - sensitivity), 0, point_range))
        return [x, y]
    
    # マトリックスに気泡（2x2のLEDを消すことで表現）を落とす関数
    def drop_bubble(matrix, bubble):
        matrix[bubble[0]][bubble[1]] = 0
        matrix[bubble[0] + 1][bubble[1]] = 0
        matrix[bubble[0]][bubble[1] + 1] = 0
        matrix[bubble[0] + 1][bubble[1] + 1] = 0
        return matrix
    
    # メインループ
    while True:
        matrix = [[1 for i in range(8)] for j in range(8)]  # すべてのLEDが点灯しているマトリックスを作成
        bubble = bubble_position()  # センサーのデータに基づいて気泡の位置を取得
        matrix = drop_bubble(matrix, bubble)  # 気泡をマトリックスに落とす
        display(matrix_2_glyph(matrix))  # LEDグリッドにマトリックスを表示
        time.sleep(0.1)  # 更新速度を制御するために少し遅延を追加

コードが実行されると、セットアップを水平な面に置いてください。
気泡（2x2のピクセル）がLEDマトリックスの中央に表示されます。
ブレッドボードまたはMPU6050モジュールを傾けてください。
気泡がLEDマトリックス上で傾きに従って移動し、実際の水準器のようにシミュレートされるのを観察できます。

**コードの理解**

このコードは、MPU6050加速度センサーとジャイロスコープからデータを読み取り、デバイスの傾きを計算して、8x8 LEDマトリックス上に「気泡」を表示します。これにより、デジタル水準器をシミュレートします。

#. インポートと初期化：

   * ``machine``: マイコンのハードウェアコンポーネントへのアクセス
   * ``I2C``, ``Pin``: I2C通信とGPIOピンの操作
   * ``time``: 遅延のためのタイミング関数
   * ``math``: 計算のための数学関数
   * ``MPU6050`` from ``imu``: MPU6050センサーとインターフェースするためのライブラリ

#. I2C初期化：

   * バス1でI2C通信を設定し、SDAをピン6、SCLをピン7に接続します。
   * 高速なデータ転送のため、周波数は400kHzに設定します。
   * ``mpu`` オブジェクトを作成し、MPU6050センサーとやり取りします。

#. 数学的な関数：

   * ``dist(a, b)`` 関数：

     * 2つの値の間のユークリッド距離を計算します。
     * 角度計算での大きさのコンポーネントを計算するために使用されます。

   * ``get_y_rotation(x, y, z)``:

     * Y軸回りの回転を度単位で計算します。
     * ``math.atan2`` を使用して、xとy、zの距離に基づく逆正接を計算します。
     * 結果は、目的の向きに合わせるために符号を反転させます。

   * ``get_x_rotation(x, y, z)``:

     * X軸周りの回転角度を計算します。
     * ``get_y_rotation`` と同様ですが、yとx、zの距離のアークタンジェントを計算します。

   * ``get_angle()``:

     * 現在のMPU6050センサーからの加速度データを取得します。
     * 加速度計データを使用して、X軸とY軸の回転角度を計算します。

#. シフトレジスタ関数：

   * ピン定義：

     * ``sdi``: シフトレジスタのシリアルデータ入力ピン（ピン18）
     * ``rclk``: シフトレジスタのレジスタクロック（ラッチ）ピン（ピン19）
     * ``srclk``: シフトレジスタのシフトクロックピン（ピン20）

   * ``hc595_in(dat)`` 関数：

     * 8ビットのデータバイトをシフトレジスタにシフトインします。
     * MSBからLSBまで各ビットを反復処理します。
     * ``srclk`` と ``sdi`` を制御して、データビットをクロックします。

   * ``hc595_out()``:

     * シフトレジスタから出力ピンにデータをラッチします。
     * ``rclk`` ピンを切り替えて、シフトレジスタからストレージレジスタにデータを転送します。

#. LEDマトリックスディスプレイ関数：

   * ``display(glyph)`` 関数：

     * 8x8のグリフをLEDマトリックスに表示します。
     * グリフの各行を反復処理します。
     * 行データと対応する列セレクターをシフトインします。
     * ``hc595_out()`` を呼び出してディスプレイを更新します。

   * ``matrix_2_glyph(matrix)`` 関数：

     * 0と1の8x8の2Dマトリックスを8バイトのグリフに変換します。
     * グリフの各バイトは、LEDマトリックスの行を表します。
     * 各バイトのビットは、その行のLEDに対応します。

#. ユーティリティ関数：

   * ``clamp_number(val, min_val, max_val)`` 関数：

     * ``val`` が指定された ``min_val`` と ``max_val`` の範囲内に収まるようにします。
     * 気泡がLEDマトリックスの境界外に移動しないようにします。

   * ``interval_mapping(x, in_min, in_max, out_min, out_max)`` 関数：

     * ``x`` の値を1つの範囲から別の範囲にマッピングします。
     * 角度測定をマトリックスの位置に変換するために使用されます。

#. 気泡の位置計算：

   * 感度設定：

     * ``sensitivity = 4``: 傾きの変化に対する気泡の反応性を決定します。
     * ``matrix_range = 7``: 8x8マトリックスの最大インデックス（0から7）。
     * ``point_range = matrix_range - 1``: 気泡の位置は0から6の範囲内に収める必要があります。

   * ``bubble_position()`` 関数：

     * 現在のX軸およびY軸の回転角度を取得します。
     * 角度をLEDマトリックスの位置にマッピングします。
     * マトリックス内に収まるように位置を制限します。

#. 気泡表示関数：

   * ``drop_bubble(matrix, bubble)`` 関数：

     * 与えられた位置で気泡を表示するために、LEDマトリックスを変更します。
     * 気泡の座標を中心に2x2のLEDブロックを消します。
     * 気泡の移動を視覚的に表現するためにマトリックスを更新します。

#. メインループ

   * センサー入力に基づいてディスプレイを更新するために継続的に実行します。
   * すべてのLEDが点灯している新しい8x8マトリックスを初期化します。
   * ``bubble_position()`` から現在の気泡位置を取得します。
   * ``drop_bubble()`` で気泡の新しい位置を反映させます。
   * ``matrix_2_glyph()`` を使用してマトリックスをグリフに変換します。
   * ``display()`` でLEDマトリックスにグリフを表示します。
   * 0.1秒の遅延を追加して、更新レートを制御します。

**トラブルシューティング**

* LEDマトリックスが正しく表示されない：

  * シフトレジスタとLEDマトリックスの間のすべての配線接続を確認します。
  * シフトレジスタがPicoに正しく接続されていることを確認します。
  * LEDマトリックスの共通アノードまたはカソード構成がコードの論理と一致しているか確認します。

* 気泡の動きが不正確：

  * MPU6050が正しく接続され、動作していることを確認します。
  * MPU6050が正しく配置されていることを確認します。

* プログラムエラー：

  * ``imu.py`` と ``vector3d.py`` が正しくアップロードされているか確認します。
  * コードにタイプミスやインデントエラーがないか確認します。

**さらなる実験**

* 感度の調整：

  角度を位置にマッピングする設定を変更して、気泡の動きの感度を変更します。

* ディスプレイの拡張：

  * 気泡のサイズや形を変更します。
  * トレイルや異なるパターンなどの視覚効果を追加します。

* 校正：

  デバイスが不均一な表面に置かれたときにゼロポイントを設定する校正手順を実装します。

* 代替表示：

  OLEDやLCDディスプレイを使用して、数値の角度を表示する機能を追加します。

**結論**

Raspberry Pi Pico 2 Wを使用してデジタル水準器を作成しました！このプロジェクトは、加速度センサーデータを使用して姿勢や傾きを視覚化し、シフトレジスタを使ってLEDマトリックスディスプレイを制御する方法を示しています。

このプロジェクトを拡張して、新しい機能を追加したり、大規模なシステムに統合したりできます。
