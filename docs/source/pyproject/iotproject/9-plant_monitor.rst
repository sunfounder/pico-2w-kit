.. note:: 

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！仲間たちと一緒にRaspberry Pi、Arduino、ESP32についてさらに深く学びましょう。

    **参加する理由は？**

    - **専門家のサポート**: コミュニティやチームの助けを借りて、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換し、スキルを向上させましょう。
    - **限定プレビュー**: 新製品の発表や先行情報をいち早く手に入れましょう。
    - **特別割引**: 最新製品の特別割引をお楽しみください。
    - **イベント・プレゼント**: プレゼント企画や祝日セールに参加しましょう。

    👉 一緒に探求し、創造を楽しみませんか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _py_iot_sunfounder_controller_plant:

8.9 @SunFounder Controllerでのプラントモニター
================================================

このプロジェクトでは、Sunfounder Controllerアプリを使用して植物の給水システムを構築する方法を学びます。

アプリ上で、環境の現在の温度・湿度や鉢植えの水位を確認できます。
水が不足していると思ったら、アプリのボタンをクリックして植物に給水することも可能です。


**必要なコンポーネント**

このプロジェクトでは、以下のコンポーネントが必要です。

キット一式を購入するのが便利です。こちらのリンクから購入できます：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前	
        - このキットに含まれるアイテム
        - リンク
    *   - Pico 2 W スターターキット	
        - 450以上
        - |link_pico2w_kit|

別々に購入することもできます。以下のリンクから購入可能です。

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - コンポーネント
        - 数量
        - リンク

    *   - 1
        - :ref:`cpn_pico_2w`
        - 1
        - |link_pico2w_buy|
    *   - 2
        - Micro USBケーブル
        - 1
        - 
    *   - 3
        - :ref:`cpn_breadboard`
        - 1
        - |link_breadboard_buy|
    *   - 4
        - :ref:`cpn_wire`
        - 複数
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_dht11`
        - 1
        - |link_dht22_buy|
    *   - 6
        - :ref:`cpn_water_level`
        - 1
        - 
    *   - 7
        - :ref:`cpn_ta6586`
        - 1
        - 
    *   - 8
        - :ref:`cpn_lipo_charger`
        - 1
        -  
    *   - 9
        - Power Pack
        - 1
        -  
    *   - 10
        - :ref:`cpn_pump`
        - 1
        -  

**手順**

.. note::
    事前に :ref:`py_iot_sunfounder_controller` プロジェクトを完了しておくことをお勧めします。SunFounder Controllerの基本的な使い方を理解するのに役立ちます。

#. 回路を組み立てます。

    .. image:: img/wiring/10.sc_2_bb.png

#. 新しいコントローラーを作成し、以下のウィジェットを追加して名前を変更します。

    .. image:: img/10_plant2.jpg
        :width: 800

#. ``pico-2w-kit-main/micropython/iot`` のパスにある ``10_plant_monitor.py`` を開き、 **現在のスクリプトを実行** ボタンをクリックするか、F5を押して実行します。接続が成功すると、Pico 2 WのIPアドレスが表示されます。

    .. image:: img/10_plant_monitor.png


#. SunFounderアプリに戻り、PicoWに接続後にRunをクリックします。アプリ上で環境の温度と湿度、さらに鉢植えの水位を確認できます。水が足りないと感じたら、ボタンをクリックして5秒間の給水を行えます。

    .. image:: img/10_plant2.jpg
        :width: 800

#. このスクリプトを起動時に実行できるようにしたい場合は、Raspberry Pi Pico 2 Wに ``main.py`` として保存できます。



**仕組みは？**

このプロジェクトは、基本的には :ref:`py_iot_sunfounder_controller` と同じ仕組みで動作します。

さらに本プロジェクトでは、DHT11、ポンプ、水位モジュールを使用しています。これらの部品の使用方法については、 :ref:`py_dht11`、 :ref:`py_pump`、 :ref:`py_water` を参照してください。
