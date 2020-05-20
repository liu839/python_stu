def solv(nums):
    x=set(nums)
    l=len(x)
    nums[:l]=sorted(list(x))
    return l
