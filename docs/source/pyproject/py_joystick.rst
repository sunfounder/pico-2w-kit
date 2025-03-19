.. note:: 

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Raspberry Pi、Arduino、ESP32を使って、他の愛好者と一緒にさらに深く学んでいきましょう。

    **なぜ参加するのか？**

    - **専門的なサポート**：コミュニティとチームのサポートを受けて、販売後の問題や技術的な課題を解決できます。
    - **学びとシェア**：スキルを高めるために、ヒントやチュートリアルを交換しましょう。
    - **限定プレビュー**：新しい製品の発表やスニークピークに早期アクセスできます。
    - **特別割引**：最新製品に対する限定割引を楽しめます。
    - **フェスティブプロモーションとプレゼント**：プレゼントやホリデープロモーションに参加しましょう。

    👉 一緒に探求し、創造を始める準備はできましたか？[|link_sf_facebook|]をクリックして、今日から参加しましょう！

.. _py_joystick:

4.1 ジョイスティックの切り替え
================================

このレッスンでは、 **ジョイスティック** をRaspberry Pi Pico 2 Wで使用して、アナログ値を読み取り、ボタンの押下を検出する方法を学びます。ジョイスティックは、2軸（X軸とY軸）に沿った動きを制御するための一般的な入力デバイスで、押し込むとボタン（Z軸）が含まれることがよくあります。

* :ref:`cpn_joystick`

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
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_joystick`
        - 1
        - 

**ジョイスティックの理解**

典型的なジョイスティックモジュールは、互いに直角に配置された2つのポテンショメータで構成されています。

* **X軸ポテンショメータ**：左右の動きを測定します。
* **Y軸ポテンショメータ**：上下の動きを測定します。
* **Z軸（スイッチ）**：ジョイスティックを押し込むとアクティブになるデジタルボタンです。

X軸とY軸からアナログ値を読み取ることで、ジョイスティックの位置を特定できます。Z軸ボタンは、ジョイスティックが押されているかどうかを検出するために使用されます。

**回路図**

|sch_joystick|

SWピンは10Kプルアップ抵抗に接続されています。これにより、ジョイスティックが押されていないときにSWピン（Z軸）が安定した高レベルの状態になります。それ以外の場合、SWはサスペンド状態になり、出力値が0または1に変動する可能性があります。

**配線**

|wiring_joystick|


**コードの作成**

ジョイスティックのX軸とY軸の位置を読み取り、ボタンの押下を検出するMicroPythonプログラムを作成します。

.. note::

    * ``4.1_toggle_the_joystick.py`` を ``pico-2w-kit-main/micropython`` から開くか、コードをThonnyにコピーして、「実行」ボタンをクリックするか、F5を押してください。
    * 正しいインタープリタが選択されていることを確認してください：MicroPython（Raspberry Pi Pico）。COMxx。



.. code-block:: python

    import machine
    import utime

    # X軸とY軸のADCを初期化
    x_adc = machine.ADC(27)  # GP27
    y_adc = machine.ADC(26)  # GP26

    # スイッチ用デジタル入力を初期化
    z_button = machine.Pin(22, machine.Pin.IN, machine.Pin.PULL_UP)

    while True:
        # アナログ値を読み取る（0-65535）
        x_value = x_adc.read_u16()
        y_value = y_adc.read_u16()
        
        # ボタンの状態を読み取る（0または1）
        z_state = z_button.value()
        
        # 値を表示
        print("X:", x_value, "Y:", y_value, "Button:", z_state)
        
        # 出力を読みやすくするために小さな遅延を追加
        utime.sleep(0.2)


**コードの理解**

#. モジュールのインポート：

   * ``machine``：ハードウェア関連の関数にアクセスするため。
   * ``utime``：遅延用の時間関連の関数。

#. ADC入力の初期化：

   GP27とGP26のピンにアナログ-デジタルコンバータ（ADC）を設定して、ジョイスティックのX軸とY軸の位置を読み取ります。

   .. code-block:: python

      x_adc = machine.ADC(27)  # X軸はGP27に接続
      y_adc = machine.ADC(26)  # Y軸はGP26に接続

#. デジタル入力の初期化：

   * GP22をジョイスティックのボタン（Z軸）のための内部プルアップ抵抗付きデジタル入力として構成します。
   * ``machine.Pin.PULL_UP`` パラメータにより、ボタンが押されていないときにピンは高（1）になり、押されたときは低（0）になります。

   .. code-block:: python

      z_button = machine.Pin(22, machine.Pin.IN, machine.Pin.PULL_UP)

#. メインループでの値の読み取り：

   * アナログ値を読み取ります： ``read_u16()`` は16ビットの値（0〜65535）を読み取り、電圧レベルを表します。
   * 値を表示：コンソールにX軸とY軸の位置、およびボタンの状態を表示します。

   .. code-block:: python

      while True:
          x_value = x_adc.read_u16()
          y_value = y_adc.read_u16()
          z_state = z_button.value()
          
          print("X:", x_value, "Y:", y_value, "Button:", z_state)
          
          utime.sleep(0.2)

プログラムを実行すると、ThonnyでシェルまたはREPLウィンドウにX、Y、ボタンの値が表示されます。

* ジョイスティックを異なる方向に動かし、ボタンを押して値の変化を確認しましょう。

**値の解釈**


* XおよびYの値：

  * 範囲は0から65535。
  * 中央位置：おおよそ32768。
  * 左または上：0に近い。
  * 右または下：65535に近い。

* ボタンの状態：

  * 押されていない：1。
  * 押された：0。

**さらに試してみる**

* 値を正規化する：

  生のADC値を-100から100の範囲に変換して、より解釈しやすくします。

  .. code-block:: python

    import machine
    import utime

    # X軸とY軸のADCを初期化
    x_adc = machine.ADC(27)  # GP27
    y_adc = machine.ADC(26)  # GP26

    # スイッチ用デジタル入力を初期化
    z_button = machine.Pin(22, machine.Pin.IN, machine.Pin.PULL_UP)

    # ADC値を-100から100の範囲に正規化する関数
    def normalize(value):
        return int((value - 32768) / 327.68)

    while True:
        # アナログ値を読み取る（0-65535）
        x_value = x_adc.read_u16()
        y_value = y_adc.read_u16()
        
        # ボタンの状態を読み取る（0または1）
        z_state = z_button.value()
        
        # 値を-100から100に正規化
        x_normalized = normalize(x_value)
        y_normalized = normalize(y_value)
        
        # 正規化された値を表示
        print("X:", x_normalized, "Y:", y_normalized, "Button:", z_state)
        
        # 出力を読みやすくするために小さな遅延を追加
        utime.sleep(0.2)


* 出力を制御する：

  ジョイスティックの入力を使用してLED、サーボ、モーターなどを制御します。例えば、X軸の値に基づいて物体を左または右に動かします。

* ゲームコントローラーを作成する：

  ジョイスティックの入力を組み合わせて、簡単なゲームやグラフィカルな出力を制御します。

**結論**


このレッスンでは、Raspberry Pi Pico 2 Wを使用して、ジョイスティックからのアナログおよびデジタル入力を読み取る方法を学びました。この知識を使って、ロボット、ゲーム、リモコンなど、さまざまなインタラクティブなアプリケーションにジョイスティック制御を組み込むことができます。


