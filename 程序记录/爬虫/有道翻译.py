import urllib.request
import urllib.parse
import json
import easygui as e
import time

while True:
    contnet=e.enterbox(msg='输入需要翻译的句子(输入"q!退出程序")')
    if contnet=='q!':
        break

    url=r"http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

    #headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400'}
    data={}
    data['i']= contnet
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

    req=urllib.request.Request(url,data)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400')

    response=urllib.request.urlopen(req)
    html=response.read().decode('utf-8')
    target=json.loads(html)
    msg="翻译结果是%s"%(target['translateResult'][0][0]['tgt'])
    e.msgbox(msg=msg)

    time.sleep(1)