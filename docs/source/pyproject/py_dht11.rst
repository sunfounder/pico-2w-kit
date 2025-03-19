.. note:: 
    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！Facebookで仲間と一緒に、Raspberry Pi、Arduino、ESP32について深く学んでいきましょう。

    **なぜ参加するべきか？**

    - **専門家のサポート**: コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び・シェア**: ヒントやチュートリアルを交換して、スキルを向上させましょう。
    - **限定プレビュー**: 新製品の発表や先取り情報をいち早くゲットできます。
    - **特別割引**: 最新製品を特別価格でお得に購入できます。
    - **お祭りプロモーションとプレゼント**: プレゼントやホリデープロモーションに参加できます。

    👉 一緒に探求して、創造していきませんか？[|link_sf_facebook|]をクリックして、今すぐ参加しよう！

.. _py_dht11:

6.2 DHT11を使った温度と湿度の測定
=======================================================

このレッスンでは、Raspberry Pi Pico 2 Wを使って **DHT11温湿度センサー** を使用する方法を学びます。DHT11は、周囲の温度と湿度を測定できる、基本的で低価格なデジタルセンサーで、キャリブレーションされたデジタル出力を提供します。

|img_Dht11|

* :ref:`cpn_dht11`

**必要な部品**

このプロジェクトに必要な部品は以下の通りです。

一式購入するのが便利です。リンクはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名称
        - このキットに含まれる部品
        - リンク
    *   - Pico 2 Wスターターキット
        - 450+
        - |link_pico2w_kit|

以下のリンクから個別に購入することもできます。


.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - 部品
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
        - :ref:`cpn_dht11`
        - 1
        - |link_dht22_buy|

**DHT11センサーの理解**

**DHT11** センサーは、周囲の空気を測定するために、キャパシタンス型湿度センサーと熱抵抗素子を使用しています。データピンでデジタル信号を出力し、使いやすいですが、データを読み取るためには正確なタイミングが必要です。

* 温度範囲：0〜50 °C、精度±2 °C
* 湿度範囲：20〜80% RH、精度±5%
* サンプリングレート：1 Hz（1秒ごと）

**回路図**

|sch_dht11|


**配線図**


|wiring_dht11|

**コードの作成**

DHT11センサーから温度と湿度の値を読み取るためのMicroPythonプログラムを書きます。

.. note::

    * ``6.2_temperature_humidity.py`` を ``pico-2w-kit-main/micropython`` から開くか、コードをThonnyにコピーして、「実行」ボタンをクリックするか、F5を押してください。
    * 正しいインタプリタが選択されていることを確認してください：MicroPython (Raspberry Pi Pico).COMxx。


    
    * このコードでは ``dht.py`` ライブラリを使用します。ライブラリがPicoにアップロードされているか確認してください。詳細なチュートリアルについては :ref:`add_libraries_py` を参照してください。

.. code-block:: python

   from machine import Pin
   import utime
   import dht

   # DHT11センサーの初期化
   sensor = dht.DHT11(Pin(16))

   while True:
      try:
         # 測定開始
         sensor.measure()
         # 値を読み取る
         temperature = sensor.temperature  # 摂氏
         humidity = sensor.humidity        # パーセント
         # 値を表示
         print("Temperature: {}°C   Humidity: {}%".format(temperature, humidity))
      except OSError as e:
         print("Failed to read sensor.")
      # 次の読み取り前に待機
      utime.sleep(2)

コードが実行されると、温度と湿度の値がThonnyシェルに表示されます。

.. code-block::

  Temperature: 29.3°C   Humidity: 60.0%
  Temperature: 29.2°C   Humidity: 60.0%
  Temperature: 29.2°C   Humidity: 60.0%
  Temperature: 29.1°C   Humidity: 60.0%
  Temperature: 29.2°C   Humidity: 60.0%
  Temperature: 29.3°C   Humidity: 60.0%

**コードの理解**

#. モジュールのインポート:

   * ``machine.Pin``: GPIOピンを制御するためのモジュール。
   * ``utime``: 時間関連の関数を含むモジュール。
   * ``dht``: DHTセンサー用のライブラリ。

#. センサーの初期化:

   .. code-block:: python

      sensor = dht.DHT11(Pin(16))
      Creates an instance of the DHT11 sensor connected to GP16.

#. メインループ:

   * ``sensor.measure()``: センサーに測定を開始させます。
   * ``sensor.temperature``: 摂氏の温度を読み取ります。
   * ``sensor.humidity``: 湿度のパーセントを読み取ります。
   * ``Exception Handling``: 読み取り中のエラーをキャッチします。
   * ``utime.sleep(2)``: 2秒間待機して、次の読み取りを行います。

   .. code-block:: python

      while True:
         try:
            sensor.measure()
            temperature = sensor.temperature
            humidity = sensor.humidity
            print("Temperature: {}°C   Humidity: {}%".format(temperature, humidity))
         except OSError as e:
            print("Failed to read sensor.")
         utime.sleep(2)

**さらに試してみる**

* 摂氏を華氏に変換する:

   .. code-block:: python

      temperature_f = temperature * 9 / 5 + 32
      print("Temperature: {}°F   Humidity: {}%".format(temperature_f, humidity))

* LCDに読み取り結果を表示する:

  LCDディスプレイを統合して、コンピュータなしで結果を表示します。


* アラートを設定する:

  温度や湿度が特定の閾値を超えたときに、LEDやブザーでアラートを出すように設定します。

**トラブルシューティングのヒント**

* 読み取りエラー:

  * センサーが正しく接続されていることを確認してください。
  * ワイヤの緩みや接続不良を確認してください。

* センサーの読み取りに失敗:

  タイミングの問題で発生することがあります。コードにはこのエラーを処理するためのtry-exceptブロックが含まれています。

* プルアップ抵抗:

  センサーが動作しない場合、センサーが必要とする場合は、VCCとデータピンの間にプルアップ抵抗を接続してください。

**結論**

このレッスンでは、Raspberry Pi Pico 2を使用してDHT11温湿度センサーを操作する方法を学びました。環境条件を監視することは、天気予報システムやホームオートメーションシステムなど、さまざまなプロジェクトの基本的な要素です。

* `Try Statement - Python Docs <https://docs.python.org/3/reference/compound_stmts.html?#the-try-statement>`_
