list_min=[]#max或者min式
list_main={}#存储主式
list_0=[]#c塔列
def count(list_min):
    i=0
    for _ in list_min:
        i+=1
    return i
def makelist():
    j=0
    global list_min
    global list_main
    global list_0
    temp_2=input("请输入以逗号为分割的MIN式")
    list_min=temp_2.split(',')
    i=count(list_min)

    while True:
        temp=input("请依次输入式子,输出end为结束")
        if temp=='end':
            break
        list_main[j]=temp.split(',')#导入主体式子

        temp_j=count(list_main[j])-1 #临时接受每个式子的长度
        if temp_j>i:
            temp_i=temp_j
            for _ in range(temp_i-i+1):
                list_min.append(0)
            i=count(list_main[j])#实时统计量补充0 

        j+=1#准备导入下一个式子
        list_0.append(0)#给 c塔列先扩充数据
    print(list_min,list_main[0],i)
def judge(list_min):
    i=0
    for each in list_min:
        if float(each)>=0:
            i+=1
    if count(list_min)==i:
        return True
    else:
        return False

makelist()
temp_999=1
while True:
   if judge(list_min):
       break
   i=0
   min1=0
   for each in list_min:
       if float(each)<float(min1):
           min1=each
   j1=list_min.index(min1)        #获取入基变量序号减一的数  列

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
   temp_fanbian=float(list_min[j1])
   for each in range(count(list_min)):
       list_min[temp_i]=(float(list_min[temp_i])+temp_fanbian*-1*float(list_main[j2][temp_i]))
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
   print(list_min)
   temp_999+=1

   #temp_999=input("输入end")
   #if temp_999=='end':
   #    break

def output():
    global list_0
    global list_main
    global list_min
    print("\n最终检验式为:")
    print(list_min)
    list_x=[]  #存储最终解
    range(count(list_main))
    i=0
    for _ in range(count(list_min)-1):
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
    print("最终取值为%d"%(int(-list_min[-1])))

output()