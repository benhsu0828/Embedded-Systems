#include "DHT.h"
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
}
