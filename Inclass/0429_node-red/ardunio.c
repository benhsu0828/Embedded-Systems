#include "DHT.h"
#include<Servo.h>
#include <Ultrasonic.h>
Servo myservo;
DHT dht1(2, DHT11);
String Str01="c";
Ultrasonic ultrasonic_2_3(4, 5);  

void setup()
{
  dht1.begin();
  Serial.begin(115200);
}

void loop()
{
  float distance = ultrasonic_2_3.convert(ultrasonic_2_3.timing(), Ultrasonic::CM);
  if(Serial.available()){
    delay(1);
    while(Serial.available()){
      Str01=(char)Serial.read();
    }
    //Serial.println(Str01);
  }

  String hum,t_c,t_f;
  hum = dht1.readHumidity();
  t_c = dht1.readTemperature();
  t_f = dht1.readTemperature(true);
  String text = "相對溼度 : " + hum + " ,"+ "攝氏溫度 : " + t_c +  " , " + "華氏溫度 : " + t_f + "," + distance +',';
  Serial.println(text);

  Str01[0] = 'c';
}
