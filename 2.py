import math
l = int(input())
des = l**2
a = 1
b = 0
def judge(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        return True
    return False
while True:
    temp = math.sqrt(des - a**2)
    if temp == int(temp):
        if not judge(a,temp,l):
            continue
        print(int(min(temp,a)),int(max(temp,a)))
        break
    a += 1