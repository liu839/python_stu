
def firstMissingPositive(self, nums: List[int]) -> int:
    nums=set(nums)
    for each in range(1,100000000000000):
        if each not in nums: return each 