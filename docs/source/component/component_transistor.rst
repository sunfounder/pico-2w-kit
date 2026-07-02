.. note:: 

    こんにちは！FacebookのSunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Raspberry Pi、Arduino、ESP32について、仲間たちと一緒にさらに深く学びましょう。

    **参加する理由は？**

    - **専門的なサポート**：コミュニティとチームの助けを借りて、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**：スキルを向上させるためのヒントやチュートリアルを交換しましょう。
    - **限定プレビュー**：新製品の発表や先行公開情報をいち早くチェックできます。
    - **特別割引**：最新製品を特別価格でお得に購入できます。
    - **季節限定プロモーションやプレゼント企画**：プレゼント企画や特別なプロモーションに参加できます。

    👉 一緒に探索し、創造を楽しみませんか？[|link_sf_facebook|] をクリックして今すぐ参加しましょう！

.. _cpn_transistor:

トランジスタ
===============

|img_NPN&PNP|

トランジスタは、電流で電流を制御する半導体素子です。弱い信号を大きな振幅の信号に増幅することで動作し、非接触スイッチとしても使用されます。

トランジスタは、P型およびN型半導体で構成された3層構造を持っています。内部で3つの領域を形成し、その中で最も薄い部分がベース領域であり、他の2つはどちらもN型またはP型の領域です。小さな領域で多数キャリアが集中しているのがエミッタ領域で、もう一方がコレクタ領域です。この構成により、トランジスタは増幅器として機能します。
これらの3つの領域からそれぞれベース（b）、エミッタ（e）、コレクタ（c）の3つの端子が生成され、2つのP-N接合、すなわちエミッタ接合とコレクタ接合を形成します。トランジスタ回路記号内の矢印の向きは、エミッタ接合の向きを示しています。

* `P–N junction - Wikipedia <https://en.wikipedia.org/wiki/P-n_junction>`_

半導体の種類に基づいて、トランジスタはNPN型とPNP型の2つのグループに分けられます。略語から、前者は2つのN型半導体と1つのP型半導体で構成され、後者はその逆であることが分かります。以下の図を参照してください。

.. note::
    s8550はPNP型トランジスタで、s8050はNPN型トランジスタです。見た目は非常に似ているため、ラベルを確認することが重要です。

|img_transistor_symbol|

高レベル信号がNPN型トランジスタを通過すると、それがエネルギーを供給します。しかし、PNP型トランジスタは低レベル信号を必要とします。両方のタイプのトランジスタは、非接触スイッチとして頻繁に使用されます。この実験でも同様です。


* `S8050 Transistor Datasheet <https://components101.com/asset/sites/default/files/component_datasheet/S8050%20Transistor%20Datasheet.pdf>`_
* `S8550 Transistor Datasheet <https://www.mouser.com/datasheet/2/149/SS8550-118608.pdf>`_

ラベル面を自分に向け、ピンを下に向けて配置します。ピンは左から順にエミッタ（e）、ベース（b）、コレクタ（c）です。

|img_ebc|

.. note::
    * ベースは大きな電力供給を制御するゲートデバイスです。
    * NPN型トランジスタでは、コレクタが大きな電力供給で、エミッタがその電力の出口です。PNP型トランジスタではその逆になります。

.. Example
.. -------------------

.. :ref:`Two Kinds of Transistors`

**例**

* :ref:`py_transistor` (MicroPythonユーザー向け)
* :ref:`py_relay` (MicroPythonユーザー向け)
* :ref:`py_ac_buz` (MicroPythonユーザー向け)
* :ref:`py_pa_buz` (MicroPythonユーザー向け)
* :ref:`py_light_theremin` (MicroPythonユーザー向け)
* :ref:`py_alarm_lamp` (MicroPythonユーザー向け)
* :ref:`py_music_player` (MicroPythonユーザー向け)
* :ref:`py_fruit_piano` (MicroPythonユーザー向け)
* :ref:`py_reversing_aid` (MicroPythonユーザー向け)
* :ref:`ar_ac_buz` (Arduinoユーザー向け)
* :ref:`ar_pa_buz` (Arduinoユーザー向け)
* :ref:`ar_transistor` (Arduinoユーザー向け)
* :ref:`ar_relay` (Arduinoユーザー向け)

.. * :ref:`per_service_bell` (Piper Makeユーザー向け)
.. * :ref:`per_reversing_system` (Piper Makeユーザー向け)
.. * :ref:`per_reaction_game` (Piper Makeユーザー向け)
