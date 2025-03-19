.. note::

    こんにちは、FacebookでSunFounder Raspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32について、同じ趣味を持つ仲間ともっと深く探求しましょう。

    **参加する理由は？**

    - **専門家のサポート**: コミュニティやチームの支援を受けて、販売後の問題や技術的な課題を解決します。
    - **学びと共有**: スキルアップに役立つヒントやチュートリアルを交換します。
    - **独占プレビュー**: 新製品の発表や先行公開に早期アクセスができます。
    - **特別割引**: 最新製品を独占的な割引で楽しめます。
    - **祭りのプロモーションとギフトの抽選**: ギフトの抽選やホリデープロモーションに参加します。

    👉 私たちと一緒に探索し、創造しませんか？[|link_sf_facebook|]をクリックして今日参加しましょう！

レッスン59: ジョイスティックを使ってサーボを制御する
=============================================================================

このチュートリアルでは、Raspberry Pi Pico Wを使用してジョイスティックでサーボを制御する方法について説明します：

* **配線セットアップ**: ジョイスティックのグランドをピン38、3.3Vをピン36、VRXをGPIO 27、VRYをGPIO 26に接続します。サーボの5Vをピン40、グランドをピン38、制御をGPIO 15に接続します。
* **コード実装**: ``machine``、 ``time``、 ``math`` をインポートします。ジョイスティック用のADCとサーボ用のPWMを設定します。ジョイスティックの値を読み取り、表示します。
* **校正と制御**: ADCの値を-100から+100にスケーリングします。ジョイスティックの角度を計算します。角度をサーボのPWMにマッピングします。
* **宿題課題**: ジョイスティックの角度（0-180度）からサーボを制御するコードを書いてください。


**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/ayY2wOJmrUE?si=HKP8qwd4WMC1et2r" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
