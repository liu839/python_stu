class Solution:
    def readBinaryWatch(self, num) :
        ans=[]
        for h in range(0,12):
            for m in range(0,60):
                if list(bin(h))[2:].count('1')+list(bin(m))[2:].count('1')==num :

                    if len(str(m))==1:
                        sm='0'+str(m)
                    else:
                        sm=str(m)
                    ans.append(str(h)+':'+sm)
        return ans
