import os
import codecs
import easygui as eg
i=0
list2=[]#待处理文件夹
title='检索文件'
sign=eg.enterbox(msg='请输入文件大概名称(可小不可大)',title=title)
eg.msgbox(msg='选择大概文件区域')
temp_dir=eg.diropenbox()
os.chdir(temp_dir)
list1=os.listdir()
#以下函数 检索特定语句(未使用)
def count(name):
    global i
    global sign
    #  print("检索文件%s中..."%(name))
    f=open(name,'rb')
    count=1
    for each in f:
        if sign in str(each):
            print("在文件%s中第%d行发现标识符含有标识符\n"%(name,count))
            count+=1
    f.close

def search(list1,temp_dir):
    #print("正在检索文件夹"+temp_dir)
    try:
        list1=os.listdir()
    except PermissionError:
        return
    for each in list1:
        if each[0]=='.':
            continue
        #print("正在检索文件"+each)
        if os.path.isdir(each):
            if '$' in each:
                continue
            temp_dir2=temp_dir+'/'+each
            try:
                os.chdir(temp_dir2)
            except PermissionError:
                continue
            search(list1,temp_dir2)
            os.chdir(temp_dir)

        if sign in each:
            temp8=temp_dir+'/'+each
            temp9='发现文件,位置为'+temp8
            eg.msgbox(msg=temp9,title=title)
            temp_10=eg.buttonbox(msg='是否继续',choices=("是","否"))
            if temp_10=="否":
                raise EOFError
            #print("发现文件,位置为%s\n"%(temp8))
            #count(temp8)
search(list1,temp_dir)
print("检测结束")