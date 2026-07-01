.. note:: 

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！仲間たちと一緒にRaspberry Pi、Arduino、ESP32についてさらに深く学びましょう。

    **参加する理由は？**

    - **専門家のサポート**: コミュニティやチームの助けを借りて、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換して、スキルを向上させましょう。
    - **限定プレビュー**: 新製品の発表や先行情報をいち早く手に入れましょう。
    - **特別割引**: 最新製品の特別割引をお楽しみください。
    - **イベント・プレゼント**: プレゼント企画や祝日セールに参加しましょう。

    👉 一緒に探求し、創造を楽しみませんか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _py_iot_openweather:

8.4 @OpenWeatherMapからリアルタイムの天気情報を取得
======================================================


このプロジェクトでは、LCDに都市の天気と時刻を表示するスマート時計を作成します。


**1. 必要なコンポーネント**

このプロジェクトで使用するコンポーネントは以下の通りです。

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
        - :ref:`cpn_i2c_lcd`
        - 1
        - |link_i2clcd1602_buy|
    *   - 6
        - :ref:`cpn_lipo_charger`
        - 1
        -  
    *   - 7
        - Power Pack
        - 1
        -  

**2. 回路を組み立てる**

    .. warning:: 
        
        Li-po充電モジュールが図のように接続されていることを確認してください。そうしないと、短絡が原因でバッテリーや回路が損傷する可能性があります。

.. image:: img/wiring/4.owm_bb.png


**3. OpenWeather APIキーを取得する**

|link_openweather| は、OpenWeather Ltdが提供するオンラインサービスで、APIを通じて世界中の天気データを提供します。これには、現在の天気データ、予報、今後の天気、そして任意の地理的場所の履歴データが含まれます。

#. |link_openweather| にアクセスして、ログインまたはアカウントを作成します。

    .. image:: img/OWM-1.png

#. ナビゲーションバーからAPIページにアクセスします。

    .. image:: img/OWM-2.png

#. **現在の天気データ** を見つけて、 **購読する** をクリックします。

    .. image:: img/OWM-3.png

#. **現在の天気および予報のコレクション** の下で、適切なサービスを購読します。プロジェクトでは、無料プランで十分です。

   .. image:: img/OWM-4.png

#. **APIキー** ページからキーをコピーします。

   .. image:: img/OWM-5.png

#. コピーしたキーを、Raspberry Pi Pico 2 Wの ``secrets.py`` スクリプトに貼り付けます。

    .. image:: img/4_openweather1(1).png

    .. note::

        Pico 2 Wに ``do_connect.py`` と ``secrets.py`` のスクリプトがない場合は、これらを作成する必要があります。作成方法については :ref:`py_iot_access` を参照してください。

    .. code-block:: python
        :emphasize-lines: 5

        secrets = {
        'ssid': 'SSID',
        'password': 'PASSWORD',
        'openweather_api_key':'OPENWEATHERMAP_API_KEY'
        }

**4. スクリプトを実行する**

#. ``pico-2w-kit-main/micropython/iot`` のパスにある ``8.4_weather.py`` ファイルを開き、 **現在のスクリプトを実行** ボタンをクリックするか、F5を押して実行します。

    .. image:: img/4_openweather2.png


#. スクリプトが実行されると、I2C LCD1602にあなたの場所の時刻と天気情報が表示されます。


    .. note:: 

        コードが実行中に画面が空白の場合、モジュールの背面にあるポテンショメーターを調整してコントラストを上げることができます。

#. このスクリプトを起動時に実行したい場合は、Raspberry Pi Pico 2 Wに ``main.py`` として保存できます。


**仕組みは？**

このプロジェクトはネットワーク接続を必要とし、 :ref:`py_iot_access` メソッドを使用してネットワークに接続します。

.. code-block:: python

    from secrets import *
    from do_connect import *
    do_connect()

from do_connect import * : これは `do_connect()` 関数をインポートし、この関数によりWi-Fi接続のロジックが含まれています。 `do_connect()` 関数が呼び出されると、 `secrets.py` で指定されたWi-Fiネットワークに接続します。接続に失敗した場合は例外が発生し、成功すれば次のステップに進みます。

from secrets import * : `secrets.py` ファイルは通常、Wi-FiのSSID、パスワード、その他の機密情報（APIキーなど）を格納するために使われます。これにより、機密情報をメインコードファイルに直接埋め込まないようにします。

インターネットに接続した後、次の数行のコードでPico 2 Wをグリニッチ標準時に同期させます。

.. code-block:: python

   import ntptime
   while True:
      try:
         ntptime.settime()
         print('Time Set Successfully')
         break
      except OSError:
         print('Time Setting...')
         continue   

LCDを初期化します。使用方法の詳細については :ref:`py_lcd` を参照してください。

.. code-block:: python

   from lcd1602 import LCD
   lcd=LCD()
   lcd.clear() 
   string = 'Loading...'
   lcd.message(string)

次に、いくつかの天気データ（例：温度、風速）の単位を選択する必要があります。この場合、単位は ``metric`` です。

.. code-block:: python

   # Open Weather
   TEMPERATURE_UNITS = {
      "standard": "K",
      "metric": "°C",
      "imperial": "°F",
   }

   SPEED_UNITS = {
      "standard": "m/s",
      "metric": "m/s",
      "imperial": "mph",
   }

   units = "metric"

次に、この関数を使って天気データを ``openweathermap.org`` から取得します。
この関数は、都市、APIキー、設定された単位を含むURLメッセージを送信します。
その結果、天気データを含む ``JSON`` ファイルを受け取ります。

.. code-block:: python

   def get_weather(city, api_key, units='metric', lang='en'):
      '''
      Get weather data from openweathermap.org
         city: City name, state code and country code divided by comma, Please, refer to ISO 3166 for the state codes or country codes. https://www.iso.org/obp/ui/#search
         api_key: Your unique API key (you can always find it on your openweather account page under the "API key" tab https://home.openweathermap.org/api_keys)
         unit: Units of measurement. standard, metric and imperial units are available. If you do not use the units parameter, standard units will be applied by default. More: https://openweathermap.org/current#data
         lang: You can use this parameter to get the output in your language. More: https://openweathermap.org/current#multi
      '''
      url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={units}&lang={lang}"
      print(url)
      res = urequests.post(url)
      return res.json()

この生データを出力すると、次のような情報が表示されます。

.. code-block:: python

   weather data example:
   {
       'timezone': 28800,
       'sys': {
           'type': 2,
           'sunrise': 1659650200,
           'country': 'CN',
           'id': 2031340,
           'sunset': 1659697371
       },
       'base': 'stations',
       'main': {
           'pressure': 1008,
           'feels_like': 304.73,
           'temp_max': 301.01,
           'temp': 300.4,
           'temp_min': 299.38,
           'humidity': 91,
           'sea_level': 1008,
           'grnd_level': 1006
       },
       'visibility': 10000,
       'id': 1795565,
       'clouds': {
           'all': 96
       }, 
       'coord': {
           'lon': 114.0683,
           'lat': 22.5455
       },
       'name': 'Shenzhen',
       'cod': 200,
       'weather':[{
           'id': 804,
           'icon': '04d',
           'main': 'Clouds',
           'description': 'overcast clouds'
       }],
       'dt': 1659663579,
       'wind': {
           'gust': 7.06,
           'speed': 3.69,
           'deg': 146
       }
   }

``print_weather(weather_data)`` 関数を使って、この生データを読みやすい形式に変換し、表示します。

この関数は呼び出されていないため、必要に応じて ``while True`` 内のこの行のコメントを解除してください。

.. image:: img/4_openweather3.png

.. code-block:: python
   :emphasize-lines: 2

   # shell print
   print_weather(weather_data)

``while True`` ループ内で、最初に ``get_weather()`` 関数を呼び出して、プロジェクトに必要な ``weather`` 、 ``temperature`` 、および ``humidity`` の情報を取得します。

.. code-block:: python

   weather_data = get_weather('shenzhen', secrets['openweather_api_key'], units=units)
   weather=weather_data["weather"][0]["main"]
   t=weather_data["main"]["temp"]
   rh=weather_data["main"]["humidity"]

ローカル時間を取得します。 ``time.localtime()`` 関数は、タプル（年、月、日、時、分、秒、曜日、年の日数）を返します。ここでは ``hour`` と ``minute`` を取り出します。

Pico 2 Wはすでにグリニッチ標準時に同期されているので、現在地のタイムゾーンを加算する必要があります。

.. code-block:: python
    
    # get time (+24 allows for western hemisphere)
    # if negative, add 24
    # hours = time.localtime()[3] + int(weather_data["timezone"] / 3600) + 24  #only for west hemisphere

    hours=time.localtime()[3]+int(weather_data["timezone"] / 3600)
    mins=time.localtime()[4]

最後に、天気情報と時間がLCD1602に表示されます。

.. code-block:: python

   lcd.clear() 
   time.sleep_ms(200)
   string = f'{hours:02d}:{mins:02d} {weather}\n'
   lcd.message(string)
   string = f'{t}{TEMPERATURE_UNITS[units]} {rh}%rh'
   lcd.message(string)

メインループが30秒ごとに実行されると、LCD1602は30秒ごとに更新される時計になります。



.. OPW的文档页面, 可以查找每种产品的所有技术信息。https://openweathermap.org/api


.. 查看获取到的key https://home.openweathermap.org/api_keys
.. 当前天气的资料页 https://openweathermap.org/current
.. https://openweathermap.org/appid