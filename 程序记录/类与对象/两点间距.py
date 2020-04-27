import math as m
class Point():
    def __init__(self,x):
        self.posion=[x[0],x[1]]
class Line():
    def __init__(self,a,b):
        self.length=0.0
        self.point_a=Point(a)
        self.point_b=Point(b)
    def get_len(self):
        self.length=m.sqrt(pow(self.point_a.posion[0]-self.point_b.posion[0],2)+pow(self.point_a.posion[1]-self.point_b.posion[1],2))

l_1=Line((1,3),(2,6))
l_1.get_len()
print(l_1.length)
    