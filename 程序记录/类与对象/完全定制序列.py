class Countlist():
    def dict_update(self,values):
        temp_dict={}
        for index in range(len(values)):
            temp_dict[index]=values[index]
        return temp_dict

    def __init__(self,*p):
        self.values=[x for x in p]
        self.count={}.fromkeys(range(len(self.values)),0)
    
    def __getitem__(self,key):
        self.count[key]+=1
        return self.values[key]

    def __setitem__(self,key,value):
        self.values[key]=value
        self.count[key]=0

    def __delitem__(self,key):
        del self.values[key]
        temp=list(self.count.values)
        del temp[key]
        self.count=self.dict_update(temp)
        
    def counter(self,key):                    # pylint: disable=E0202
        return self.count[key]
    
    def append(self,value):
        self.values.append(value)
        self.count[len(self.count)]=0

    def pop(self):
        self.values.pop()
        del self.count[len(self.count)-1]

    def remove(self,value):
        index=self.values.index(value)
        self.values.remove(value)
        del self.count[index]
        self.count=self.dict_update(list(self.values))

    def insert(self,index,value):
        self.values.insert(index,value)
        temp=list(self.count.values())
        temp.insert(index,0)
        self.count=self.dict_update(temp)

    def clear(self):
        del self.values
        del self.count
    
    def reverse(self):
        self.values.reverse()
        temp=list(self.count.values())
        temp.reverse()
        self.count=self.dict_update(temp)
        


c1=Countlist(1,3,5,7,9)
c2=Countlist(2,4,6,8,10)
print(c1[3]+c2[2])
c1.insert(3,5)
print(c1[3])
c1.pop()
c2.reverse()
c1.remove(3)
c1.clear()
c2.clear()
