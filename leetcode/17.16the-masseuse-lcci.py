class Solution:
    def massage(self, nums) -> int:
        if not nums:
            return 0
        nums.insert(0,0)
        nums.insert(0,0)
        for i in range(2,len(nums)):
            nums[i] = max(nums[i-2]+nums[i],nums[i-1])
        return nums[-1]
Solution().massage([1,2,3,1])