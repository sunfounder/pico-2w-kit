.. note::

    こんにちは、FacebookでSunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Raspberry Pi、Arduino、ESP32の深い洞察を仲間と共に探求しましょう。

    **参加する理由は？**

    - **専門家のサポート**: 販売後の問題や技術的な課題を、コミュニティやチームのサポートを得て解決します。
    - **学習＆共有**: スキルを向上させるためのヒントやチュートリアルを交換します。
    - **独占プレビュー**: 新製品発表や特別情報への早期アクセスが可能です。
    - **特別割引**: 最新製品に対する独占割引をお楽しみください。
    - **祭りのプロモーションとギブアウェイ**: ギブアウェイや祝日のプロモーションに参加します。

    👉 私たちと一緒に探索し、創造しましょうか？[|link_sf_facebook|]をクリックして今日参加してください！

レッスン34：MicropythonでHSVからRGBへの変換
=============================================================================
このチュートリアルでは、Raspberry Pi Pico Wを使用してHSV（色相、彩度、明度）の色値をRGB（赤、緑、青）の色値に変換し、それをRGB LEDで表示する方法について説明します：

* **HSVカラーホイールの紹介**: HSVカラーホイールと、特に温度データの視覚化において滑らかな色の変化に利用する方法について説明します。
* **プロジェクトの設定と目標**: 気象ステーションプロジェクトの概要と、温度に対するRGB LEDの色表現を追加する目標の復習。
* **HSVからRGBへの変換理解**: HSVカラーホイールの数学的表現、ゾーン、及びRGB変換について説明します。
* **アルゴリズム開発**: HSVからRGB値に変換する関数を作成し、Raspberry Pi Pico WのPWMを使用してRGB LEDを設定します。
* **コード実装**: PWM制御とHSVからRGBへの変換のためのPythonコードの実行手順を説明し、ライブラリ関数を含みます。
* **実践デモンストレーション**: HSVに基づいてRGB LEDの色変化を示し、気象ステーションプロジェクトへのLEDの統合を課題として割り当てます。



**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/gg_hYPiCn_U?si=V32plkV0jGdV-4qV" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
