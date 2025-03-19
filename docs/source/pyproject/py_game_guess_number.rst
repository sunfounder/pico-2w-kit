.. note:: 

    SunFounderのRaspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32について、他の愛好者と共にさらに深く学びましょう。

    **参加する理由は？**

    - **専門家サポート**: 購入後の問題や技術的な課題を、コミュニティやチームの支援で解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **限定プレビュー**: 新製品の発表や先行公開に早期アクセスできます。
    - **特別割引**: 最新製品に対する独占的な割引を享受できます。
    - **フェスティブプロモーションとプレゼント**: プレゼント企画やホリデープロモーションに参加できます。

    👉 一緒に探求し、創造しましょう！[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _py_guess_number:

7.7 「数当てゲーム」の作成
=============================================================

このプロジェクトでは、Raspberry Pi Pico 2 W、4x4行列型キーパッド、I2C接続のLCD1602ディスプレイを使用して、インタラクティブな **「数当てゲーム」** を作成します。このゲームは、0から99までのランダムな数字を生成し、プレイヤーがその数字を当てることを目的とします。各推測の後、推測が高すぎるか低すぎるかに基づいて範囲を絞り込み、誰かが正しい数字を当てるまで続きます。


**必要なコンポーネント**

このプロジェクトに必要なコンポーネントは次の通りです。

全セットを購入するのが便利です。リンクはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前	
        - セットに含まれるアイテム
        - リンク
    *   - Pico 2 Wスターターキット	
        - 450+
        - |link_pico2w_kit|

個別に購入することもできます。以下のリンクから購入できます。


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
        - マイクロUSBケーブル
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
    *   - 7
        - :ref:`cpn_i2c_lcd`
        - 1
        - |link_i2clcd1602_buy|

**コンポーネントの理解**

* **4x4行列型キーパッド**: 16個のボタンが4行4列のマトリックスで配置されているキーパッド。これを使って数字やコマンドを入力します。
* **I2C接続のLCD1602ディスプレイ**: 16x2文字のLCDディスプレイで、I2Cインターフェースを使用して、データライン(SDAとSCL)2本で配線が簡単になります。

**回路図**

|sch_guess_number|

この回路は、 :ref:`py_keypad` を基に、押されたキーを表示するためにI2C LCD1602を追加したものです。


**配線**

|wiring_game_guess_number|

配線を簡単にするために、上記の図では、マトリックスキーパッドの列と10KΩの抵抗を、G10〜G13に位置する穴に同時に挿入しています。

**コードの作成**

MicroPythonプログラムを作成して、以下の動作を行います：

* 0から99までのランダムな数字を生成します。
* キーパッドからの入力を読み取ります。
* LCDディスプレイにヒントとプレイヤーの入力を更新します。
* 各推測後に範囲を狭めます。

.. note::

    * ``7.7_game_guess_number.py``  を ``pico-2w-kit-main/micropython`` から開くか、コードをThonnyにコピーして、「Run」をクリックするか、F5キーを押してください。
    * 正しいインタープリターが選択されていることを確認してください：MicroPython（Raspberry Pi Pico）。COMxx。
    * ここでは ``lcd1602.py`` ライブラリを使用する必要があります。Picoにアップロードされているか確認してください。詳細なチュートリアルについては :ref:`add_libraries_py` を参照してください。

.. code-block:: python

    from lcd1602 import LCD
    from machine import I2C, Pin
    import utime
    import urandom

    # LCD1602ディスプレイのためにI2C通信を初期化
    i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)
    lcd = LCD(i2c)

    # 4x4行列型キーパッドのキャラクターマッピング
    keypad_map = [
        ["1", "2", "3", "A"],
        ["4", "5", "6", "B"],
        ["7", "8", "9", "C"],
        ["*", "0", "#", "D"]
    ]

    # 行列の行と列ピンを定義
    row_pins = [Pin(pin_num, Pin.OUT) for pin_num in [21, 20, 19, 18]]  # R1-R4
    col_pins = [Pin(pin_num, Pin.IN, Pin.PULL_DOWN) for pin_num in [13, 12, 11, 10]]  # C1-C4

    # キーパッドをスキャンする関数
    def read_keypad():
        for row_num, row_pin in enumerate(row_pins):
            row_pin.high()
            for col_num, col_pin in enumerate(col_pins):
                if col_pin.value() == 1:
                    row_pin.low()
                    return keypad_map[row_num][col_num]
            row_pin.low()
        return None

    # ゲームを初期化する関数
    def init_game():
        global target_number, lower_bound, upper_bound, guess
        target_number = urandom.randint(0, 99)
        lower_bound = 0
        upper_bound = 99
        guess = ""
        lcd.clear()
        lcd.message("Press A to Start")

    # 表示を更新する関数
    def update_display(message):
        lcd.clear()
        lcd.message(message)

    # メインプログラム
    init_game()
    game_started = False

    while True:
        key = read_keypad()
        if key:
            utime.sleep(0.2)  # デバウンス遅延

            if not game_started:
                if key == "A":
                    game_started = True
                    update_display("Enter your guess:")
            else:
                if key in "0123456789":
                    if len(guess) < 2:
                        guess += key
                        update_display("Guess: {}\n{} < ? < {}".format(guess, lower_bound, upper_bound))
                elif key == "D":
                    if guess != "":
                        guess_number = int(guess)
                        if guess_number < lower_bound or guess_number > upper_bound:
                            update_display("Out of range!\n{} < ? < {}".format(lower_bound, upper_bound))
                        elif guess_number > target_number:
                            upper_bound = guess_number - 1
                            guess = ""
                            update_display("Too High!\n{} < ? < {}".format(lower_bound, upper_bound))
                        elif guess_number < target_number:
                            lower_bound = guess_number + 1
                            guess = ""
                            update_display("Too Low!\n{} < ? < {}".format(lower_bound, upper_bound))
                        else:
                            update_display("Correct!\nNumber is {}".format(target_number))
                            game_started = False
                            utime.sleep(2)
                            init_game()
                    else:
                        update_display("Enter a number")
                elif key == "A":
                    # ゲームを再開
                    init_game()
                    game_started = True
                    update_display("Enter your guess:")
                elif key == "B":
                    # 現在の推測をクリア
                    guess = ""
                    update_display("Guess cleared")
                elif key == "C":
                    # ヒントを表示（または他の機能）
                    update_display("Hint not available")
        utime.sleep(0.1)

ゲームが実行されると、次の手順でゲームをプレイできます：

* ゲーム開始：

  キーパッドの「A」キーを押します。

* 推測の入力：

  * 数字キーを使って推測を入力します（0〜99）。
  * 「D」を押して推測を送信します。

* フィードバックの受け取り：

  * LCDは、推測が高すぎるか、低すぎるか、正しいかを表示します。
  * 範囲が適切に調整されます。

* ゲームに勝つ：

  * 正しい数字を推測すると、LCDに「Correct! Number is XX」と表示されます。
  * ゲームは短い遅延の後、自動的にリセットされます。

**コードの理解**

#. インポートと初期化：

   * ``lcd1602.LCD``: LCDディスプレイを制御します。
   * ``machine.Pin``: GPIOピンとの対話。
   * ``urandom``: ランダムな数字を生成します。
   * LCD1602ディスプレイのためにI2C通信を初期化します。

#. キーパッドスキャン関数（ ``read_keypad`` ）：

   * 各行を一度に高く設定。
   * どの列が高いかをチェックし、ボタンが押されたことを検出します。
   * 押されたキーに対応するキャラクターを返します。

   .. code-block:: python

        def read_keypad():
            for row_num, row_pin in enumerate(row_pins):
                row_pin.high()
                for col_num, col_pin in enumerate(col_pins):
                    if col_pin.value() == 1:
                        row_pin.low()
                        return keypad_map[row_num][col_num]
                row_pin.low()
            return None

#. ゲーム変数と初期化（ ``init_game`` ）：

   * ``target_number``: 0から99までのランダムな数。
   * ``lower_bound`` と ``upper_bound``: 最初はそれぞれ0と99。
   * ``guess``: 現在の推測入力を格納する文字列。

   .. code-block:: python

        def init_game():
            global target_number, lower_bound, upper_bound, guess
            target_number = urandom.randint(0, 99)
            lower_bound = 0
            upper_bound = 99
            guess = ""
            lcd.clear()
            lcd.message("Press A to Start")

#. 表示更新関数（ ``update_display`` ）：

   LCDをクリアし、指定されたメッセージを表示します。

   .. code-block:: python

        # 表示関数
        def update_display(message):
            lcd.clear()
            lcd.message(message)

#. メインプログラムループ：

   * キー入力を待機し、ゲームロジックを処理します。
   * ``A`` キー: ゲームを開始または再開します。
   * 数字 ``0`` 〜 ``9`` : 現在の推測番号を構築します。
   * ``D`` キー: 推測を送信し、範囲を更新します。
   * 推測が現在の範囲内にあるかを確認します。
   * 推測に基づいて ``lower_bound`` または ``upper_bound`` を更新します。
   * 次の入力のために推測をリセットします。
   * 推測が正しい場合、成功メッセージを表示し、ゲームをリセットします。
   * ``B`` キー: 現在の推測をクリアします。
   * ``C`` キー: 追加機能のために予約されています（例: ヒント）。

   .. code-block:: python

        while True:
            key = read_keypad()
            if key:
                utime.sleep(0.2)  # デバウンス遅延

                if not game_started:
                    if key == "A":
                        game_started = True
                        update_display("Enter your guess:")
        ...
        ...
            utime.sleep(0.1)

#. デバウンスと遅延：


   * ``utime.sleep(0.2)``: キーを押した後のデバウンス用の短い遅延。
   * ``utime.sleep(0.1)``: メインループでCPUの使用を減らすための小さな遅延。

**トラブルシューティング**

* LCDがテキストを表示しない：

  * SDAとSCLの接続（GP6とGP7）を確認します。
  * LCDが正しく電源が供給されているか確認します。
  * LCDモジュールの背面にあるコントラストポテンショメータを調整します。

* キーパッドが反応しない：

  * すべての行と列の接続を確認します。
  * 内部プルダウンを使用しない場合、プルダウン抵抗が正しく接続されていることを確認します。
  * キーパッドが正常に動作していることを確認します。

* ランダムな数が変わらない：

  * ``urandom`` が正しくインポートされて使用されていることを確認します。
  * より良いランダム性のためにランダムシードを初期化する必要があるかもしれません。

* ゲームロジックに問題がある：

  * 推測を処理する際の条件と範囲を再確認します。
  * 上限と下限が正しく更新されているかを確認します。

**拡張と強化**

* マルチプレイヤー対応：

  * 各プレイヤーが何回推測したかを追跡します。
  * プレイヤーごとにターンを交代させます。

* スコアシステムの実装：

  * 数字を推測する速さに応じてポイントを付与します。
  * スコアをLCDに表示します。

* ヒントの提供：

  * 「C」キーを使ってヒントを表示します。例えば「数は偶数です」や「5の倍数です」など。

* 範囲の拡大：

  * ゲームを0から999までの数字に変更します。
  * 表示と入力方法をそれに応じて調整します。

* 視覚的および音声フィードバック：

  * LEDやブザーを追加してフィードバックを提供します。

**結論**

Raspberry Pi Pico 2 Wを使用して、インタラクティブな「数当てゲーム」を作成しました！このプロジェクトは、ユーザー入力、ランダムな数字の生成、表示の制御を組み合わせて、楽しく魅力的なゲームを作成します。キー入力、LCDディスプレイ、ゲームロジックの操作の練習に最適です。

新しい機能を追加したり、インターフェースを改善したりして、このゲームをさらに強化してください。このプロジェクトは、より複雑なインタラクティブアプリケーションの基盤となるでしょう。
