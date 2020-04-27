class Nstr(str):
    def __rshift__(self,other):
        self=list(self)
        list_temp=self[:]
        for i in range(len(self)):
            list_temp[(i+other)%(len(self))]=self[i]
        print(''.join(list_temp))

    def __lshift__(self,other):
        self=list(self)
        list_temp=self[:]
        for i in range(len(self)):
            list_temp[(len(self)+i-other)%(len(self))]=self[i]
        print(''.join(list_temp))
a=Nstr('i love fishc')
a<<1
 """ 
class Nstr(str):
    def __lshift__(self, other):
        return self[other:] + self[:other]

    def __rshift__(self, other):
        return self[-other:] + self[:-other]
 """