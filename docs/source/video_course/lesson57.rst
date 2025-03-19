.. note::

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32について、同じ趣味を持つ仲間ともっと深く探求しましょう。

    **参加する理由は？**

    - **専門家のサポート**: コミュニティやチームの支援を受けて、販売後の問題や技術的な課題を解決します。
    - **学びと共有**: スキルアップに役立つヒントやチュートリアルを交換します。
    - **独占プレビュー**: 新製品の発表や先行公開に早期アクセスができます。
    - **特別割引**: 最新製品を独占的な割引で楽しめます。
    - **祭りのプロモーションとギフトの抽選**: ギフトの抽選やホリデープロモーションに参加します。

    👉 私たちと一緒に探索し、創造しませんか？[|link_sf_facebook|]をクリックして今日参加しましょう！

レッスン57: MicroPythonでジョイスティックを調整する
=============================================================================

このチュートリアルでは、Raspberry Pi Pico Wを使用してジョイスティックの調整について説明します：

* **配線セットアップ**: グランドをピン38、3.3Vをピン36、VRXをGPIOピン27、VRYをGPIOピン26に接続します。
* **コード実装**: ``machine`` 、 ``time`` 、 ``math`` をインポートし、ジョイスティック軸のためのADCを設定し、ジョイスティックの値を読み取って表示します。
* **キャリブレーション**: 生のADC値を-100から+100のスケールに変換し、ニュートラル位置のノイズを調整します。
* **宿題課題**: ジョイスティックの位置に基づいて角度を計算し報告するプログラムを書いてください。

**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/rRHyho4vwIQ?si=cV75rrwEWSYoKhAN" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
