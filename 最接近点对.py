import random
def get_distance(p1,p2):
    res = 0
    for i in range(len(p1)):
        res += p1[i]**2 + p2[i]**2
    return pow(res,1/2)

data = []

def data_sort():
    global data
    lens = len(data[0])
    if lens == 1:
        data.sort()
    elif lens == 2:
        data.sort(key=lambda x:(x[0],x[1]))
    elif lens == 3:
        data.sort(key=lambda x:(x[1],x[2],x[0]))

def get_data(m, n, i, j):
    global data
    for _ in range(m):
        while True:
            temp = [random.randint(i, j) for _ in range(n)]
            if temp not in data:
                data.append(temp)
                break

def solv(i,j):
    mid = (i+j)//2
    left = solv(i,mid) if (mid + 1 - i) > 2 else data[i:mid]
    right = solv(mid,j) if (j - mid) > 2 else data[mid:j]
    
get_data(10,1,-30,30)
data_sort()
print(data)

