class Solution:
    def waysToStep(self, n: int) -> int:
        a, b, c = 1,1,2
        k = 2
        if not n :
            return 1
        if n == 1 or n == 2:
            return n 
        while True: 
            a, b, c = b%1000000007, c%1000000007, (a+b+c)%1000000007
            k += 1
            if k == n:
                return c