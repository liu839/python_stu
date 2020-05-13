from tkinter import *

def callback():
    var.set("吹吧你,我才不信")
root=Tk()
Frame1=Frame(root)
Frame2=Frame(root)

var=StringVar()
#tkinter的变量字符串,可由StribgVar()实列化
var.set("含有不被允许内容")
textlable=Label(Frame1,
                textvariable=var,
                #这里没使用text=,这个只能显示一个字符串
                #变成textvariable后就变成一个tkinter的变量
                justify=LEFT,
                #左对齐
                padx=10)
textlable.pack(side=LEFT)
#本部分靠左
photo=PhotoImage(file="C:/Users/71037/Desktop/666.gif")
imglable=Label(Frame1,image=photo)
imglable.pack(side=RIGHT)
#本部分靠右

thebutton=Button(Frame2,text="我已满十八周岁",command=callback)
#command必须由函数实现
thebutton.pack()

Frame1.pack(pady=10,padx=10)
Frame2.pack(pady=10,padx=10)
mainloop()
