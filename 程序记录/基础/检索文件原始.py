import os
temp_dir='C:\\Users\\71037\\Desktop\\计算机'
temp_name='登录.txt'
os.chdir(temp_dir)
list1=os.listdir()
list2=[]#待处理文件夹
def search(list1,temp_dir):
    global temp_name
    for each in list1:
        if each==temp_name:
            print("%s\\%s"%(temp_dir,each))
            break
        if os.path.isdir(each):
            temp_dir2=temp_dir+'\\'+each
            os.chdir(temp_dir2)
            list1=os.listdir()
            search(list1,temp_dir2)
            os.chdir(temp_dir)
search(list1,temp_dir)