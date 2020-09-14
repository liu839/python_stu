import easygui as eg
import os
eg.msgbox("检录代码量程序")
dir_name=eg.diropenbox()
file_houzhui=['.py','.html','.asp','.cpp','.c','.js','.css','.php', 'vue']
dict_={}
list_dict=[0,0,0,0,0,0,0,0]                       #依次存储一个
list_i=0
def count(dir_name):
    global file_houzhui
    global dict_

    os.chdir(dir_name)
    list_dir=os.listdir()
    for each in list_dir:
        if each == "node_modules":
            continue
        if os.path.isdir(each):
            dir_name2=(dir_name+'\\'+each)  #获取实际名称
            count(dir_name2)                #进入递归  使用的为DFS算法
            os.chdir(dir_name)              #函数递归返回后,更改os模块操作区域为上层文件操作域

        if os.path.isfile(each):
            if os.path.splitext(each)[1] in file_houzhui:
                list_dict[file_houzhui.index(os.path.splitext(each)[1])]+=1 #处理文件个数   
                file_name=dir_name+'\\'+each                                
                file_hou=os.path.splitext(each)[1]                          #获取后缀名
                with open(file_name,'rb') as file_:
                    for each in file_:
                        try:
                            dict_[file_hou]+=1
                        except KeyError:
                            dict_[file_hou]=1
count(dir_name)
list_result=[]
sum_1=0
for each in dict_:
    sum_1+=dict_[each]
    each=each[1:]+'有'+str(list_dict[file_houzhui.index(each)])+'个文件,'+each[1:]+'有'+str(dict_[each])+'行代码'+'\n'
    list_result.append(each)
text='你的目标是十万行代码还差'+str(100000-sum_1)+'行,已完成'+str(float(sum_1)/1000)+'%,加油啊.'
eg.textbox(msg=text,title='统计代码量',text=list_result)