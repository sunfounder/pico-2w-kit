.. note::

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32の深い探求を一緒に楽しみましょう。

    **参加する理由は？**

    - **専門家のサポート**: 当コミュニティやチームからのサポートで販売後の問題や技術的な課題を解決します。
    - **学びと共有**: ヒントやチュートリアルを交換してスキルを向上させます。
    - **独占的なプレビュー**: 新製品の発表や先取り情報に早期アクセス。
    - **特別割引**: 最新製品を独占的な割引価格で。
    - **お祭りプロモーションとギブアウェイ**: ギブアウェイやホリデープロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造してみませんか？[|link_sf_facebook|]をクリックして今日から参加しましょう！

レッスン47: ローパスフィルターを使用してセンサーデータを改善
=============================================================================

このチュートリアルでは、MPU6050センサーをRaspberry Pi Pico Wに接続し、ローパスフィルターを実装することで安定した二軸傾斜計を作成します：

* **セットアップ**: MPU6050をRaspberry Pi Pico Wに接続します。
* **コンセプト**: 加速度計のデータを使用して傾斜を測定し、加速度による誤差に対処します。
* **ローパスフィルター**: データを滑らかにするために以下の式を実装します:  ``\(\text{new value} = \text{confidence} \times \text{measurement} + (1 - \text{confidence}) \times \text{old value}\)``。
* **コード**: X、Y、Zを測定し、ピッチとロールの角度をフィルター処理して結果を表示します。
* **宿題**: ローパスフィルターをテストし、信頼度の値を実験してみてください。

**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/3YqGIg4crEk?si=rwiDFcJ98nlj_Sg3" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
