class Solution:
    def arrangeCoins(self, n: int) -> int:
        res = -1
        val = 1
        while n >= 0:
            res +=1
            n -= val
            val += 1
        return res 