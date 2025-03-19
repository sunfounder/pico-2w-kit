.. note::

    FacebookでのSunFounder Raspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32のさらなる深堀りを一緒に楽しんでいきましょう。

    **なぜ参加すべきか？**

    - **エキスパートサポート**: 当コミュニティおよびチームの助けを借りて、販売後の問題や技術的な挑戦を解決します。
    - **学習＆共有**: ヒントやチュートリアルを交換し、スキルを向上させます。
    - **独占的なプレビュー**: 新製品発表や先取り情報を早期に入手。
    - **特別割引**: 最新製品を独占的な割引価格で享受。
    - **祭りのプロモーションとギブアウェイ**: ギブアウェイや休日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索して創造しませんか？[|link_sf_facebook|]をクリックして今日から参加しましょう！

レッスン45：自由落下中の物体から高さを計算する
=============================================================================

このチュートリアルでは、MPU6050センサーをRaspberry Pi Pico Wと組み合わせて垂直距離を測定します：

* **セットアップ**: MPU6050とOLED 1306をRaspberry Pi Pico Wに接続し、ノイズを減らすために接続が安定していることを確認します。
* **コンセプト**: 自由落下の時間（T_drop）を計算し、その時間を使って落下した高さを求めます。
* **公式**: 高さ（H）を \( H = 16 \times (T_{drop})^2 \) で計算し、時間をミリ秒から秒に変換します。
* **コード実装**: ライブラリを設定し、Z軸の加速度を測定して0Gを検出、自由落下中にタイマーを開始し、落下時間と高さをOLEDに表示します。
* **実地デモンストレーション**: 既知の高さからセンサーを落としてテストし、必要に応じて精度を調整します。

**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/xpHDAcdrTF0?si=NdmV4J5G6DhJ4f6M" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
