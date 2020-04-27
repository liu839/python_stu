import os
temp_dir='C:\\Users\\71037\\Desktop\\计算机'
i=0
os.chdir(temp_dir)
list1=os.listdir()
list2=[]#待处理文件夹
def count(name):
    global i
    print("检索文件%s中..."%(name))
    f=open(name,'rb')
    f1=list(f)
    for _ in f1:     #_为真正的临时变量,用后就丢弃
        i+=1
    print("检索完毕已经有%d行代码"%(i))
def search(list1,temp_dir):
    for each in list1:
        if os.path.splitext(each)[-1]=='.txt':
            temp8=temp_dir+'\\'+each
            count(temp8)
        if os.path.isdir(each):
            temp_dir2=temp_dir+'\\'+each
            os.chdir(temp_dir2)
            list1=os.listdir()
            search(list1,temp_dir2)
            os.chdir(temp_dir)
search(list1,temp_dir)
print("检测结束")