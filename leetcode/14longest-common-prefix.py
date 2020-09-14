class Solution:
    def longestCommonPrefix(self, strs) -> str:
        lens = len(strs)
        if lens == 0 or ("" in strs):
            return ""
        if lens == 1:
            return strs[0]
        i = 0
        index = 0
        while True:
            try:
                if index+1<lens and strs[index][i] != strs[index+1][i]:
                    return strs[0][:i]
                else:
                    index += 1
                if index == lens:
                    i += 1
                    index = 0
            except IndexError:
                return strs[0][:i]