class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=str(x)
        num=(len(y)+1)//2
        for i in range(num):
            if y[i]!=y[-(i+1)]:
                return False
        return True

"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        return x==x[::-1]
"""