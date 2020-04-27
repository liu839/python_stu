import bs4
import urllib.request
import re
import time
list_jig=[]
url=r'https://movie.douban.com/top250'
def url_solve_class(url,class_data):
    #返回一个beautifulsoup.result类型的结果
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400'}
    req=urllib.request.Request(url,headers=headers)
    response=urllib.request.urlopen(req).read()
    html=response.decode('utf-8')
    soup=bs4.BeautifulSoup(html,'html.parser')
    data=soup.find_all(class_=class_data)
    return data
    #网页以class类型搜寻处理

def url_find(url=r'https://movie.douban.com/top250'):
    url_directory_find=re.compile('a href="(.{0,15});')
    number_filter_find=re.compile('filter=">([0-9]*)<')


    data=url_solve_class(url,'paginator')

    url_directory_temp=url_directory_find.findall(str(data))
    number_filter=number_filter_find.findall(str(data))

    for index in range(len(url_directory_temp)):
        url_directory_temp[index]=url+url_directory_temp[index]

    url_directory=dict(zip(url_directory_temp,url_directory_temp))
    url_directory[url]='1'
    #加入当前页面
    return url_directory

def data_collect(url):
    pic={}
    pic_name_judge=re.compile('alt="(.*)"')
    pic_name_judge_2=re.compile('(.*)" cla')
    pic_url_judge=re.compile('src="(.*)" w')
    pic_url=[]
    pic_name=[]

    url_directory=url_find(url)
    url_prepare=[]
    url_prepare=list(url_directory.keys())
    url_prepare.reverse()
    #数据准备完毕

    for _ in range(len(url_prepare)):
        url_temp=url_prepare.pop()

        data=url_solve_class(url_temp,'pic')
        pic_name=pic_name_judge.findall(str(data))
        for each in pic_name:
            pic[pic_name_judge_2.findall(each)[0]]=pic_url_judge.findall(each)[0]
        time.sleep(0.5)
    with open(r'C:\Users\71037\Desktop\豆瓣电影top250.txt','a') as f:
        for each in pic:
            f.writelines(each+'->'+pic[each]+'\n')





    
        

if __name__=="__main__":
    data_collect(url)
