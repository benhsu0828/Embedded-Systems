import time
import serial
import tkinter 
import re

ser=serial.Serial("COM7", 115200,timeout=2)
data=""
condition=False

var=tkinter.IntVar()
var2=tkinter.IntVar()
var3=tkinter.IntVar()

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

def print_selection():     
    if(var.get()==True)&(var2.get()==False)&(var3.get()==False):
        LabelA.config(text='相對溫度'+msg[1])
    elif (var.get()==False)&(var2.get()==True)&(var3.get()==False):
        LabelA.config(text='攝氏溫度'+msg[3])
    elif (var.get()==False)&(var2.get()==False)&(var3.get()==True):
        LabelA.config(text='華氏溫度'+msg[5])
    else:
        LabelA.config(text='error')
        
def print_selection2(value): 
    #將拉桿位置顯示出來
    if int(msg_data[1]) > scale.get():
        Ardiuno_cmd='a'
        cmd=Ardiuno_cmd.encode("utf-8")
        SerialWrite(cmd)
        condition=False
        
        LabelA.config(text="Send the command 'a' to Ardiuno")
        LabelA.update_idletasks()
        Tkwindow.update()
        
def SerialWrite(command):
    ser.write(command)
    rv=ser.readline()
    
    print(rv.decode("utf-8"))
    data=rv.decode("utf-8")
    print(data)
    time.sleep(1)
    ser.flushInput()

def Serial_Connect():
    print("Connecting to Ardiuno.....")
    
    LabelA.config(text="Connecting to Ardiuno.....")
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
        
        if Str_Message[0:5]=='Ready':
            print("Get Ardiuno Ready!")
            LabelA.config(text="Get Ardiuno Ready!")
            buttonStart.config(state="disabled")
            LabelA.update_idletasks()
            Tkwindow.update()
            break
        
def Exit():
    Isexit = tkinter.messagebox.askokcancel(title='askquestion',message='是否要退出')
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
Tkwindow.title("Python with ardiuno")
Tkwindow.minsize(600,400)
LabelA=tkinter.Label(Tkwindow,bg='white',fg='black',text="Press 'connect' button to start",width=30,height=10,justify=tkinter.LEFT)
LabelA.pack(side=tkinter.TOP)
buttonStart=tkinter.Button(Tkwindow,anchor=tkinter.S,text="Connect",width=10,height=1,command=Serial_Connect)
buttonStart.pack(side=tkinter.RIGHT)
buttonEnd=tkinter.Button(Tkwindow,anchor=tkinter.S,text="Exit",width=10,height=1,command=Exit)
buttonEnd.pack(side=tkinter.RIGHT)

checkbutton=tkinter.Checkbutton(Tkwindow,text='相對溼度',variable=var,\
                onvalue=True,offvalue=False,command=print_selection)
checkbutton.pack()

checkbutton2=tkinter.Checkbutton(Tkwindow,text='攝氏溫度',variable=var2,\
                onvalue=True,offvalue=False,command=print_selection)
checkbutton2.pack()
checkbutton3=tkinter.Checkbutton(Tkwindow,text='華氏溫度',variable=var3,\
                onvalue=True,offvalue=False,command=print_selection)
checkbutton3.pack()

scale=tkinter.Scale(Tkwindow,label='try me',from_=5 ,to = 11,\
               orient='horizontal',length=200, show=True,\
              tickinterval=3,resolution=0.01,command=print_selection2)
scale.pack()
Tkwindow.mainloop()