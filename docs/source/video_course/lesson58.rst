.. note::

    こんにちは、FacebookでSunFounder Raspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32について、同じ趣味を持つ仲間と深く探求しましょう。

    **参加する理由は？**

    - **専門家のサポート**: コミュニティやチームの支援を受けて、販売後の問題や技術的な課題を解決します。
    - **学びと共有**: スキルアップに役立つヒントやチュートリアルを交換します。
    - **独占プレビュー**: 新製品の発表や先行公開に早期アクセスができます。
    - **特別割引**: 最新製品を独占的な割引で楽しめます。
    - **祭りのプロモーションとギフトの抽選**: ギフトの抽選やホリデープロモーションに参加します。

    👉 私たちと一緒に探索し、創造しませんか？[|link_sf_facebook|]をクリックして今日参加しましょう！

レッスン58: MicroPythonでジョイスティックの角度を測定する
=============================================================================

このチュートリアルでは、Raspberry Pi Pico Wを使用してジョイスティックの調整について説明します：

* **配線セットアップ**: グランドをピン38、3.3Vをピン36、VRXをGPIOピン27、VRYをGPIOピン26に接続します。
* **コード実装**: 必要なライブラリをインポートします。ジョイスティック軸のADCを設定し、調整用の値を読み取ります。
* **キャリブレーション**: 生のADC値を-100から+100のスケールに変換します。三角法を使用してジョイスティックの角度を計算します。
* **宿題課題**: ジョイスティックの角度に基づいてサーボモーターを制御するプログラムを書き、0度から180度までの正確な追跡を確保してください。

**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/KpDIv0i41Tw?si=PUEInyKbRTIUcvCa" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
