import time
def getPermutation(self, n: int, k: int) -> str:
    num = [str(i) for i in range(1, n+1)]
    res = ""
    n -= 1
    while n > -1:
        t = math.factorial(n)
        loc = math.ceil(k / t) - 1
        res += num[loc]
        num.pop(loc)
        k %= t
        n -= 1
    return res
a=time.time()
print(x(9,155915))
print(time.time()-a)