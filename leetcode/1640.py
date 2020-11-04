class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        chars = ''.join([str(each) for each in arr])
        for arr in pieces:
            if ''.join([str(each) for each in arr]) not in chars:
                return False
        return True