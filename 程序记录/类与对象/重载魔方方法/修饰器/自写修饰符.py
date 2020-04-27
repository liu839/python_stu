class Mydes:
        def __init__(self,value=None,name=None):
            self.value=value
            self.name=name
        
        def __get__(self,instance,owner):
            print("正在调用变量"+self.name)
            return self.value
        def __set__(self,instance,value):
            print("正在修改变量"+self.name)
            self.value=value
        def __delete__(self,obj):
            print("正在删除变量")
            del self.name
            del self.value

class Test:
	x=Mydes(10,'x')
test = Test()
y = test.x
