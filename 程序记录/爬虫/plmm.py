import urllib.request
import chardet
from bs4 import BeautifulSoup
import easygui as eg
import time
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400'}
url_low='http://jandan.net/ooxx'
jpg_count=0
def jpg_download(url):
    #图片下载区域
    global jpg_count
    global headers
    global div_name
    if 'gif'in url:
        return
    req=urllib.request.Request(url,headers=headers)
    response=urllib.request.urlopen(req)
    img=response.read()
    file_name=div_name+'\\'+str(jpg_count)+'.jpg'
    with open(file_name,'wb') as f:
        f.write(img)
    jpg_count+=1
def url_next(url):
    global headers
    url_judge=re.compile(r'href="(.*)"')
    req=urllib.request.Request(url,headers=headers)
    response=urllib.request.urlopen(req)

    html=response.read().decode('utf-8')
    #正常处理成html文件
    soup=BeautifulSoup(html, 'html.parser')
    target=soup.find_all(class_='cp-pagenavi')
    temp=url_judge.findall(str(target[0].a))[0]
    url_temp='http:'+temp

    return url_temp

if __name__=="__main__":
    end=0
    eg.msgbox(msg='来,咱来点好康的')
    eg.msgbox(msg='先选下保存的位置')
    div_name=eg.diropenbox(msg='请选择保存的文件夹')
    eg.msgbox(msg='请按确定后稍等一哈,然后打开刚刚的文件夹(根据网速为准,一般3-5秒)')
    while True:
        jpg_judge=re.compile(r'src="(.*)"')
        req=urllib.request.Request(url_low,headers=headers)
        response=urllib.request.urlopen(req)
        html=response.read().decode('utf-8')
        #正常处理成html文件
        soup=BeautifulSoup(html, 'html.parser')
        target=soup.find_all(class_='text')
        for each in target:
            temp=jpg_judge.findall(str(each.p.img))
            url_temp='http:'+temp[0]
            jpg_download(url_temp)
            if jpg_count%21==0:
                choices=eg.buttonbox(msg="再来点?",choices=('来点', '不了不了'))
                if choices=='不了不了':
                    end=1
        if end==1:
            break
        url_low=url_next(url_low)
    eg.msgbox(msg='溜了溜了')

    
