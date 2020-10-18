class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        s = ''
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if int(str(nums[i]) + str(nums[j])) < int(str(nums[j]) + str(nums[i])):
                    nums[i], nums[j] = nums[j], nums[i]
        for x in (nums):
            s += str(x)
        return str(int(s))