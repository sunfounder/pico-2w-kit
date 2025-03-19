.. note:: 

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！仲間たちと一緒にRaspberry Pi、Arduino、ESP32についてさらに深く学びましょう。

    **参加する理由は？**

    - **専門家のサポート**: コミュニティやチームの助けを借りて、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換して、スキルを向上させましょう。
    - **限定プレビュー**: 新製品の発表や先行情報をいち早く手に入れましょう。
    - **特別割引**: 最新製品の特別割引をお楽しみください。
    - **イベント・プレゼント**: プレゼント企画や祝日セールに参加しましょう。

    👉 一緒に探求し、創造を楽しみませんか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _py_iot_sunfounder_controller:

8.8 @SunFounder Controllerで遊ぼう
====================================

このプロジェクトでは、Sunfounder Controllerアプリを使用してリモートプロジェクトを構築する方法を学びます。
LAN環境では、Pico 2 Wの回路をスマートフォンやタブレットで制御することができます。
Pico 2 Wでシンプルなロボットを作りたい場合、このアプリは非常に便利です。

ここでは、アプリのスライダーバーを使用してサーボの角度を制御し、アプリのゲージで超音波センサーが検出した距離を表示します。

**1. 必要なコンポーネント**

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
        - :ref:`cpn_servo`
        - 1
        - |link_servo_buy|
    *   - 6
        - :ref:`cpn_ultrasonic`
        - 1
        - |link_ultrasonic_buy|
    *   - 7
        - :ref:`cpn_lipo_charger`
        - 1
        -  
    *   - 8
        - 18650バッテリー
        - 1
        -  

**2. 回路を組み立てる**

    .. warning:: 
        
        Li-po充電モジュールが図のように接続されていることを確認してください。そうしないと、短絡が原因でバッテリーや回路が損傷する可能性があります。

.. image:: img/wiring/9.sc_bb.png
    :width: 800


**3. SunFounder Controllerをセットアップする**

1. `SunFounder Controller APP <https://docs.sunfounder.com/projects/sf-controller/en/latest/>`_ を **APP Store(iOS)** または **Google Play(Android)** からインストールします。

2. アプリを開き、ホームページで **+** ボタンをクリックしてコントローラーを作成します。

    .. image:: img/sc-a-2.jpg
        :width: 800

3. ここで **Blank** と **Dual Stick** を選択します。

    .. image:: img/sc-a-3.jpg
        :width: 800

4. これで空のコントローラーが作成されます。

    .. image:: img/sc-a-4.jpg
        :width: 800

5. **H** エリアをクリックし、 **Slider** ウィジェットを追加します。

    .. image:: img/sc-a-5.jpg
        :width: 800

6. コントロールのギアをクリックして、設定ウィンドウを開きます。

    .. image:: img/sc-a-6.png
        :width: 300

7. 最大値を180、最小値を0に設定し、 **確認** をクリックします。

    .. image:: img/sc-a-7.jpg
        :width: 800

8. **L** エリアをクリックし、 **Gauge** ウィジェットを追加します。

    .. image:: img/sc-a-8.jpg
        :width: 800

9. ゲージのギアをクリックして設定ウィンドウを開き、最大値を100、最小値を0、単位をcmに設定します。

    .. image:: img/sc-a-9.jpg
        :width: 800

10. ウィジェットの設定が完了したら、保存をクリックします。

    .. image:: img/sc-a-10.png
        :width: 300



**4. コードを実行する**

.. note:: 
    Pico 2 Wが現在Anvilファームウェアを使用している場合、 :ref:`install_micropython_on_pico` が必要です。

1. ``pico-2w-kit-main/micropython/libs`` のパスから ``ws.py`` と ``websocket_helper.py`` をRaspberry Pi Pico 2 Wにアップロードします。

    .. image:: img/9_sc3.png

2. ``ws.py`` スクリプトをダブルクリックし、WiFiの ``SSID`` と ``PASSWORD`` を入力します。

    .. image:: img/9_sc1.png

3. ``pico-2w-kit-main/micropython/iot`` のパスにある ``9_sunfounder_controller.py`` を開き、 **現在のスクリプトを実行** ボタンをクリックするか、F5を押して実行します。接続が成功すると、Pico 2 WのIPアドレスが表示されます。

    .. image:: img/9_sc2.png

    .. note::
        このスクリプトを起動時に実行できるようにするには、Raspberry Pi Pico 2 Wに ``main.py`` として保存できます。

4. SunFounder Controllerアプリに戻り、 **接続** ボタンをクリックします。

    .. image:: img/sc-c-4.jpg
        :width: 300

5. Pico Wが検出された場合、直接タップして接続します。

    .. image:: img/sc-c-5.jpg
        :width: 300

6. 自動で検索されない場合は、手動でIPを入力して接続できます。

    .. image:: img/sc-c-6.png
        :width: 800

7. 実行ボタンをクリックした後、Hエリアのスライダーバーをスライドさせると、サーボが角度を調整します。Lエリアのゲージは、手が超音波センサーから100cm以内にある場合、その距離を表示します。

    .. image:: img/sc-c-8.jpg
        :width: 300

**仕組みは？**

``ws.py`` ライブラリの ``WS_Server`` クラスは、アプリとの通信を実装しています。以下はその基本機能を実装するためのフレームワークです。

.. code-block:: python

    from ws import WS_Server
    import json
    import time

    ws = WS_Server(8765) # WebSocketを初期化

    def main():
        ws.start()
        while True:
            status,result=ws.transfer()
            time.sleep_ms(100)

    try:
        main()
    finally:
        ws.stop()


まず、 ``WS_Server`` オブジェクトを作成する必要があります。

.. code-block:: python

    ws = WS_Server(8765)

次に、 ``ws.start()`` を呼び出してWebSocketを開始します。

.. code-block:: python

    ws.start()

次に、 ``while True`` ループを使用して、Pico 2 WとSunFounder Controllerアプリ間でデータ転送を行います。

.. code-block:: python

    while True:
        # WebSocketデータ転送
        status,result = ws.transfer()

        # データ転送のステータス
        print(status)

        # 受信したデータ
        print(result)

        # 送信したデータ
        print(ws.send_dict)


        time.sleep_ms(100)

``status`` が ``False`` の場合、SunFounder Controllerアプリからデータを取得できなかったことを意味します。

そして、 ``result`` はPico 2 WがSunFounder Controllerアプリから取得したデータです。
出力すると、次のようなデータが表示されます。これはすべてのウィジェットエリアの値です。

.. code-block:: 

    {'C': None, 'B': None, 'M': None,,,,, 'A': None, 'R': None}

この場合、Hエリアの値を個別に表示して、それを回路の操作に使用します。

.. code-block:: python

        status,result=ws.transfer()
        #print(result)
        if status == True:
            print(result['H'])


``ws.send_dict`` 辞書は、Pico 2 WがSunFounder Controllerアプリに送信するデータです。これは ``WS_Server`` クラスで作成され、 ``ws.transfer()`` が実行されると送信されます。

そのメッセージは以下のように表示されます。

.. code-block:: python

    {'Check': 'SunFounder Controller', 'Name': 'Pico2W', 'Type': 'Blank'}

これは空のメッセージです。これをSunFounder Controllerアプリのウィジェットにコピーするには、対応するエリアに値を割り当てる必要があります。例えば、Lエリアに値 ``50`` を割り当てます。

.. code-block:: python

        ws.send_dict['L'] = 50

データは以下のように表示されます。

.. code-block:: python

    {'L': 50, 'Type': 'Blank', 'Name': 'Pico2W', 'Check': 'SunFounder Controller'}


SunFounder Controllerの詳細な使い方については、 `SunFounder Controller APP <https://docs.sunfounder.com/projects/sf-controller/en/latest/>`_ を参照してください。