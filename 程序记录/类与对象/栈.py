
class Stack():
    __list_0=[]
    def isEmpty(self):
        if self.__list_0==[]:
            return True
        else:
            return False

    def pop(self):
        return self.__list_0.pop()

    def push(self,x):
        self.__list_0.append()
    
    def top(self):
        return self.__list_0[-1]
    def botton(self):
        return self.__list_0[0]
s=Stack()
s.push(6)

