.. note:: 

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！仲間たちと一緒にRaspberry Pi、Arduino、ESP32についてさらに深く学びましょう。

    **参加する理由は？**

    - **専門家のサポート**: コミュニティやチームの支援を受けながら、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換し、スキルを高めましょう。
    - **限定プレビュー**: 新製品の情報や先行発表をいち早くチェックできます。
    - **特別割引**: 最新製品の特別割引をお楽しみください。
    - **イベント・プレゼント**: プレゼント企画や祝日セールに参加しましょう。

    👉 一緒に探求し、創造を楽しみませんか？Click [|link_sf_facebook|] and join today!

Data Types
=============

Built-in Data Types
---------------------
MicroPythonには以下のデータ型があります：

* Text Type: str
* Numeric Types: int, float, complex
* Sequence Types: list, tuple, range
* Mapping Type: dict
* Set Types: set, frozenset
* Boolean Type: bool
* Binary Types: bytes, bytearray, memoryview

Getting the Data Type
-----------------------------
任意のオブジェクトのデータ型は、 ``type()`` 関数を使って取得できます。



.. code-block:: python

    a = 6.8
    print(type(a))

>>> %Run -c $EDITOR_CONTENT
<class 'float'>

Setting the Data Type
-------------------------
MicroPythonでは、変数に値を代入した時点でデータ型が決定されるため、明示的に型を指定する必要はありません。



.. code-block:: python

    x = "welcome"
    y = 45
    z = ["apple", "banana", "cherry"]

    print(type(x))
    print(type(y))
    print(type(z))

>>> %Run -c $EDITOR_CONTENT
<class 'str'>
<class 'int'>
<class 'list'>
>>>

Setting the Specific Data Type
----------------------------------

明示的にデータ型を指定したい場合は、以下のコンストラクタ関数を利用できます：

.. list-table::
    :widths: 25 10
    :header-rows: 1

    *   - Example
        - Date Type
    *   - x = int(20)
        - int
    *   - x = float(20.5)
        - float
    *   - x = complex(1j)
        - complex
    *   - x = str("Hello World")
        - str
    *   - x = list(("apple", "banana", "cherry"))
        - list
    *   - x = tuple(("apple", "banana", "cherry"))
        - tuple
    *   - x = range(6)
        - range
    *   - x = dict(name="John", age=36)
        - dict
    *   - x = set(("apple", "banana", "cherry"))
        - set
    *   - x = frozenset(("apple", "banana", "cherry"))
        - frozenset
    *   - x = bool(5)
        - bool
    *   - x = bytes(5)
        - bytes
    *   - x = bytearray(5)
        - bytearray
    *   - x = memoryview(bytes(5))
        - memoryview

いくつか出力して結果を確認してみましょう。



.. code-block:: python

    a = float(20.5)
    b = list(("apple", "banana", "cherry"))
    c = bool(5)

    print(a)
    print(b)
    print(c)

>>> %Run -c $EDITOR_CONTENT
20.5
['apple', 'banana', 'cherry']
True
>>>

Type Conversion
----------------
int()、float()、complex() メソッドを使って、ある型から別の型へ変換（キャスト）できます。Pythonでのキャストはコンストラクタ関数を用いて行います。

* int() - 整数リテラル、浮動小数点リテラル（少数を削除）、または文字列リテラル（文字列が整数を表す場合）から整数を構築
* float() - 整数リテラル、浮動小数点リテラル、あるいは文字列リテラル（文字列が浮動小数点もしくは整数を表す場合）から浮動小数点数を構築
* str() - 文字列、整数リテラル、浮動小数点リテラルなど、さまざまなデータ型から文字列を構築




.. code-block:: python

    a = float("5")
    b = int(3.7)
    c = str(6.0)

    print(a)
    print(b)
    print(c)

Note: 複素数（complex）は他の数値型に変換できません。