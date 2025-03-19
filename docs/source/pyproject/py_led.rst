.. note:: 

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Facebookで他の愛好者と一緒に、Raspberry Pi、Arduino、ESP32をさらに深く学びましょう。

    **なぜ参加するのか？**

    - **専門的なサポート**：コミュニティとチームのサポートで、販売後の問題や技術的な課題を解決できます。
    - **学びとシェア**：スキルを高めるために、ヒントやチュートリアルを交換しましょう。
    - **限定プレビュー**：新しい製品発表や先行情報に早期アクセスできます。
    - **特別割引**：最新製品に対する限定割引をお楽しみいただけます。
    - **フェスティブプロモーションとプレゼント**：プレゼントやホリデープロモーションに参加しましょう。

    👉 一緒に探求し、創造を始める準備はできましたか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _py_led:

2.1 こんにちは、LED！
=======================================

Raspberry Pi Picoでの最初のハードウェアプロジェクトへようこそ！このレッスンでは、MicroPythonを使ってLEDを点滅させる方法を学びます。このシンプルなプロジェクトは、フィジカルコンピューティングを始め、コードでハードウェアを制御する方法を理解するのに最適です。

* :ref:`cpn_led`

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
        - 1(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|

**回路図**

|sch_led|

GPIOピンを高または低に設定することで、そのピンの電圧出力を制御しています。ピンが高の時、LEDを流れる電流は抵抗によって制限され、LEDが点灯します。ピンが低の時は電流が流れず、LEDは消灯します。

**配線図**

|wiring_led|

**コードの作成**

.. note::

    * ``pico-2w-kit-main/micropython`` 内の ``2.1_hello_led.py`` ファイルを開くか、このコードをThonnyにコピーして、「現在のスクリプトを実行」をクリックするか、F5を押して実行してください。

    * Thonnyの右下隅で「MicroPython（Raspberry Pi Pico）。COMxx」が選択されていることを確認してください。

    * 詳細なチュートリアルについては、 :ref:`open_run_code_py` をご参照ください。

.. code-block:: python

  import machine
  import utime
  
  led = machine.Pin(15, machine.Pin.OUT)
  while True:
      led.value(1)      # LEDをオンにする
      utime.sleep(2)    # 2秒待機
      led.value(0)      # LEDをオフにする
      utime.sleep(2)    # 2秒待機

プログラムを実行すると、LEDは2秒間オンになり、その後2秒間オフになります。


**コードの理解**

このプロジェクトでは、MicroPythonを使ってリストとループで複数のLEDを制御しています。これにより、コードが効率的で読みやすくなります。

コードの主な部分を分解してみましょう：

1. ライブラリのインポート：

   * ``import machine``: Raspberry Pi Pico 2 Wのハードウェアコンポーネントへのアクセスを提供します。
   * ``import utime``: 遅延などの時間関連の関数を使用するため。

2. LEDピンの設定：

   * ``led = machine.Pin(15, machine.Pin.OUT)``: GP15を出力ピンとして初期化し、変数 ``led`` に割り当てます。

3. 無限ループの作成：

   * ``while True``: 終わりのないループを開始し、その中のコードを継続的に実行します。

4. LEDの制御：

   * ``led.value(1)``: ピン出力を高（3.3V）に設定してLEDをオンにします。
   * ``utime.sleep(2)``: プログラムを2秒間一時停止します。
   * ``led.value(0)``: ピン出力を低（0V）に設定してLEDをオフにします。
   * ``utime.sleep(2)``: もう2秒間、プログラムを一時停止します。

**さらに試してみる**

* **点滅速度を変更**: ``utime.sleep(1)`` の値を変更して、LEDの点滅を速くまたは遅くすることができます。
* **異なるピンを使用**: LEDを異なるGPIOピンに接続し、コードをそれに応じて更新してみましょう。
* **複数のLED**: 他のGPIOピンにLEDを追加し、それらをコードで制御してみましょう。

**トラブルシューティング**

* LEDが点灯しない：

  * LEDの向きが正しいことを確認してください。アノードとカソードが正しく接続されているか確認してください。
  * すべての接続がしっかりしているか確認してください。
  * 抵抗がLEDと直列に接続されているか確認してください。

* Thonnyでエラーメッセージが表示される：

  * 正しいインタプリタが選択されていることを確認してください。
  * コードにタイプミスがないか確認してください。

**結論**

おめでとうございます！Raspberry Pi PicoとMicroPythonを使ってLEDを点滅させることに成功しました。この基本的なプロジェクトは、コードでハードウェアを制御する方法を学ぶための良いスタートであり、さらに複雑なプロジェクトに向けた基盤を築くことができます。

**参考文献**

* |link_mpython_machine_pin|
* |link_mpython_machine|
* |link_mpython_utime|
* |link_python_while|