.. note::

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community auf Facebook! Vertiefen Sie gemeinsam mit anderen begeisterten Mitgliedern Ihre Kenntnisse rund um Raspberry Pi, Arduino und ESP32.

    **Why Join?**

    - **Expert Support**: Erhalten Sie Unterstützung bei technischen Herausforderungen und Fragen nach dem Kauf durch unsere Community und unser Team.
    - **Learn & Share**: Tauschen Sie wertvolle Tipps und Tutorials aus, um Ihre Fähigkeiten weiterzuentwickeln.
    - **Exclusive Previews**: Seien Sie die Ersten, die Produktankündigungen und exklusive Vorschauen erhalten.
    - **Special Discounts**: Profitieren Sie von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festive Promotions and Giveaways**: Nehmen Sie an Gewinnspielen und saisonalen Aktionen teil.

    👉 Bereit, mit uns auf Entdeckungsreise zu gehen und kreativ zu werden? Klicken Sie auf [|link_sf_facebook|] und treten Sie uns noch heute bei!

.. _cpn_dot_matrix:

LED-Dot-Matrix
==========================

|img_led_matrix|

LED-Dot-Matrizen werden generell in zwei Kategorien unterteilt: Common Anode (CA) und Common Cathode (CC). Der Hauptunterschied liegt in der internen Verdrahtung der LEDs. In diesem Kit kommt eine CA-Dot-Matrix (Common Anode) zum Einsatz, erkennbar am Label „788BS“ an der Seite.

Die Anordnung der Pins entnehmen Sie bitte der nachfolgenden Abbildung. Die Pins befinden sich auf beiden Seiten der Rückseite der Dot-Matrix. Mit Blick auf die Seite mit dem Etikett sind die Pins an diesem Ende von 1 bis 8 durchnummeriert, während die Pins auf der gegenüberliegenden Seite von 9 bis 16 nummeriert sind.

Externe Ansicht:

|img_788bs_i|

Die interne Verschaltung einer CA-Matrix unterscheidet sich von einer 
CC-Matrix hinsichtlich der Polarität: Bei einer CA-Matrix bilden die 
ROW-Pins die Anoden, während die COL-Pins als Kathoden fungieren. 
Bei einer CC-Matrix verhält es sich genau umgekehrt. Gemeinsam ist 
beiden Typen jedoch, dass die Pins 13, 3, 4, 10, 6, 11, 15 und 16 stets 
den COL zugeordnet sind, während die Pins 9, 14, 8, 12, 1, 7, 2 und 5 stets 
den ROW entsprechen.

Um beispielsweise die erste LED oben links zu aktivieren, setzen Sie bei 
einer CA-Matrix den COL-Pin 13 auf Low und den ROW-Pin 9 auf High. Bei 
einer CC-Matrix hingegen setzen Sie den COL-Pin 13 auf High und den ROW-Pin 9 
auf Low. Möchten Sie die gesamte erste Spalte beleuchten, setzen Sie bei der 
CA-Matrix den COL-Pin 13 auf Low und alle ROW-Pins (9, 14, 8, 12, 1, 7, 2 und 5) 
auf High. Bei der CC-Matrix invertiert sich entsprechend die Logik.

Innere Struktur:

|img_788bs_sche|

Pinbelegung der LED-Dot-Matrix:

=========== ====== ====== ===== ====== ===== ====== ====== ======
**COL**     **1**  **2**  **3** **4**  **5** **6**  **7**  **8**
**Pin No.** **13** **3**  **4** **10** **6** **11** **15** **16**
**ROW**     **1**  **2**  **3** **4**  **5** **6**  **7**  **8**
**Pin No.** **9**  **14** **8** **12** **1** **7**  **2**  **5**
=========== ====== ====== ===== ====== ===== ====== ====== ======

Zusätzlich werden in diesem Aufbau zwei 74HC595-Chips verwendet. 
Ein Chip steuert die Reihen (ROW), während der andere die Spalten (COL) 
der LED-Dot-Matrix ansteuert.

**Example**

* :ref:`py_74hc_788bs` (Für MicroPython-Nutzer)
* :ref:`py_bubble_level` (Für MicroPython-Nutzer)
* :ref:`ar_74hc_788bs` (Für Arduino-Nutzer)
