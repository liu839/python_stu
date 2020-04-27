import time as t
class Mytime():
    def __init__(self): 
        self.prompt="未开始计时"
        self.start_1=0
        self.stop_1=0
        self.lasted=[]
    def __str__(self):
        return self.prompt
    __repr__=__str__
    def start(self):
        self.start_1=t.localtime()
        print("计时开始...")
    def stop(self):
        self.stop_1=t.localtime()
        self.__calc()
        print("计时结束..")
    
    def __calc(self):
        self.lasted=[]
        self.prompt="总共运行了"
        for index in range(6):
            self.lasted.append(self.stop_1[index]-self.start_1[index])
            self.prompt+=str(self.lasted[index])
        print(self.prompt)
t1=Mytime()
t1.start()
t1.stop()
t1

