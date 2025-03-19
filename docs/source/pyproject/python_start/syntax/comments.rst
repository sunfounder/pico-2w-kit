.. note:: 

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！仲間たちと一緒にRaspberry Pi、Arduino、ESP32についてさらに深く学びましょう。

    **参加する理由は？**

    - **専門家のサポート**: コミュニティやチームの助けを借りて、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換し、スキルを向上させましょう。
    - **限定プレビュー**: 新製品の発表や先行情報をいち早く入手できます。
    - **特別割引**: 最新製品の特別割引をお楽しみください。
    - **イベント・プレゼント**: プレゼント企画や祝日セールに参加しましょう。

    👉 一緒に探求し、創造を楽しみませんか？Click [|link_sf_facebook|] and join today!

Comments
=============

コードにおけるコメントは、コードを理解しやすくし、可読性を高めたり、テスト時に特定の部分を実行しないよう一時的に無効化する目的で使用されます。

Single-line Comment
----------------------------

MicroPythonにおける単一行コメントは「#」で始まり、その行の終わりまでがコメントとして扱われます。コメントはコードの前後に置くことができます。

.. code-block:: python

    print("hello world") #これはアノテーションです

>>> %Run -c $EDITOR_CONTENT
hello world

コメントは必ずしもコードを説明するテキストだけではありません。実行を防ぎたいコードをコメントアウトして、MicroPythonに認識させない方法としても使えます。

.. code-block:: python

    #print("Can't run it！")
    print("hello world") #これはアノテーションです

>>> %Run -c $EDITOR_CONTENT
hello world

Multi-line comment
------------------------------

複数行にわたるコメントを記述したい場合は、複数の「#」を使う方法があります。

.. code-block:: python

    #これはコメントです
    #複数行に
    #わたって書かれています
    print("Hello, World!")

>>> %Run -c $EDITOR_CONTENT
Hello, World!

もしくは、複数行の文字列を使う方法があります。

MicroPythonは、変数に代入されていない文字列リテラルを無視するため、トリプルクォートを使って複数行の文字列をコード内に書き、その中にコメントを含めることができます。

.. code-block:: python

    """
    This is a comment
    written in
    more than just one line
    """
    print("Hello, World!")

>>> %Run -c $EDITOR_CONTENT
Hello, World!

変数に代入されていない限り、この文字列はMicroPythonがコードを読み込んだ後に無視するため、実質的に複数行コメントのように扱えます。
