def solv(matrix,target):
    if not matrix or not matrix[0]:
            return False
    low=0
    high=len(matrix)-1
    mid_1=(low+high)//2
    while low<=high:
        if matrix[mid_1][0]>target:
            high=mid_1-1
            mid_1=(low+high)//2
        elif matrix[mid_1][0]<target:
            low=mid_1+1
            mid_1=(low+high)//2
        else:
            break
    low=0
    high=len(matrix[mid_1])-1
    while low<=high:
        mid_2=(low+high)//2
        if matrix[mid_1][mid_2]>target:
            high=mid_2-1
        elif matrix[mid_1][mid_2]<target:
            low=mid_2+1
        else:
            return True
    return False

print((solv([[1,3]],3)))