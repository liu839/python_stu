class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        for i in range(len(nums)+1):
            self.make([],nums,i)
        return self.res
    def make(self, char_list, characters, combinationLength):
        if not combinationLength:
            self.res.append(char_list)
            return
        for index,each in enumerate(characters):
            self.make(char_list+[each], characters[index+1:], combinationLength-1)