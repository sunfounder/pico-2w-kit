.. note:: 

    こんにちは！FacebookのSunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Raspberry Pi、Arduino、ESP32について、仲間たちと一緒にさらに深く学びましょう。

    **参加する理由は？**

    - **専門的なサポート**：コミュニティとチームの助けを借りて、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**：スキルを向上させるためのヒントやチュートリアルを交換しましょう。
    - **限定プレビュー**：新製品の発表や先行公開情報をいち早くチェックできます。
    - **特別割引**：最新製品を特別価格でお得に購入できます。
    - **季節限定プロモーションやプレゼント企画**：プレゼント企画や特別なプロモーションに参加できます。

    👉 一緒に探索し、創造を楽しみませんか？[|link_sf_facebook|] をクリックして今すぐ参加しましょう！

.. _cpn_led:

LED
==========

|img_led|

LED（発光ダイオード）は、PN接合を通じて電気エネルギーを光エネルギーに変換する半導体素子です。波長に基づいて、これらのダイオードはレーザーダイオード、赤外線発光ダイオード、および一般的にLEDとして知られる可視光発光ダイオードに分類されます。

ダイオードの一方向性導電性により、回路記号の矢印の方向に電流が流れます。LEDを動作させるには、アノードを正の電源に、カソードを負の電源に接続し、LEDが光を放出するようにします。

|img_led_symbol|

LEDには2本のピンがあります。長い方がアノードで、短い方がカソードです。逆接続しないよう注意してください。LEDには固定された順方向電圧降下があり、電源電圧がこの降下を超えるとLEDが焼損する恐れがあるため、直接回路に接続することはできません。赤、黄、緑のLEDの順方向電圧は1.8Vで、白色LEDのそれは2.6Vです。ほとんどのLEDは最大20mAの電流に耐えることができるため、直列に電流制限抵抗を接続する必要があります。

抵抗値の式は次のとおりです：

    R = (Vsupply – VD)/I

ここで、 **R** は電流制限抵抗の抵抗値、 **Vsupply** は電源電圧、 **VD** は電圧降下、 **I** はLEDの動作電流を表します。

LEDについての詳細はこちらを参照してください: `LED - Wikipedia <https://en.wikipedia.org/wiki/Light-emitting_diode>`_.

.. **例**

.. * :ref:`Hello, Breadboard!` (MicroPythonユーザー向け)
.. * :ref:`fading_led_micropython` (MicroPythonユーザー向け)
.. * :ref:`fading_led_arduino` (C/C++(Arduino)ユーザー向け)
.. * :ref:`hello_led_arduino` (C/C++(Arduino)ユーザー向け)

**例**

* :ref:`py_led` (MicroPythonユーザー向け)
* :ref:`py_fade` (MicroPythonユーザー向け)
* :ref:`py_alarm_lamp` (MicroPythonユーザー向け)
* :ref:`py_traffic_light` (MicroPythonユーザー向け)
* :ref:`py_reversing_aid` (MicroPythonユーザー向け)
* :ref:`py_iot_read_ble` (MicroPythonユーザー向け)
* :ref:`py_iot_ble_relay` (MicroPythonユーザー向け)
* :ref:`ar_led` (Arduinoユーザー向け)
* :ref:`ar_fade` (Arduinoユーザー向け)
.. * :ref:`per_blink` (Piper Makeユーザー向け)
.. * :ref:`per_button` (Piper Makeユーザー向け)
.. * :ref:`per_service_bell` (Piper Makeユーザー向け)
.. * :ref:`per_reversing_system` (Piper Makeユーザー向け)
.. * :ref:`per_reaction_game` (Piper Makeユーザー向け)
