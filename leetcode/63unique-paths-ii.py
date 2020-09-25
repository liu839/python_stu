class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        list_res = [[0 for _ in range(m+1)] for _ in range(n+1)]
        list_res[0][1] = 1
        for i in range(1, n+1):
            for j in range(1, m+1):
                list_res[i][j] = list_res[i-1][j] + list_res [i][j-1]
                if obstacleGrid[i-1][j-1]:
                    list_res[i][j] = 0
        return list_res[-1][-1]