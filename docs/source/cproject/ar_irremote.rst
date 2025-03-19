.. note::

    こんにちは！FacebookのSunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！ Raspberry Pi、Arduino、ESP32に関する情報を仲間と一緒に深く掘り下げて学びましょう。

    **参加する理由は？**

    - **専門的なサポート**: 購入後の問題や技術的な課題をコミュニティとチームのサポートで解決できます。
    - **学び・共有**: スキル向上のためのヒントやチュートリアルを交換しましょう。
    - **限定プレビュー**: 新製品の発表や先行情報をいち早くゲット！
    - **特別割引**: 最新製品に対する限定割引をお楽しみいただけます。
    - **フェスティブなプロモーションやプレゼント企画**: プレゼントや季節ごとのプロモーションに参加しよう！

    👉 一緒に探求し、作成する準備はできましたか？今すぐ[|link_sf_facebook|]をクリックして参加しましょう！

.. _ar_irremote:


6.4 赤外線リモコンの使用
==========================================================

このレッスンでは、 **赤外線(IR)リモコン** と **IR受信機** をRaspberry Pi Pico 2 Wで使用する方法を学びます。これにより、IRリモコンからの信号を受信し、デコードしてプロジェクトをワイヤレスで制御できるようになります。

* :ref:`cpn_ir_receiver`

**必要な部品**

このプロジェクトには以下の部品が必要です。

セットを購入するのが便利です。リンクはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 部品名
        - このキットに含まれるアイテム
        - 購入リンク
    *   - Pico 2 W スターターキット
        - 450+
        - |link_pico2w_kit|

これらは別々に購入することもできます。リンクは以下の通りです。

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - 番号
        - 部品紹介
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
        - 数個
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_ir_receiver`
        - 1
        - |link_receiver_buy|

**赤外線通信の理解**

赤外線通信は、赤外線光を使用してデータをワイヤレスで送信する技術です。家庭用のテレビやDVDプレーヤーなどは、IRリモコンを使って操作されます。

* **IR送信機（リモコン）**: ボタンを押すと、変調された赤外線光を放出します。
* **IR受信機**: 変調された赤外線光を検出し、それを電気信号に変換してデコードします。

**回路図**

|sch_irrecv|

**配線**

|wiring_irrecv|

**コードの作成**

IR受信機を初期化し、受信したIR信号をデコードし、対応するボタンをシリアルモニタに表示するプログラムを作成します。

.. note::

    * ファイル ``6.4_ir_remote_control.ino`` を ``pico-2w-kit-main/arduino/6.4_ir_remote_control`` 内で開けます。
    * または、このコードを **Arduino IDE** にコピーして使ってください。
    * Raspberry Pi Picoボードと正しいポートを選択した後、Uploadボタンをクリックしてください。
    * ここでは ``IRremote`` ライブラリを使用しています。このライブラリは **ライブラリマネージャー** からインストールできます。

      .. image:: img/lib_ir.png

.. code-block:: arduino

    #define SEND_PWM_BY_TIMER

    #include <IRremote.hpp>  // IRremoteライブラリをインクルード

    const int receiverPin = 17;  // IRセンサーのピン番号を定義

    void setup() {
      // シリアル通信を115200のボーレートで開始
      Serial.begin(115200);
      // 指定したピンでIR受信機を初期化し、LEDフィードバックを有効に
      IrReceiver.begin(receiverPin, ENABLE_LED_FEEDBACK);
    }

    void loop() {
      if (IrReceiver.decode()) {  // IR受信機が信号を受信したか確認
        bool result = 0;
        String key = decodeKeyValue(IrReceiver.decodedIRData.command);
        if (key != "ERROR") {
          Serial.println(key);  // デコードされたコマンドをシリアルモニタに表示
          delay(100);
        }
      IrReceiver.resume();  // 次の信号を受信できるようにIR受信機を準備
      }
    }

    // 受信したIR信号を対応するキーにマッピングする関数
    String decodeKeyValue(long result) {
      switch (result) {
        case 0x45: return "POWER";
        case 0x47: return "MUTE";
        case 0x46: return "MODE";
        case 0x44: return "PLAY/PAUSE";
        case 0x40: return "BACKWARD";
        case 0x43: return "FORWARD";
        case 0x7: return "EQ";
        case 0x15: return "-";
        case 0x9: return "+";
        case 0x19: return "CYCLE";
        case 0xD: return "U/SD";
        case 0x16: return "0";
        case 0xC: return "1";
        case 0x18: return "2";
        case 0x5E: return "3";
        case 0x8: return "4";
        case 0x1C: return "5";
        case 0x5A: return "6";
        case 0x42: return "7";
        case 0x52: return "8";
        case 0x4A: return "9";
        case 0x0: return "ERROR";
        default: return "ERROR";
      }
    }

コードをアップロード後、IRリモコンのボタンを押してみてください。シリアルモニタに対応するキーラベルが表示されるのを確認できます。

.. code-block:: arduino

    BACKWARD
    CYCLE
    POWER
    MODE
    EQ
    5
    9

.. note::

  新しいリモコンにはバッテリーを隔離するためのプラスチック片がついている場合があります。このプラスチック片を取り外してリモコンを有効化してください。


**コードの理解**

#. ヘッダーと定数:

   * ``#define SEND_PWM_BY_TIMER``: これはPWM信号をタイマーを使って送信するためのマクロ定義のようですが、コード内で使用されていないため、おそらく残りの部分かプレースホルダーです。
   * ``#include <IRremote.hpp>``: ``IRremote`` ライブラリをインクルードし、IR信号の送受信機能を提供します。
   * ``const int receiverPin = 17;``: IR受信機モジュールがArduinoのピン17に接続されていることを定義します。

#. setup関数:

   * ``Serial.begin(115200);``: シリアル通信を115200のボーレートで開始し、デバッグ用にArduinoとコンピュータ間で通信を可能にします。
   * ``IrReceiver.begin(receiverPin, ENABLE_LED_FEEDBACK);``: IR受信機を ``receiverPin`` で初期化し、LEDフィードバックを有効にして、IR信号を受信するとLEDが点灯します。

   .. code-block:: arduino

      void setup() {
        Serial.begin(115200);
        IrReceiver.begin(receiverPin, ENABLE_LED_FEEDBACK);
      }

#. loop関数:

   * ``if (IrReceiver.decode())``: IR受信機が有効なIR信号を受信したか確認します。受信した場合、信号をデコードします。
   * ``decodeKeyValue(IrReceiver.decodedIRData.command)``: 受信したIRコマンドを人間が読みやすいキー（例えば、「POWER」や「MUTE」）に変換する関数を呼び出します。
   * ``Serial.println(key);``: デコードされたキーをシリアルモニタに表示します。
   * ``delay(100);``: 同じ信号を複数回表示しないように短い遅延を追加します。
   * ``IrReceiver.resume();``: 次の信号を受信できるようにIR受信機を準備します。

   .. code-block:: arduino

      void loop() {
        if (IrReceiver.decode()) {
          bool result = 0;
          String key = decodeKeyValue(IrReceiver.decodedIRData.command);
          if (key != "ERROR") {
            Serial.println(key);
            delay(100);
          }
          IrReceiver.resume();
        }
      }

#. ``decodeKeyValue`` 関数:

   * この関数は、受信したIRコマンド（長い値）を受け取り、switch文を使って対応するキー名にマッピングします。各ケースはリモコンの異なるボタンに対応しています。
   * 例えば、0x45は「POWER」に、0x47は「MUTE」にマッピングされます。
   * コマンドが既知のキーに一致しない場合、関数は「ERROR」を返します。

   .. code-block:: arduino

      String decodeKeyValue(long result) {
        switch (result) {
          case 0x45: return "POWER";
          case 0x47: return "MUTE";
          case 0x46: return "MODE";
          ...
          case 0x4A: return "9";
          case 0x0: return "ERROR";
          default: return "ERROR";
        }
      }

**トラブルシューティング**

* 表示されない場合:

  * IR受信機がGPIO17に正しく接続されているか確認してください。
  * IR受信機に電源が供給されているか（VCCとGND接続）確認してください。
  * コードで正しいGPIOピンが定義されているか確認してください（ ``receiverPin`` ）。

* 不正確な読み取り:

  * リモコンがIR受信機と互換性があることを確認してください。
  * ``decodeKeyValue`` 関数が正しくIRコードをマッピングしているか確認してください。
  * ユニバーサルリモコンを使用して互換性を確認してください。

* 不明なコマンド:

  * ``decodeKeyValue`` 関数を更新して、リモコン固有のIRコードを含めてください。
  * IRデコードツールやリファレンスを使用して、リモコンが発する正しいコードを見つけてください。

* 信号干渉:

  * リモコンとIR受信機の間に障害物がないことを確認してください。
  * 他のIR信号を発するデバイスの近くにセンサーを置かないようにしてください。

**さらに探求**

* IR信号でデバイスを制御:

  デコードされたIR信号を使って、LED、モーター、サーボなどのアクチュエーターをリモコンからの入力に基づいて制御します。

* ユニバーサルリモコンの作成:

  ``decodeKeyValue()`` 関数を拡張して、複数のリモコンをサポートするために、広範囲のIRコードをマッピングします。

* フィードバック機能の追加:

  LCDやOLEDディスプレイを使って、現在の状態や受信したコマンドを表示します。

**結論**

このレッスンでは、Raspberry Pi Picoを使って赤外線（IR）リモコンとIR受信機を使用し、IR信号を受信してデコードする方法を学びました。IRremoteライブラリを統合することで、リモコンの入力を簡単に解釈し、ワイヤレスでプロジェクトと対話できるようになります。このセットアップは、リモートコントロールデバイス、オートメーションシステム、さまざまなアプリケーションでのユーザーフレンドリーなインターフェース作成の基盤となります。
