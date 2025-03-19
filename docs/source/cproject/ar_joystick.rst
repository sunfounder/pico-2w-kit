.. note::

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Raspberry Pi、Arduino、ESP32に関する情報を他の愛好者と共に深く学びましょう。

    **なぜ参加するのか？**

    - **専門家のサポート**: 購入後の問題や技術的な課題をコミュニティやチームの助けを借りて解決できます。
    - **学びと共有**: スキルを高めるためのヒントやチュートリアルを交換できます。
    - **限定プレビュー**: 新製品の発表や先行公開をいち早くチェックできます。
    - **特別割引**: 新製品に対する独占的な割引を楽しめます。
    - **季節的なプロモーションとプレゼント**: プレゼントやホリデーセールに参加できます。

    👉 一緒に探求し、創造してみませんか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _ar_joystick:

4.1 ジョイスティックからの値の読み取り
======================================

このレッスンでは、 **ジョイスティック** を使用して、Raspberry Pi Pico 2 Wでアナログ値を読み取ったり、ボタンの押下を検出する方法を学びます。ジョイスティックは、2軸（X軸とY軸）で移動を制御できる一般的な入力デバイスで、押すとボタンが作動することが多いです（Z軸）。

* :ref:`cpn_joystick`

**必要な部品**

このプロジェクトでは、以下の部品が必要です。

全体キットを購入するのが便利です。リンクはこちらです：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前
        - キット内のアイテム
        - 購入リンク
    *   - Pico 2 W スターターキット
        - 450+
        - |link_pico2w_kit|

以下のリンクから、部品を個別に購入することもできます。

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - 部品の紹介
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
        - 複数
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_resistor`
        - 1（10KΩ）
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_joystick`
        - 1
        - 

**ジョイスティックの理解**

典型的なジョイスティックモジュールは、直角に配置された2つのポテンショメータで構成されています：

* **X軸ポテンショメータ**: 左右の動きを測定します。
* **Y軸ポテンショメータ**: 上下の動きを測定します。
* **Z軸（スイッチ）**: ジョイスティックを押し下げたときに作動するデジタルボタンです。

X軸とY軸からアナログ値を読み取ることで、ジョイスティックの位置を判別できます。Z軸のボタンを押すことで、ジョイスティックが押されたことを検出できます。

**回路図**

|sch_joystick|

SWピンは10Kのプルアップ抵抗に接続されています。これは、ジョイスティックが押されていないときにSWピン（Z軸）で安定した高レベルを得るためです。そうでない場合、SWはサスペンド状態になり、出力値が0または1の間で変動する可能性があります。

**配線**

|wiring_joystick|

**コードの記述**

.. note::

    * 「 ``4.1_toggle_the_joyostick.ino`` 」ファイルを「 ``pico-2w-kit-main/arduino/4.1_toggle_the_joyostick`` 」パス内で開きます。
    * または、このコードを **Arduino IDE** にコピーします。
    * アップロードボタンをクリックする前に、ボード（Raspberry Pi Pico）と正しいポートを選択するのを忘れないでください。

.. code-block:: arduino

   // ピンの定義
   const int joystickX = 26;  // GP26 (ADC0) - VRxに接続
   const int joystickY = 27;  // GP27 (ADC1) - VRyに接続
   const int joystickSW = 22; // GP22 - SW（ボタン）に接続

   void setup() {
     // シリアル通信を115200ボーレートで初期化
     Serial.begin(115200);

     // ジョイスティックスイッチピンを入力モードに設定
     pinMode(joystickSW, INPUT_PULLUP);

   }

   void loop() {
     // ジョイスティックからアナログ値を読み取る
     int xValue = analogRead(joystickX);
     int yValue = analogRead(joystickY);

     // ジョイスティックボタンの状態を読み取る
     int buttonState = digitalRead(joystickSW);

     // シリアルモニターにジョイスティックの値を出力
     Serial.print("X: ");
     Serial.print(xValue);
     Serial.print(" | Y: ");
     Serial.print(yValue);
     Serial.print(" | Button: ");
     Serial.println(buttonState == LOW ? "Pressed" : "Released");

     delay(500); // 次の読み取り前に0.5秒待つ
   }

コードを実行し、シリアルモニターが開いているとき：

* ジョイスティックを異なる方向（左、右、上、下）に動かして、X軸とY軸の値がそれに応じて変化する様子を観察します。
* ジョイスティックボタン（Z軸）を押して、ボタンの状態が「Released」から「Pressed」に変わるのを観察します。

**コードの理解**

#. ピンの定義：

   * ``joystickX`` と ``joystickY`` : ジョイスティックのX軸とY軸に接続されたアナログピン。
   * ``joystickSW``: ジョイスティックのボタン（Z軸）に接続されたデジタルピン。

#. setup() 関数：

   * デバッグとモニタリングのためにシリアル通信を初期化します。
   * ジョイスティックのボタンピンを内部プルアップ抵抗を使って入力モードに設定します。

   .. code-block:: arduino

        void setup() {
          Serial.begin(115200); // シリアル通信を115200ボーレートで初期化
          pinMode(joystickSW, INPUT_PULLUP); // ジョイスティックボタンをプルアップ抵抗付きで入力に設定
        }

#. ``loop()`` 関数：

   * アナログ値の読み取り：

     ジョイスティックのX軸とY軸の現在の位置を読み取ります。値は0から1023の範囲で、アナログ電圧レベルに対応しています。

     .. code-block:: arduino

           int xValue = analogRead(joystickX);
           int yValue = analogRead(joystickY);

   * ボタン状態の読み取り：

     ジョイスティックのボタンの状態を読み取ります。 ``LOW`` は押された状態、 ``HIGH`` は解放された状態を示します。

     .. code-block:: arduino

           int buttonState = digitalRead(joystickSW);

   * シリアルモニターへの出力：

     ジョイスティックの現在の位置とボタン状態をシリアルモニターに出力し、デバッグとモニタリングを行います。

     .. code-block:: arduino

       Serial.print("X: ");
       Serial.print(xValue);
       Serial.print(" | Y: ");
       Serial.print(yValue);
       Serial.print(" | Button: ");
       Serial.println(buttonState == LOW ? "Pressed" : "Released");

**さらなる探索**

* アナログ値をアクションにマッピング：

  * ジョイスティックの位置を使用して、サーボモーター、LED、または他のアクチュエータを移動方向や大きさに基づいて制御します。

* デッドゾーンの実装：

  * 中央位置周辺にデッドゾーンを実装して、ジョイスティックのわずかな揺れによる意図しない動きを防ぎます。

* 他のセンサーとの組み合わせ：

  * ジョイスティックを他のセンサー（例えば、加速度センサー、距離センサー）と統合して、より複雑なインタラクションを作成します。

* ゲームコントローラーの作成：

  * 複数のジョイスティックとボタンを使用して、簡単なゲームやロボット制御用のカスタムゲームコントローラーを作成します。

**結論**

このレッスンでは、Raspberry Pi Picoとジョイスティックをインターフェースし、X軸とY軸からアナログ値を読み取り、Z軸のボタン押下を検出する方法を学びました。このセットアップは、リモートコントロール、ロボット工学、インタラクティブなインストールなど、さまざまなプロジェクトの入力方法として使用できます。ジョイスティックの値を読み取って解釈する方法を理解することで、反応的で動的なアプリケーションを作成できます。
