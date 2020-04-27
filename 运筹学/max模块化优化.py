
def myinput(string):
    temp=[]
    try:
        temp.append(float(string.split('=')[1]))
        temp_tec=string.split('=')[0].split('+')
    except ValueError:
        temp.append(0.0)
        temp_tec=string.split('=')[1].split('+')
    for each in temp_tec:
        while True:
            try:
                temp[int(each.split('x')[1])]=float(each.split('x')[0])
                break
            except IndexError:
                temp.append(0.0)
            except ValueError:
                try:
                    temp[int(each.split('x')[1])]=1.0
                    break
                except IndexError:
                    temp.append(0.0)
    return temp

def myoutput(matrix):
    for each in matrix:
        print(each.tec)

class Hang():
        def __init__(self,string):
            self.tec=[]
            self.tec=myinput(string)



        def __add__(self,other):
            temp=[]
            for i in range(len(self.tec)):
                temp.append(self.tec[i]+other[i])
            return temp
        def __sub__(self,other):
            temp=[]
            for i in range(len(self.tec)):
                temp.append(self.tec[i]-other.tec[i])
            return temp
        def __truediv__(self,other):
            temp=[]
            for i in range(len(self.tec)):
                temp.append(self.tec[i]/other)
            return temp
        def __mul__(self,other):
            temp=[]
            for i in range(len(self.tec)):
                temp.append(self.tec[i]*other)
            return temp      

def standard(matrix):
    max_len=0
                    #长度统一
    for i in range(len(matrix)):
        if max_len<len(matrix[i].tec):
            max_len=len(matrix[i].tec)
    for i in range(len(matrix)):
        for _ in range(max_len-len(matrix[i].tec)):
            matrix[i].tec.append(0.0)
 
 #i为行,j为列,采用的方法为依次遍历每一列,若只有一个非零数则为基向量
    for i in range(len(matrix)):
        for j in range(1,len(matrix[i].tec)):
            count_temp=False
            if matrix[i].tec[j]!=0:
                temp_count=0
                                    #遍历每一列
                for k in range(len(matrix)):
                    if k==i:
                        continue
                    if matrix[k].tec[j]==0:
                        temp_count+=1
                if temp_count==len(matrix)-1:
                                    #确定这一列是基向量,同时基向量归一
                    if matrix[i].tec[j]!=1:
                        matrix[i].tec=matrix[i]/(matrix[i].tec[j]/1)
                        count_temp=True  #确定了基变量
                        break                  
            if count_temp:
                                #最终没有发现基向量
                matrix[i].tec.append(1.0)
                for k in range(len(matrix)):
                                #开始添加松弛变量
                    if k==i:
                        continue
                    matrix[k].tec.append(0.0)
  
def max_danchun():
    
    temp=input("请输入max式")
  
    max_=Hang(temp)      #max列
    #print(max_)            #导入max式

    i=0                     #准备导入主式
    matrix=[]
    while True:
        i+=1
        temp=input("请依次输入行列式,输入end为结束")
        if temp=='end':
            break
        matrix.append(Hang(temp))
    standard(matrix)        #标准化矩阵
                            #开始计算
    while True:
        count=0
        list_0=[]                           #c塔列
        max_temp=0
        for i in range(len(max_.tec)):
            if max_.tec[i]<=0:
                continue                    #定入基变量
            max_temp=max(max_temp,max_.tec[i])
        j1=max_.tec.index(max_temp)             #入基变量下缀 列

        for i in range(len(matrix)):
            list_0.append(0.0)
            if matrix[i].tec[j1]!=0:
                list_0[i]=matrix[i].tec[0]/matrix[i].tec[j1]    #构建c塔列
        temp_i=0


        min_temp=10000.0
        for each in list_0:
            if each<min_temp and each>0:
                min_temp=each
        i1=list_0.index(min_temp)           #行数
        
        matrix[i1].tec=matrix[i1]/(matrix[i1].tec[j1])           #定主元,归一
            
        for  i in range(len(matrix)):
            if i==i1:                                       #翻边运算
                continue
            temp_hang=matrix[i1]*(matrix[i].tec[j1]*(-1))
            matrix[i].tec=matrix[i]+temp_hang

        temp_hang=matrix[i1]*(max_.tec[j1]*(-1))
        max_.tec=max_+temp_hang

        temp_i=0
        for each in max_.tec:
            if each>0:
                break
            temp_i+=1       

        count+=1                                  #输出部分
        print("第%d次计算:"%(count))
        print("本轮ci塔列为")
        print(list_0)
        print('\n')
        myoutput(matrix)

        temp_i=0
        for each in max_.tec[1:]:
            if each>0:
                break
            temp_i+=1
        if temp_i==len(max_.tec)-1:
            print("结束了")
            temp_x=[]
            for i in range(len(matrix)):
                for j in range(len(matrix[0].tec)):
                    if matrix[i].tec[j]==1.0:
                        temp_666=0
                        for k in range(len(matrix)):
                            if k==i:
                                continue
                            if matrix[k].tec[j]==0.0:
                                temp_666+=1
                        temp_999=0
                        if temp_666==len(matrix)-1:
                            while True:
                                try:
                                    temp_x[j-1]=matrix[i].tec[0]
                                    temp_999+=1
                                    break
                                except:
                                    temp_x.append('0')
                        if temp_999:
                            break

            print("解为")
            print(temp_x)            
                        
            break 
        
max_danchun()
