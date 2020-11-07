class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        res = set()
        for each in nums:
            if each not in res:
                res.add(each)
            else:
                return each