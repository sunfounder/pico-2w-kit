.. note:: 

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！仲間たちと一緒にRaspberry Pi、Arduino、ESP32についてさらに深く学びましょう。

    **参加する理由は？**

    - **専門家のサポート**: コミュニティやチームの助けを借りて、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換して、スキルを向上させましょう。
    - **限定プレビュー**: 新製品の発表や先行情報をいち早く手に入れましょう。
    - **特別割引**: 最新製品の特別割引をお楽しみください。
    - **イベント・プレゼント**: プレゼント企画や祝日セールに参加しましょう。

    👉 一緒に探求し、創造を楽しみませんか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _py_iot_cheerlights:

8.2 @CheerLightsに従う
=======================================

このプロジェクトはロマンチックなものです。 |link_cheerlights| LEDの色が世界中のLEDを同時に変えるコミュニティに参加しましょう。

オフィスの一角に置いて、あなたが一人ではないことを思い出させてくれます。

Twitterで@cheerlightsをつぶやき、色の名前を含めることで、世界中のLEDの色を指定した色に変更できます。

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
        - :ref:`cpn_ws2812`
        - 1
        - |link_ws2812_buy|
    *   - 6
        - :ref:`cpn_lipo_charger`
        - 1
        -  
    *   - 7
        - Power Pack
        - 1
        -  


**手順**

#. 回路を組み立てます。

    ここで使用するLi-po充電モジュールは回路に電力を供給するため、USBケーブルを外してプロジェクトを別の場所に持っていって楽しむことができます！

    .. warning:: 
        
        Li-po充電モジュールが図のように接続されていることを確認してください。そうしないと、短絡が原因でバッテリーや回路が損傷する可能性があります。

    .. image:: img/wiring/2.cheerlights_bb.png
        :width: 800

#. 前にダウンロードした`コードパッケージ `code package <https://github.com/sunfounder/pico-2w-kit/archive/refs/heads/main.zip>`_ のフォルダに移動し、 ``8.2_cheer_light.py`` ファイルを開きます。

#. スクリプトを実行するには、 **現在のスクリプトを実行** ボタンをクリックするか、F5を押してください。その後、接続のプロンプト、IPアドレス、色（0xff0000は赤）がシェルに表示されます。


    .. note::

        コードを実行する前に、Pico 2 Wに ``do_connect.py`` と ``secrets.py`` スクリプトを作成する必要があります。作成方法については :ref:`py_iot_access` を参照してください。

    .. image:: img/2_cheerlight1.png

#. グローバルな@CheerLightsデバイスを制御

   - |link_discord_server| に参加し、CheerLightsボットを使用して色を設定します。 **CheerLights Discordサーバー** のいずれかのチャンネルで ``/cheerlights`` と入力すると、ボットが起動します。

   .. image:: img/05_iot_cheerlights_1.png

   - ボットの指示に従って色を設定します。これにより、CheerLightsデバイスを世界中で制御できます。

   .. image:: img/05_iot_cheerlights_2.png

5. スクリプトが実行された後、WS2812 RGBストリップは色を表示し、時々色が変わります。

6. このスクリプトを起動時に実行したい場合は、 ``main.py`` としてRaspberry Pi Pico 2 Wに保存する必要があります。次の手順に従ってください。

    * スクリプトの実行を停止し、 **ファイル**  -> **名前を付けて保存** をクリックします。

        .. image:: img/2_cheerlight2.png

    * ポップアップウィンドウで **Raspberry Pi Pico** を選択します。

        .. image:: img/2_cheerlight3.png

    * ファイル名を ``main.py`` に設定します。同じファイルがPico 2 Wに既に存在している場合、確認のプロンプトが表示されます。

        .. image:: img/2_cheerlight4.png
    
    * USBケーブルを外し、Li-po充電モジュールを使ってRaspberry Pi Pico 2 Wに電力を供給できます。これを一角に置けば、Picoは自動的に動作します。

**仕組みは？**

このプロジェクトはネットワーク接続を必要とし、 `network` モジュールを使用してネットワークに接続します。
`network` モジュールの使用方法については :ref:`py_iot_access` を参照してください。

.. code-block:: python

    from secrets import *
    from do_connect import *
    do_connect()

from do_connect import * : これは `do_connect()` 関数をインポートし、その中にWi-Fi接続を管理するロジックが含まれています。 `do_connect()` 関数が呼び出されると、 `secrets.py` に指定されたWi-Fiネットワークに接続します。接続に失敗した場合は例外を発生させ、成功すれば次のステップに進みます。

from secrets import * : これは通常、Wi-FiのSSID、パスワード、およびその他の機密情報（APIキーなど）を格納するために使われる独立したファイルであり、機密情報をメインのコードファイルに直接埋め込まないようにします。

WS2812 RGBストリップを設定する方法については、 :ref:`py_neopixel` を参照してください。

.. code-block:: python

    import machine
    from ws2812 import WS2812
    ws = WS2812(machine.Pin(18), 8)

次に、@CheerLightsの色を取得する方法を説明します。Twitterからの色変更を受け取るバックエンドシステムがあり、その変更をJSON形式でURL: http://api.thingspeak.com/channels/1417/field/2/last.json に投稿します。

このURLを直接ブラウザで開くと、次のような内容が表示されます。必要なのは ``field2`` データで、これは16進数の色コード文字列です。

.. code-block:: 

    {"created_at":"2022-08-16T06:12:44Z","entry_id":870488,"field2":"#ff00ff"}

``urequests`` モジュールを使用してこのデータを取得し、 ``json`` モジュールを使用してPythonの辞書に変換します。
以下のコードは最新の@CheerLights色をURLから取得し、WS2812で使用できる色値を返します。

.. code-block:: python

    def get_colour():
        url = "http://api.thingspeak.com/channels/1417/field/2/last.json"
        try:
            r = urequests.get(url)
            if r.status_code > 199 and r.status_code < 300:
                cheerlights = json.loads(r.content.decode('utf-8'))
                print(cheerlights['field2'])
                colour = int('0x'+cheerlights['field2'][1:7])#文字列から整数に変換
                r.close()
                return colour
            else:
                return None
        except Exception as e:
            print(e)
            return None

最後に、5秒ごとにWS2812を動作させるループを作成します。

.. code-block:: python

    while True:
        colour = get_colour()
        if colour is not None:
            ws.write_all(colour)
        time.sleep(5)

