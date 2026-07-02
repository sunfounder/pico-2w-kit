.. note::

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32について、同じ趣味を持つ仲間ともっと深く探求しましょう。

    **参加する理由は？**

    - **専門家のサポート**: 販売後の問題や技術的な課題を、コミュニティやチームのサポートを受けて解決します。
    - **学びと共有**: スキルアップに役立つヒントやチュートリアルを交換しましょう。
    - **独占プレビュー**: 新商品の発表やちら見せに早期アクセスが可能です。
    - **特別割引**: 最新商品を独占的な割引価格でお楽しみいただけます。
    - **祭りプロモーションとギフトの抽選**: ギフトの抽選や祝日のプロモーションに参加しましょう。

    👉 一緒に探索して創造してみませんか？[|link_sf_facebook|]をクリックして今すぐ参加！

.. _cpn_pico_2w:

Pico 2 Wの概要
=======================================

|pico_2w_side|

Raspberry Pi Pico 2 Wは、2.4GHzの802.11n無線LANとBluetooth 5.2を搭載しており、IoTやスマート製品の設計においてさらなる柔軟性を提供し、プロジェクトの可能性を広げます。
ステーションモードとアクセスポイントモードの両方で操作が可能です。C言語とMicroPythonの開発者にネットワーク機能へのフルアクセスが提供されます。
Raspberry Pi Pico 2 Wは、RP2350マイクロコントローラーと4MBのフラッシュメモリを搭載し、1.8～5.5Vの入力電圧をサポートする電源チップがあります。26個のGPIOピンを提供し、そのうち3つはアナログ入力として機能します。0.1インチピッチのスルーホールパッドにはキャステレーションが施されています。
Raspberry Pi Pico 2 Wは、単体または480単位のリールでの自動組立に向けて提供されています。

機能
--------------
* RP2350マイクロコントローラーを搭載し、4MBのフラッシュメモリがあります。
* オンボードの2.4GHz無線インターフェース（802.11n、Bluetooth 5.2）。
  - Bluetooth LEのセントラルおよびペリフェラルロールをサポート。
  - Bluetoothクラシックをサポート。
* マイクロUSB Bポートは電源とデータのためのものです（フラッシュの再プログラムも可能）。
* 40ピン、21mm×51mmの「DIP」スタイルの1mm厚PCBで、0.1インチのスルーホールピンもキャステレーションが施されています。
  - 26個の多機能3.3V GPIO（一般目的入出力）を露出。
  - 23個のGPIOはデジタル専用で、そのうち3つはADC対応可能。
  - モジュールとしての表面実装が可能。
* 3ピンのArmシリアルワイヤデバッグ（SWD）ポート。
* シンプルかつ高度に柔軟な電源供給アーキテクチャ。
  - マイクロUSB、外部電源、またはバッテリーから簡単に電源を供給するための様々なオプションがあります。
* USB 1.1コントローラーおよびPHYを1つ搭載し、ホストおよびデバイスサポートがあります。
* 3つのプログラマブルI/O（PIO）ブロック、合計12のステートマシン。
  - フレキシブルでユーザープログラマブルな高速I/O。
  - SDカードやVGAなどのインターフェースをエミュレート可能。
* サポートされている入力電力1.8-5.5V DC。
* 動作温度 -20°Cから+85°C。
* キャステレーションモジュールにより、キャリアボードへの直接はんだ付けが可能。
* USBを介した大量記憶装置を使用したドラッグアンドドロッププログラミング。
* 正確なオンチップクロック。
* 温度センサー。
* チップ上に高速整数および浮動小数点ライブラリが加速されています。

Picoのピン
------------

|pico2w_pin|


.. list-table::
    :widths: 3 5 10
    :header-rows: 1

    *   - 名前
        - 説明
        - 機能
    *   - GP0-GP28
        - 一般目的の入出力ピン
        - 入力または出力として機能し、固有の目的はありません
    *   - GND
        - 0ボルトのグラウンド
        - Pico 2 Wの配線を容易にするためのいくつかのGNDピンがあります。
    *   - RUN
        - Picoの有効/無効を制御
        - 他のマイクロコントローラからPico 2 Wの起動と停止を制御します。
    *   - GPxx_ADCx
        - 一般目的の入出力またはアナログ入力
        - アナログ入力として、またはデジタル入出力として使用可能ですが、同時には使用できません。
    *   - ADC_VREF
        - アナログデジタルコンバータ（ADC）の電圧参照
        - アナログ入力用の参照電圧を設定する特別な入力ピンです。
    *   - AGND
        - アナログデジタルコンバータ（ADC）の0ボルトグラウンド
        - ADC_VREFピンのための特別なグラウンド接続です。
    *   - 3V3(O)
        - 3.3ボルトの電源
        - VSYS入力から生成される、Pico 2 Wが内部で使用するのと同じ3.3Vの電源です。
    *   - 3v3(E)
        - 電源の有効/無効を制御
        - 3V3(O)電源のオン/オフを切り替え、Pico 2 W自体もオフにすることができます。
    *   - VSYS
        - 2-5ボルトの電源
        - Picoの内部電源に直接接続されたピンで、Pico 2 Wをオフにしない限り切断することはできません。
    *   - VBUS
        - 5ボルトの電源
        - PicoのマイクロUSBポートから取得される5Vの電源で、3.3V以上の電力を必要とするハードウェアを駆動するために使用されます。

Raspberry Pi Pico 2 Wの詳細情報、始め方については、 `こちら <https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html>`_ を参照してください。

また、以下のリンクもご覧ください:

* `Raspberry Pi Pico 2製品概要 <https://datasheets.raspberrypi.com/pico/pico-2-product-brief.pdf>`_
* `Raspberry Pi Pico 2 Wデータシート <https://datasheets.raspberrypi.com/picow/pico-2-w-datasheet.pdf>`_
* `Raspberry Pi Picoの始め方：C/C++開発 <https://datasheets.raspberrypi.org/pico/getting-started-with-pico.pdf>`_
* `Raspberry Pi Pico C/C++ SDK <https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-c-sdk.pdf>`_
* `Raspberry Pi Pico C/C++ SDKのAPIレベルDoxygenドキュメント <https://raspberrypi.github.io/pico-sdk-doxygen/>`_
* `Raspberry Pi Pico Python SDK <https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-python-sdk.pdf>`_
* `Raspberry Pi RP2350データシート <https://datasheets.raspberrypi.com/rp2350/rp2350-datasheet.pdf>`_
* `RP2350を用いたハードウェア設計 <https://datasheets.raspberrypi.com/rp2350/hardware-design-with-rp2350.pdf>`_
* `Raspberry Pi Pico W設計ファイル <https://datasheets.raspberrypi.com/picow/RPi-PicoW-PUBLIC-20220607.zip>`_
* `Raspberry Pi Pico W STEPファイル <https://datasheets.raspberrypi.com/picow/PicoW-step.zip>`_
