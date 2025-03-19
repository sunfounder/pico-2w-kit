.. note::

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Raspberry Pi、Arduino、ESP32について、他の愛好者とともにさらに深く学びましょう。

    **なぜ参加するのか？**

    - **専門家のサポート**: コミュニティやチームのサポートを受けて、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**: スキルを向上させるためのヒントやチュートリアルを交換できます。
    - **独占的なプレビュー**: 新製品の発表や先取り情報をいち早くチェックできます。
    - **特別割引**: 最新製品に対する独占的な割引を楽しめます。
    - **祭事プロモーションとプレゼント**: ギブアウェイや休日のプロモーションに参加できます。

    👉 一緒に探求し、創造しませんか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _ar_lcd:

3.4 液晶ディスプレイ（LCD1602）
=====================================

このレッスンでは、Raspberry Pi Pico 2 Wを使用して **1602 LCD** を操作し、テキストを表示する方法を学びます。LCD1602は、2行16文字を表示できる文字ベースの液晶ディスプレイで、メッセージ、センサーの読み取り、ステータス更新などの情報を表示するプロジェクトに最適です。

LCDをマイクロコントローラに直接接続するには、多くのGPIOピンが必要となり、プロジェクトの機能に制限を与えることがあります。この問題を解決するために、 **I2Cインターフェース** を備えたLCD1602モジュールを使用できます。I2Cプロトコルは、データライン（SDAとSCL）の2本だけを使用するため、2つのGPIOピンでLCDを制御でき、他のピンは追加のセンサーやデバイスに自由に使用できます。

**Raspberry Pi Pico 2 WでのI2Cの理解**

Raspberry Pi Pico 2 Wは、複数のGPIOピンを使用してI2C通信をサポートしており、プロジェクトの柔軟性を高めます。I2CバスはI2C0とI2C1の2つがあり、それぞれに複数のピンセットをマッピングできます。

Pico 2のI2C対応ピンは以下の通りです：

|pin_i2c|

I2C0またはI2C1のいずれかに対応するSDAとSCLのピンペアを選択できます。この柔軟性により、プロジェクトの他の周辺機器とのピン競合を避けることができます。


**必要な部品**

このプロジェクトでは、以下の部品が必要です。

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
        - :ref:`cpn_i2c_lcd`
        - 1
        - |link_i2clcd1602_buy|

**回路図**

|sch_lcd_ar|

**配線**

|wiring_lcd_ar|

**コードの記述**

.. note::

    * 「 ``3.4_liquid_crystal_display.ino`` 」ファイルを「 ``pico-2w-kit-main/arduino/3.4_liquid_crystal_display`` 」のパスで開きます。
    * または、このコードを **Arduino IDE** にコピーしてください。
    * アップロードボタンをクリックする前に、Raspberry Pi Picoボードと正しいポートを選択してください。
    * ここでは ``LiquidCrystal I2C`` ライブラリを使用しています。 **ライブラリマネージャー** からインストールできます。

      .. image:: img/lib_i2c_lcd.png

.. code-block:: arduino

  #include <Wire.h>
  #include <LiquidCrystal_I2C.h>

  // LCDのI2Cアドレスを設定（通常は0x27または0x3F）
  #define LCD_ADDRESS 0x27
  #define LCD_COLUMNS 16
  #define LCD_ROWS    2

  // I2Cアドレスとサイズでライブラリを初期化
  LiquidCrystal_I2C lcd(LCD_ADDRESS, LCD_COLUMNS, LCD_ROWS);

  void setup() {
    // LCDを初期化
    lcd.init();
    lcd.backlight();  // バックライトをオンにする

    // LCDにメッセージを表示
    lcd.setCursor(0, 0);  // 列0、行0
    lcd.print("Hello, World!");
    lcd.setCursor(0, 1);  // 列0、行1
    lcd.print("LCD1602 with I2C");
  }

  void loop() {
    // 何も行いません
  }


コードをRaspberry Pi Picoにアップロードした後、LCDには次のように表示されるはずです：

* 1行目：「Hello, World!」
* 2行目：「LCD1602 with I2C」

画面に何も表示されない場合は、LCDモジュールの背面にある小さなポテンショメータ（つまみ）を回してコントラストを調整し、テキストが表示されるようにしてください。

**コードの理解**

#. ライブラリのインクルード：

   * ``Wire.h``: I2C通信を処理します。
   * ``LiquidCrystal_I2C.h``: I2C LCDとのやり取りを簡単にします。

#. LCDパラメータの定義：

   * ``LCD_ADDRESS``: LCDモジュールのI2Cアドレス。一般的なアドレスは0x27または0x3Fです。アドレスが不明な場合は、I2Cスキャナースケッチを使用してアドレスを確認できます。

   .. code-block:: arduino

      #define LCD_ADDRESS 0x27
      #define LCD_COLUMNS 16
      #define LCD_ROWS    2

#. LCDの初期化：

   .. code-block:: arduino

      LiquidCrystal_I2C lcd(LCD_ADDRESS, LCD_COLUMNS, LCD_ROWS);

#. ``setup()`` 関数内：

   .. code-block:: arduino

      lcd.init();         // LCDを初期化
      lcd.backlight();    // バックライトをオンにする

#. テキストの表示：

   .. code-block:: arduino

      lcd.setCursor(0, 0);  // 列0、行0にカーソルを設定
      lcd.print("Hello, World!");

      lcd.setCursor(0, 1);  // 列0、行1にカーソルを設定
      lcd.print("LCD1602 with I2C");

**シリアル入力を使用してLCDにテキストを表示**

プログラムを拡張して、シリアルモニターから入力を読み取り、LCDに表示することができます。

* 修正後のコード：

  .. code-block:: arduino

    #include <Wire.h>
    #include <LiquidCrystal_I2C.h>

    #define LCD_ADDRESS 0x27
    #define LCD_COLUMNS 16
    #define LCD_ROWS    2

    LiquidCrystal_I2C lcd(LCD_ADDRESS, LCD_COLUMNS, LCD_ROWS);

    void setup() {
      lcd.init();
      lcd.backlight();

      Serial.begin(115200);
      lcd.setCursor(0, 0);
      lcd.print("Enter text:");
    }

    void loop() {
      if (Serial.available() > 0) {
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("You typed:");

        String inputText = Serial.readStringUntil('\n');
        lcd.setCursor(0, 1);
        lcd.print(inputText);
      }
    }

コードをアップロードした後、メッセージを入力して ``Enter`` を押すと、そのメッセージがLCDに表示されます。

* 説明：

  * シリアル入力の読み取り: シリアルポートでデータが利用可能かどうかをチェックし、改行文字が現れるまで入力文字列を読み取ります。

   .. code-block:: arduino

      if (Serial.available() > 0) {
        String inputText = Serial.readStringUntil('\n');
        // ...
      }

  * シリアル入力のLCD表示：

    .. code-block:: arduino

      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("You typed:");
      lcd.setCursor(0, 1);
      lcd.print(inputText);

**トラブルシューティング**

* LCDに表示されない場合：

  * LCDモジュールの背面にあるコントラストポテンショメータを調整してください。
  * 配線接続を確認してください。
  * 正しいI2Cアドレスが使用されているか確認してください。I2Cバス上でデバイスをスキャンし、接続が正しければアドレスが表示されます。通常、デフォルトのアドレスは0x27ですが、場合によっては0x3Fであることもあります。

  .. code-block:: arduino

      #include <Wire.h>

      void setup() {
          Wire.begin();
          Serial.begin(115200);
          while (!Serial); // シリアル接続が確立するまで待機
          Serial.println("\nI2C Scanner");
      }

      void loop() {
          byte error, address;
          int nDevices;

          Serial.println("Scanning...");

          nDevices = 0;
          for (address = 1; address < 127; address++) {
              Wire.beginTransmission(address);
              error = Wire.endTransmission();

              if (error == 0) {
                  Serial.print("I2C device found at address 0x");
                  if (address < 16) {
                      Serial.print("0");
                  }
                  Serial.println(address, HEX);

                  nDevices++;
              }else if (error == 4) {
                  Serial.print("Unknown error at address 0x");
                  if (address < 16) {
                      Serial.print("0");
                  }
                  Serial.println(address, HEX);
              }
          }
          if(nDevices == 0) {
              Serial.println("No I2C devices found\n");
          }else {
              Serial.println("done\n");
          }
          delay(5000); // 再スキャン前に5秒待機
      }

* 不正な文字が表示される場合：

  * 接続が緩んでいないか確認してください。
  * LCDが正しく初期化されているか確認してください。

**さらなる探索**

* カスタムキャラクター：

  LCDにカスタムキャラクターやシンボルを作成して表示します。

* センサーデータの表示：

  センサー（温度や湿度など）のデータを読み取り、その読み取り値をLCDに表示します。

* 複数のI2Cデバイス：

  Picoに複数のI2Cデバイスを接続し、同時に管理します。

**結論**

このレッスンでは、I2C LCD1602ディスプレイをRaspberry Pi Picoで操作し、テキストを表示する方法を学びました。I2Cインターフェースを使用することで、必要なGPIOピンの数を最小限に抑え、追加のセンサーや周辺機器を使用したより複雑なプロジェクトを実現することができます。
