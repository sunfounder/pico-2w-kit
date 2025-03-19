.. note::

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Raspberry Pi、Arduino、ESP32について、同じ趣味を持つ仲間と一緒にさらに深く学びましょう。

    **参加する理由は？**

    - **専門家によるサポート**: 販売後の問題や技術的な課題をコミュニティやチームの助けで解決します。
    - **学びと共有**: スキルを高めるためのヒントやチュートリアルを交換します。
    - **独占的なプレビュー**: 新製品の発表や先行プレビューを早期に手に入れることができます。
    - **特別割引**: 最新製品を特別価格で手に入れることができます。
    - **祝祭プロモーションとプレゼント**: ギフトやホリデープロモーションに参加できます。

    👉 一緒に探索して創造しませんか？[|link_sf_facebook|]をクリックして今すぐ参加！

.. _ar_photoresistor:


2.12 光を感じる
=====================

このレッスンでは、 **フォトレジスター** （または光依存抵抗器、LDR）を使用して、Raspberry Pi Pico 2 Wで光の強さを測定する方法を学びます。フォトレジスターは受け取る光の量に応じて抵抗値が変化します。光が明るいほど抵抗は低くなります。この特性により、周囲の光の変化を検出するのに最適です。

* :ref:`cpn_photoresistor`

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
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_photoresistor`
        - 1
        - |link_photoresistor_buy|

**回路図**

|sch_photoresistor|

この回路では、10KΩの抵抗とフォトレジスターが直列に接続され、電圧分割器を形成します。GP28はフォトレジスターを通る電圧を読み取り、10KΩの抵抗が電流を制限して保護します。

* **明るい光**: フォトレジスターの抵抗が低下し、電圧が下がり、GP28の読み値も下がります。強い光では、抵抗がゼロに近づき、GP28の読み値は0に近くなります。この時、10KΩの抵抗が保護役割を果たし、3.3VとGNDが直結されないようになり、ショート回路を防ぎます。
* **暗闇**: フォトレジスターの抵抗が増加し、電圧が上昇し、GP28の読み値も上がります。完全な暗闇では、抵抗はほぼ無限大になり（10KΩの抵抗は無視できる）、GP28の読み値は1023に近づきます。

計算式は以下の通りです。

.. code-block::

  Digital Value = (Analog Voltage/3.3V) * 1023




**配線**


|wiring_photoresistor|


**コードの記述**


.. code-block:: Arduino

   const int sensorPin = 28;   // フォトレジスターはGP28（ADC2）に接続

   void setup() {
     Serial.begin(115200);    // シリアルモニターの初期化
   }

   void loop() {
     // フォトレジスターからアナログ値を読み取る
     int sensorValue = analogRead(sensorPin);
     // センサーの値をシリアルモニターに表示
     Serial.println(sensorValue);
     delay(500);  // 500ミリ秒待機してから再度読み取る
   }

コードが実行され、シリアルモニターが開いているとき：

* センサー値の観察：

  フォトレジスターからのアナログ値を表す数値のストリームが表示されます。

* フォトレジスターとのインタラクション：

  * フォトレジスターに懐中電灯やランプを当ててみましょう。センサーの値が減少するはずです（光が強いと抵抗が減少するため）。
  * フォトレジスターを手で覆うか、暗い場所に置いてみましょう。センサーの値が増加するはずです（光が少ないと抵抗が増加するため）。

**コードの理解**

#. センサーピンの定義：

   センサーピンをGPIO 28に設定します。このピンはアナログ入力に接続されています。

   .. code-block:: arduino

        const int sensorPin = 28;   // フォトレジスターはGP28（ADC2）に接続

#. シリアル通信の初期化：

   シリアル通信を開始し、シリアルモニターにメッセージを表示できるようにします。

   .. code-block:: arduino

        Serial.begin(115200);

#. アナログ値の読み取り：

   sensorPinでアナログ電圧を読み取り、0から1023の間の値を返します。

   .. code-block:: arduino

        int sensorValue = analogRead(sensorPin);

#. センサー値の表示：

   センサー値をシリアルモニターに出力します。

   .. code-block:: arduino

        Serial.println(sensorValue);

#. 遅延の追加：

   次の読み取りの前に500ミリ秒待機します。

   .. code-block:: arduino

        delay(500);

**電圧への変換**

実際の電圧値を表示したい場合は、コードを次のように変更できます。

.. code-block:: arduino

   const int sensorPin = 28;   // フォトレジスターはGP28（ADC2）に接続

   void setup() {
     Serial.begin(115200);    // シリアルモニターの初期化
   }

    void loop() {
      int sensorValue = analogRead(sensorPin);
      // アナログ読み取り値を電圧に変換
      float voltage = sensorValue * (3.3 / 1023.0);
      Serial.print("Sensor Value: ");
      Serial.print(sensorValue);
      Serial.print("  Voltage: ");
      Serial.print(voltage);
      Serial.println(" V");
      delay(500);
    }

**さらなる探求**

* 光に応じてLEDを制御：

  フォトレジスターを使用して、LEDの明るさを制御したり、光の強さに応じてオン/オフを切り替えます。

* データロギング：

  時間をかけて光の強度を記録し、環境の変化を監視します。

* ナイトライトの作成：

  暗くなると自動的に点灯するライトを作成します。

**まとめ**

このレッスンでは、Raspberry Pi Picoを使用してフォトレジスターで光の強度を測定する方法を学びました。電圧分割回路からアナログ電圧を読み取ることで、光の変化を検出し、その情報をプロジェクトで活用できます。
