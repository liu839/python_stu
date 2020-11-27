class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums :return -1
        dict_used = {}
        lens = len(nums)
        for each in nums:
            try:
                dict_used[each] += 1
                if dict_used[each] == (lens+1)//2:
                    return each
            except KeyError:
                dict_used[each] = 1
                if dict_used[each] == (lens+1)//2:
                    return each
        return -1