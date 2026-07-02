.. note:: 

    こんにちは、FacebookのSunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！ Raspberry Pi、Arduino、ESP32について、他の愛好者とともにさらに深く学びましょう。

    **なぜ参加するべきか？**

    - **専門家のサポート**: 購入後の問題や技術的な課題を、コミュニティやチームのサポートを受けて解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換して、スキルを向上させましょう。
    - **限定プレビュー**: 新製品の発表やプレビューを早期にチェックできます。
    - **特別割引**: 新製品に対する独占的な割引をお楽しみいただけます。
    - **季節限定のプロモーションやプレゼント**: プレゼント企画やホリデープロモーションに参加できます。

    👉 一緒に探求し、創造を楽しむ準備はできましたか？ [|link_sf_facebook|] をクリックして、今すぐ参加してください！

.. _cpn_buzzer:

ブザー
========


ブザーは、一般的にDCで駆動される統合された構造を持つ電子部品です。コンピュータ、プリンタ、コピー機、アラーム、電子おもちゃ、自動車電子機器、電話、タイマー、その他の電子製品や音響信号デバイスなど、さまざまなデバイスに広く使用されています。

ブザーは、アクティブ型とパッシブ型の2種類に分類されます（下記の画像を参照）。種類を識別するには、ブザーを回転させてピンが上向きになるようにします。パッシブブザーは緑色の回路基板を特徴とし、アクティブブザーは黒いテープで囲まれています。

|img_buzzer|

アクティブブザーとパッシブブザーの違い：

アクティブブザーには内蔵された発振源があり、電源が供給されるとすぐに音を発生させます。一方、パッシブブザーには内蔵の発振源がないため、DC信号で駆動されても音を出しません。代わりに、動作するためには2 kHzから5 kHzの周波数を持つ方形波が必要です。追加の内部回路があるため、アクティブブザーは通常、パッシブブザーよりも高価です。

ブザーの電気的記号は以下の通りです。2つのピンがあり、1つは正、もう1つは負です。表面に「+」と記載されているピンがアノードを示し、もう一方のピンはカソードを示します。

|img_buzzer_symbol|

ブザーのピンを確認できます。長いピンがアノードで、短いピンがカソードです。接続時にこれらを間違えないようにしてください。そうしないと、ブザーが音を出しません。

`Buzzer - Wikipedia <https://en.wikipedia.org/wiki/Buzzer>`_

.. Example
.. -------------------

.. :ref:`Intruder Alarm`

.. :ref:`Custom Tone`

**例**

* :ref:`py_ac_buz` (MicroPythonユーザー向け)
* :ref:`py_pa_buz` (MicroPythonユーザー向け)
* :ref:`py_light_theremin` (MicroPythonユーザー向け)
* :ref:`py_alarm_lamp` (MicroPythonユーザー向け)
* :ref:`py_music_player` (MicroPythonユーザー向け)
* :ref:`py_fruit_piano` (MicroPythonユーザー向け)
* :ref:`py_reversing_aid` (MicroPythonユーザー向け)
* :ref:`py_iot_mqtt_subscribe` (MicroPythonユーザー向け)
* :ref:`py_iot_ble_piano` (MicroPythonユーザー向け)
* :ref:`ar_ac_buz` (Arduinoユーザー向け)
* :ref:`ar_pa_buz` (Arduinoユーザー向け)

.. * :ref:`per_service_bell` (Piper Makeユーザー向け)
.. * :ref:`per_reversing_system` (Piper Makeユーザー向け)
.. * :ref:`per_reaction_game` (Piper Makeユーザー向け)
