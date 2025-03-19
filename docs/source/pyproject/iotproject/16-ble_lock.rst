.. note:: 

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！仲間たちと一緒にRaspberry Pi、Arduino、ESP32についてさらに深く学びましょう。

    **参加する理由は？**

    - **専門家のサポート**: コミュニティやチームの助けを借りて、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換し、スキルを向上させましょう。
    - **限定プレビュー**: 新製品の発表や先行情報をいち早く入手できます。
    - **特別割引**: 最新製品の特別割引をお楽しみください。
    - **イベント・プレゼント**: プレゼント企画や祝日セールに参加しましょう。

    👉 一緒に探求し、創造を楽しみませんか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _py_iot_ble_lock:

8.16 Bluetoothロックコントローラー
==========================================

このプロジェクトでは、Bluetooth機能を備えたRaspberry Pi Pico 2 Wを使用してスマートロックシステムを構築します。ロックに使用するサーボモーターはPico 2 Wに接続され、カスタムモバイルアプリからのコマンドをBLE（Bluetooth Low Energy）通信で受け取り、ロックやアンロックを行います。

本プロジェクトを通じて、Raspberry Pi Pico 2 Wを使ったIoTアプリケーション開発の一例として、Bluetooth機能と物理的な制御メカニズムとの統合方法を学ぶことができます。BLE通信とサーボ制御の両面から、MicroPythonを利用した実践的な学習に役立ちます。

使用するアプリは |link_appinventor| で開発しました。

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
        - :ref:`cpn_servo`
        - 1
        - |link_servo_buy|

.. image:: img/wiring/8.16_bb.png
   :width: 90%

.. raw:: html

   <br/>

2. Androidアプリを作成する
+++++++++++++++++++++++++++++++++

|link_appinventor| という無料のウェブアプリケーションを利用し、Android向けのアプリを開発します。ドラッグ＆ドロップ操作で機能的なアプリを直感的に作成でき、Android開発の初心者にも適しています。

以下の手順に従ってください：

#. |link_appinventor_login| へアクセスし、"online tool"をクリックしてログインします。Googleアカウントを使ってMIT App Inventorに登録が必要です。

   .. image:: img/13-ai-signup.png
       :width: 90%
       :align: center

#. ログイン後、 **Projects** -> **Import project (.aia) from my computer** を選択し、 ``pico-2w-kit/micropython/iot/8.16-ble_lock`` にある ``ble_lock_picow.aia`` ファイルをアップロードします。

   または、以下から直接ダウンロードできます： :download:`ble_lock_picow.aia</_static/other/ble_lock_picow.aia>`

   .. image:: img/13-ai-import.png
        :align: center

#. アップロードが完了すると、MIT App Inventorのインターフェイスにあらかじめ設定されたアプリのテンプレートが表示されます。プラットフォームに慣れたら、自由にカスタマイズできます。

#. MIT App Inventorには、 **Designer** と **Blocks** の2つの主要セクションがあります。ページ右上のタブで切り替えられます。

   .. image:: img/13-ai-intro-1.png

#. **Designer** では、ボタンやテキスト、画面レイアウトなどを追加し、アプリの全体的なデザインを編集できます。

   .. image:: img/16-ai-intro-2.png
      :width: 100%
   
#. **Blocks** セクションでは、アプリの各コンポーネントに対してどのような機能を持たせるかを、ブロックを組み合わせる形で定義します。

   .. image:: img/16-ai-intro-3.png
      :width: 100%

#. スマートフォンにアプリをインストールするには、 **Build** タブをクリックします。

   .. image:: img/13-ai-intro-4.png
      :width: 60%
      :align: center

   * ``.apk`` ファイルを生成します。このオプションを選択すると、 ``.apk`` ファイルをダウンロードするか、QRコードをスキャンしてインストールするかを選択できるページが表示されます。インストールガイドに従ってアプリのインストールを完了してください。  

     事前コンパイル済みのAPKファイルは、こちらからダウンロード可能です：:download:`ble_lock_picow.apk</_static/other/ble_lock_picow.apk>`

   * Google Playなどのアプリマーケットに公開したい場合は、 ``.aab``  ファイルを生成できます。


3. コードを実行する
+++++++++++++++++++++++++++++++++

``pico-2w-kit/micropython/iot/8.16-ble_lock`` のパスにある ``8.16-ble_lock.py`` ファイルを開くか、以下のコードをIDEにコピーしてください。
   
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
   
   import struct
   from micropython import const
   
   servo = machine.PWM(machine.Pin(15))
   servo.freq(50)
   
   _IRQ_CENTRAL_CONNECT = const(1)
   _IRQ_CENTRAL_DISCONNECT = const(2)
   _IRQ_GATTS_WRITE = const(3)
   
   _FLAG_READ = const(0x0002)
   _FLAG_WRITE_NO_RESPONSE = const(0x0004)
   _FLAG_WRITE = const(0x0008)
   _FLAG_NOTIFY = const(0x0010)
   
   _LOCK_UUID = bluetooth.UUID("f3ac7f80-5045-47b0-88fe-24d858e2e92f")
   _SWITCH_CHAR = (
       bluetooth.UUID("808b6a74-8d38-4114-8cb7-0ac9465db42d"),
       _FLAG_READ | _FLAG_WRITE | _FLAG_WRITE_NO_RESPONSE,
   )
   _LOCK_SERVICE = (
       _LOCK_UUID,
       (_SWITCH_CHAR,),
   )
   
   
   class BLELock:
       def __init__(self, ble, name="PICO-LOCK"):
   
           self._ble = ble
           self._ble.active(True)
           self._ble.irq(self._irq)
   
           handles = self._ble.gatts_register_services((_LOCK_SERVICE,))
           # print("Registered handles:", handles)
   
           ((self._handle_note,),) = handles
           self._connections = set()
   
           self._write_callback = None
   
           self._payload = advertising_payload(name=name, services=[_LOCK_UUID])
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
   
   def interval_mapping(x, in_min, in_max, out_min, out_max):
       return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
   
   def servo_write(pin,angle):
       pulse_width=interval_mapping(angle, 0, 180, 0.5,2.5)
       duty=int(interval_mapping(pulse_width, 0, 20, 0,65535))
       pin.duty_u16(duty)
   
   def lock_update(data):
       print("Receive:", data)
   
       decoded_data = struct.unpack('I', data)[0]
   
       if decoded_data == 1:
           servo_write(servo,90)
       else:
           servo_write(servo,0)
   
   
   def demo():
       ble = bluetooth.BLE()
       piano = BLELock(ble,"pico2w")
   
       while True:
           if piano.is_connected():
               piano.on_write(lock_update)
           # time.sleep_ms(100)
   
   if __name__ == "__main__":
       demo()

4. アプリとBluetoothの接続
++++++++++++++++++++++++++++++++++++++++++

先ほど作成した「Bluetooth controlled lock ble」アプリをスマートフォンにインストールしておきます。

#. スマートフォンのBluetoothを有効にします。

#. **Bluetooth controlled lock ble** アプリを起動します。

   .. image:: img/16_app_2.png
      :width: 25%
      :align: center

#. 初回起動時には、Bluetooth機能のために2つの連続ダイアログが表示されます。これらの権限を許可してください。

   .. image:: img/16_app_3.png
      :width: 100%
      :align: center

#. アプリで鍵のアイコンをタップし、アプリとPico 2 WをBluetoothで接続します。

   .. image:: img/16_app_4.png
      :width: 55%
      :align: center

#. 表示されるデバイス一覧から ``xx.xx.xx.xx.xx.xx pico2w`` を選択します。各デバイス名の横にはMACアドレスが付属しています。

   .. image:: img/13_app_5.png
      :width: 60%
      :align: center

#. デバイスが表示されない場合、スマートフォンで位置情報を有効にしてみてください。（一部のAndroidバージョンでは、位置情報とBluetooth機能が連動しています。）

#. 接続完了後、メイン画面に戻り、解除・ロックのボタンをタップするとサーボモーターが制御され、ロックの開閉を行います。

   .. image:: img/16_app_7.png
      :width: 90%
      :align: center