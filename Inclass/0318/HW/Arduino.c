#include "DHT.h"
#include<Servo.h>
Servo myservo;
DHT dht1(2, DHT11);

String Str01="";

void setup()
{
  // Initialize LED pin
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW);
  dht1.begin();
  Serial.begin(115200);
  Serial.println("Ready");
  //伺服馬達
  myservo.attach(3);


}

void loop()
{
  if(Serial.available()){
    Str01="";
    delay(1);
    while(Serial.available()){
      Str01+=(char)Serial.read();
    }
    Serial.println(Str01);
  }

  if(Str01[0]=='a'){
    digitalWrite(LED_BUILTIN,HIGH);
    delay(500);
    digitalWrite(LED_BUILTIN,LOW);
    delay(500);
  }

  if(Str01[0]=='b'){
    digitalWrite(LED_BUILTIN,LOW);
  }
  
  if(Str01[0]=='c'){
    String hum,t_c;
    hum = dht1.readHumidity();
    t_c = dht1.readTemperature();
    String text = hum + "% " + t_c + "C ";
    Serial.println(text);
  }

  if(Str01[0]=='d'){
    for(int i=0;i<180;i++){
       myservo.write(i);//將角度寫入馬達
       delay(20);
    }
    for(int i=180;i>0;i--){
       myservo.write(i);//將角度寫入馬達
       delay(20);
    }
  }
}
