.. note::

    こんにちは、FacebookでSunFounder Raspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32について、同じ趣味を持つ仲間と深く探求しましょう。

    **参加する理由は？**

    - **専門家のサポート**: コミュニティやチームの支援を受けて、販売後の問題や技術的な課題を解決します。
    - **学びと共有**: スキルアップに役立つヒントやチュートリアルを交換します。
    - **独占プレビュー**: 新製品の発表や先行公開に早期アクセスができます。
    - **特別割引**: 最新製品を独占的な割引で楽しめます。
    - **祭りのプロモーションとギフトの抽選**: ギフトの抽選やホリデープロモーションに参加します。

    👉 私たちと一緒に探索し、創造しませんか？[|link_sf_facebook|]をクリックして今日参加しましょう！

レッスン55: MicroPythonでネオピクセルで動的なレインボーを作成する
=============================================================================

このチュートリアルでは、Raspberry Pi Pico WとMicroPythonを使用してネオピクセルアレイに流れるレインボーパターンを作成する方法について説明します：

* **配線セットアップ**: 5V、GND、データピンをPico WのGPIOピン0に接続します。
* **コンセプト説明**: HSV値を増分させ、それぞれのピクセルに適用することで流れるレインボーパターンを作成します。
* **コード実装**: HSVをRGBに変換する関数を使用します。HSVカラーホイールを巡るネストされたループを実装し、ネオピクセルアレイを更新します。
* **デモンストレーションとテスト**: 流れるレインボーパターンを表示し、トラブルシューティングのヒントを提供します。
* **宿題課題**: 新しいパターンを実験し、コミュニティと結果を共有してください。


**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/lZYEQLorXMY?si=nj7LHGxmNnCoVfqi" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
