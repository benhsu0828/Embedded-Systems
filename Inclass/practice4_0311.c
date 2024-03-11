#include <LBLE.h>
#include <LBLEPeriphral.h>
#include "DHT.h"
DHT dht1(2, DHT11);

LBLEService AService("19B10010-E8F2-537E-4F6C-D104768A1214");
LBLECharacteristicString ARead("19B10011-E8F2-537E-4F6C-D104768A1214", LBLE_READ | LBLE_WRITE);

void setup()
{
  // Initialize LED pin
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW);
  dht1.begin();
  Serial.begin(9600);
  LBLE.begin();
  while (!LBLE.ready()) { delay(100); }
  Serial.print("Device Address = [");
  Serial.print(LBLE.getDeviceAddress());
  Serial.println("]");
  
  LBLEAdvertisementData advertisement;
  advertisement.configAsConnectableDevice("D1053020");
  LBLEPeripheral.setName("D1053020");
  AService.addAttribute(ARead);
  LBLEPeripheral.addService(AService);
  LBLEPeripheral.begin();
  LBLEPeripheral.advertise(advertisement);
}

void loop()
{
  Serial.print("conected=");
  Serial.println(LBLEPeripheral.connected());
  if (ARead.isWritten()) {
    char value = ARead.getValue()[0];
//    if(value == '1'){
//      digitalWrite(LED_BUILTIN, HIGH);
//    }else if(value == '0'){
//      digitalWrite(LED_BUILTIN, LOW);
//    }else{
//      Serial.println("Unknown value written");
//    }
    switch (value) {
      case '1':
        digitalWrite(LED_BUILTIN, HIGH);
        Serial.println("ON");
        break;
      case '0':
        digitalWrite(LED_BUILTIN, LOW);
        Serial.println("OFF");
        break;
      default:
        Serial.println("Unknown value written");
        break;
    }
  }
  
  String hum, t_c, t_f;
  hum = dht1.readHumidity();
  t_c = dht1.readTemperature();
  t_f = dht1.readTemperature(true);
  String sr = "相對溼度 : " + hum + "  " + "攝氏溫度 : " + t_c + "  " + "華氏溫度 : " + t_f + "  ";
  Serial.println(sr);
  ARead.setValue(sr);

  delay(1000);
}
