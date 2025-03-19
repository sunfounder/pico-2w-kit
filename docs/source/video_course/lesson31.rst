.. note::

    こんにちは、FacebookでSunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Raspberry Pi、Arduino、ESP32の深い洞察を仲間と共に探求しましょう。

    **参加する理由は？**

    - **専門家のサポート**: 販売後の問題や技術的な課題を、コミュニティやチームのサポートを得て解決します。
    - **学習＆共有**: スキルを向上させるためのヒントやチュートリアルを交換します。
    - **独占プレビュー**: 新製品発表や特別情報への早期アクセスが可能です。
    - **特別割引**: 最新製品に対する独占割引をお楽しみください。
    - **祭りのプロモーションとギブアウェイ**: ギブアウェイや祝日のプロモーションに参加します。

    👉 私たちと一緒に探索し、創造しましょうか？[|link_sf_facebook|]をクリックして今日参加してください！

レッスン31：センサーレスリモート気象ステーションプロジェクト
=============================================================================

このチュートリアルでは、Raspberry Pi Pico Wを使用してセンサーレス気象ステーションを作成する方法について説明します：

* **WiFiへの接続**: ライブラリをインポートし、WLANオブジェクトを使用してWiFiに接続します。
* **天気データの取得**: OpenWeatherMap APIを使用してリアルタイムの天気データを取得し、APIキーが必要です。
* **JSONデータの解析**: JSONレスポンスから気温、湿度、気圧、日の出と日の入りの時間を抽出します。
* **コード説明**: ``urequests.get()`` を使用してデータを取得し、Unix時間を変換し、気圧単位を調整します。
* **天気データの表示**: 気温、湿度、気圧、天候条件、風速を表示します。
* **宿題**: ディスプレイを追加し、携帯型でバッテリー駆動の気象ステーションを作成します。



**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/hbcA90S7Jtk?si=mHMxKUEEpqiYM7DA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
