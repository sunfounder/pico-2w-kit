.. note::

    こんにちは、FacebookでSunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Raspberry Pi、Arduino、ESP32の深い洞察を仲間と共に探求しましょう。

    **参加する理由は？**

    - **専門家のサポート**: 販売後の問題や技術的な課題を、コミュニティやチームのサポートを得て解決します。
    - **学習＆共有**: スキルを向上させるためのヒントやチュートリアルを交換します。
    - **独占プレビュー**: 新製品発表や特別情報への早期アクセスが可能です。
    - **特別割引**: 最新製品に対する独占割引をお楽しみください。
    - **祭りのプロモーションとギブアウェイ**: ギブアウェイや祝日のプロモーションに参加します。

    👉 私たちと一緒に探索し、創造しましょうか？[|link_sf_facebook|]をクリックして今日参加してください！

レッスン35：RGB LED温度指示器付きリモート気象ステーション
=============================================================================
このチュートリアルでは、Raspberry Pi Pico Wを使用して気象ステーションに温度データを表示するRGB LEDを統合する方法について説明します：

* **プロジェクト概要**: Raspberry Pi Pico W、OLEDディスプレイ、およびRGB LEDを使用して、温度を視覚的に表現するリモート気象ステーションを構築します。
* **HSVからRGBへの変換**: 気温を-20°F（バイオレット）から120°F（レッド）までHSVカラーホイール上の角度にマッピングします。
* **回路セットアップ**: OLEDディスプレイとRGB LEDをRaspberry Pi Pico Wに接続し、GPIOとPWMを設定します。
* **コーディング**: 温度データを取得し、色相を計算してRGBに変換し、HSVからRGB変換ライブラリを使用してRGB LEDを制御します。
* **デモンストレーション**: OLEDとRGB LEDに温度を表示し、バッテリー電源でセットアップを実行します。
* **結論**: 異なる色のマッピングや温度範囲でプロジェクトをカスタマイズし、チュートリアルへの対話を奨励します。



**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/c9tQHyQWIYk?si=ORHsIXt8eBGeXDdp" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
