import serial
COM_PORT='COM3'
BAUD_RATES=115200
ser=serial.Serial(COM_PORT,BAUD_RATES)
try:
    while True:
        while ser.in_waiting:
            msg=ser.readline().decode()
            print('Serial_msg:{}'.format(msg))
            
except KeyboardInterrupt:
    ser.close()
    print('closed!')
except OSError as er:
    ser.close()
    print(er)