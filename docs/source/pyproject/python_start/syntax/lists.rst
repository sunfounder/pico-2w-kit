.. note::  

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！仲間たちと一緒にRaspberry Pi、Arduino、ESP32についてさらに深く学びましょう。

    **なぜ参加するべきか？**

    - **専門家のサポート**: 購入後の問題や技術的な課題を、コミュニティやチームの助けを借りて解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換し、スキルを向上させましょう。
    - **限定プレビュー**: 新製品の発表や先行情報をいち早く手に入れることができます。
    - **特別割引**: 最新製品の特別割引をお楽しみいただけます。
    - **季節限定プロモーションやプレゼント企画**: プレゼント企画や祝日セールに参加しましょう。

    👉 一緒に探求し、創造を楽しみませんか？[|link_sf_facebook|] をクリックして、今すぐ参加してください！


.. _syntax_list:

Lists
===================

リストは、複数のアイテムを単一の変数に格納するために使用され、角括弧で作成します：

.. code-block:: python

    B_list = ["Blossom", "Bubbles","Buttercup"]
    print(B_list)


リストのアイテムは変更可能で順序があり、重複した値も許容します。
リストのアイテムにはインデックスが付けられており、最初のアイテムはインデックス[0]、2番目のアイテムはインデックス[1]、というように順番が付けられます。

.. code-block:: python

    C_list = ["Red", "Blue", "Green", "Blue"]
    print(C_list)            # 重複あり
    print(C_list[0]) 
    print(C_list[1])         # 順序あり
    C_list[2] = "Purple"     # 変更可能
    print(C_list)

>>> %Run -c $EDITOR_CONTENT
['Red', 'Blue', 'Green', 'Blue']
Red
Blue
['Red', 'Blue', 'Purple', 'Blue']


リストは異なるデータ型を含むことができます：

.. code-block:: python

    A_list = ["Banana", 255, False, 3.14]
    print(A_list)

>>> %Run -c $EDITOR_CONTENT
['Banana', 255, False, 3.14]


リストの長さ
------------------
リストに含まれるアイテムの数を確認するには、len()関数を使用します。

.. code-block:: python

    A_list = ["Banana", 255, False, 3.14]
    print(len(A_list))

>>> %Run -c $EDITOR_CONTENT
4

リストのアイテムを確認する
--------------------------

リストの2番目のアイテムを表示する：

.. code-block:: python

    A_list = ["Banana", 255, False, 3.14]
    print(A_list[1])

>>> %Run -c $EDITOR_CONTENT
[255]

リストの最後のアイテムを表示する：

.. code-block:: python

    A_list = ["Banana", 255, False, 3.14]
    print(A_list[-1])

>>> %Run -c $EDITOR_CONTENT
[3.14]

2番目、3番目のアイテムを表示する：

.. code-block:: python

    A_list = ["Banana", 255, False, 3.14]
    print(A_list[1:3])

>>> %Run -c $EDITOR_CONTENT
[255, False]


リストのアイテムを変更する
----------------------------

2番目、3番目のアイテムを変更する：

.. code-block:: python

    A_list = ["Banana", 255, False, 3.14]
    A_list[1:3] = [True,"Orange"] 
    print(A_list)

>>> %Run -c $EDITOR_CONTENT
['Banana', True, 'Orange', 3.14]

2番目の値を2つの値で置き換える：

.. code-block:: python

    A_list = ["Banana", 255, False, 3.14]
    A_list[1:2] = [True,"Orange"] 
    print(A_list)

>>> %Run -c $EDITOR_CONTENT
['Banana', True, 'Orange', False, 3.14]


リストにアイテムを追加する
------------------------------

append()メソッドを使用してアイテムを追加する：

.. code-block:: python

    C_list = ["Red", "Blue", "Green"]
    C_list.append("Orange")
    print(C_list)

>>> %Run -c $EDITOR_CONTENT
['Red', 'Blue', 'Green', 'Orange']

アイテムを2番目の位置に挿入する：

.. code-block:: python

    C_list = ["Red", "Blue", "Green"]
    C_list.insert(1, "Orange")
    print(C_list)

>>> %Run -c $EDITOR_CONTENT
['Red', 'Orange', 'Blue', 'Green']



リストからアイテムを削除する
-------------------------------

remove()メソッドは指定されたアイテムを削除します。

.. code-block:: python

    C_list = ["Red", "Blue", "Green"]
    C_list.remove("Blue")
    print(C_list)

>>> %Run -c $EDITOR_CONTENT
['Red', 'Green']

pop()メソッドは指定されたインデックスを削除します。インデックスを指定しない場合、pop()メソッドは最後のアイテムを削除します。

.. code-block:: python

    A_list = ["Banana", 255, False, 3.14, True,"Orange"]
    A_list.pop(1)
    print(A_list)
    A_list.pop()
    print(A_list)

>>> %Run -c $EDITOR_CONTENT
255
['Banana', False, 3.14, True, 'Orange']
'Orange'
['Banana', False, 3.14, True]

``del`` キーワードも指定されたインデックスを削除します：

.. code-block:: python

    C_list = ["Red", "Blue", "Green"]
    del C_list[1]
    print(C_list)

>>> %Run -c $EDITOR_CONTENT
['Red', 'Green']

clear()メソッドはリストを空にします。リストはまだ存在しますが、内容はありません。

.. code-block:: python

    C_list = ["Red", "Blue", "Green"]
    C_list.clear()
    print(C_list)

>>> %Run -c $EDITOR_CONTENT
[]