import urllib.request as u
import chardet as c
import os
os.chdir(r"C:\Users\71037\Desktop\新建文件夹")
with open(r"C:\Users\71037\Desktop\新建文本文档.txt") as f:
    url_txt=f.read().split('\n')
del url_txt[-1]
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400'}
file_name='url_'
i=0
for each in url_txt:
    ret=u.Request(each,headers=headers)
    print(ret)
    response=u.urlopen(ret).read()
    encoding=c.detect(response)['encoding']
    txt=response.decode(encoding)
    name=file_name+str(i)+'.txt'
    print("正在访问%s"%(each))
    with open(name,'w',encoding=encoding) as f:
        f.write(txt)
    i+=1
    