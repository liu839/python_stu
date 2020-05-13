from tkinter import *

root=Tk()

v=IntVar()

Radiobutton(root,text="One",variable=v,value=1).pack(anchor=W)
Radiobutton(root,text="Two",variable=v,value=2).pack(anchor=W)
Radiobutton(root,text="Three",variable=v,value=3).pack(anchor=W)
#variable共同使用V,点击某一个按钮,V的值会覆盖进value,以此得知按的按钮
#anchor=W靠左 N北....
mainloop()