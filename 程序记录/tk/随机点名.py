#版本 : 1.0
#作者 : 柳家望
#时间 2020 08 01
from tkinter import *
import random
import tkinter.font as tf
import time
name={0:'还未抽取',
1:'刘奕池', 2:'丰志强', 3:'张翔轩', 4:'卢聪', 5:'邵嘉林', 6:'袁菲',
7:'张银滨', 8:'黄鑫鑫',9:'金慧敏', 10:'丁亦宁', 11:'杨仕炜', 12:'笱书洋',
13:'午晨旭', 14:'刘晓月', 15:'余言', 16:'肖浩宇', 17:'廖宇豪', 18:'熊一江',
19:'柯昊辉', 20:'李蕾茹', 21:'幸航宇', 22:'吴浩楠', 23:'邵飞龙', 24:'李攀峰',
25:'刘勇', 26:'朱安娜'
}

def callback():
    t = 0.001
    while True:
        v1.set(name[random.randint(1,26)])
        master.update()
        time.sleep(t)
        t += 0.001
        if t >= 0.12:
            break

master=Tk()
master.geometry("1000x400")
master.title("算法协会随机抽取")
v1 = StringVar()
v1.set(name[0])

ft = tf.Font(family='楷体', size=30)
ft2 = tf.Font(family='楷体', size=50)

frame=Frame(master)
frame.pack(padx=10,pady=10)

Label(frame,width=50,text="点击即可随机抽取一人",font=ft).grid(row=1,column=0)
e1=Button(frame,text="抽取",command=callback,font=ft).grid(row=3,column=0)
Label(frame,text="↓↓↓").grid(row=5,column=0)
e2=Label(frame,textvariable=v1,font=ft2).grid(row=7,column=0)
Button(frame,text="退出",command=master.quit,width=10,font=ft).grid(row=9,column=0,pady=5)

mainloop()
