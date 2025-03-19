.. note:: 

    こんにちは！FacebookのSunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Raspberry Pi、Arduino、ESP32を他の愛好者と一緒に深く学びましょう。

    **参加する理由は？**

    - **専門的なサポート**: 購入後の問題や技術的な課題をコミュニティやチームの助けを借りて解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換し、スキルを向上させましょう。
    - **限定プレビュー**: 新製品の発表や先行公開をいち早くチェックできます。
    - **特別割引**: 新しい製品に対して独占的な割引を楽しめます。
    - **祭典のプロモーションやプレゼント**: プレゼントや祝日プロモーションに参加しましょう。

    👉 一緒に探求し、創造を楽しむ準備はできましたか？[|link_sf_facebook|]をクリックして、今日から参加しましょう！

.. _ar_reed:

2.9 磁気を感じる
===============================

このレッスンでは、 **reedスイッチ** を使用してRaspberry Pi Pico 2 Wで磁場の存在を検出する方法を学びます。reedスイッチは、磁場を利用して動作するシンプルな電気スイッチです。磁石がスイッチの近くに来ると、その内部の接点が閉じ、電気回路が完成します。

* :ref:`cpn_reed`

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
        - 1（10KΩ）
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_reed`
        - 1
        - 

**reedスイッチの理解**

reedスイッチは、2本の細い金属のリードがガラスのカプセル内に密閉されている構造をしています。これらのリードはフェロ磁性材料でできており、少し離れて配置されています。磁場がない場合、リードは分離されており、スイッチは **開いています** 。磁石が近づくと、リードが磁化され、互いに引き寄せられて回路を閉じます。

* **磁石が近くにない場合**: スイッチは **開いています** 。回路は不完全です。
* **磁石が近くにある場合**: スイッチは **閉じています** 。回路は完了しています。

|img_reed_sche|

**回路図**

|sch_reed|

デフォルトでは、GP14は低く、reedスイッチの近くに磁石があると高くなります。

10KΩの抵抗の目的は、磁石が近くにない場合でもGP14を安定して低い状態に保つことです。

* **磁石が近くにない場合**:

  * reedスイッチは **開いています** 。
  * **GP14** はプルダウン抵抗を介して **GND** に接続されています。
  * GPIOピンは **LOW** （0）を読み取ります。

* **磁石が近くにある場合**:

  * reedスイッチは **閉じています** 。
  * **GP14** はreedスイッチを介して **3.3V** に接続されています。
  * GPIOピンは **HIGH** （1）を読み取ります。

**配線**

|wiring_reed|

**コード**

.. note::

    * ``pico-2w-kit-main/arduino/2.9_feel_the_magnetism`` 内の ``2.9_feel_the_magnetism.ino`` ファイルを開きます。
    * または、このコードを **Arduino IDE** にコピーします。
    * アップロードボタンをクリックする前に、ボード（Raspberry Pi Pico）と適切なポートを選択するのを忘れないでください。

.. code-block:: Arduino


   const int reedPin = 14;    // reedスイッチに接続されているGPIOピン
   int reedState = 0;

   void setup() {
     Serial.begin(115200);       // シリアルモニタを115200ボーレートで初期化
     pinMode(reedPin, INPUT);    // reedピンを入力モードに設定
   }

   void loop() {
     reedState = digitalRead(reedPin);  // reedスイッチの状態を読み取る

     if (reedState == HIGH) {
       Serial.println("Magnet Detected!");
     } else {
       Serial.println("No Magnet.");
     }
     delay(500);  // シリアルモニタが溢れないように遅延
   }

コードが実行され、シリアルモニタが開いているとき：

* **磁石が近くにない場合**: シリアルモニタに「磁石はありません。」と表示されます。
* **磁石が近くにある場合**: reedスイッチの近くに磁石を持っていくと、シリアルモニタに「磁石が検出されました！」と表示されます。

**コードの理解**

#. シリアル通信の初期化:

   115200のボーレートでシリアル通信を開始します。これにより、シリアルモニタにメッセージを表示できます。

   .. code-block:: Arduino

        Serial.begin(115200);

#. reedピンの設定:
 
   reedPin（GP14）を入力として設定し、reedスイッチの状態を読み取ります。

   .. code-block:: Arduino

        pinMode(reedPin, INPUT);

#. reedスイッチの状態を読み取る:

   reedスイッチの現在の状態を読み取ります。磁石が近いとHIGH、磁石がないとLOWになります。

   .. code-block:: Arduino

        reedState = digitalRead(reedPin);

#. 磁石の存在に応じた反応:

   磁石が近くにあるかどうかに応じてメッセージを表示します。

   .. code-block:: Arduino

        if (reedState == HIGH) {
          Serial.println("Magnet Detected!");
        } else {
          Serial.println("No Magnet.");
        }


**学ぶ：reedスイッチと割り込みの使用**

* **割り込みの紹介**

  本を読んでいるとき、誰かが肩を叩いて質問をしてきたとしましょう。あなたは一時的に本を中断し、その質問に答えてから本に戻ります。この中断のように、割り込みはマイクロコントローラで重要なイベントが発生したときに即座に反応できるようにするものです。
  
  割り込みを使用すると、プログラムのメインの流れを一時停止して、割り込みサービスルーチン（ISR）という特別な関数を実行できます。その後、プログラムは中断したところから再開します。

* **割り込みを使用する理由**

  reedスイッチに割り込みを使うことで、マグネットが検出されたときにマイクロコントローラが即座に反応し、 ``loop()`` 関数で reedスイッチを繰り返し確認する必要がなくなります。これにより効率が良くなり、バッテリー駆動のアプリケーションでは省電力にもなります。

* **割り込みを使用したコードの記述**

  プログラムを変更して、磁石の検出に割り込みを使用するようにします。

  .. code-block:: Arduino

        const int reedPin = 14;            // reedスイッチに接続されているGPIOピン
        volatile bool magnetDetected = false;  // 磁石が検出されたかを示すフラグ

        void setup() {
          Serial.begin(115200);               // シリアルモニタを初期化
          pinMode(reedPin, INPUT);            // reedピンを入力モードに設定
          attachInterrupt(digitalPinToInterrupt(reedPin), onMagnetChange, CHANGE);  // 変更があった時に割り込みを設定
        }

        void loop() {
          if (magnetDetected) {
            Serial.println("Magnet Present!");
          } else {
            Serial.println("Waiting for magnet...");
          }
          delay(1000);                         // シリアルモニタが溢れないように遅延
        }

        void onMagnetChange() {
          // reedピンの現在の状態に基づいてフラグを更新
          magnetDetected = digitalRead(reedPin) == HIGH;  // HIGHなら磁石が存在、LOWなら磁石がない
        }


  .. code-block:: Arduino

        attachInterrupt(digitalPinToInterrupt(reedPin), onMagnetChange, CHANGE);
    
  * ``digitalPinToInterrupt(reedPin)``: ピン番号を適切な割り込み番号に変換します。
  * ``onMagnetChange``: 割り込みが発生したときに呼び出されるISR関数の名前です。
  * ``CHANGE``: ピンの状態が変化したときに割り込みがトリガーされます。

**結論**

このレッスンでは、Raspberry Pi Picoでreedスイッチを使用して磁場の存在を検出する方法を学びました。また、割り込みを使用してプログラムを効率的にし、センサーをメインループで常にチェックすることなく即座に反応する方法を学びました。割り込みを使用する技術は組み込みプログラミングにおいて非常に価値のあるスキルであり、より応答性の高い効率的なアプリケーションを作成することができます。

**さらなる探求**

* **ドアセンサー**: reedスイッチを使って、ドアが開いたときにトリガーされるシンプルなドアアラームを作成します。
* **回転数のカウント**: 回転する物体に磁石を取り付け、reedスイッチで回転数（RPM）をカウントします。
* **セキュリティシステム**: 複数のreedスイッチを組み合わせて、セキュリティシステムで窓やドアを監視します。

**追加リソース**

* `attachInterrupt() - Arduino Reference <https://www.arduino.cc/reference/en/language/functions/external-interrupts/attachinterrupt/>`_


