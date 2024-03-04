#include <SPI.h>
#include <MFRC522.h>
#include<Servo.h>
#include <LedControlMS.h>
#define NBR_MTX 2 
String card_uid = "0211e97e";
LedControl lc=LedControl(17,16,15, NBR_MTX);
String read_id;
MFRC522 rfid(/*SS_PIN*/ 10, /*RST_PIN*/ 9);
Servo myservo;

String mfrc522_readID()
{
  String ret;
  if ( rfid.PICC_IsNewCardPresent() &&rfid.PICC_ReadCardSerial())  //
   //讀取並確認不是重複卡片
  {
    MFRC522::PICC_Type piccType = rfid.PICC_GetType(rfid.uid.sak);
    for (byte i = 0; i < rfid.uid.size; i++) {
      ret += (rfid.uid.uidByte[i] < 0x10 ? "0" : "");
      ret += String(rfid.uid.uidByte[i], HEX);
    }//轉成16進制儲存
  }
 rfid.PICC_HaltA();
  // Stop encryption on PCD
  rfid.PCD_StopCrypto1();
  return ret;//回傳已完成轉存之id
}
void opendoor(){
  myservo.write(100);
  scrollLeft('O');
  scrollLeft('P');
  scrollLeft('E');
  scrollLeft('N');
  delay(1000);
  myservo.write(10);
  scrollLeft('C');
  scrollLeft('L');
  scrollLeft('O');
  scrollLeft('S');
  scrollLeft('E');
}
void setup()
{
  myservo.attach(2);
  SPI.begin();
  rfid.PCD_Init();
  Serial.begin(115200);
  for (int i=0; i< NBR_MTX; i++){
    lc.shutdown(i,false);
    lc.setIntensity(i,5);
    lc.clearDisplay(i);
    }

}
void loop()
{
  read_id = mfrc522_readID(); //呼叫函式取得16進制id
  if (read_id != "") {
    Serial.print("偵測到 RFID: ");
    Serial.println(read_id); 
    if(read_id==card_uid){
      opendoor();
    }
  }
  lc.clearAll();
  delay(1000);
}

void scrollLeft(char ch){
  int pos =lc.getCharArrayPosition(ch);
  for (int scroll =0; scroll<6; scroll++) {
     for (int i=scroll; i<6;i++) {
        lc.setRow(0,i-scroll, alphabetBitmap[pos][i]);
    } 
    delay(300);
    lc.clearDisplay(0);
  }
}


