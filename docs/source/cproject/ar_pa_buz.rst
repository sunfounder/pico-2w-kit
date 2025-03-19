.. note::

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Raspberry Pi、Arduino、ESP32について、同じ趣味を持つ人たちとさらに深く掘り下げましょう。

    **参加する理由は？**

    - **専門家によるサポート**: 販売後の問題や技術的な課題をコミュニティやチームの助けを借りて解決します。
    - **学びと共有**: スキル向上のためのヒントやチュートリアルを交換します。
    - **独占的なプレビュー**: 新製品の発表や先行プレビューに早期アクセスが可能です。
    - **特別割引**: 最新製品の独占的な割引を楽しむことができます。
    - **祭りのプロモーションとギフト**: ギフトや祝日のプロモーションに参加しましょう。

    👉 一緒に探索し、創造してみませんか？こちらのリンク [|link_sf_facebook|] から今すぐ参加！

.. _ar_pa_buz:


3.2 パッシブブザーでカスタムトーンを再生する
===============================================

このレッスンでは、Raspberry Pi Pico 2 Wを使用して、 **パッシブブザー** でさまざまなトーンや単純なメロディを再生する方法を学びます！アクティブブザーとは異なり、パッシブブザーは変化する電気信号を必要として音を生じさせるため、信号の周波数を変更することで音のピッチを制御できます。

* :ref:`cpn_buzzer`

**必要なコンポーネント**

このプロジェクトには以下のコンポーネントが必要です。

キット全体を購入することは確かに便利です。こちらがリンクです:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前	
        - このキットのアイテム
        - 購入リンク
    *   - Pico 2 W スターターキット	
        - 450+
        - |link_pico2w_kit|

それぞれの部品を以下のリンクから個別に購入することもできます。


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
        - Passive :ref:`cpn_buzzer`
        - 1
        - |link_passive_buzzer_buy|

**パッシブブザーの理解**

パッシブブザーは小さなスピーカーのように動作します。それ自体では音を出さず、振動する信号が必要です。異なる周波数の信号を提供することで、ブザーに異なるピッチの音を出させ、音符やメロディを再生させることができます。

|img_buzzer|

**回路図**

|sch_buzzer|

この回路では、パッシブブザーはトランジスタ（ **S8050** NPN）を通じて電力を供給されます。トランジスタは電流を増幅し、Picoに直接接続されている場合よりもブザーの音を大きくします。

こうなります:

* **GP15** が高い信号を出力してトランジスタを制御します。
* トランジスタが作動すると、ブザーを鳴らすために電流が流れます。

トランジスタを保護するために **1kΩの抵抗** が使用されます。

**配線**

|img_buzzer|

**パッシブブザー** を使用していることを確認してください。裏面が封印されていないPCBが露出しているものが正しいブザーです。

|wiring_buzzer|

**コードの記述**


.. note::

    * ``3.2_custom_tone.ino`` ファイルを ``pico-2w-kit-main/arduino/3.2_custom_tone`` パスの下で開くことができます。
    * または、このコードを **Arduino IDE** にコピーします。
    * **Upload** ボタンをクリックする前に、ボード（Raspberry Pi Pico）と正しいポートを選択することを忘れないでください。
    



.. code-block:: arduino

    const int buzzerPin = 15;  // トランジスタのベースに接続されているGPIOピン

    void setup() {
      pinMode(buzzerPin, OUTPUT);
    }

    void loop() {
      // 440 Hz（A4の音符）で1秒間トーンを鳴らす
      tone(buzzerPin, 440, 1000);
      delay(1000);  // トーンが終わるのを待つ
      // 再び演奏する前に1秒間待つ
      delay(1000);
    }

このコードは、1秒間440 Hzのトーン（標準のAノート）を再生し、1秒間待って繰り返します。

* ``tone(pin, frequency, duration)``:

  * ``pin``: ブザーに接続されたGPIOピン（トランジスタを介して）。
  * ``frequency``: トーンの周波数（Hz単位）。周波数が高いほどピッチが高くなります。
  * ``duration (任意)``: トーンを再生する時間（ミリ秒単位）。

**メロディの演奏**

コードを拡張して、単純なメロディを演奏することができます。メロディのノートとそれに対応する周波数を定義します。

* 配列 ``melody[]`` には、演奏するノートのシーケンスが保持されています。
* 配列 ``noteDurations[]`` は、各ノートの持続時間を定義します。持続時間4は四分音符を表します。
* ``for`` ループはメロディの各ノートを反復処理します。

  * ノートの持続時間をミリ秒で計算します。
  * ``tone()`` を使用して各ノートを演奏します。
  * ノート間の一時停止に ``delay()`` を使用します。
  * 次のノートに移る前に ``noTone()`` でトーンを停止します。

.. code-block:: arduino

        // ブザーピンを定義する
        const int buzzerPin = 15;

        // ノート周波数を定義する
        #define NOTE_C4  262
        #define NOTE_D4  294
        #define NOTE_E4  330
        #define NOTE_F4  349
        #define NOTE_G4  392
        #define NOTE_A4  440
        #define NOTE_B4  494
        #define NOTE_C5  523

        // メロディノート
        int melody[] = {
          NOTE_C4, NOTE_D4, NOTE_E4, NOTE_F4,
          NOTE_G4, NOTE_A4, NOTE_B4, NOTE_C5
        };

        // ノートの持続時間：4 = 四分音符、8 = 八分音符など
        int noteDurations[] = {
          4, 4, 4, 4,
          4, 4, 4, 4
        };

        void setup() {
          pinMode(buzzerPin, OUTPUT);
        }

        void loop() {
          // メロディのノートを順に演奏する
          for (int thisNote = 0; thisNote < 8; thisNote++) {
            int noteDuration = 1000 / noteDurations[thisNote];
            tone(buzzerPin, melody[thisNote], noteDuration);
            // ノート間の一時停止
            int pauseBetweenNotes = noteDuration * 1.30;
            delay(pauseBetweenNotes);
            // トーンの再生を停止する
            noTone(buzzerPin);
          }
          // メロディを繰り返す前に遅延を加える
          delay(2000);
        }

コードをアップロードした後、ブザーがメロディを演奏するのが聞こえるはずです。音が小さい場合は、すべての接続が確実であることを確認してください。パッシブブザーは非常に大きな音を出さないことがあります。


**詳細学習**

* 独自のメロディの作成：

  ``melody[]`` および ``noteDurations[]`` 配列を変更することで、独自のメロディを作成できます。

* ``pitches.h`` ライブラリの使用：

  便宜上、多くのノートの定義を含む ``pitches.h`` というライブラリファイルを含めることができます。
  ``pitches.h`` というファイルを作成し、スケッチに含めます。

  .. code-block:: arduino

    #include "pitches.h"

**さらなる探求**

* 自作の曲を作曲する：

  新しいノートと持続時間のシーケンスを定義して、自分だけの曲を作曲してみましょう。

* インタラクティブな音楽：

  ボタンやセンサーを追加して、メロディの再生を制御します。

* 視覚的フィードバック：

  演奏されたノートと同期して点灯するLEDを統合します。

**まとめ**

このレッスンでは、Raspberry Pi Picoを使用してパッシブブザーで異なるトーンとメロディを演奏する方法を学びました。ブザーに送信される信号の周波数を制御することで、さまざまなピッチを生成し、プロジェクトに音楽を作成することができます。




