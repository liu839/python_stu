from tkinter import *
import time
class PCB_type():
    def __init__(self, pid, priority, cputime):
        self.pid = pid
        self.priority = priority
        self.cputime = cputime
root = Tk()
frame = Frame(root)
frame.pack(padx = 10, pady = 10)

def create():
    create_ =Tk()
    frame_create =Frame(create_).pack(padx = 10, pady = 10)
    create_.destroy()
    return
def run():
    return
def change():
    return
def kill():
    return

Label(frame,text="进程演示系统").grid(row=0,column=2,sticky="NESW")
Button(frame, text = "创建新的进程", command=create()).grid(row=1,column=1,sticky=W)
Button(frame, text = "查看运行进程", command=run()).grid(row=1,column=3,sticky=W)
Button(frame, text = "换出某个进程", command=change()).grid(row=2,column=1,sticky=W)
Button(frame, text = "杀死运行进程").grid(row=2,column=3,sticky=W)
Button(frame, text = "推出系统", command=root.quit).grid(row=3,column=2)

mainloop()