import random
class Bianka():
    def __init__(self):
        self.hp = 100
        self.attack = 19
        self.defense = 10
        self.speed = 15
    
class Aling():
    def __init__(self):
        self.hp = 100
        self.attack = 18
        self.defense = 10
        self.speed = 10
        self.num = 1 
def begin():
    a = Aling()
    b = Bianka()
    while True:
        b.attack += 3

        a.hp -= (b.attack - a.defense)
        if a.num == 1:
            a.hp = 20
            a.num = 0
        else:
            return 1
        
        if a.num == 0:
            if random.randint(1,100) in list(range(1,17)):
                a.hp -= 30
                if a.hp <= 0:
                    return 1
            else:
                if random.randint(0,1) == 1:
                    b.hp -= (233 - b.defense)
                else:
                    b.hp -= (50 - b.defense)
        else :
            b.hp -= (a.attack - b.defense)
        if b.hp <=0:
            return 0

a = {0:0,1:0}
for _ in range(1000000):
    a[begin()] += 1
print("一百万场测试,双子赢了%d盘,呆鹅赢了%d盘\n胜率分别为%.2f,%.2f,数学期望为%.3f,%.3f"%(a[0],a[1],a[0]/1000000,a[1]/1000000,2.8 *(a[0]/1000000),2.1*(a[1]/1000000)))

        