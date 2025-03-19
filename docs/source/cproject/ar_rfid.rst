.. note:: 

    こんにちは！FacebookのSunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Raspberry Pi、Arduino、ESP32を他の愛好者と一緒に深く学びましょう。

    **参加する理由は？**

    - **専門的なサポート**: 購入後の問題や技術的な課題をコミュニティやチームの助けを借りて解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換し、スキルを向上させましょう。
    - **限定プレビュー**: 新製品の発表や先行公開をいち早くチェックできます。
    - **特別割引**: 新しい製品に対して独占的な割引を楽しめます。
    - **祭典のプロモーションやプレゼント**: プレゼントや祝日プロモーションに参加しましょう。

    👉 一緒に探求し、創造を楽しむ準備はできましたか？[|link_sf_facebook|]をクリックして、今日から参加しましょう！

.. _ar_rfid:


6.5 RFIDのインターフェース
===========================================

このレッスンでは、 **無線周波数識別（RFID）** 技術をRaspberry Pi Pico 2 Wと共に使用する方法を学びます。RFIDは、リーダーとタグ間でワイヤレス通信を可能にし、識別、認証、データ保存に使用できます。

* :ref:`cpn_mfrc522`

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
        - :ref:`cpn_mfrc522`
        - 1
        - |link_rfid_buy|

**RFIDの理解**

RFID技術は、物体に取り付けられたタグを自動的に識別し追跡するために電磁場を使用します。タグには電子的に保存された情報が含まれており、視線が直接届かなくても遠隔で読み取ることができます。

* **RFIDリーダー（MFRC522）**: RFIDタグと通信するために電波を発信するデバイス。
* **RFIDタグ**: マイクロチップとアンテナを内蔵した小さな物体（カードやキーフォブなど）。パッシブ（バッテリーなし）またはアクティブ（バッテリー駆動）のものがあります。

**回路図**

|sch_rfid|


**配線**

|wiring_rfid|

**コード作成**

MFRC522 RFIDリーダーを初期化し、RFIDタグを読み取って、そのユニークな識別子（UID）を読み取る2つのプログラムを作成します。

**コード**

.. note::

   * ここでは ``MFRC522`` ライブラリを使用しています。このライブラリは **ライブラリマネージャー** からインストールできます。

      .. image:: img/lib_mfrc522.png


1. RFIDタグへの情報書き込み：

   .. note::

      * ``6.5_rfid_read.ino`` ファイルを ``pico-2w-kit-main/arduino/6.5_rfid_read`` から開きます。
      * または、このコードを **Arduino IDE** にコピーします。
      * **Raspberry Pi Pico 2 W** ボードと正しいポートを選択して、「アップロード」をクリックします。

   .. code-block:: arduino
   
       #include <SPI.h>
       #include <MFRC522.h>
   
       // RFIDモジュールの接続ピンを定義
       #define SS_PIN 17    // SDAピンをGPIO 17（SPI SS）に接続
       #define RST_PIN 9    // RSTピンをGPIO 9に接続
   
       MFRC522 mfrc522(SS_PIN, RST_PIN); // MFRC522インスタンスを作成
   
       void setup() {
         // シリアル通信を初期化
         Serial.begin(115200);
         while (!Serial); // シリアルポート接続を待機
   
         // SPIバスを初期化
         SPI.begin();
   
         // RFIDリーダーを初期化
         mfrc522.PCD_Init();
         Serial.println("RFID Writer Initialized!");
   
       }
   
       void loop() {
         // シリアルバッファにデータがあるか確認
         if (Serial.available() > 0) {
           String data = Serial.readStringUntil('#'); // '#'が受信されるまで読み取る
           data.trim(); // 後ろの空白を削除
   
           // 新しいRFIDカードを待機
           Serial.println("Place your RFID tag near the reader...");
           if ( ! mfrc522.PICC_IsNewCardPresent()) {
             return;
           }
   
           // カードを選択
           if ( ! mfrc522.PICC_ReadCardSerial()) {
             return;
           }
   
           // キーAで認証
           MFRC522::MIFARE_Key key;
           for (byte i = 0; i < 6; i++) {
             key.keyByte[i] = 0xFF;
           }
   
           byte block = 4; // 書き込むブロック（例）
           byte sector = mfrc522.PICC_GetUid()->uidByte[0] % 32; // セクターを計算
   
           MFRC522::StatusCode status;
           status = mfrc522.PCD_Authenticate(MFRC522::PICC_CMD_MF_AUTH_KEY_A, block, &key, &(mfrc522.uid));
           if (status != MFRC522::STATUS_OK) {
             Serial.print("Authentication failed: ");
             Serial.println(mfrc522.GetStatusCodeName(status));
             return;
           }
   
           // 書き込むデータを準備（16バイト）
           byte buffer[18];
           data.getBytes(buffer, sizeof(buffer));
           buffer[16] = 0x00; // パディング
           buffer[17] = 0x00; // パディング
   
           // データを書き込む
           status = mfrc522.MIFARE_Write(block, buffer, 16);
           if (status != MFRC522::STATUS_OK) {
             Serial.print("Write failed: ");
             Serial.println(mfrc522.GetStatusCodeName(status));
             return;
           }
   
           Serial.println("Data written successfully!");
         }
       }

   コードをアップロード後、次のことが行われます：

   * シリアルモニタには次のように表示されます：
   
     .. code-block::

        RFID Reader Initialized!
        Place your RFID tag near the reader...

   * RFIDタグに書き込むデータを入力し、 ``#`` で終了します。例：

     .. code-block::

        Hello World#

   * RFIDタグをリーダーの近くに置いて、シリアルモニタに確認メッセージが表示されます：

     .. code-block::

        Data written successfully!

2. RFIDタグの読み取り：

   .. note::

      * ``6.5_rfid_read.ino`` ファイルを ``pico-2w-kit-main/arduino/6.5_rfid_read`` から開きます。
      * または、このコードを **Arduino IDE** にコピーします。
      * **Raspberry Pi Pico 2 W** ボードと正しいポートを選択して、「アップロード」をクリックします。

   .. code-block:: arduino

        #include <SPI.h>
        #include <MFRC522.h>

        // RFIDモジュールの接続ピンを定義
        #define SS_PIN 17    // SDAピンをGPIO 17（SPI SS）に接続
        #define RST_PIN 9    // RSTピンをGPIO 9に接続

        MFRC522 mfrc522(SS_PIN, RST_PIN); // MFRC522インスタンスを作成

        void setup() {
          // シリアル通信を初期化
          Serial.begin(115200);
          while (!Serial); // シリアルポート接続を待機

          // SPIバスを初期化
          SPI.begin();

          // RFIDリーダーを初期化
          mfrc522.PCD_Init();
          Serial.println("RFID Reader Initialized!");
        }

        void loop() {
          // 新しいRFIDカードを探す
          if ( ! mfrc522.PICC_IsNewCardPresent()) {
            return;
          }

          // カードを選択
          if ( ! mfrc522.PICC_ReadCardSerial()) {
            return;
          }

          // カードのUIDを読み取る
          Serial.print("UID tag :");
          String content= "";
          byte letter;
          for (byte i = 0; i < mfrc522.uid.size; i++) {
             content.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " "));
             content.concat(String(mfrc522.uid.uidByte[i], HEX));
          }
          Serial.println(content);

          // 関連するユーザーデータを表示
          if (userData.length() > 0) {
            Serial.print("Associated Data: ");
            Serial.println(userData);
          } else {
            Serial.println("No data associated with this UID.");
          }
        }

   コードをアップロード後、次のことが行われます：

   * シリアルモニタには次のように表示されます：
   
     .. code-block::

        RFID Reader Initialized!

   * RFIDタグ（例：キーフォブやカード）をMFRC522 RFIDモジュールの近くに置いてください。シリアルモニタにはタグのUIDとデータが表示されます：

     .. code-block::

        UID tag : 04 A3 1B 7C 3E
        Data on tag: HelloWorld

**トラブルシューティング**


* 読み取りが表示されない：


  * 配線接続を確認し、特にSPIライン（SCK、MOSI、MISO、SS）をチェックしてください。
  * RFIDモジュールが電源を受け取っているか確認してください（VCCおよびGND接続）。
  * コード内で正しいGPIOピンが定義されていることを確認してください。

* 誤った読み取り：

  * RFIDタグがMFRC522モジュールと互換性があることを確認してください。
  * 他のRFIDタグを使用してタグ固有の問題を除外してください。

* 書き込み失敗：

  * RFIDタグがロックされていないこと、または書き込み保護されていないことを確認してください。
  * 認証キーがタグのキーと一致していることを確認してください。
  * データバッファが正しくフォーマットされ、16バイトを超えていないことを確認してください。

* 信号干渉：

  * RFIDモジュールを干渉を引き起こす可能性のある他の電子機器の近くに置かないようにしてください。
  * RFIDタグとリーダー間の通信を妨げる物理的な障害物がないことを確認してください。

**さらなる探求**

* アクセス制御システム：

  RFIDタグで制御されるドアロックメカニズムを実装します。

* 在庫管理：

  RFIDタグを使用して在庫アイテムを追跡および管理し、自動計測と監視を行います。

* RFIDベースの認証：

  ユーザーログインやデバイスアクセスのためのセキュリティ認証システムを作成します。

* 他のセンサーとの統合：

  RFIDを温度センサーや動きセンサーなどと統合して、総合的な監視システムを作成します。

**結論**

このレッスンでは、MFRC522 RFIDモジュールを使用してRFIDシステムをRaspberry Pi Picoとインターフェースする方法を学びました。SPI通信プロトコルとMFRC522ライブラリを活用することで、RFIDタグへのデータの読み取りと書き込みが簡単に行えるようになり、アクセス制御システム、在庫管理、インタラクティブなプロジェクトなどの幅広いアプリケーションが実現可能です。
