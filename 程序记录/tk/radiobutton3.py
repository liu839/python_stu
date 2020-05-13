from tkinter import *

root=Tk()

group=LabelFrame(root,text="最好的脚本语言是?")
group.pack(padx=5,pady=5)

langs=[
    ("Python",1),
    ("Perl",2),
    ("Ruby",3),
    ("Lua",4)]
v=IntVar()
v.set(1)
#默认值为1即直接设置默认选python

for lang,num in langs:
    b=Radiobutton(group,text=lang,variable=v,value=num,indicatoron=False)
    b.pack(anchor=W,padx=10,pady=10,fill=X)

mainloop()