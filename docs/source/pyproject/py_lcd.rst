.. note:: 

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Facebookで他の愛好者と一緒に、Raspberry Pi、Arduino、ESP32をさらに深く学びましょう。

    **なぜ参加するのか？**

    - **専門的なサポート**：コミュニティとチームのサポートで、販売後の問題や技術的な課題を解決できます。
    - **学びとシェア**：スキルを高めるために、ヒントやチュートリアルを交換しましょう。
    - **限定プレビュー**：新しい製品発表や先行情報に早期アクセスできます。
    - **特別割引**：最新製品に対する限定割引をお楽しみいただけます。
    - **フェスティブプロモーションとプレゼント**：プレゼントやホリデープロモーションに参加しましょう。

    👉 一緒に探求し、創造を始める準備はできましたか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _py_lcd:

3.4 液晶ディスプレイ
===============================

このレッスンでは、Raspberry Pi Pico 2 Wを使用して **1602 LCD** を操作し、テキストを表示する方法を学びます。LCD1602は16文字×2行で表示できるキャラクターベースの液晶ディスプレイで、メッセージ、センサーデータ、またはステータス更新など、情報を表示する必要があるプロジェクトに最適です。

液晶ディスプレイをマイクロコントローラに直接接続するには、多くのGPIOピンが必要ですが、これがプロジェクトの機能を制限することがあります。この問題を解決するために、 **I2Cインターフェース** を持つLCD1602モジュールを使用することができます。I2Cプロトコルでは、2本のデータライン（SDAおよびSCL）だけを使用するため、LCDの制御にGPIOピンを2本だけ使用でき、他のピンを追加のセンサーやデバイス用に解放できます。

* :ref:`cpn_i2c_lcd`


**Raspberry Pi Pico 2 WでのI2Cの理解**

Raspberry Pi Pico 2 Wは、複数のGPIOピンを通じてI2C通信をサポートしており、プロジェクトに柔軟性を提供します。I2C0とI2C1という2つのI2Cバスがあり、それぞれ複数のピンセットにマッピングできます。

PicoのI2C対応ピンの詳細は以下の通りです：cpn_pico_2w

|pin_i2c|

SDAとSCLのピンペアをI2C0またはI2C1のどちらにも選択できるため、他の周辺機器とのピンの競合を避けることができます。

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
        - :ref:`cpn_i2c_lcd`
        - 1
        - |link_i2clcd1602_buy|

**回路図**

|sch_lcd|

**配線**

|wiring_lcd|

**コードの作成**

LCD1602にメッセージを表示するためのMicroPythonプログラムを作成しましょう。

.. note::

   * ``3.4_liquid_crystal_display.py`` を ``pico-2w-kit-main/micropython`` から開くか、コードをThonnyにコピーして、「実行」ボタンをクリックするか、F5を押してください。
   * 正しいインタープリタが選択されていることを確認してください：MicroPython（Raspberry Pi Pico）。COMxx。  
   * ここで使用するライブラリは ``lcd1602.py`` です。このライブラリがPicoにアップロードされていることを確認し、詳細なチュートリアルについては :ref:`add_libraries_py` を参照してください。


.. code-block:: python

   from machine import I2C, Pin
   from lcd1602 import LCD
   import utime

   # I2C通信の初期化（I2C0）
   i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)

   # LCDオブジェクトの作成
   lcd = LCD(i2c)

   # 最初のメッセージを表示
   lcd.clear()
   lcd.message("Hello, World!")
   utime.sleep(2)

   # 2行目に移動して別のメッセージを表示
   lcd.write(0, 1,"LCD1602 with I2C")  # 列0、行1
   utime.sleep(5)

   # ディスプレイをクリア
   lcd.clear()

プログラムを実行すると、次のことが表示されます：

* LCDには最初の行に「Hello, World!」が表示されます。
* 2秒後、2行目に「LCD1602 with I2C」が表示されます。
* さらに5秒後、ディスプレイがクリアされます。

**コードの理解**

#. モジュールのインポート：

   * ``machine``: ハードウェアへのアクセスを提供します。
   * ``lcd1602``: LCD制御用のカスタムライブラリ。
   * ``utime``: 遅延に関連する時間関数。

#. I2C通信の初期化：

   .. code-block:: python
   
   i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)
   
   * ``I2C(0, ...)``: I2C0バスを使用。
   * ``sda=Pin(4)``: GP4をSDAとして設定。
   * ``scl=Pin(5)``: GP5をSCLとして設定。
   * ``freq=400000``: I2Cの周波数を400kHzに設定。

#. LCDオブジェクトの作成：

   * ``lcd = LCD(i2c)``: I2Cオブジェクトを渡してLCDクラスのインスタンスを作成。

#. メッセージの表示：

   * ``lcd.clear()``: 画面上のテキストをクリアします。
   * ``lcd.message("Hello, World!")``: LCDに「Hello, World!」を表示します。
   * ``utime.sleep(2)``: 次のコマンドを実行する前に2秒待機。

#. カーソルの移動と追加のテキストの表示：

   * ``lcd.write(0, 1,"LCD1602 with I2C")``: カーソルを2行目の最初の列に移動し、メッセージを表示します。

#. 最後の遅延とクリア：

   * ``utime.sleep(5)``: 5秒待機。
   * ``lcd.clear()``: 画面をクリアします。

**さらに試してみる**

* **カスタムメッセージの表示**: ``lcd.message()`` 内の文字列を変更して、自分のメッセージを表示します。
* **改行を使用**: LCD1602は2行なので、カーソルを2行目に移動して ``(0, 1, message[i:i+16])`` を使用できます。
* **スクロールテキストを作成**: ループ内でディスプレイを更新することでスクロール効果を作成できます。

  .. code-block:: python

      from machine import I2C, Pin
      from lcd1602 import LCD
      import utime

      # I2C通信の初期化（I2C0）
      i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)

      # LCDオブジェクトの作成
      lcd = LCD(i2c)

      message = "Scrolling Text Demo "
      lcd.clear()
      while True:
         for i in range(len(message)):
            lcd.write(0, 0, message[i:i+16])  # 16文字ずつ表示
            utime.sleep(0.3)

**トラブルシューティングのヒント**

* 正しい文字が表示されない、または表示されない：

  * 配線が正しいか確認してください、特にSDAおよびSCLの接続。
  * lcd1602ライブラリ内のI2CアドレスがLCDのアドレスと一致していることを確認してください。デフォルトでは0x27または0x3Fです。

* コントラストの調整：

  一部のLCDモジュールにはコントラスト調整用のポテンショメータがあります。画面に何も表示されない場合は、それを調整してみてください。

* 電源供給：

  LCDが十分な電力を受けていることを確認してください。5Vを使用する場合は、PicoのVSYSピン（USB経由で電源供給されている場合）または外部の5V電源に接続してください。

* I2Cアドレスの理解：

  LCDがテキストを表示しない場合、異なるI2Cアドレスを使用している可能性があります。I2Cバス上のデバイスをスキャンすることができます：

  .. code-block:: python
  
      from machine import I2C, Pin
      i2c = I2C(0, sda=Pin(4), scl=Pin(5))
      devices = i2c.scan()

      # I2Cアドレスを16進形式で表示
      print("I2C addresses found:", [hex(device) for device in devices])

  これにより、I2Cバスに接続されているデバイスのアドレスが表示されます。lcd1602.pyライブラリやコードを正しいアドレスを使用するように更新してください。

**結論**

I2Cインターフェースを使用してLCD1602ディスプレイを制御する方法を学びました。このスキルを活用することで、プロジェクトに視覚的な出力を追加し、よりインタラクティブで情報豊富なプロジェクトを作成できます。
