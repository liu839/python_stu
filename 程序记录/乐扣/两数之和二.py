import time
def solv(numbers,target):
    n = len(numbers)
    if n < 2:
        return
    left = 0
    right = n-1
    while left < right:
        if target == numbers[left] + numbers[right]:
            return [left+1,right+1]
        elif target > numbers[left] + numbers[right]:
            left += 1
        else:
            right -= 1
    return[left,right]

a=time.time()
for _ in range(19999):
    solv([2,7,11,15],9)
b=time.time()
c=b-a
print(c)