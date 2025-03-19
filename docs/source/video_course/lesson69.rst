.. note::

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32について、同じ趣味を持つ仲間と深く探求しましょう。

    **参加する理由は？**

    - **専門家のサポート**: コミュニティやチームの支援を受けて、販売後の問題や技術的な課題を解決します。
    - **学びと共有**: スキルアップに役立つヒントやチュートリアルを交換します。
    - **独占プレビュー**: 新製品の発表や先行公開に早期アクセスができます。
    - **特別割引**: 最新製品を独占的な割引で楽しめます。
    - **祭りのプロモーションとギフトの抽選**: ギフトの抽選やホリデープロモーションに参加します。

    👉 私たちと一緒に探索し、創造しませんか？[|link_sf_facebook|]をクリックして今日参加しましょう！

レッスン69: プログラム終了時にMicroPythonスレッドをきれいに終了させる
===================================================================================

このチュートリアルでは、Raspberry Pi Pico Wを使用して両コアでサーボとLEDを制御する方法について説明します：

* **配線セットアップ**: 赤いLEDをGPIO 15、緑のLEDをGPIO 14、サーボをGPIO 17に接続し、電源をピン40、グランドをピン38に接続します。
* **コード実装**: ``machine``, ``time``, ``_thread``, ``Servo`` をインポートします。LEDとサーボのピンを設定します。サーボの動きに基づいてLEDを点滅させる ``other_core`` を定義します。サーボとLEDを制御するループを作成します。
* **宿題課題**: コードを変更して、時計回りのサーボ動作で赤いLED、反時計回りで緑のLEDが点滅するようにします。


**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/mcXxqx0lZYo?si=tIek_zJ4EMuZ3bC4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
