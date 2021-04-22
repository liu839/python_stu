data = [int(each) for each in input().split(' ')]
n,v,m,a = data[0],data[1],data[2],data[3]
res = 0
flag = 0
price = v
for _ in range(n):
    if flag == m:
        price += a
        flag = 0
    res += price
    flag += 1
print(res)