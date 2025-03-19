.. note::

    こんにちは！FacebookのSunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！ Raspberry Pi、Arduino、ESP32について、他の愛好者と深く学びましょう。

    **参加する理由は？**

    - **専門的なサポート**: 購入後の問題や技術的な課題をコミュニティやチームのサポートで解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換して、スキルを向上させましょう。
    - **限定プレビュー**: 新製品の発表や先行情報をいち早く入手できます。
    - **特別割引**: 最新の製品をお得に購入できる割引を提供します。
    - **特別なプロモーションやプレゼント**: プレゼントや祝日プロモーションに参加できます。

    👉 一緒に探索して創造してみませんか？ [|link_sf_facebook|] をクリックして、今すぐ参加しましょう！

.. _ar_button:

2.5 ボタンの値を読み取る
=============================

このレッスンでは、Raspberry Pi Pico 2 Wを使ってボタンの入力を読み取る方法を学びます。これまで、GPIOピンは主にLEDの点灯などの出力に使用してきました。今回は、ボタンが押されたときにその入力を検出するために、GPIOピンを入力として使用します。これはインタラクティブなプロジェクトを作成するための基本的な技術です。

* :ref:`cpn_button`

**必要なコンポーネント**

このプロジェクトでは、以下のコンポーネントが必要です。

全てが揃ったキットを購入するのはとても便利です。こちらのリンクから購入できます:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前	
        - キット内容
        - 購入リンク
    *   - Pico 2 W スターターキット	
        - 450+
        - |link_pico2w_kit|

また、以下のリンクから個別に購入することもできます。


.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
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
        - 数本
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_resistor`
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_button`
        - 1
        - |link_button_buy|

**回路図**

|sch_button|

ボタンの片側のピンが3.3Vに接続され、もう一方がGP14に接続されていれば、ボタンが押されたときにGP14はHIGHになります。しかし、ボタンが押されていないとき、GP14は浮遊状態になり、HIGHまたはLOWのいずれかになります。ボタンが押されていない時に安定したLOWレベルを得るためには、GP14を10KΩのプルダウン抵抗を通してGNDに接続する必要があります。

* **ボタンが押されていない場合**: GP14ピンは抵抗を通してGNDに接続されているため、 **LOW (0)** として読み取られます。
* **ボタンが押された場合**: GP14ピンはボタンを通して3.3Vに接続され、 **HIGH (1)** として読み取られます。

**配線**

4ピンのボタンはH字型をしています。左右の2つのピンが接続されており、中央の隙間を越えると、同じ行番号を持つ2つの半列を接続します（例えば、私の回路では、E23とF23が接続されており、E25とF25も接続されています）。

ボタンが押されるまでは、左右のピンは互いに独立しており、電流は一方から他方に流れません。

|wiring_button|

**コード**

.. note::

    * ファイル ``2.5_reading_button_value.ino`` を ``pico-2w-kit-main/arduino/2.5_reading_button_value`` のパスで開いてください。
    * または、このコードを **Arduino IDE** にコピーしてください。
    * **アップロード** ボタンをクリックする前に、ボード（Raspberry Pi Pico）と適切なポートを選択するのを忘れないでください。


.. code-block:: Arduino

   const int buttonPin = 14;  // ボタンに接続されているGPIOピン

   void setup() {
     Serial.begin(115200);       // シリアルモニターを115200ボーレートで初期化
     pinMode(buttonPin, INPUT);  // ボタンピンを入力モードに設定
   }

   void loop() {
     int buttonState = digitalRead(buttonPin);  // ボタンの状態を読み取る

     if (buttonState == HIGH) {
       Serial.println("You pressed the button!");
     }
     delay(100);  // ボタンを頻繁に読み取らないための短い遅延
   }


* コードのアップロード後、Arduino IDEの右上隅にある虫眼鏡アイコン（シリアルモニター）をクリックします。
* ``Serial.begin(115200);`` 行と一致するように、ボーレートを115200に設定します。
* ボタンを押すたびに、シリアルモニターに「ボタンが押されました！」と表示されるはずです。

.. image:: ../img/serial_monitor.png

**コードの理解**

#. シリアル通信の初期化:

   115200ボーレートでシリアル通信を開始します。これにより、シリアルモニターにメッセージを表示できます。

   .. code-block:: Arduino

        Serial.begin(115200);

#. ボタンピンの設定:

   ``buttonPin`` （GP14）を入力として設定し、ボタンの状態を読み取る準備をします。

   .. code-block:: Arduino

        pinMode(buttonPin, INPUT);

#. ボタン状態の読み取り:

   ボタンの現在の状態を読み取ります。押されていると ``HIGH`` , 押されていないと ``LOW`` として読み取られます。

   .. code-block:: Arduino

        int buttonState = digitalRead(buttonPin);


#. ボタンが押されたときの反応:

   ボタンが押されている場合、シリアルモニターにメッセージを表示します。

   .. code-block:: Arduino

        if (buttonState == HIGH) {
          Serial.println("You pressed the button!");
        }


**代替案: プルアップ抵抗設定**

ボタンをプルアップ抵抗で配線することもできます。この設定では:

* **ボタンが押されていない場合**: プルアップ抵抗により、GP14はHIGH（1）として読み取られます。
* **ボタンが押された場合**: ボタンが押されると、GP14はGNDに接続され、LOW（0）として読み取られます。

* 配線方法:

  * 10KΩ抵抗をGP14と3.3Vに接続します。
  * ボタンの一方の端をGP14に接続します。
  * もう一方の端をGNDに接続します。

* コードの変更:

  ``if`` 文の条件を変更します:

  .. code-block:: Arduino

        if (buttonState == LOW) {
          Serial.println("You pressed the button!");
        }

**内部プルアップ抵抗の使用**

Raspberry Pi Pico 2では、内部プルアップ抵抗を有効にすることができ、外部抵抗を省略できます。

内部抵抗を使用することで、配線が簡単になり、ブレッドボード上の追加の外部抵抗が不要になります。

* **ボタンが押されていない場合**: 内部プルアップ抵抗により、GP14はHIGH（1）として読み取られます。
* **ボタンが押された場合**: ボタンが押されると、GP14はGNDに接続され、LOW（0）として読み取られます。

* 配線方法:

  * 10KΩ抵抗を取り外します。

* コードの変更:

  * ボタンピンを内部プルアップ抵抗を持つ入力として設定します。
  * ``if`` 文の条件を変更します。

  .. code-block:: Arduino

     const int buttonPin = 14;  // ボタンに接続されているGPIOピン
  
     void setup() {
       Serial.begin(115200);       // シリアルモニターを115200ボーレートで初期化
       pinMode(buttonPin, INPUT_PULLUP);  // ボタンピンを内部プルアップ抵抗を持つ入力として設定
     }
  
     void loop() {
       int buttonState = digitalRead(buttonPin);  // ボタンの状態を読み取る
  
       if (buttonState == LOW) {
         Serial.println("You pressed the button!");
       }
       delay(100);  // ボタンを頻繁に読み取らないための短い遅延
     }


**結論**

このレッスンでは、Raspberry Pi Picoを使ってボタンからの入力を読み取る方法を学びました。この基本的な技術を使うことで、ユーザーの入力に反応するインタラクティブなプロジェクトを作成できるようになります。

**さらなる探求**

* **LEDの制御**: ボタンが押されたときにLEDを点灯させるようにコードを変更します。
* **デバウンス処理**: より信頼性の高い入力を得るために、ボタンのチャタリングを処理するコードを実装します。
* **複数のボタン**: 複数のボタンからの入力を読み取って、異なる動作を実行してみましょう。
