import operator
class Student():
    number=0
    name=''
    score_1=0
    score_2=0
list2=[]
i=0
def myinput(list1):
    temp=Student()
    temp.number=int(list1[0])
    temp.name=list1[1]
    temp.score_1=int(list1[2])
    temp.score_2=int(list1[3])
    return temp
def myoutout(student):
    print("学号:0%d\t姓名:%s\t平时分数:%d\t期末分数:%d"%(student.number,student.name,student.score_1,student.score_2))
with open(r"C:\Users\71037\Desktop\student.txt") as f:
    for each in f:
        if each=='\n':
            continue
        list1=each.split(' ')
        list1.remove('\n')
        while '' in list1:
            list1.remove('')
        temp=myinput(list1)
        list2.append(temp)
cmpfun=operator.attrgetter('score_1')   #核心语句operator模块的attrgetor可以转换,使用cmpfun(f)为f.score_1                                        #在这里采用key读取后实际排序为list2[i].score_1
list2.sort(key=cmpfun)
for each in list2:
    myoutout(each)
    