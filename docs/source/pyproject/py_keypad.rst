.. note:: 

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Raspberry Pi、Arduino、ESP32を使って、他の愛好者と一緒にさらに深く学んでいきましょう。

    **なぜ参加するのか？**

    - **専門的なサポート**：コミュニティとチームのサポートを受けて、販売後の問題や技術的な課題を解決できます。
    - **学びとシェア**：スキルを高めるために、ヒントやチュートリアルを交換しましょう。
    - **限定プレビュー**：新しい製品の発表やスニークピークに早期アクセスできます。
    - **特別割引**：最新製品に対する限定割引を楽しめます。
    - **フェスティブプロモーションとプレゼント**：プレゼントやホリデープロモーションに参加しましょう。

    👉 一緒に探求し、創造を始める準備はできましたか？[|link_sf_facebook|]をクリックして、今日から参加しましょう！

.. _py_keypad:

4.2 4x4 キーパッド
========================

このレッスンでは、Raspberry Pi Pico 2 Wを使用して **4x4マトリックスキーパッド** をインターフェースし、どのキーが押されたかを検出する方法を学びます。マトリックスキーパッドは、計算機、電話、販売機、セキュリティシステムなどで数値入力として一般的に使用されています。

* :ref:`cpn_keypad`
* `E.161 - Wikipedia <https://en.wikipedia.org/wiki/E.161>`_

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
        - :ref:`cpn_resistor`
        - 4(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_keypad`
        - 1
        - |link_keypad_buy|

**4x4マトリックスキーパッドの理解**

4x4キーパッドは以下で構成されています：

* **16個のキー** が4行4列のマトリックスに配置されています。
* **8本のピン**：4本は行に接続され、4本は列に接続されています。

キーを押すと、特定の行と列が接続され、その行番号と列番号に基づいて押されたキーを識別することができます。

キーの配置は以下のようになっています：

|img_keypad|

**回路図**

|sch_keypad|

4つのプルダウン抵抗がキーパッドの各列に接続されており、キーが押されていないときにG6～G9は安定した低レベルを取得します。

キーパッドの行（G2～G5）は高レベルに設定され、G6～G9のいずれかが高レベルを読み取ると、どのキーが押されたかがわかります。

例えば、G6が高レベルを読み取ると、数字の「1」が押されたことになります。これは、数字キー「1」の制御ピンがG2とG6であり、数字キー「1」が押されるとG2とG6が接続され、G6も高レベルになるためです。


**配線**

|wiring_keypad|

配線を簡単にするために、上記の図では、マトリックスキーパッドの列行と10K抵抗が、G6～G9がある穴に同時に挿入されています。


**コードの作成**

どのキーが押されたかを読み取るMicroPythonプログラムを作成します。

.. note::

    * ``4.2_4x4_keypad.py`` を ``pico-2w-kit-main/micropython`` から開くか、コードをThonnyにコピーして、「実行」ボタンをクリックするか、F5を押してください。
    * 正しいインタープリタが選択されていることを確認してください：MicroPython（Raspberry Pi Pico）。COMxx。


.. code-block:: python

    import machine
    import time

    # キーパッド上の文字を定義
    keys = [
        ['1', '2', '3', 'A'],
        ['4', '5', '6', 'B'],
        ['7', '8', '9', 'C'],
        ['*', '0', '#', 'D']
    ]

    # 行と列に接続されているGPIOピンを定義
    row_pins = [2, 3, 4, 5]   # GP2-GP5
    col_pins = [6, 7, 8, 9]   # GP6-GP9

    # 行ピンを出力として初期化
    rows = [machine.Pin(pin_num, machine.Pin.OUT) for pin_num in row_pins]

    # 列ピンを入力として初期化（プルダウン抵抗付き）
    cols = [machine.Pin(pin_num, machine.Pin.IN, machine.Pin.PULL_DOWN) for pin_num in col_pins]

    def scan_keypad():
        for i, row in enumerate(rows):
            # 全ての行を低レベルに設定
            for r in rows:
                r.value(0)
            # 現在の行を高レベルに設定
            row.value(1)
            # 列が高レベルを検出
            for j, col in enumerate(cols):
                if col.value() == 1:
                    # キーが検出されました
                    return keys[i][j]
        return None

    last_key = None

    while True:
        key = scan_keypad()
        if key != last_key:
            if key is not None:
                print("Key pressed:", key)
            last_key = key
        time.sleep(0.1)

**コードの理解**

#. キーパッドの文字の定義

この2Dリストは、物理的な配置に一致するキーパッドのレイアウトを表しています。

.. code-block:: python

    keys = [
        ['1', '2', '3', 'A'],
        ['4', '5', '6', 'B'],
        ['7', '8', '9', 'C'],
        ['*', '0', '#', 'D']
    ]

#. ピンの初期化：

.. code-block:: python

    row_pins = [2, 3, 4, 5]   # 行用のGPIOピン
    col_pins = [6, 7, 8, 9]   # 列用のGPIOピン

    # 行を出力として初期化
    rows = [machine.Pin(pin_num, machine.Pin.OUT) for pin_num in row_pins]

    # 列を入力として初期化（プルダウン抵抗付き）
    cols = [machine.Pin(pin_num, machine.Pin.IN, machine.Pin.PULL_DOWN) for pin_num in col_pins]

#. キーパッドスキャン関数の定義：

この関数は各行をスキャンし、それを高レベルに設定して、どの列が高レベルを示すかを確認し、どの行と列でキーが押されたかを示します。

.. code-block:: python

    def scan_keypad():
        for i, row in enumerate(rows):
            # 全ての行を低レベルに設定
            for r in rows:
                r.value(0)
            # 現在の行を高レベルに設定
            row.value(1)
            # 列でキー押下を確認
            for j, col in enumerate(cols):
                if col.value() == 1:
                    # キーが押された
                    return keys[i][j]
        return None

#. メインループでのキー押下の検出：

* ループはキー押下を継続的にスキャンします。
* 現在のキーが前回のキーと異なるかを確認して、同じキーが複数回検出されないように（デバウンシング）します。
* 新しいキー押下が検出されると、そのキーを表示します。

.. code-block:: python

    last_key = None

    while True:
        key = scan_keypad()
        if key != last_key:
            if key is not None:
                print("Key pressed:", key)
            last_key = key
        time.sleep(0.1)

プログラムを実行後、キーパッドで異なるキーを押してみてください。対応するキー文字がThonnyシェルに表示されるはずです。

**トラブルシューティングのヒント**

* キーを押しても出力がない：

  * 全ての接続が正しいか確認してください。
  * プルダウン抵抗が列ピンとGNDの間に適切に接続されているか確認してください。

* 正しくないキーが検出される：

  * keys配列がキーパッドのレイアウトに一致しているか再確認してください。
  * コード内の行と列のピンが物理的な接続と一致しているか確認してください。

* 複数のキーが検出される：

  機械的なキーパッドでは、複数のキーが同時に押されるとゴースティング（誤ったキー押下）が発生することがあります。この基本的なセットアップでは、同時に複数のキーを押さないようにしましょう。

**さらに試してみる**

* **簡単なパスワードロックの実装**：キーの入力シーケンスを保存し、事前設定されたパスワードと比較します。
* **LCDディスプレイの追加**：押されたキーをLCDスクリーンに表示します。
* **計算機の作成**：キーパッドを使用して数字を入力し、基本的な算術演算を行います。

**結論**

このレッスンでは、Raspberry Pi Pico 2 Wを使用して4x4マトリックスキーパッドを接続およびプログラムする方法を学びました。これでキー押下を検出し、プロジェクトと対話できるようになります。ロック、計算機、制御インターフェースのようなインタラクティブなデバイスを作成するための可能性が広がります。
