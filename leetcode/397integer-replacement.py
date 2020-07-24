class Solution:
    def __init__(self):
        self.count = 0
    def integerReplacement(self, n: int) -> int:
        while n>1:
            if n==3:
                n-=1
            elif n%4==1:
                n-=1
            elif n%4==3:
                n+=1
            else:
                n/=2
            self.count+=1
        return self.count