"""
class Solution(): 
    def validPalindrome(self, s): 
        l = len(s) 
        h = l//2
        if s[:h] == s[-1:-1-h:-1]: return True 

        for i in range(h): 
            if s[i] != s[~i]: 
                j = len(s) - 1 - i 
                h = (j-i)//2
                return s[i:i+h] == s[j-1:j-h-1:-1] or s[i+1:i+h+1] == s[j:j-h:-1]
"""

def x(s):
        if not s:
            return None
        low_=0
        high_=len(s)-1
        i=0
        def solv(s,low,high):
            nonlocal low_,high_,i
            while low<high:
                if s[low]!=s[high]:
                    if i==0:
                        low_=low
                        high_=high
                        i+=1
                    return False
                low+=1
                high-=1
            return True
        if solv(s,low_,high_):
            return True
        else:
            return solv(s,low_+1,high_) or solv(s,low_,high_-1)
            
print(x("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))