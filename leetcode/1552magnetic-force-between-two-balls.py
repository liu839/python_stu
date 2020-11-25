class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        max_dis = (position[-1] - position[0]) // (m - 1)
        l, r = 1, max_dis + 1
        while r - l > 1:
            mid = (r + l) // 2
            if self.check(mid, position) >= m:
                l = mid
            else:
                r = mid
        return l

    def check(self, dis, positions):
        start, count = positions[0], 1
        for position in positions:
            if position - start >= dis:
                count += 1
                start = position
        return count
        