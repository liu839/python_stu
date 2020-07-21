class Solution:
    def __init__(self):
        self.visited=dict()

    def numTrees(self, n: int) -> int:

        if n in self.visited:
            return self.visited.get(n)

        if n <= 1:
            return 1
            
        res = 0
        for i in range(1, n + 1):
            res += self.numTrees(i - 1) * self.numTrees(n - i)

        self.visited[n] = res

        return res
print(Solution().numTrees(5))
