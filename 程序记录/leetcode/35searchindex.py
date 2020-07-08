def solv(list_,target):
    if not list_:
        return
    low=0
    high=len(list_)-1
    while low<=high:
        mid=(low+high)//2
        if list_[mid]>target:
            high=mid-1
        elif list_[mid]<target:
            low=mid+1
        else:
            return mid
        return low

print(solv([1,3,5,6],2))