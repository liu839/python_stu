class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        all_path_sum = []
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j, v):
            can_go_on = False
            for l, c in zip((i - 1, i + 1, i, i),(j, j, j + 1, j -1)):
                if 0 <= l < m and 0 <= c < n and grid[l][c]:
                    cur = grid[l][c]
                    grid[l][c] -= cur
                    dfs(l, c, v + cur)
                    grid[l][c] += cur
                    can_go_on = True
            if not can_go_on:
                all_path_sum.append(v)
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    cur = grid[i][j]
                    grid[i][j] -= cur
                    dfs(i, j, cur)
                    grid[i][j] += cur
        return max(all_path_sum)
