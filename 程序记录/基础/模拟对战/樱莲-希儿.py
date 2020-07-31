import random
class Ying():
    def __init__(self):
        self.hp = 100
        self.attack = 20
        self.defense = 9
        self.speed = 18

        self.number = 1
    
class Xier():
    def __init__(self):
        self.hp = 100
        self.attack = 23
        self.defense = 13
        self.speed = 26
        self.color = 0

def begin():
    x = Xier()
    y = Ying()
    while True:
        if x.color == 0:
            x.attack += 10
            x.defense -= 5
            x.color = 1
        else:
            x.attack -= 10
            x.defense +=5
            x.color = 0
            x.hp += random.randint(1,15)
            if x.hp > 100:
                x.hp = 100
        if random.randint(1,10) in range(3):
            if y.hp + 25 > 100:
                y.hp = 100
            else:
                y.hp += 25
        if y.number == 2:
            x.hp -= 25
            y.number = 0
            if x.hp <= 0:
                return 2
        
        y.hp -= (x.attack-y.defense)
        if y.hp <=0 :
            return 1
        x.hp -= (y.attack-x.defense)
        if x.hp <=0:
            return 2
        y.number += 1
a = [0,0]
for i in range(1,1000001):
    a[begin()-1]+=1

print(a)
        

        
