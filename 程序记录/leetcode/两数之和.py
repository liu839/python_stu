class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums=[3,2,4]
        target=6
        hashmap={}
        for i,num in enumerate(nums):
            if hashmap.get(target - num) is not None:
                a=[i,hashmap.get(target - num)]
                print(a)
            hashmap[num] = i 
#采用字典代替哈希表
