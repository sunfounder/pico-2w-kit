.. note::

    こんにちは！SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Raspberry Pi、Arduino、ESP32について、他の愛好者とともに深く学びましょう。

    **参加する理由**

    - **専門家サポート**: 購入後の問題や技術的な課題を、コミュニティとチームのサポートで解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換し、スキルを向上させましょう。
    - **限定プレビュー**: 新製品の発表や先行情報をいち早くチェックできます。
    - **特別割引**: 新しい製品に対する独占的な割引が利用できます。
    - **季節限定キャンペーンとプレゼント**: プレゼントやホリデープロモーションに参加しましょう。

    👉 私たちと一緒に探求し、創造する準備はできましたか？[|link_sf_facebook|] をクリックして、今すぐ参加しましょう！

1.1 MicroPythonの紹介
========================

MicroPythonは、主にPython 3と互換性のあるプログラミング言語をC言語で実装したもので、マイクロコントローラー上で動作するよう最適化されています。

MicroPythonは、Pythonコンパイラとそのバイトコードの実行環境（ランタイムインタプリタ）で構成されており、ユーザーはインタラクティブなプロンプト（REPL）を介して、サポートされているコマンドを即座に実行できます。含まれているのは、Pythonの基本的なライブラリのセレクションであり、MicroPythonには、プログラマーが低レベルのハードウェアにアクセスできるモジュールが含まれています。

* 参考: `MicroPython - Wikipedia <https://en.wikipedia.org/wiki/MicroPython>`_

物語はここから始まる
--------------------------------

2013年、Damien Georgeがクラウドファンディングキャンペーン（Kickstarter）を開始したことが転機でした。

Damienはケンブリッジ大学の学部生で、熱心なロボットプログラマーでした。彼はPythonの世界をギガバイトのマシンからキロバイトのマシンへと縮小したいと考えていました。彼のKickstarterキャンペーンは、概念実証を完成形にするための開発を支援するものでした。

MicroPythonは、プロジェクトの成功を願う多様なPythonistaコミュニティによってサポートされています。

コードベースのテストやサポートに加えて、開発者たちはチュートリアル、コードライブラリ、ハードウェアのポーティングを提供し、Damienがプロジェクトの他の側面に集中できるようにしました。

* 参考: `realpython <https://realpython.com/micropython/>`_

なぜMicroPythonなのか？
------------------------

元々、Kickstarterキャンペーンでは、MicroPythonはSTM32F4を搭載した開発ボード「pyboard」としてリリースされましたが、MicroPythonは多くのARMベースの製品アーキテクチャをサポートしています。主にサポートされているポートは、ARM Cortex-M（多くのSTM32ボード、TI CC3200/WiPy、Teensyボード、Nordic nRFシリーズ、SAMD21およびSAMD51）、ESP8266、ESP32、16bit PIC、Unix、Windows、Zephyr、JavaScriptなどです。
次に、MicroPythonは迅速なフィードバックを可能にします。これは、REPLを使ってインタラクティブにコマンドを入力し、レスポンスを得ることができるからです。コードを変更してすぐに実行することもでき、コードのコンパイル、アップロード、実行のサイクルを繰り返す必要はありません。

Pythonも同じ利点を持っていますが、Raspberry Pi Picoのような一部のマイクロコントローラボードでは、メモリが少なく、Pythonを実行するには小さすぎます。だからこそ、MicroPythonは進化し、Pythonの主要な機能を保持しつつ、これらのマイクロコントローラボードで動作するための新しい機能が追加されました。

次に、Raspberry Pi PicoにMicroPythonをインストールする方法を学びます。

* 参考: `MicroPython - Wikipedia <https://en.wikipedia.org/wiki/MicroPython>`_
* 参考: `realpython <https://realpython.com/micropython/>`_
