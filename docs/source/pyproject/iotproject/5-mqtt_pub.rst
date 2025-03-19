.. note:: 

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！仲間たちと一緒にRaspberry Pi、Arduino、ESP32についてさらに深く学びましょう。

    **参加する理由は？**

    - **専門家のサポート**: コミュニティやチームの助けを借りて、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換して、スキルを向上させましょう。
    - **限定プレビュー**: 新製品の発表や先行情報をいち早く手に入れましょう。
    - **特別割引**: 最新製品の特別割引をお楽しみください。
    - **イベント・プレゼント**: プレゼント企画や祝日セールに参加しましょう。

    👉 一緒に探求し、創造を楽しみませんか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _py_iot_mqtt_publish:

8.5 @MQTTを使ったクラウド呼び出しシステム
============================================

Message Queuing Telemetry Transport (MQTT)はシンプルなメッセージングプロトコルであり、モノのインターネット（IoT）において最も一般的なメッセージングプロトコルでもあります。

MQTTプロトコルは、IoTデバイスがデータを転送する方法を定義しています。
これらはイベント駆動型で、Pub/Subモデルを使用して相互接続されています。
送信者（Publisher）と受信者（Subscriber）は、トピックを通じて通信します。
デバイスが特定のトピックでメッセージを公開し、そのトピックを購読しているすべてのデバイスがそのメッセージを受け取ります。

このセクションでは、Pico 2 W、HiveMQ（無料の公開MQTTブローカーサービス）、および4つのボタンを使用してサービスベルシステムを作成します。
4つのボタンはレストラン内の4つのテーブルを意味しており、顧客がボタンを押すと、HiveMQでどのテーブルのゲストがサービスを必要としているかを確認できます。

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
        - :ref:`cpn_resistor`
        - 4(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_button`
        - 4
        - |link_button_buy|
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

.. image:: img/wiring/5.mqtt_pub.png
    :width: 800

**3. HiveMQにアクセスする**

HiveMQは、IoTデバイスへの迅速で効率的、かつ信頼性の高いデータ転送を可能にするMQTTブローカーおよびクライアントベースのメッセージングプラットフォームです。

1. |link_hivemq| をブラウザで開きます。

2. クライアントがデフォルトの公開プロキシに接続します。

   .. image:: img/mqtt-1.png

3. **Add New Topic Subscription** をクリックします。

   .. image:: img/mqtt-2.png

4. 購読したいトピックを入力し、 **Subscribe** をクリックします。ここで設定するトピックは、他のユーザーからのメッセージを避けるため、個別に設定し、大文字小文字の違いに注意してください。

   .. image:: img/mqtt-3.png

**4. MQTTモジュールをインストールする**

プロジェクトを開始する前に、Pico 2 WにMQTTモジュールをインストールする必要があります。

1. 以前に記述した ``do_connect()`` をShellで実行してネットワークに接続します。

    .. note::
        * 以下のコマンドをShellに入力し、 ``Enter`` を押して実行します。
        * ``do_connect.py`` および ``secrets.py`` スクリプトがPico 2 Wにない場合は、 :ref:`py_iot_access` を参照して作成してください。

    .. code-block:: python

        from do_connect import *
        do_connect()

2. ネットワーク接続が成功したら、Shellで ``mip`` モジュールをインポートし、 ``mip`` を使用して ``umqtt.simple`` モジュールをインストールします。これはMicroPython用の簡略化されたMQTTクライアントです。

    .. code-block:: python

        import mip
        mip.install('umqtt.simple')

3. インストールが完了したら、 ``umqtt`` モジュールはPico 2 Wの ``/micropython/libs/`` パスにインストールされます。

    .. image:: img/5_calling_system1.png

**5. スクリプトを実行する**

#. ``pico-2w-kit-main/micropython/iot`` のパスにある ``8.5_mqtt_publish.py`` ファイルを開きます。

#. **現在のスクリプトを実行** ボタンをクリックするか、F5を押して実行します。

    .. image:: img/5_calling_system2.png

#. 再度 |link_hivemq| に戻り、ブレッドボードのボタンの1つを押すと、HiveMQのメッセージプロンプトに表示されるのが確認できます。

    .. image:: img/mqtt-4.png

#. このスクリプトを起動時に実行したい場合は、Raspberry Pi Pico 2 Wに ``main.py`` として保存できます。


**仕組みは？**

このプロジェクトはネットワーク接続を必要とし、 :ref:`py_iot_access` メソッドを使用してネットワークに接続します。

.. code-block:: python

    from secrets import *
    from do_connect import *
    do_connect()
    
from do_connect import * : これは `do_connect()` 関数をインポートし、この関数にはWi-Fi接続のロジックが含まれています。 `do_connect()` 関数が呼び出されると、 `secrets.py` で指定されたWi-Fiネットワークに接続します。接続に失敗した場合は例外が発生し、成功すれば次のステップに進みます。

from secrets import * : `secrets.py` ファイルは通常、Wi-FiのSSID、パスワード、その他の機密情報（APIキーなど）を格納するために使われます。これにより、機密情報をメインコードファイルに直接埋め込まないようにします。

4つのボタンピンを初期化します。

.. code-block:: python

    sensor1 = Pin(16, Pin.IN)
    sensor2 = Pin(17, Pin.IN)
    sensor3 = Pin(18, Pin.IN)
    sensor4 = Pin(19, Pin.IN)

MQTTブローカーへの接続に使用する ``URL`` と ``client ID`` を保存する変数を作成します。
公開ブローカーを使用するため、 ``client ID`` は要求されても使用されません。

.. code-block:: python

    mqtt_server = 'broker.hivemq.com'
    client_id = 'Jimmy'

MQTTエージェントに接続し、1時間保持します。接続に失敗した場合、Pico 2 Wをリセットします。

.. code-block:: python

    try:
        client = MQTTClient(client_id, mqtt_server, keepalive=3600)
        client.connect()
        print('Connected to %s MQTT Broker'%(mqtt_server))
    except OSError as e:
        print('Failed to connect to the MQTT Broker. Reconnecting...')
        time.sleep(5)
        machine.reset()

``topic`` という変数を作成します。これは購読者が追跡する必要があるトピックで、上記の **ステップ4** の **2. HiveMQを訪れる** で入力したトピックと同じにする必要があります。
ちなみに、ここでの ``b`` は文字列をバイトに変換します。MQTTはバイナリベースのプロトコルであり、制御要素はバイナリバイトであって、テキスト文字列ではありません。

.. code-block:: python

    topic = b'SunFounder MQTT Test'

各ボタンに対して割り込みを設定します。ボタンが押されると、 ``topic`` にメッセージが投稿されます。

.. code-block:: python

    def press1(pin):
        message = b'button 1 is pressed'
        client.publish(topic, message)
        print(message)

    sensor1.irq(trigger=machine.Pin.IRQ_RISING, handler=press1)


* `UMQTT Client API  <https://pypi.org/project/micropython-umqtt.simple/>`_



.. https://www.tomshardware.com/how-to/send-and-receive-data-raspberry-pi-pico-w-mqtt