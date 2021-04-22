import tkinter as tk
from tkinter.simpledialog import askstring, askinteger, askfloat

# 接收一个整数
def print_integer():
    res = askinteger("Spam", "Egg count", initialvalue=12*12)
    print(res)
    
# 接收一个浮点数
def print_float():
    res = askfloat("Spam", "Egg weight\n(in tons)", minvalue=1, maxvalue=100)
    print(res)

# 接收一个字符串
def print_string():
    res = askstring("Spam", "Egg label")
    print(res)
    
    
root = tk.Tk()
    
tk.Button(root, text='取一个字符串', command=print_string).pack()
tk.Button(root, text='取一个整数', command=print_integer).pack()
tk.Button(root, text='取一个浮点数', command=print_float).pack()

root.mainloop()