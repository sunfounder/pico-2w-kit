.. note:: 

    こんにちは！FacebookのSunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Raspberry Pi、Arduino、ESP32を他の愛好者と一緒に深く学びましょう。

    **参加する理由は？**

    - **専門的なサポート**: 購入後の問題や技術的な課題をコミュニティやチームの助けを借りて解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換し、スキルを向上させましょう。
    - **限定プレビュー**: 新製品の発表や先行公開をいち早くチェックできます。
    - **特別割引**: 新しい製品に対して独占的な割引を楽しめます。
    - **祭典のプロモーションやプレゼント**: プレゼントや祝日プロモーションに参加しましょう。

    👉 一緒に探求し、創造を楽しむ準備はできましたか？[|link_sf_facebook|]をクリックして、今日から参加しましょう！

.. _ar_water:

2.14 水位検出
============================

このレッスンでは、Raspberry Pi Pico 2 Wを使用して **水センサー** で水の存在を検出したり、水位を測定する方法を学びます。このセンサーは、降雨検出、浮き水位の監視、液体漏れ警告などのプロジェクトで広く使用されています。

**水センサーの動作原理**

水センサーには、一連の露出した平行ワイヤーがあり、水滴を検出したり、水の量を測定することができます。水がこれらのワイヤーに接触すると、センサーはアナログ信号を出力します。センサーに接触する水の量が多くなるほど、出力値が高くなり、その値はRaspberry Pi Pico 2 Wのアナログ・デジタル変換器（ADC）によって読み取ることができます。

|img_water_sensor|

* センサーを完全に水に浸さないでください。露出したワイヤーの部分のみを水に接触させるようにしてください。
* 電源が入ったままで湿気の多い環境で使用すると、プローブが早く腐食する可能性があるため、読み取り時にのみセンサーの電源を入れることをお勧めします。

* :ref:`cpn_water_level`

**必要なコンポーネント**

このプロジェクトでは、以下のコンポーネントが必要です。

全セットを購入するのが便利なので、こちらのリンクをチェックしてください：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前
        - このキットのアイテム
        - 購入リンク
    *   - Pico 2 Wスターターキット
        - 450+
        - |link_pico2w_kit|

以下のリンクから、コンポーネントを個別に購入することもできます。


.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - コンポーネント紹介
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
        - 数個
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_water_level`
        - 1
        - 

**回路図**

|sch_water|


**配線**

|wiring_water|

**コード作成**

.. note::

    * ``2.14_feel_the_water_level.ino`` ファイルを ``pico-2w-kit-main/arduino/2.14_feel_the_water_level`` から開きます。
    * または、このコードを **Arduino IDE** にコピーします。
    * **Raspberry Pi Pico** ボードと正しいポートを選択して、「アップロード」をクリックします。

.. code-block:: arduino

   const int waterSensorPin = 28;  // 水センサーがGP28（ADC2）に接続されています

   void setup() {
     Serial.begin(115200);  // シリアルモニタの初期化
   }

   void loop() {
     // 水センサーからアナログ値を読み取る
     int sensorValue = analogRead(waterSensorPin);
     // シリアルモニタにセンサー値を表示
     Serial.print("Water Sensor Value: ");
     Serial.println(sensorValue);
     delay(500);  // 500ミリ秒待ってから再度読み取る
   }

コードをアップロードした後、シリアルモニタを開くと、水センサーからのアナログ値を表す数値が表示されるはずです。

* センサーが乾いているとき、センサー値は低く（0に近い）なります。
* センサーを水に優しく浸し、センサーのワイヤーがさらに多く水に浸かると、センサー値が増加します。

**コードの理解**

#. センサーピンの定義：

   ``waterSensorPin`` をGPIO 28に割り当て、アナログ入力に接続します。

   .. code-block:: arduino

      const int waterSensorPin = 28;  // 水センサーがGP28（ADC2）に接続されています


#. シリアル通信の初期化：

   シリアル通信を開始し、シリアルモニタにメッセージを表示できるようにします。

   .. code-block:: arduino

      Serial.begin(115200);

#. アナログ値の読み取り：

   ``waterSensorPin`` でアナログ電圧を読み取り、0から1023の間の値を返します（10ビットのADC）。

   .. code-block:: arduino

      int sensorValue = analogRead(waterSensorPin);

#. センサー値の表示：

   センサー値をシリアルモニタに出力します。

   .. code-block:: arduino

      Serial.print("Water Sensor Value: ");
      Serial.println(sensorValue);

#. 遅延の追加：

   次の読み取りまで500ミリ秒待機します。

   .. code-block:: arduino

      delay(500);


**水センサーをデジタルセンサーとして使用する**

アナログ入力モジュールをデジタルセンサーとして使用するために、閾値値を設定することができます。

* 閾値を決定する：

  * センサーが乾いているときにセンサー値を読み取ります。
  * この値を基準値として使用します（例：乾いているときの値が約100の場合）。

* コードの変更：

   .. code-block:: arduino

      const int waterSensorPin = 28;  // 水センサーがGP28（ADC2）に接続されています
      const int threshold = 500;      // 閾値を設定

      void setup() {
        Serial.begin(115200);  // シリアルモニタの初期化
      }

      void loop() {
        // 水センサーからアナログ値を読み取る
        int sensorValue = analogRead(waterSensorPin);

        // センサー値が閾値を超えたかどうか確認
        if (sensorValue > threshold) {
          Serial.println("Water Detected!");
        } else {
          Serial.println("No Water Detected.");
        }
        delay(500);  // 500ミリ秒待ってから再度読み取る
      }

センサーを水漏れの可能性がある場所に設置します。水がセンサーに接触すると、シリアルモニタに「水が検出されました！」と表示されるはずです。

**安全上の注意**

* 短絡を避ける：

  * 接続が確実であり、センサーが露出したワイヤー部分以上に浸水しないことを確認してください。
  * Picoやその他の電子部品が水に接触しないようにしてください。

* 腐食防止：

  * センサーを長時間水に浸したままで電源を入れたままにしないでください。
  * 使用後はセンサーをしっかり乾燥させ、腐食を防止してください。

**さらなる探求**

* 水位アラーム：

  水が検出されたときにブザーやLEDで通知する機能を追加します。

* 自動ポンプ制御：

  センサーを使用して水位に基づきポンプをオンまたはオフに制御します。

* データロギング：

  時間の経過とともに水位の変化を記録し、解析します。

**結論**

このレッスンでは、Raspberry Pi Picoを使用して水センサーで水の存在を検出したり、水位を測定したりする方法を学びました。センサーからのアナログ値を読み取ることで、水位の変化を監視し、プロジェクト内でそれに応じた対応ができるようになります。
