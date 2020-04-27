sum=0#同步注释
for i in range(100,999):
    for j in str(i):
        sum+=int(j)**3
    if sum==i:
        print(i)
    sum=0