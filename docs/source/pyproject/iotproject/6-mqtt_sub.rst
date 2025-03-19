.. note:: 

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！仲間たちと一緒にRaspberry Pi、Arduino、ESP32についてさらに深く学びましょう。

    **参加する理由は？**

    - **専門家のサポート**: コミュニティやチームの助けを借りて、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換して、スキルを向上させましょう。
    - **限定プレビュー**: 新製品の発表や先行情報をいち早く手に入れましょう。
    - **特別割引**: 最新製品の特別割引をお楽しみください。
    - **イベント・プレゼント**: プレゼント企画や祝日セールに参加しましょう。

    👉 一緒に探求し、創造を楽しみませんか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _py_iot_mqtt_subscribe:

8.6 @MQTTを使ったクラウドプレイヤー
=========================================

まず、 :ref:`py_iot_mqtt_publish` プロジェクトを先に実施して、いくつかのモジュールをインストールし、HiveMQプラットフォームの設定を完了することをお勧めします。

このプロジェクトでは、Pico 2 Wはサブスクライバーとして機能し、トピックの下で曲名を受信します。
もし曲名がすでにコード内に含まれていれば、Pico 2 Wはブザーでその曲を再生します。

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
        - :ref:`cpn_transistor`
        - 1(S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_resistor`
        - 1(1KΩ)
        - |link_resistor_buy|
    *   - 7
        - パッシブ :ref:`cpn_buzzer`
        - 1
        - |link_passive_buzzer_buy|
    *   - 8
        - :ref:`cpn_lipo_charger`
        - 1
        -  
    *   - 9
        - 18650バッテリー
        - 1
        -  

**2. 回路を組み立てる**

キットには2つのブザーが含まれていますが、ここではパッシブブザー（背面にPCBが露出しているタイプ）を使用します。ブザーは動作させるためにトランジスタが必要で、ここではS8050を使用します。

    .. warning:: 
        
        Li-po充電モジュールが図のように接続されていることを確認してください。そうしないと、短絡が原因でバッテリーや回路が損傷する可能性があります。

.. image:: img/wiring/6.mqtt_sub_bb.png



**3. コードを実行する**

#. ``pico-2w-kit-main/micropython/iot`` のパスにある ``play_music.py`` ファイルをRaspberry Pi Pico 2 Wにアップロードします。

    .. image:: img/mqtt-A-1.png

#. ``pico-2w-kit-main/micropython/iot`` のパスにある ``8.6_mqtt_subscribe_music.py`` ファイルを開き、 **現在のスクリプトを実行** ボタンをクリックするか、F5を押して実行します。

    .. image:: img/6_cloud_player.png

    .. note::

        コードを実行する前に、Pico 2 Wに ``do_connect.py`` および ``secrets.py`` スクリプトを作成する必要があります。作成方法については :ref:`py_iot_access` を参照してください。

#. ブラウザで|link_hivemq|を開き、トピックを ``SunFounder MQTT Music`` として、曲名を **Message** として入力します。 **Publish** ボタンをクリックすると、Pico 2 Wに接続されたブザーが対応する曲を再生します。

    .. note::
        ``play_music.py`` には、 ``nokia`` 、 ``starwars`` 、 ``nevergonnagiveyouup`` 、 ``gameofthrone`` 、 ``songofstorms`` 、 ``zeldatheme`` 、 ``harrypotter`` が含まれています。

    .. image:: img/mqtt-5.png
        :width: 500

#. このスクリプトを起動時に実行できるようにしたい場合は、Raspberry Pi Pico 2 Wに ``main.py`` として保存できます。

**仕組みは？**

理解を容易にするため、MQTTのコードを他の部分から分けました。
その結果、以下のコードが得られ、MQTTサブスクリプションの最も基本的な機能が3つの場所で実装されています。

.. code-block:: python
    :emphasize-lines: 13,14,15,16,20,28,29,30

    import time
    from umqtt.simple import MQTTClient

    # `do_connect()`関数をインポートします。この関数には、`network`モジュールを使ってWi-Fiに接続するロジックが含まれています。`do_connect()`関数が呼び出されると、`secrets.py`で指定されたWi-Fiネットワークに接続します。接続に失敗した場合は例外が発生し、成功すれば次のステップに進みます。
    from do_connect import * 
    do_connect()

    mqtt_server = 'broker.hivemq.com'
    client_id = 'Jimmy'

    # メッセージをサブスクライブする
    topic = b'SunFounder MQTT Music'

    def callback(topic, message):
        print("New message on topic {}".format(topic.decode('utf-8')))
        message = message.decode('utf-8')
        print(message)

    try:
        client = MQTTClient(client_id, mqtt_server, keepalive=60)
        client.set_callback(callback)
        client.connect()
        print('Connected to %s MQTT Broker'%(mqtt_server))
    except OSError as e:
        print('Failed to connect to MQTT Broker. Reconnecting...')
        time.sleep(5)
        machine.reset()
        
    while True:
        client.subscribe(topic)
        time.sleep(1)


MQTTブローカーに接続する際、 ``client.set_callback(callback)`` 関数を呼び出し、これが受信したサブスクリプションメッセージのコールバックとして機能します。

.. code-block:: python
    :emphasize-lines: 3

    try:
        client = MQTTClient(client_id, mqtt_server, keepalive=60)
        client.set_callback(callback)
        client.connect()
        print('Connected to %s MQTT Broker'%(mqtt_server))
    except OSError as e:
        print('Failed to connect to MQTT Broker. Reconnecting...')
        time.sleep(5)
        machine.reset()

次に、コールバック関数では、取得したトピックからメッセージを出力します。
MQTTはバイナリベースのプロトコルであり、制御要素はバイナリバイトであって、テキスト文字列ではないため、これらのメッセージは ``message.decode('utf-8')`` を使ってデコードする必要があります。

.. code-block:: python

    def callback(topic, message):
        print("New message on topic {}".format(topic.decode('utf-8')))
        message = message.decode('utf-8')
        print(message)

``While True`` ループを使用して、このトピックのメッセージを定期的に取得します。

.. code-block:: python

    while True:
        client.subscribe(topic)
        time.sleep(1)


次に、音楽が再生されます。この関数は ``play_music.py`` スクリプトに配置されており、3つの主要な部分から構成されています。

   * ``Tone``: 基本的な |link_piano_frequency| を基にした特定の音色をシミュレートし、それを再生します。

        .. code-block:: python

            NOTE_B0 =  31
            NOTE_C1 =  33
            ...
            NOTE_DS8 = 4978
            REST =      0

   * ``Score`` : 音楽をプログラムが使用できる形式に編集します。これらのスコアは `Robson Coutoの無料共有 <https://github.com/robsoncouto/arduino-songs>`_ から取得したもので、以下の形式でお気に入りの曲を追加することもできます。

    .. code-block:: python

        # メロディのノートとその長さ
        # 4は4分音符、8は8分音符、16は16分音符などを意味します
        # !!負の数は付点音符を表すため、-4は付点4分音符、すなわち4分音符＋8分音符！！

        song = {
            "nokia":[NOTE_E5, 8, NOTE_D5, 8, NOTE_FS4, 4, NOTE_GS4, 4, NOTE_CS5, 8, NOTE_B4, 8, NOTE_D4, 4, 
                        NOTE_E4, 4,NOTE_B4, 8, NOTE_A4, 8, NOTE_CS4, 4, NOTE_E4, 4, NOTE_A4, 2],
            "starwars":[,,,],
            "nevergonnagiveyouup":[,,,],
            "gameofthrone":[,,,],
            "songofstorms":[,,,],
            "zeldatheme":[,,,],
            "harrypotter":[,,,],
        }

   * ``Play``: この部分は基本的に :ref:`py_pa_buz` と同じですが、上記のスコアに合わせて少し最適化されています。

   .. code-block:: python

       import time
       import machine

       # 曲を遅くまたは速くするために調整
       tempo = 220

       # 4分音符の長さをミリ秒単位で計算
       wholenote = (60000 * 4) / tempo

       def tone(pin,frequency,duration):
           if frequency is 0:
               pass
           else:
               pin.freq(frequency)
               pin.duty_u16(30000)
           time.sleep_ms(duration)
           pin.duty_u16(0)

       def noTone(pin):
           tone(pin,0,100)

       def play(pin,melody):

           # メロディのノートを反復
           # 配列はノートとその長さで2倍の数になります
           for thisNote in range(0,len(melody),2):
               # 各ノートの長さを計算
               divider = melody[thisNote+1]
               if divider > 0:
                   noteDuration = wholenote/divider
               elif divider < 0:
                   noteDuration = wholenote/-(divider)
                   noteDuration *= 1.5

               # ノートの90％の時間だけ再生し、残りの10％はポーズ
               tone(pin,melody[thisNote],int(noteDuration*0.9))

               # 次のノートの前に指定された時間だけ待機
               time.sleep_ms(int(noteDuration))

               # 次のノートの前に波形生成を停止
               noTone(pin)


メイン関数に戻り、MQTTで音楽の再生をトリガーします。
コールバック関数内で、送信されたメッセージがすでに含まれている曲名であるかを確認します。
そうであれば、曲名を ``melody`` 変数に割り当て、 ``play_flag`` を ``True`` に設定します。

.. code-block:: python
    :emphasize-lines: 5,6,7,8

    def callback(topic, message):
        print("New message on topic {}".format(topic.decode('utf-8')))
        message = message.decode('utf-8')
        print(message)
        if message in song.keys():
            global melody,play_flag
            melody = song[message]
            play_flag = True

メインループ内で、 ``play_flag`` が ``True`` の場合、 ``melody`` を再生します。

.. code-block:: python
    :emphasize-lines: 4,5,6

    while True:
        client.subscribe(topic)
        time.sleep(1)
        if play_flag is True:
            play(buzzer,melody)
            play_flag = False