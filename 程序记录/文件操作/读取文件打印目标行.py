i=1
dict1={}
def search(dict1,p1,p2):
    temp=True
    while temp:
        print(dict1.get(p1))
        p2=int(p2)
        if p1==p2:
            temp=False
        p1=int(p1)+1


f0=open(r'C:\Users\71037\Desktop\666.txt',encoding='utf-8')
for each in f0:
    dict1[i]=each
    i+=1
f0.close
str1=input("请输入要输出多少行到多少行")
temp=str1.split(':')
if temp.count('')==0:
    p1=temp[0]
    p2=temp[1]
elif temp.index('')==0:
    p1=1
    p2=temp[1]
elif temp.index('')==1:
    p1=temp[0]
    p2=i-1
search(dict1,p1=p1,p2=p2)
