.. note::

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Raspberry Pi、Arduino、ESP32について、他の愛好者とともにさらに深く学びましょう。

    **なぜ参加するのか？**

    - **専門家のサポート**: コミュニティやチームのサポートを受けて、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**: スキルを向上させるためのヒントやチュートリアルを交換できます。
    - **独占的なプレビュー**: 新製品の発表や先取り情報をいち早くチェックできます。
    - **特別割引**: 最新製品に対する独占的な割引を楽しめます。
    - **祭事プロモーションとプレゼント**: ギブアウェイや休日のプロモーションに参加できます。

    👉 一緒に探求し、創造しませんか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _ar_mpu6050:

6.3 MPU-6050からのデータ読み取り
=================================

このレッスンでは、 **MPU-6050** 6軸モーショントラッキングセンサーをRaspberry Pi Pico 2 Wに接続して使用する方法を学びます。MPU-6050は、3軸ジャイロスコープと3軸加速度計を組み合わせたセンサーで、I2C通信プロトコルを通じて生データを提供します。

* :ref:`cpn_mpu6050`

**必要な部品**

このプロジェクトには、以下の部品が必要です。

全体キットを購入するのが非常に便利です。リンクはこちらです：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前
        - このキットに含まれるアイテム
        - 購入リンク
    *   - Pico 2 W スターターキット
        - 450以上
        - |link_pico2w_kit|

以下のリンクから個別に購入することもできます。


.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - 部品紹介
        - 数量
        - 購入リンク

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

**MPU-6050センサーの理解**

**MPU-6050** センサーは、ドローン、ロボット、ゲームデバイスなど、モーショントラッキングや方向検出を必要とするプロジェクトで広く使用されています。

* **加速度計**: X、Y、Z軸に沿った加速度を測定します。これには重力加速度も含まれており、センサーの傾きや方向を検出することができます。
* **ジャイロスコープ**: X、Y、Z軸を中心に回転速度を測定し、センサーがどれだけ速く回転しているかの情報を提供します。

**回路図**

|sch_mpu6050_ar|

**配線**

|wiring_mpu6050_ar|

**コードの記述**

MPU-6050センサーを初期化し、加速度計とジャイロスコープのデータを読み取り、シリアルモニターに値を表示するプログラムを作成します。


.. note::

    * 「 ``6.3_6axis_motion_tracking.ino`` 」ファイルを「 ``pico-2w-kit-main/arduino/6.3_6axis_motion_tracking`` 」のパスで開きます。
    * または、このコードを **Arduino IDE** にコピーしてください。
    * アップロードボタンをクリックする前に、Raspberry Pi Picoボードと正しいポートを選択してください。
    * ここでは ``Adafruit MPU6050`` ライブラリを使用しています。 **ライブラリマネージャ** からインストールできます。


      .. image:: img/lib_mpu6050.png


.. code-block:: arduino

    #include <Adafruit_MPU6050.h>
    #include <Wire.h>

    // MPU6050オブジェクトを作成
    Adafruit_MPU6050 mpu;

    void setup(void) {
      // シリアル通信の初期化
      Serial.begin(115200);

      Serial.println("Adafruit MPU6050 test!");

      // MPU6050の初期化を試みる
      if (!mpu.begin()) {
        Serial.println("Failed to find MPU6050 chip");
        while (1) {
          delay(10);
        }
      }
      Serial.println("MPU6050が見つかりました!");

      // 加速度計の範囲設定
      mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
      Serial.print("Accelerometer range set to: ");
      switch (mpu.getAccelerometerRange()) {
        case MPU6050_RANGE_2_G:
          Serial.println("+-2G");
          break;
        case MPU6050_RANGE_4_G:
          Serial.println("+-4G");
          break;
        case MPU6050_RANGE_8_G:
          Serial.println("+-8G");
          break;
        case MPU6050_RANGE_16_G:
          Serial.println("+-16G");
          break;
      }

      // ジャイロスコープの範囲設定
      mpu.setGyroRange(MPU6050_RANGE_500_DEG);
      Serial.print("Gyro range set to: ");
      switch (mpu.getGyroRange()) {
        case MPU6050_RANGE_250_DEG:
          Serial.println("+-250 deg/s");
          break;
        case MPU6050_RANGE_500_DEG:
          Serial.println("+-500 deg/s");
          break;
        case MPU6050_RANGE_1000_DEG:
          Serial.println("+-1000 deg/s");
          break;
        case MPU6050_RANGE_2000_DEG:
          Serial.println("+-2000 deg/s");
          break;
      }

      // フィルタ帯域幅設定
      mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);
      Serial.print("Filter bandwidth set to: ");
      switch (mpu.getFilterBandwidth()) {
        case MPU6050_BAND_260_HZ:
          Serial.println("260 Hz");
          break;
        case MPU6050_BAND_184_HZ:
          Serial.println("184 Hz");
          break;
        case MPU6050_BAND_94_HZ:
          Serial.println("94 Hz");
          break;
        case MPU6050_BAND_44_HZ:
          Serial.println("44 Hz");
          break;
        case MPU6050_BAND_21_HZ:
          Serial.println("21 Hz");
          break;
        case MPU6050_BAND_10_HZ:
          Serial.println("10 Hz");
          break;
        case MPU6050_BAND_5_HZ:
          Serial.println("5 Hz");
          break;
      }

      Serial.println("");
      delay(100);
    }

    void loop() {
      // 新しいセンサーイベントを取得
      sensors_event_t a, g, temp;
      mpu.getEvent(&a, &g, &temp);

      // 加速度の値を表示
      Serial.print("Acceleration X: ");
      Serial.print(a.acceleration.x);
      Serial.print(" m/s^2, Y: ");
      Serial.print(a.acceleration.y);
      Serial.print(" m/s^2, Z: ");
      Serial.print(a.acceleration.z);
      Serial.println(" m/s^2");

      // ジャイロの値を表示
      Serial.print("Rotation X: ");
      Serial.print(g.gyro.x);
      Serial.print(" rad/s, Y: ");
      Serial.print(g.gyro.y);
      Serial.print(" rad/s, Z: ");
      Serial.print(g.gyro.z);
      Serial.println(" rad/s");

      delay(500); // 必要に応じて遅延を調整
    }


コードをアップロードした後、シリアルモニターに加速度と回転の値が継続的に表示されます。

.. code-block::

    Adafruit MPU6050 test!
    MPU6050 Found!
    Accelerometer range set to: +-8G
    Gyro range set to: +-500 deg/s
    Filter bandwidth set to: 21 Hz

    Acceleration X: 0.00 m/s^2, Y: 0.00 m/s^2, Z: 9.81 m/s^2
    Rotation X: 0.02 rad/s, Y: -0.01 rad/s, Z: 0.00 rad/s
    Acceleration X: 0.10 m/s^2, Y: 0.05 m/s^2, Z: 9.76 m/s^2
    Rotation X: 0.15 rad/s, Y: -0.05 rad/s, Z: 0.02 rad/s

MPU-6050センサーモジュールを優しく回転または動かしてください。
加速度と回転の値が移動に応じて変化するのを観察してください。

**コードの理解**

#. ライブラリのインクルードと定数の定義：


   * ``Adafruit_MPU6050.h``: MPU6050ライブラリをインクルードし、簡単にインターフェースします。
   * ``Wire.h``: I2C通信ライブラリをインクルードします。
   * ``mpu``: MPU6050オブジェクトを作成し、センサーとやり取りします。

#. Setup Function:

   * MPU6050の初期化：
   
     MPU6050センサーを初期化し、失敗した場合はエラーメッセージを表示し、プログラムを停止します。
   
     .. code-block:: arduino
   
         Serial.println("Adafruit MPU6050 test!");
   
         // MPU6050の初期化を試みる
         if (!mpu.begin()) {
           Serial.println("Failed to find MPU6050 chip");
           while (1) {
             delay(10);
           }
         }
         Serial.println("MPU6050 Found!");

   * 加速度計の範囲：
   
     加速度計の範囲を±8Gに設定し、現在の範囲を表示します。
   
     .. code-block:: arduino
   
         mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
         Serial.print("Accelerometer range set to: ");
         switch (mpu.getAccelerometerRange()) {
           case MPU6050_RANGE_2_G:
             Serial.println("+-2G");
             break;
            ...
           case MPU6050_RANGE_16_G:
             Serial.println("+-16G");
             break;
         }

   * ジャイロスコープの範囲：
   
     ジャイロスコープの範囲を±500度/秒に設定し、現在の範囲を表示します。
   
     .. code-block:: arduino
   
         mpu.setGyroRange(MPU6050_RANGE_500_DEG);
         Serial.print("Gyro range set to: ");
         switch (mpu.getGyroRange()) {
           case MPU6050_RANGE_250_DEG:
             Serial.println("+-250 deg/s");
             break;
            ...
           case MPU6050_RANGE_2000_DEG:
             Serial.println("+-2000 deg/s");
             break;
         }

   * フィルタ帯域幅の設定：
   
     フィルタ帯域幅を21Hzに設定し、現在の設定を表示します。
   
     .. code-block:: arduino
   
         mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);
         Serial.print("Filter bandwidth set to: ");
         switch (mpu.getFilterBandwidth()) {
           case MPU6050_BAND_260_HZ:
             Serial.println("260 Hz");
             break;
            ...
           case MPU6050_BAND_5_HZ:
             Serial.println("5 Hz");
             break;
         }

#. Loop Function:

   * センサーデータの読み取り：
   
     * ``sensors_event_t a, g, temp;``: 加速度計、ジャイロスコープ、温度データを格納するイベントオブジェクトを作成します。
     * ``mpu.getEvent(&a, &g, &temp);``: 最新のセンサーデータを取得します。
   
     .. code-block:: arduino
   
         sensors_event_t a, g, temp;
         mpu.getEvent(&a, &g, &temp);
   
   * センサーデータの表示：
   
     * **加速度**: X、Y、Z軸に沿った加速度の値をm/s²で表示します。
     * **回転**: ジャイロスコープの回転速度（rad/s）をX、Y、Z軸に沿って表示します。
   
     .. code-block:: Arduino
   
       // 加速度の値を表示
       Serial.print("Acceleration X: ");
       Serial.print(a.acceleration.x);
       ...
       Serial.print(g.gyro.y);
       Serial.print(" rad/s, Z: ");
       Serial.print(g.gyro.z);
       Serial.println(" rad/s");


**トラブルシューティング**


* 表示されない場合：

  * 配線の接続、特にI2Cライン（SCLおよびSDA）を確認してください。
  * MPU-6050センサーが電力（VCCおよびGND接続）を受け取っていることを確認してください。
  * コード内で正しいGPIOピンが定義されているかを確認してください。


* 読み取り値が正しくない場合：

  * MPU-6050センサーがブレッドボードにしっかりと装着されていることを確認してください。
  * センサーの範囲とフィルター設定が希望するアプリケーションに合っていることを確認してください。
  * 配線の接続が緩んでいないか、ショートがないかを確認してください。

* センサーの干渉：

  * センサーを他の電子デバイスの近くに置かないようにしてください。それによって干渉が生じる可能性があります。
  * センサーの動きを遮る物理的な障害物がないことを確認してください。

**さらなる探求**

* 他のセンサーとの組み合わせ：

  MPU-6050をGPSモジュール、磁力計、その他のセンサーと統合して、包括的な追跡システムを作成してください。

* モーションベースのゲームコントローラーの構築：

  MPU-6050を使用して動きと向きを検出し、モーションコントロール型のゲームデバイスを作成してください。

* 自己バランスロボットの作成：

  加速度計とジャイロスコープのデータを利用して、ロボティクスアプリケーションでのバランスと安定性を維持してください。

* センサーフュージョンアルゴリズムの実装：

  加速度計とジャイロスコープのデータを組み合わせて、カルマンフィルターや補完フィルターのようなアルゴリズムを使用して、向きの角度を計算してください。

**まとめ**

このレッスンでは、MPU-6050 6軸モーショントラッキングセンサーをRaspberry Pi Picoに接続する方法を学びました。Adafruit MPU6050ライブラリを活用することで、加速度計とジャイロスコープのデータを容易に取得し解釈でき、多岐にわたる動きと向きベースのアプリケーションを可能にします。オプションのLEDインジケーターは、センサーの読み取りに基づいた視覚的なフィードバックを提供する簡単な方法を追加し、プロジェクトの対話性を向上させます。

