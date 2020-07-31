class Solution:
    def missingNumber(self, nums) -> int:
        right = len(nums)
        left = 0
        mid = (right + left)//2
        while left < right:
            if nums[mid] == mid:
                left = mid+1
                mid = (left+right)//2
                continue
            else:
                right = mid
                mid = (left+right)//2
                continue
        return mid
print(Solution().missingNumber([0,1,3]))
