.. note:: 

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！仲間たちと一緒にRaspberry Pi、Arduino、ESP32についてさらに深く学びましょう。

    **参加する理由は？**

    - **専門家のサポート**: コミュニティやチームの助けを借りて、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換して、スキルを向上させましょう。
    - **限定プレビュー**: 新製品の発表や先行情報をいち早く手に入れましょう。
    - **特別割引**: 最新製品の特別割引をお楽しみください。
    - **イベント・プレゼント**: プレゼント企画や祝日セールに参加しましょう。

    👉 一緒に探求し、創造を楽しみませんか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _py_iot_access:

8.1 ネットワークへの接続
===========================

.. note::

    他のIoTプロジェクトから来た場合は、ステップ3から始めて、 ``do_connect.py`` と ``secrets.py`` の作成を進めてください。

それでは、Wi-Fiネットワークへの接続方法を見ていきましょう。

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


1. インターネットへの接続
------------------------------------

わずか5行のMicroPythonコードで、Raspberry Pi Pico 2 Wはインターネットに接続されます。

これらの5行のコードは、シェルから直接実行できます。入力後に ``Enter`` を押してください。
または、以下の方法で新しい ``.py`` ファイルを作成して実行することもできます。

.. code-block:: python

    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect("SSID","PASSWORD")
    print(wlan.isconnected())

#. Thonnyで **新規作成** ボタンをクリックし、上記のコードをコピー＆ペーストして、 ``SSID`` と ``PASSWORD`` を自分のものに変更してください。

   .. image:: img/access1.png

#. スクリプトを実行するには、 **現在のスクリプトを実行** ボタンをクリックするか、F5を押してください。接続が成功すれば、 ``true`` が表示されます。

   .. note::

       Raspberry Pi Pico 2 WがUSBケーブルでコンピュータに接続されていることを確認し、右下隅をクリックして、MicroPython (Raspberry Pi Pico).COMXxxをインタープリタとして選択してください。

   .. image:: img/access2.png


2. タイムアウト判定とIP表示
-----------------------------------------------


ネットワーク環境が悪い場合を考慮して、コードにタイムアウト判定を追加しましょう。

接続が成功した場合、Pico 2 WのIPが表示されます。以下のスクリプトをコピーして実行してください。

.. code-block:: python

    import network
    import time

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect("SSID","PASSWORD")

    # 接続待機または失敗
    wait = 10
    while wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        wait -= 1
        print('waiting for connection...')
        time.sleep(1)

    # 接続エラーの処理
    if wlan.status() != 3:
        raise RuntimeError('wifi connection failed')
    else:
        print('connected')
        print('IP: ', wlan.ifconfig()[0])

.. image:: img/access3.png

* ``wlan.status()`` 関数: 無線接続の現在の状態を返します。戻り値は以下の表に示されています。


    .. list-table::
        :widths: 40 10 50

        * - 状態
          - 値
          - 説明
        * - STAT_IDLE 
          - 0 
          - 接続なし、アクティビティなし、
        * - STAT_CONNECTING 
          - 1 
          - 接続中、
        * - STAT_WRONG_PASSWORD 
          - -3 
          - パスワード間違いで接続失敗、
        * - STAT_NO_AP_FOUND 
          - -2 
          - アクセスポイントが見つからなかったため接続失敗、
        * - STAT_CONNECT_FAIL 
          - -1 
          - その他の問題で接続失敗、
        * - STAT_GOT_IP 
          - 3 
          - 接続成功。

* ``wlan.ifconfig()`` 関数: IPアドレス、サブネットマスク、ゲートウェイ、DNSサーバーを取得します。このメソッドを呼び出すと、上記の情報を含む4つのタプルが返されます。この場合、IPアドレスのみを表示しています。

*  `class WLAN – MicroPython Docs <https://docs.micropython.org/en/latest/library/network.WLAN.html>`_

.. _create_secrets:

3. ``secrets.py`` に個人情報を保存
----------------------------------------------------------

Pico 2 Wプロジェクトを共有する際に、他の人にWi-FiパスワードやAPIキーを見られたくない場合があります。
セキュリティを確保するために、 ``secrets.py`` ファイルを作成して個人情報を保存することができます。

#. 以下のコードを新しいスクリプトファイルにコピーします。 ``SSID`` と ``PASSWORD`` は自分のものに変更してください。

    .. code-block:: python

        secrets = {
        'ssid': 'SSID',
        'password': 'PASSWORD',
        }

#. 保存ボタンをクリックするか、 ``Ctrl+S`` を押すと、ポップアップウィンドウが表示されます。そこでRaspberry Pi Picoを選択します。

    .. image:: img/access4.png

#. 名前を ``secrets.py`` に設定します。

    .. image:: img/access5.png

#. Raspberry Pi Pico 2 Wでこのスクリプトが表示されるようになります。

    .. image:: img/access6.png

#. 他のスクリプトで以下のように呼び出すことができます。実行すると、Wi-Fi接続が成功します。 ``secrets.py`` ファイルはライブラリとしてインポートされるため、情報漏洩を心配する必要はありません。

    .. code-block:: python
        :emphasize-lines: 3,7

        import network
        import time
        from secrets import secrets

        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(secrets['ssid'], secrets['password'])

        # 接続待機または失敗
        wait = 10
        while wait > 0:
            if wlan.status() < 0 or wlan.status() >= 3:
                break
            wait -= 1
            print('waiting for connection...')
            time.sleep(1)

        # 接続エラーの処理
        if wlan.status() != 3:
            raise RuntimeError('wifi connection failed')
        else:
            print('connected')
            print('IP: ', wlan.ifconfig()[0])

    .. image:: img/access8.png

.. _do_connect:

4. ``do_connect.py`` を使ってインターネットに接続
--------------------------------------------------------------

次のプロジェクトでネットワーク接続が必要になることを考慮し、 ``do_connect.py`` ファイルを新たに作成し、再利用可能な関数をその中に書き込むと、複雑なプロジェクトのコードが大幅に簡素化されます。

#. 以下のコードを新しいスクリプトファイルにコピーし、Raspberry Pi Picoに ``do_connect.py`` として保存します。

    .. code-block:: python

        import network
        import time
        from secrets import *

        def do_connect(ssid=secrets['ssid'],psk=secrets['password']):
            wlan = network.WLAN(network.STA_IF)
            wlan.active(True)
            wlan.connect(ssid, psk)

            # 接続待機または失敗
            wait = 10
            while wait > 0:
                if wlan.status() < 0 or wlan.status() >= 3:
                    break
                wait -= 1
                print('waiting for connection...')
                time.sleep(1)

            # 接続エラーの処理
            if wlan.status() != 3:
                raise RuntimeError('wifi connection failed')
            else:
                print('connected')
                ip=wlan.ifconfig()[0]
                print('network config: ', ip)
                return ip

    .. image:: img/access7.png

#. 他のスクリプトで以下のように呼び出すことで、Raspberry Pi Pico 2 Wがネットワークに接続されます。

    .. code-block:: python

        from do_connect import *
        do_connect()


.. https://www.tomshardware.com/reviews/raspberry-pi-pico-w


