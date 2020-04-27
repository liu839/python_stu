try:
    f1=open('我为什么是个文件.txt','w')
    for each in f1:
        print(f1)
    sum=1+'1'
    f1.close()
except (OSError,TypeError) as reason:
    print("文件出错,错误为"+str(reason))