class Solution:
    def maxValue(self, grid):
        if not grid:
            return 0 
        lens_x = len(grid[0])
        lens_y = len(grid)
        grid.insert(0, [0 for _ in range(lens_x)])
        for i in range(lens_y+1):
            grid[i].insert(0,0)
        for i in range(1, lens_y+1):
            for j in range(1, lens_x+1):
                grid[i][j] = max(grid[i-1][j], grid[i][j-1]) + grid[i][j]
        return grid[-1][-1]