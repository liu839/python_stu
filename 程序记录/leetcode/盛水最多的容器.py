def solv(list_):
    area=0
    high=len(list_)-1
    low=0
    max_number=(low,high)
    max_area=0
    while True:
        if low>=high:
            break
        area=min(list_[low],list_[high])*(high-low)
        if area>max_area:
            max_number=(low,high)
            max_area=area
        if list_[low]<list_[high]:
            low+=1
        else:
            high-=1
    return max_number
        
    
print(solv([1,8,6,2,5,4,8,3,7]))