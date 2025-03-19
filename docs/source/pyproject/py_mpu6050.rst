.. note:: 

    こんにちは！FacebookのSunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Raspberry Pi、Arduino、ESP32を深く学び、仲間たちと一緒に探索していきましょう。

    **参加する理由は？**

    - **専門的なサポート**: 購入後の問題や技術的な課題を、コミュニティとチームのサポートで解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **特別な先行公開**: 新製品の発表や先取り情報をいち早くゲットできます。
    - **特別割引**: 最新製品をお得に購入できる割引を提供します。
    - **季節ごとのプロモーションとプレゼント**: プレゼント企画やホリデープロモーションに参加しましょう。

    👉 さあ、私たちと一緒に探索し、創造を始めましょう！[|link_sf_facebook|] をクリックして、今すぐ参加してください！

.. _py_mpu6050:

6.3 6軸モーショントラッキング
=====================================


このレッスンでは、Raspberry Pi Pico 2 Wと **MPU-6050** 6軸モーショントラッキングセンサーをインターフェースする方法を学びます。MPU-6050は、3軸ジャイロスコープと3軸加速度計を組み合わせており、I2C通信プロトコルを通じて生のセンサーデータを提供します。

* :ref:`cpn_mpu6050`


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
        - :ref:`cpn_mpu6050`
        - 1
        - 

**MPU-6050センサーの理解**

**MPU-6050** センサーは、ドローン、ロボット、ゲームデバイスなど、モーショントラッキングと向き検出を必要とするプロジェクトで広く使用されています。

* **加速度計**: X、Y、Z軸に沿った加速度を測定します。これには重力加速度も含まれ、センサーの傾きや向きを判断できます。
* **ジャイロスコープ**: X、Y、Z軸を中心に回転速度を測定し、センサーの回転速度を提供します。

**回路図**

|sch_mpu6050_ar|


**配線**

|wiring_mpu6050_ar|

**コードの作成**

MPU-6050センサーから加速度計とジャイロスコープのデータを読み取るMicroPythonスクリプトを作成しましょう。

.. note::

    * ``pico-2w-kit-main/micropython`` から ``6.3_6axis_motion_tracking.py`` を開くか、コードをThonnyにコピーして、「実行」をクリックするか、F5を押します。
    * 正しいインタープリターが選択されていることを確認してください：MicroPython（Raspberry Pi Pico）.COMxx。
     
    * ここでは ``imu.py`` と ``vector3d.py`` を使用する必要があります。これらがPicoにアップロードされているか確認し、詳細なチュートリアルについては :ref:`add_libraries_py` を参照してください。

.. code-block:: python

   from machine import I2C, Pin
   import utime
   from imu import MPU6050

   # I2Cインターフェースの初期化（I2C0） SDAをGP4、SCLをGP5に設定
   i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)

   # MPU-6050センサーの初期化
   mpu = MPU6050(i2c)

   def read_accelerometer():
      """Reads accelerometer data and returns it as a tuple (x, y, z)."""
      accel = mpu.accel
      return accel.x, accel.y, accel.z

   def read_gyroscope():
      """Reads gyroscope data and returns it as a tuple (x, y, z)."""
      gyro = mpu.gyro
      return gyro.x, gyro.y, gyro.z

   def main():
      """Main loop to read and print sensor data."""
      while True:
         # 加速度計データを読み取る
         ax, ay, az = read_accelerometer()
         print("Accelerometer (g) - X: {:.3f}, Y: {:.3f}, Z: {:.3f}".format(ax, ay, az))
         
         # 見やすくするために一時停止
         utime.sleep(0.5)
         
         # ジャイロスコープデータを読み取る
         gx, gy, gz = read_gyroscope()
         print("Gyroscope (°/s) - X: {:.3f}, Y: {:.3f}, Z: {:.3f}".format(gx, gy, gz))
         
         # 次のデータ読み取り前に一時停止
         utime.sleep(0.5)

   # メイン関数を実行
   if __name__ == "__main__":
      main()


このスクリプトは、加速度計とジャイロスコープの読み取り値を交互に0.5秒ごとに表示します。

* 加速度計の出力：

  .. code-block::

     Accelerometer (g) - X: 0.000, Y: 0.000, Z: 1.000

  静止状態では、X軸とY軸は0gに近く、Z軸は重力の影響でおおよそ1gになります。

* ジャイロスコープの出力：

  .. code-block::

     Gyroscope (°/s) - X: 0.000, Y: 0.000, Z: 0.000

  静止状態では、ジャイロスコープの読み取り値は全て0°/sに近くなります。
  センサーを回転させると、これらの値が変化し、角速度を反映します。

**コードの理解**

#. インポートとセットアップ：


   * ``machine.I2C`` と ``machine.Pin``: ハードウェアインターフェースのためのモジュール。
   * ``utime``: 時間関連の関数。
   * ``MPU6050``: imu.pyライブラリからのセンサークラス。

#. I2Cの初期化：

   I2Cバス0を、GP4（SDA）とGP5（SCL）に設定し、通信速度は400 kHzに設定します。

   .. code-block:: python

      i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)


#. センサーの初期化：

   I2Cインターフェースを使用してMPU-6050センサーのインスタンスを作成します。

   .. code-block:: python

      mpu = MPU6050(i2c)

#. 加速度計データの読み取り：

   加速度計データにアクセスし、X、Y、Zの値を取得します。

   .. code-block:: python

      def read_accelerometer():
         accel = mpu.accel
         return accel.x, accel.y, accel.z


#. ジャイロスコープデータの読み取り：

   ジャイロスコープデータにアクセスし、X、Y、Zの値を取得します。

   .. code-block:: python

      def read_gyroscope():
         gyro = mpu.gyro
         return gyro.x, gyro.y, gyro.z


#. メインループ：

   * 加速度計データを読み取り、表示します。
   * 0.5秒待機します。
   * ジャイロスコープデータを読み取り、表示します。
   * もう一度0.5秒待機してから繰り返します。

   .. code-block:: python

      def main():
         while True:
            # 加速度計データを読み取って表示
            ax, ay, az = read_accelerometer()
            print("Accelerometer (g) - X: {:.3f}, Y: {:.3f}, Z: {:.3f}".format(ax, ay, az))
            
            utime.sleep(0.5)
            
            # ジャイロスコープデータを読み取って表示
            gx, gy, gz = read_gyroscope()
            print("Gyroscope (°/s) - X: {:.3f}, Y: {:.3f}, Z: {:.3f}".format(gx, gy, gz))
            
            utime.sleep(0.5)


#. プログラムのエントリーポイント：

   スクリプトが直接実行されるときに、 ``main()`` を呼び出すことを保証します。

   .. code-block:: python

      if __name__ == "__main__":
         main()


**さらに実験する**

* **1つのセンサーに集中する**: 加速度計またはジャイロスコープデータのみに集中したい場合、他方のセンサーのprint文をコメントアウトできます。
* **データの可視化**: センサーデータをリアルタイムでプロットするツールやソフトウェアを使用して、視覚的に確認します。
* **向きの計算**: 加速度計データからピッチとロールを計算するアルゴリズムを実装します。
* **動作検出**: 特定の動作閾値を超えた時にアクションを実行するプログラムを作成します。

**センサーデータの理解**

* 加速度計：

  * g（重力加速度）単位で加速度を測定します。
  * 向き、傾き、直線的な動きを検出するのに役立ちます。

* ジャイロスコープ：

  * °/s（毎秒度）単位で回転速度を測定します。
  * 回転や角度の動きを検出するのに役立ちます。

**トラブルシューティングのヒント**

* 出力がない、またはエラーが出る：

  * 配線接続、特にSDAとSCLのラインを確認してください。
  * センサーに正しい電源が供給されていることを確認してください。

* 静止した読み取り：

  * センサーを動かしても読み取りが変化しない場合は、接続が緩んでいないか確認してください。
  * 正しいI2Cアドレスが使用されているか確認してください。

* 一貫性のないデータ：

  * 環境の振動がセンサーの読み取りに影響を与えることがあります。
  * テスト時にはセンサーを安定した面に置いてください。

**結論**

このレッスンでは、MPU-6050加速度計とジャイロスコープセンサーをRaspberry Pi Pico 2 Wとインターフェースする方法を学びました。生のセンサーデータを読み取ることで、モーション検出、向きの追跡、さらには他のさまざまなアプリケーションに応用することができます。
