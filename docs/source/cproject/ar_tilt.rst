.. note:: 

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！ Raspberry Pi、Arduino、ESP32について、仲間たちと一緒にさらに深く学びましょう。

    **なぜ参加するべきか？**

    - **専門的なサポート**：コミュニティやチームの助けを借りて、購入後の問題や技術的な課題を解決します。
    - **学び＆共有**：スキルを向上させるためのヒントやチュートリアルを交換しましょう。
    - **限定プレビュー**：新製品の発表や先行情報をいち早く入手できます。
    - **特別割引**：最新の製品に対する専用の割引を楽しめます。
    - **季節限定プロモーションやプレゼント**：プレゼント企画やホリデープロモーションに参加しましょう。

    👉 一緒に探求し、創造してみませんか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _ar_tilt:

2.6 傾けてみよう！
=======================

このレッスンでは、Raspberry Pi Pico 2 Wを使用して、傾斜スイッチを使って向きの変化を検出する方法を学びます。傾斜スイッチは、直立しているか傾いているかを感知できるシンプルなデバイスで、モーション検出や向き検出、または位置に基づくトリガーとして役立ちます。


**必要なコンポーネント**

このプロジェクトに必要なコンポーネントは以下の通りです。

セットで購入すると便利です。こちらのリンクから購入できます：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前	
        - このキットに含まれているアイテム
        - 購入リンク
    *   - Pico 2 Wスターターキット	
        - 450+
        - |link_pico2w_kit|

以下のリンクから個別に購入することもできます。

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
        - :ref:`cpn_resistor`
        - 1（10KΩ）
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_tilt`
        - 1
        - 

**回路図**

|sch_tilt|

* **直立時（スイッチが閉じている場合）**：

  * 傾斜スイッチは **3.3V** を直接 **GP14** に接続します。
  * GPIOピンは **HIGH** （1）を読み取ります。

* **傾いた時（スイッチが開いている場合）**：

  * 傾斜スイッチは **3.3V** を **GP14** から切り離します。
  * プルダウン抵抗が **GP14** を **GND** に引き下げます。
  * GPIOピンは **LOW** （0）を読み取ります。

**配線**

|wiring_tilt|

**コードの記述**

.. note::

    * ``2.6_tilt_it.ino`` ファイルは ``pico-2w-kit-main/arduino/2.4_colorful_light`` パスにあります。
    * あるいは、このコードを **Arduino IDE** にコピーしてください。
    * **アップロード** ボタンをクリックする前に、ボード（Raspberry Pi Pico）と適切なポートを選択することを忘れないでください。

.. code-block:: Arduino

   const int tiltPin = 14;  // 傾斜スイッチが接続されたGPIOピン

   void setup() {
     Serial.begin(115200);       // シリアルモニターを115200ボーレートで初期化
     pinMode(tiltPin, INPUT);    // 傾斜ピンを入力として設定
   }

   void loop() {
     int tiltState = digitalRead(tiltPin);  // 傾斜スイッチの状態を読み取る

     if (tiltState == HIGH) {
       Serial.println("The switch works!");
     }
     delay(100);  // シリアルモニターが洪水状態にならないように小さな遅延
   }

コードが実行され、シリアルモニターが開いている状態で、ブレッドボードまたは傾斜スイッチを傾けてみましょう。
スイッチを直立位置に戻すたびに、「スイッチが機能しています！」というメッセージがシリアルモニターに表示されるはずです。

**コードの理解**

#. シリアル通信の初期化：

   115200のボーレートでシリアル通信を開始します。これにより、シリアルモニターにメッセージを表示できるようになります。

   .. code-block:: Arduino

        Serial.begin(115200);

#. 傾斜ピンの設定：

   ``tiltPin`` （GP14）を入力として設定し、傾斜スイッチの状態を読み取ります。

   .. code-block:: Arduino

        pinMode(tiltPin, INPUT);


#. 傾斜スイッチの状態を読み取る：

   傾斜スイッチの現在の状態を読み取ります。直立していれば ``HIGH`` 、傾いていれば ``LOW`` です。

   .. code-block:: Arduino

        int tiltState = digitalRead(tiltPin);

#. 傾斜に反応する：

   傾斜スイッチが直立している場合（閉じている場合）、シリアルモニターにメッセージを表示します。

   .. code-block:: Arduino

        if (tiltState == HIGH) {
          Serial.println("The switch works!");
        }

**さらに実験してみよう**

* **LEDの制御**：傾斜スイッチが直立している時にLEDを点灯させ、傾いた時に消灯させるようにコードを変更してみましょう。

  .. code-block:: Arduino

        const int tiltPin = 14;   // 傾斜スイッチが接続されたGPIOピン
        const int ledPin = 15;    // LEDが接続されたGPIOピン

        void setup() {
          Serial.begin(115200);
          pinMode(tiltPin, INPUT);
          pinMode(ledPin, OUTPUT);
        }

        void loop() {
          int tiltState = digitalRead(tiltPin);

          if (tiltState == HIGH) {
            Serial.println("The switch works!");
            digitalWrite(ledPin, HIGH);  // LEDを点灯
          } else {
            digitalWrite(ledPin, LOW);   // LEDを消灯
          }
          delay(100);
        }

* **感度の調整**：いくつかの傾斜スイッチには異なる感度レベルがあります。傾斜角度を調整して、スイッチが作動する角度を確認してみましょう。

**結論**

このレッスンでは、Raspberry Pi Picoを使って傾斜スイッチで向きの変化を検出する方法を学びました。この基本的なスキルを使えば、モーション検出や位置に基づいた反応（アラーム、オートメーション、インタラクティブデバイスなど）のプロジェクトを作成することができます。
