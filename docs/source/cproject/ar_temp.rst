.. note:: 

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！ Raspberry Pi、Arduino、ESP32について、仲間たちと一緒にさらに深く学びましょう。

    **なぜ参加するべきか？**

    - **専門的なサポート**：コミュニティやチームの助けを借りて、購入後の問題や技術的な課題を解決します。
    - **学び＆共有**：スキルを向上させるためのヒントやチュートリアルを交換しましょう。
    - **限定プレビュー**：新製品の発表や先行情報をいち早く入手できます。
    - **特別割引**：最新の製品に対する専用の割引を楽しめます。
    - **季節限定プロモーションやプレゼント**：プレゼント企画やホリデープロモーションに参加しましょう。

    👉 一緒に探求し、創造してみませんか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _ar_temp:

2.13 サーモメーター
===========================

このレッスンでは、Raspberry Pi Pico 2 Wを使用して **サーミスタ** で温度を測定する方法を学びます。サーミスタは、温度によって抵抗が大きく変化するタイプの抵抗です。特に、温度が上昇すると抵抗が減少する負の温度係数（NTC）サーミスタを使用します。

* :ref:`cpn_thermistor`


**必要なコンポーネント**

このプロジェクトに必要なコンポーネントは以下の通りです。

セットで購入すると便利です。こちらのリンクから購入できます：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前	
        - このキットに含まれているアイテム
        - 購入リンク
    *   - Pico 2 Wスターターキット	
        - 450+
        - |link_pico2w_kit|

以下のリンクから個別に購入することもできます。


.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - 番号
        - コンポーネント紹介	
        - 数量
        - 購入リンク

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
        - 1（10KΩ）
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_thermistor`
        - 1
        - |link_thermistor_buy|


**サーミスタの理解**

NTCサーミスタは、温度に敏感な抵抗器です。温度が上昇すると抵抗が減少します。これを電圧分割回路に組み込むことで、温度に応じて変化する電圧を測定できます。Raspberry Pi Pico 2 Wのアナログ-デジタルコンバーター（ADC）を使用して、この電圧を読み取り、対応する温度を計算することができます。

**回路図**

|sch_temp|

この回路では、10KΩの抵抗とNTCサーミスタが電圧分割回路を形成し、GP28がサーミスタにかかる電圧を読み取ります。10KΩの抵抗は、電流を制限することにより保護も提供します。

* **高温時**：サーミスタの抵抗が減少し、電圧が低下、GP28の読み取り値も低くなります。十分に高い温度では、抵抗がゼロに近づき、GP28の値は0に近くなります。
* **低温時**：サーミスタの抵抗が増加し、電圧が上昇、GP28の値も高くなります。極端な寒さでは、抵抗がほぼ無限大になり、GP28の読み取り値は1023に近づきます。

10KΩの抵抗は、3.3VとGNDが直接接続されないようにし、ショートを防ぎます。



**配線**

|wiring_temp|

.. #. Pico 2 Wの3V3とGNDをブレッドボードの電源バスに接続します。
.. #. サーミスタの一方のリードをGP28ピンに接続し、同じリードを10KΩの抵抗を通して正の電源バスに接続します。
.. #. サーミスタのもう一方のリードを負の電源バスに接続します。

**コードの記述**

.. note::

    * ``2.13_thermometer.ino`` ファイルは ``pico-2w-kit-main/arduino/2.13_thermometer`` パスにあります。
    * あるいは、このコードを **Arduino IDE** にコピーしてください。
    * **アップロード** ボタンをクリックする前に、ボード（Raspberry Pi Pico）と適切なポートを選択することを忘れないでください。

.. code-block:: arduino

    // ピンの定義
    const int thermistorPin = 28;  // サーミスタが接続されたGP28（ADC2）

    // サーミスタと計算のための定数
    const float BETA = 3950;       // サーミスタのベータ値（製造元から提供）
    const float SERIES_RESISTOR = 10000; // 10KΩの抵抗
    const float NOMINAL_RESISTANCE = 10000; // 25°Cでの抵抗値（製造元から提供）
    const float NOMINAL_TEMPERATURE = 25.0; // 25°Cの温度

    void setup() {
      Serial.begin(115200);  // シリアルモニターを初期化
    }

    void loop() {
      // サーミスタからアナログ値を読み取る
      int adcValue = analogRead(thermistorPin);
      // ADC値を電圧に変換
      float voltage = adcValue * (3.3 / 1023.0);
      // サーミスタの抵抗を計算
      float resistance = (voltage * SERIES_RESISTOR) / (3.3-voltage);
      // ベータ式を使用してケルビン温度を計算
      float temperatureK = 1 / ( (1 / (NOMINAL_TEMPERATURE + 273.15)) + (1 / BETA) * log(resistance / NOMINAL_RESISTANCE) );
      // ケルビンを摂氏に変換
      float temperatureC = temperatureK - 273.15;
      // 摂氏を華氏に変換
      float temperatureF = (temperatureC * 9.0 / 5.0) + 32.0;

      // 温度の読み取り結果を表示
      Serial.print("Temperature: ");
      Serial.print(temperatureC);
      Serial.print(" °C, ");
      Serial.print(temperatureF);
      Serial.println(" °F");

      delay(1000);  // 次の読み取り前に1秒待機
    }

コードが実行され、シリアルモニターが開いているとき：

* 摂氏と華氏で温度が表示されるはずです。
* サーミスタを指で優しく挟むと、温度が上がるにつれて読み取り値が増加するはずです。
* サーミスタに冷たい空気を吹きかけたり、冷たい物体を近づけたりすると、温度が下がるはずです。

**コードの理解**

#. ピンと定数の定義：

   サーミスタの読み取りに使用するGPIOピンを設定します。

   .. code-block:: arduino

        const int thermistorPin = 28;  // サーミスタが接続されたGP28（ADC2）

#. 計算のための定数：

   温度を計算するために使用する定数です。

   .. code-block:: arduino

        const float BETA = 3950;       // サーミスタのベータ値
        const float SERIES_RESISTOR = 10000; // 10KΩの抵抗
        const float NOMINAL_RESISTANCE = 10000; // 25°Cでの抵抗値
        const float NOMINAL_TEMPERATURE = 25.0; // 25°C

#. アナログ値の読み取り：

   thermistorPinでサーミスタのアナログ電圧を読み取り、0から1023の値を返します。

   .. code-block:: arduino

        int adcValue = analogRead(thermistorPin);

#. 電圧の計算：

   ADC値を実際の電圧に変換します。

   .. code-block:: arduino

        float voltage = adcValue * (3.3 / 1023.0);

#. サーミスタの抵抗の計算：

   電圧分割の公式を使用してサーミスタの抵抗を計算します。

   .. code-block:: arduino

        float resistance = (voltage * SERIES_RESISTOR) / (3.3-voltage);

#. 温度の計算：

   ベータ式を使用して温度を計算します。

   .. code-block:: arduino

        float temperatureK = 1 / ( (1 / (NOMINAL_TEMPERATURE + 273.15)) + (1 / BETA) * log(resistance / NOMINAL_RESISTANCE) );
        float temperatureC = temperatureK - 273.15;
        float temperatureF = (temperatureC * 9.0 / 5.0) + 32.0;

#. 温度の表示：

   シリアルモニターに摂氏と華氏の温度を出力します。

   .. code-block:: arduino

        Serial.print("Temperature: ");
        Serial.print(temperatureC);
        Serial.print(" °C, ");
        Serial.print(temperatureF);
        Serial.println(" °F");

#. 遅延：

   次の読み取りまで1秒間待機します。

   .. code-block:: arduino

        delay(1000);

**温度計算の理解**

* スタインハート・ハート方程式：

スタインハート・ハート方程式は、サーミスタの抵抗を温度の関数としてモデル化します：

|temp_format|

* ``T`` はサーミスタの温度（ケルビン）。
* ``T0`` は基準温度、通常は25°C（ケルビンでは273.15 + 25）。
* ``B`` は材料のベータパラメータ。このキットで使用するNTCサーミスタのベータ係数は3950です。
* ``R`` は測定した抵抗値。
* ``R0`` は基準温度T0での抵抗値。このキットで使用するNTCサーミスタの25°Cでの抵抗値は10キロオームです。

**精度についての注意**

* サーミスタは非線形のデバイスであり、ベータ式は近似値を提供します。
* より広い範囲で正確な温度測定を行うためには、スタインハート・ハート方程式を使用することができます。
* 精密な用途にはキャリブレーションが必要な場合があります。

**さらなる探求**

* LCDに温度を表示する：

  LCDディスプレイを接続して、コンピュータなしで温度を表示できるようにします。

* データロギング：

  時間経過に伴う温度の変化を記録し、環境の変化を監視します。

* 温度制御デバイス：

  温度読み取り結果を使用して、ファンやヒーターを制御します。

**結論**

このレッスンでは、Raspberry Pi Picoを使用してサーミスタで温度を測定する方法を学びました。電圧分割回路を作成し、ベータ式を使用してアナログ値を読み取り、抵抗を計算し、摂氏と華氏の両方で温度を求めることができました。
