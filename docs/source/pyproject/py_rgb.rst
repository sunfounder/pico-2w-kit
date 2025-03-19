.. note::

    こんにちは！FacebookのSunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！仲間たちと一緒にRaspberry Pi、Arduino、ESP32についてさらに深く学びましょう。

    **参加する理由は？**

    - **専門的なサポート**: 当コミュニティとチームの助けを借りて、販売後の問題や技術的な課題を解決できます。
    - **学び・共有**: スキルを向上させるためのヒントやチュートリアルを交換しましょう。
    - **特別なプレビュー**: 新製品の発表やプレビューに早期アクセスできます。
    - **特別割引**: 最新製品の独占的な割引を楽しめます。
    - **フェスティブなプロモーションとプレゼント企画**: プレゼント企画やホリデープロモーションに参加できます。

    👉 私たちと一緒に探索し、創造を始める準備はできましたか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _py_rgb:


2.4 カラフルな光
==============================================

このレッスンでは、RGB LEDとRaspberry Pi Pico 2 Wを使用してさまざまな色を作成する方法について学びます。赤、緑、青の各成分の強度を調整することによって、光を混ぜて広範な色を作り出すことができます。この概念は、加法混色法に基づいています。

**加法混色とは？**

加法混色は、異なる色の光を組み合わせて新しい色を作り出す方法です。赤、緑、青の光を異なる強度で組み合わせると、可視光線の任意の色を作り出すことができます。例えば：

* **赤 + 緑 = 黄**
* **赤 + 青 = マゼンタ**
* **緑 + 青 = シアン**
* **赤 + 緑 + 青 = 白**

|img_rgb_mix|

**必要な部品**

このプロジェクトでは、以下の部品が必要です。

キット一式を購入するのが便利です。こちらがリンクです：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名称
        - このキットに含まれる部品
        - リンク
    *   - Pico 2 Wスターターキット
        - 450+
        - |link_pico2w_kit|

また、以下のリンクから個別に購入することもできます。


.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - 部品
        - 数量
        - リンク

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
        - 3(1-330Ω, 2-220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_rgb`
        - 1
        - |link_rgb_led_buy|

**回路図**

|sch_rgb|

PWMピンGP13、GP14、GP15がRGB LEDの赤、緑、青のピンをそれぞれ制御し、共通カソードピンをGNDに接続します。これにより、PWM値を変えることによってRGB LEDに特定の色を表示させることができます。

**配線図**

|img_rgb_pin|

RGB LEDには4本のピンがあります：長いピンは共通カソードピンで、通常はGNDに接続します。長いピンの隣の左側のピンは赤、右側の2本のピンは緑と青です。

赤いLEDには、同じ電流で緑や青よりも明るいため、より高い抵抗を使用します。

|wiring_rgb|



**コードの作成**

PWM（パルス幅変調）を使用して、各色の強度を制御し、さまざまな色を作り出すMicroPythonプログラムを作成します。

.. note::

    * ``2.4_colorful_light.py`` を ``pico-2w-kit-main/micropython`` から開くか、このコードをThonnyにコピーして、「Run」をクリックするか、F5キーを押して実行します。
    * 正しいインタープリターが選択されていることを確認してください：MicroPython（Raspberry Pi Pico）。COMxx。

.. code-block:: python

    import machine
    import utime

    # 赤、緑、青のピンのPWM初期化
    red = machine.PWM(machine.Pin(13))
    green = machine.PWM(machine.Pin(14))
    blue = machine.PWM(machine.Pin(15))

    # PWMの周波数を設定
    red.freq(1000)
    green.freq(1000)
    blue.freq(1000)

    def map_value(x, in_min, in_max, out_min, out_max):
        # 値を範囲から範囲へマッピング
        return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

    def set_color(r, g, b):
        # Duty cycleを調整して色を設定
        red.duty_u16(map_value(r, 0, 255, 0, 65535))
        green.duty_u16(map_value(g, 0, 255, 0, 65535))
        blue.duty_u16(map_value(b, 0, 255, 0, 65535))

    # 例: 色をオレンジに設定
    set_color(255, 165, 0)

コードを実行すると、RGB LEDがオレンジ色に光ります。

**コードの理解**

#. ライブラリのインポート：

   * ``machine``: ハードウェア固有の機能にアクセスするため。
   * ``utime``: 時間に関連する関数（この例では使用しませんが、アニメーションなどには役立ちます）。

#. PWMオブジェクトの初期化：

   * 赤、緑、青のピンに接続されたRGB LEDのためにPWMオブジェクトを作成し、すべての色のPWM周波数を1000 Hzに設定します。

   .. code-block:: python

        # 赤、緑、青のピンのPWM初期化
        red = machine.PWM(machine.Pin(13))
        green = machine.PWM(machine.Pin(14))
        blue = machine.PWM(machine.Pin(15))

        # PWMの周波数を設定
        red.freq(1000)
        green.freq(1000)
        blue.freq(1000)

#. ``map_value`` 関数の定義：

   * ``duty_u16`` メソッドは0から65535の値を受け取りますが、色の値は通常0から255の範囲であるため、この範囲を0から65535にマッピングする必要があります。
   * ``map_value`` 関数は、入力値を適切にスケールします。

   .. code-block:: python

        def map_value(x, in_min, in_max, out_min, out_max):
            # 値を範囲から範囲へマッピング
            return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

#. ``set_color`` 関数の定義：

   この関数は、RGBの各値（0から255まで）を受け取り、それぞれの色チャンネルに対してDuty Cycleを設定します。

   .. code-block:: python

        def set_color(r, g, b):
            # Duty cycleを調整して色を設定
            red.duty_u16(map_value(r, 0, 255, 0, 65535))
            green.duty_u16(map_value(g, 0, 255, 0, 65535))
            blue.duty_u16(map_value(b, 0, 255, 0, 65535))

#. 希望の色を設定：

   ``set_color(255, 165, 0)`` を呼び出して、RGB LEDをオレンジ色に設定します。値を変更すれば、お好きなRGB色に変更できます。

**例: 色のサイクル**

コードを拡張して、異なる色をサイクルさせてみましょう。

#. 異なる色のRGB値を調べるには、グラフィックソフトウェアやオンラインのカラーピッカーを使用できます。例えば：

   * 赤: (255, 0, 0)
   * 緑: (0, 255, 0)
   * 青: (0, 0, 255)
   * 白: (255, 255, 255)
   * 紫: (128, 0, 128)

#. コードを記述：

   異なる色を表すRGBのタプルのリストを定義し、 ``while True`` ループで色をサイクルし、1秒ごとに次の色に移動します。

   .. code-block:: python
       
       import machine
       import utime
       
       # 赤、緑、青のピンのPWM初期化
       red = machine.PWM(machine.Pin(13))
       green = machine.PWM(machine.Pin(14))
       blue = machine.PWM(machine.Pin(15))
       
       # PWMの周波数を設定
       red.freq(1000)
       green.freq(1000)
       blue.freq(1000)
       
       def map_value(x, in_min, in_max, out_min, out_max):
           return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
       
       def set_color(r, g, b):
           red.duty_u16(map_value(r, 0, 255, 0, 65535))
           green.duty_u16(map_value(g, 0, 255, 0, 65535))
           blue.duty_u16(map_value(b, 0, 255, 0, 65535))
       
       # サイクルする色のリスト
       colors = [
           (255, 0, 0),     # 赤
           (0, 255, 0),     # 緑
           (0, 0, 255),     # 青
           (255, 255, 0),   # 黄
           (0, 255, 255),   # シアン
           (255, 0, 255),   # マゼンタ
           (255, 255, 255)  # 白
       ]
       
       while True:
           for color in colors:
               set_color(*color)
               utime.sleep(1)

このコードを実行すると、RGB LEDが赤、緑、青、黄、シアン、マゼンタ、白の色を順番にサイクルします。

各色は1秒間表示され、その後次の色に移行します。

**結論**

PWMを使用してRGB LEDの赤、緑、青の各成分の強度を制御することにより、膨大な種類の色を作り出すことができます。このプロジェクトは、加法混色の原理を示し、マイクロコントローラーを使用してカラフルな光のディスプレイを作成するための基礎を提供します。

**参考文献**

* |link_mpython_pwm|
