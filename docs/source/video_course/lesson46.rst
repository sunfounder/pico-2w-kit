.. note::

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32のさらなる探求を共に楽しみましょう。

    **なぜ参加するのか？**

    - **エキスパートのサポート**: 当コミュニティやチームの支援で、販売後の問題や技術的な課題を解決します。
    - **学びと共有**: ヒントやチュートリアルを交換して、スキルを向上させます。
    - **独占プレビュー**: 新製品の発表や先取り情報を早期に入手。
    - **特別割引**: 最新製品を独占的な割引価格で提供。
    - **祭りのプロモーションとギブアウェイ**: ギブアウェイやホリデープロモーションに参加しましょう。

    👉 私たちと一緒に探索して創造しませんか？[|link_sf_facebook|]をクリックして今日から参加しましょう！

レッスン46: MPU6050を使用して2軸傾斜計をディスプレイ付きで構築
=============================================================================

このチュートリアルでは、MPU6050センサーをRaspberry Pi Pico Wと組み合わせて2軸傾斜計を作成します：

* **設定**: MPU6050とOLED 1306をRaspberry Pi Pico Wに接続します。
* **コンセプト**: ピッチとロールの角度を使用して傾斜を測定し、OLEDにバブルレベルを表示します。
* **計算式**: 
   - ピッチ: \(\arctan\left(\frac{Y}{Z}\right)\)
   - ロール: \(\arctan\left(\frac{X}{Z}\right)\)
   - ラジアンを度に変換。
* **コード**: ライブラリを設定し、X、Y、Zの加速度を測定、角度を計算し、OLEDに表示。
* **デモンストレーション**: 傾斜をテストし、反応性のためのバブルの動きを調整します。
* **応用**: 加速や振動からの誤差を避けるために傾斜読み取りを安定させます。

**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/wYv39RMwXvU?si=6gJoFFIa1HSdGIFt" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
