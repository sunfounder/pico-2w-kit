.. note:: 

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Facebookで他の愛好者と一緒に、Raspberry Pi、Arduino、ESP32をさらに深く学びましょう。

    **なぜ参加するのか？**

    - **専門的なサポート**：コミュニティとチームのサポートで、販売後の問題や技術的な課題を解決できます。
    - **学びとシェア**：スキルを高めるために、ヒントやチュートリアルを交換しましょう。
    - **限定プレビュー**：新しい製品発表や先行情報に早期アクセスできます。
    - **特別割引**：最新製品に対する限定割引をお楽しみいただけます。
    - **フェスティブプロモーションとプレゼント**：プレゼントやホリデープロモーションに参加しましょう。

    👉 一緒に探求し、創造を始める準備はできましたか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _py_led_bar:

2.2 レベルの表示
=============================

このレッスンでは、Raspberry Pi Picoを使用して **LEDバーグラフ** 制御し、レベルを表示する方法を学びます。LEDバーグラフは、一般的に音量や信号強度、その他の測定値などのレベルを表示するために使用される、10個のLEDが直線状に配置されたものです。LEDを順番に点灯させてレベル表示効果を作り出します。

|img_led_bar_pin|

* :ref:`cpn_led_bar`

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
        - 10(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led_bar`
        - 1
        - 

**回路図**

|sch_ledbar|

このプロジェクトでは、LEDバーグラフの10個のLEDそれぞれがRaspberry Pi Pico 2 Wに接続されています。LEDのアノード（正端子）はGPIOピンGP6からGP15に接続され、カソード（負端子）は220Ωの抵抗を介してGND（グランド）ピンに接続されています。



**配線図**

|wiring_ledbar|

**コードの作成**

.. note::

    * ``pico-2w-kit-main/micropython`` 内の ``2.2_display_the_level.py`` ファイルを開くか、このコードをThonnyにコピーして、「現在のスクリプトを実行」をクリックするか、F5を押して実行してください。

    * Thonnyの右下隅で「MicroPython（Raspberry Pi Pico）。COMxx」が選択されていることを確認してください。

.. code-block:: python

  import machine
  import utime

  # LEDに接続されたGPIOピンを定義
  pins = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
  leds = []

  # 各ピンを出力として初期化し、ledsリストに格納
  for pin_number in pins:
      led = machine.Pin(pin_number, machine.Pin.OUT)
      leds.append(led)

  while True:
      # LEDを1つずつ点灯させてレベルを増加させる
      for led in leds:
          led.value(1)  # LEDをオンにする
          utime.sleep(0.2)
      # LEDを1つずつ消灯させてレベルを減少させる
      for led in leds:
          led.value(0)  # LEDをオフにする
          utime.sleep(0.2)

プログラムを実行すると、LEDバーグラフのLEDが最初から最後まで順番に点灯し、レベルが増加していく効果が得られます。その後、LEDが1つずつ消灯し、レベルが減少していきます。

**コードの理解**

このプロジェクトでは、MicroPythonを使ってリストとループを使用して複数のLEDを制御しており、コードが効率的で読みやすくなっています。

コードの主な部分を分解してみましょう：

1. モジュールのインポート：

   * ``import machine``: Raspberry Pi Pico 2 Wのハードウェア機能へのアクセスを提供します。
   * ``import utime``: 遅延などの時間関連の関数を使用するため。

2. ピンの定義とLEDの初期化：

   * ``pins`` リストには、LEDに接続されたGPIOピンの番号を格納し、空の ``leds`` リストを作成してLEDオブジェクトを格納します。

     .. code-block:: python

      # LEDに接続されたGPIOピンを定義
      pins = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
      leds = []
     
   * ``for`` ループを使用して、各ピン番号を反復処理し、出力ピンとして設定し、対応する ``Pin`` オブジェクトを ``leds`` リストに追加します。
     
     .. code-block:: python

        for pin_number in pins:
            led = machine.Pin(pin_number, machine.Pin.OUT)
            leds.append(led)

3. レベル表示効果の作成：

   * ``while True:`` ループは無限に実行されます。
   * レベルの増加：

     * ``for`` ループを使って、 ``leds`` リスト内の各 ``led`` を反復処理します。
     * ``led.value(1)`` でLEDをオンにします。
     * ``utime.sleep(0.2)`` で次のLEDが点灯する前に200msの遅延を追加します。
     
     .. code-block:: python

        for led in leds:
            led.value(1)
            utime.sleep(0.2)

   * レベルの減少：

     * 別の ``for`` ループを使って、各LEDを順番に消灯させます。
     * ``led.value(0)`` でLEDをオフにします。

     .. code-block:: python

        for led in leds:
            led.value(0)
            utime.sleep(0.2)

**さらに試してみる**

コードを試してみましょう：

* 速度を変更：

  * ``utime.sleep(0.2)`` の遅延を調整して、LEDがより速くまたは遅く点灯するようにします。

* 順序を逆にする：

  * ``reversed(leds)`` を使用して、LEDの順序を逆にします。

    .. code-block:: python

        for led in reversed(leds):
            led.value(1)
            utime.sleep(0.2)

* ピンポン効果を作成：

  * LEDが左から右に点灯し、その後右から左に戻るようにします。

    .. code-block:: python

        while True:
            for led in leds:
                led.value(1)
                utime.sleep(0.1)
            for led in reversed(leds):
                led.value(0)
                utime.sleep(0.1)

**結論**

各LEDを個別に制御することにより、Raspberry Pi Pico 2 Wを使用してシンプルで効果的なレベル表示を作成しました。このプロジェクトは、Pythonのリストとループを活用する力を示し、複数の出力を効率的に管理する方法を学べます。

複数のGPIOピンを使いこなし、リストやループのようなプログラミング構造を利用する方法は、アニメーションの作成、複数のセンサーの制御、インタラクティブなデバイスの構築など、より複雑なプロジェクトに不可欠です。

**参考文献**

* |link_python_for|
* |link_python_list|
