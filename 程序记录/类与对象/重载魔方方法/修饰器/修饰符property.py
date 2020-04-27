class Myproperty:
    def __init__(self,fget=None,fset=None,fdel=None):
        self.fget=fget
        self.fset=fset
        self.fdel=fdel

    def __get__(self,instance,owner):
        return self.fget(instance)

    def __set__(self,instance,value):
        self.fset(instance,value)

    def __deletle__(self,instance):
        self.fdel(instance)

class C:
    def __init__(self):
        self._wen=None
        self._hua=None
    def getwen(self):
        return self._wen

    def setwen(self,value):
        self._wen=value
        self._hua=value*1.8+32

    def delwen(self):
        del self._wen
    
    def gethua(self):
        return self._hua

    def sethua(self,value):
        self._hua=value
        self._wen=(value-32)/1.8

    def delhua(self):
        del self._hua
    wen=property(getwen,setwen,delwen)
    hua=property(gethua,sethua,delhua)
c=C()
c.wen=38
print(c.wen,c.hua)