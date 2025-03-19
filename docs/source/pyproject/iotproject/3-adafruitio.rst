.. note:: 

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！仲間たちと一緒にRaspberry Pi、Arduino、ESP32についてさらに深く学びましょう。

    **参加する理由は？**

    - **専門家のサポート**: コミュニティやチームの助けを借りて、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換して、スキルを向上させましょう。
    - **限定プレビュー**: 新製品の発表や先行情報をいち早く手に入れましょう。
    - **特別割引**: 最新製品の特別割引をお楽しみください。
    - **イベント・プレゼント**: プレゼント企画や祝日セールに参加しましょう。

    👉 一緒に探求し、創造を楽しみませんか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _py_iot_adafruitio: 

8.3 @AdafruitIOを使用した温度と湿度のモニタリング
==========================================================

このプロジェクトでは、強力で使いやすいIoTプラットフォームであるAdafruit IOを使用します。MicroPythonを使って、Raspberry Pi Pico WをWi-Fiに接続し、Adafruit IOと統合してリアルタイムの通信と制御機能をデモンストレーションします。

プロジェクトでは、温度と湿度を測定するDHT11センサーを使用し、MQTTプロトコルを使ってデータをAdafruit IOのダッシュボードに送信します。さらに、ダッシュボード上の仮想スイッチの状態により、LEDを遠隔で制御できます。コードは、LEDの状態を同期させるためにAdafruit IOのREST APIも利用しており、ハードウェアとのスムーズな動作を確保しています。

MQTTを使用したリアルタイムのデータ交換と、REST APIを使用した設定の同期により、このプロジェクトはIoTプログラミングの概念を学ぶための優れた導入となります。

1. 回路を組み立てる
+++++++++++++++++++++++++++++++++

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
        - \-

.. image:: img/wiring/8.13_bb.png
   :width: 90%

.. raw:: html

   <br/>

2. Adafruit IOダッシュボードの設定
+++++++++++++++++++++++++++++++++++++++++

#. |link_adafruit_io| にアクセスし、 **無料で始める** をクリックして無料アカウントを作成します。

   .. image:: img/3-1_get_start.png
      :width: 90%

#. サインアップフォームに必要事項を記入してアカウントを作成します。

   .. image:: img/3-2_sign_up.png
      :width: 90%

#. アカウントが作成されたら、Adafruit IOに戻り、 **Dashboards** をクリックし、 **新しいダッシュボード** を選択します。

   .. image:: img/3-3_create_dashboard.png
      :width: 90%

#. **新しいダッシュボード** を作成します。

   .. image:: img/3-4_create_dashboard_2.png
      :width: 75%

#. 新しく作成した **ダッシュボード** に入り、新しいブロックを作成します。

   .. image:: img/3-5_create_block.png
      :width: 90%

   .. image:: img/3-6_create_block_2.png
      :width: 90%

#. **トグルブロック** をダッシュボードに追加します。

   .. image:: img/3-7_toggle_block.png
      :width: 90%

#. このブロックに新しいフィードを作成します。このフィードはLEDを制御するため、名前をLEDに設定します。

   .. image:: img/3-8_connect_feed.png
      :width: 90%

#. **LED** フィードを選択して、次のステップに進みます。

   .. image:: img/3-9_connect_feed_2.png
      :width: 90%

#. ブロックの設定（主にブロックタイトル、オンのテキスト、オフのテキスト）を完了し、右下の **ブロックを作成** ボタンをクリックして終了します。

   .. image:: img/3-10_create_block_2.png
      :width: 90%

#. 追加で2つの **テキストブロック** を作成し、温度と湿度を表示します。これらのブロックには、 **temperature** と **humidity** という名前のフィードを作成します。

   .. image:: img/3-11_text_block.png
      :width: 90%

   .. image:: img/3-12_connect_feed.png
      :width: 90%

#. ブロック作成後、ダッシュボードは以下のようになります：

   .. image:: img/3-13_connect_feed.png
      :width: 90%

#. 必要に応じて **レイアウトの編集** オプションでレイアウトを調整します。

   .. image:: img/3-14_edit_layout.png
      :width: 50%

#. **APIキー** をクリックして、ユーザー名とAPIキーを表示します。これらの認証情報はコードで必要になるため、メモしておいてください。

   .. image:: img/3-15_api_key.png
      :width: 90%

   .. image:: img/3-16_api_key.png
      :width: 90%


3. コードを実行する
+++++++++++++++++++++++++++++++++

#. 次に、USBケーブルを使ってPico 2 Wボードをコンピュータに接続します。

#. ``pico-2w-kit/micropython/iot/8.3_adafruitio`` のパスにある ``8.3_adafruitio.py`` ファイルを開くか、このコードをIDEにコピーして貼り付けます。

   .. note::
      このコードは ``lib/umqtt/simple.mpy`` ファイルに依存しています。スクリプトを実行する前に、このファイルをPicoボードにアップロードしてください。

   .. note::
      コードを実行する前に、Wi-Fiの認証情報とAdafruit IOの設定（ステップ2.13で説明した内容）を更新しておいてください。

   .. code-block:: python
      :emphasize-lines: 10,11,16,17

      import network
      import time
      from umqtt.simple import MQTTClient
      from machine import Pin
      import utime
      import dht
      import urequests
      
      # Wi-Fi設定
      SSID = "your_wifi_ssid"            # ここを変更
      PASSWORD = "your_password"         # ここを変更
      
      # Adafruit IO設定
      AIO_SERVER = "io.adafruit.com"
      AIO_PORT = 1883
      AIO_USER = "your_name_adafruitIO"  # ここを変更
      AIO_KEY = "aio_xxxxxxxxx"          # ここを変更
      AIO_FEED_HUM = "humidity"
      AIO_FEED_TEMP = "temperature"
      AIO_FEED_LED = "led"
      
      # DHT11およびLED設定
      sensor = dht.DHT11(Pin(15))
      led = Pin("LED", Pin.OUT)
      
      # 定期的なタスクのためのタイムスタンプ
      last_update = time.ticks_ms()
      
      # Wi-Fiに接続
      def connect_wifi():
         wlan = network.WLAN(network.STA_IF)
         wlan.active(True)
         wlan.connect(SSID, PASSWORD)
         while not wlan.isconnected():
            print("Connecting to WiFi...")
            time.sleep(1)
         print("WiFi Connected:", wlan.ifconfig())
      
      # 受信したMQTTメッセージの処理
      def message_callback(topic, msg):
         global led
         message = msg.decode()
         print("Received message on topic {}: {}".format(topic, message))
         if message.lower() == "on":
            led.value(1)  # LEDをオン
         elif message.lower() == "off":
            led.value(0)  # LEDをオフ
      
      # Adafruit IOに接続
      def connect_adafruit():
         client = MQTTClient("pico", AIO_SERVER, AIO_PORT, AIO_USER, AIO_KEY)
         client.set_callback(message_callback)
         client.connect()
         print("Connected to Adafruit IO")
         return client
      
      # フィードから最後の値を取得
      def get_feed_value(feed_name):
         url = f"https://io.adafruit.com/api/v2/{AIO_USER}/feeds/{feed_name}/data/last"
         headers = {"X-AIO-Key": AIO_KEY}
         try:
            response = urequests.get(url, headers=headers)
            if response.status_code == 200:
                  data = response.json()
                  print(f"Feed {feed_name} last value: {data['value']}")
                  return data["value"]
            else:
                  print(f"Failed to get feed value: {response.status_code}")
                  return None
         except Exception as e:
            print("Error fetching feed value:", e)
            return None
      
      # メインプログラム
      def main():
         global last_update
      
         connect_wifi()
         client = connect_adafruit()
      
         # LEDフィードを購読
         led_topic = f"{AIO_USER}/feeds/{AIO_FEED_LED}"
         client.subscribe(led_topic)
         print(f"Subscribed to {led_topic}")
      
         # 初期LED状態の同期
         led_state = get_feed_value(AIO_FEED_LED)
         if led_state:
            if led_state.lower() == "on":
                  led.value(1)
            elif led_state.lower() == "off":
                  led.value(0)
      
         while True:
            # 新しいMQTTメッセージをチェック
            client.check_msg()
      
            # 10秒ごとにDHT11データを更新
            if time.ticks_diff(time.ticks_ms(), last_update) > 10000:
                  try:
                     sensor.measure()
                     temperature = str(sensor.temperature)  # 温度
                     humidity = str(sensor.humidity)        # 湿度
      
                     print("Temperature: {}C   Humidity: {}%".format(temperature, humidity))
      
                     # データをAdafruit IOに公開
                     client.publish(f"{AIO_USER}/feeds/{AIO_FEED_TEMP}", temperature)
                     client.publish(f"{AIO_USER}/feeds/{AIO_FEED_HUM}", humidity)
      
                     last_update = time.ticks_ms()  # タイムスタンプの更新
                  except Exception as e:
                     print("Error:", e)
      
      try:
         main()
      except Exception as e:
         print("Error:", e)

#. コードが正常にPicoに保存され、実行されると、シリアルモニタに次のメッセージが表示され、Adafruit IOとの通信が確認されます。
   
   .. image:: img/3-17_micropython.png
      :width: 90%

#. Adafruit IOに戻ります。ダッシュボードで温度と湿度の読み取り値を表示するか、LEDトグルスイッチを使用して回路に接続された外部LEDのオン/オフ状態を制御できます。

   .. image:: img/3-18_adafruitio.png
      :width: 90%