.. note::  

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！仲間たちと一緒にRaspberry Pi、Arduino、ESP32についてさらに深く学びましょう。

    **なぜ参加するべきか？**

    - **専門家のサポート**: 購入後の問題や技術的な課題を、コミュニティやチームの助けを借りて解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換し、スキルを向上させましょう。
    - **限定プレビュー**: 新製品の発表や先行情報をいち早く手に入れることができます。
    - **特別割引**: 最新製品の特別割引をお楽しみいただけます。
    - **季節限定プロモーションやプレゼント企画**: プレゼント企画や祝日セールに参加しましょう。

    👉 一緒に探求し、創造を楽しみませんか？[|link_sf_facebook|] をクリックして、今すぐ参加してください！


Functions
===============

MicroPythonにおいて、関数は特定のタスクを実行する関連ステートメントの集まりです。

関数を使うことでプログラムを小さくモジュール化されたブロックに分割できます。プランが大きくなるほど、関数を使うことで整理しやすくなり、管理が容易になります。

さらに、重複を避け、コードを再利用可能にします。

Create a Function
--------------------

.. code-block::

    def function_name(parameters): 
        """docstring"""
        statement(s)

* 関数は ``def`` キーワードで定義します

* 関数名は関数を一意に識別するための名前です。変数の命名と同様のルールに従います。
    
   * 数字、文字、アンダースコアのみを使用可能
   * 先頭文字は文字またはアンダースコア
   * 大文字と小文字を区別

* 引数（パラメータ）を使って関数に値を渡せます（オプション）

* コロン (:) は関数ヘッダの終わりを示します

* 任意のdocstring（複数行に渡る場合はトリプルクォート）で、関数の説明を記述できます

* 関数本体は1つ以上のMicropythonステートメントからなるブロックで、すべて同じインデントレベル（通常は4スペース）です

* 関数本体を空にする必要がある場合は、エラーを回避するために pass ステートメントを使用できます

* オプションで ``return`` 文を使い、関数から値を返せます


Calling a Function
--------------------

関数を呼び出すには、関数名の後ろに丸括弧を付けます。



.. code-block:: python

    def my_function():
        print("Your first function")

    my_function()

>>> %Run -c $EDITOR_CONTENT
Your first function

The return Statement
-----------------------

return 文は関数を終了し、呼び出し元に戻るために使われます。

**Syntax of return**

.. code-block:: python

    return [expression_list]

式を含む場合、その式は評価されて値として返されます。式がない、または関数に ``return`` 文自体がない場合、関数は ``None`` を返します。

.. code-block:: python

    def my_function():
            print("Your first function")

    print(my_function())

>>> %Run -c $EDITOR_CONTENT
Your first function
None

この例では、return 文を使っていないため、戻り値は ``None`` になります。

Arguments
-------------

関数には引数（arguments）を渡すことで情報を渡せます。

関数名の後に丸括弧を付け、必要なだけ引数をカンマで区切って指定します。



.. code-block:: python

    def welcome(name, msg):
        """This is a welcome function for
        the person with the provided message"""
        print("Hello", name + ', ' + msg)

    welcome("Lily", "Welcome to China!")

>>> %Run -c $EDITOR_CONTENT
Hello Lily, Welcome to China!


Number of Arguments
*************************

デフォルトでは、関数に正しい数の引数を与える必要があります。つまり、関数が2つのパラメータを期待するならば、引数を2つ与える必要があり、それ以上でも以下でもエラーになります。



.. code-block:: python

    def welcome(name, msg):
        """This is a welcome function for
        the person with the provided message"""
        print("Hello", name + ', ' + msg)

    welcome("Lily", "Welcome to China!")

ここで、welcome() は2つのパラメータを受け取ります。2つの引数を与えて呼び出しているため、エラーは起きません。

引数の数が合わない場合、インタープリタはエラーメッセージを表示します。

以下は引数が1つしかない呼び出しと、引数がない呼び出しに対するエラー例です。


.. code-block::

    welcome("Lily")＃Only one argument

>>> %Run -c $EDITOR_CONTENT
Traceback (most recent call last):
  File "<stdin>", line 6, in <module>
TypeError: function takes 2 positional arguments but 1 were given

.. code-block::

    welcome()＃No arguments

>>> %Run -c $EDITOR_CONTENT
Traceback (most recent call last):
  File "<stdin>", line 6, in <module>
TypeError: function takes 2 positional arguments but 0 were given


Default Arguments
*************************

MicroPythonでは、パラメータに初期値を設定（デフォルト引数）できます。
関数呼び出し時に引数が与えられなければ、このデフォルト値が使われます。

.. code-block:: python

    def welcome(name, msg = "Welcome to China!"):
        """This is a welcome function for
        the person with the provided message"""
        print("Hello", name + ', ' + msg)
    welcome("Lily")

>>> %Run -c $EDITOR_CONTENT
Hello Lily, Welcome to China!

ここで、パラメータ ``name`` はデフォルト値なしで必須。 ``msg`` はデフォルト値 "Welcome to China!" があるためオプションです。呼び出し時に別の値を渡せばデフォルト値を上書きできます。

いずれかのパラメータにデフォルト引数を設定した場合、その右側のパラメータもすべてデフォルト引数を持たなければいけません。

つまり、非デフォルト引数をデフォルト引数の後に置くことはできません。

例えば、以下の関数ヘッダはエラーとなります:

.. code-block:: python

    def welcome(name = "Lily", msg):

次のエラーメッセージが表示されます:

>>> %Run -c $EDITOR_CONTENT
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
SyntaxError: non-default argument follows default argument


Keyword Arguments
**************************

関数を特定の値で呼び出すと、これらの値は位置に基づいて引数に割り当てられます。

たとえば、先ほどのwelcome()関数をwelcome("Lily", "Welcome to China")と呼び出すと、"Lily"は ``name`` に割り当てられ、同様に"Welcome to China"は ``msg`` に割り当てられます。

MicroPythonでは、キーワード引数を使って関数を呼び出すことも可能です。この方法では、引数の順序（位置）を変更できます。

.. code-block:: python

    # キーワード引数
    welcome(name = "Lily",msg = "Welcome to China!")

    # キーワード引数（順不同）
    welcome(msg = "Welcome to China！",name = "Lily") 

    # 1つは位置引数、1つはキーワード引数
    welcome("Lily", msg = "Welcome to China!")


このように、関数呼び出しでは位置引数とキーワード引数を混在させることができます。ただし、キーワード引数は常に位置引数の後に置かなければなりません。

キーワード引数の後に位置引数を置くとエラーが発生します。

たとえば、関数呼び出しが次のようになっている場合:


.. code-block:: python

    welcome(name="Lily","Welcome to China!")

エラーが発生します:

>>> %Run -c $EDITOR_CONTENT
Traceback (most recent call last):
  File "<stdin>", line 5, in <module>
SyntaxError: non-keyword arg after keyword arg


Arbitrary Arguments
********************

時には、関数に渡される引数の数があらかじめわからないことがあります。

関数定義では、パラメータ名の前にアスタリスク(*)を付けられます。



.. code-block:: python

    def welcome(*names):
        """This function welcomes all the person
        in the name tuple"""
        # names はタプル
        for name in names:
            print("Welcome to China!", name)
            
    welcome("Lily","John","Wendy")

>>> %Run -c $EDITOR_CONTENT
Welcome to China! Lily
Welcome to China! John
Welcome to China! Wendy

ここでは、複数の引数を指定して関数を呼び出しています。これらの引数は、関数に渡される前にタプルとしてまとめられます。

関数内部では、for ループを使ってすべての引数を取り出します。

Recursion
----------------
Pythonでは、ある関数が他の関数を呼び出すだけでなく、自身を再帰的に呼び出す（再帰関数）ことができます。

再帰を正しく使うと効率的かつ数学的にエレガントな解法を得られますが、終了条件が適切でないと無限ループに陥ったり、メモリ・CPUを過剰に消費する恐れがあるため注意が必要です。




.. code-block:: python

    def rec_func(i):
        if(i > 0):
            result = i + rec_func(i - 1)
            print(result)
        else:
            result = 0
        return result

    rec_func(6)

>>> %Run -c $EDITOR_CONTENT
1
3
6
10
15
21

この例では、rec_func()は自分自身を呼び出す「再帰」用に定義した関数です。変数 ``i`` を再帰のデータとして使い、毎回再帰するたびに ``i`` を1ずつ減らします。条件が0（つまり0より大きくない）になった時点で再帰は終了します。

開発を始めたばかりの方にとっては、この仕組みを理解するのに時間がかかるかもしれませんが、試行錯誤しながらテストと修正をするのが最も良い方法です。

**Advantages of Recursion**

* コードがより読みやすく整理される
* 複雑な問題を小さなサブ問題に分割しやすい
* ネストした繰り返しより再帰のほうが扱いやすい場合がある

**Disadvantages of Recursion**

* ロジックが分かりにくいことがある
* 再帰呼び出しはメモリと処理時間を多く消費する可能性がある
* デバッグが難しくなる場合がある
