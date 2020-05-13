from tkinter import *

root=Tk()
photo=PhotoImage(file="C:/Users/71037/Desktop/666.gif")

thelable=Label(root,
                text="含有不被允许内容,\n别看了",
                justify=LEFT,
                #居左
                padx=10,
                #距离左边最近的有10尺寸距离
                image=photo,
                compound=CENTER,
                #图片与文字重合
                font=("楷体",20),
                fg="white",)
                #前背景色(字体颜色)
thelable.pack()
mainloop()
