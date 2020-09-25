class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        list_res = [[0 for _ in range(m+1)] for _ in range(n+1)]
        list_res[0][1] = 1
        for i in range(1, n+1):
            for j in range(1, m+1):
                list_res[i][j] = list_res[i-1][j] + list_res [i][j-1]
        return list_res[-1][-1]
Solution().uniquePaths(7,3)