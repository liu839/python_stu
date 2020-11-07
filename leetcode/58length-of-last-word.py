class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        if not s:
            return 0
        i = -1
        res = 0
        try:
            while s[i]!=' ':
                res += 1
                i -= 1
        except:
            pass
        return res