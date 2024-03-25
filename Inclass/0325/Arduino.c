#include "DHT.h"
#include<Servo.h>
Servo myservo;
DHT dht1(2, DHT11);

String Str01="";
int flag = 0;

void setup()
{
  // Initialize LED pin
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW);
  dht1.begin();
  Serial.begin(115200);
  Serial.println("Ready");
}

void loop()
{
  if(Serial.available()){
    Str01="";
    delay(1);
    while(Serial.available()){
      Str01+=(char)Serial.read();
    }
    //Serial.println(Str01);
    flag = 1;
  }

  if(flag == 1){
    String hum,t_c,t_f;
    hum = dht1.readHumidity();
    t_c = dht1.readTemperature();
    t_f = dht1.readTemperature(true);
    String text = "相對溼度 : " + hum + "," + "攝氏溫度 : " + t_c +  " , " + "華氏溫度 : " + t_f + ",";
    Serial.println(text);
  }
  if(Str01[0] == 'a'){
    digitalWrite(LED_BUILTIN,HIGH);
    delay(500);
    digitalWrite(LED_BUILTIN,LOW);
    delay(500);
  }
  if(Str01[0] == 'b'){
    digitalWrite(LED_BUILTIN,LOW);
  }
    

}
