import tkinter as tk
from PIL import Image,ImageTk
#視窗
window=tk.Tk()
window.title('test')
window.geometry('600x600')
'''
#定義移動的方式
def move_it():  
   canvas.move(rect,5,5)
   
#建立畫布
canvas=tk.Canvas(master=window,bg='blue',height=400,width=400)

#讀取並顯示圖檔
image_file=tk.PhotoImage(file='cat.gif')
image=canvas.create_image(0,0,anchor='nw',image=image_file)


#設定參數並作圖
x0,y0,x1,y1=300,300,380,380
line=canvas.create_line(x0,y0,x1,y1) #畫線
oval=canvas.create_oval(x0,y0,x1,y1,fill='red')#畫圓
arc=canvas.create_arc(x0+100,y0+100,x1+100,y1+100,start=0,extent=180)#扇形
rect=canvas.create_rectangle(200,30,200+20,30+20)#矩形
canvas.pack()

#建立按鈕來觸發畫布的移動
button=tk.Button(window,text='move',command=move_it).pack()#建立並包裝的用法
'''
   
#建立畫布
canvas=tk.Canvas(master=window,height=400,width=400)

#讀取並顯示圖檔
image_file=Image.open('pic.jpg')
image_file2=ImageTk.PhotoImage(image_file)
imag=canvas.create_image(0,0,anchor='nw',image=image_file2)

#畫布完成包裝
canvas.pack()

window.mainloop() #一定要有，會一直刷新視窗