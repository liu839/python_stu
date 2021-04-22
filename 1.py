res = int(input())
sum_ = 0
def judge(n):
    data = str(n)
    data = list(data)
    return sum([int(x) for x in data])
if res >=900000:
    print("2002")
else:
    for i in range(1,res+1):
        if judge(i) == 9:
            sum_+=1
    print(sum_)
