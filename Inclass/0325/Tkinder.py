import tkinter as tk
#tk._test()

#視窗
window=tk.Tk()
window.title('test')
window.geometry('500x900')

#宣告並建立初始的文字顯示
labletext=tk.StringVar()
labletext.set('')

#宣告並建立按鈕
buttontest=tk.StringVar()
buttontest.set('print_selection')

#################list
#宣告並建立list
listtext=tk.StringVar()
#設定初始的listbox
listtext.set(('牛肉','雞肉','豬肉','羊肉','魚肉'))

#按鈕綁定函數
def print_selection(): 
    #從listbox獲得所選擇的餐點
    value=listbox.get(listbox.curselection())
    #將選擇的餐點顯示在label上
    labletext.set(value)

#文字顯示參數設定
lable=tk.Label(master=window,textvariable=labletext,\
    bg='green',font=('Aroal',12),width=15,height=2)
lable.pack()

#按鈕參數設定
button=tk.Button(master=window,textvariable=buttontest,\
        width=15,height=2,command=print_selection)
button.pack()

#宣告並建立listbox
listbox=tk.Listbox(window,listvariable=listtext)
list_items=['天使紅蝦','帝王蟹','魚翅','鮭魚卵']
for item in list_items:
    #將資料輸入listbox 方式為末端新增
    listbox.insert('end',item)
    
#對指定的list位置輸入 如該位置有值將取代原值
listbox.insert(1,'龍蝦') 
listbox.insert(2,'海膽')

#刪除指定位置的值
listbox.delete(8)
listbox.pack()

#############radiobutton
#宣告按鈕的變數
radiobuttonvar=tk.StringVar()

#按鈕綁定函數
def printRadio_selection(): 
    #獲得所選擇的值並顯示出來
    lable2.config(text='you have selected : '+ radiobuttonvar.get())

#文字顯示參數設定
lable2=tk.Label(master=window,text=' ',\
    bg='green',font=('Aroal',12),width=20,height=2)
lable2.pack()

#按鈕參數設定 value為按下按鈕時該按鈕所發出的值 可被.get接收
radiobutton=tk.Radiobutton(window,text='Option A',variable=radiobuttonvar,\
                           value='A',command=printRadio_selection)
radiobutton.pack()

radiobutton2=tk.Radiobutton(window,text='Option B',variable=radiobuttonvar,\
                            value='B',command=printRadio_selection)
radiobutton2.pack()

radiobutton3=tk.Radiobutton(window,text='Option C',variable=radiobuttonvar,\
                            value='C',command=printRadio_selection)
radiobutton3.pack()


##################Scale
#拉膽觸發時會將當前位置也傳入，因此可用變數儲存
def printScale_selection(value): 
    #將拉桿位置顯示出來
    lable3.config(text='you have selected : '+ value)
    print(scale.get())

#文字顯示參數設定
lable3=tk.Label(master=window,text=' ',\
    bg='green',font=('Aroal',12),width=20,height=2)
lable3.pack()

#設定拉桿的參數
scale=tk.Scale(window,label='try me',from_=0 ,to = 50,\
               orient='horizontal',length=200, show=True,\
              tickinterval=5,resolution=0.01,command=printScale_selection)
scale.pack()

###############Checkbutton
#建立兩個變數用來存放選擇
var=tk.IntVar()
var2=tk.IntVar()

#將不同結果判斷並顯示合理的輸出
def printCheckbutton_selection():     
    if(var.get()==True)&(var2.get()==False):
        label4.config(text='I love only BMW')
    elif (var.get()==False)&(var2.get()==True):
        label4.config(text='I love only MAZDA')
    elif (var.get()==False)&(var2.get()==False):
        label4.config(text='I do not love either')
    else:
        label4.config(text='i love both')   

#文字顯示參數設定
label4=tk.Label(master=window,text=' ',\
    bg='green',font=('Aroal',12),width=20,height=2)
label4.pack()

#按鈕的參數
checkbutton=tk.Checkbutton(master=window,text='BMW',variable=var,\
                onvalue=True,offvalue=False,command=printCheckbutton_selection)
checkbutton.pack()

checkbutton2=tk.Checkbutton(master=window,text='MAZDA',variable=var2,\
                onvalue=True,offvalue=False,command=printCheckbutton_selection)
checkbutton2.pack()

###mesageBox
def hit_me():
    tk.messagebox.showinfo(title='showinfo',message='HIHIHI')
    '''
    tk.messagebox.showwarning(title='showwarning',message='HIHIHI')
    tk.messagebox.showerror(title='showerror',message='HIHIHI')
    '''
    #ask系列都會有回傳值,根據是按下叉叉還是確認回傳True/False
    print(tk.messagebox.askquestion(title='askquestion',message='HIHIHI'))
    print(tk.messagebox.askyesno(title='askyesno',message='HIHIHI'))
    print(tk.messagebox.askretrycancel(title='askretrycancel',message='HIHIHI'))
    print(tk.messagebox.askokcancel(title='askokcancel',message='HIHIHI'))

messageBotton = tk.Button(master=window,text='hit me ',command=hit_me)
messageBotton.pack()

window.mainloop() #一定要有，會一直刷新視窗
