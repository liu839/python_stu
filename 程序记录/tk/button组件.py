from tkinter import *

def callback():
    var.set("吹吧你,我才不信")
root=Tk()
Frame1=Frame(root)
Frame2=Frame(root)

var=StringVar()
var.set("含有不被允许内容")
textlable=Label(Frame1,
                textvariable=var,
                justify=LEFT,
                padx=10)
textlable.pack(side=RIGHT)

thebutton=Button(Frame2,text="我已满十八周岁",command=callback)
thebutton.pack()

Frame1.pack(pady=10,padx=10)
Frame2.pack(pady=10,padx=10)
mainloop()
