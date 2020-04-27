from tkinter import *

root=Tk()
textlable=Label(root,text="含有不被允许内容",justify=LEFT,padx=10)
textlable.pack(side=LEFT)

photo=PhotoImage(file="C:/Users/71037/Desktop/666.gif")
imglable=Label(root,image=photo)
imglable.pack(side=RIGHT)

mainloop()
