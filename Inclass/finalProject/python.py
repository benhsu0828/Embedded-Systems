import time
import serial
import tkinter
import pymysql
import re

ser=serial.Serial("COM7", 115200,timeout=2)
data=""
condition=False
C = ''
F = ''
H = ''

host= '192.168.56.1'

flag = True
#db = pymysql.connect(host=host,user="nima",password="123",database="test")
 
def print_selection():     
    if(var.get()==True)&(var2.get()==False)&(var3.get()==False):
        LabelA.config(text='相對溫度'+msg_data[1])
    elif (var.get()==False)&(var2.get()==True)&(var3.get()==False):
        LabelA.config(text='攝氏溫度'+msg_data[3])
    elif (var.get()==False)&(var2.get()==False)&(var3.get()==True):
        LabelA.config(text='華氏溫度'+msg_data[5])
    else:
        LabelA.config(text='error')
        
def setFlag(value):
    global flag 
    flag = True
    
def print_selection2(value): 
    global flag
    try:
        db = pymysql.connect(host=host,user="nima",password="123",database="test")
        cursor1=db.cursor()
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
                    elif("距離"in str(msg_data[0])):
                            #將拉桿位置顯示出來
                            if float(msg_data[2]) < 10:
                                tkinter.messagebox.showwarning(title='距離',message='距離過近')
                            elif float(msg_data[2]) == 0:
                                if flag:
                                    tkinter.messagebox.showerror(title='距離',message='危險')
                                    distance = msg_data[2].replace(r"\r\n", '')
                                    cursor1.execute('Insert into `dht`(`distance`) values(%s)' %(distance))
                                    db.commit()
                                    flag = False
                                    LabelA.config(text="Send to database")
                                    LabelA.update_idletasks()
                                    print("上傳完成")
                                
                                Tkwindow.update()
                                
                               
                            else: 
                                Ardiuno_cmd='b'
                                cmd=Ardiuno_cmd.encode("utf-8")
                                SerialWrite(cmd)
                                condition=False
                    else:
                        continue
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
    db.close()
    Tkwindow.after(10000,print_selection2(1))
    
def SerialWrite(command):
    ser.write(command)
    rv=ser.readline()
    
    print(rv.decode("utf-8"))
    data=rv.decode("utf-8")
    print(data)
    time.sleep(1)
    ser.flushInput()


def SendCmdC():
    Ardiuno_cmd='c'
    cmd=Ardiuno_cmd.encode("utf-8")
    SerialWrite(cmd)
    condition=True
    while(condition):
        rv1=ser.readline()
        data=rv1.decode("utf-8")
        print(data)
        LabelA.config(text=data)
        LabelA.update_idletasks()
        Tkwindow.update()
        if(condition==False):
            break
        
def Send_turnOff():
    Ardiuno_cmd='turnOff'
    cmd=Ardiuno_cmd.encode("utf-8")
    SerialWrite(cmd)
    condition=False
    
    LabelA.config(text="Send the command 'turnOff' to Ardiuno")
    LabelA.update_idletasks()
    Tkwindow.update()

def Serial_Connect():
    print("Connecting to Ardiuno.....")
    
    LabelA.config(text="No detect key")
    LabelA.update_idletasks()
    Tkwindow.update()
    time.sleep(1)
    for i in range(1,10):
        rv=ser.readline()
        print("Loading....")
        
        LabelA.config(text="Loading....")
        LabelA.update_idletasks()
        Tkwindow.update()
        
        print(rv.decode("utf-8"))
        ser.flushInput()
        time.sleep(1)
        Str_Message=rv.decode("utf-8")
        
        if Str_Message[0:6]=='Unlock':
            print("Unlock the car.")
            LabelA.config(text="Unlock the car.") 
            buttonStart.config(state="disabled")
            LabelA.update_idletasks()
            Tkwindow.update()
            break
        
def Exit():
    Isexit = tkinter.messagebox.askokcancel(title='askquestion',message='是否要熄火?')
    if Isexit:
        print("Exit...")
        LabelA.config(text="Exit...")
        LabelA.update_idletasks()
        Tkwindow.update()
        time.sleep(1)
        chr_num=27
        cmd=(chr(chr_num).encode('utf-8'))
        SerialWrite(cmd)
        ser.close()
        Tkwindow.destroy()
    

    
Tkwindow=tkinter.Tk()
Tkwindow.title("車輛儀表板")
Tkwindow.minsize(600,400)
LabelA=tkinter.Label(Tkwindow,bg='white',fg='black',text="Press 'connect' button to start",width=30,height=10,justify=tkinter.LEFT)
LabelA.pack(side=tkinter.TOP)
buttonStart=tkinter.Button(Tkwindow,anchor=tkinter.S,text="發動",width=10,height=1,command=Serial_Connect)
buttonStart.pack(side=tkinter.RIGHT)
buttonEnd=tkinter.Button(Tkwindow,anchor=tkinter.S,text="熄火",width=10,height=1,command=Exit)
buttonEnd.pack(side=tkinter.RIGHT)

var=tkinter.IntVar()
var2=tkinter.IntVar()
var3=tkinter.IntVar()

msg=ser.readline().decode()
print('serial_msg: ',msg)
msg_data=re.split(',|:',msg)
time.sleep(1)

# scale=tkinter.Scale(Tkwindow,label='華氏警示溫度',from_=50 ,to = 100,\
#                orient='horizontal',length=200, show=True,\
#               tickinterval=3,resolution=0.01,command=setFlag)
# scale.pack()    

Tkwindow.after(10000,print_selection2(1))

Tkwindow.mainloop()
