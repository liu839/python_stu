import os

os.chdir(r'C:\Users\71037\Desktop\临时')
list1=os.listdir()
list2=['dir']#存储文件后缀
dict1={}#存储文件后缀及对应数量
dict1['dir']=0
temp=[]
def judge(name):
    global list2
    for each in list2:
        if each==name:
            return True
        else:
            continue
    list2.append(name)
    dict1[name]=1
        
for each in list1:
    if os.path.isdir(each):
        if judge('dir'):
            dict1['dir']+=1
        else:
            continue
    else:
        temp=os.path.splitext(each)[-1]
        if judge(temp):
            dict1[temp]+=1
        else:
            continue
for each in list2:
     temp=dict1.get(each)
     print("类型为%s的文件有%d个"%(each,temp))