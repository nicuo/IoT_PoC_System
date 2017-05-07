Raspberry pi × Arduino
===========

**Raspberry pi** と　**Arduino**　を用いた温度測定システムである。

Description
-----------
本システムは、**Raspberry pi** と **Arduino** と連携することで、温度測定を実施する。
Sensor&LEDの温度測定をArduinoで実施している。
Aruduinoの制御には、C言語を用いており、温度センサによる温度計測及び20度から30度の間は、緑のLED、それ以外の温度は赤のLEDが発光するように、記述している。
また、全体のシステム制御をRaspberry piで実施しており、使用言語は、Pythonである。

Requirement
-----------
必要なものとしては、以下がある。
* Arduino
* 温度センサ (LM75B)
* LED (緑と赤)
* ジャンパー線とブレッドボード
* Raspberry pi

Author
------------
nicuo

バージョン管理
-------------
### ver 1.0
* Aruduino <br>
Aruduinoに関しては、完成した。

* Raspberry Pi　<br>
Raspberry pi に関しては、シリアル通信により、Arduinoの温度の計測の取得及び計測温度の画面表示には、成功した
