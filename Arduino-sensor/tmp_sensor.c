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
