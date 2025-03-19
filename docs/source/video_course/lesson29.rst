.. note::

    こんにちは、FacebookでSunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Raspberry Pi、Arduino、ESP32の深い洞察を仲間と共に探求しましょう。

    **参加する理由は？**

    - **専門家のサポート**: 販売後の問題や技術的な課題を、コミュニティやチームのサポートを得て解決します。
    - **学習＆共有**: スキルを向上させるためのヒントやチュートリアルを交換します。
    - **独占プレビュー**: 新製品発表や特別情報への早期アクセスが可能です。
    - **特別割引**: 最新製品に対する独占割引をお楽しみください。
    - **祭りのプロモーションとギブアウェイ**: ギブアウェイや祝日のプロモーションに参加します。

    👉 私たちと一緒に探索し、創造しましょうか？[|link_sf_facebook|]をクリックして今日参加してください！

レッスン29：RGB LEDを制御するシンプルなクライアントサーバープロジェクト
=============================================================================

このチュートリアルでは、Raspberry Pi Pico WとPCをWi-Fi経由で使用してリモート制御可能なRGB LEDを設定する方法について説明します：

* **はじめに**: 目標は、Wi-Fiを使用してRaspberry Pi Pico W上のRGB LEDを遠隔から制御することです。
* **配線図とセットアップ**: RGB LEDをGPIOピン16, 17, 18に接続し、OLEDをGPIOピン2（SDA）と3（SCL）に接続します。
* **サーバー側のセットアップ**: ライブラリをインポートし、GPIOピンを初期化し、Wi-Fiに接続してUDPサーバーを作成し、OLEDにIPを表示します。
* **クライアント側のセットアップ**: PC上にUDPクライアントを作成し、サーバーに色のコマンドを送信します。
* **実践デモンストレーション**: PCから送信されたコマンドによってRGB LEDの色が変化する様子と、OLEDがコマンドとIPを表示する様子を示します。
* **最終セットアップとテスト**: Raspberry Pi Pico Wをバッテリーで動作させ、「main.py」としてコードを保存し、ワイヤレス操作をデモンストレーションします。


**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/eZTETVkX-N8?si=TtZ6B4-Ljm75rhPB" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
