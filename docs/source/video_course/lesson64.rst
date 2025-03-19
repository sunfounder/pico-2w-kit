.. note::

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32について、同じ趣味を持つ仲間と深く探求しましょう。

    **参加する理由は？**

    - **専門家のサポート**: コミュニティやチームの支援を受けて、販売後の問題や技術的な課題を解決します。
    - **学びと共有**: スキルアップに役立つヒントやチュートリアルを交換します。
    - **独占プレビュー**: 新製品の発表や先行公開に早期アクセスができます。
    - **特別割引**: 最新製品を独占的な割引で楽しめます。
    - **祭りのプロモーションとギフトの抽選**: ギフトの抽選やホリデープロモーションに参加します。

    👉 私たちと一緒に探索し、創造しませんか？[|link_sf_facebook|]をクリックして今日参加しましょう！

レッスン64: MicroPythonでLEDを使用したオブジェクト指向プログラミングの例
===================================================================================

このチュートリアルでは、Raspberry Pi Pico Wを使用してLEDの制御に焦点を当てたオブジェクト指向プログラミング（OOP）について説明します：

* **配線セットアップ**: 赤いLEDをGPIO 15に、緑のLEDをGPIO 14に接続し、330オームの抵抗を通してグランドに接続します。
* **クラスとメソッド**:

   1. ``LED`` クラスを定義します。
   2. ``__init__`` でピンを設定します。
   3. LEDを制御する ``blink`` メソッドを実装します。

* **コード実装**:

   1. ``machine`` と ``time`` をインポートします。
   2. ``__init__`` と ``blink`` を持つ ``LED`` クラスを作成します。
   3. 赤と緑のLEDをインスタンス化します。
  

**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/3wyCL9QK_uY?si=G0GXEHqdo2jQ_F-5" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
