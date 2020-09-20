class Solution:
    def sortString(self, s: str) -> str:
        md = dict()
        for i in s:
            md[i] = md.get(i,0)+1
        _small = sorted(md.keys())
        _big = _small[::-1]
        flag,result = len(s),''
        while flag:
            for i in _small:
                if md[i]>0:
                    result+=i
                    flag-=1
                    md[i]-=1
            for i in _big:
                if md[i]>0:
                    result+=i
                    flag-=1
                    md[i]-=1
        return result