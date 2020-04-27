list_max=[]#max或者min式
list_main={}#存储主式
list_0=[]#c塔列
def count(list_max):
    i=0
    for _ in list_max:
        i+=1
    return i
#导入整个表并尝试化为标准形
def makelist():
    j=0
    global list_max
    global list_main
    global list_0
    temp_2=input("请输入以逗号为分割的MAX式")
    list_max=temp_2.split(',')
    i=count(list_max)

    while True:
        temp=input("请依次输入式子,输出end为结束")
        if temp=='end':
            break
        list_main[j]=temp.split(',')#导入主体式子

        temp_j=count(list_main[j])-1 #临时接受每个式子的长度
        if temp_j>i:
            temp_i=temp_j
            for _ in range(temp_i-i+1):
                list_max.append(0)
            i=count(list_main[j])#实时统计量补充0 

        j+=1#准备导入下一个式子
        list_0.append(0)#给 c塔列先扩充数据
    
#输出
def output():
    global list_0
    global list_main
    global list_max
    print("\n最终检验式为:")
    print(list_max)
    list_x=[]  #存储最终解
    range(count(list_main))
    i=0
    for _ in range(count(list_max)-1):
        j=0
        for _ in range(count(list_main)):
            if list_main[j][i]==1.0:
                list_x.append(list_main[j][-1])
                break
            j+=1
        if j==count(list_main):
            list_x.append(0)
        i+=1
    print("解为x\t")
    print(list_x)
    print("最终取值为%f"%(-list_max[-1]))
#判断ci塔是否达到标准
def judge(list_max):
    i=0
    for each in list_max:
        if float(each)<=0:
            i+=1
    if count(list_max)==i:
        return True
    else:
        return False
makelist()
#temp_666=True
temp_999=1

#主体两看一算
while True:
   if judge(list_max):
       break
   i=0
   max1=0
   for each in list_max:
       if float(each)>float(max1):
           max1=each
   j1=list_max.index(max1)        #获取入基变量序号减一的数  列

   for each in list_0:
       if float(list_main[i][j1])<=0:
           i+=1
           continue
       list_0[i]=float(list_main[i][-1])/float(list_main[i][j1])#建立c塔列
       i+=1

   min1=10000
   for each in list_0:
       if float(each)<float(min1) and float(each)>0:
           min1=each                     #寻找出基变量
   j2=list_0.index(min1)    #获取出基变量减一的数 行

   i=0
   temp_guiyuan=float(list_main[j2][j1])#主元值
   for each in list_main[j2]:
       list_main[j2][i]=float(each)/temp_guiyuan  #将主元list_main[j2][j1]归一
       i+=1

   i=0    #翻边运算代表行数
   temp_i=0  #翻边运算列数       由于计算机原因  都各自减一
   for each in range(count(list_main)):
       if i==j2:
           i+=1
           continue
       temp_fanbian=float(list_main[i][j1])
       for each in list_main[i]:
           #if float(list_main[i][temp_i])==0:
           #    temp_i+=1
           #    continue
           list_main[i][temp_i]=(float(list_main[i][temp_i])+temp_fanbian*(-1)*float(list_main[j2][temp_i]))
           temp_i+=1
       temp_i=0
       i+=1            #翻边运算式完成  
       
   temp_i=0
   temp_fanbian=float(list_max[j1])
   for each in range(count(list_max)):
       list_max[temp_i]=(float(list_max[temp_i])+temp_fanbian*-1*float(list_main[j2][temp_i]))
       temp_i+=1      #检验数式矫正完毕
   print("\n\n第%d次计算:"%(temp_999))

   p=0
   for each in list_main:
       print("第%d行式子是\t"%(p+1))
       print(list_main[p])
       p+=1
   print("本轮计算'cta'列为")
   print(list_0)
   print("检验式为:")
   print(list_max)
   temp_999+=1

   #temp_999=input("输入end")
   #if temp_999=='end':
   #    break

output()