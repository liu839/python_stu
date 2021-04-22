import tkinter
from  tkinter  import ttk
import json
provice = {}
city ={}
city_list = []
with open(r"程序记录\tk\省市.txt","rb") as f:
    data = json.load(f)
for pro in data:
    data = pro["city"]
    pro_name = pro["name"]
    city_list = []
    for ci in data:
        city_list.append(ci["name"])
        city[ci["name"]] = ci["area"]
    provice[pro_name] = city_list

province_show = []
city_show = []
def go(*args):   
    comvalue2.set("")
    comvalue3.set("")
    comboxlist3["values"]= []
    pro = comboxlist.get()
    comboxlist2["values"] = provice[pro]
def go2(*args):   
    comvalue3.set("")
    ci = comboxlist2.get()
    comboxlist3["values"] = city[ci]

def show():
    pro = comboxlist.get()
    ci = comboxlist2.get()
    co = comboxlist3.get()
    text = "你来自"+pro + ci + co
    label.set(text)
win=tkinter.Tk() #构造窗体

comvalue=tkinter.StringVar()#窗体自带的文本，新建一个值
comvalue2=tkinter.StringVar()#窗体自带的文本，新建一个值
comvalue3=tkinter.StringVar()#窗体自带的文本，新建一个值
label=tkinter.StringVar()

comboxlist=ttk.Combobox(win,textvariable=comvalue) #初始化
comboxlist2=ttk.Combobox(win,textvariable=comvalue2) #初始化
comboxlist3=ttk.Combobox(win,textvariable=comvalue3) #初始化

comboxlist["values"]=list(provice.keys())
comboxlist2["values"]=[]
comboxlist3["values"]=[]

comboxlist.current(0)  #选择第一个
comboxlist.bind("<<ComboboxSelected>>",go)  #绑定事件,(下拉列表框被选中时，绑定go()函数)
comboxlist2.bind("<<ComboboxSelected>>",go2)  #绑定事件,(下拉列表框被选中时，绑定go()函数)

comboxlist.grid(row=0,column=0)
comboxlist2.grid(row=0,column=1)
comboxlist3.grid(row=0,column=2)
tkinter.Button(win, text="获取信息", width=10, command=show).grid(row=1, column=1, padx=10, pady=5)
tkinter.Label(win, textvariable = label).grid(row=2,column=1, padx=20, pady=5)


win.mainloop() #进入消息循环
