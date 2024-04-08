#include "DHT.h"
#include<Servo.h>
Servo myservo;
DHT dht1(2, DHT11);
String Str01="c";

void setup()
{
  // Initialize LED pin
//  pinMode(LED_BUILTIN, OUTPUT);
//  digitalWrite(LED_BUILTIN, LOW);
  dht1.begin();
  Serial.begin(115200);
  Serial.println("Ready");
  //伺服馬達
  myservo.attach(3);


}

void loop()
{
  if(Serial.available()){
    delay(1);
    while(Serial.available()){
      Str01=(char)Serial.read();
    }
    Serial.println(Str01);
  }


  String hum,t_c,t_f;
  hum = dht1.readHumidity();
  t_c = dht1.readTemperature();
  t_f = dht1.readTemperature(true);
  String text = "相對溼度 : " + hum + "," + "攝氏溫度 : " + t_c +  " , " + "華氏溫度 : " + t_f + ",";
  Serial.println(text);


  if(Str01[0]=='d'){
    for(int i=0;i<180;i++){
       myservo.write(i);//將角度寫入馬達
       delay(1);
    }
    for(int i=180;i>0;i--){
       myservo.write(i);//將角度寫入馬達
       delay(1);
    }
  }
  Str01[0] = 'c';
}
