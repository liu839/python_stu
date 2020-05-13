from tkinter import *

master = Tk()

Label(master, text="作品：").grid(row=0)
Label(master, text="作者：").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)
#加入show="*"即可展示效果为*****
e1.grid(row=0, column=1, padx=10, pady=5)
e2.grid(row=1, column=1, padx=10, pady=5)
#加入show="*"
def show():
    print("作品：《%s》" % e1.get())
    print("作者：%s" % e2.get())
    e1.delete(0, END)
    e2.delete(0, END)

Button(master, text="获取信息", width=10, command=show).grid(row=3, column=0, sticky=W, padx=10, pady=5)
#stick表示方位
Button(master, text="退出", width=10, command=master.quit).grid(row=3, column=1, sticky=E, padx=10, pady=5)

mainloop()
