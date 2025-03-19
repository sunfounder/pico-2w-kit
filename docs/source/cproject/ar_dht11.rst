.. note:: 

    こんにちは！FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Raspberry Pi、Arduino、ESP32について、同じ趣味を持つ人々と一緒にさらに深く探求しましょう。

    **なぜ参加するのか？**

    - **専門的サポート**: コミュニティやチームからの支援を受けて、販売後の問題や技術的な課題を解決します。
    - **学びと共有**: ヒントやチュートリアルを交換し、スキルを向上させます。
    - **独占プレビュー**: 新製品の発表や先取り情報を早期に入手できます。
    - **特別割引**: 最新製品を独占的に割引価格で楽しめます。
    - **祝祭プロモーションとギフト**: ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造してみませんか？[|link_sf_facebook|]をクリックして、今日から参加しましょう！

.. _ar_dht11:


6.2 DHT11を使用した温度と湿度の測定
=======================================================

このレッスンでは、Raspberry Pi Pico 2 Wを使用して **DHT11温湿度センサー** の使い方を学びます。DHT11は、基本的で低コストなデジタルセンサーで、周囲の温度と湿度を測定し、校正されたデジタル出力を提供します。

|img_Dht11|

* :ref:`cpn_dht11`

**必要なコンポーネント**

このプロジェクトには、以下のコンポーネントが必要です。

キット全体を購入すると便利です。こちらがリンクです:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前	
        - このキットに含まれるアイテム
        - 購入リンク
    *   - Pico 2 W スターターキット	
        - 450+
        - |link_pico2w_kit|

以下のリンクから個別に購入することもできます。


.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - コンポーネントの説明	
        - 数量
        - 購入リンク

    *   - 1
        - :ref:`cpn_pico_2w`
        - 1
        - |link_pico2w_buy|
    *   - 2
        - Micro USB Cable
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
        - :ref:`cpn_dht11`
        - 1
        - |link_dht22_buy|

**DHT11センサーについて理解する**

**DHT11** センサーは、容量性湿度センサーとサーミスタを使用して周囲の空気を測定します。データピンにデジタル信号を出力し、使用は非常にシンプルですが、データを読み取るためには正確なタイミングが必要です。

* 温度範囲：0–50°C（±2°Cの精度）
* 湿度範囲：20–80% RH（±5%の精度）
* サンプリングレート：1 Hz（1秒ごと）

**回路図**

|sch_dht11|

**配線**

|wiring_dht11|


**コードの書き方**

DHT11センサーから温度と湿度のデータを読み取り、その値をシリアルモニターに表示するプログラムを書きます。


.. note::

    * ファイル ``6.2_dht11.ino`` を ``pico-2w-kit-main/arduino/6.2_dht11`` のパスで開くことができます。
    * または、このコードを **Arduino IDE** にコピーしてください。
    * アップロードボタンをクリックする前に、Raspberry Pi Picoボードと正しいポートを選択してください。
    * ここでは ``DHT sensor library`` を使用しています。 **ライブラリマネージャー** からインストールできます。

      .. image:: img/lib_dht.png



.. code-block:: arduino

    #include <DHT.h>

    // 接続ピンを定義
    #define DHTPIN 16       // GPIO 16 -> DHT11のデータピン
    #define DHTTYPE DHT11    // センサータイプを定義

    // DHTオブジェクトを作成
    DHT dht(DHTPIN, DHTTYPE);

    unsigned long previousMillis = 0; // 最後に表示が更新された時間を格納
    const long interval = 2000;        // センサーを読み取る間隔（ミリ秒）

    void setup() {
      // 115200ボーでシリアル通信を初期化
      Serial.begin(115200);
      Serial.println(F("DHT11 Sensor Test!"));
    
      // DHTセンサーを初期化
      dht.begin();
   
    }

    void loop() {
      unsigned long currentMillis = millis();

      // 'interval'ミリ秒ごとにセンサーの読み取りを更新
      if (currentMillis - previousMillis >= interval) {
        previousMillis = currentMillis;

        // 湿度と温度を読み取る
        float humidity = dht.readHumidity();
        float temperatureC = dht.readTemperature();
        float temperatureF = dht.readTemperature(true);

        // 読み取りに失敗した場合のチェック
        if (isnan(humidity) || isnan(temperatureC) || isnan(temperatureF)) {
          Serial.println(F("Failed to read from DHT sensor!"));
          return;
        }

        // 熱指数を計算
        float heatIndexC = dht.computeHeatIndex(temperatureC, humidity, false);
        float heatIndexF = dht.computeHeatIndex(temperatureF, humidity);

        // 結果をシリアルモニターに表示
        Serial.print(F("Humidity: "));
        Serial.print(humidity);
        Serial.print(F("%  Temperature: "));
        Serial.print(temperatureC);
        Serial.print(F("°C "));
        Serial.print(temperatureF);
        Serial.print(F("°F  Heat index: "));
        Serial.print(heatIndexC);
        Serial.print(F("°C "));
        Serial.print(heatIndexF);
        Serial.println(F("°F"));
      }
    }

コードをアップロードした後、シリアルモニターは2秒ごとに温度と湿度の読み取り値を表示します。

.. code-block::

    DHT11 Sensor Test!
    Humidity: 45.00%  Temperature: 25.00°C 77.00°F  Heat index: 25.00°C 77.00°F
    Humidity: 46.00%  Temperature: 25.50°C 78.00°F  Heat index: 25.50°C 78.00°F
    Humidity: 47.00%  Temperature: 26.00°C 79.00°F  Heat index: 26.00°C 79.00°F

* **湿度**: センサーを異なる湿度レベルにさらして、読み取り値の変化を観察します。
* **温度**: センサー周囲の温度を変えて、温度計測を観察します。

**コードの理解**

#. ライブラリのインクルードと定数の定義:

   * ``DHT.h``: DHTセンサーライブラリを含むことで、センサーとのやり取りを簡素化します。
   * ``DHTPIN``: DHT11のデータピンに接続されたGPIOピンを指定します。
   * ``DHTTYPE``: 使用しているDHTセンサーのタイプを定義します（この場合はDHT11）。

   .. code-block:: arduino

        #include <DHT.h>
        #define DHTPIN 16       // GPIO 16 -> DHT11のデータピン
        #define DHTTYPE DHT11    // センサータイプを定義

#. ``DHT`` オブジェクトの作成:

   指定されたデータピンとセンサータイプで ``DHT`` オブジェクトを初期化します。

   .. code-block:: arduino

        DHT dht(DHTPIN, DHTTYPE);

#. セットアップ関数:

   * **シリアル通信**: デバッグとデータ表示のためのシリアル通信を開始します。
   * **DHTセンサーの初期化**: データ読取りのためのDHT11センサーを準備します。

   .. code-block:: arduino

        void setup() {
          // 115200ボーでシリアル通信を初期化
          Serial.begin(115200);
          Serial.println(F("DHT11 Sensor Test!"));

          // DHTセンサーを初期化
          dht.begin();
        }

#. ループ関数:

   * ``millis()`` によるタイミング:
   
     ノンブロッキングタイミングを使用して、2秒ごと（interval = 2000ミリ秒）にセンサーを読み取ります。
   
     .. code-block:: arduino
   
        if (currentMillis - previousMillis >= interval) {
          previousMillis = currentMillis;
          ...
        }
   
   * センサーデータの読み取り:
   
     * ``dht.readHumidity()``: 現在の湿度を読み取ります。
     * ``dht.readTemperature()``: セルシウス度で現在の温度を読み取ります。
     * ``dht.readTemperature(true)``: ファーレンハイト度で現在の温度を読み取ります。
   
   * エラーハンドリング:
   
     読み取りに失敗した場合（NaNを返した場合）をチェックし、そうであればエラーメッセージを表示します。
   
     .. code-block:: arduino
   
        if (isnan(humidity) || isnan(temperatureC) || isnan(temperatureF)) {
          Serial.println(F("Failed to read from DHT sensor!"));
          return;
        }
   
   * 熱指数の計算:
   
     * ``dht.computeHeatIndex(temperatureC, humidity, false)``: セルシウス度で熱指数を計算します。
     * ``dht.computeHeatIndex(temperatureF, humidity)``: ファーレンハイト度で熱指数を計算します。
   
   * データの表示:
   
     シリアルモニターに湿度、セルシウス度とファーレンハイト度の温度、熱指数を表示します。
   
     .. code-block:: arduino
   
        Serial.print(F("Humidity: "));
        Serial.print(humidity);
        Serial.print(F("%  Temperature: "));
        Serial.print(temperatureC);
        Serial.print(F("°C "));
        Serial.print(temperatureF);
        Serial.print(F("°F  Heat index: "));
        Serial.print(heatIndexC);
        Serial.print(F("°C "));
        Serial.print(heatIndexF);
        Serial.println(F("°F"));

**トラブルシューティング**

* 表示されない読み取り値:

  * すべての配線接続を確認してください。
  * DHT11センサーが電力を受けていることを確認してください。
  * コード内で正しいGPIOピンが定義されていることを確認してください。

* 読み取り値が不正確:

  * DHT11センサーが損傷していないことを確認してください。
  * センサーのデータシートを確認し、適切なタイミングと信号要件を確認してください。

* センサー干渉:

  * センサーを他の電子デバイスの近くに置かないようにしてください。それによって干渉が起こる可能性があります。
  * センサーの視線を遮る障害物がないことを確認してください。

**さらなる探求**

* ディスプレイとの統合:

  LCDやOLEDディスプレイを接続して、シリアルモニターを使用せずに温度と湿度の読み取り値を表示します。

* アラートの作成:

  温度または湿度が特定の閾値を超えたときに起動するブザーや通知システムを実装します。

* 他のセンサーとの組み合わせ:

  DHT11を動作センサーや光センサー、または他の環境センサーと組み合わせて、包括的なモニタリングシステムを作成します。

* 気象ステーションの構築:

  気圧センサー、雨量計、風速センサーなどの追加センサーをプロジェクトに追加して、本格的な気象ステーションを構築します。

**結論**

このレッスンでは、Raspberry Pi Picoを使用してDHT11温湿度センサーで周囲の温度と湿度を測定し表示する方法を学びました。DHTライブラリを活用することで、環境センシングをプロジェクトに簡単に統合できます。オプショナルのLEDインジケーターは、センサーの読み取り値に基づいた視覚的なフィードバックを追加する簡単な方法を提供し、システムの対話性を高めます。
