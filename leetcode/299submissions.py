class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        b = 0
        guesss = guess[:]
        for each in secret:
            if each in guesss:
                b += 1
                guesss=guesss.replace(each,'',1)
        a = 0
        for chara,charb in zip(secret,guess):
            if chara == charb:
                a += 1
        b -= a
        return str(a)+"A"+str(b)+"B"
print(Solution().getHint("11","10"))