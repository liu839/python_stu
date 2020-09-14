class Solution():
    def extend(self,i ,index,n,s): 
        while i >= 1 and index<n-1:
            if s[i-1] == s[index+1]:
                i -= 1
                index += 1
            else:
                break
        return i,index
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        i = 0 
        max = 0
        start = 0
        end = 0
        while i < n:
            index = i
            while index < n-1 and s[index]==s[index+1] :
                index += 1
            a,b=self.extend(i, index, n, s)
            if b-a+1 > max:
                max = b - a + 1
                start = a
                end = b
            i = index + 1
        return s[start:end + 1]