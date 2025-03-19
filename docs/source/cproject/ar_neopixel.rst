.. note:: 

    Facebookで「SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community」へようこそ！Raspberry Pi、Arduino、ESP32に情熱を持つ仲間たちと一緒に、さらに深く探求しましょう。

    **参加する理由は？**

    - **専門的サポート**: コミュニティやチームの助けを借りて、アフターサービスの問題や技術的な課題を解決します。
    - **学び・共有**: スキルを高めるためのヒントやチュートリアルを交換します。
    - **独占的なプレビュー**: 新製品の発表やスニークピークに早期アクセス。
    - **特別割引**: 最新製品の独占的な割引を楽しんでください。
    - **祭りのプロモーションとギブアウェイ**: ギブアウェイやホリデープロモーションに参加してください。

    👉一緒に探索し、創造してみませんか？クリックして今すぐ参加しましょう！[|link_sf_facebook|]

.. _ar_neopixel:

3.3 RGB LEDストリップの制御
===========================================================

このレッスンでは、Raspberry Pi Pico 2 WとMicroPythonを使用して、 **RGB LEDストリップ** （具体的にはWS2812タイプ）の制御方法を学びます。

WS2812は、制御回路とRGBチップを5050サイズのLEDパッケージに統合したスマートLEDです。各LEDには独自のビルトインコントローラーがあり、単一のデータラインを使用して各LEDを個別に制御できます。これにより、ストリップ上の各LEDの色と明るさを独立して変更することができます。


* :ref:`cpn_ws2812`

**必要なコンポーネント**

このプロジェクトに必要なコンポーネントは以下の通りです。

全キットを購入するのが便利です。こちらがリンクです：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前
        - このキットのアイテム
        - 購入リンク
    *   - Pico 2 W Starter Kit
        - 450+
        - |link_pico2w_kit|

以下のリンクから個別に購入することもできます。

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
        - 複数
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_ws2812`
        - 1
        - |link_ws2812_buy|

**回路図**

|sch_ws2812|

**配線**

|wiring_ws2812|

電流の引き出しに注意してください。PicoのVBUSピンは少数のLED（例えば8個）に電力を供給できますが、より多くのLEDを使用する場合は、Picoを過負荷から守るために外部電源が必要になる場合があります。

**コードの記述**

.. note::

    * ファイル ``3.3_rgb_led_strip.ino`` を ``pico-2w-kit-main/arduino/3.3_rgb_led_strip`` のパスで開くことができます。
    * または、このコードを **Arduino IDE** にコピーします。
    * Raspberry Pi Picoボードと正しいポートを選択してから、アップロードボタンをクリックしてください。
    * ここでは ``Adafruit_NeoPixel`` ライブラリが使用されています。 **ライブラリマネージャ** からインストールできます。

      .. image:: img/lib_neopixel.png

.. code-block:: arduino

  #include <Adafruit_NeoPixel.h>

  #define PIXEL_PIN    0    // NeoPixelsに接続されたデジタルIOピン
  #define PIXEL_COUNT  8    // NeoPixelsの数

  // NeoPixelストリップオブジェクトを宣言
  Adafruit_NeoPixel strip(PIXEL_COUNT, PIXEL_PIN, NEO_GRB + NEO_KHZ800);

  void setup() {
    strip.begin();           // NeoPixelライブラリを初期化
    strip.show();            // できるだけ早くすべてのピクセルを消灯
  }

  void loop() {
    // 各ピクセルの色を設定
    strip.setPixelColor(0, strip.Color(255, 0, 0));   // 赤
    strip.setPixelColor(1, strip.Color(0, 255, 0));   // 緑
    strip.setPixelColor(2, strip.Color(0, 0, 255));   // 青
    strip.setPixelColor(3, strip.Color(255, 255, 0)); // 黄色
    strip.setPixelColor(4, strip.Color(0, 255, 255)); // シアン
    strip.setPixelColor(5, strip.Color(255, 0, 255)); // マゼンタ
    strip.setPixelColor(6, strip.Color(255, 255, 255)); // 白
    strip.setPixelColor(7, strip.Color(0, 0, 0));     // 消灯

    strip.show();  // ストリップを新しい内容で更新
    delay(1000);   // 1秒待つ

    // すべてのピクセルを消灯
    strip.clear();
    strip.show();
    delay(1000);   // 1秒待つ
  }

コードをアップロードした後、LEDが異なる色で点灯し、1秒間点灯した後、1秒間消灯するのが確認できます。

**コードの理解**

#. ライブラリを含む：

   .. code-block:: arduino
    
      #include <Adafruit_NeoPixel.h>

#. 定数を定義：

   * ``PIXEL_PIN``: LEDストリップのデータ入力に接続されたGPIOピン（GP0）。
   * ``PIXEL_COUNT``: ストリップ上のLEDの数。

#. ストリップを初期化：

   ``NEO_GRB + NEO_KHZ800``: 色の順序と通信速度を指定します。

   .. code-block:: arduino
    
      Adafruit_NeoPixel strip(PIXEL_COUNT, PIXEL_PIN, NEO_GRB + NEO_KHZ800);
      
#. ``setup()`` 関数内：

   * ``strip.begin()``: NeoPixelライブラリを初期化します。
   * ``strip.show()``: すべてのピクセルが消灯されていることを確認します。

#. ``loop()`` 関数内：

   * ``strip.setPixelColor(index, color)``: 特定のピクセルの色を設定します。
   * ``strip.Color(r, g, b)``: 赤、緑、青の成分（0-255）から24ビットの色値を作成します。
   * ``strip.show()``: 更新された色データをストリップに送信します。
   * ``strip.clear()``: メモリ内のピクセルデータをクリアします（次の ``show()`` でピクセルが消灯します）。

**応用例：カラーワイプアニメーション**

順番に各LEDが点灯するシンプルなアニメーションを作成しましょう。

* ``colorWipe()`` 関数：指定された色で順番に各ピクセルを点灯させます。
* 異なる色で ``colorWipe()`` を呼び出してアニメーションを作成します。

.. code-block:: arduino
    
  #include <Adafruit_NeoPixel.h>

  #define PIXEL_PIN    0
  #define PIXEL_COUNT  8

  Adafruit_NeoPixel strip(PIXEL_COUNT, PIXEL_PIN, NEO_GRB + NEO_KHZ800);

  void setup() {
    strip.begin();
    strip.show(); // すべてのピクセルをオフに初期化
  }

  void loop() {
    colorWipe(strip.Color(255, 0, 0), 50); // 赤
    colorWipe(strip.Color(0, 255, 0), 50); // 緑
    colorWipe(strip.Color(0, 0, 255), 50); // 青
  }

  void colorWipe(uint32_t color, int wait) {
    for(int i=0; i<strip.numPixels(); i++) {
      strip.setPixelColor(i, color);
      strip.show();
      delay(wait);
    }
  }

コードをアップロードした後、LEDは赤、緑、青と順に点灯し、それぞれが1秒間続きます。

**応用例：レインボーサイクルアニメーション**

* ``rainbowCycle()`` 関数：すべてのピクセルにわたって虹色のサイクルを実行します。
* ネストされたループが色の滑らかな遷移を作り出します。
* ``Wheel()`` 関数：0から255の位置にわたって虹色を生成します。

.. code-block:: arduino
    
  #include <Adafruit_NeoPixel.h>

  #define PIXEL_PIN    0
  #define PIXEL_COUNT  8

  Adafruit_NeoPixel strip(PIXEL_COUNT, PIXEL_PIN, NEO_GRB + NEO_KHZ800);

  void setup() {
    strip.begin();
    strip.show(); // すべてのピクセルをオフに初期化
  }

  void loop() {
    rainbowCycle(20); // ステップごとに20msの遅延でレインボーサイクル
  }

  void rainbowCycle(int wait) {
    uint16_t i, j;

    for(j = 0; j < 256 * 5; j++) { // 5回の全色サイクル
      for(i=0; i< strip.numPixels(); i++) {
        strip.setPixelColor(i, Wheel(((i * 256 / strip.numPixels()) + j) & 255));
      }
      strip.show();
      delay(wait);
    }
  }

  // 0から255の値を入力して色の値を取得します。
  // 色はr - g - b - rへと戻る遷移です。
  uint32_t Wheel(byte WheelPos) {
    if(WheelPos < 85) {
      return strip.Color(WheelPos * 3, 255 - WheelPos * 3, 0);
    } else if(WheelPos < 170) {
      WheelPos -= 85;
      return strip.Color(255 - WheelPos * 3, 0, WheelPos * 3);
    } else {
      WheelPos -= 170;
      return strip.Color(0, WheelPos * 3, 255 - WheelPos * 3);
    }
  }

コードをアップロードした後、LEDストリップはスムーズに色の虹を循環表示するはずです。

**さらなる探求**

* カスタムアニメーションの作成：

  * 異なる色やアニメーションを試してみましょう。
  * 複数のアニメーション機能を組み合わせてみましょう。

* センサーへの応答：

  センサーからの入力を使って、LEDの色やパターンを変更します。

* ビジュアライザーの構築：

  音声入力に基づいてLEDを変化させる音楽ビジュアライザーを作成します。

**電力に関する考慮事項**

* 電流の引き出し：

  * 各LEDは最大で60mAの電流を引き出すことができます。
  * 8個のLEDの場合、最大で480mAです。
  * 電源が必要な電流を供給できることを確認してください。

* 外部電源：

  * より大きなストリップや高い明るさの場合は、外部の5V電源を使用してください。
  * 外部電源のグラウンドをPicoのグラウンドに接続します。

**結論**

このレッスンでは、Raspberry Pi PicoとAdafruit NeoPixelライブラリを使用してWS2812 RGB LEDストリップを制御する方法を学びました。個々のピクセルを操作することで、プロジェクトに素晴らしい視覚効果を作成できます。
