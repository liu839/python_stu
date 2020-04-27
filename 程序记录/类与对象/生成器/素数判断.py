import math as m
def isprime(x):
    for i in range(2,int(m.sqrt(x))+1) :
        if x%i==0:
            return False
    print(x)
    return True

def xun(top):
    for i in range(2,top):
        if isprime(i):
            yield i

sum_0=xun(2000000)
sum_=0
while True:
    try:
        sum_+=next(sum_0)
    except StopIteration:
        break
print(sum_)
