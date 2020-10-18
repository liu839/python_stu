class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lens = len(nums)
        index = 0
        while index < lens:
            if nums[index] == 0:
                del nums[index]
                nums.insert(0,0)
            if nums[index] == 2:
                nums.append(2)
                del nums[index]
                lens -= 1
                index -= 1
            index+=1