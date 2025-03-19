.. note:: 

    こんにちは、FacebookでSunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Raspberry Pi、Arduino、ESP32の深い探求を仲間と共に楽しみましょう。

    **なぜ参加するのか？**

    - **専門的なサポート**: コミュニティやチームからの助けを借りて、購入後の問題や技術的な挑戦を解決します。
    - **学びと共有**: ヒントやチュートリアルを交換して、技術を磨きましょう。
    - **独占的なプレビュー**: 新製品の発表や先取り情報を早期にアクセスしましょう。
    - **特別割引**: 最新製品の独占的な割引を楽しみましょう。
    - **祭りのプロモーションとギブアウェイ**: ギブアウェイや祝祭のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造しませんか？[|link_sf_facebook|]をクリックして、今日参加しましょう！

.. _py_pa_buz:

3.2 パッシブブザーでカスタムトーンを再生
==============================================


このレッスンでは、Raspberry Pi Pico 2 Wを使用して **パッシブブザー** で異なるトーンや簡単なメロディーを再生する方法を学びます！アクティブブザーとは異なり、パッシブブザーは音を生成するために変化する電気信号を必要とし、信号の周波数を変えることで音のピッチを制御できます。


* :ref:`cpn_buzzer`

**必要な部品**

このプロジェクトに必要な部品は以下の通りです。

全ての部品がセットになったキットを購入するのが便利です。こちらのリンクをご覧ください：

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
        - 数本
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_transistor`
        - 1(S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_resistor`
        - 1(1KΩ)
        - |link_resistor_buy|
    *   - 7
        - パッシブ :ref:`cpn_buzzer`
        - 1
        - |link_passive_buzzer_buy|

**パッシブブザーの理解**

パッシブブザーは小型スピーカーのように機能します。自身で音を発することはなく、音を出すためには振動する信号が必要です。異なる周波数の信号を提供することで、ブザーから異なるピッチの音を出すことができ、音符やメロディーを演奏できます。

|img_buzzer|

**回路図**

|sch_buzzer|

この回路では、パッシブブザーはトランジスタ（ **S8050** NPN）を通じて電源が供給されます。トランジスタは電流を増幅し、Picoに直接接続されている場合よりもブザーの音を大きくします。

ここでの流れは以下の通りです：

* **GP15** が高信号を出力してトランジスタを制御します。
* トランジスタが作動すると、ブザーを通じて電流が流れ、ブザーが鳴ります。

**1kΩの抵抗** は、トランジスタを保護するために電流を制限します。

**配線図**

**パッシブブザー** を使用していることを確認してください。裸のPCBが見えるものが正しいブザーです（アクティブブザーは裏面が封印されています）。

|img_buzzer|

|wiring_buzzer|


.. 1. Connect 3V3 and GND of Pico 2 W to the power bus of the breadboard.
.. #. Connect the positive pin of the buzzer to the positive power bus.
.. #. Connect the cathode pin of the buzzer to the **collector** lead of the transistor.
.. #. Connect the **base** lead of the transistor to the GP15 pin through a 1kΩ resistor.
.. #. Connect the **emitter** lead of the transistor to the negative power bus.


**コードの記述**

それでは、異なるトーンを再生するためのコードを書いてみましょう。

.. note::

    * ``pico-2w-kit-main/micropython`` から ``3.2_custom_tone.py`` を開くか、コードをThonnyにコピーして、「実行」をクリックするか、F5を押します。
    * 正しいインタープリターが選択されていることを確認してください：MicroPython（Raspberry Pi Pico）.COMxx。


.. code-block:: python

   import machine
   import utime

   # GP15でPWMを初期化
   buzzer = machine.PWM(machine.Pin(15))

   def play_tone(frequency, duration):
       # PWM信号の周波数を設定
       buzzer.freq(frequency)
       # デューティサイクルを50%に設定
       buzzer.duty_u16(32768)
       # 指定された期間でトーンを再生
       utime.sleep_ms(duration)
       # ブザーをオフにする
       buzzer.duty_u16(0)

   # いくつかのトーンを再生
   play_tone(440, 500)  # 500msのA4ノート
   utime.sleep_ms(200)
   play_tone(494, 500)  # 500msのB4ノート
   utime.sleep_ms(200)
   play_tone(523, 500)  # 500msのC5ノート

このコードが実行されると、パッシブブザーはそれぞれ500ミリ秒でA4、B4、C5の音符を演奏します。
コードを実行すると、パッシブブザーがそれぞれ500ms間、A4ノート、B4ノート、C5ノートを再生します。


**コードの説明**

#. PWMの初期化：

   * ``buzzer = machine.PWM(machine.Pin(15))``: これにより、GP15ピンでPWM（パルス幅変調）を設定し、ブザーの制御に使用します。

#. ``play_tone`` 関数の定義：

   .. code-block:: python

      def play_tone(frequency, duration):
          buzzer.freq(frequency)
          buzzer.duty_u16(32768)
          utime.sleep_ms(duration)
          buzzer.duty_u16(0)

   * ``frequency``: 音の高さ（周波数）。周波数が高いほど音程が高くなります。
   * ``duration``: トーンの再生時間（ミリ秒単位）。
   * ``buzzer.duty_u16(32768)``: デューティサイクルを50%に設定（65535の半分）、音を出すのに最適です。
   * 再生時間後、デューティサイクルを0に設定してブザーをオフにします。

#. ノートの再生：

   ``play_tone`` を呼び出し、異なる周波数の音符を再生します。

   .. code-block:: python

      # いくつかのトーンを再生
      play_tone(440, 500)  # A4ノートを500ms再生
      utime.sleep_ms(200)
      play_tone(494, 500)  # B4ノートを500ms再生
      utime.sleep_ms(200)
      play_tone(523, 500)  # C5ノートを500ms再生


**メロディーの再生**

パッシブブザーで個別のトーンを再生する方法を学んだので、次は簡単なメロディーを作成しましょう！これにより、ノートを並べ、音符の持続時間を制御して音楽を作る方法が理解できます。

.. code-block:: python

    import machine
    import utime

    # 音符の周波数（Hz）
    NOTE_C4 = 262
    NOTE_D4 = 294
    NOTE_E4 = 330
    NOTE_F4 = 349
    NOTE_G4 = 392
    NOTE_A4 = 440
    NOTE_B4 = 494
    NOTE_C5 = 523

    melody = [
        NOTE_C4, NOTE_D4, NOTE_E4, NOTE_F4,
        NOTE_G4, NOTE_A4, NOTE_B4, NOTE_C5
    ]

    note_durations = [
        500, 500, 500, 500,
        500, 500, 500, 500
    ]

    # GP15でPWMを初期化
    buzzer = machine.PWM(machine.Pin(15))

    def play_tone(frequency, duration):
        buzzer.freq(frequency)
        buzzer.duty_u16(32768)
        utime.sleep_ms(duration)
        buzzer.duty_u16(0)
        utime.sleep_ms(50)  # 音符間の短い休止

    for i in range(len(melody)):
        play_tone(melody[i], note_durations[i])

このコードを実行すると、ブザーはシーケンスの各音符を再生する簡単なメロディーを演奏します。各音符は500ミリ秒持続し、音符の間に短い休止があります。ブザーはミドルC（C4）から次のオクターブのC（C5）まで、上昇するスケールを再生します。

**さらに実験する**

* **自分だけのメロディーを作成する**: メロディーと ``note_durations`` リストの音符と持続時間を変更して、自分の曲を作成しましょう。
* **テンポを調整する**: ``note_durations`` の値を変更して、メロディーの速さを調整できます。
* **音符を追加する**: 音符の周波数を定義し、メロディーに追加して、より多くの音符を使ってみましょう。
* **音量を調整する**: ``buzzer.duty_u16()`` でデューティサイクルを調整し、ブザーの音量を大きくしたり小さくしたりできます。32768の値は50%のデューティサイクルです。

**結論**

このレッスンでは、Raspberry Pi Pico 2 Wを使ってパッシブブザーでトーンやメロディーを再生する方法を学びました。PWM信号の周波数を制御することで、さまざまな音を作り、シンプルな曲まで演奏できるようになります。これは、プロジェクトに音声フィードバックや楽しい音楽要素を加える素晴らしい方法です。
