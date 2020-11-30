class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        res ={}
        for each in arr:
            try:
                res[each] += 1
            except:
                res[each] = 1
        vals = list(res.values())
        return len(vals) == len(set(vals))
        
