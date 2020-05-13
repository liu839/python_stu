from tkinter import *

root=Tk()


langs=[
    ("Python",1),
    ("Perl",2),
    ("Ruby",3),
    ("Lua",4)]
v=IntVar()
v.set(1)
#默认值为1即直接设置默认选python

for lang,num in langs:
    b=Radiobutton(root,text=lang,variable=v,value=num,indicatoron=False)
    b.pack(anchor=W,padx=10,pady=10,fill=X)

mainloop()