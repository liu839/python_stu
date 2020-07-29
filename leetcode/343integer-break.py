class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        elif n == 3:
            return 2
        res = [i for i in range(n + 1)]
        for i in range(3, n+1):
            for j in range(1, i+1):
                if i + j <= n and res[i] * res[j] > res[i + j]:
                    res[i + j] = res[i] * res[j]
        return res[n]

