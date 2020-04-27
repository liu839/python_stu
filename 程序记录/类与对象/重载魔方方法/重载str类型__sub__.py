class Nstr(str):
    def __sub__(self,other):
        self=list(self)
        while other in self:
            self.remove(other)
        self=''.join(self)
        return self
a=Nstr("I love FishC.com!iiiiii")
b=Nstr('i')
print(a-b)        

""" class Nstr(str):
    def __sub__(self, other):
        return self.replace(other, '')
 """