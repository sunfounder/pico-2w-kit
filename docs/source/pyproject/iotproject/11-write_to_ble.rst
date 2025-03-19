.. note:: 

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！仲間たちと一緒にRaspberry Pi、Arduino、ESP32についてさらに深く学びましょう。

    **参加する理由は？**

    - **専門家のサポート**: コミュニティやチームの助けを借りて、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換し、スキルを向上させましょう。
    - **限定プレビュー**: 新製品の発表や先行情報をいち早く手に入れましょう。
    - **特別割引**: 最新製品の特別割引をお楽しみください。
    - **イベント・プレゼント**: プレゼント企画や祝日セールに参加しましょう。

    👉 一緒に探求し、創造を楽しみませんか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

8.11 Bluetoothへのデータ書き込み
=================================

このプロジェクトでは、Raspberry Pi Pico 2 WがBluetooth Low Energy（BLE）ネットワークの周辺機器として機能します。カスタムBLEサービスを提供し、読み取りおよび通知の両方をサポートする特徴を持っています。スマートフォンなどの中央機器がPico Wに接続し、BLE経由で送信されたテキストメッセージを受信できます。

オンボードLEDは接続状況を示します：中央機器が接続すると点灯し、デバイスが切断されると消灯します。デバイス名はカスタマイズ可能で、MACアドレスに基づいてシステムが自動的に生成することもできます。このスクリプトはBLEサービスを継続的に広告し、ターミナルからテキストを入力することで、接続されているすべての中央機器に送信します。

1. 回路を作成する
+++++++++++++++++++++++++++++++++

**必要なコンポーネント**

このプロジェクトでは、以下のコンポーネントが必要です。

一式を購入するのが便利です。こちらのリンクを参照してください：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名称  
        - このキットに含まれているアイテム  
        - リンク  
    *   - Pico 2 W スターターキット  
        - 450+  
        - |link_pico2w_kit|

以下のリンクから個別に購入することもできます。


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
        - マイクロUSBケーブル  
        - 1  
        -  

このプロジェクトでは、追加の回路を構築する必要はありません。USBデータケーブルを使用してRaspberry Pi Pico 2 Wをコンピュータに接続するだけです。

2. コードを実行する
+++++++++++++++++++++++++++++++++

以下のコードをIDEにコピーしてください。別途、リポジトリのパス「 ``pico-2w-kit/micropython/iot/8.11-write_to_ble/8.11-write_to_ble.py`` 」にもあります。

注：このコードは、 ``ble_advertising.py`` ファイルに依存しています。実行前にPicoボードにアップロードしてください。

.. code-block:: python

   import bluetooth
   import struct
   import time
   import machine
   import ubinascii
   from ble_advertising import advertising_payload
   from micropython import const
   from machine import Pin 
   
   _IRQ_CENTRAL_CONNECT = const(1)
   _IRQ_CENTRAL_DISCONNECT = const(2)
   _IRQ_GATTS_INDICATE_DONE = const(20)
   
   _FLAG_READ = const(0x0002)
   _FLAG_NOTIFY = const(0x0010)
   
   # カスタムサービスおよび特徴のUUID
   # 必要に応じてこれらを変更してください。
   _SERVICE_UUID = bluetooth.UUID("3ec837af-b0c6-4e7e-a8c5-4b31311d98cf")
   _CHAR_UUID = (
       bluetooth.UUID("945c4d90-825d-452f-820a-0d8b0cc74a12"),
       _FLAG_READ | _FLAG_NOTIFY,
   )
   
   _SERVICE = (
       _SERVICE_UUID,
       (_CHAR_UUID,),
   )
   
   led = Pin("LED", Pin.OUT)
   
   class BLEText:
       def __init__(self, ble, name=""):
           # BLEインターフェースを初期化し、カスタムサービスを登録
           self._ble = ble
           self._ble.active(True)
           self._ble.irq(self._irq)
           ((self._handle,),) = self._ble.gatts_register_services((_SERVICE,))
           self._connections = set()
   
           # 名前が提供されていない場合、MACアドレスに基づいて名前を生成
           if len(name) == 0:
               name = 'Pico %s' % ubinascii.hexlify(self._ble.config('mac')[1], ':').decode().upper()
           print('Device name: %s' % name)
   
           # 広告ペイロードを作成
           self._payload = advertising_payload(
               name=name, services=[_SERVICE_UUID]
           )
           self._advertise()
   
       def _irq(self, event, data):
           # BLEイベントを処理
           if event == _IRQ_CENTRAL_CONNECT:
               # セントラルが接続
               conn_handle, _, _ = data
               self._connections.add(conn_handle)
               print("New connection", conn_handle)
               led.value(1)
           elif event == _IRQ_CENTRAL_DISCONNECT:
               # セントラルが切断
               conn_handle, _, _ = data
               self._connections.remove(conn_handle)
               print("Disconnected", conn_handle)
               led.value(0)
               # 再度広告を開始して新しい接続を許可
               self._advertise()
           elif event == _IRQ_GATTS_INDICATE_DONE:
               # インディケーション確認を受け取った（ここでは使用しません）
               conn_handle, value_handle, status = data
   
       def send_text(self, text):
           # 特徴値にテキストを設定
           self._ble.gatts_write(self._handle, text.encode('utf-8'))
           # すべての接続されているセントラルに通知
           for conn_handle in self._connections:
               self._ble.gatts_notify(conn_handle, self._handle)
   
       def _advertise(self, interval_us=500000):
           print("Starting advertising")
           # BLE広告を開始
           self._ble.gap_advertise(interval_us, adv_data=self._payload)
       
       def is_connected(self):
           return len(self._connections) > 0
   
   def demo():
       # BLEインスタンスとBLEText周辺機器を作成
       ble = bluetooth.BLE()
       ble_text = BLEText(ble,"pico2w")
   
       # ターミナルからの入力を読み取り、BLE経由で送信
       while True:
           if ble_text.is_connected():
               line = input("Enter text to send via BLE (Ctrl+C to exit): ")
               ble_text.send_text(line)
   
   
   if __name__ == "__main__":
       demo()

3. Bluetoothからデータを読み取る
+++++++++++++++++++++++++++++++++

このコードで定義されたサービスと特徴を操作するには、LightBlueなどの一般的なBluetooth® Low Energyセントラルアプリを使用します（iOSおよびAndroidで利用可能）。

このセクションでは、LightBlueを使って、Bluetooth経由でPico 2 Wの機能を制御する方法を示します。

a. LightBlueのインストール

   LightBlueアプリを |link_lightblue_apple| （iOS）または |link_lightblue_google| （Android）からダウンロードします。

   .. image:: img/lightblue.png
      :width: 90%

b. Pico 2 Wに接続

   LightBlueを起動し、位置情報とBluetoothの権限を有効にします。 **Peripherals** ページで検索バーに「pico」と入力し、Pico 2 Wデバイスに接続します。

   .. image:: img/11-1-connect-pico.png
      :width: 60%
      :align: center

c. BLEからデータを読み取る

   接続後、LightBlueはPico 2 WのBluetoothデバイスに関する詳細情報を表示します。スクロールして **サービス（3ec837af-b0c6-4e7e-a8c5-4b31311d98cf）** と **特徴（945c4d90-825d-452f-820a-0d8b0cc74a12）** を見つけます。

   特徴945c4d90-825d-452f-820a-0d8b0cc74a12をタップします。この特徴のプロパティが表示され、読み取りと通知をサポートしていることが確認できます。

   .. image:: img/11-2-new.png
      :width: 100%

   右上隅で **"UTF-8 String"** を選択します。

   .. image:: img/11-4-new.png
      :width: 100%
    
   「読み取り」をタップして現在の値を取得します。まだデータが定義されていないため、「No Value」と表示されます。次に、コンピュータに戻り、ターミナルに「hello」と入力します。再度LightBlueに戻り、 **"読み取り"** をタップします。今度は「hello」と表示され、Pico 2 Wからスマートフォンに送信されたメッセージが表示されます。

   .. image:: img/11-6-new.png
      :width: 100%

   .. image:: img/11-6-micropython.png
      :align: center
      :width: 80%

   更新を継続的に監視するには、 **"購読"** をタップして、この特徴を購読することもできます。ターミナルから新しい文字を送信すると、それが自動的に更新され、スマートフォンに表示されます。

   .. image:: img/11-8-new.png
      :width: 100%

