.. note:: 

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Facebookで他の愛好者と一緒に、Raspberry Pi、Arduino、ESP32をさらに深く学びましょう。

    **なぜ参加するのか？**

    - **専門的なサポート**：コミュニティとチームのサポートで、販売後の問題や技術的な課題を解決できます。
    - **学びとシェア**：スキルを高めるために、ヒントやチュートリアルを交換しましょう。
    - **限定プレビュー**：新しい製品発表や先行情報に早期アクセスできます。
    - **特別割引**：最新製品に対する限定割引をお楽しみいただけます。
    - **フェスティブプロモーションとプレゼント**：プレゼントやホリデープロモーションに参加しましょう。

    👉 一緒に探求し、創造を始める準備はできましたか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _py_light_theremin:

7.1 ライト・テルミンの作成
====================================================

このエキサイティングなプロジェクトでは、Raspberry Pi Pico 2 W、フォトレジスタ、そしてパッシブブザーを使用して **ライト・テルミン** を作成します。テルミンは、物理的な接触なしに演奏するユニークな楽器で、プレイヤーの手の位置に基づいて異なる音を生み出します。完全に伝統的なテルミンを再現することはできませんが、光の強度を使って音の周波数を制御することで、その機能をシミュレートできます。

* `テルミン - Wikipedia <https://en.wikipedia.org/wiki/Theremin>`_

**必要なコンポーネント**

このプロジェクトには以下のコンポーネントが必要です。

キットを購入するのが便利です。こちらのリンクをご覧ください：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前
        - このキットに含まれるアイテム
        - リンク
    *   - Pico 2 W Starter Kit
        - 450+
        - |link_pico2w_kit|

下記のリンクからも個別に購入できます。


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
        - 
    *   - 9
        - :ref:`cpn_photoresistor`
        - 1
        - |link_photoresistor_buy|

**コンセプトの理解**

* **フォトレジスタ**：光の強度に基づいて抵抗が変化するセンサー。光が強いと抵抗は減少し、光が弱いと増加します。
* **パッシブブザー**：外部信号を使用して音を鳴らします。PWM（パルス幅変調）を使用してその周波数を制御できます。
* **トランジスタ（S8050）**：電流を増幅し、ピコから効率よくブザーを駆動できるようにします。

フォトレジスタの値を読み取ることで、光の強度を音の周波数にマッピングできます。手をフォトレジスタの上に移動させることで、ブザーから出る音のピッチが変わり、テルミンを演奏するような効果が得られます。

**回路図**

|sch_light_theremin|

プロジェクトを開始する前に、フォトレジスタの上に手を上下に動かして光の強度の範囲をキャリブレーションします。GP16に接続されたLEDはデバッグ時間を示し、LEDが点灯するとデバッグが開始され、消灯するとデバッグが終了します。

GP15が高レベルを出力すると、S8050（NPNトランジスタ）が導通し、パッシブブザーが鳴り始めます。

光が強いと、GP28の値は小さくなり、光が弱いと値は大きくなります。
フォトレジスタの値をプログラムして、パッシブブザーの周波数に影響を与えることで、光感知デバイスをシミュレートできます。

**配線**

|wiring_light_theremin|

**コードの作成**

光の強度をフォトレジスタから読み取り、それを周波数にマッピングして、その周波数をブザーで鳴らすMicroPythonプログラムを作成します。

.. note::

    * ``pico-2w-kit-main/micropython`` 内の ``7.1_light_theremin.py`` を開くか、このコードをThonnyにコピーして、「現在のスクリプトを実行」するか、F5を押して実行してください。
    * Thonnyで「MicroPython（Raspberry Pi Pico）。COMxx」が選択されていることを確認してください。

.. code-block:: python

    import machine
    import utime

    # コンポーネントの初期化
    led = machine.Pin(16, machine.Pin.OUT)  # GP16のLED
    photoresistor = machine.ADC(28)         # GP28に接続されたフォトレジスタ
    buzzer = machine.PWM(machine.Pin(15))   # GP15に接続されたブザー

    # キャリブレーション用変数
    light_low = 65535
    light_high = 0

    # 値を1つの範囲から別の範囲にマッピングする関数
    def interval_mapping(x, in_min, in_max, out_min, out_max):
        # in_min != in_maxを確認してゼロ除算を避ける
        if in_max - in_min == 0:
            return out_min
        return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

    # ブザーで音を鳴らす関数
    def play_tone(pin, frequency):
        if frequency <= 0:
            pin.duty_u16(0)
        else:
            pin.freq(frequency)
            pin.duty_u16(32768)  # 50%のデューティサイクル

    # キャリブレーションプロセス
    def calibrate():
        global light_low, light_high
        print("Calibrating... Move your hand over the sensor.")
        led.value(1)  # キャリブレーション中であることを示すためLEDを点灯
        start_time = utime.ticks_ms()
        while utime.ticks_diff(utime.ticks_ms(), start_time) < 5000:  # 5秒間のキャリブレーション
            light_value = photoresistor.read_u16()
            if light_value > light_high:
                light_high = light_value
            if light_value < light_low:
                light_low = light_value
            utime.sleep_ms(10)
        led.value(0)  # キャリブレーション後にLEDを消灯
        print("Calibration complete.")
        print("Light Low:", light_low)
        print("Light High:", light_high)

    # メイン関数
    def main():
        calibrate()
        try:
            while True:
                light_value = photoresistor.read_u16()
                # 光の値を周波数範囲（例：200Hz〜2000Hz）にマッピング
                frequency = interval_mapping(light_value, light_low, light_high, 200, 2000)
                play_tone(buzzer, frequency)
                utime.sleep_ms(20)
        except KeyboardInterrupt:
            buzzer.deinit()
            print("Program stopped.")

    # メイン関数の実行
    if __name__ == "__main__":
        main()

コードが実行されると、LEDが点灯し、キャリブレーション期間を示します。

* キャリブレーション:

  * 5秒間のキャリブレーション中に、フォトレジスタの上に手を動かしてください。
  * これにより、プログラムが光の条件の範囲を理解するのに役立ちます。

* テルミンの演奏:

  * キャリブレーション後、LEDが消灯します。
  * フォトレジスタの上に手を動かしてください。
  * ブザーが光の強度に基づいて音の高さを変えて音を出します。
  * 異なる手の位置や動きで音を作る実験をしてみてください。


**コードの理解**

1. 初期化:

   * **LEDインジケーター**: キャリブレーションが行われていることを示すために使用します。
   * **フォトレジスタ**: 光の強度に対応するアナログ値を読み取ります。
   * **ブザー**: PWMを使用して、異なる周波数の音を生成します。

2. キャリブレーション関数（ ``calibrate()`` ）:

   * 5秒間実行され、その間に最小および最大の光値を記録します。
   * ユーザーにセンサーの上で手を動かして範囲を取得するよう指示します。
   * LEDを視覚的なインジケーターとして使用します。

   .. code-block:: python

        # キャリブレーションプロセス
        def calibrate():
            global light_low, light_high
            print("Calibrating... Move your hand over the sensor.")
            led.value(1)  # キャリブレーション中であることを示すLEDの点灯
            start_time = utime.ticks_ms()
            while utime.ticks_diff(utime.ticks_ms(), start_time) < 5000:  # 5秒間のキャリブレーション
                light_value = photoresistor.read_u16()
                if light_value > light_high:
                    light_high = light_value
                if light_value < light_low:
                    light_low = light_value
                utime.sleep_ms(10)
            led.value(0)  # キャリブレーション後にLEDを消灯
            print("Calibration complete.")
            print("Light Low:", light_low)
            print("Light High:", light_high)

3. インターバルマッピング関数（ ``interval_mapping()`` ）:

   * フォトセンサーの値をブザーに適した周波数範囲にマッピングします。
   * ゼロ除算エラーを防止します。

   .. code-block:: python

        # 1つの範囲から別の範囲に値をマッピングする関数
        def interval_mapping(x, in_min, in_max, out_min, out_max):
            # in_min != in_maxを確認してゼロ除算を防ぐ
            if in_max - in_min == 0:
                return out_min
            return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

4. 音の再生（ ``play_tone()`` ）:

   * PWMを使用してブザーの周波数を設定します。
   * 周波数がゼロまたは負の場合、ブザーをオフにします。

   .. code-block:: python

        # ブザーで音を鳴らす関数
        def play_tone(pin, frequency):
            if frequency <= 0:
                pin.duty_u16(0)
            else:
                pin.freq(frequency)
                pin.duty_u16(32768)  # 50%のデューティサイクル
                
5. メインループ:

   * フォトレジスタから光の値を継続的に読み取ります。
   * この値を周波数にマッピングします。
   * マッピングした周波数に対応する音を再生します。
   * 終了時にエラーハンドリングを行い、クリーンアップします。

   .. code-block:: python

        # メイン関数
        def main():
            calibrate()
            try:
                while True:
                    light_value = photoresistor.read_u16()
                    # 光の値を周波数範囲（例：200Hz〜2000Hz）にマッピング
                    frequency = interval_mapping(light_value, light_low, light_high, 200, 2000)
                    play_tone(buzzer, frequency)
                    utime.sleep_ms(20)
            except KeyboardInterrupt:
                buzzer.deinit()
                print("Program stopped.")

**さらなる実験**

* 周波数範囲の調整：

  ``interval_mapping()`` の値を変更して、ピッチ範囲を変更できます。例：200、2000を100、5000に変更して、より広い範囲を作成します。

* 視覚的フィードバック：

  追加のLEDを使用して、ピッチに対応する視覚的な手がかりを提供します。

* センサーの追加：

  もう1つのフォトレジスタを追加して、音量や他のパラメータを制御します。

* 音楽楽器の作成：

  他のセンサーや入力を組み合わせて、より複雑な楽器を作成します。

**制限事項の理解**

* 周囲の光：

  周囲の光の変化がパフォーマンスに影響を与える可能性があります。一貫した照明を確保するか、必要に応じて再キャリブレーションを行ってください。

* センサーの感度：

  フォトレジスタは素早い手の動きに素早く反応しない場合があります。

* 音質：

  パッシブブザーは音質に限界があります。より良い音質を求める場合は、DAC出力を持つアクティブスピーカーを使用してください。

**結論**

Raspberry Pi Pico 2 Wを使用して、ライト・テルミンを作成することに成功しました！このプロジェクトは、センサーとアクチュエーターを組み合わせてインタラクティブで楽しい実験を作成する方法を示しています。プロジェクトをさらに探求し、修正することで、理解と創造力を深めていきましょう。
