class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        res=[]
        nums1 = list(filter(lambda a: a % 2 == 0, A))
        nums2 = list(filter(lambda a: a % 2 == 1, A))
        for a,b in zip(nums1,nums2):
            res.extend([a,b])
        return res