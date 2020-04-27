import urllib.parse
import urllib.request
import json
import easygui as eg

a=eg.multpasswordbox(msg="请输入豆瓣账号和密码",title='登录',fields=("用户名","密码"))
data={}
data['ck']=''
data['name']= a[0]
data['password']= a[1]  
data['remember']='false'
data['ticket']= ''
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400'}

url=r'https://accounts.douban.com/j/mobile/login/basic'     #输入网址
data=urllib.parse.urlencode(data).encode("utf-8")           #准备data数据包用urllib.parse转换格式并转码成UTF-8
urq=urllib.request.Request(url,headers=headers,data=data)   #准备提交数据,导入网站,访问模式,数据包
response=urllib.request.urlopen(urq)                        #提交数据并返回数据到response,此时为HTML内容
html=response.read().decode("utf-8")                        #读取数据包转码成UTF-8
arget=json.loads(html)                                      #因为收到的包为json数据,用json库转换出来
msg=(arget['description'])
eg.msgbox(msg=msg)                                  
