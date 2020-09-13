class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_={}
        for each in nums:
            try:
                dict_[each] += 1
            except KeyError:
                dict_[each] = 1
        res = list(dict_.keys())
        res.sort(key=lambda x: dict_[x],reverse=True)
        return res[:k]
            