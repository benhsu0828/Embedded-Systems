#include "DHT.h"
#include<Servo.h>
#include <Ultrasonic.h>
Servo myservo;
DHT dht1(2, DHT11);
String Str01="c";
Ultrasonic ultrasonic_2_3(2, 3);  

void setup()
{
  dht1.begin();
  Serial.begin(115200);
  //Serial.println("Ready");
  //伺服馬達
  myservo.attach(14);
  //pinMode(14,INPUT);

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
  
  if(distance>50){
    myservo.write(100);
  }else{
    myservo.write(0);
  }
  Str01[0] = 'c';
}
