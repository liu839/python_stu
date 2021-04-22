n,k = [int(x) for x in input().split(" ")]

start = int(''.join([str(1) for _ in range(n)]))
end = int(''.join([str(6) for _ in range(n)]))
position = start

def judge(num):
    for i in range(len(num)):
        if int(num[i])>6 or int(num[i]) == 0:
            return True
    return False

flag = 1
res = 0
while start <= position <=end:
    if judge(str(position)):
        position += flag
        continue
    if not position%k:
        flag = k
        print(position)
        res += 1
    position += flag

print(res%(10**9+7))