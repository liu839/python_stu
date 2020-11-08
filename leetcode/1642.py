class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        def check(m):
            a = diff[:m+1]
            a.sort()
            if ladders >= len(a) or sum(a[:len(a) - ladders]) <= bricks:
                return True
            return False
        
        n = len(heights)
        diff = [0] * n
        for i in range(1, n):
            diff[i] = max(0, heights[i] - heights[i-1])
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        return l - 1