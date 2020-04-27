import time as t
class Record:
    def __init__(self, value=None, name=None):
        self.value=value
        self.name=name
        with open(r"C:\Users\71037\Desktop\record.txt",'a') as f1:
            temp=t.asctime()
            f1.write("%s变量于北京时间%s 被初始化 %s=%s\n"%(self.name,temp,self.name,self.value))
    
    def __get__(self,instance,own):
        with open(r"C:\Users\71037\Desktop\record.txt",'a') as f1:
            temp=t.asctime()
            f1.write("%s变量于北京时间%s 被读取 %s=%s\n"%(self.name,temp,self.name,self.value))
        return self.value
    
    def __set__(self,instance,value):
        self.value=value
        with open(r"C:\Users\71037\Desktop\record.txt",'a') as f1:
            temp=t.asctime()
            f1.write("%s变量于北京时间%s 被修改 %s=%s\n"%(self.name,temp,self.name,self.value))
class Test:
    x =Record(10, 'x')
    y =Record(8.8, 'y')

test =Test()
print(test.x)
print(test.y)
test.x = 123
test.x = 1.23
test.y = "I love FishC.com!"