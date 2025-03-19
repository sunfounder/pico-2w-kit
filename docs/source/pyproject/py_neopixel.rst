.. note:: 

    こんにちは！FacebookのSunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Raspberry Pi、Arduino、ESP32を深く学び、仲間たちと一緒に探索していきましょう。

    **参加する理由は？**

    - **専門的なサポート**: 購入後の問題や技術的な課題を、コミュニティとチームのサポートで解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **特別な先行公開**: 新製品の発表や先取り情報をいち早く手に入れましょう。
    - **特別割引**: 最新製品をお得に購入できる割引があります。
    - **季節ごとのプロモーションとプレゼント**: プレゼント企画やホリデープロモーションに参加しましょう。

    👉 さあ、私たちと一緒に探索し、創造を始めましょう！[|link_sf_facebook|] をクリックして、今すぐ参加してください！

.. _py_neopixel:

3.3 RGB LEDストリップ
======================

このレッスンでは、Raspberry Pi Pico 2 WとMicroPythonを使用して **RGB LEDストリップ** （具体的にはWS2812タイプ）を制御する方法を学びます。

WS2812は、制御回路とRGBチップを5050サイズのLEDパッケージに統合したスマートLEDです。各LEDには独自のコントローラーが内蔵されており、1本のデータラインで個々のLEDを制御できます。これにより、ストリップの各LEDの色と明るさを個別に変更することができます。


* :ref:`cpn_ws2812`

**必要な部品**

このプロジェクトで必要な部品は以下の通りです。

全ての部品がセットになったキットを購入するのが便利です。こちらのリンクをご参照ください：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前    
        - このキットのアイテム
        - リンク
    *   - Pico 2 Wスターターキット    
        - 450+
        - |link_pico2w_kit|

また、以下のリンクから部品を個別に購入することもできます。

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - コンポーネント    
        - 数量
        - リンク

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
        - 数個
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_ws2812`
        - 1
        - |link_ws2812_buy|


**回路図**

|sch_ws2812|


**配線**


|wiring_ws2812|

電流の消費に注意してください。PicoのVBUSピンは少数のLED（例えば8個）に電力を供給できますが、LEDの数が多くなると、Picoの過負荷を避けるために外部電源が必要になる場合があります。




**コードの作成**

.. note::

    * ``pico-2w-kit-main/micropython`` から ``3.3_rgb_led_strip.py`` を開くか、コードをThonnyにコピーして、「実行」をクリックするか、F5を押します。
    * 正しいインタープリターが選択されていることを確認してください：MicroPython（Raspberry Pi Pico）.COMxx。
    * ここでは ``ws2812.py`` というライブラリを使用する必要があります。これがPicoにアップロードされているか確認し、詳細なチュートリアルについては :ref:`add_libraries_py` を参照してください。

.. code-block:: python

    import machine
    from ws2812 import WS2812

    # LEDストリップの初期化
    led_strip = WS2812(machine.Pin(0), 8)  # GP0を使用、8個のLED

    # 各LEDの色を設定
    led_strip[0] = [255, 0, 0]     # 赤
    led_strip[1] = [0, 255, 0]     # 緑
    led_strip[2] = [0, 0, 255]     # 青
    led_strip[3] = [255, 255, 0]   # 黄色
    led_strip[4] = [0, 255, 255]   # シアン
    led_strip[5] = [255, 0, 255]   # マゼンタ
    led_strip[6] = [255, 255, 255] # 白
    led_strip[7] = [128, 128, 128] # グレー

    # LEDストリップを更新して色を表示
    led_strip.write()

このコードが実行されると、GP0に接続された8個のWS2812 LEDストリップは、以下の色を表示します：

* **LED 0**: 赤 (255, 0, 0)
* **LED 1**: 緑 (0, 255, 0)
* **LED 2**: 青 (0, 0, 255)
* **LED 3**: 黄色 (255, 255, 0)
* **LED 4**: シアン (0, 255, 255)
* **LED 5**: マゼンタ (255, 0, 255)
* **LED 6**: 白 (255, 255, 255)
* **LED 7**: グレー (128, 128, 128)

**コードの理解**

#. ライブラリのインポート：

   * ``machine``: ハードウェア関連の関数にアクセスするためのモジュール。
   * ``WS2812``: WS2812 LEDストリップを制御するためのライブラリ。

#. LEDストリップの初期化：

   * ``led_strip = WS2812(machine.Pin(0), 8)``: GP0に接続された8個のLEDを持つLEDストリップを初期化します。

#. 色の設定：

   * ``led_strip[0] = [255, 0, 0]``: 各LEDにRGB値（赤、緑、青）を使って色を割り当てます。値は0から255の範囲です。

#. LEDストリップの更新：

   * ``led_strip.write()``: 色データをLEDストリップに送信して、色を表示します。

**流れる虹色効果を作ろう！**

次に、ランダムに色を生成して、それをストリップに沿ってシフトさせるカラフルな流れる光のエフェクトを作成します。

.. code-block:: python

    import machine
    from ws2812 import WS2812
    import utime
    import urandom

    # LEDストリップのLED数
    NUM_LEDS = 8

    # 8個のLEDを持つLEDストリップを初期化
    led_strip = WS2812(machine.Pin(0), NUM_LEDS)

    def flowing_light():
        # ストリップに沿って色をシフト
        for i in range(NUM_LEDS - 1, 0, -1):
            led_strip[i] = led_strip[i - 1]
        # 最初のLEDにランダムな色を生成
        led_strip[0] = [urandom.getrandbits(8), urandom.getrandbits(8), urandom.getrandbits(8)]
        # ストリップを更新
        led_strip.write()
        # アニメーションがスムーズになるように少し遅延
        utime.sleep_ms(100)

    # メインループ
    while True:
        flowing_light()


コードが実行されると、LEDストリップは流れるダイナミックなエフェクトを表示し、各サイクルで新しいランダムな色が最初に導入され、それがストリップの先端に向かってシフトします。

**コードの理解**

#. ランダムカラー生成：0から255までの範囲で各コンポーネントがランダムなRGB色を生成します。

   .. code-block:: python

        [urandom.getrandbits(8), urandom.getrandbits(8), urandom.getrandbits(8)]

#. 色のシフト：各LEDの色を次の位置に移動させて、流れるエフェクトを作成します。

   .. code-block:: python

        for i in range(NUM_LEDS - 1, 0, -1):
            led_strip[i] = led_strip[i - 1]

#. 無限ループ：LEDストリップを継続的に更新してアニメーションを実行し続けます。

   .. code-block:: python

        while True:
            flowing_light()

**さらに実験する**

* **速度調整**: ``utime.sleep_ms(100)`` を変更して、流れるエフェクトを速くしたり遅くしたりできます。
* **より多くのLED**: より長いストリップがある場合、 ``WS2812(machine.Pin(0), number_of_leds)`` の数を変更してください。
* **カスタムアニメーション**: 異なるパターンや色の組み合わせを試して、自分だけのアニメーションを作成します。

**結論**

Raspberry Pi Pico 2 WとMicroPythonを使用してRGB LEDストリップを制御する方法を学びました！これにより、素晴らしい光のディスプレイ、ムードライティング、さらにはインタラクティブなアートプロジェクトを作成する可能性が広がります。



