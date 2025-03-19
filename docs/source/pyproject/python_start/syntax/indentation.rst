.. note::  

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！仲間たちと一緒にRaspberry Pi、Arduino、ESP32についてさらに深く学びましょう。

    **なぜ参加するべきか？**

    - **専門家のサポート**: 購入後の問題や技術的な課題を、コミュニティやチームの助けを借りて解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換し、スキルを向上させましょう。
    - **限定プレビュー**: 新製品の発表や先行情報をいち早く手に入れることができます。
    - **特別割引**: 最新製品の特別割引をお楽しみいただけます。
    - **季節限定プロモーションやプレゼント企画**: プレゼント企画や祝日セールに参加しましょう。

    👉 一緒に探求し、創造を楽しみませんか？[|link_sf_facebook|] をクリックして、今すぐ参加してください！


Indentation
=============

インデントとは、コード行の先頭にある空白のことを指します。
標準的なPythonプログラムと同様に、MicroPythonプログラムも通常は上から下へと実行されます。
それぞれの行を順に解釈して実行し、次の行に進んでいきます。
これはシェルで1行ずつ入力するのと同じような動きですが、
単に行を順番に読み込むだけでは、プログラムとしてはあまり賢くありません。
そこで、Pythonと同様にMicroPythonでも、インデントを使ってプログラムの実行順序を制御します。

少なくとも1つのスペースをprint()の前に入れないと、
「Invalid syntax」というエラーメッセージが表示されます。
通常はTabキーを使って空白を統一するようにするとよいでしょう。


.. code-block:: python

    if 8 > 5:
    print("Eight is greater than Five!")

>>> %Run -c $EDITOR_CONTENT
Traceback (most recent call last):
  File "<stdin>", line 2
SyntaxError: invalid syntax

同じコードブロック内では、スペースの数を統一して使わないと、Pythonはエラーを起こします。


.. code-block:: python

    if 8 > 5:
    print("Eight is greater than Five!")
            print("Eight is greater than Five")

>>> %Run -c $EDITOR_CONTENT
Traceback (most recent call last):
  File "<stdin>", line 2
SyntaxError: invalid syntax
