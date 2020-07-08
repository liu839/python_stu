
def convert(self, s: str, numRows: int) -> str:
    if len(s)==0 or len(s)==1 or numRows==1:
            return s
        matrix=[[' ']for _ in range(numRows)]
        matrix[0][0]=s[0]
        i=1
        j=0
        num=1
        x=1
        while True:    
            matrix[i][j]=s[num]
            if x==-1 and i!=0:
                j+=1
                for index in range(numRows):
                    matrix[index].append(' ')
            if i+1==numRows:
                x=-x
                j+=1
                for index in range(numRows):
                    matrix[index].append(' ')
            elif i==0:
                x=-x
            i=i+x*1
            num+=1
            if num==len(s):
                break
        str1=''
        for i in range(numRows):
            str1+=''.join(matrix[i])
        str1=str1.replace(" ","")
        return str1

"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2: return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1: flag = -flag
            i += flag
        return "".join(res)

"""