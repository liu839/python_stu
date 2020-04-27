import easygui as eg
text=''

file_name=eg.fileopenbox(title='打开文件')
with open(file_name,encoding='utf-8') as file_:
    file_list=list(file_)
list2=eg.textbox(msg='%s文件内容如下'%(file_name),title='读取文件',text=file_list)
if file_list!=list2:
    choices=eg.buttonbox(msg='检测到内容发生改变是否保存',title='检测文件',choices=('保存','取消','另存为'))
    if choices=='保存':
        with open(file_name,'w',encoding='utf-8') as file_:
            file_.write(list2)
    elif choices=='另存为':
            file_dir2=eg.filesavebox(default='666.txt')
            with open(file_dir2,'w',encoding='utf-8') as file_:
                file_.write(list2)
