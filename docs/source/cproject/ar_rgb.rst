.. note:: 

    こんにちは！FacebookのSunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Raspberry Pi、Arduino、ESP32を他の愛好者と一緒に深く学びましょう。

    **参加する理由は？**

    - **専門的なサポート**: 購入後の問題や技術的な課題をコミュニティやチームの助けを借りて解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換し、スキルを向上させましょう。
    - **限定プレビュー**: 新製品の発表や先行公開をいち早くチェックできます。
    - **特別割引**: 新しい製品に対して独占的な割引を楽しめます。
    - **祭典のプロモーションやプレゼント**: プレゼントや祝日プロモーションに参加しましょう。

    👉 一緒に探求し、創造を楽しむ準備はできましたか？[|link_sf_facebook|]をクリックして、今日から参加しましょう！

.. _ar_rgb:


2.4 カラフルな光
====================

このレッスンでは、RGB LEDとRaspberry Pi Pico 2 Wを使用してさまざまな色を作成する方法を学びます。赤、緑、青の各成分の強度を調整することで、光を混ぜて幅広い色を生成できます。この概念は、加法混色法に基づいています。

**加法混色とは？**

加法混色は、異なる色の光を組み合わせて新しい色を作る方法です。赤、緑、青の光をさまざまな強度で組み合わせると、可視光線の範囲内の任意の色を作り出すことができます。例えば：

* **赤 + 緑 = 黄**
* **赤 + 青 = マゼンタ**
* **緑 + 青 = シアン**
* **赤 + 緑 + 青 = 白**

|img_rgb_mix|

* :ref:`cpn_rgb`

**必要なコンポーネント**

このプロジェクトでは、以下のコンポーネントが必要です。

全セットを購入するのが便利なので、こちらのリンクをチェックしてください：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前
        - このキットのアイテム
        - 購入リンク
    *   - Pico 2 Wスターターキット
        - 450+
        - |link_pico2w_kit|

以下のリンクから、コンポーネントを個別に購入することもできます。


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
        - Micro USBケーブル
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
        - 3（1-330Ω、2-220Ω）
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_rgb`
        - 1
        - |link_rgb_led_buy|

**回路図**

|sch_rgb|

PWMピンGP13、GP14、GP15は、それぞれRGB LEDの赤、緑、青のピンを制御し、共通カソードピンをGNDに接続します。これにより、異なるPWM値でこれらのピンに光を重ねることで、特定の色を表示できます。



**配線**

|img_rgb_pin|

RGB LEDには4つのピンがあります。長いピンは共通カソードピンで、通常GNDに接続します。最長のピンの隣にある左のピンは赤、右側の2つのピンは緑と青です。

赤色LEDは、緑や青のLEDに比べて同じ電流でより明るいため、赤色用には高い抵抗値を使用します。

|wiring_rgb|


**コード作成**

ここでは、描画ソフトウェア（例えばペイント）でお気に入りの色を選んで、それをRGB LEDで表示する方法を学びます。

.. note::

    * ``2.4_colorful_light.ino`` ファイルを ``pico-2w-kit-main/arduino/2.4_colorful_light`` から開きます。
    * または、このコードを **Arduino IDE** にコピーします。
    * **Raspberry Pi Pico 2 W** ボードと正しいポートを選択して、「アップロード」をクリックします。
    



.. code-block:: Arduino

   // RGB LEDに接続されたGPIOピンを定義
   const int redPin = 13;   // 赤ピン
   const int greenPin = 14; // 緑ピン
   const int bluePin = 15;  // 青ピン

   void setup() {
     // 各RGB LEDピンを出力として初期化
     pinMode(redPin, OUTPUT);
     pinMode(greenPin, OUTPUT);
     pinMode(bluePin, OUTPUT);
   }

   // 色を設定する関数
   void setColor(unsigned char red, unsigned char green, unsigned char blue) {
     analogWrite(redPin, red);
     analogWrite(greenPin, green);
     analogWrite(bluePin, blue);
   }

   void loop() {
     // 赤色
     setColor(255, 0, 0);
     delay(1000);

     // 緑色
     setColor(0, 255, 0);
     delay(1000);

     // 青色
     setColor(0, 0, 255);
     delay(1000);

     // 黄色（赤 + 緑）
     setColor(255, 255, 0);
     delay(1000);

     // シアン（緑 + 青）
     setColor(0, 255, 255);
     delay(1000);

     // マゼンタ（赤 + 青）
     setColor(255, 0, 255);
     delay(1000);

     // 白色（赤 + 緑 + 青）
     setColor(255, 255, 255);
     delay(1000);

     // オフ
     setColor(0, 0, 0);
     delay(1000);
   }

コードをアップロード後、RGB LEDは赤、緑、青、黄色、シアン、マゼンタ、白色に順番に変わり、1秒ごとに各色が表示され、その後オフになります。

**コードの理解**

#. ピンの定義：

   RGB LEDの各成分に接続されたGPIOピンを定義します。

   .. code-block:: Arduino

        const int redPin = 13;
        const int greenPin = 14;
        const int bluePin = 15;

#. ピンの初期化：

   RGB LEDのピンを出力として設定します。

   .. code-block:: Arduino

        void setup() {
          pinMode(redPin, OUTPUT);
          pinMode(greenPin, OUTPUT);
          pinMode(bluePin, OUTPUT);
        }

#. 色の設定：

   ``setColor`` 関数はPWM（パルス幅変調）を使用して、各色成分の明るさを調整します。

   .. code-block:: Arduino

        void setColor(unsigned char red, unsigned char green, unsigned char blue) {
          analogWrite(redPin, red);
          analogWrite(greenPin, green);
          analogWrite(bluePin, blue);
        }

#. 色をループで表示：

   ``loop()`` 関数内で ``setColor()`` を呼び出し、異なる値を使ってさまざまな色を表示し、1秒ごとに色が変わるようにします。

   .. code-block:: Arduino

        void loop() {
          // 赤色
          setColor(255, 0, 0);
          delay(1000);
          ...

          // オフ
          setColor(0, 0, 0);
          delay(1000);
        }

**色の実験**

``setColor()`` に渡す値を調整することで、自分だけの色を作ることができます。値は0（オフ）から255（最大輝度）の範囲です。例えば：

* オレンジ：setColor(255, 165, 0);
* 紫：setColor(128, 0, 128);

特定の色のRGB値を調べるためには、カラーピッカーツールや **ペイント** などのソフトウェアを使用できます。

**結論**

このレッスンでは、Raspberry Pi Picoを使用してRGB LEDを制御し、赤、緑、青の光を混ぜることでさまざまな色を作成する方法を学びました。この知識は、LEDディスプレイ、ムードライト、または色の制御を必要とするアプリケーションに役立つ基本的な技術です。
