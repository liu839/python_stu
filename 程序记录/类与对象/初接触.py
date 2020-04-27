
class Ticket:
    price=100.0
    def real_prine(self,time,age):
        if time==7:
            self.price*=1.2
        if 0<age<=18:
            self.price/=2
A=Ticket()
B=Ticket()
c=Ticket()
A.real_prine(1,27)
B.real_prine(1,19)
c.real_prine(1,15)
print("三个成年人带一个小孩周一去游乐园价钱为%.2f"%(A.price+B.price+c.price))