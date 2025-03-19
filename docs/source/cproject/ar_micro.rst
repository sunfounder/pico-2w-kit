.. note::

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Raspberry Pi、Arduino、ESP32について、他の愛好者とともにさらに深く学びましょう。

    **なぜ参加するのか？**

    - **専門家のサポート**: コミュニティやチームのサポートを受けて、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**: スキルを向上させるためのヒントやチュートリアルを交換できます。
    - **独占的なプレビュー**: 新製品の発表や先取り情報をいち早くチェックできます。
    - **特別割引**: 最新製品に対する独占的な割引を楽しめます。
    - **祭事プロモーションとプレゼント**: ギブアウェイや休日のプロモーションに参加できます。

    👉 一緒に探求し、創造しませんか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _ar_micro:

2.8 - やさしく押して
==========================

|img_micro_switch|

このレッスンでは、 **マイクロスイッチ** （またはリミットスイッチ）をRaspberry Pi Pico 2 Wで使用して、スイッチが押されたり放されたりしたときに検出する方法を学びます。マイクロスイッチは、電子レンジのドア、プリンターのカバー、3Dプリンターのエンドストップなどのデバイスで一般的に使用されており、信頼性が高く、頻繁な作動にも耐えることができます。

* :ref:`cpn_micro_switch`

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
        - :ref:`cpn_resistor`
        - 1（10KΩ）
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_capacitor`
        - 1（104）
        - |link_capacitor_buy|
    *   - 7
        - :ref:`cpn_micro_switch`
        - 1
        - 

**マイクロスイッチの理解**

マイクロスイッチは通常、3つのピンを持っています：

|img_micro_switch|

- **共通（C）**: 中央のピン。
- **通常開（NO）**: スイッチが **押されたとき** に共通ピンに接続されます。
- **通常閉（NC）**: スイッチが **押されていないとき** に共通ピンに接続されます。

スイッチを適切に接続することで、GPIOピンの電圧レベルを読み取ることで、スイッチが押されたか放されたかを検出できます。

**回路図**

|sch_limit_sw|

デフォルトでは、GP14はLOWで、押されるとGP14はHIGHになります。

10KΩ抵抗の目的は、スイッチが押されている間、GP14をLOWのままに保つことです。

機械的スイッチを押すと、接点がバウンスする可能性があり、開閉状態が素早く何度も変化することがあります。GP14とGNDの間に接続されたコンデンサは、このノイズをフィルタリングするのに役立ちます。

* **スイッチが押されていない場合**：

  * **共通（C）** ピンは **NC** ピンに接続され、 **GND** に接続されています。
  * **GP14** は **LOW** （0V）を読み取ります。

* **スイッチが押された場合**：

  * **共通（C）** ピンは **NO** ピンに接続され、 **3.3V** に接続されています。
  * **GP14** は **HIGH** （3.3V）を読み取ります。

**配線**

|wiring_limit_sw|


**コードの記述**

マイクロスイッチが押されたときに、それを検出してシリアルモニターにメッセージを表示する簡単なプログラムを作成します。

.. note::

    * 「 ``2.8_press_gently.ino`` 」ファイルを「 ``pico-2w-kit-main/arduino/2.8_press_gently`` 」のパスで開きます。
    * または、このコードを **Arduino IDE** にコピーしてください。
    * アップロードボタンをクリックする前に、Raspberry Pi Picoボードと正しいポートを選択してください。

.. code-block:: Arduino

   const int switchPin = 14;   // マイクロスイッチに接続されたGPIOピン
   int switchState = 0;

   void setup() {
     Serial.begin(115200);       // シリアルモニターを115200ボーレートで初期化
     pinMode(switchPin, INPUT);  // スイッチピンを入力として設定
   }

   void loop() {
     switchState = digitalRead(switchPin);  // スイッチの状態を読み取る

     if (switchState == HIGH) {
       Serial.println("The switch is pressed!");
     } else {
       Serial.println("The switch is not pressed.");
     }
     delay(200);  // シリアルモニターが洪水のように表示されないように小さな遅延を入れる
   }

コードが実行され、シリアルモニターが開いているときに、マイクロスイッチを押したり放したりしてください。
スイッチを押すとシリアルモニターに「スイッチが押されました！」と表示され、放すと「スイッチは押されていません。」と表示されます。

**コードの理解**

#. シリアル通信の初期化：

   シリアル通信を115200ボーレートで開始します。これにより、シリアルモニターにメッセージを表示できるようになります。

   .. code-block:: Arduino

        Serial.begin(115200);

#. スイッチピンの設定：

   switchPin（GP14）を入力として設定し、スイッチの状態を読み取れるようにします。

   .. code-block:: Arduino

        pinMode(switchPin, INPUT);

#. スイッチの状態の読み取り：

   スイッチの現在の状態を読み取ります。スイッチが押されたときはHIGH、押されていないときはLOWになります。

   .. code-block:: Arduino

        switchState = digitalRead(switchPin);

#. スイッチ押下への反応：

   スイッチが押されているかどうかに基づいてメッセージを表示します。

   .. code-block:: Arduino

        if (switchState == HIGH) {
          Serial.println("The switch is pressed!");
        } else {
          Serial.println("The switch is not pressed.");
        }

**代替案：内部プルアップ抵抗の使用**

回路を簡素化し、部品数を減らしたい場合は、Picoの内部プルアップ抵抗を使用できます。

* スイッチが押されているとき、GP14はGNDに接続され、LOW（0）を読み取ります。
* スイッチが押されていないとき、内部プルアップ抵抗によりGP14はHIGHを読み取ります。

* 回路の変更：

  外部10KΩ抵抗とコンデンサを取り外します。

* マイクロスイッチの接続：

  * **共通（C）端子**：GP14に接続します。
  * **通常開（NO）端子**：PicoのGNDに接続します。
  * **通常閉（NC）端子**：接続しません。

* コードの変更：

  .. code-block:: Arduino

        const int switchPin = 14;   // マイクロスイッチに接続されたGPIOピン
        int switchState = 0;

        void setup() {
          Serial.begin(115200);          // シリアルモニターを115200ボーレートで初期化
          pinMode(switchPin, INPUT_PULLUP);  // 内部プルアップ抵抗を有効にする
        }

        void loop() {
          switchState = digitalRead(switchPin);  // スイッチの状態を読み取る

          if (switchState == LOW) {
            Serial.println("The switch is pressed!");
          } else {
            Serial.println("The switch is not pressed.");
          }
          delay(200);  // シリアルモニターが洪水のように表示されないように小さな遅延を入れる
        }

**スイッチのデバウンス**

機械的スイッチは、接点がバウンスすることでノイズを発生させることがあります。読み取りの信頼性を向上させるために、ソフトウェアデバウンスを実装することができます。


.. code-block:: Arduino

    const int switchPin = 14;   // マイクロスイッチに接続されたGPIOピン
    int switchState = 0;        // スイッチの現在の状態
    int lastSwitchState = HIGH; // スイッチの前の状態
    unsigned long lastDebounceTime = 0;  // 最後の状態変更の時間
    unsigned long debounceDelay = 50;    // デバウンス時間（ミリ秒）

    void setup() {
      Serial.begin(115200);
      pinMode(switchPin, INPUT_PULLUP);
    }

    void loop() {
      int reading = digitalRead(switchPin);

      if (reading != lastSwitchState) {
        lastDebounceTime = millis();
      }

      if ((millis() - lastDebounceTime) > debounceDelay) {
        if (reading != switchState) {
          switchState = reading;

          if (switchState == LOW) {
            Serial.println("The switch is pressed!");
          } else {
            Serial.println("The switch is not pressed.");
          }
        }
      }

      lastSwitchState = reading;
    }

* 読み取りが前回の状態と異なるかどうかを確認します。
* 異なっていれば、 ``lastDebounceTime`` をリセットします。
* 読み取りがデバウンス遅延時間を過ぎて安定した場合、新しい状態が有効として認識されます。

**結論**

このレッスンでは、Raspberry Pi Picoを使用してマイクロスイッチが押されたり放されたりするのを検出する方法を学びました。また、回路にプルダウン抵抗を実装して信頼性のある読み取りを確保する方法や、内部プルアップ抵抗を使って回路を簡素化する方法についても学びました。さらに、機械的スイッチノイズに対処するためのデバウンスについても学びました。

**さらに探索する**

* **LEDを制御する**: スイッチが押されたときにLEDを点灯させるようにコードを変更します。
* **複数のスイッチ**: 複数のマイクロスイッチを追加して異なる入力を検出してみましょう。
* **カウンターを作成する**: スイッチが押された回数をカウントして表示するプログラムを作成します。
