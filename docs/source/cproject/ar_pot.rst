.. note::

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Raspberry Pi、Arduino、ESP32について、同じ興味を持つ仲間と一緒にさらに深く学びましょう。

    **参加する理由は？**

    - **専門家によるサポート**: 販売後の問題や技術的な課題をコミュニティやチームの助けで解決します。
    - **学びと共有**: スキル向上のためのヒントやチュートリアルを交換します。
    - **独占的なプレビュー**: 新製品の発表や先行プレビューに早期アクセスできます。
    - **特別割引**: 最新製品を特別価格で購入できます。
    - **祝祭プロモーションとプレゼント**: ギフトやホリデープロモーションに参加できます。

    👉 一緒に探索して創造しませんか？[|link_sf_facebook|]をクリックして今すぐ参加！

.. _ar_pot:

2.11 ノブを回す
==========================

このレッスンでは、Raspberry Pi Pico 2 Wの内蔵アナログ-デジタル変換器（ADC）を使用してアナログ入力を読み取り、その入力を使ってLEDの明るさを制御する方法を学びます。具体的には、可変抵抗器であるポテンショメーターをアナログ入力デバイスとして使用します。ポテンショメーターのノブを回すことで、Picoが読み取る電圧レベルが調整され、その後、パルス幅変調（PWM）を使用してLEDの明るさを制御します。


**アナログ入力の理解**

これまで、デジタル入力および出力を使用してきましたが、これはON（高電圧）またはOFF（低電圧）のいずれかです。しかし、多くの実際の信号はアナログであり、値の範囲内で連続的に変化することができます。例えば、光の強度、温度、音のレベルなどが挙げられます。

Raspberry Pi Pico 2 Wには内蔵ADCがあり、これを使ってアナログ電圧を読み取り、コードで処理可能なデジタル値に変換できます。

ADCは、ポテンショメーターからのアナログ電圧を次の式を使ってデジタル値に変換します：

.. code-block::

  Digital Value = (Analog Voltage/3.3V) * 1023

**PicoのADCピン**

|pin_adc|

Picoにはアナログ入力に使用できる3つのGPIOピンがあります：

* **GP26** （ADC0）
* **GP27** （ADC1）
* **GP28** （ADC2）

さらに、内部で温度センサーに接続された4番目のADCチャンネル（ADC4）があります。このセンサーについては後のレッスンで扱います。

**必要なコンポーネント**

このプロジェクトに必要なコンポーネントは以下の通りです。

キットをまとめて購入するのが便利です。こちらがリンクです：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前	
        - このキットのアイテム
        - 購入リンク
    *   - Pico 2 W スターターキット	
        - 450+
        - |link_pico2w_kit|


これらのコンポーネントは、下記のリンクから個別に購入することもできます。

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
        - 1(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 7
        - :ref:`cpn_potentiometer`
        - 1
        - |link_potentiometer_buy|

**回路図**

|sch_pot|

**配線**

|wiring_pot|

**コード**

.. note::

    * ``2.11_turn_the_knob.ino`` ファイルを ``pico-2w-kit-main/arduino/2.11_turn_the_knob`` パスで開くことができます。
    * または、このコードを **Arduino IDE** にコピーします。
    * **Upload** ボタンをクリックする前に、ボード（Raspberry Pi Pico）と正しいポートを選択するのを忘れないでください。

.. code-block:: Arduino

   // ピンを定義
   const int potPin = 28;   // ポテンショメーターはGP28（ADC2）に接続
   const int ledPin = 15;   // LEDはGP15（PWM対応）に接続

   void setup() {
     // デバッグ用にシリアル通信を初期化
     Serial.begin(115200);
     // LEDピンを出力として設定
     pinMode(ledPin, OUTPUT);
   }

   void loop() {
     // ポテンショメーターからアナログ値を読み取る（0-1023）
     int sensorValue = analogRead(potPin);
     // デバッグ用にセンサー値をシリアルモニターに表示
     Serial.println(sensorValue);

     // センサー値をPWM値にマッピング（0-255）
     int brightness = map(sensorValue, 0, 1023, 0, 255);
     // LEDの明るさを設定
     analogWrite(ledPin, brightness);

     // 安定性のために少し遅延
     delay(10);
   }

コードが実行中でシリアルモニターが開いているとき：

* ポテンショメーターのノブを回すと、LEDの明るさが滑らかに暗くから明るく変化するはずです。
* ポテンショメーターを調整すると、アナログ値が約0から1023の範囲で表示されるはずです。

**コードの理解**

#. ピンの定義：

   ポテンショメーターとLEDに使用するGPIOピンを設定します。

   .. code-block:: Arduino

        const int potPin = 28;   // ポテンショメーターはGP28（ADC2）に接続
        const int ledPin = 15;   // LEDはGP15（PWM対応）に接続

#. シリアル通信の初期化：

   シリアル通信を開始し、シリアルモニターにメッセージを表示できるようにします。

   .. code-block:: Arduino

        Serial.begin(115200);

#. アナログ値の読み取り：

   potPin（GP28）のアナログ電圧を読み取り、0から1023の範囲で値を返します。

   .. code-block:: Arduino

        int sensorValue = analogRead(potPin);

#. センサー値の表示：

   現在のセンサー値をシリアルモニターに表示してデバッグします。

   .. code-block:: Arduino

        Serial.println(sensorValue);

#. センサー値のマッピング：

   センサー値（0-1023）をPWM出力に適した明るさ値（0-255）に変換します。

   .. code-block:: Arduino

        int brightness = map(sensorValue, 0, 1023, 0, 255);

#. LEDの明るさ設定：

   ledPin（GP15）のPWMデューティサイクルを設定することで、LEDの明るさを調整します。

   .. code-block:: Arduino

        analogWrite(ledPin, brightness);

#. 小さな遅延の追加：

   読み取りを安定させ、ループが速すぎないようにするための短い遅延です。

   .. code-block:: Arduino

        delay(10);

**さらなる探求**

* **電圧の表示**：コードを変更して、ポテンショメーターから読み取った実際の電圧を計算して表示します。

  .. code-block:: Arduino

        // ピンを定義
        const int potPin = 28;  // ポテンショメーターはGP28（ADC2）に接続
        const int ledPin = 15;  // LEDはGP15（PWM対応）に接続
        
        void setup() {
          // デバッグ用にシリアル通信を初期化
          Serial.begin(115200);
          // LEDピンを出力として設定
          pinMode(ledPin, OUTPUT);
        }
        
        void loop() {
          // ポテンショメーターからアナログ値を読み取る（0-1023）
          int sensorValue = analogRead(potPin);
        
          // デバッグ用にセンサー値をシリアルモニターに表示
          Serial.println(sensorValue);
        
          // 実際の電圧を計算して表示
          float voltage = sensorValue * (3.3 / 1023.0);
          Serial.print("Voltage: ");
          Serial.print(voltage);
          Serial.println(" V");
        
          // センサー値をPWM値にマッピング（0-255）
          int brightness = map(sensorValue, 0, 1023, 0, 255);
          // LEDの明るさを設定
          analogWrite(ledPin, brightness);
        
          // 安定性のために少し遅延
          delay(10);
        }

* **複数のLEDを制御**：複数のポテンショメーターを使用して、異なるLEDやRGB LEDの色を制御します。
* **他のセンサーとの組み合わせ**：ポテンショメーターを他のアナログセンサー（例えば光依存抵抗器（LDR））に置き換えて、周囲の光に応じてLEDを制御します。

**概念の説明**

* アナログ-デジタル変換（ADC）：

  * PicoのADCは、ポテンショメーターからのアナログ電圧をデジタル値に変換します。
  * 0Vから3.3Vの電圧範囲を0から1023の数値に変換します。

* パルス幅変調（PWM）：

  * PWMは、デジタルピンを高速でHIGHとLOWの状態で切り替えることによってアナログ電圧をシミュレートする技術です。
  * 信号がHIGHの時間の割合（デューティサイクル）を調整することで、LEDやモーターなどのデバイスを制御できます。

* 値のマッピング：

  * ``map()`` 関数は、値の範囲を別の範囲にスケーリングします。
  * この場合、ポテンショメーターの0-1023の範囲をPWMの0-255の範囲にマッピングします。

**まとめ**

このレッスンでは、Raspberry Pi PicoのADCを使用してポテンショメーターからアナログ入力を読み取り、その入力を使用してPWMを介してLEDの明るさを制御する方法を学びました。この基本的な技術により、さまざまなアナログセンサーとインターフェースし、出力を比例的に制御できるようになります。
