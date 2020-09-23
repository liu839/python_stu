class NumArray:

    def __init__(self, nums: List[int]):
        self.num_sum = [0,]
        for i in range(len(nums)):
            self.num_sum.append(self.num_sum[i]+nums[i])


    def sumRange(self, i: int, j: int) -> int:
        return self.num_sum[j+1] - self.num_sum[i]


