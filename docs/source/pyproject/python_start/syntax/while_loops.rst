.. note::  

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！仲間たちと一緒にRaspberry Pi、Arduino、ESP32についてさらに深く学びましょう。

    **なぜ参加するべきか？**

    - **専門家のサポート**: 購入後の問題や技術的な課題を、コミュニティやチームの助けを借りて解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換し、スキルを向上させましょう。
    - **限定プレビュー**: 新製品の発表や先行情報をいち早く手に入れることができます。
    - **特別割引**: 最新製品の特別割引をお楽しみいただけます。
    - **季節限定プロモーションやプレゼント企画**: プレゼント企画や祝日セールに参加しましょう。

    👉 一緒に探求し、創造を楽しみませんか？[|link_sf_facebook|] をクリックして、今すぐ参加してください！


.. _py_syntax_while:

While Loops
====================

``while`` 文は、特定の条件が満たされている限り、プログラムをループして実行するために使用されます。つまり、繰り返し処理が必要なタスクを処理するためにループ内でプログラムを実行します。

その基本的な形式は次の通りです：

.. code-block:: python

    while test expression:
        Body of while


``while`` ループでは、まず ``test expression`` を確認します。 ``test expression`` が ``True`` の場合にのみ、while の本体に入ります。1回のイテレーション後に、再度 ``test expression`` をチェックします。このプロセスは、 ``test expression`` が ``False`` になるまで続きます。

MicroPython では、 ``while`` ループの本体はインデントで決まります。

本体はインデントから始まり、最初のインデントなしの行で終了します。

Python は、非ゼロの値を ``True`` と解釈します。None と 0 は ``False`` と解釈されます。

**while ループのフローチャート**

.. image:: img/while_loop.png



.. code-block:: python

    x = 10

    while x > 0:
        print(x)
        x -= 1

>>> %Run -c $EDITOR_CONTENT
10
9
8
7
6
5
4
3
2
1


Break Statement
--------------------

break文を使用すると、while 条件が true の場合でもループを停止できます：



.. code-block:: python

    x = 10

    while x > 0:
        print(x)
        if x == 6:
            break
        x -= 1

>>> %Run -c $EDITOR_CONTENT
10
9
8
7
6

While Loop with Else
------------------------

``if`` ループと同様に、 ``while`` ループにもオプションの ``else`` ブロックがあります。

``while`` ループ内の条件が ``False`` と評価されると、 ``else`` 部分が実行されます。

.. code-block:: python

    x = 10

    while x > 0:
        print(x)
        x -= 1
    else:
        print("Game Over")

>>> %Run -c $EDITOR_CONTENT
10
9
8
7
6
5
4
3
2
1
Game Over