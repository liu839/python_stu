class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        temp = list(sorted(nums))
        for each in nums:
            res.append(temp.index(each))
        return res