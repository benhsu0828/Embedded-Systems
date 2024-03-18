from time import sleep
import serial
import tkinter

ser=serial.Serial("COM7", 115200,timeout=2)
data=""
condition=False

def SerialWrite(command):
    ser.write(command)
    rv=ser.readline()
    
    print(rv.decode("utf-8"))
    data=rv.decode("utf-8")
    print(data)
    sleep(1)
    ser.flushInput()

def SendCmdA():
    Ardiuno_cmd='a'
    cmd=Ardiuno_cmd.encode("utf-8")
    SerialWrite(cmd)
    condition=False
    
    LabelA.config(text="Send the command 'a' to Ardiuno")
    LabelA.update_idletasks()
    Tkwindow.update()

def SendCmdB():
    Ardiuno_cmd='b'
    cmd=Ardiuno_cmd.encode("utf-8")
    SerialWrite(cmd)
    condition=False
    
    LabelA.config(text="Send the command 'b' to Ardiuno")
    LabelA.update_idletasks()
    Tkwindow.update()

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
        
def SendCmdD():
    Ardiuno_cmd='d'
    cmd=Ardiuno_cmd.encode("utf-8")
    SerialWrite(cmd)
    condition=False
    
    LabelA.config(text="Send the command 'd' to Ardiuno")
    LabelA.update_idletasks()
    Tkwindow.update()

def Serial_Connect():
    print("Connecting to Ardiuno.....")
    
    LabelA.config(text="Connecting to Ardiuno.....")
    LabelA.update_idletasks()
    Tkwindow.update()
    sleep(1)
    for i in range(1,10):
        rv=ser.readline()
        print("Loading....")
        
        LabelA.config(text="Loading....")
        LabelA.update_idletasks()
        Tkwindow.update()
        
        print(rv.decode("utf-8"))
        ser.flushInput()
        sleep(1)
        Str_Message=rv.decode("utf-8")
        
        if Str_Message[0:5]=='Ready':
            print("Get Ardiuno Ready!")
            LabelA.config(text="Get Ardiuno Ready!")
            buttonStart.config(state="disabled")
            LabelA.update_idletasks()
            Tkwindow.update()
            break
        
def Exit():
    print("Exit...")
    
    LabelA.config(text="Exit...")
    LabelA.update_idletasks()
    Tkwindow.update()
    sleep(1)
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
buttonA=tkinter.Button(Tkwindow,anchor=tkinter.S,text="LED ON",width=10,height=1,command=SendCmdA)
buttonA.pack(side=tkinter.LEFT)
buttonB=tkinter.Button(Tkwindow,anchor=tkinter.S,text="LED OFF",width=10,height=1,command=SendCmdB)
buttonB.pack(side=tkinter.LEFT)
buttonC=tkinter.Button(Tkwindow,anchor=tkinter.S,text="SHOW DHT",width=10,height=1,command=SendCmdC)
buttonC.pack(side=tkinter.LEFT)
buttonD=tkinter.Button(Tkwindow,anchor=tkinter.S,text="伺服馬達",width=10,height=1,command=SendCmdD)
buttonD.pack(side=tkinter.LEFT)
buttonStart=tkinter.Button(Tkwindow,anchor=tkinter.S,text="Connect",width=10,height=1,command=Serial_Connect)
buttonStart.pack(side=tkinter.RIGHT)
buttonEnd=tkinter.Button(Tkwindow,anchor=tkinter.S,text="Exit",width=10,height=1,command=Exit)
buttonEnd.pack(side=tkinter.RIGHT)
Tkwindow.mainloop()
