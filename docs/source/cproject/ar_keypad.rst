.. note::

    こんにちは、FacebookでSunFounder Raspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32について、他の愛好者とさらに深く探求しましょう。

    **なぜ参加するのか？**

    - **エキスパートのサポート**: コミュニティとチームの助けを借りて、購入後の問題や技術的な課題を解決します。
    - **学びと共有**: 技術を向上させるためのヒントやチュートリアルを交換します。
    - **独占プレビュー**: 新製品の発表や先取り情報に早期アクセスが可能です。
    - **特別割引**: 最新製品に対する独占的な割引を楽しめます。
    - **祭事プロモーションとギブアウェイ**: ギブアウェイや休日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造しませんか？[|link_sf_facebook|]をクリックして、今日から参加しましょう！

.. _ar_keypad:

4.2 4x4キーパッドの使用
=================================================

このレッスンでは、 **4x4マトリックスキーパッド** をRaspberry Pi Pico 2 Wに接続して、どのキーが押されたかを検出する方法を学びます。マトリックスキーパッドは、計算機、電話、自動販売機、セキュリティシステムなどで数値入力用として一般的に使用されています。

* :ref:`cpn_keypad`


**必要な部品**

このプロジェクトには、以下の部品が必要です。

全体のキットを購入することは非常に便利です。こちらがリンクです：

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
        - コンポーネントの紹介
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
        - :ref:`cpn_resistor`
        - 4（10KΩ）
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_keypad`
        - 1
        - |link_keypad_buy|

**4x4キーパッドの理解**

4x4キーパッドは以下のように構成されています：

* **16個のキー** が4行4列に配置されています。
* **8本のピン**：4本が行に、4本が列に接続されています。

キーを押すと、特定の行と列が接続され、行と列の番号に基づいてキーを識別することができます。

キーの配置は以下の通りです：

|img_keypad|

**回路図**

|sch_keypad_ar|

キーボードの行（G2〜G5）は高い状態に設定されており、G6〜G9のどれかが高い状態として読み取られた場合、どのキーが押されたかを知ることができます。

たとえば、G6が高い状態で読み取られた場合、数字のキー1が押されたことになります。これは、数字キー1の制御ピンがG2とG6に接続されており、数字キー1が押されるとG2とG6が接続され、G6も高い状態になるからです。


**配線**

|wiring_keypad_ar|

**コードの書き方**

.. note::

    * ``4.2_4x4_keypad.ino`` ファイルを ``pico-2w-kit-main/arduino/4.2_4x4_keypad`` のパスで開くことができます。
    * または、このコードを **Arduino IDE** にコピーしてください。
    * アップロードボタンをクリックする前に、Raspberry Pi Picoボードと正しいポートを選択してください。
    * ここでは ``Adafruit Keypad`` ライブラリを使用しています。 **ライブラリマネージャー** からインストールできます。

      .. image:: img/lib_ad_keypad.png

.. code-block:: arduino

    #include "Adafruit_Keypad.h"

    // 行と列の数を定義
    const byte ROWS = 4;
    const byte COLS = 4;

    // キーパッドのキーマップを定義
    char keys[ROWS][COLS] = {
      { '1', '2', '3', 'A' },
      { '4', '5', '6', 'B' },
      { '7', '8', '9', 'C' },
      { '*', '0', '#', 'D' }
    };

    // キーパッドの行のピンアウトに接続
    byte rowPins[ROWS] = { 2, 3, 4, 5 };

    // キーパッドの列のピンアウトに接続
    byte colPins[COLS] = { 6, 7, 8, 9 };

    // Keypadオブジェクトを作成
    Adafruit_Keypad myKeypad = Adafruit_Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

    void setup() {
      // シリアル通信を初期化
      Serial.begin(115200);

      // キーパッドを初期化
      myKeypad.begin();
    }

    void loop() {
      // キーの状態を更新
      myKeypad.tick();

      // 新しいキーパッドイベントがあるかチェック
      while (myKeypad.available()) {
        // キーパッドイベントを読み取る
        keypadEvent e = myKeypad.read();

        // イベントがキー押下かどうかをチェック
        if (e.bit.EVENT == KEY_JUST_PRESSED) {
          // シリアルモニターにキー値を出力
          Serial.println((char)e.bit.KEY);
        }
      }

      delay(10); // 安定性を向上させるための短い遅延
    }

コードをアップロードした後、キーパッドの任意のキーを押します。対応するキーラベル（例えば「1」や「A」など）がシリアルモニターに表示されるはずです。

各キーの押下が正確に検出され、表示されていることを確認してください。すべてのキーをテストして、正常に動作することを確認しましょう。

**コードの理解**

#. ライブラリのインクルード：

   この行は、キーパッドとやり取りするための関数を提供するAdafruit Keypadライブラリをインクルードします。

   .. code-block:: arduino

      #include "Adafruit_Keypad.h"

#. キーパッドレイアウトの定義：

   ``ROWS`` と ``COLS`` は、キーパッドの行数と列数を定義します。 ``keys`` は、キーパッド上の各キーに対応するラベルを示す2D配列です。

   .. code-block:: arduino

      const byte ROWS = 4;
      const byte COLS = 4;

      char keys[ROWS][COLS] = {
        { '1', '2', '3', 'A' },
        { '4', '5', '6', 'B' },
        { '7', '8', '9', 'C' },
        { '*', '0', '#', 'D' }
      };

#. キーパッドをGPIOピンに接続：

   ``rowPins`` と ``colPins`` は、キーパッドの行と列に接続されたGPIOピンを格納する配列です。

   .. code-block:: arduino

      byte rowPins[ROWS] = { 2, 3, 4, 5 };
      byte colPins[COLS] = { 6, 7, 8, 9 };

#. キーパッドオブジェクトの初期化：

   この行では、 ``Adafruit_Keypad`` クラスのインスタンスを作成し、キーマップとピン設定で初期化します。

   .. code-block:: arduino

      Adafruit_Keypad myKeypad = Adafruit_Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

#. Setup Function:

   シリアル通信を初期化し、デバッグ用にキーパッドを開始します。

   .. code-block:: arduino

      void setup() {
        Serial.begin(115200);    // シリアル通信を115200ボーレートで初期化
        myKeypad.begin();        // キーパッドを初期化
      }

#. Loop Function:

   * キーイベントを継続的にチェックします。
   * キーが押されると、シリアルモニターにそのキーの値を表示します。

   .. code-block:: arduino

      void loop() {
        myKeypad.tick(); // キーの状態を更新

        while (myKeypad.available()) {
          keypadEvent e = myKeypad.read(); // キーパッドイベントを読み取る

          if (e.bit.EVENT == KEY_JUST_PRESSED) {
            Serial.println((char)e.bit.KEY); // 押されたキーを表示
          }
        }
        delay(10); // 安定性を向上させるための短い遅延
      }

**さらなる探索**

* キーデバウンスの実装：

  機械的なノイズによる誤動作を防ぐために、キーデバウンステクニックを実装してキー検出の信頼性を向上させます。

* パスワード入力システムの作成：

  キーパッドを使用してパスワードを入力し、プロジェクト内で特定の機能へのアクセスを制御します。

* 他のコンポーネントとの統合：

  キーパッドをLCDディスプレイ、LED、またはブザーと組み合わせて、より複雑なユーザーインターフェースを作成します。

* シンプルな計算機の作成：

  キーパッドを使用して数字を入力し、LCDに表示された基本的な算術演算を実行します。

**結論**

このレッスンでは、Adafruit Keypadライブラリを使用して、4x4マトリックスキーパッドをRaspberry Pi Picoにインターフェースさせる方法を学びました。キー押下を検出することで、キーベースの入力システムやパスワード入力メカニズムなど、インタラクティブなプロジェクトを作成できます。キーパッドの入力を読み取り、処理する方法を理解することは、エレクトロニクスプロジェクトにおける使いやすいインターフェースを構築するために重要です。
