import tkinter as tk

class App():
    def __init__(self,master):
        frame=tk.Frame(master)
        frame.pack(side=tk.LEFT,padx=10,pady=10)

        self.hi_there=tk.Button(frame,text="打招呼",bg='black',fg="white",command=self.sayhi)
        self.hi_there.pack()
    
    def sayhi(self):
        print("你好")


root=tk.Tk()
app=App(root)

root.mainloop()