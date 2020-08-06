class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        str_dict={'R': 'D', 'D': 'R'}
        i = 0
        len_senate =len(senate)
        while True:
            if 'D' not in senate:
                return 'Radiant'
            if 'R' not in senate:
                return 'Dire' 
            dele_temp = str_dict[senate[i]]
            if dele_temp in senate[i+1:]:
                senate = senate[ 0 : i+1]+ senate[i+1:].replace(dele_temp,'',1)
            else:
                senate = senate[ 0 : i+1].replace(dele_temp,'',1)+senate[i+1:]
            len_senate -= 1
            i += 1
            if i >= len_senate:
                i = 0

print(Solution().predictPartyVictory('DDRRR'))