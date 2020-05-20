class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.append(float("inf"))
        houses.sort()
        heaters.sort()
        index = 0
        res = 0
        for house in houses:
            while house >= heaters[index]:
                index += 1
            if index > 0:
                cur = min(heaters[index] - house, house - heaters[index - 1])
            else:
                cur = abs(heaters[index] - house)
            res = max(res, cur)
        return res
"""
def findRadius(self, houses: List[int], heaters: List[int]) -> int:
    list_=[]
    for each in houses:
        list_.append(min(list(map(lambda each,x:abs(each-x),[each for _ in range(len(heaters))],heaters))))
    return max(list_)
"""