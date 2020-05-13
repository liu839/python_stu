"""
@Author : 柳家望
@Date   : 20-5-1
@Gitee  : gitee.com/liu839
@version: 1.0
"""
import urllib.request
import urllib.parse
import json
from tkinter import *



master=Tk()
master.title("翻译")
v1 = StringVar()
v2 = StringVar()

frame=Frame(master)
frame.pack(padx=10,pady=10)

Label(frame,text="填写内容,点击翻译即可得到结果").grid(row=0,column=0)
e1=Entry(frame,width=100,textvariable=v1).grid(row=1,column=0)
Label(frame,text="↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓").grid(row=2,column=0)
e2=Entry(frame,width=100,textvariable=v2,state="readonly").grid(row=3,column=0)
#Message(frame,textvariable=v2,width=50,justify=LEFT).grid(row=0,column=2)

def fanyi():
    #headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400'}
    content=v1.get()
    data={}
    data['i']= content
    data['from']= 'AUTO'
    data['to']= 'AUTO'
    data['smartresult']= 'dict'
    data['client']= 'fanyideskweb'
    data['salt']= '15855766270856'
    data['sign']= '8e9361ec253c592a3a488f7b66d1a5a7'
    data['ts']= '1585576627085'
    data['bv']= 'ec579abcd509567b8d56407a80835950'
    data['doctype']= 'json'
    data['version']= '2.1'
    data['keyfrom']: 'fanyi.web'
    data['action']: 'FY_BY_CLICKBUTTION'
    data=urllib.parse.urlencode(data).encode('utf-8')

    url=r"http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

    req=urllib.request.Request(url,data)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400')

    response=urllib.request.urlopen(req)
    html=response.read().decode('utf-8')
    target=json.loads(html)
    v2.set(target['translateResult'][0][0]['tgt'])
    #msg="翻译结果是%s"%(target['translateResult'][0][0]['tgt'])
    #v2.set(msg)

Button(frame,text="翻译",command=fanyi,width=10).grid(row=4,column=0,pady=5,sticky=W)
Button(frame,text="退出",command=master.quit,width=10).grid(row=4,column=0,pady=5,sticky=E)
mainloop()