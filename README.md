Raizin: temperature sensing system
==================================

Our sensor system **Raizin** is temperature measurement system using **Raspberry pi** and　**Arduino**.　
All application can run on docker.

Description
-----------
The system senses and displays temperature using **Raspberry pi** with **Arduino**.   
The arduino senses temperature, and controlls LED based on temperature.  
Concretely, arduino programming language (like C) controlls sensor and LED connected aruduino.
The LED light green when range of temperature is 20-30 degrees Celsius, and red otherwise.  
In addition, Raspberry pi controlls the arduino using python, and displays temperatures.

Requirement
-----------
our system require below:
* Arduino
* Temperature sensor (LM75B)
* Resistor 100 Ω
* LED (green and red)
* Jumper wire and breadboard
* Raspberry pi

Circuit wiring
----------

Wiring diagram is below: <br>
![配線図](https://user-images.githubusercontent.com/14259271/29491991-43e64510-85a8-11e7-80f8-9475fff6b1ae.jpg)

| Aruduino pin  | LM75B | LED (RED)       | LED (GREEN)   |
|:-------------:|:-----:|:---------------:|:-------------:|
|       5V      |  VCC  |                 |               |
|       A5      |  SCL  |                 |               |
|       A4      |  SDA  |                 |               |
|       GND     |  GND  |                 |               |
|       GND     |       |Cathode（Short leg）　 |               |
|   DIGITAL 13  |       |Anode (Long leg)   |               |
|       GND     |       |                 |Cathode（Short leg）|
|   DIGITAL 12  |       |                 |Anode (Long leg)|      

Install
------------

### Arduino setting (windows)

1. Download Aruduino IDE

URL to download is below:

[https://www.arduino.cc/en/Main/Software](https://www.arduino.cc/en/Main/Software)

2. Sketch, compile, loading

code is below:

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
### Raspberry pi setting

command is below:

```
# git clone
git clone https://github.com/nicuo/Sensor_app.git

# Docker install
sudo apt-get update
sudo apt-get install docker.io
sudo ln -sf /usr/bin/docker.io /usr/local/bin/docker

# Docker file run
cd Sensor_app/Raspberry_system/
sudo docker build -t nicuo/sensor .
sudo docker run -ti --privileged nicuo/sensor
```

Author
------------
nicuo

Versioning
-------------
### ver 1.1
* Raspberry Pi　<br>
This application run on container　by adding Docker file.


### ver 1.0
* Aruduino <br>
Aruduino develop plan is closed.

* Raspberry Pi　<br>
Raspberry pi gets temperatures sensed by aruduino via serial communication, displays the temperatures. <br>
**We plan the app loaded to container. **
