
def qiuhe(*params,base=3):
    sum=0
    for each in params:
        sum+=each
    if base==5:
        print(sum)
        return
    print(sum*base)
def flower():
    sum=0
    list1=[]
    for each in range(100,1000):
        for i in str(each):
            sum+=int(i)**3
        if sum==each:
            list1.append(each)
        sum=0
    print(list1)
def findstr(a):
    temp=input("请输入标识符")
    x=len(temp)
    sum=0
    i=-1
    for each in list(a):
        i+=1
        if temp[0]==each:
            if temp==a[i:i+x]:
                sum+=1
    print(sum)
     
qiuhe(1,3,7,9,base=5)
flower()
a="You cannot improve your past, but you can improve your future. Once time is wasted, life is wasted"
findstr(a)
