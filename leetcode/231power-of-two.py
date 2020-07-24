class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and (not (n & (n-1)))
    #以位运算进行,2的幂必定为1带很多0,减一后进行与运算
    #判断要大于零才能用