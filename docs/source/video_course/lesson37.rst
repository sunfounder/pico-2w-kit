.. note::

    こんにちは、FacebookでSunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Raspberry Pi、Arduino、ESP32の深い洞察を仲間と共に探求しましょう。

    **参加する理由は？**

    - **専門家のサポート**: 販売後の問題や技術的な課題を、コミュニティやチームのサポートを得て解決します。
    - **学習＆共有**: スキルを向上させるためのヒントやチュートリアルを交換します。
    - **独占プレビュー**: 新製品発表や特別情報への早期アクセスが可能です。
    - **特別割引**: 最新製品に対する独占割引をお楽しみください。
    - **祭りのプロモーションとギブアウェイ**: ギブアウェイや祝日のプロモーションに参加します。

    👉 私たちと一緒に探索し、創造しましょうか？[|link_sf_facebook|]をクリックして今日参加してください！

レッスン37：MicroPythonでポテンショメーターを使ってサーボを制御
=============================================================================
このチュートリアルでは、Raspberry Pi Pico Wを使ってポテンショメーターでサーボモーターを制御する方法について説明します：

* **サーボモーターの制御**: SG90サーボをRaspberry Pi Pico Wに接続します。接続はグラウンド、電源（5V）、そしてGPIOピン15に制御線。
* **配線セットアップ**: ポテンショメーターを3.3V、グラウンド、そしてGPIOピン26のシグナルに接続します。
* **PWMの基本**: PWMを50Hzで使用して、サーボの位置を制御します。
* **コード説明**: GPIO 15でPWMを設定し、ポテンショメーターの入力をサーボの角度に変換します。
* **実演**: コードを実行してポテンショメーターでサーボを制御します。サーボホーンの手動回転は避けてください。
* **応用アイデア**: 外部電源を使用して、より大きなサーボを制御し、高度なプロジェクトに応用します。


**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/iiJasGsLTrQ?si=f-avwQIJNypRuh4t" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
