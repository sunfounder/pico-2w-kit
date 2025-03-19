.. note::

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Raspberry Pi、Arduino、ESP32について、他の愛好者とともにさらに深く学びましょう。

    **なぜ参加するのか？**

    - **専門家のサポート**: コミュニティやチームのサポートを受けて、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**: スキルを向上させるためのヒントやチュートリアルを交換できます。
    - **独占的なプレビュー**: 新製品の発表や先取り情報をいち早くチェックできます。
    - **特別割引**: 最新製品に対する独占的な割引を楽しめます。
    - **祭事プロモーションとプレゼント**: ギブアウェイや休日のプロモーションに参加できます。

    👉 一緒に探求し、創造しませんか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _ar_led:



2.1 - こんにちは、LED！
=======================================

Raspberry Pi Pico 2 Wを使った最初のハードウェアプロジェクトへようこそ！このレッスンでは、MicroPythonを使ってLEDを点滅させる方法を学びます。このシンプルなプロジェクトは、物理コンピューティングの始め方を学ぶ素晴らしい方法であり、コードでハードウェアを制御する方法を理解する手助けとなります。
* :ref:`cpn_led`

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
        - 1（220Ω）
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|

**回路図**

|sch_led|

GPIOピンを高または低に設定することで、そのピンの出力電圧を制御しています。ピンが高の場合、LEDを通って電流が流れ（抵抗で制限されます）、LEDが点灯します。ピンが低の場合、電流は流れず、LEDは消灯します。

**配線**

|wiring_led|


**コードの記述**

.. note::

    * 「 ``2.1_hello_led.ino`` 」ファイルを「 ``pico-2w-kit-main/arduino/2.1_hello_led`` 」のパスで開きます。
    * または、このコードを **Arduino IDE** にコピーしてください。
    * アップロードボタンをクリックする前に、Raspberry Pi Picoボードと正しいポートを選択してください。

.. code-block:: Arduino

    const int ledPin = 15;  // LEDに接続されたGPIOピン

    void setup() {
      pinMode(ledPin, OUTPUT);  // GPIOピンを出力として初期化
    }

    void loop() {
      digitalWrite(ledPin, HIGH);  // LEDをオン
      delay(1000);                 // 1秒間待機
      digitalWrite(ledPin, LOW);   // LEDをオフ
      delay(1000);                 // 1秒間待機
    }

コードをアップロードした後、LEDは1秒間点灯し、次の1秒間は消灯を繰り返します。

**コードの理解**

#. 変数の宣言：

   定数整数型 ``ledPin`` を宣言し、その値を15に設定します。これは、LEDが接続されているGPIOピン15に対応しています。

   .. code-block:: Arduino

        const int ledPin = 15;

#. Setup Function:

   ``setup()`` 関数は、ボードが電源オンまたはリセットされると一度だけ実行されます。ここでは、 ``pinMode()`` を使用して ``ledPin`` を出力ピンとして初期化します。

   .. code-block:: Arduino

        void setup() {
          pinMode(ledPin, OUTPUT);
        }

#. Loop Function:

   * ``loop()`` 関数は、 ``setup()`` の後に繰り返し実行されます。
   * ``digitalWrite()`` を使用して、 ``ledPin`` の電圧を設定します。 ``HIGH`` に設定すると3.3Vが供給され、LEDが点灯します。 ``LOW`` に設定すると、電圧は0Vに下がり、LEDが消灯します。
   * ``delay(1000)`` 関数は、LEDのオン・オフの間に1秒の待機時間を作成します。

   .. code-block:: Arduino

        void loop() {
          digitalWrite(ledPin, HIGH);
          delay(1000);
          digitalWrite(ledPin, LOW);
          delay(1000);
        }

**追加のヒント**

* **抵抗の理解**: 220Ωの抵抗は、LEDに流れる電流を制限し、LEDが焼き切れないように保護します。
* **極性の重要性**: LEDが正しく接続されていることを確認してください。長い脚がプラスのアノードで、GPIOピンに接続される抵抗に向けて接続する必要があります。
* **実験**: ``delay(1000)`` の値を変更して、LEDの点滅速度を速くしたり遅くしたりしてみましょう。

**結論**

おめでとうございます！Raspberry Pi Pico 2 Wを使用した最初のハードウェアプロジェクトを作成しました。このシンプルなLED点滅プロジェクトは、物理コンピューティングの世界への基本的なステップです。ここからは、ボタン、センサー、その他のコンポーネントを追加して、さらに複雑なプロジェクトに挑戦できます。
