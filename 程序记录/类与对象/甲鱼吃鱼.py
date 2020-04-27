import random
class Jiayu:
    __maxseet=2
    posion=[0,0]
    direction=''
    phy=20
    dict_posion={1:'上',2:'下',3:'左',4:'右'}
    def __init__(self):
        self.posion[0]=random.randint(0,10)
        self.posion[1]=random.randint(0,10)

    def check_posion(self,target,temp_feet):
        if target==1:
            if self.posion[1]+temp_feet>10:
                return False
            else:
                self.posion[1]+=temp_feet
                return True

        elif target==2:
            if self.posion[1]-temp_feet<0:
                return False
            else:
                self.posion[1]-temp_feet
                return True

        elif target==3:
            if self.posion[0]-temp_feet<0:
                return False
            else:
                self.posion[0]-=temp_feet
                return True
        elif target==4:
            if self.posion[1]+temp_feet>10:
                return False
            else:
                self.posion[1]+=temp_feet
                return True

    def chect_phy(self):
        if  self.phy==0:
            return False
        elif self.phy>20:
            self.phy=20
            return True
        else:
            return True
        
    def move(self):
        while True:
            temp=random.randint(1,4)#方向
            temp_feet=random.randint(0,self.__maxseet)#步数
            if self.check_posion(temp,temp_feet):
                break
        self.phy-=1
class Fish(Jiayu):
    __maxseer=1

xiaojiayu=Jiayu()
list_fish=[]
for i in range(10):
    temp=Fish()
    list_fish.append(temp)
while True:
    if xiaojiayu.chect_phy():
        print("我还有%d点体力,还能再来"%(xiaojiayu.phy))
    else:
        print('小甲鱼没体力了,啊我死了')
        break
    if list_fish==[]:
        print("鱼被吃完了")
        break
    xiaojiayu.move()
    for i in range(len(list_fish)):
        list_fish[i].move()
    for i in range(10):
        try:
            if xiaojiayu.posion==list_fish[i].posion:
                print("吃了一条鱼,真舒服")
                xiaojiayu.phy+=5
                del list_fish[i]
        except IndexError:
            break


