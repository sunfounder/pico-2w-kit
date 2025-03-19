.. note:: 

    こんにちは！FacebookのSunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Raspberry Pi、Arduino、ESP32を深く学び、仲間たちと一緒に探求していきましょう。

    **なぜ参加するのか？**

    - **専門的なサポート**: コミュニティやチームのサポートで、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換し、スキルを向上させましょう。
    - **独占的な先行公開**: 新製品の発表や先取り情報に早期アクセスできます。
    - **特別割引**: 最新製品の特別割引を楽しめます。
    - **祭りのプロモーションとギブアウェイ**: ギブアウェイやホリデープロモーションに参加できます。

    👉 私たちと一緒に探索し、創造を始めましょう！[|link_sf_facebook|]をクリックして、今すぐ参加してください！

.. _py_photoresistor:

2.12 光を感じる
=============================

このレッスンでは、Raspberry Pi Pico 2 Wを使用して **フォトレジスター** （光依存抵抗器またはLDRとしても知られています）で光の強度を測定する方法を学びます。フォトレジスターは、受ける光の量に応じてその抵抗が変化します。光が強いほど、抵抗は低くなります。これにより、周囲の光の変化を検出するのに理想的なセンサーとなります。

* :ref:`cpn_photoresistor`

**必要な部品**

このプロジェクトで必要な部品は以下の通りです。

全ての部品がセットになったキットを購入するのが便利です。こちらのリンクをご覧ください：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前    
        - このキットのアイテム
        - リンク
    *   - Pico 2 Wスターターキット    
        - 450+
        - |link_pico2w_kit|

また、以下のリンクから部品を個別に購入することもできます。


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
        - 数本
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_resistor`
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_photoresistor`
        - 1
        - |link_photoresistor_buy|


**回路図**

|sch_photoresistor|

この回路では、10KΩの抵抗とフォトレジスターが直列に接続され、電圧分割器を形成しています。GP28はフォトレジスターを通過する電圧を読み取ります。一方、10KΩ抵抗は電流を制限して保護の役割を果たします。

* **明るい光**: フォトレジスターの抵抗が減少し、その電圧とGP28の読み取り値が低くなります。強い光の中では、その抵抗はゼロに近づき、GP28は0に近い値を読み取ります。この時、10KΩ抵抗は保護的な役割を果たし、3.3VとGNDが接続されることによるショートを防ぎます。
* **暗闇**: フォトレジスターの抵抗が増加し、その電圧とGP28の値が上昇します。完全な暗闇では、その抵抗はほぼ無限大（10KΩ抵抗は無視できる）となり、GP28は65535に近い値を読み取ります。

計算式は以下の通りです。

.. code-block::

  デジタル値 = (アナログ電圧/3.3V) * 65535



**配線**

|wiring_photoresistor|

**コードの記述**

フォトレジスターからアナログ値を読み取り、表示するためのMicroPythonプログラムを作成します。

.. note::

  * ``pico-2w-kit-main/micropython`` の ``2.12_feel_the_light.py`` ファイルを開くか、以下のコードをThonnyにコピーします。次に「現在のスクリプトを実行」をクリックするか、 **F5** を押して実行します。
  * Thonnyの右下に「MicroPython（Raspberry Pi Pico）.COMxx」のインタープリタが選択されていることを確認してください。
  * 詳細な手順については :ref:`open_run_code_py` を参照してください。

.. code-block:: python

    import machine
    import utime

    # GP28のADCを初期化
    photoresistor = machine.ADC(28)

    while True:
        # アナログ値（0-65535）を読み取る
        light_value = photoresistor.read_u16()
        print("Light value:", light_value)
        utime.sleep(0.5)

コードを実行すると、コンソールに表示された値を観察します。

* フォトレジスターに手をかざして暗闇をシミュレートします。値は増加するはずです。
* フォトレジスターに光や懐中電灯を当てると、値は減少するはずです。

**コードの理解**

#. モジュールのインポート：

   * ``machine``: ハードウェア関連の関数にアクセスします。
   * ``utime``: 時間関連の関数（スリープなど）を使用します。

#. ADCピンの初期化：

   * ``photoresistor = machine.ADC(28)``: GP28をアナログ入力として設定し、電圧レベルを読み取ります。

#. メインループ：

   ``while True``: 無限ループを開始します。
   ``light_value = photoresistor.read_u16()``: フォトレジスターからアナログ値を読み取ります。値は0（0V）から65535（3.3V）までの範囲です。
   ``print("Light value:", light_value)``: 光の値をコンソールに出力します。
   ``utime.sleep(0.5)``: 次の読み取り前に0.5秒間待機します。

**さらに実験する**

* 測定値のキャリブレーション：

  アナログ値をパーセンテージやより意味のあるスケールにマッピングします。

  .. code-block:: python
  
      import machine
      import utime
  
      photoresistor = machine.ADC(28)
  
      while True:
          light_value = photoresistor.read_u16()
          light_percentage = (light_value / 65535) * 100
          print("Light level: {:.2f}%".format(light_percentage))
          utime.sleep(0.5)

* 光の強度に基づいてLEDを制御：

  光センサーを使用して、暗闇でLEDを点灯させ、明るい光でLEDを消灯させます。

  .. code-block:: python

    import machine
    import utime

    photoresistor = machine.ADC(28)
    led = machine.Pin(15, machine.Pin.OUT)

    while True:
        light_value = photoresistor.read_u16()
        if light_value > 50000:
            led.value(1)  # 暗闇でLEDを点灯
        else:
            led.value(0)  # 明るい光でLEDを消灯
        utime.sleep(0.5)

* 光で作動するアラームや通知を作成：

  光のレベルが大きく変化したときにアクションをトリガーします。

**結論**

Raspberry Pi Pico 2 Wとフォトレジスターを使用して、アナログ入力を読み取り、環境光の変化に応じて反応する方法を学びました。この知識は、自動照明システム、光追従ロボット、または光の変化に反応するセキュリティデバイスなど、さまざまなプロジェクトに応用できます。
