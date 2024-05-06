#include <LWiFi.h>
#include "DHT.h"
#include <Ultrasonic.h>
Ultrasonic ultrasonic_2_3(4, 5);
char ssid[] = "WILLIAM 3152";    
char pass[] = "8[08U73o";   
DHT dht2(2, DHT11); 
int status = WL_IDLE_STATUS;
char server[] = "172.20.10.4"; 
WiFiClient client;
void setup() {
    Serial.begin(115200);
    pinMode(LED_BUILTIN, OUTPUT);
    digitalWrite(LED_BUILTIN,LOW);
    while (!Serial) {
        ;
    }

}
void loop() {
    while (status != WL_CONNECTED) {
        Serial.print("Attempting to connect to SSID: ");
        Serial.println(ssid);
        status = WiFi.begin(ssid, pass);
    }  
    Serial.println("Connected to wifi");
    if (client.connect(server, 80)) {
        Serial.println("connected to server (GET)");
    }
    delay(1000);
    String hum , temc , temf;
    float cm = ultrasonic_2_3.convert(ultrasonic_2_3.timing(), Ultrasonic::CM);
    hum=dht2.readHumidity();
    temc=dht2.readTemperature();
    temf=dht2.readTemperature(true);
    String str="相對溼度:"+hum+","+"攝氏溫度:"+temc+","+"華氏溫度:"+temf+"Distance:"+cm;
    Serial.println(str);
    String GET="GET /insert.php";
    String getStr = GET + "?c=" + String(temc)+
                  "&f=" + String(temf) +
                  "&h=" + String(hum) +
                  "&d=" + cm +
                  " HTTP/1.1";
    client.println(getStr);
    client.println("Host: 172.20.10.4");
    client.println("Accept: */*");
    client.println("Connection: close");
    client.println();
    delay(1000);
        
    while (client.available()) {
        char c = client.read();
//        Serial.println(c);
        if(c=='1')
        {
          digitalWrite(LED_BUILTIN,HIGH);
          delay(100);
        }
        else
        {
          digitalWrite(LED_BUILTIN,LOW);
        }
        Serial.write(c);
        }
    }
