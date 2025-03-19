.. note:: 

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！仲間たちと一緒にRaspberry Pi、Arduino、ESP32についてさらに深く学びましょう。

    **参加する理由は？**

    - **専門家のサポート**: コミュニティやチームの助けを借りて、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換し、スキルを向上させましょう。
    - **限定プレビュー**: 新製品の発表や先行情報をいち早く手に入れましょう。
    - **特別割引**: 最新製品の特別割引をお楽しみください。
    - **イベント・プレゼント**: プレゼント企画や祝日セールに参加しましょう。

    👉 一緒に探求し、創造を楽しみませんか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _py_iot_ble_relay:

8.15 Bluetooth音声制御リレー
==========================================

このプロジェクトでは、Raspberry Pi Pico 2 Wを使ってリレーを制御する方法を示します。Pico WはBluetooth Low Energy (BLE)を介してスマートフォンなどのBLE対応デバイスからコマンドを受信し、「1」信号を受け取るとリレーをオンに、「0」信号を受け取るとリレーをオフに切り替えます。

Raspberry Pi Pico 2 WでのBLE通信やIoTアプリケーションを探求したい方に最適なプロジェクトです。

1. 回路を作成する
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
        - :ref:`cpn_diode`
        - 1
        - 
    *   - 7
        - :ref:`cpn_resistor`
        - 1(1KΩ) 1(220Ω)
        - |link_resistor_buy|
    *   - 8
        - :ref:`cpn_relay`
        - 1
        - |link_relay_buy|
    *   - 9
        - :ref:`cpn_lipo_charger`
        - 1
        -  
    *   - 10
        - 18650バッテリー
        - 1
        - 

.. warning ::

   ここではリレーを使ってLEDを制御する例を紹介していますが、実際のアプリケーションでリレーを高電圧のAC電源に接続する場合は十分注意してください。誤った使用は重大な怪我や死亡事故につながる可能性があります。安全を最優先してください。
   
.. image:: img/wiring/8.15_bb.png
   :width: 90%

.. raw:: html

   <br/>

1. Androidアプリを作成する
+++++++++++++++++++++++++++++++++

|link_appinventor| という無料のウェブアプリケーションを使ってAndroidアプリを開発します。ドラッグアンドドロップ操作で簡単に機能的なアプリを作成でき、Android開発初心者に適しています。

次の手順に従ってください：

#. |link_appinventor_login| へアクセスし、"online tool"をクリックしてログインします。Googleアカウントを使ってMIT App Inventorに登録する必要があります。

   .. image:: img/13-ai-signup.png
       :width: 90%
       :align: center

#. ログイン後、 **Projects** -> **Import project (.aia) from my computer** を選択し、 ``pico-2w-kit/micropython/iot/8.15-ble_relay`` にある ``ble_relay_picow.aia`` ファイルをアップロードします。

   または、こちらから直接ファイルをダウンロードできます：:download:`ble_relay_picow.aia</_static/other/ble_relay_picow.aia>`

   .. image:: img/13-ai-import.png
        :align: center

#. アップロードが完了すると、MIT App Inventorのインターフェイスにプリセットされたアプリのテンプレートが表示されます。プラットフォームに慣れてから、自由にカスタマイズ可能です。

#. MIT App Inventorには、 **Designer** と **Blocks** という2つの主要セクションがあります。ページ右上のタブから切り替えることができます。

   .. image:: img/13-ai-intro-1.png

#. **Designer** では、ボタンやテキスト、画面、デザインなどを追加・調整し、アプリの外観を整えることができます。

   .. image:: img/15-ai-intro-2.png
      :width: 100%
   
#. **Blocks** セクションでは、アプリの各コンポーネントに対して動作を指定するブロックを組み合わせて、機能を実装します。

   .. image:: img/15-ai-intro-3.png
      :width: 100%

#. スマートフォンにアプリをインストールする場合、 **Build** タブに移動してください。

   .. image:: img/13-ai-intro-4.png
      :width: 60%
      :align: center

   * ``.apk`` ファイルを生成します。選択後、 ``.apk`` ファイルのダウンロードまたはQRコードスキャンのいずれかを選べます。ガイドに従ってアプリをインストールしてください。

     または、事前コンパイル済みのAPKファイルを以下からダウンロードできます： :download:`ble_relay_picow.apk</_static/other/ble_relay_picow.apk>`

   * Google Playなどへの公開を希望する場合は ``.aab`` ファイルを生成できます。


3. コードを実行する
+++++++++++++++++++++++++++++++++

``pico-2w-kit/micropython/iot/8.15-ble_relay`` のパスにある ``8.15-ble_relay.py`` ファイルを開くか、以下のコードをIDEにコピーしてください。
   
.. note:: 
   このコードは ``ble_advertising.py`` ファイルに依存しています。実行前にPicoボードにアップロードしておいてください。

.. code-block:: python

   import bluetooth
   import random
   import struct
   import time
   from ble_example.ble_advertising import advertising_payload
   from machine import Pin
   import time
   
   from micropython import const
   
   relay = machine.Pin(15, machine.Pin.OUT)
   
   _IRQ_CENTRAL_CONNECT = const(1)
   _IRQ_CENTRAL_DISCONNECT = const(2)
   _IRQ_GATTS_WRITE = const(3)
   
   _FLAG_READ = const(0x0002)
   _FLAG_WRITE_NO_RESPONSE = const(0x0004)
   _FLAG_WRITE = const(0x0008)
   _FLAG_NOTIFY = const(0x0010)
   
   _RELAY_UUID = bluetooth.UUID("46719f98-3141-4bbb-aede-47a7630d024b")
   _SWITCH_CHAR = (
       bluetooth.UUID("08b82cd0-6877-4308-b08d-a32520c327a2"),
       _FLAG_READ | _FLAG_WRITE | _FLAG_WRITE_NO_RESPONSE,
   )
   _RELAY_SERVICE = (
       _RELAY_UUID,
       (_SWITCH_CHAR,),
   )
   
   
   class BLERelay:
       def __init__(self, ble, name="ble-relay"):
   
           self._ble = ble
           self._ble.active(True)
           self._ble.irq(self._irq)
   
           handles = self._ble.gatts_register_services((_RELAY_SERVICE,))
           # print("Registered handles:", handles)
   
           ((self._handle_note,),) = handles
           self._connections = set()
   
           self._write_callback = None
   
           self._payload = advertising_payload(name=name, services=[_RELAY_UUID])
           self._advertise()
   
       def _irq(self, event, data):
           # Track connections so we can send notifications.
           if event == _IRQ_CENTRAL_CONNECT:
               conn_handle, _, _ = data
               print("New connection", conn_handle)
               self._connections.add(conn_handle)
           elif event == _IRQ_CENTRAL_DISCONNECT:
               conn_handle, _, _ = data
               print("Disconnected", conn_handle)
               self._connections.remove(conn_handle)
               # Start advertising again to allow a new connection.
               self._advertise()
           elif event == _IRQ_GATTS_WRITE:
               conn_handle, value_handle = data
               value = self._ble.gatts_read(value_handle)
               # print("Write event: conn_handle={}, value_handle={}, value={}".format(conn_handle, value_handle, value))
               if value_handle == self._handle_note and self._write_callback:
                   self._write_callback(value)
                   
   
       def is_connected(self):
           return len(self._connections) > 0
   
       def _advertise(self, interval_us=500000):
           print("Starting advertising")
           self._ble.gap_advertise(interval_us, adv_data=self._payload)
   
       def on_write(self, callback):
           self._write_callback = callback
   
   def relay_update(data):
       print("Receive:", data)
   
       decoded_data = int(data.decode('utf-8').rstrip('\x00'))
   
       # print(decoded_data)
   
       relay.value(decoded_data)
   
   
   def demo():
       ble = bluetooth.BLE()
       relay = BLERelay(ble,"pico2w")
   
       while True:
           if relay.is_connected():
               relay.on_write(relay_update)
           # time.sleep_ms(100)
   
   if __name__ == "__main__":
       demo()


4. アプリとBluetoothの接続
++++++++++++++++++++++++++++++++++++++++++

先ほど作成した「Voice-Controlled Relay BLE」アプリをスマートフォンにインストールしておきましょう。

#. スマートフォンのBluetoothを有効にします。

#. **Voice-Controlled Relay BLE** アプリを開きます。

   .. image:: img/15_app_2.png
      :width: 25%
      :align: center

#. 初回起動時には2つの連続するダイアログが表示され、権限を求められます。これらの権限はBluetooth機能を使用するために必要です。

   .. image:: img/15_app_3.png
      :width: 100%
      :align: center

#. アプリ内で **Connect** をタップし、Pico 2 WとBluetoothで接続します。

   .. image:: img/15_app_4.png
      :width: 55%
      :align: center

#. この画面には、すべてのBluetoothデバイスが一覧表示されます。 ``xx.xx.xx.xx.xx.xx pico2w`` といった名前のデバイスを選択します。各デバイス名にはMACアドレスが付属しています。

   .. image:: img/13_app_5.png
      :width: 60%
      :align: center

#. デバイスが表示されない場合は、スマートフォンの位置情報を有効にしてみてください。（一部のAndroidバージョンでは、位置情報設定とBluetooth機能が連動しています。）

#. 接続が完了するとメイン画面に戻ります。マイクアイコンをタップすると音声コマンドでリレーを操作できます。音声コマンド内に「on」が含まれているとリレーはオン、「off」が含まれているとリレーはオフになります。

   .. image:: img/15_app_7.png
      :width: 80%
      :align: center