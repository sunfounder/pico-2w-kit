.. note::

    こんにちは、FacebookでSunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Raspberry Pi、Arduino、ESP32の深い洞察を仲間と共に探求しましょう。

    **参加する理由は？**

    - **専門家のサポート**: 販売後の問題や技術的な課題を、コミュニティやチームのサポートを得て解決します。
    - **学習＆共有**: スキルを向上させるためのヒントやチュートリアルを交換します。
    - **独占プレビュー**: 新製品発表や特別情報への早期アクセスが可能です。
    - **特別割引**: 最新製品に対する独占割引をお楽しみください。
    - **祭りのプロモーションとギブアウェイ**: ギブアウェイや祝日のプロモーションに参加します。

    👉 私たちと一緒に探索し、創造しましょうか？[|link_sf_facebook|]をクリックして今日参加してください！

レッスン16：MicroPythonでRGB LEDの色のシーケンスを制御
=============================================================================

このチュートリアルでは、Raspberry Pi Pico Wを使用して、MicroPythonでRGB LEDの色を制御する方法について説明します：

* **はじめに**: forループとPWMを使用して、RGB LEDの明るさと色を制御する概要。
* **回路設定**: RGB LEDをGPIOピン13、14、15に接続し、330オームの抵抗を使用します。
* **PWM設定**: 各LEDチャンネルに1000Hzの周波数でPWMを設定し、滑らかな遷移を実現します。
* **色のシーケンス入力**: ユーザーに色のシーケンスを入力させ、入力を配列に保存します。
* **色制御ロジック**: if文を使用して、赤、緑、青、シアン、マゼンタ、黄、オレンジ、オフの色にPWM値を割り当てます。
* **継続的ループ**: while trueループを使用して色のシーケンスを循環し、スリープステートメントを使って間隔を調整します。



**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/VivNlgYg3wY?si=ECUsRAWanIAShyxk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

