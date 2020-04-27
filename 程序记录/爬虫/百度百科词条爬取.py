#coding=utf-8
import urllib.request
import chardet
from bs4 import BeautifulSoup
import easygui as eg
import time
import re

url_low=r"https://baike.baidu.com"
url_high=''
#基层地址和高层地址
url_judge=re.compile('href="(.*?)"')
name_judge=re.compile('>(.{1,5})</a>')
data_totle=[]
#判断名称和网页的正则表达式
#存储最终数据   name->url的形式
def url_born():
    global url_low
    global url_high
    string=eg.enterbox(msg='输入要搜索的词条(输入end结束)',title='搜索')
    if string=='end':
        return True

    a=string.encode('utf-8')
    a=str(a)
    string=a[2:-1].replace(r'\x','%').upper()
    url_high=url_low+'/item/'+string
    return False
url_high=r'https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400'}
#模拟浏览器访问    
while True:
    if url_born():
        break

    req=urllib.request.Request(url_high,headers=headers)
    response=urllib.request.urlopen(req).read()
    #收集数据

    encoding=chardet.detect(response)['encoding']                
    html=response.decode(encoding)
    #先使用chardet.detect确定大概的编码,再转码成HTML

    soup = BeautifulSoup(html, 'html.parser')
    data=str(soup.find_all(class_='lemma-summary'))
    #data=data.split(',')
    #使用BeautifulSoup(html, 'html.parser')将HTML转换成BeautifulSoup类型进行处理数据
    
    data_url=url_judge.findall(data)
    data_name=name_judge.findall(data)
    for index in range(len(data_name)):
        data_totle.append(data_name[index]+' -> '+url_low+data_url[index])
        print(data_totle[index])
    #eg.textbox(msg="相关名称->",title='百科相关',text=data_totle)
    #实际内容处理完毕

    