x='柳家望666'
m=0
n=0
while True:
    if n==3:
        break
    temp=str(input("请输入密码"))
    for j in temp:
        if j=='*' :
            print("密码中不能含有*,您还有",3-n,"次机会")
            m+=1
            break
    if m==1:
        m=0
        continue
  
    if n!=3:
        if temp==x:
            print("密码正确,正在进入程序")
            break
        else :
            n+=1
            if n==3:
                 break
            print("密码输入,您还有",3-n,"次机会")