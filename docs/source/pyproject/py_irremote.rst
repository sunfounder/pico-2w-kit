.. note::

    こんにちは！SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityにようこそ！Raspberry Pi、Arduino、ESP32を愛する仲間たちと一緒に、さらに深く学びましょう。

    **参加する理由は？**

    - **専門的なサポート**: コミュニティやチームのサポートを受けて、販売後の問題や技術的な課題を解決できます。
    - **学び・共有**: ヒントやチュートリアルを交換して、スキルを向上させましょう。
    - **限定プレビュー**: 新製品の発表や先行情報をいち早くチェックできます。
    - **特別割引**: 新製品をお得に購入できます。
    - **フェスティブプロモーションやプレゼント**: プレゼントやホリデープロモーションに参加しましょう。

    👉 私たちと一緒に探求し、創造しましょう！[|link_sf_facebook|]をクリックして、今すぐ参加しよう！

.. _py_irremote:


6.4 赤外線リモコンの使用
==========================================================

このレッスンでは、Raspberry Pi Pico 2 Wを使用して、 **赤外線（IR）リモコン** と **IR受信モジュール** を使う方法を学びます。これにより、赤外線リモコンからの信号を受信して解読し、ワイヤレスでプロジェクトを制御することができるようになります。

* :ref:`cpn_ir_receiver`

**必要な部品**

このプロジェクトには、以下の部品が必要です。

一式購入するのが便利です。こちらから購入できます：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 部品名
        - セットに含まれるアイテム
        - リンク
    *   - Pico 2 W スターターキット
        - 450+
        - |link_pico2w_kit|

以下のリンクから個別に購入することもできます。


.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - 部品名
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
        - 数個
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_ir_receiver`
        - 1
        - |link_receiver_buy|

**赤外線通信の理解**

赤外線通信は、赤外線光を使用してデータをワイヤレスで送信する方法です。家庭用のデバイス（テレビやDVDプレーヤーなど）は、赤外線リモコンを使って操作されます。

* **IR送信機（リモコン）**: ボタンが押されると、変調された赤外線光を発します。
* **IR受信モジュール**: 変調された赤外線光を検出し、それを電気信号に変換して解読します。

**回路図**

|sch_irrecv|

**配線**

|wiring_irrecv|


**コードの作成**

リモコンからの赤外線信号を受信して解読するMicroPythonスクリプトを作成します。

.. note::

    * ``6.4_ir_remote_control.py`` を ``pico-2w-kit-main/micropython`` から開くか、コードをThonnyにコピーして、「Run」をクリックするか、F5を押します。
    * 正しいインタプリタ（MicroPython (Raspberry Pi Pico).COMxx）が選択されていることを確認してください。
    * ここで使用する ``ir_rx`` フォルダ内のライブラリがアップロードされているか確認してください。詳細なチュートリアルは :ref:`add_libraries_py` を参照してください。

.. code-block:: python

    import time
    from machine import Pin
    from ir_rx.nec import NEC_8  # 使用するリモコンのプロトコルに応じて調整
    from ir_rx.print_error import print_error

    # IR受信ピンの初期化
    ir_pin = Pin(17, Pin.IN)

    # 受信データを処理するコールバック関数
    def ir_callback(data, addr, ctrl):
        if data < 0:  # リピートコードまたはエラー
            pass
        else:
            key = decode_key(data)
            print("Received Key:", key)

    # 受信データをキー入力に変換する関数
    def decode_key(data):
        key_codes = {
            0x45: "POWER",
            0x46: "MODE",
            0x47: "MUTE",
            0x44: "PLAY/PAUSE",
            0x40: "BACKWARD",
            0x43: "FORWARD",
            0x07: "EQ",
            0x15: "-",
            0x09: "+",
            0xD: "U/SD",
            0x16: "0",
            0x19: "cycle",
            0xC: "1",
            0x5E: "3",
            0x18: "2",
            0x8: "4",
            0x1C: "5",
            0x5A: "6",
            0x42: "7",
            0x52: "8",
            0x4A: "9",
            0x0: "ERROR",
            # リモコンに基づいてさらにキーコードを追加
        }
        return key_codes.get(data, "UNKNOWN")

    # IR受信機のインスタンスを作成
    ir = NEC_8(ir_pin, ir_callback)
    ir.error_function(print_error)  # エラーメッセージの表示（オプション）

    try:
        while True:
            time.sleep(1)  # メインスレッドを維持
    except KeyboardInterrupt:
        ir.close()
        print("Program terminated")

コードを実行し、赤外線リモコンのボタンを押すと、Thonnyシェル（または他のシリアルモニタ）に押したキーの名前が表示されます。たとえば、リモコンの「PLAY」ボタンを押すと、シェルに「Received Key: PLAY」と表示されます。

**コードの理解**

#. インポートと初期化:

   * ``ir_rx.nec.NEC_8``: 8ビットアドレスのNECプロトコルデコーダ。
   * ``print_error``: エラーメッセージを表示するための関数。

   .. code-block:: python

        import time
        from machine import Pin
        from ir_rx.nec import NEC_8
        from ir_rx.print_error import print_error

#. IR受信ピンの初期化:

   .. code-block:: python

        ir_pin = Pin(17, Pin.IN)

#. コールバック関数の定義:

   この関数は、データが受信されると自動的に呼び出されます。dataパラメータにはキーコードが含まれます。

   .. code-block:: python

        def ir_callback(data, addr, ctrl):
            if data < 0:
                pass  # リピートコードを無視
            else:
                key = decode_key(data)
                print("Received Key:", key)

#. キー解読関数:

   受信したキーコードを人間が読みやすいラベルに変換します。

   .. code-block:: python

        def decode_key(data):
            key_codes = {
            0x45: "POWER",
            0x46: "MODE",
            0x47: "MUTE",
            0x44: "PLAY/PAUSE",
            0x40: "BACKWARD",
            0x43: "FORWARD",
            0x07: "EQ",
            0x15: "-",
            0x09: "+",
            0xD: "U/SD",
            0x16: "0",
            0x19: "cycle",
            0xC: "1",
            0x5E: "3",
            0x18: "2",
            0x8: "4",
            0x1C: "5",
            0x5A: "6",
            0x42: "7",
            0x52: "8",
            0x4A: "9",
            0x0: "ERROR",
            # リモコンに基づいてさらにキーコードを追加
            }
            return key_codes.get(data, "UNKNOWN")

#. IR受信機のインスタンス化:

   コールバック関数でIR受信機を設定します。

   .. code-block:: python

        ir = NEC_8(ir_pin, ir_callback)
        ir.error_function(print_error)


#. メインループ:

   IR信号をリスンし続けるためにプログラムを実行します。プログラム終了時にエラーなく終了します。

   .. code-block:: python

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            ir.close()
            print("Program terminated")

**アプリケーション**

* **ワイヤレスでプロジェクトを制御**: 赤外線リモコンを使用してLEDやモーター、その他の周辺機器を制御します。
* **ユニバーサルリモコンデコーダの作成**: コードを拡張して、複数のプロトコルやリモコンに対応させます。

**結論**

このレッスンでは、Raspberry Pi Pico 2 Wと赤外線受信モジュールを使用して、赤外線リモコンからの信号を解読する方法を学びました。これにより、家庭用のリモコンを使用して、プロジェクトにワイヤレス制御を追加することができます。

* `コールバック関数 - Wikipedia <https://en.wikipedia.org/wiki/Callback_(computer_programming)>`_
