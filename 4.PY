lens = int(input())
data = [int(i) for i in input().split(" ")]
temp = data[:3]
min_ = min(temp)
max_ = max(temp)
avg = sum(temp)- min_ -max_
sum_=avg
print("%.2f"%(avg))
for i in range(3,lens):
    if data[i] > max_ :
        sum_ += max_
        max_ = data[i]
        print("%.2f"%(sum_/(i-1)))
        continue
    elif data[i] < min_ :
        sum_ += min_
        min_ = data[i]
        print("%.2f"%(sum_/(i-1)))
        continue
    sum_ += data[i]
    print("%.2f"%(sum_/(i-1)))
