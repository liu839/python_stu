from tkinter import *

root=Tk()

v=IntVar()

c=Checkbutton(root,text="text",variable=v)
c.pack()

l=Label(root,textvariable=v)
l.pack()

mainloop()