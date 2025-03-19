.. note:: 

    こんにちは、SunFounderのRaspberry Pi、Arduino、ESP32愛好者コミュニティへようこそ！ Raspberry Pi、Arduino、ESP32について、他の愛好者と一緒にさらに深く学んでいきましょう。

    **なぜ参加するべきか？**

    - **専門家サポート**：コミュニティやチームから、販売後の問題や技術的な課題の解決をサポートします。
    - **学びと共有**：ヒントやチュートリアルを交換し、スキルを向上させましょう。
    - **限定プレビュー**：新製品の発表や先行情報をいち早くゲットできます。
    - **特別割引**：最新製品に対する限定割引を楽しめます。
    - **フェスティブプロモーションとプレゼント企画**：プレゼント企画や祝祭プロモーションに参加しましょう。

    👉 一緒に探求し、創造してみませんか？ [|link_sf_facebook|] をクリックして今すぐ参加しましょう！

.. _ar_74hc_4dig:

5.3 4桁7セグメントディスプレイを使ったタイムカウンターの作成
==============================================================

このレッスンでは、Raspberry Pi Pico 2 Wを使用して、 **4桁7セグメントディスプレイ** を使ったシンプルなタイムカウンターを作成する方法を学びます。このディスプレイは、1秒ごとにカウントアップし、経過時間を秒単位で表示します。


**必要なコンポーネント**

このプロジェクトでは、以下のコンポーネントが必要です。

全てが含まれたキットを購入するのが便利です。リンクはこちらです：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前
        - キット内容
        - 購入リンク
    *   - Pico 2 Wスターターキット
        - 450+
        - |link_pico2w_kit|

これらの部品を別々に購入することもできます。リンクは下記にあります。


.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - 番号
        - コンポーネントの紹介
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
        - 数個
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_resistor`
        - 4個（220Ω）
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_4_dit_7_segment`
        - 1
        - 
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|


**4桁7セグメントディスプレイの理解**

4桁7セグメントディスプレイは、4つの個別の7セグメントディスプレイが1つのモジュールに組み合わさったものです。各桁は同じセグメント制御線（ **a** 〜 **g** および **dp** ）を共有していますが、各桁には独自の **共通カソード** 制御があります。この構成により、どの桁をアクティブにするかを制御できます。

共有されたセグメント線を使用して異なる数字を表示するために、 **マルチプレクシング** という技術を使用します。桁間を高速で切り替え、1回の更新で1桁ずつ更新しますが、視覚的にはすべての桁が同時に表示されているように見えます。

|4digit_control_pins|

**回路図**

|sch_4dig|

ここでの配線原理は基本的に :ref:`ar_74hc_led` と同じですが、違いはQ0-Q7が4桁7セグメントディスプレイのa〜gピンに接続されている点です。

次に、G10〜G13がどの7セグメントディスプレイを動作させるかを選択します。

**配線**

|wiring_4dig|

* **セグメント接続（220Ωの抵抗を介して）**:

  * **Q0** → セグメント **a**
  * **Q1** → セグメント **b**
  * **Q2** → セグメント **c**
  * **Q3** → セグメント **d**
  * **Q4** → セグメント **e**
  * **Q5** → セグメント **f**
  * **Q6** → セグメント **g**
  * **Q7** → セグメント **dp** （小数点）

* **共通カソード接続（桁選択ピン）**:

  * **桁1（最左桁）** : **GP10** に接続
  * **桁2** : **GP11** に接続
  * **桁3** : **GP12** に接続
  * **桁4（最右桁）** : **GP13** に接続

**コードの記述**

.. note::

    * ファイル ``5.3_time_counter.ino`` を ``pico-2w-kit-main/arduino/5.3_time_counter`` のパスで開くことができます。
    * または、このコードを **Arduino IDE** にコピーして使用してください。
    * **アップロード** ボタンをクリックする前に、ボード（Raspberry Pi Pico）と正しいポートを選択することを忘れないでください。

.. code-block:: arduino

    // シフトレジスタの接続ピンを定義
    #define DATA_PIN 18   // DS（シリアルデータ入力）
    #define LATCH_PIN 19  // STCP（ストレージレジスタクロック）
    #define CLOCK_PIN 20  // SHCP（シフトレジスタクロック）

    // 4桁7セグメントディスプレイの桁制御ピンを定義
    const int digitPins[4] = { 10, 11, 12, 13 };  // DIG1, DIG2, DIG3, DIG4

    // 数字0〜9のセグメントバイトマップ
    const byte digitCodes[10] = {
      // Pgfedcba
      0b00111111,  // 0
      0b00000110,  // 1
      0b01011011,  // 2
      0b01001111,  // 3
      0b01100110,  // 4
      0b01101101,  // 5
      0b01111101,  // 6
      0b00000111,  // 7
      0b01111111,  // 8
      0b01101111   // 9
    };

    unsigned long previousMillis = 0;  // 最後にディスプレイが更新された時間を保存
    unsigned int counter = 0;          // カウンター値

    void setup() {
      // シフトレジスタのピンを初期化
      pinMode(DATA_PIN, OUTPUT);
      pinMode(LATCH_PIN, OUTPUT);
      pinMode(CLOCK_PIN, OUTPUT);

      // 桁制御ピンを初期化
      for (int i = 0; i < 4; i++) {
        pinMode(digitPins[i], OUTPUT);
        digitalWrite(digitPins[i], HIGH);  // すべての桁をオフにする
      }
    }

    void loop() {
      unsigned long currentMillis = millis();

      // 1000ミリ秒ごとにカウンターを更新
      if (currentMillis - previousMillis >= 1000) {
        previousMillis = currentMillis;
        counter++;  // カウンターを増加
        if (counter > 9999) {
          counter = 0;  // 9999を超えたらカウンターをリセット
        }
      }

      // カウンター値を表示
      displayNumber(counter);
    }

    void displayNumber(int num) {
      // 数字を桁ごとに分解
      int digits[4];
      digits[0] = num / 1000;        // 千の位
      digits[1] = (num / 100) % 10;  // 百の位
      digits[2] = (num / 10) % 10;   // 十の位
      digits[3] = num % 10;          // 一の位

      // 各桁を表示
      for (int i = 0; i < 4; i++) {
        digitalWrite(digitPins[i], LOW);  // 現在の桁をアクティブに
        shiftOutDigit(digitCodes[digits[i]]);
        delay(5);                          // マルチプレクシング用の小さな遅延
        digitalWrite(digitPins[i], HIGH);  // 現在の桁を非アクティブに
      }
    }

    void shiftOutDigit(byte data) {
      // シフトレジスタにデータを送信
      digitalWrite(LATCH_PIN, LOW);
      shiftOut(DATA_PIN, CLOCK_PIN, MSBFIRST, data);
      digitalWrite(LATCH_PIN, HIGH);
    }

アップロード後、4桁7セグメントディスプレイは0000からカウントアップを開始し、1秒ごとに1ずつ増加します。
カウントは次のように進みます: 0000, 0001, 0002, ..., 9999、そして再び0000にリセットされます。

**コードの理解**

#. 制御ピンの定義:

   * ``DATA_PIN (DS)``: シリアルデータを74HC595にシフトインするためのピン。
   * ``LATCH_PIN (STCP)``: シフトレジスタから出力ピンへのデータのロッチを制御するピン。
   * ``CLOCK_PIN (SHCP)``: シフトレジスタにデータをシフトするためのピン。

   .. code-block:: arduino

      #define DATA_PIN   18  // DS（シリアルデータ入力）
      #define LATCH_PIN  19  // STCP（ストレージレジスタクロック）
      #define CLOCK_PIN  20  // SHCP（シフトレジスタクロック）

#. 桁制御ピンの定義:

   * 各桁の共通カソードはそれぞれのGPIOピンに接続されています。
   * 桁ピンをLOWに設定すると、その桁がアクティブになり、HIGHに設定すると非アクティブになります。

   .. code-block:: arduino

      const int digitPins[4] = {10, 11, 12, 13}; // DIG1, DIG2, DIG3, DIG4

#. セグメントバイトマップの作成:

   * 各バイトは、数字0〜9を共通カソード7セグメントディスプレイに表示するために点灯すべきセグメントを表します。
   * ビットはa〜gおよびdpのセグメントに対応しています。

   .. code-block:: arduino

      const byte digitCodes[10] = {
        0b00111111, // 0
        0b00000110, // 1
        0b01011011, // 2
        0b01001111, // 3
        0b01100110, // 4
        0b01101101, // 5
        0b01111101, // 6
        0b00000111, // 7
        0b01111111, // 8
        0b01101111  // 9
      };

#. setup関数:

   * ``DATA_PIN`` 、 ``LATCH_PIN`` 、 ``CLOCK_PIN`` を出力として設定します。
   * すべての桁制御ピンを ``HIGH`` に設定して、スタート時にすべての桁を非アクティブにします。

   .. code-block:: arduino

      void setup() {
        // シフトレジスタのピンを初期化
        pinMode(DATA_PIN, OUTPUT);
        pinMode(LATCH_PIN, OUTPUT);
        pinMode(CLOCK_PIN, OUTPUT);

        // 桁制御ピンを初期化
        for (int i = 0; i < 4; i++) {
          pinMode(digitPins[i], OUTPUT);
          digitalWrite(digitPins[i], HIGH); // すべての桁を初期状態でオフにする
        }
      }

#. loop関数:

   * ``millis()`` 関数を使用して、ブロックせずに経過時間を追跡します。
   * カウンターを1秒ごとにインクリメントし、9999に達したらリセットします。

   .. code-block:: arduino

      void loop() {
        unsigned long currentMillis = millis();

        // 1000ミリ秒ごとにカウンターを更新
        if (currentMillis - previousMillis >= 1000) {
          previousMillis = currentMillis;
          counter++; // カウンターを増加
          if (counter > 9999) {
            counter = 0; // 9999を超えたらカウンターをリセット
          }
        }

        // カウンター値を表示
        displayNumber(counter);
      }

#. 数字の表示:

   * ``counter`` の値を千の位、百の位、十の位、一の位に分けます。
   * 各桁を順番にアクティブにし、対応するセグメントデータを送信して桁を非アクティブにします。
   * 桁間の迅速な切り替えにより、すべての桁が同時に点灯しているように見えます。

   .. code-block:: arduino

      void displayNumber(int num) {
        // 数字を個別の桁に分解
        int digits[4];
        digits[0] = num / 1000;         // 千の位
        digits[1] = (num / 100) % 10;   // 百の位
        digits[2] = (num / 10) % 10;    // 十の位
        digits[3] = num % 10;           // 一の位

        // 各桁を順番に表示
        for (int i = 0; i < 4; i++) {
          digitalWrite(digitPins[i], LOW); // 現在の桁をアクティブに

          // 現在の桁のセグメントデータをシフトアウト
          shiftOutDigit(digitCodes[digits[i]]);

          delay(5);                        // マルチプレクシング用の小さな遅延
          digitalWrite(digitPins[i], HIGH); // 現在の桁を非アクティブに
        }
      }

#. セグメントデータのシフトアウト:

   * 74HC595シフトレジスタにセグメントデータを送信します。
   * ``shiftOut()`` は、最上位ビット（ ``MSBFIRST`` ）から1ビットずつデータを送信します。
   * ``LATCH_PIN`` をトグルして、出力ピンにデータをロッチします。

   .. code-block:: arduino

      void shiftOutDigit(byte data) {
        // シフトレジスタにデータを送信
        digitalWrite(LATCH_PIN, LOW);
        shiftOut(DATA_PIN, CLOCK_PIN, MSBFIRST, data);
        digitalWrite(LATCH_PIN, HIGH);
      }
  
**さらなる実験**



* リセットボタンの追加:

  Picoにボタンを接続して、押すことでカウンターをリセットします。

* 異なるデータの表示:

  センサーの読み取り値（温度や光レベルなど）を表示するようにコードを変更します。

* ストップウォッチの作成:

  開始、停止、リセット機能を実装して、ディスプレイをストップウォッチとして使用します。

**結論**

このプロジェクトでは、シフトレジスタとマルチプレクシング技術を使って4桁7セグメントディスプレイを制御する方法を示しました。 ``millis()`` を使用してタイミングを効率的に管理し、ディスプレイのパフォーマンスを損なうことなく、レスポンシブで正確なタイムカウンターを作成しました。
