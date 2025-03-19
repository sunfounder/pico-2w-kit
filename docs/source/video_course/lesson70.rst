.. note::

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32について、同じ趣味を持つ仲間と深く探求しましょう。

    **参加する理由は？**

    - **専門家のサポート**: コミュニティやチームの支援を受けて、販売後の問題や技術的な課題を解決します。
    - **学びと共有**: スキルアップに役立つヒントやチュートリアルを交換します。
    - **独占プレビュー**: 新製品の発表や先行公開に早期アクセスができます。
    - **特別割引**: 最新製品を独占的な割引で楽しめます。
    - **祭りのプロモーションとギフトの抽選**: ギフトの抽選やホリデープロモーションに参加します。

    👉 私たちと一緒に探索し、創造しませんか？[|link_sf_facebook|]をクリックして今日参加しましょう！

レッスン70: MicroPythonでデュアルコアプログラムをきれいに終了する例
===================================================================================

このチュートリアルでは、Raspberry Pi Pico Wを使用してサーボとボタンを制御するためのスレッド使用について説明します：

* **配線セットアップ**: サーボコントロールをGPIO 17に接続し、電源をピン40、グランドをピン38に接続します。ボタンをGPIO 16とグランドに接続します。
* **コード実装**: ``machine``, ``time``, ``_thread``, ``Servo`` をインポートします。ボタンとサーボのピンを設定します。サーボの位置を制御するトグルスイッチを実装します。サーボの動きとプログラムのきれいな終了のためにスレッドを使用します。
* **宿題課題**: サーボの動き中に中断された場合でも、プログラムがきれいに終了するように修正してください。


**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/UHbboCxIOYE?si=eDDi-2mYO0LSWSLJ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
