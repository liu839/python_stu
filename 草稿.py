def solv(houses,heaters):
    max_=0
    for each in houses:
        num=0
        while True:
            low=each-num
            high=each+num
            if low in heaters or high in heaters:
                max_=max(num,max_)
                break
            num+=1
    return max_
print(solv([1,2,3],[2]))