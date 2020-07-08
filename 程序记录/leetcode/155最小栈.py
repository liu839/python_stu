class MinStack:

    def __init__(self,*x):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.min_=[float(inf)]
        map(self.push,x)


    def push(self, x: int) -> None:
        self.stack.append(x)
        if x<=self.min_[-1]:
            self.min_.append(x)
    def pop(self) -> None:
        if self.stack[-1]==self.min_[-1]:
            del self.min_[-1]
        del self.stack[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_[-1]