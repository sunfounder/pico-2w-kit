.. note::

    こんにちは、FacebookでSunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Raspberry Pi、Arduino、ESP32の深い洞察を仲間と共に探求しましょう。

    **参加する理由は？**

    - **専門家のサポート**: 販売後の問題や技術的な課題を、コミュニティやチームのサポートを得て解決します。
    - **学習＆共有**: スキルを向上させるためのヒントやチュートリアルを交換します。
    - **独占プレビュー**: 新製品発表や特別情報への早期アクセスが可能です。
    - **特別割引**: 最新製品に対する独占割引をお楽しみください。
    - **祭りのプロモーションとギブアウェイ**: ギブアウェイや祝日のプロモーションに参加します。

    👉 私たちと一緒に探索し、創造しましょうか？[|link_sf_facebook|]をクリックして今日参加してください！

レッスン32：モバイル気象ステーションプロジェクト
=============================================================================

このチュートリアルでは、Raspberry Pi Pico Wを使用して携帯型気象ステーションを作成する方法について説明します：

* **WiFiへの接続**: ライブラリをインポートし、WLANオブジェクトを作成してWiFiに接続します。
* **天気データの取得**: OpenWeatherMap APIを使用してリアルタイムの天気データを取得し、APIキーが必要です。
* **JSONデータの解析**: JSONレスポンスから気温、湿度、気圧、日の出と日の入りの時間を抽出します。
* **OLEDでのデータ表示**: OLEDディスプレイを設定し接続し、「ssd1306」ライブラリを使用して、画面に天気データをループで更新します。
* **デバイスの電源供給**: Raspberry Pi Pico Wをバッテリーで駆動し、携帯性を確保します。
* **コード説明**: OLEDを初期化し、WiFiに接続して天気データを取得・表示し、定期的な更新のためのループを設定します。
* **宿題**: 温度、湿度、風速に基づいて天気条件を示すためのRGB LEDを追加します。



**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/zovC4CvR1Hw?si=d_lhJvfzTC3pR5cS" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
