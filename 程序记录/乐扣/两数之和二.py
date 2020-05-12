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