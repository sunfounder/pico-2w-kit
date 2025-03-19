.. note::

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！ Raspberry Pi、Arduino、ESP32について、仲間たちと一緒にさらに深く学びましょう。

    **なぜ参加するべきか？**

    - **専門的なサポート**：コミュニティやチームの助けを借りて、購入後の問題や技術的な課題を解決します。
    - **学び＆共有**：スキルを向上させるためのヒントやチュートリアルを交換しましょう。
    - **限定プレビュー**：新製品の発表や先行情報をいち早く入手できます。
    - **特別割引**：最新の製品に対する専用の割引を楽しめます。
    - **季節限定プロモーションやプレゼント**：プレゼント企画やホリデープロモーションに参加しましょう。

    👉 一緒に探求し、創造してみませんか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _ar_ultrasonic:

6.1 超音波センサーを使った距離測定
===================================

このレッスンでは、Raspberry Pi Pico 2 Wを使用して **超音波センサー モジュール** で物体までの距離を測定する方法を学びます。超音波センサーは、物体検出や距離測定のためにロボティクスや自動化システムで広く使用されています。

* :ref:`cpn_ultrasonic`

**必要なコンポーネント**

このプロジェクトには、以下のコンポーネントが必要です。

セットで購入すると便利です。こちらがリンクです：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前	
        - このキットに含まれているアイテム
        - 購入リンク
    *   - Pico 2 Wスターターキット	
        - 450+
        - |link_pico2w_kit|

また、以下のリンクから個別に購入することもできます。


.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - 番号
        - コンポーネント紹介	
        - 数量
        - 購入リンク

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

**超音波センサーの理解**

超音波センサーは、 **Trig** ピンから短い超音波パルスを発信し、 **Echo** ピンで反響を受信することで動作します。反響が戻るまでの時間を測定することにより、音速を利用して物体までの距離を計算できます。

|ultrasonic_prin|

* **トリガーパルス**：Trigピンに10マイクロ秒の高いパルスを出力して測定を開始します。
* **超音波バースト**：センサーは40 kHzで8サイクルの超音波バーストを発信します。
* **エコー受信**：Echoピンが高くなり、エコーが戻るまで高い状態を保ちます。
* **時間測定**：Echoピンが高い状態を保っている時間を測定し、距離を計算します。

**回路図**

|sch_ultrasonic|

**配線**

|wiring_ultrasonic|

**コードを書く**

超音波センサーをトリガーし、エコーの時間を測定して物体までの距離を計算するプログラムを作成します。計算された距離はシリアルモニターに表示されます。

.. note::

    * ``6.1_ultrasonic.ino`` ファイルは、 ``pico-2w-kit-main/arduino/6.1_ultrasonic`` パスにあります。
    * あるいは、このコードを **Arduino IDE** にコピーしてください。
    * **アップロード** ボタンをクリックする前に、ボード（Raspberry Pi Pico）と適切なポートを選択することを忘れないでください。


.. code-block:: arduino

    // 接続ピンの定義
    const int trigPin = 17;  // GPIO 17 -> Trig
    const int echoPin = 16;  // GPIO 16 -> Echo

    void setup() {
      // シリアル通信を115200ボーレートで開始
      Serial.begin(115200);
    
      // センサーピンの初期化
      pinMode(trigPin, OUTPUT);
      pinMode(echoPin, INPUT);
    }

    void loop() {
      long duration;
      float distance;

      // Trigピンを10マイクロ秒間HIGHにしてセンサーをトリガー
      digitalWrite(trigPin, HIGH);
      delayMicroseconds(10);
      digitalWrite(trigPin, LOW);
    
      // Echoピンを読み、マイクロ秒単位での時間を取得
      duration = pulseIn(echoPin, HIGH);
    
      // 距離をセンチメートル単位で計算
      distance = duration * 0.034 / 2;
    
      // シリアルモニターに距離を表示
      Serial.print("Distance: ");
      Serial.print(distance);
      Serial.println(" cm");
    
      delay(500); // 次の測定まで0.5秒待機
    }

コードをアップロードした後、シリアルモニターにはセンチメートル単位での距離が表示されます。

.. code-block::

    Distance: 25.3 cm
    Distance: 24.8 cm
    Distance: 24.5 cm

センサーから異なる距離に物体を配置してください。
物体を近づけたり遠ざけたりして、距離の変化を観察してください。

**コードの理解**

#. 接続ピンの定義：

   * ``trigPin``：超音波パルスを送信します。
   * ``echoPin``：超音波パルスの反響を受信します。

   .. code-block:: arduino

        const int trigPin = 17;  // GPIO 17 -> Trig
        const int echoPin = 16;  // GPIO 16 -> Echo

#. setup関数：

   * **シリアル通信**：Picoとコンピュータ間の通信を有効にしてデバッグします。
   * **ピンモード**： ``Trig`` ピンを ``OUTPUT`` に、 ``Echo`` ピンを ``INPUT`` に設定します。

   .. code-block:: arduino

        void setup() {
          // シリアル通信を115200ボーレートで開始
          Serial.begin(115200);

          // センサーピンの初期化
          pinMode(trigPin, OUTPUT);
          pinMode(echoPin, INPUT);
        }

#. loop関数：

   * **センサーのトリガー**： ``Trig`` ピンを10マイクロ秒間 ``HIGH`` にして超音波パルスを送信。 ``Trig`` ピンを ``LOW`` にしてパルスを終了します。

     .. code-block:: arduino

        digitalWrite(trigPin, HIGH);
        delayMicroseconds(10);
        digitalWrite(trigPin, LOW);

   * **エコーの読み取り**： ``Echo`` ピンが ``HIGH`` で保持されている時間（反響の戻るまでの時間）を測定します。

     .. code-block:: arduino

        duration = pulseIn(echoPin, HIGH);

   * **距離の計算**：時間を距離（cm/マイクロ秒）に変換します。パルスの往復時間を考慮して2で割ります。

     .. code-block:: arduino

        distance = duration * 0.034 / 2;

   * **シリアル出力**：計算された距離をシリアルモニターに表示してリアルタイムでモニタリングします。

     .. code-block:: arduino

        Serial.print("Distance: ");
        Serial.print(distance);
        Serial.println(" cm");

   * **遅延**：シリアルモニターが洪水のように出力されないように500ミリ秒の遅延を加えます。次の測定まで時間を空けます。

**トラブルシューティング**

* 測定結果が表示されない場合：

  * TrigピンとEchoピンが正しく接続されていることを確認してください。
  * センサーが電力供給（VCCおよびGND接続）を受けているか確認してください。
  * シリアルモニターが正しいボーレートに設定されていることを確認してください。

* 誤った測定値が表示される場合：

  * コード内の計算が正しいか確認してください。
  * 環境によって音速定数（0.034）が適切か確認してください（湿度や温度が音速に影響を与えることがあります）。


* センサーの干渉：

  * 超音波パルスを妨害する障害物や反射面がないことを確認してください。
  * 他の超音波デバイスの近くにセンサーを置かないようにしてください。誤った測定が行われることがあります。


**さらに探求してみよう**

* LEDやディスプレイとの統合：

  * 複数のLEDを使って距離を視覚的に表示する。
  * 7セグメントディスプレイやLCDディスプレイを使って距離を数値的に表示する。

* 近接警報システムの作成：

  距離が特定の閾値に達したときに警報を鳴らすなどのシステムを作成する。

* シンプルな障害物回避ロボットの作成：

  超音波センサーを使用して障害物を検出し、それらを回避するロボットを作成する。

**結論**

このレッスンでは、超音波センサー モジュールを使用してRaspberry Pi Picoで物体までの距離を測定する方法を学びました。超音波パルスをトリガーし、エコーの時間を測定することにより、近くの物体までの距離を正確に測定できます。このプロジェクトは、ロボティクス、自動化、インタラクティブシステムなど、より複雑なアプリケーションの基盤となります。
