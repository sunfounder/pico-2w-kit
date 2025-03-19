.. note::

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Raspberry Pi、Arduino、ESP32について、他の愛好者とともにさらに深く学びましょう。

    **なぜ参加するのか？**

    - **専門家のサポート**: コミュニティやチームのサポートを受けて、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**: スキルを向上させるためのヒントやチュートリアルを交換できます。
    - **独占的なプレビュー**: 新製品の発表や先取り情報をいち早くチェックできます。
    - **特別割引**: 最新製品に対する独占的な割引を楽しめます。
    - **祭事プロモーションとプレゼント**: ギブアウェイや休日のプロモーションに参加できます。

    👉 一緒に探求し、創造しませんか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _ar_motor:

3.5 小型ファンの制御（DCモーター）
=========================================

このレッスンでは、Raspberry Pi Pico 2 Wと **TA6586モータードライバ** を使用して、 **DCモーター** （小型ファンなど）を制御する方法を学びます。TA6586を使うことで、モーターの回転方向を時計回りと反時計回りに制御することができます。DCモーターはPicoが直接供給できる電流よりも多くの電流を必要とするため、モーターを安全に駆動するために外部電源を使用します。

* :ref:`cpn_motor`
* :ref:`cpn_ta6586`
* :ref:`cpn_power_module`

**必要な部品**

このプロジェクトでは、以下の部品が必要です。

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
        - 18650バッテリー
        - 1
        -  

**回路図**

|sch_motor|

**配線**

|wiring_motor|

**コード**

.. note::

    * 「 ``3.5_small_fan.ino`` 」ファイルを「 ``pico-2w-kit-main/arduino/3.5_small_fan`` 」のパスで開きます。
    * または、このコードを **Arduino IDE** にコピーしてください。
    * アップロードボタンをクリックする前に、Raspberry Pi Picoボードと正しいポートを選択してください。

.. code-block:: arduino

    // モータードライバに接続されたピンを定義
    const int motor1A = 14; // モーター制御ピン1
    const int motor2A = 15; // モーター制御ピン2

    void setup() {
      // モーター制御ピンをOUTPUTとして初期化
      pinMode(motor1A, OUTPUT); 
      pinMode(motor2A, OUTPUT); 
    }

    void loop() {
         // モーターを時計回りに回転
         clockwise();
         delay(1000); // モーターを1秒間時計回りに回転
    
        // モーターを停止
        stopMotor();
        delay(1000); // 1秒間停止
    
        // モーターを反時計回りに回転
        anticlockwise();
        delay(1000); // モーターを1秒間反時計回りに回転
    
        // モーターを停止
        stopMotor();
        delay(1000); // 1秒間停止
    }

        // モーターを時計回りに回転させる関数
    void clockwise()
    {
        digitalWrite(motor1A, HIGH); // motor1AをHIGHに設定
        digitalWrite(motor2A, LOW);  // motor2AをLOWに設定
       // この組み合わせでモーターが時計回りに回転します
    }

    // モーターを反時計回りに回転させる関数
    void anticlockwise()
    {
        digitalWrite(motor1A, LOW);  // motor1AをLOWに設定
        digitalWrite(motor2A, HIGH); // motor2AをHIGHに設定
    // この組み合わせでモーターが反時計回りに回転します
    }

    // モーターを停止させる関数
    void stopMotor()
    {
        digitalWrite(motor1A, LOW);  // motor1AをLOWに設定
        digitalWrite(motor2A, LOW);  // motor2AをLOWに設定
    // 両方のピンをLOWに設定することでモーターを停止させます
    }

コードをアップロードした後、モーターは定期的に前後に回転します。


**コードの理解**

#. 制御ピンの定義：

   .. code-block:: arduino

        const int motor1A = 14; // モーター制御ピン1
        const int motor2A = 15; // モーター制御ピン2

#. ピンモードの設定：

   .. code-block:: arduino

        void setup() {
          pinMode(motor1A, OUTPUT); 
          pinMode(motor2A, OUTPUT); 
        }

#. モーターの方向の制御：

   * **時計回りの回転**: motor1をHIGH、motor2AをLOWに設定し、モーターを時計回りに回転させます。

   .. code-block:: arduino

        digitalWrite(motor1A, HIGH); // motor1AをHIGHに設定
        digitalWrite(motor2A, LOW);  // motor2AをLOWに設定

   * **反時計回りの回転**: motor1AをLOW、motor2AをHIGHに設定し、モーターを反時計回りに回転させます。

   .. code-block:: arduino

        digitalWrite(motor1A, LOW);
        digitalWrite(motor2A, HIGH);

   * モーターを1秒間時計回りに回転させます

   .. code-block:: arduino

        anticlockwise();
        delay(1000); 

   * モーターを1秒間反時計回りに回転させます

   .. code-block:: arduino

        anticlockwise();
        delay(1000); 

#. モーターを停止させる：

   両方のピンをLOWに設定してモーターを停止させます。

   .. code-block:: arduino

        digitalWrite(motor1A, LOW);  // motor1AをLOWに設定
        digitalWrite(motor2A, LOW);  // motor2AをLOWに設定
    
   1秒間の停止

      .. code-block:: arduino

        stopMotor();
        delay(1000); 

**さらなる探索**

* 速度制御：

  PWM（パルス幅変調）を使用してモーターの速度を制御することができます。EN1ピンをPWM対応のGPIOピンに接続し、デューティサイクルを変更します。

* センサー統合：

  センサー（例：リミットスイッチ、エンコーダ）を組み合わせて、より高度なモーター制御システムを作成します。

**安全上の注意**

* 電源：

  * 外部電源の電圧がモーターの電圧定格と一致していることを確認してください。
  * Picoの3.3Vピンからモーターを直接駆動しないでください。

* 電流消費：

  * モーターは特に起動時や停止時に大きな電流を消費することがあります。
  * 電源がモーターの電流要求に対応できることを確認してください。

* Picoのリセット：

  * モーターの電流消費が原因で電圧が低下し、Picoがリセットされたり切断されたりする場合があります。
  * モーターを動作させた後にコードのアップロードに問題が生じた場合は、RUNピンをGNDに一時的に接続して手動でPicoをリセットできます。

  |wiring_run_reset|


**結論**

このレッスンでは、Raspberry Pi PicoとTA6586モータードライバを使用してDCモーターを制御する方法を学びました。TA6586への入力制御を行うことで、モーターの回転方向を変更できます。この基本的な概念は、ロボティクスや自動化、モーターを使った多くのアプリケーションで不可欠です。
