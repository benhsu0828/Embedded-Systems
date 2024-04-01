import sys
import pymysql
import serial
import time
import re 

COM_PORT = 'COM7'
BAUD_RATES = 115200
ser = serial.Serial(COM_PORT,BAUD_RATES,timeout=2)
C = ''
F = ''
H = ''

host= '192.168.56.1'
try:
    db = pymysql.connect(host=host,user="william",\
                         password="123456",database="test")
    cursor1=db.cursor()
    while True:
        while ser.in_waiting:
            try:
                msg = ser.readline().decode()
                if(msg==''):
                    continue
                else:
                    print('msg format ={}'.format(msg))
                    msg_data=re.split(',|:',msg)
                    if len(msg_data) < 5:
                        continue
                    elif("攝氏溫度"in str(msg_data[2])) and ("華氏溫度"in str(msg_data[4]))\
                        and ("相對溼度" in str(msg_data[0])):
                            H = msg_data[1]
                            C = msg_data[3]
                            F = msg_data[5].replace(r"\r\n", '')
                            cursor1.execute('Insert into `dht`(`C`,`F`,`H`)\
                                       values(%s,%s,%s)' %(C,H,F))
                            db.commit()
                    else:
                        continue
                    print("上傳完成")
            except OSError as er:
                db.rollback()
                db.close()
                print(er)
except OSError as er:
    db.rollback()
    db.close()
    print(er)
except KeyboardInterrupt:
    ser.close()
    db.close()
    print("closed!")
