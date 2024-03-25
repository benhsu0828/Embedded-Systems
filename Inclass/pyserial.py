import serial
import time
import re
COM_PORT='COM7'
BAUD_RATES=115200
ser=serial.Serial(COM_PORT,BAUD_RATES)
try:
    while True:
        while ser.in_waiting:
            try:
                msg=ser.readline().decode()
                print('serial_msg: ',msg)
                msg_data=re.split(',|:',msg)
                
                if("攝氏溫度" in str(msg_data)) and ("華氏溫度" in str(msg_data)) and ('相對溼度' in str(msg_data)):
                    print('msg_data='+str(msg_data))
                    print('msg_data[0]='+str(msg_data[1]))
                else:
                    continue
                time.sleep(1)
            except OSError as er:
                ser.close()
                print(er)
                
except KeyboardInterrupt:
    ser.close()
    print('closed!')
except OSError as er:
    ser.close()
    print(er)