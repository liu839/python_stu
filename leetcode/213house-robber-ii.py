class Solution:
    def get(self, nums):
        res=[0,0]
        for index,each in enumerate(nums):
            res.append(max(res[index]+nums[index],res[index+1]))
        return res[-1]
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.get(nums[1:]),self.get(nums[:-1]))