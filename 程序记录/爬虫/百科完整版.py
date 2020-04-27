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
name_judge=re.compile('title="(.*?)"')      #对近义词的正则
name_judge_1=re.compile('>(.{1,10})</a>')    #对蓝词(索引词的)的正则
title_judge=re.compile('>(.*)</h2>')
chinese_judge=re.compile(r'[\u4e00-\u9fa5]|[\，\。]')
#判断名称和网页的正则表达式
#存储最终数据   name->url的形式
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400'}
#模拟浏览器访问
def url_born():
    global url_low
    global url_high
    string=input('输入要搜索的词条(输入end结束):')
    if string=='end':
        return True

    a=string.encode('utf-8')
    a=str(a)
    string=a[2:-1].replace(r'\x','%').upper()
    url_high=url_low+'/item/'+string
    return False

def output(a,b):
    #输出模块
    global url_low
    #判断解释词是否在文章内
    i=0
    a=iter(a)
    b=iter(b)
    while True:
        i+=1
        if i%10==0:
            temp=input("请问是否需要继续Y/N: ")
            if temp=='N' or temp=='n':
                print("结束",end='\n\n')
                break
        try:
            print(next(a),end='->')
            print(url_low+next(b),end='\n')
        except StopIteration:
            if i==1:
                print("没有近义词")
            print("结束",end='\n\n')
            return
        time.sleep(0.3)

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
    #以soup类型准备

    data=str(soup.find_all(class_='lemmaWgt-lemmaTitle-title'))
    print("副标题:",end='')
    try:
        print(title_judge.findall(data)[0])
    except IndexError:
        print("空")
    #打出副标题

    data=soup.find_all(class_='lemma-summary')
    data_expain=data[0].text
    print(data_expain)
    #打出直接解释

    soup = BeautifulSoup(html, 'html.parser')
    data=str(soup.find_all(class_='lemma-summary'))
    #使用BeautifulSoup(html, 'html.parser')将HTML转换成BeautifulSoup类型进行处理数据
    #打出注解
    data_url=url_judge.findall(data)
    data_name=name_judge_1.findall(data)
    for i in range(len(data_name)):
        try:
            if data_name[i] not in data_expain:
                del data_name[i]
                i-=1
        except IndexError:
            break
    output(data_name,data_url)
    #先提前处理数据名称内部是否有异常词汇

    data=str(soup.find_all(class_='polysemantList-wrapper cmn-clearfix'))
    data_name=name_judge.findall(data)
    data_url=url_judge.findall(data)
    output(data_name,data_url)
    #打出近义词

