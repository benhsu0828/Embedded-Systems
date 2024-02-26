#include <Ultrasonic.h>
#include "DHT.h"
DHT dht1(2, DHT11);
int ledPin = 9;
Ultrasonic ultrasonic_2_3(4, 5);

void setup()
{
  Serial.begin(115200);
  dht1.begin();
  pinMode(14, INPUT);   
  pinMode(ledPin, OUTPUT);

}
void loop()
{
  int light = analogRead(14); 
  float temperature = dht1.readTemperature();//攝氏溫度
  float distance = ultrasonic_2_3.convert(ultrasonic_2_3.timing(), Ultrasonic::CM);
  Serial.print("亮度: ");
  Serial.println(light);
  Serial.print("溫度: ");
  Serial.println(temperature);
  Serial.print("距離: ");
  Serial.println(distance);
  if(temperature>20 && light>70 && distance<50){
    digitalWrite(ledPin, HIGH);
    delay(500);
  }else if(temperature>20 && light>70 && distance>50){
    digitalWrite(ledPin, HIGH);
    delay(1000);
  }else if(temperature<20 && light<70 && distance>50){
    digitalWrite(ledPin, LOW);
    delay(1500);
  }
  
  digitalWrite(ledPin, LOW); 
}
