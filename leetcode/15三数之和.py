def x(nums):
    if len(nums)<3:
        return []
    res=[]
    temp=[]
    nums.sort()
    for  i,each in enumerate(nums):
        if each >0:
            break
        for j in range(i+1,len(nums)-1):
            try:
                temp=[nums[i],nums[j],nums[nums.index(0-nums[i]-nums[j])]]
                if temp not in res:
                    res.append(temp[:])
            except:
                pass
    return res
                

print(x([-1,0,1,2,-1,-4]))
    