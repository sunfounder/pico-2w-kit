.. note::  

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！仲間たちと一緒にRaspberry Pi、Arduino、ESP32についてさらに深く学びましょう。

    **なぜ参加するべきか？**

    - **専門家のサポート**: 購入後の問題や技術的な課題を、コミュニティやチームの助けを借りて解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換し、スキルを向上させましょう。
    - **限定プレビュー**: 新製品の発表や先行情報をいち早く手に入れることができます。
    - **特別割引**: 最新製品の特別割引をお楽しみいただけます。
    - **季節限定プロモーションやプレゼント企画**: プレゼント企画や祝日セールに参加しましょう。

    👉 一緒に探求し、創造を楽しみませんか？[|link_sf_facebook|] をクリックして、今すぐ参加してください！


Variables
============

変数はデータ値を格納するためのコンテナです。

変数を作成するのは非常に簡単です。名前を付けて値を割り当てるだけです。変数に値を割り当てる際にデータ型を指定する必要はありません。変数は参照であり、割り当てを通じて異なるデータ型のオブジェクトにアクセスします。

変数名を付ける際には、次のルールに従う必要があります：

* 変数名には数字、アルファベット、アンダースコアのみを含めることができます。
* 変数名の最初の文字はアルファベットまたはアンダースコアでなければなりません。
* 変数名は大文字と小文字を区別します。

Create Variable
-------------------

MicroPythonでは、変数を宣言するためのコマンドはありません。変数は、初めて値を割り当てたときに作成されます。特定の型宣言を使用する必要はなく、変数を設定した後に型を変更することもできます。

.. code-block:: python

    x = 8       # xはint型
    x = "lily"  # xはstr型に変更
    print(x)

>>> %Run -c $EDITOR_CONTENT
lily


Casting
-------------

変数のデータ型を指定したい場合、キャスティングを使用して行うことができます。

.. code-block:: python

    x = int(5)    # y will be 5
    y = str(5)    # x will be '5'
    z = float(5)  # z will be 5.0
    print(x,y,z)

>>> %Run -c $EDITOR_CONTENT
5 5 5.0

Get the Type
-------------------

変数のデータ型を取得するには、`type()` 関数を使用します。

.. code-block:: python

    x = 5
    y = "hello"
    z = 5.0
    print(type(x),type(y),type(z))

>>> %Run -c $EDITOR_CONTENT
<class 'int'> <class 'str'> <class 'float'>

Single or Double Quotes?
---------------------------

MicroPythonでは、文字列変数を定義する際に、シングルクォートまたはダブルクォートのいずれも使用できます。

.. code-block:: python

    x = "hello"
    # は次のように同じです
    x = 'hello'

Case-Sensitive
---------------------

変数名は大文字と小文字を区別します。

.. code-block:: python

    a = 5
    A = "lily"
    # Aはaを上書きしません
    print(a, A)

>>> %Run -c $EDITOR_CONTENT
5 lily


