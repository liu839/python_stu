import easygui as eg
msg="请填写以下联系方式\n带*的必填"
title='登录'
file_name=["*用户名","*真实姓名","固定电话","*手机号码","QQ","e mail"]
file_value=[]
file_value=eg.multenterbox(msg,title ,file_name)
dict_1={}
file_i=0
while True:
    errer=0
    for each in file_value:
        if each=='' and file_name[file_value.index(each)][0]=='*':
            errer+=1
            break
    if errer==1:
        eg.msgbox("请完成带有*的填选项")
        file_value=eg.multenterbox(msg,title ,file_name)
        continue
    for each in file_name:
        file_name[file_i]=each.strip('*')
        dict_1[file_name[file_i]]=file_value[file_i]
        file_i+=1
    break
for each in dict_1:
    print("%s:%s"%(each,dict_1[each]))