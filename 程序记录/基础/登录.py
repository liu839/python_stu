temp1=True
dict1={}
temp_ip=''
def judge(temp):
    global temp1
    if temp=='N' or temp=='n':
        return new
    if temp=='E' or temp=='e':
        return join
    if temp=='Q' or temp=='q':
        temp1=False
def new():
    global temp_ip
    temp2=True
    while temp2:
        temp=input("请输入账号")
        if temp not in dict1.keys():
            temp_ip=temp
            temp2=False
        else:
            print("账号已存在")
    temp=input("请输入密码")
    dict1.update(temp_ip=temp)
    print("注册成功")
def join():
    temp2=True
    while temp2:
        global dict1
        temp_ip=input("请输入账号")
        temp_mi=input("请输入密码")
        if dict1.get(temp_ip,False)!=False:
            if dict1.get(temp_ip)==temp_mi:
                print("登录成功")
            else:
                print("登录失败")
        else:
            print("登录失败")
        temp=input("是否继续输入y/n")
        if temp=='n' or temp=='N':
            temp2=False

while temp1:
    temp=input("""
|--- 新建用户：N/n ---|
|--- 登录账号：E/e ---|
|--- 推出程序：Q/q ---|
|--- 请输入指令代码：
    """)
    if temp=='n' or temp=='N':
        new()
    if temp=='E' or temp=='e':
        join()
    if temp=='Q' or temp=='q':
        temp1=False