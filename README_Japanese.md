Raizin:　温度測定システム
=============================

**Raspberry pi** と **Arduino**を用いた温度測定システムである。<br>
**Raspberry pi** 上の全アプリは、**Docker** 上で動作可能としている。

Description
-----------
本システムは、**Raspberry pi** と **Arduino** が連携することで、温度測定を実施する。
Arduinoを用いて、温度測定およびLED警告を実装している。
LED警告では、20度から30度の間は、緑のLED、それ以外の温度は赤のLEDが発光する。
Raspberry piによって、温度測定の結果を表示する。

Requirement
-----------
必要なものとしては、以下がある。
* Arduino
* 温度センサ (LM75B)
* 抵抗 100Ω (いわゆる、茶黒茶金)
* LED (緑と赤)
* ジャンパー線とブレッドボード
* Raspberry pi

Circuit wiring
----------

配線図は、下記。
![配線図](https://cloud.githubusercontent.com/assets/14259271/26763300/b7287e98-498b-11e7-8cd3-93667b49b096.jpg)

配線の詳細は、下記の表を参照

| Aruduino pin  | LM75B | LED (RED)       | LED (GREEN)   |
|:-------------:|:-----:|:---------------:|:-------------:|
|       5V      |  VCC  |                 |               |
|       A5      |  SCL  |                 |               |
|       A4      |  SDA  |                 |               |
|       GND     |  GND  |                 |               |
|       GND     |       |カソード（短足）　 |               |
|   DIGITAL 13  |       |アノード (長足)   |               |
|       GND     |       |                 |カソード (短足) |
|   DIGITAL 12  |       |                 |アノード (長足) |      

Install
------------

### Arduinoの設定 (windows)

1. Aruduino IDEをダウンロード

下記のリンク先よりダウンロード

[https://www.arduino.cc/en/Main/Software](https://www.arduino.cc/en/Main/Software)

2. スケッチ、検証、書き込み

ソースコードは、以下
```
#include<Wire.h>
#define LM75B_address 0x48
#define temp_reg 0x00
#define REDLED 13
#define GREENLED 12

void setup() {
  // put your setup code here, to run once:
  Wire.begin();
  Serial.begin(9600);

  //  temp sensor setup
  Wire.beginTransmission(LM75B_address);
  Wire.write(temp_reg);
  Wire.endTransmission();

  // Led
  pinMode(REDLED,OUTPUT);
  pinMode(GREENLED,OUTPUT);
}

void judge(double temp){
  // judge temp < 30 or temp >=30
  if (temp >= 20 && temp <= 30){
    digitalWrite(REDLED,LOW);
    digitalWrite(GREENLED,HIGH);
  }else {
     digitalWrite(GREENLED,LOW);
     digitalWrite(REDLED,HIGH);
    }
}

void loop() {
  // put your main code here, to run repeatedly:
  signed int temp_data=0;
  double temp = 0.0;
  Wire.requestFrom(LM75B_address,2);
  while(Wire.available()){
    temp_data |= (Wire.read()<<8);
    temp_data |= Wire.read();
  }

  temp = (temp_data>>5)*0.125;
  Serial.println(temp);
  judge(temp);
  delay(3000);
}
```

### Raspberry piの設定

以下のコマンドを実行
```
# git clone
git clone https://github.com/nicuo/Sensor_app.git

# Docker インストール
sudo apt-get update
sudo apt-get install docker.io
sudo ln -sf /usr/bin/docker.io /usr/local/bin/docker

# Docker file 実行
cd Sensor_app/
sudo docker build -t nicuo/sensor .
sudo docker run -ti --privileged nicuo/sensor
```

Author
------------
nicuo

バージョン管理
-------------

### ver 1.1
* Aruduino <br>
Aruduinoに関しては、修正なし
* Raspberry Pi　<br>
Raspberry pi に関しては、Docker fileの追加によって、コンテナ上で動作するように変更した

### ver 1.0
* Aruduino <br>
Aruduinoに関しては、完成した。
* Raspberry Pi　<br>
Raspberry pi に関しては、シリアル通信により、Arduinoの温度の計測の取得及び計測温度の画面表示には、成功した
