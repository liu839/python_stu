class Nstr(str):
    def mysum(self,list_string):
        sum_=0
        for each in list_string:
            sum_+=ord(each)
        return sum_
    def __add__(self,other):
        return self.mysum(list(self))+self.mysum(list(other))
    def __sub__(self,other):
        return self.mysum(list(self))-self.mysum(list(other))
    def __mul__(self,other):
        return self.mysum(list(self))*self.mysum(list(other))
    def __truediv__(self,other):
        return  float(self.mysum(list(self)))/float(self.mysum(list(other)))
    def __floordiv__(self,other):
        return  float(self.mysum(list(self)))//float(self.mysum(list(other)))
a = Nstr('FishC')
b = Nstr('love')
print(a+b)
print(a-b)
print(a/b)
print(a//b)
""" 
class Nstr:
    def __init__(self, arg=''):
        if isinstance(arg, str):
            self.total = 0
            for each in arg:
                self.total += ord(each)
        else:
            print("参数错误！")

    def __add__(self, other):
        return self.total + other.total

    def __sub__(self, other):
        return self.total - other.total

    def __mul__(self, other):
        return self.total * other.total

    def __truediv__(self, other):
        return self.total / other.total

    def __floordiv__(self, other):
        return self.total // other.total
 """