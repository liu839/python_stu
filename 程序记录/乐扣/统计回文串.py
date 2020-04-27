def xx(s):
    if s=='':
        return s
    def judge(s,i):
        q=len(s)-1
        temp=[s[i]]
        r=0
        l=0
        if i+1>q or i-1<0:
            return ''.join(temp)
        if s[i]==s[i+1]:
            temp.append(s[i+1])
            r=1
        elif s[i]==s[i-1]:
            temp.insert(0,s[i-1])
            l=1
        for j in range(1,1000):
            if i+j+r>q or i-j-l<0:
                return ''.join(temp)
            if s[i-j-l]==s[i+j+r]:
                temp.insert(0,s[i-j])
                temp.append(s[i+j])
    temp=[]
    for i in range(len(s)):
        key=judge(s,i)
        if len(key)>len(temp):
            temp=key
    return temp
print(xx("ccc"))
"""
class Solution():
    def extend(self,i ,index,n,s): 
        while i>=1 and index<n-1:
            if s[i-1]==s[index+1]:
                i-=1
                index+=1
            else:
                break
        return i,index
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        i=0
        max=0
        start=0
        end=0
        while i < n:
            index=i
            while index < n-1 and s[index]==s[index+1] :
                index+=1
            a,b=self.extend(i,index,n,s)
            if b-a+1>max:
                max=b-a+1
                start=a
                end=b
            i=index+1
        return s[start:end+1]
"""