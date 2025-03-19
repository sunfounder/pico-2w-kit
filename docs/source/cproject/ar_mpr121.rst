.. note::

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Raspberry Pi、Arduino、ESP32について、他の愛好者とともにさらに深く学びましょう。

    **なぜ参加するのか？**

    - **専門家のサポート**: コミュニティやチームのサポートを受けて、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**: スキルを向上させるためのヒントやチュートリアルを交換できます。
    - **独占的なプレビュー**: 新製品の発表や先取り情報をいち早くチェックできます。
    - **特別割引**: 最新製品に対する独占的な割引を楽しめます。
    - **祭事プロモーションとプレゼント**: ギブアウェイや休日のプロモーションに参加できます。

    👉 一緒に探求し、創造しませんか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _ar_mpr121:

4.3 MPR121を使った電極キーボード
========================================================

このレッスンでは、 **MPR121静電容量式タッチセンサー** を使用して、Raspberry Pi Pico 2 Wでタッチセンサー付きのキーボードを作成する方法を学びます。MPR121は最大12個の電極にタッチ入力を検出でき、ワイヤー、アルミ箔、さらにはバナナのような果物にも接続できます！

* :ref:`cpn_mpr121`

**必要な部品**

このプロジェクトには、以下の部品が必要です。

全体キットを購入するのが非常に便利です。リンクはこちらです：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前
        - このキットに含まれるアイテム
        - 購入リンク
    *   - Pico 2 W スターターキット
        - 450以上
        - |link_pico2w_kit|

以下のリンクから個別に購入することもできます。

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - 部品紹介
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
        - 数本
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_mpr121`
        - 1
        - 

**MPR121センサーの理解**

**MPR121** は、I2Cインターフェースを介して通信する静電容量式タッチセンサーコントローラです。最大12個のタッチ入力を扱うことができ、複数のタッチポイントを使ったインタラクティブなプロジェクトの作成に最適です。

MPR121センサーは、電極における容量の変化を検出します。電極を触ると容量が変化し、センサーがタッチを登録します。その情報はI2Cを通じてRaspberry Pi Pico 2に送信されます。

**回路図**

|sch_mpr121_ar|

**配線**

|wiring_mpr121_ar|

* MPR121の電極ピン（ **E0** から **E11** ）にワイヤーまたは導電材料を接続します。
* ワイヤーのもう一方の端を、果物、アルミ箔の形、またはタッチパッドなどの導電物体に接続できます。

**コードの記述**

.. note::

    * 「 ``4.3_electrode_keyboard.ino`` 」ファイルを「 ``pico-2w-kit-main/arduino/4.3_electrode_keyboard`` 」のパスで開きます。
    * または、このコードを **Arduino IDE** にコピーしてください。
    * アップロードボタンをクリックする前に、Raspberry Pi Picoボードと正しいポートを選択してください。
    * ここでは ``Adafruit MPR121`` ライブラリを使用しています。 **ライブラリマネージャ** からインストールできます。


      .. image:: img/lib_mpr121.png

.. code-block:: arduino

    #include <Wire.h>
    #include <Adafruit_MPR121.h>

    // MPR121センサーのインスタンスを作成
    Adafruit_MPR121 cap = Adafruit_MPR121();

    // 各電極のタッチ状態を保持する配列
    bool touchStates[12] = { false };

    // 現在のタッチ状態と前回のタッチ状態を保存する変数
    uint16_t currtouched = 0;
    uint16_t lasttouched = 0;

    void setup() {
      Serial.begin(115200); // シリアル通信を115200ボーレートで初期化
      while (!Serial);    // シリアルモニターのオープンを待機

      // MPR121センサーをI2Cアドレス0x5Aで初期化
      if (!cap.begin(0x5A)) {
        Serial.println("MPR121 not found, check wiring?");
        while (1);
      }
      Serial.println("MPR121 found!");
    }

    void loop() {
      // 現在のタッチされたパッドを取得
      currtouched = cap.touched();

      // タッチ状態に変更があったか確認
      if (currtouched != lasttouched) {
        // 最後のタッチ状態を更新
        lasttouched = currtouched;

        // 各電極をチェック
        for (int i = 0; i < 12; i++) {
          // 電極がタッチされたか確認
          if (currtouched & (1 << i)) {
            touchStates[i] = true;
          } else {
            touchStates[i] = false;
          }
        }

        // タッチ状態を2進数で表示
        for (int i = 0; i < 12; i++) {
          Serial.print(touchStates[i] ? "1" : "0");
        }
        Serial.println();
      }

      delay(100); // 読み取りの安定化のための短い遅延
    }

コードをアップロードした後、MPR121センサーに接続された電極を触れてください。

* シリアルモニターで、どの電極が触れられたかを示す2進数の出力を観察します。
* 例えば、最初と11番目の電極を触れると、 ``100000000010`` が表示されます。

**コードの理解**

#. ライブラリのインクルード：

   * ``Wire.h``: I2C通信を処理します。
   * ``Adafruit_MPR121.h``: MPR121センサーとやり取りするための関数を提供します。

#. MPR121センサーの初期化：

   MPR121センサーのインスタンスを作成します。

   .. code-block:: arduino

      Adafruit_MPR121 cap = Adafruit_MPR121();

#. Setup Function:

   * デバッグのためにシリアル通信を開始します。
   * I2Cアドレス0x5AでMPR121センサーを初期化します。
   * センサーが見つからない場合、エラーメッセージを表示し、プログラムを停止します。

   .. code-block:: arduino

      void setup() {
        Serial.begin(115200); // シリアル通信を初期化
        while (!Serial);    // シリアルモニターのオープンを待機

        // MPR121センサーをI2Cアドレス0x5Aで初期化
        if (!cap.begin(0x5A)) {
          Serial.println("MPR121 not found, check wiring?");
          while (1);
        }
        Serial.println("MPR121 found!");
      }

#. ``loop()`` Function: 

   * MPR121センサーから現在のタッチ状態を取得します。 ``currtouched`` の各ビットは、電極のタッチ状態（1はタッチされている、0はタッチされていない）を表します。

     .. code-block:: arduino
  
        currtouched = cap.touched();

   * 前回のループからタッチ状態に変更があったかを確認します。

     .. code-block:: arduino

        if (currtouched != lasttouched) {
          // タッチ状態を更新
        }

   * 各電極を繰り返し確認し、 ``touchStates`` 配列を更新します。

     .. code-block:: arduino

        for (int i = 0; i < 12; i++) {
          if (currtouched & (1 << i)) {
            touchStates[i] = true;
          } else {
            touchStates[i] = false;
          }
        }

   * タッチ状態を12ビットの2進数としてシリアルモニターに表示します。例えば、最初と11番目の電極がタッチされていると、 100000000010が表示されます。

     .. code-block:: arduino

        for (int i = 0; i < 12; i++) {
          Serial.print(touchStates[i] ? "1" : "0");
        }
        Serial.println();

   * 読み取りの安定化とシリアルモニターの洪水を防ぐため、短い遅延を入れます。

     .. code-block:: arduino

        delay(100);

**電極の拡張**

プロジェクトを拡張して、さまざまな導電材料に電極を接続できます：

* **果物**: バナナ、リンゴ、その他の果物にワイヤーを接続してタッチ入力に変えることができます。
* **アルミ箔の形**: アルミ箔を切って形を作り、電極に接続します。
* **導電インク**: 導電インクやペイントでパターンを描きます。

.. note::

    電極を変更した場合（例：異なる材料を接続した場合）、センサーをリセットして基準値を再調整する必要がある場合があります。

**さらなる探索**

* インタラクティブプロジェクトの作成：

  各電極が個別のLEDを制御するタッチ制御LEDマトリックスを作成します。

* キーデバウンスの実装：

  不正確なタッチをフィルタリングするために、デバウンス技術を使ってタッチ検出の信頼性を高めます。

* 他のセンサーとの統合：

  MPR121を温度センサーや光センサーと組み合わせて、より複雑なインタラクティブシステムを作成します。

* タッチベースのゲームコントローラーの開発：

  タッチ入力を使ってキャラクターを動かしたりオプションを選択したりするゲーム要素を制御します。

**結論**

このレッスンでは、Raspberry Pi Picoを使用してMPR121静電容量式タッチセンサーを利用し、タッチ入力に反応するキーボードを作成する方法を学びました。複数の電極にタッチ入力を検出することにより、カスタムキーパッド、コントロールパネル、創造的な入力デバイスなど、インタラクティブなインターフェースを作成できます。タッチ入力の読み取りと処理方法を理解することは、反応の良いユーザーフレンドリーな電子機器プロジェクトを開発するために重要なスキルです。
