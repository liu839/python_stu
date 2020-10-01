class Solution:
    def rob(self, nums: List[int]) -> int:
        res=[0,0]
        for index,each in enumerate(nums):
            res.append(max(res[index]+nums[index],res[index+1]))
        return res[-1]