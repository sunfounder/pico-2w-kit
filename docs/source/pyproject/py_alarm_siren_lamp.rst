.. note:: 

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32について、仲間たちと一緒にさらに深く学んでいきましょう。

    **参加する理由は？**

    - **専門的なサポート**：販売後の問題や技術的な課題を、コミュニティとチームのサポートを受けて解決できます。
    - **学びと共有**：スキルを高めるために、ヒントやチュートリアルを交換できます。
    - **限定プレビュー**：新製品の発表を早期に知り、先行して情報を得ることができます。
    - **特別割引**：最新製品の独占割引をお楽しみいただけます。
    - **フェスティブプロモーションとプレゼント**：プレゼント企画やホリデープロモーションに参加できます。

    👉 私たちと一緒に探索し、創造する準備はできましたか？[|link_sf_facebook|]をクリックして、今すぐ参加してください！

.. _py_alarm_lamp:

7.3 警報サイレンランプの作成
=======================================================

このプロジェクトでは、Raspberry Pi Pico 2 Wを使用して **警報サイレンランプ** を作成します。このデバイスは、警察車両や緊急車両のフラッシングライトとサイレン音をシミュレートします。PWM（パルス幅変調）、割り込み、およびLEDやブザーなどの複数のコンポーネントを制御する方法を学ぶための楽しい方法です。



**必要な部品**

このプロジェクトで必要な部品は以下の通りです。

一式を購入するのが非常に便利です。こちらからリンクを確認してください：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前
        - このキットに含まれる部品
        - リンク
    *   - Pico 2 W スターターキット
        - 450+
        - |link_pico2w_kit|

下記のリンクから個別に購入することもできます。


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
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 6
        - :ref:`cpn_transistor`
        - 1(S8050)
        - |link_transistor_buy|
    *   - 7
        - :ref:`cpn_resistor`
        - 3(1KΩ, 220Ω, 10KΩ)
        - |link_resistor_buy|
    *   - 8
        - パッシブ :ref:`cpn_buzzer`
        - 1
        - |link_passive_buzzer_buy|
    *   - 9
        - :ref:`cpn_capacitor`
        - 1(104)
        - |link_capacitor_buy|
    *   - 10
        - :ref:`cpn_slide_switch`
        - 1
        - 

**コンポーネントの理解**

* **パッシブブザー**：音を鳴らすためには外部信号が必要です。PWMを使って周波数を変化させ、サイレン効果を作ります。
* **LED**：サイレンのフラッシュライトをシミュレートするために明るさを変更します。
* **スライドスイッチ**：アラームのオン/オフを制御するためのスイッチとして使用します。
* **NPNトランジスタ（S8050）**：PicoのGPIOピンでは十分な電流を供給できないため、ブザーを駆動するために使用します。
* **抵抗とコンデンサ**：スライドスイッチのデバウンスを行い、安定した読み取りを確保します。

**回路図**

|sch_alarm_siren_lamp|

* GP17はスライドスイッチの中央ピンに接続され、10Kの抵抗とコンデンサ（フィルタ）が並列にGNDに接続されており、スライドスイッチを左または右に切り替えたときに、安定した高または低レベルの出力を得ることができます。
* GP15が高信号になると、NPNトランジスタが導通し、パッシブブザーが鳴り始めます。このパッシブブザーは周波数を徐々に上げて、サイレン音を発生させます。
* LEDはGP16に接続され、サイレンをシミュレートするために、周期的に明るさを変化させるようにプログラムされています。



**配線**

|wiring_alarm_siren_lamp|


**コードの作成**

スライドスイッチの位置に基づいて、ブザーとLEDを制御するMicroPythonスクリプトを作成します。

.. note::

    * ``pico-2w-kit-main/micropython`` の ``7.3_alarm_siren_lamp.py`` を開くか、コードをThonnyにコピーして、「Run」をクリックするか、F5を押してください。
    * 正しいインタープリタが選択されていることを確認してください：MicroPython（Raspberry Pi Pico）。COMxx。

.. code-block:: python

    import machine
    import utime

    # ブザーとLEDのPWM初期化
    buzzer = machine.PWM(machine.Pin(15))
    led = machine.PWM(machine.Pin(16))
    led.freq(1000)  # LEDのPWM周波数を設定

    # スライドスイッチの初期化
    switch = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_DOWN)

    # 値を別の範囲にマッピングする関数
    def interval_mapping(x, in_min, in_max, out_min, out_max):
        # in_min != in_max を確保してゼロ除算を防ぐ
        if in_max - in_min == 0:
            return out_min
        return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

    # メインループ
    try:
        while True:
            if switch.value() == 1:
                # アラームがON
                # 周波数と明るさを増加
                for i in range(0, 100, 2):
                    # 'i'をLEDの明るさとブザーの周波数にマッピング
                    brightness = interval_mapping(i, 0, 100, 0, 65535)
                    frequency = interval_mapping(i, 0, 100, 500, 2000)
                    
                    # LEDの明るさを設定
                    led.duty_u16(brightness)
                    
                    # ブザーの周波数とデューティサイクルを設定
                    buzzer.freq(frequency)
                    buzzer.duty_u16(32768)  # 50%デューティサイクル
                    
                    utime.sleep(0.01)
                    
                # 周波数と明るさを減少
                for i in range(100, 0, -2):
                    brightness = interval_mapping(i, 0, 100, 0, 65535)
                    frequency = interval_mapping(i, 0, 100, 500, 2000)
                    
                    led.duty_u16(brightness)
                    buzzer.freq(frequency)
                    buzzer.duty_u16(32768)
                    
                    utime.sleep(0.01)
            else:
                # アラームがOFF
                # LEDとブザーをオフ
                led.duty_u16(0)
                buzzer.duty_u16(0)
                utime.sleep(0.1)
    except KeyboardInterrupt:
        # クリーンアップ
        buzzer.deinit()
        led.deinit()
        print("Program stopped.")

コードが実行されると、スライドスイッチをONにすると、ブザーがサイレン音を発し、
LEDがそれに合わせてフラッシュします。OFFにすると、アラームが停止します。

**コードの理解**

#. 初期化：

   * **buzzer**：GP15のPWMオブジェクト。
   * **led**：GP16のPWMオブジェクト、明るさを滑らかに制御するために周波数を1kHzに設定。
   * **switch**：GP17の入力ピン、内部プルダウン抵抗を使用。

#. インターバルマッピング関数：

   ある範囲から別の範囲へ値をマッピングする関数。ループ変数を目的の周波数や明るさの範囲にスケーリングするのに便利です。

   .. code-block:: python

        # 値を別の範囲にマッピングする関数
        def interval_mapping(x, in_min, in_max, out_min, out_max):
            # in_min != in_max を確保してゼロ除算を防ぐ
            if in_max - in_min == 0:
                return out_min
            return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

#. メインループ：

   * スイッチの状態を確認。
   * スイッチがONの場合（ ``switch.value() == 1`` ）：

     * サイレン効果をシミュレートするために2つのループを実行：
     * 周波数と明るさを増加。
     * 周波数と明るさを減少。
     * ブザーの周波数は500Hzから2000Hzに変化します。
     * LEDの明るさはオフから最大明るさまで変化します。

     .. code-block:: python

        if switch.value() == 1:
            # アラームがON
            # 周波数と明るさを増加
            for i in range(0, 100, 2):
                # 'i'をLEDの明るさとブザーの周波数にマッピング
                brightness = interval_mapping(i, 0, 100, 0, 65535)
            ...
                
                utime.sleep(0.01)

   * スイッチがOFFの場合：LEDとブザーをオフにします。

     .. code-block:: python

            else:
                # アラームがOFF
                # LEDとブザーをオフ
                led.duty_u16(0)
                buzzer.duty_u16(0)
                utime.sleep(0.1)

   * 例外処理：キーボード割り込み（Ctrl+C）をキャッチして、PWMオブジェクトをクリーンに終了します。

     .. code-block:: python
    
        except KeyboardInterrupt:
            # クリーンアップ
            buzzer.deinit()
            led.deinit()
            print("Program stopped.")

**さらに実験してみましょう**

* サイレン効果の調整：

  * ``interval_mapping`` 関数の周波数範囲を変更して、音の高さを変更します。
  * ループの遅延（ ``utime.sleep(0.01)`` ）を調整して、サイレンのサイクルの速度を速くしたり遅くしたりします。

* 追加のLEDを加える：

  * 複数の色のLEDを追加して、よりダイナミックな光のショーを作成します。
  * 複数のGPIOピンとPWMチャネルを使用します。

* 動作検出でのアクティベーション：

  * スライドスイッチを動きセンサー（例：PIRセンサー）に置き換えて、動きが検出されたときにアラームをトリガーします。

* リモコン操作：

  * 赤外線受信機を統合して、リモコンを使ってアラームを操作します。


**結論**


Raspberry Pi Pico 2 Wを使用して警報サイレンランプを成功裏に作成しました！このプロジェクトでは、複数のコンポーネントを制御し、インタラクティブな効果を作成する方法を学びました。セキュリティシステムや緊急信号、創造的なアートインスタレーションなど、より複雑なプロジェクトのための優れた基盤となります。
