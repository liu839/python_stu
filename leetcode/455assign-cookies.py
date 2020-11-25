class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        lens = len(g)
        res = 0
        g.sort()
        s.sort()
        for each in s:
            if res == lens:
                return res
            if g[res] <= each:
                res +=1
        return res