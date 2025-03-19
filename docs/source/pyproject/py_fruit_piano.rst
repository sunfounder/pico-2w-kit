.. note:: 

    SunFounderのRaspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32について、他の愛好者とともにさらに深く学んでいきましょう。

    **参加する理由は？**

    - **専門的なサポート**: 購入後の問題や技術的な課題を、コミュニティやチームのサポートで解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **限定プレビュー**: 新製品の発表や先行公開に早期アクセスできます。
    - **特別割引**: 最新製品に対する独占的な割引を楽しめます。
    - **フェスティブプロモーションやプレゼント**: プレゼント企画やホリデープロモーションに参加できます。

    👉 一緒に探求し、創造してみませんか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _py_fruit_piano:

7.9 フルーツピアノの製作
=================================================

このプロジェクトでは、Raspberry Pi Pico 2 W、MPR121静電容量式タッチセンサー、ブザー、およびRGB LEDを使用して **フルーツピアノ** を作成します。フルーツ（または導電性のある物体）を静電容量式タッチセンサーに接続することで、それらをピアノの鍵盤に変換し、触れると音符を再生し、カラフルなライトを表示します。

**必要なコンポーネント**

このプロジェクトで必要なコンポーネントは次の通りです。

全セットを購入するのは便利です。リンクはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前	
        - セットに含まれるアイテム
        - リンク
    *   - Pico 2 Wスターターキット	
        - 450+
        - |link_pico2w_kit|

個別に購入することもできます。以下のリンクから購入できます。


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
        - 複数
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_transistor`
        - 1(S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_resistor`
        - 4(1-1KΩ, 1-330Ω, 2-220Ω)
        - |link_resistor_buy|
    *   - 7
        - パッシブ :ref:`cpn_buzzer`
        - 1
        - |link_passive_buzzer_buy|
    *   - 8
        - :ref:`cpn_rgb`
        - 1
        - |link_rgb_led_buy|
    *   - 9
        - :ref:`cpn_mpr121`
        - 1
        - 

**コンポーネントの理解**

* **MPR121 静電容量式タッチセンサー**: 最大12のタッチ入力を処理できる静電容量式タッチセンサーコントローラー。接続された電極を触れることで、静電容量の変化を検出します。
* **パッシブブザー**: PWM信号で駆動することで音を発生させる電子部品。異なる音符を鳴らすために使用します。
* **RGB LED**: 赤、緑、青のLEDを1つのパッケージに統合したLED。各色の強度を調整することで、広範囲の色を表示できます。
* **フルーツや導電性の物体**: フルーツや金属物、さらには水などの物体が、MPR121に接続されることで導電性のタッチ入力として機能します。

**回路図**

|sch_fruit_piano| 

フルーツをピアノの鍵盤に変えるためには、MPR121の電極をフルーツ（例：バナナの柄など）に接続する必要があります。

最初に、MPR121が初期化され、各電極は現在の電荷に基づいた値を取得します。導体（人の体など）が電極に触れると、電荷がシフトして再調整されます。
その結果、電極の値が初期値と異なり、メイン制御ボードはその電極が触れられたことを認識します。
このプロセス中に、各電極の配線が安定していることを確認し、初期化時にその電荷がバランスを取るようにします。



**配線**

|wiring_fruit_piano|


**コードの作成**

MicroPythonスクリプトを作成して、以下の動作を行います：

* MPR121タッチセンサーを初期化します。
* 接続されたフルーツからタッチ入力を検出します。
* ブザーで対応する音符を鳴らします。
* RGB LEDをランダムな色で点灯させます。

.. note::

    * ``7.9_fruit_piano.py`` を ``pico-2w-kit-main/micropython`` から開くか、コードをThonnyにコピーして「実行」またはF5を押してください。
    * 正しいインタープリタが選択されていることを確認してください：MicroPython（Raspberry Pi Pico）。COMxx。 
    * ここでは、 ``mpr121.py`` ライブラリが必要です。Picoにアップロードされているか確認してください。詳細なチュートリアルについては、 :ref:`add_libraries_py` を参照してください。

.. code-block:: python

    from mpr121 import MPR121
    from machine import Pin, I2C, PWM
    import time
    import urandom

    # MPR121静電容量式タッチセンサーのI2C接続を初期化
    i2c = I2C(1, sda=Pin(6), scl=Pin(7))
    mpr = MPR121(i2c)

    # 音符の周波数を定義（ヘルツ単位）
    NOTE_FREQUENCIES = [
        220,  # A3
        247,  # B3
        262,  # C4
        294,  # D4
        330,  # E4
        349,  # F4
        392,  # G4
        440,  # A4
        494,  # B4
        523,  # C5
        587,  # D5
        659   # E5
    ]

    # GP15でブザーのPWMを初期化
    buzzer = PWM(Pin(15))

    # GP13（赤）、GP12（緑）、GP11（青）でRGB LEDのPWMを初期化
    red = PWM(Pin(13))
    green = PWM(Pin(12))
    blue = PWM(Pin(11))

    # LEDのPWM周波数を設定
    red.freq(1000)
    green.freq(1000)
    blue.freq(1000)

    # 音を鳴らす関数
    def play_tone(frequency):
        if frequency == 0:
            buzzer.duty_u16(0)
        else:
            buzzer.freq(frequency)
            buzzer.duty_u16(32768)  # 50%のデューティサイクル

    # 音を止める関数
    def stop_tone():
        buzzer.duty_u16(0)

    # RGB LEDにランダムな色を設定する関数
    def set_random_color():
        red.duty_u16(urandom.getrandbits(16))
        green.duty_u16(urandom.getrandbits(16))
        blue.duty_u16(urandom.getrandbits(16))

    # RGB LEDをオフにする関数
    def turn_off_led():
        red.duty_u16(0)
        green.duty_u16(0)
        blue.duty_u16(0)

    # メインループ
    try:
        last_touched = mpr.touched()
        while True:
            current_touched = mpr.touched()
            for i in range(12):
                pin_bit = 1 << i
                if current_touched & pin_bit and not last_touched & pin_bit:
                    # 電極iがタッチされた
                    print("Pin {} touched".format(i))
                    play_tone(NOTE_FREQUENCIES[i])
                    set_random_color()
                if not current_touched & pin_bit and last_touched & pin_bit:
                    # 電極iが離された
                    print("Pin {} released".format(i))
                    stop_tone()
                    turn_off_led()
            last_touched = current_touched
            time.sleep(0.01)
    except KeyboardInterrupt:
        pass
    finally:
        stop_tone()
        turn_off_led()


.. note::

    プログラムを実行する前にフルーツや導電性物体に触れないようにし、適切に初期化してください。

プログラムが開始したら、フルーツに優しく触れてください。

* ブザーは対応する音符を鳴らします。
* RGB LEDはランダムな色で点灯します。
* 異なるフルーツに触れることで異なる音符を演奏できます。

**コードの理解**

#. 初期化：

   * **I2C接続**: MPR121センサーとの通信を設定します。
   * **PWM設定**: ブザーとRGB LEDピンのPWMを初期化します。

#. 音符の周波数：

   音符に対応する周波数のリスト（A3からE5）。

#. 関数：

   * ``play_tone(frequency)``: 指定された周波数で音を鳴らします。
   * ``stop_tone()``: ブザーを停止します。
   * ``set_random_color()``: RGB LEDをランダムな色に設定します。
   * ``turn_off_led()``: RGB LEDをオフにします。

#. メインループ：

   * **タッチ検出**: 電極のタッチイベントを継続的にチェックします。
   * **タッチ処理**：

     * 電極がタッチされると、対応する音符を鳴らし、RGB LEDを点灯させます。
     * 電極が離されると、音符を止めてLEDをオフにします。

   * **デバウンス**: 短い遅延（ ``time.sleep(0.01)`` ）を追加してバウンス問題を防ぎます。

#. 例外処理：

   * キーボード割り込みでの正常終了をサポートします。
   * 最後にブザーとLEDをオフにします。


**トラブルシューティング**

* 音や光が出ない：

  * すべての配線接続を確認してください。
  * MPR121がPicoに適切に接続されているか確認してください。
  * フルーツが電極に確実に接続されているか確認してください。
  * ``mpr121.py`` がPicoに正しくアップロードされていることを確認してください。

* タッチが検出されない：

  * 複数の電極を同時に触れていないか確認してください。
  * 配線を直接触れず、フルーツや導電性物体に触れてください。
  * フルーツが乾燥しすぎていないか確認してください。湿ったフルーツの方が導電性が高いです。

* 不安定な動作：

  * Picoやセンサーが静電気にさらされていないことを確認してください。
  * 配線と接続が安定していることを確認してください。

**さらに試してみる**

* 楽器の拡張：

  * 異なる導電性の素材（例：水、金属物）をキーとして使用します。
  * 電極に対応する音符の数を増やして、より多くの音を作成します。

* ビジュアル効果：

  * ``set_random_color()`` 関数を変更して、特定の色のパターンを作成します。
  * より多くのLEDを追加して視覚的体験を強化します。

* 感度の調整：

  MPR121のタッチしきい値設定を調整して感度を変更します。

* 他のセンサーと組み合わせる：

  他のセンサー（例：光センサー）を統合して、環境条件に基づいた音や光の効果を変更します。

**結論**

Raspberry Pi Pico 2 Wを使用してフルーツピアノを成功裏に構築しました！このプロジェクトは、静電容量式タッチセンサーを音と光と組み合わせてインタラクティブな体験を作成する方法を示しています。導電性、タッチセンサー、創造的なコーディングの原則を探求する楽しい方法です。

このプロジェクトに新機能を追加したり、さまざまな素材で実験したり、追加コンポーネントを統合したりして、さらに拡張してみてください。
