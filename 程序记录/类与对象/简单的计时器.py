import time as t
class Time():
    def __init__(self):
        self.begin=0
        self.end=0
        self.realtime='计时错误'
    def __str__(self):
       return str(self.realtime)  
    __repr__=__str__
    def start(self):
        self.begin=t.localtime()[5]
    def stop(self):
        self.end=t.localtime()[5]
        self.realtime=self.end-self.begin
    def __add__(self,other):
        return self.realtime+other.realtime
    def __sub__(self,other):
        return self.realtime-other.realtime
def test():
        text = "I love FishC.com!"
        char = 'o'
        if char in text:
                pass
def mytime(text,num):
    t1=Time()
    t1.start()
    for _ in range(num):
        test()
    t1.stop()
    print(t1)
mytime(test,10000)