.. note::

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Raspberry Pi、Arduino、ESP32について、他の愛好者とともにさらに深く学びましょう。

    **なぜ参加するのか？**

    - **専門家のサポート**: コミュニティやチームのサポートを受けて、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**: スキルを向上させるためのヒントやチュートリアルを交換できます。
    - **独占的なプレビュー**: 新製品の発表や先取り情報をいち早くチェックできます。
    - **特別割引**: 最新製品に対する独占的な割引を楽しめます。
    - **祭事プロモーションとプレゼント**: ギブアウェイや休日のプロモーションに参加できます。

    👉 一緒に探求し、創造しませんか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _ar_led_bar:

2.2 - レベルの表示
=============================

このレッスンでは、Raspberry Pi Pico 2 Wを使用してLEDバーグラフを制御する方法を学びます。LEDバーグラフは、通常、音量、信号強度、その他の測定値などのレベルを表示するために使用される、1列に配置された10個のLEDから構成されています。LEDを順番に点灯させて、レベル表示効果を作り出します。

|img_led_bar_pin|

* :ref:`cpn_led_bar`

**必要な部品**

このプロジェクトでは、以下の部品が必要です。

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
        - 10（220Ω）
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led_bar`
        - 1
        - 

**回路図**

|sch_ledbar|

LEDバーグラフには10個のLEDがあり、それぞれを個別に制御できます。ここでは、10個のLEDのアノードがGP6〜GP15に接続され、カソードは220Ωの抵抗を介してGNDに接続されています。

**配線**

|wiring_ledbar|

**コードの記述**

.. note::

    * 「 ``2.2_display_the_level.ino`` 」ファイルを「 ``pico-2w-kit-main/arduino/2.2_display_the_level`` 」のパスで開きます。
    * または、このコードを **Arduino IDE** にコピーしてください。
    * アップロードボタンをクリックする前に、Raspberry Pi Picoボードと正しいポートを選択してください。

.. code-block:: Arduino

    // LEDバーグラフに接続されたGPIOピンを定義
    const int ledPins[] = {6, 7, 8, 9, 10, 11, 12, 13, 14, 15};

    void setup() {
      // 各ピンを出力として初期化
      for (int i = 0; i < 10; i++) {
        pinMode(ledPins[i], OUTPUT);
      }
    }

    void loop() {
      // LEDを順番に点灯
      for (int i = 0; i < 10; i++) {
        digitalWrite(ledPins[i], HIGH); // LEDを点灯
        delay(500);                     // 500ミリ秒待機
        digitalWrite(ledPins[i], LOW);  // LEDを消灯
        delay(500);                     // 500ミリ秒待機
      }
    }    

コードをアップロードした後、バーグラフのLEDが順番に点灯し、レベル表示効果が作成されるはずです。各LEDは0.5秒間点灯し、その後消灯し、次のLEDが点灯します。

**コードの理解**

#. LEDピンの定義：

   配列 ``ledPins`` を作成し、バーグラフの各LEDに接続されたGPIOピン番号を保持します。

   .. code-block:: Arduino

      const int ledPins[] = {6, 7, 8, 9, 10, 11, 12, 13, 14, 15};

#. ピンの初期化：

   ``setup()`` 関数内で、 ``ledPins`` 配列内の各ピンを出力として設定します。

   .. code-block:: Arduino

      void setup() {
        for (int i = 0; i < 10; i++) {
          pinMode(ledPins[i], OUTPUT);
        }
      }

#. LEDの制御：

   ``loop()`` 関数内で、 ``for`` ループを使用して各LEDを順番に制御します。LEDを点灯させ、500ミリ秒待機してから消灯し、次のLEDに進みます。

   .. code-block:: Arduino

      void loop() {
        for (int i = 0; i < 10; i++) {
          digitalWrite(ledPins[i], HIGH);
          delay(500);
          digitalWrite(ledPins[i], LOW);
          delay(500);
        }
      }

**さらに実験する**

* **順番を逆にする**: コードを修正して、LEDを逆順に点灯させてみましょう。

* **バウンス効果を作成する**: 最後のLEDに到達した後、シーケンスが逆順に戻るようにします。

  .. code-block:: Arduino
    
      void loop() {
        // 昇順シーケンス
        for (int i = 0; i < 10; i++) {
          digitalWrite(ledPins[i], HIGH);
          delay(200);
          digitalWrite(ledPins[i], LOW);
        }
        // 降順シーケンス
        for (int i = 8; i >= 0; i--) {
          digitalWrite(ledPins[i], HIGH);
          delay(200);
          digitalWrite(ledPins[i], LOW);
        }
      }

* **速度を調整する**: 遅延時間を変更して、LEDの点灯速度を速くしたり遅くしたりできます。


**結論**

このレッスンでは、Raspberry Pi Picoを使用して複数のLEDを制御する方法と、ループや遅延などの簡単なプログラミング構造を使って視覚的な効果を作成する方法を学びました。この基本的な知識は、LEDディスプレイやインジケーターを使用したより高度なプロジェクトに役立ちます。
