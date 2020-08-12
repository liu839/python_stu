class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = nums[:n]
        for index,each in enumerate(nums[n:]):
            res.insert(index*2+1,each)
        return res

